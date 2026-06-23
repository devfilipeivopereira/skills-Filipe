#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import json
import mimetypes
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


NOTION_VERSION = "2026-03-11"
API_BASE = "https://api.notion.com/v1"


def normalize_name(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    ascii_only = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return "".join(ch.lower() for ch in ascii_only if ch.isalnum())


class NotionClient:
    def __init__(self, token: str) -> None:
        self.token = token

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        query: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        url = f"{API_BASE}{path}"
        if query:
            url = f"{url}?{urllib.parse.urlencode(query)}"

        body = None
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": NOTION_VERSION,
        }
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            details = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Notion API error {exc.code} on {method} {path}: {details}") from exc

    def retrieve_database(self, database_id: str) -> dict[str, Any]:
        return self.request("GET", f"/databases/{database_id}")

    def retrieve_data_source(self, data_source_id: str) -> dict[str, Any]:
        return self.request("GET", f"/data_sources/{data_source_id}")

    def query_data_source(self, data_source_id: str, start_cursor: str | None = None) -> dict[str, Any]:
        payload: dict[str, Any] = {"page_size": 100}
        if start_cursor:
            payload["start_cursor"] = start_cursor
        return self.request("POST", f"/data_sources/{data_source_id}/query", payload=payload)

    def retrieve_page_property(self, page_id: str, property_id: str, start_cursor: str | None = None) -> dict[str, Any]:
        query = {"start_cursor": start_cursor} if start_cursor else None
        encoded_property_id = urllib.parse.quote(property_id, safe="")
        return self.request("GET", f"/pages/{page_id}/properties/{encoded_property_id}", query=query)

    def update_page_properties(self, page_id: str, properties: dict[str, Any]) -> dict[str, Any]:
        return self.request("PATCH", f"/pages/{page_id}", payload={"properties": properties})

    def send_file_upload(self, upload_url: str, filename: str, content: bytes, content_type: str) -> dict[str, Any]:
        body, multipart_content_type = build_multipart_form_data("file", filename, content, content_type)
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": multipart_content_type,
        }
        req = urllib.request.Request(upload_url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            details = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Notion upload error {exc.code} on POST {upload_url}: {details}") from exc


def read_text_file(path: str) -> str:
    return decode_text_bytes(Path(path).read_bytes())


def read_bytes_file(path: str) -> bytes:
    return Path(path).read_bytes()


def count_words(value: str) -> int:
    return len(re.findall(r"\b\w+\b", value, flags=re.UNICODE))


def normalize_text_for_comparison(value: str) -> str:
    lowered = value.lower()
    normalized = unicodedata.normalize("NFKD", lowered)
    ascii_only = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    ascii_only = re.sub(r"\s+", " ", ascii_only)
    return ascii_only.strip()


def split_paragraphs(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"\n\s*\n", value) if part.strip()]


