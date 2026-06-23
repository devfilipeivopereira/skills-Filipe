#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
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


class NotionClient:
    def __init__(self, token: str) -> None:
        self.token = token

    def request(
        self,
        method: str,
        path: str,
        payload: dict[str, Any] | None = None,
        query: dict[str, str] | None = None,
        raw_url: str | None = None,
        body_override: bytes | None = None,
        content_type_override: str | None = None,
    ) -> dict[str, Any]:
        url = raw_url or f"{API_BASE}{path}"
        if query:
            url = f"{url}?{urllib.parse.urlencode(query)}"

        body = body_override
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": NOTION_VERSION,
        }
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif content_type_override:
            headers["Content-Type"] = content_type_override

        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            details = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Notion API error {exc.code} on {method} {url}: {details}") from exc

    def retrieve_database(self, database_id: str) -> dict[str, Any]:
        return self.request("GET", f"/databases/{database_id}")

    def retrieve_data_source(self, data_source_id: str) -> dict[str, Any]:
        return self.request("GET", f"/data_sources/{data_source_id}")

    def query_data_source(self, data_source_id: str, start_cursor: str | None = None) -> dict[str, Any]:
        payload: dict[str, Any] = {"page_size": 100}
        if start_cursor:
            payload["start_cursor"] = start_cursor
        return self.request("POST", f"/data_sources/{data_source_id}/query", payload=payload)

    def update_page_properties(self, page_id: str, properties: dict[str, Any]) -> dict[str, Any]:
        return self.request("PATCH", f"/pages/{page_id}", payload={"properties": properties})

    def upload_file(self, filename: str, content: bytes, content_type: str) -> str:
        upload = self.request(
            "POST",
            "/file_uploads",
            payload={"mode": "single_part", "filename": filename, "content_type": content_type},
        )
        file_upload_id = upload["id"]
        body, body_type = build_multipart_form_data("file", filename, content, content_type)
        result = self.request(
            "POST",
            "",
            raw_url=upload["upload_url"],
            body_override=body,
            content_type_override=body_type,
        )
        if result.get("status") != "uploaded":
            raise RuntimeError(f"Upload incompleto para '{filename}': {result}")
        return file_upload_id


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


def extract_files_from_property_value(value: dict[str, Any]) -> list[dict[str, str]]:
    if value.get("type") != "files":
        return []
    extracted: list[dict[str, str]] = []
    for file_obj in value.get("files", []):
        file_type = file_obj.get("type")
        if file_type == "file":
            url = file_obj.get("file", {}).get("url", "")
        elif file_type == "external":
            url = file_obj.get("external", {}).get("url", "")
        else:
            url = ""
        extracted.append({"name": file_obj.get("name", ""), "url": url, "type": file_type or ""})
    return extracted


def extract_plain_text_from_property_value(value: dict[str, Any]) -> str:
    if value.get("type") == "files":
        return "\n".join(file_obj["name"] for file_obj in extract_files_from_property_value(value) if file_obj["name"])
    prop_type = value.get("type")
    if prop_type in {"title", "rich_text"}:
        return "".join(part.get("plain_text", "") for part in value.get(prop_type, []))
    return ""


def download_text_from_files(files: list[dict[str, str]]) -> tuple[str, list[str]]:
    texts: list[str] = []
    names: list[str] = []
    for file_obj in files:
        if not file_obj.get("url"):
            continue
        with urllib.request.urlopen(file_obj["url"]) as response:
            content = response.read()
        texts.append(decode_text_bytes(content).strip())
        names.append(file_obj.get("name", ""))
    return "\n\n".join(part for part in texts if part), names