def split_sentences(value: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", value.strip())
    return [sentence.strip() for sentence in sentences if sentence.strip()]


def summarize_text(value: str, head_chars: int = 1200, tail_chars: int = 600) -> dict[str, str]:
    text = value.strip()
    if len(text) <= head_chars + tail_chars + 40:
        return {
            "head": text,
            "tail": "",
        }
    return {
        "head": text[:head_chars].strip(),
        "tail": text[-tail_chars:].strip(),
    }


SERMON_START_PATTERNS = (
    r"\babra sua b[ií]blia\b",
    r"\bvamos ler\b",
    r"\ba mensagem de hoje\b",
    r"\bo texto diz\b",
    r"\bquero compartilhar\b",
    r"\bquero falar\b",
    r"\ba palavra de deus\b",
    r"\best[aá] em\b",
    r"\bcap[ií]tulo\b",
    r"\bvers[ií]culo\b",
)


def find_sermon_start_excerpt(value: str, excerpt_chars: int = 1200) -> dict[str, Any]:
    text = value.strip()
    lowered = text.lower()
    for pattern in SERMON_START_PATTERNS:
        match = re.search(pattern, lowered, flags=re.IGNORECASE)
        if not match:
            continue
        start = match.start()
        excerpt = text[start : start + excerpt_chars].strip()
        return {
            "found": True,
            "char_index": start,
            "excerpt": excerpt,
        }
    return {
        "found": False,
        "char_index": 0,
        "excerpt": text[:excerpt_chars].strip(),
    }


def analyze_text_quality(value: str) -> dict[str, Any]:
    paragraphs = split_paragraphs(value)
    comparable_paragraphs = [
        normalize_text_for_comparison(paragraph)
        for paragraph in paragraphs
        if count_words(paragraph) >= 40
    ]
    paragraph_counts = collections.Counter(comparable_paragraphs)
    duplicated_paragraphs = [
        {"text": text[:160], "count": count}
        for text, count in paragraph_counts.items()
        if count > 1
    ]

    sentences = split_sentences(value)
    comparable_sentences = [
        normalize_text_for_comparison(sentence)
        for sentence in sentences
        if count_words(sentence) >= 12
    ]
    sentence_counts = collections.Counter(comparable_sentences)
    repeated_sentences = [
        {"text": text[:160], "count": count}
        for text, count in sentence_counts.items()
        if count > 1
    ]

    repeated_sentence_instances = sum(count - 1 for count in sentence_counts.values() if count > 1)
    repeated_sentence_ratio = (
        repeated_sentence_instances / len(comparable_sentences) if comparable_sentences else 0.0
    )

    return {
        "word_count": count_words(value),
        "paragraph_count": len(paragraphs),
        "long_paragraph_count": len(comparable_paragraphs),
        "duplicated_paragraphs": duplicated_paragraphs,
        "sentence_count": len(sentences),
        "long_sentence_count": len(comparable_sentences),
        "repeated_sentences": repeated_sentences,
        "repeated_sentence_ratio": repeated_sentence_ratio,
    }


def validate_ebook_text(
    value: str,
    min_words: int,
    max_repeated_sentence_ratio: float,
    allow_repeated_paragraphs: bool,
) -> dict[str, Any]:
    analysis = analyze_text_quality(value)
    errors: list[str] = []

    if analysis["word_count"] < min_words:
        errors.append(
            f"Ebook com {analysis['word_count']} palavras. Minimo exigido: {min_words}."
        )

    if not allow_repeated_paragraphs and analysis["duplicated_paragraphs"]:
        errors.append(
            f"Foram detectados {len(analysis['duplicated_paragraphs'])} paragrafos longos repetidos."
        )

    if analysis["repeated_sentence_ratio"] > max_repeated_sentence_ratio:
        errors.append(
            "Taxa de frases longas repetidas acima do limite: "
            f"{analysis['repeated_sentence_ratio']:.2%} > {max_repeated_sentence_ratio:.2%}."
        )

    analysis["errors"] = errors
    analysis["valid"] = not errors
    return analysis


def chunk_text(value: str, size: int = 1800) -> list[str]:
    chunks: list[str] = []
    text = value.strip()
    while text:
        if len(text) <= size:
            chunks.append(text)
            break
        split_at = text.rfind("\n", 0, size)
        if split_at < size // 2:
            split_at = text.rfind(" ", 0, size)
        if split_at < size // 2:
            split_at = size
        chunks.append(text[:split_at].strip())
        text = text[split_at:].strip()
    return [chunk for chunk in chunks if chunk]


def rich_text_payload(value: str) -> list[dict[str, Any]]:
    return [
        {
            "type": "text",
            "text": {"content": chunk},
        }
        for chunk in chunk_text(value)
    ]


def decode_text_bytes(content: bytes) -> str:
    for encoding in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            continue
    return content.decode("utf-8", errors="replace")


def sanitize_filename(value: str, default_stem: str) -> str:
    stem = value.strip() or default_stem
    stem = re.sub(r"[\\\\/:*?\"<>|]+", "-", stem)
    stem = re.sub(r"\s+", " ", stem).strip(" .")
    return stem or default_stem


def normalize_page_id(value: str) -> str:
    return (value or "").replace("-", "").strip().lower()


def build_multipart_form_data(field_name: str, filename: str, content: bytes, content_type: str) -> tuple[bytes, str]:
    boundary = "----CodexNotionBoundary7MA4YWxkTrZu0gW"
    body = bytearray()
    body.extend(f"--{boundary}\r\n".encode("utf-8"))
    body.extend(
        f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'.encode("utf-8")
    )
    body.extend(f"Content-Type: {content_type}\r\n\r\n".encode("utf-8"))
    body.extend(content)
    body.extend(f"\r\n--{boundary}--\r\n".encode("utf-8"))
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def extract_rich_text_from_property_item(item: dict[str, Any]) -> str:
    item_type = item.get("type")
    if item_type in {"rich_text", "title"}:
        blocks = item.get(item_type, [])
        return "".join(part.get("plain_text", "") for part in blocks)
    if item_type == "property_item":
        nested_type = item.get("property_item", {}).get("type")
        nested_value = item.get("property_item", {}).get(nested_type, {})
        if nested_type == "rich_text":
            return nested_value.get("plain_text", "")
    return ""


def extract_files_from_property_value(value: dict[str, Any]) -> list[dict[str, str]]:
    if value.get("type") != "files":
        return []
    extracted: list[dict[str, str]] = []
    for file_obj in value.get("files", []):
        file_type = file_obj.get("type")
        if file_type == "file":
            url = file_obj.get("file", {}).get("url")
        elif file_type == "external":
            url = file_obj.get("external", {}).get("url")
        elif file_type == "file_upload":
            url = ""
        else:
            url = ""
        extracted.append(
            {
                "name": file_obj.get("name", ""),
                "type": file_type or "",
                "url": url or "",
            }
        )
    return extracted


def extract_plain_text_from_property_value(value: dict[str, Any]) -> str:
    prop_type = value.get("type")
    if prop_type in {"rich_text", "title"}:
        return "".join(part.get("plain_text", "") for part in value.get(prop_type, []))
    if prop_type == "files":
        return "\n".join(file_obj["name"] for file_obj in extract_files_from_property_value(value) if file_obj["name"])
    if prop_type == "number":
        number = value.get("number")
        return "" if number is None else str(number)
    if prop_type == "url":
        return value.get("url") or ""
    if prop_type == "email":
        return value.get("email") or ""
    if prop_type == "phone_number":
        return value.get("phone_number") or ""
    if prop_type == "checkbox":
        return "true" if value.get("checkbox") else "false"
    if prop_type == "select":
        option = value.get("select")
        return option.get("name", "") if option else ""
    if prop_type == "status":
        status = value.get("status")
        return status.get("name", "") if status else ""
    if prop_type == "date":
        date = value.get("date")
        return "" if not date else date.get("start", "")
    if prop_type == "formula":
        formula = value.get("formula", {})
        formula_type = formula.get("type")
        formula_value = formula.get(formula_type)
        return "" if formula_value is None else str(formula_value)
    return ""


def build_local_text_index(local_source_dir: str | None) -> dict[str, Path]:
    if not local_source_dir:
        return {}
    base_dir = Path(local_source_dir)
    if not base_dir.exists():
        raise RuntimeError(f"Diretorio local de corrigidos nao encontrado: {base_dir}")

    index: dict[str, Path] = {}
    for path in base_dir.rglob("*"):
        if not path.is_file():
            continue
        index[normalize_name(path.name)] = path
        index[normalize_name(path.stem)] = path
    return index


def find_local_source_file(
    local_index: dict[str, Path],
    source_file_names: list[str],
    page_title: str,
    allow_title_fallback: bool,
) -> Path | None:
    for source_file_name in source_file_names:
        normalized_candidates = (
            normalize_name(source_file_name),
            normalize_name(Path(source_file_name).stem),
        )
        for candidate in normalized_candidates:
            if candidate in local_index:
                return local_index[candidate]

    if allow_title_fallback:
        title_key = normalize_name(page_title)
        if title_key and title_key in local_index:
            return local_index[title_key]
    return None


def build_candidate_entry(
    page: dict[str, Any],
    page_title: str,
    source_name: str,
    target_name: str,
    source_type: str,
    target_type: str,
    source_files: list[dict[str, str]],
    target_files: list[dict[str, str]],
    local_index: dict[str, Path],
    allow_title_fallback: bool,
) -> dict[str, Any]:
    source_file_names = [file_obj["name"] for file_obj in source_files if file_obj.get("name")]
    local_source_file = find_local_source_file(
        local_index,
        source_file_names,
        page_title,
        allow_title_fallback=allow_title_fallback,
    )
    local_source_word_count: int | None = None
    local_source_char_count: int | None = None
    if local_source_file:
        local_source_text = read_text_file(str(local_source_file)).strip()
        local_source_word_count = count_words(local_source_text)
        local_source_char_count = len(local_source_text)
    return {
        "page_id": page["id"],
        "title": page_title,
        "source_property": source_name,
        "target_property": target_name,
        "source_type": source_type,
        "target_type": target_type,
        "corrigido_files": source_file_names,
        "has_local_source": bool(local_source_file),
        "local_source_path": str(local_source_file) if local_source_file else "",
        "local_source_word_count": local_source_word_count,
        "local_source_char_count": local_source_char_count,
        "target_is_filled": bool(target_files),
    }


def candidate_matches_min_local_source_words(candidate: dict[str, Any], min_local_source_words: int | None) -> bool:
    if not min_local_source_words:
        return True
    local_source_word_count = candidate.get("local_source_word_count")
    if local_source_word_count is None:
        return True
    return local_source_word_count >= min_local_source_words


def sort_candidates_for_writing(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        candidates,
        key=lambda candidate: (
            candidate.get("local_source_word_count") is not None,
            candidate.get("local_source_word_count") or 0,
            candidate.get("title", ""),
        ),
        reverse=True,
    )


def candidate_pool_limit(max_pages: int | None) -> int | None:
    if not max_pages:
        return None
    return max(max_pages * 5, 25)


def resolve_data_source_id(client: NotionClient, database_id: str | None, data_source_id: str | None) -> str:
    if data_source_id:
        return data_source_id
    if not database_id:
        raise SystemExit("Forneca --database-id ou --data-source-id.")

    database = client.retrieve_database(database_id)
    data_sources = database.get("data_sources", [])
    if not data_sources:
        raise RuntimeError(f"Nenhum data source encontrado para o database {database_id}.")
    return data_sources[0]["id"]


def find_property_name(properties: dict[str, Any], wanted_name: str) -> str:
    target = normalize_name(wanted_name)
    for prop_name in properties:
        if normalize_name(prop_name) == target:
            return prop_name
    raise RuntimeError(
        f"Coluna '{wanted_name}' nao encontrada. Colunas disponiveis: {', '.join(sorted(properties))}"
    )


def retrieve_full_property_text(client: NotionClient, page_id: str, property_id: str) -> str:
    chunks: list[str] = []
    cursor: str | None = None
    while True:
        response = client.retrieve_page_property(page_id, property_id, start_cursor=cursor)
        if response.get("object") == "list":
            for item in response.get("results", []):
                chunks.append(extract_rich_text_from_property_item(item))
            if not response.get("has_more"):
                break
            cursor = response.get("next_cursor")
            continue

        chunks.append(extract_rich_text_from_property_item(response))
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return "".join(chunks).strip()


def download_text_from_files(files: list[dict[str, str]]) -> tuple[str, list[str]]:
    texts: list[str] = []
    names: list[str] = []
    for file_obj in files:
        url = file_obj.get("url", "")
        name = file_obj.get("name", "")
        if not url:
            continue
        with urllib.request.urlopen(url) as response:
            content = response.read()
        texts.append(decode_text_bytes(content).strip())
        names.append(name)
    return "\n\n".join(part for part in texts if part), names


def upload_file_to_notion(client: NotionClient, filename: str, content: bytes, content_type: str) -> str:
    upload = client.request(
        "POST",
        "/file_uploads",
        payload={"mode": "single_part", "filename": filename, "content_type": content_type},
    )
    file_upload_id = upload["id"]
    upload_url = upload["upload_url"]
    send_result = client.send_file_upload(upload_url, filename, content, content_type)
    if send_result.get("status") != "uploaded":
        raise RuntimeError(f"Upload do arquivo '{filename}' nao foi concluido. Resposta: {send_result}")
    return file_upload_id


def inspect_command(args: argparse.Namespace) -> int:
    client = NotionClient(args.token)
    data_source_id = resolve_data_source_id(client, args.database_id, args.data_source_id)
    data_source = client.retrieve_data_source(data_source_id)
    properties = data_source.get("properties", {})
    result = {
        "data_source_id": data_source_id,
        "title": "".join(part.get("plain_text", "") for part in data_source.get("title", [])),
        "properties": {
            name: {"id": value.get("id"), "type": value.get("type")}
            for name, value in sorted(properties.items())
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def list_command(args: argparse.Namespace) -> int:
    client = NotionClient(args.token)
    data_source_id = resolve_data_source_id(client, args.database_id, args.data_source_id)
    data_source = client.retrieve_data_source(data_source_id)
    properties = data_source.get("properties", {})

    source_name = find_property_name(properties, args.source_property)
    target_name = find_property_name(properties, args.target_property)
    title_name = next(
        (name for name, value in properties.items() if value.get("type") == "title"),
        None,
    )
    if not title_name:
        raise RuntimeError("Nenhuma coluna de titulo encontrada no data source.")

    source_type = properties[source_name]["type"]
    target_type = properties[target_name]["type"]
    local_index = build_local_text_index(args.local_source_dir)
    pool_limit = candidate_pool_limit(args.max_pages)
    cursor: str | None = None
    pages: list[dict[str, Any]] = []

    while True:
        response = client.query_data_source(data_source_id, start_cursor=cursor)
        for page in response.get("results", []):
            normalized_requested_page_id = normalize_page_id(args.page_id) if args.page_id else ""
            if normalized_requested_page_id and normalize_page_id(page["id"]) != normalized_requested_page_id:
                continue

            page_properties = page.get("properties", {})
            page_title = extract_plain_text_from_property_value(page_properties.get(title_name, {})).strip()
            if args.title_contains and args.title_contains.lower() not in page_title.lower():
                continue

            source_value = page_properties.get(source_name, {})
            target_value = page_properties.get(target_name, {})
            source_preview = extract_plain_text_from_property_value(source_value).strip()
            target_preview = extract_plain_text_from_property_value(target_value).strip()
            source_files = extract_files_from_property_value(source_value)
            target_files = extract_files_from_property_value(target_value)

            if source_type == "files" and not source_files:
                continue
            if source_type != "files" and not source_preview:
                continue
            if target_type == "files" and target_files and not args.include_filled_target:
                continue
            if target_type != "files" and target_preview and not args.include_filled_target:
                continue

            candidate_entry = build_candidate_entry(
                page=page,
                page_title=page_title,
                source_name=source_name,
                target_name=target_name,
                source_type=source_type,
                target_type=target_type,
                source_files=source_files,
                target_files=target_files,
                local_index=local_index,
                allow_title_fallback=args.allow_title_fallback,
            )
            if not candidate_matches_min_local_source_words(candidate_entry, args.min_local_source_words):
                continue
            pages.append(candidate_entry)
            if pool_limit and len(pages) >= pool_limit:
                break
            if normalized_requested_page_id:
                break

        if pool_limit and len(pages) >= pool_limit:
            break
        if normalized_requested_page_id and pages:
            break
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    pages = sort_candidates_for_writing(pages)
    if args.max_pages:
        pages = pages[: args.max_pages]

    payload = {
        "data_source_id": data_source_id,
        "source_property": source_name,
        "target_property": target_name,
        "pages": pages,
    }

    if args.out:
        Path(args.out).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def pull_command(args: argparse.Namespace) -> int:
    if (
        not args.summary_only
        and not args.page_id
        and not args.allow_multi_page_text
        and ((args.max_pages is None) or (args.max_pages > 1))
    ):
        raise RuntimeError(
            "Para evitar JSONs enormes, use 'list' para descoberta, "
            "'pull --page-id' para uma pagina especifica, "
            "'pull --summary-only' para resumo, ou confirme explicitamente com '--allow-multi-page-text'."
        )

    client = NotionClient(args.token)
    data_source_id = resolve_data_source_id(client, args.database_id, args.data_source_id)
    data_source = client.retrieve_data_source(data_source_id)
    properties = data_source.get("properties", {})

    source_name = find_property_name(properties, args.source_property)
    target_name = find_property_name(properties, args.target_property)
    title_name = next(
        (name for name, value in properties.items() if value.get("type") == "title"),
        None,
    )
    if not title_name:
        raise RuntimeError("Nenhuma coluna de titulo encontrada no data source.")

    source_type = properties[source_name]["type"]
    target_type = properties[target_name]["type"]
    source_id = properties[source_name]["id"]
    local_index = build_local_text_index(args.local_source_dir)
    cursor: str | None = None
    pages: list[dict[str, Any]] = []

    while True:
        response = client.query_data_source(data_source_id, start_cursor=cursor)
        for page in response.get("results", []):
            normalized_requested_page_id = normalize_page_id(args.page_id) if args.page_id else ""
            if normalized_requested_page_id and normalize_page_id(page["id"]) != normalized_requested_page_id:
                continue

            page_properties = page.get("properties", {})
            page_title = extract_plain_text_from_property_value(page_properties.get(title_name, {})).strip()
            if args.title_contains and args.title_contains.lower() not in page_title.lower():
                continue

            source_value = page_properties.get(source_name, {})
            target_value = page_properties.get(target_name, {})
            source_preview = extract_plain_text_from_property_value(source_value).strip()
            target_preview = extract_plain_text_from_property_value(target_value).strip()
            source_files = extract_files_from_property_value(source_value)
            target_files = extract_files_from_property_value(target_value)

            if source_type == "files" and not source_files:
                continue
            if source_type != "files" and not source_preview:
                continue
            if target_type == "files" and target_files and not args.include_filled_target:
                continue
            if target_type != "files" and target_preview and not args.include_filled_target:
                continue

            source_file_names: list[str] = []
            local_source_file: Path | None = None
            if source_type == "files":
                source_file_names = [file_obj["name"] for file_obj in source_files if file_obj.get("name")]
                local_source_file = find_local_source_file(
                    local_index,
                    source_file_names,
                    page_title,
                    allow_title_fallback=args.allow_title_fallback,
                )
                if local_source_file:
                    full_source = read_text_file(str(local_source_file)).strip()
                else:
                    full_source, source_file_names = download_text_from_files(source_files)
            else:
                full_source = retrieve_full_property_text(client, page["id"], source_id)
                if not full_source:
                    full_source = source_preview
            if not full_source:
                continue

            pages.append(
                build_candidate_entry(
                    page=page,
                    page_title=page_title,
                    source_name=source_name,
                    target_name=target_name,
                    source_type=source_type,
                    target_type=target_type,
                    source_files=source_files,
                    target_files=target_files,
                    local_index=local_index,
                    allow_title_fallback=args.allow_title_fallback,
                )
            )
            if args.summary_only:
                pages[-1]["corrigido_summary"] = summarize_text(full_source)
                pages[-1]["sermon_start_hint"] = find_sermon_start_excerpt(full_source)
            else:
                pages[-1]["corrigido_text"] = full_source
            pages[-1]["used_local_source"] = bool(source_type == "files" and local_source_file)

            if args.max_pages and len(pages) >= args.max_pages:
                break
            if normalized_requested_page_id:
                break

        if args.max_pages and len(pages) >= args.max_pages:
            break
        if normalized_requested_page_id and pages:
            break
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    payload = {
        "data_source_id": data_source_id,
        "source_property": source_name,
        "target_property": target_name,
        "pages": pages,
    }

    if args.out:
        Path(args.out).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def push_command(args: argparse.Namespace) -> int:
    client = NotionClient(args.token)
    data_source_id = resolve_data_source_id(client, args.database_id, args.data_source_id)
    data_source = client.retrieve_data_source(data_source_id)
    properties = data_source.get("properties", {})
    target_name = find_property_name(properties, args.target_property)
    target_type = properties[target_name]["type"]

    if args.input_file:
        ebook_text = read_text_file(args.input_file).strip()
        ebook_bytes = read_bytes_file(args.input_file)
        filename = args.filename or Path(args.input_file).name
    else:
        ebook_text = sys.stdin.read().strip()
        filename = args.filename or f"ebook-{args.page_id[:8]}.md"
        ebook_bytes = ebook_text.encode("utf-8")

    if not ebook_text:
        raise RuntimeError("Nenhum conteudo de ebook foi fornecido.")

    validation = validate_ebook_text(
        ebook_text,
        min_words=args.min_words,
        max_repeated_sentence_ratio=args.max_repeated_sentence_ratio,
        allow_repeated_paragraphs=args.allow_repeated_paragraphs,
    )
    if not args.skip_validation and not validation["valid"]:
        raise RuntimeError(
            "Validacao do ebook falhou: "
            + " ".join(validation["errors"])
        )

    if target_type == "rich_text":
        properties_payload = {
            target_name: {
                "rich_text": rich_text_payload(ebook_text),
            }
        }
    elif target_type == "files":
        safe_filename = sanitize_filename(Path(filename).stem, f"ebook-{args.page_id[:8]}")
        extension = Path(filename).suffix or ".md"
        final_filename = f"{safe_filename}{extension}"
        content_type = mimetypes.guess_type(final_filename)[0] or "text/markdown"
        file_upload_id = upload_file_to_notion(client, final_filename, ebook_bytes, content_type)
        properties_payload = {
            target_name: {
                "files": [
                    {
                        "name": final_filename,
                        "type": "file_upload",
                        "file_upload": {"id": file_upload_id},
                    }
                ]
            }
        }
    else:
        raise RuntimeError(
            f"A coluna '{target_name}' precisa ser do tipo rich_text ou files para receber o ebook. Tipo atual: {target_type}"
        )

    client.update_page_properties(args.page_id, properties_payload)

    response_payload = {
        "page_id": args.page_id,
        "target_property": target_name,
        "target_type": target_type,
        "status": "updated",
        "characters": len(ebook_text),
        "word_count": validation["word_count"],
        "repeated_sentence_ratio": round(validation["repeated_sentence_ratio"], 6),
        "duplicated_paragraphs": len(validation["duplicated_paragraphs"]),
    }
    if target_type == "files":
        response_payload["filename"] = final_filename
    print(json.dumps(response_payload, ensure_ascii=False, indent=2))
    return 0


def validate_command(args: argparse.Namespace) -> int:
    if not args.input_file:
        raise RuntimeError("Forneca --input-file para validar um ebook local.")
    ebook_text = read_text_file(args.input_file).strip()
    validation = validate_ebook_text(
        ebook_text,
        min_words=args.min_words,
        max_repeated_sentence_ratio=args.max_repeated_sentence_ratio,
        allow_repeated_paragraphs=args.allow_repeated_paragraphs,
    )
    print(json.dumps(validation, ensure_ascii=False, indent=2))
    return 0 if validation["valid"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ler e atualizar ebooks em um banco do Notion.")
    parser.add_argument("--token", default=os.environ.get("NOTION_TOKEN"), help="Token do Notion.")
    parser.add_argument(
        "--database-id",
        default=os.environ.get("NOTION_DATABASE_ID"),
        help="Database ID do Notion. O primeiro data source sera usado.",
    )
    parser.add_argument(
        "--data-source-id",
        default=os.environ.get("NOTION_DATA_SOURCE_ID"),
        help="Data source ID do Notion. Se informado, tem prioridade sobre --database-id.",
    )
    parser.add_argument(
        "--source-property",
        default="corrigido",
        help="Nome da coluna de origem que contem o texto corrigido.",
    )
    parser.add_argument(
        "--target-property",
        default="ebook",
        help="Nome da coluna de destino que recebera o ebook.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect", help="Mostra o esquema do data source.")
    inspect_parser.set_defaults(func=inspect_command)

    list_parser = subparsers.add_parser("list", help="Lista paginas candidatas sem baixar o texto completo.")
    list_parser.add_argument("--out", help="Arquivo JSON de saida.")
    list_parser.add_argument("--include-filled-target", action="store_true", help="Inclui paginas que ja tem ebook.")
    list_parser.add_argument("--max-pages", type=int, help="Limita a quantidade de paginas listadas.")
    list_parser.add_argument(
        "--min-local-source-words",
        type=int,
        help="Ignora candidatas cujo arquivo local corrigido tenha menos do que esta contagem de palavras.",
    )
    list_parser.add_argument("--page-id", help="Filtra uma unica pagina pelo ID.")
    list_parser.add_argument("--title-contains", help="Filtra paginas por trecho do titulo.")
    list_parser.add_argument(
        "--local-source-dir",
        help="Diretorio local com arquivos corrigidos .txt para verificar cache local.",
    )
    list_parser.add_argument(
        "--allow-title-fallback",
        action="store_true",
        help="Permite procurar arquivo local por titulo quando o nome do arquivo nao bate exatamente.",
    )
    list_parser.set_defaults(func=list_command)

    pull_parser = subparsers.add_parser("pull", help="Exporta paginas com corrigido preenchido.")
    pull_parser.add_argument("--out", help="Arquivo JSON de saida.")
    pull_parser.add_argument("--include-filled-target", action="store_true", help="Inclui paginas que ja tem ebook.")
    pull_parser.add_argument("--max-pages", type=int, help="Limita a quantidade de paginas exportadas.")
    pull_parser.add_argument("--page-id", help="Filtra uma unica pagina pelo ID.")
    pull_parser.add_argument("--title-contains", help="Filtra paginas por trecho do titulo.")
    pull_parser.add_argument(
        "--local-source-dir",
        help="Diretorio local com arquivos corrigidos .txt para reutilizar e evitar novo download do Notion.",
    )
    pull_parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Retorna apenas um resumo do corrigido_text, sem exportar o texto completo.",
    )
    pull_parser.add_argument(
        "--allow-multi-page-text",
        action="store_true",
        help="Permite exportar texto completo de varias paginas; use com cuidado.",
    )
    pull_parser.add_argument(
        "--allow-title-fallback",
        action="store_true",
        help="Permite procurar arquivo local por titulo quando o nome do arquivo nao bate exatamente.",
    )
    pull_parser.set_defaults(func=pull_command)

    push_parser = subparsers.add_parser("push", help="Atualiza a coluna ebook de uma pagina.")
    push_parser.add_argument("--page-id", required=True, help="ID da pagina a atualizar.")
    push_parser.add_argument("--input-file", help="Arquivo com o ebook. Se omitido, le do stdin.")
    push_parser.add_argument("--filename", help="Nome do arquivo ao enviar para uma coluna files.")
    push_parser.add_argument("--min-words", type=int, default=10000, help="Minimo de palavras exigido antes do upload.")
    push_parser.add_argument(
        "--max-repeated-sentence-ratio",
        type=float,
        default=0.02,
        help="Percentual maximo tolerado de frases longas repetidas.",
    )
    push_parser.add_argument(
        "--allow-repeated-paragraphs",
        action="store_true",
        help="Permite paragrafos longos duplicados; use apenas se houver motivo justificado.",
    )
    push_parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Ignora validacao de contagem e repeticao antes do upload.",
    )
    push_parser.set_defaults(func=push_command)

    validate_parser = subparsers.add_parser("validate", help="Valida um ebook local antes do upload.")
    validate_parser.add_argument("--input-file", required=True, help="Arquivo local do ebook.")
    validate_parser.add_argument("--min-words", type=int, default=10000, help="Minimo de palavras exigido.")
    validate_parser.add_argument(
        "--max-repeated-sentence-ratio",
        type=float,
        default=0.02,
        help="Percentual maximo tolerado de frases longas repetidas.",
    )
    validate_parser.add_argument(
        "--allow-repeated-paragraphs",
        action="store_true",
        help="Permite paragrafos longos duplicados; use apenas se houver motivo justificado.",
    )
    validate_parser.set_defaults(func=validate_command)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command in {"inspect", "pull", "push"} and not args.token:
        raise SystemExit("Defina NOTION_TOKEN ou use --token.")
    if args.command in {"inspect", "pull", "push"} and not args.database_id and not args.data_source_id:
        raise SystemExit("Defina NOTION_DATABASE_ID/NOTION_DATA_SOURCE_ID ou use --database-id/--data-source-id.")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