def inspect_command(args: argparse.Namespace) -> int:
    client = NotionClient(args.token)
    data_source_id = resolve_data_source_id(client, args.database_id, args.data_source_id)
    data_source = client.retrieve_data_source(data_source_id)
    result = {
        "data_source_id": data_source_id,
        "title": "".join(part.get("plain_text", "") for part in data_source.get("title", [])),
        "properties": {
            name: {"id": value.get("id"), "type": value.get("type")}
            for name, value in sorted(data_source.get("properties", {}).items())
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def pull_command(args: argparse.Namespace) -> int:
    client = NotionClient(args.token)
    data_source_id = resolve_data_source_id(client, args.database_id, args.data_source_id)
    data_source = client.retrieve_data_source(data_source_id)
    properties = data_source.get("properties", {})

    source_name = find_property_name(properties, args.source_property)
    target_name = find_property_name(properties, args.target_property)
    title_name = next((name for name, value in properties.items() if value.get("type") == "title"), None)
    if not title_name:
        raise RuntimeError("Nenhuma coluna de titulo encontrada no data source.")

    if properties[source_name]["type"] != "files" or properties[target_name]["type"] != "files":
        raise RuntimeError("Esta skill espera que Transcrições e Corrigido sejam colunas do tipo files.")

    pages: list[dict[str, Any]] = []
    cursor: str | None = None
    while True:
        response = client.query_data_source(data_source_id, start_cursor=cursor)
        for page in response.get("results", []):
            page_properties = page.get("properties", {})
            source_files = extract_files_from_property_value(page_properties.get(source_name, {}))
            target_files = extract_files_from_property_value(page_properties.get(target_name, {}))
            if not source_files:
                continue
            if target_files and not args.include_filled_target:
                continue

            source_text, source_names = download_text_from_files(source_files)
            if not source_text:
                continue

            pages.append(
                {
                    "page_id": page["id"],
                    "title": extract_plain_text_from_property_value(page_properties.get(title_name, {})).strip(),
                    "source_property": source_name,
                    "target_property": target_name,
                    "transcricoes_files": source_names,
                    "transcricoes_text": source_text,
                }
            )
            if args.max_pages and len(pages) >= args.max_pages:
                break

        if args.max_pages and len(pages) >= args.max_pages:
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


def build_target_filename(input_name: str, fallback_title: str, keep_name: bool) -> str:
    if keep_name and input_name:
        stem = Path(input_name).stem
    else:
        stem = fallback_title
    safe_stem = sanitize_filename(stem, "corrigido")
    if not safe_stem.startswith("_"):
        safe_stem = f"_{safe_stem}"
    return f"{safe_stem}.txt"


def push_command(args: argparse.Namespace) -> int:
    client = NotionClient(args.token)
    data_source_id = resolve_data_source_id(client, args.database_id, args.data_source_id)
    data_source = client.retrieve_data_source(data_source_id)
    properties = data_source.get("properties", {})
    target_name = find_property_name(properties, args.target_property)
    if properties[target_name]["type"] != "files":
        raise RuntimeError(f"A coluna '{target_name}' precisa ser do tipo files.")

    corrected_text = Path(args.input_file).read_text(encoding="utf-8").strip()
    if not corrected_text:
        raise RuntimeError("Arquivo corrigido vazio.")

    file_name = build_target_filename(args.original_name or "", args.fallback_title or "", args.keep_original_name)
    file_upload_id = client.upload_file(file_name, corrected_text.encode("utf-8"), "text/plain")
    client.update_page_properties(
        args.page_id,
        {
            target_name: {
                "files": [
                    {
                        "name": file_name,
                        "type": "file_upload",
                        "file_upload": {"id": file_upload_id},
                    }
                ]
            }
        },
    )
    print(
        json.dumps(
            {
                "page_id": args.page_id,
                "target_property": target_name,
                "status": "updated",
                "filename": file_name,
                "characters": len(corrected_text),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ler Transcrições e gravar Corrigido em um banco do Notion.")
    parser.add_argument("--token", default=os.environ.get("NOTION_TOKEN"), help="Token do Notion.")
    parser.add_argument("--database-id", default=os.environ.get("NOTION_DATABASE_ID"), help="Database ID do Notion.")
    parser.add_argument("--data-source-id", default=os.environ.get("NOTION_DATA_SOURCE_ID"), help="Data source ID.")
    parser.add_argument("--source-property", default="Transcrições", help="Coluna de origem.")
    parser.add_argument("--target-property", default="Corrigido", help="Coluna de destino.")

    subparsers = parser.add_subparsers(dest="command", required=True)
    inspect_parser = subparsers.add_parser("inspect", help="Mostra o schema.")
    inspect_parser.set_defaults(func=inspect_command)

    pull_parser = subparsers.add_parser("pull", help="Exporta paginas com transcrição pendente.")
    pull_parser.add_argument("--out", help="Arquivo JSON de saida.")
    pull_parser.add_argument("--include-filled-target", action="store_true", help="Inclui paginas ja corrigidas.")
    pull_parser.add_argument("--max-pages", type=int, help="Limita paginas.")
    pull_parser.set_defaults(func=pull_command)

    push_parser = subparsers.add_parser("push", help="Envia o corrigido para o Notion.")
    push_parser.add_argument("--page-id", required=True, help="ID da pagina.")
    push_parser.add_argument("--input-file", required=True, help="Arquivo txt corrigido.")
    push_parser.add_argument("--original-name", help="Nome original do arquivo de transcrição.")
    push_parser.add_argument("--fallback-title", help="Titulo da pagina para fallback no nome.")
    push_parser.add_argument("--keep-original-name", action="store_true", help="Mantem base do nome original.")
    push_parser.set_defaults(func=push_command)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not args.token:
        raise SystemExit("Defina NOTION_TOKEN ou use --token.")
    if not args.database_id and not args.data_source_id:
        raise SystemExit("Defina NOTION_DATABASE_ID/NOTION_DATA_SOURCE_ID ou use --database-id/--data-source-id.")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
