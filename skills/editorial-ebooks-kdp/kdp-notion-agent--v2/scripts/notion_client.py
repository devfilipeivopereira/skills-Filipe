from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import requests


NOTION_API_VERSION = "2022-06-28"
NOTION_FILE_API_VERSION = "2026-03-11"
TRANSCRIPTION_CUTOFF_DATE = date(2024, 10, 1)
DEFAULT_CORRECTED_PROPERTY = "Corrigido"
DEFAULT_TRANSCRIPTION_PROPERTY = "Transcrições"
MOJIBAKE_MARKERS = ("Ã", "Â", "â€", "â€™", "â€œ", "â€", "ðŸ", "�")


def _decode_bytes_best_effort(data: bytes) -> str:
    if data.startswith(b"\xff\xfe") or data.startswith(b"\xfe\xff"):
        return data.decode("utf-16", errors="strict")
    for encoding in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return data.decode(encoding, errors="strict")
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def _looks_mojibake(text: str) -> bool:
    return any(marker in text for marker in MOJIBAKE_MARKERS)


def _repair_mojibake_once(text: str) -> str:
    for source_encoding in ("latin-1", "cp1252"):
        try:
            candidate = text.encode(source_encoding).decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
        if _mojibake_score(candidate) < _mojibake_score(text):
            return candidate
    return text


def _mojibake_score(text: str) -> int:
    return sum(text.count(marker) for marker in MOJIBAKE_MARKERS)


def _normalize_notion_text(text: str) -> str:
    normalized = text.replace("\ufeff", "")
    for _ in range(2):
        if not _looks_mojibake(normalized):
            break
        repaired = _repair_mojibake_once(normalized)
        if repaired == normalized:
            break
        normalized = repaired
    return normalized


@dataclass
class NotionConfig:
    token: str
    database_id: str

    @classmethod
    def from_env(cls) -> "NotionConfig":
        token = os.environ.get("NOTION_TOKEN")
        database_id = os.environ.get("NOTION_DATABASE_ID")
        if token and database_id:
            return cls(token=token, database_id=database_id)

        config_path = Path(__file__).resolve().parents[1] / "config.local.json"
        if config_path.exists():
            data = json.loads(config_path.read_text(encoding="utf-8-sig"))
            token = token or data.get("notion_token")
            database_id = database_id or data.get("notion_database_id")

        if not token or not database_id:
            raise RuntimeError(
                "Defina NOTION_TOKEN e NOTION_DATABASE_ID no ambiente ou preencha config.local.json na skill."
            )
        return cls(token=token, database_id=database_id)


class NotionClient:
    def __init__(self, config: NotionConfig):
        self.config = config

    @property
    def headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.config.token}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_API_VERSION,
        }

    @property
    def file_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.config.token}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_FILE_API_VERSION,
        }

    def get_database(self) -> dict[str, Any]:
        resp = requests.get(
            f"https://api.notion.com/v1/databases/{self.config.database_id}",
            headers=self.headers,
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    def ensure_status_property(self) -> None:
        database = self.get_database()
        properties = database.get("properties", {})
        if "Status" in properties:
            return
        payload = {
            "properties": {
                "Status": {
                    "select": {
                        "options": [
                            {"name": "Executando", "color": "yellow"},
                            {"name": "Pronto", "color": "green"},
                        ]
                    }
                }
            }
        }
        response = requests.patch(
            f"https://api.notion.com/v1/databases/{self.config.database_id}",
            headers=self.headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()

    def query_database(self, *, start_cursor: str | None = None, page_size: int = 100) -> dict[str, Any]:
        payload: dict[str, Any] = {"page_size": page_size}
        if start_cursor:
            payload["start_cursor"] = start_cursor
        resp = requests.post(
            f"https://api.notion.com/v1/databases/{self.config.database_id}/query",
            headers=self.headers,
            json=payload,
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    def list_database_pages(self) -> list[dict[str, Any]]:
        pages: list[dict[str, Any]] = []
        cursor: str | None = None
        while True:
            payload = self.query_database(start_cursor=cursor)
            pages.extend(payload.get("results", []))
            if not payload.get("has_more"):
                return pages
            cursor = payload.get("next_cursor")

    def get_page(self, page_id: str) -> dict[str, Any]:
        resp = requests.get(
            f"https://api.notion.com/v1/pages/{page_id}",
            headers=self.headers,
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    def extract_title(self, page: dict[str, Any]) -> str:
        for prop in page.get("properties", {}).values():
            if prop.get("type") == "title":
                text = "".join(part.get("plain_text", "") for part in prop.get("title", []))
                if text.strip():
                    return text.strip()
        return "E-book"

    def get_file_property(self, page: dict[str, Any], property_name: str) -> list[dict[str, Any]]:
        return page.get("properties", {}).get(property_name, {}).get("files", [])

    def has_ebook_output(self, page: dict[str, Any]) -> bool:
        return self.page_has_file_property(page, "Ebook_HTML")

    def extract_status_name(self, page: dict[str, Any], property_name: str = "Status") -> str | None:
        prop = page.get("properties", {}).get(property_name)
        if not prop:
            return None
        prop_type = prop.get("type")
        if prop_type == "status":
            status = prop.get("status") or {}
            return status.get("name")
        if prop_type == "select":
            selected = prop.get("select") or {}
            return selected.get("name")
        if prop_type == "rich_text":
            return "".join(piece.get("plain_text", "") for piece in prop.get("rich_text", [])).strip() or None
        return None

    def page_matches_title(self, page: dict[str, Any], title_query: str | None) -> bool:
        if not title_query:
            return True
        return title_query.casefold() in self.extract_title(page).casefold()

    def is_page_eligible_for_next_ebook(self, page: dict[str, Any]) -> tuple[bool, str]:
        title = self.extract_title(page)
        if self.has_ebook_output(page):
            return False, f"{title}: já possui Ebook_HTML."
        status = (self.extract_status_name(page) or "").strip()
        if status.casefold() in {"executando", "pronto", "pronto kdp", "rascunho revisável", "rascunho revisavel"}:
            return False, f"{title}: status atual '{status}' indica item já processado."
        try:
            source_property = self.select_editorial_source(page, requested_property="AUTO")
        except ValueError as exc:
            return False, f"{title}: {exc}"
        return True, f"{title}: elegível com fonte {source_property}."

    def page_has_file_property(self, page: dict[str, Any], property_name: str) -> bool:
        return bool(self.get_file_property(page, property_name))

    def extract_page_date(self, page: dict[str, Any]) -> date | None:
        properties = page.get("properties", {})
        preferred_names = ("DATA", "Data")
        for name in preferred_names:
            prop = properties.get(name)
            parsed = self._extract_date_property(prop)
            if parsed:
                return parsed
        for prop in properties.values():
            parsed = self._extract_date_property(prop)
            if parsed:
                return parsed
        return None

    def select_editorial_source(
        self,
        page: dict[str, Any],
        *,
        requested_property: str = "AUTO",
        cutoff_date: date = TRANSCRIPTION_CUTOFF_DATE,
    ) -> str:
        if requested_property and requested_property.upper() != "AUTO":
            if not self.page_has_file_property(page, requested_property):
                raise ValueError(f"A página não possui arquivo em {requested_property}.")
            return requested_property

        if self.page_has_file_property(page, DEFAULT_CORRECTED_PROPERTY):
            return DEFAULT_CORRECTED_PROPERTY

        page_date = self.extract_page_date(page)
        if self.page_has_file_property(page, DEFAULT_TRANSCRIPTION_PROPERTY):
            if page_date and page_date < cutoff_date:
                return DEFAULT_TRANSCRIPTION_PROPERTY
            raise ValueError(
                "A página não possui arquivo em Corrigido. "
                "Transcrições só pode ser usada como fonte automática para sermões anteriores a 2024-10-01."
            )

        raise ValueError("A página não possui arquivo utilizável em Corrigido ou Transcrições.")

    def download_first_file(self, page: dict[str, Any], property_name: str) -> tuple[str, str]:
        files = self.get_file_property(page, property_name)
        if not files:
            raise ValueError(f"A página não possui arquivo em {property_name}.")
        file_obj = files[0]
        file_info = file_obj.get("file") or {}
        url = file_info.get("url")
        if not url:
            raise ValueError(f"O primeiro arquivo de {property_name} não possui URL temporária.")
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        return file_obj.get("name", "origem.txt"), _decode_bytes_best_effort(response.content)

    def inspect_schema(self) -> dict[str, str]:
        database = self.get_database()
        return {
            name: definition.get("type", "unknown")
            for name, definition in database.get("properties", {}).items()
        }

    def create_file_upload(self, local_path: Path) -> str:
        payload = {
            "filename": local_path.name,
            "mode": "single_part",
            "content_type": self._guess_content_type(local_path),
        }
        created = requests.post(
            "https://api.notion.com/v1/file_uploads",
            headers=self.file_headers,
            json=payload,
            timeout=60,
        )
        created.raise_for_status()
        data = created.json()
        upload_url = data["upload_url"]
        file_id = data["id"]
        with local_path.open("rb") as handle:
            uploaded = requests.post(
                upload_url,
                headers={
                    "Authorization": f"Bearer {self.config.token}",
                    "Notion-Version": NOTION_FILE_API_VERSION,
                },
                files={"file": (local_path.name, handle, payload["content_type"])},
                timeout=180,
            )
        if uploaded.status_code not in {200, 204}:
            raise RuntimeError(uploaded.text)
        return file_id

    def upload_file_property(self, page_id: str, property_name: str, local_path: Path) -> None:
        file_id = self.create_file_upload(local_path)
        self.update_page_properties(
            page_id,
            {
                property_name: {
                    "files": [
                        {
                            "name": local_path.name,
                            "type": "file_upload",
                            "file_upload": {"id": file_id},
                        }
                    ]
                }
            },
        )

    def build_property_payload(self, page: dict[str, Any], updates: dict[str, Any]) -> dict[str, Any]:
        payload: dict[str, Any] = {}
        schema = page.get("properties", {})
        for prop_name, value in updates.items():
            if prop_name not in schema or value is None:
                continue
            prop_type = schema[prop_name]["type"]
            normalized_text = _normalize_notion_text(str(value))
            if prop_type == "rich_text":
                payload[prop_name] = {"rich_text": self._rich_text(normalized_text)}
            elif prop_type == "number":
                payload[prop_name] = {"number": value}
            elif prop_type == "date":
                payload[prop_name] = {"date": {"start": value}}
            elif prop_type == "status":
                payload[prop_name] = {"status": {"name": normalized_text}}
            elif prop_type == "select":
                payload[prop_name] = {"select": {"name": normalized_text}}
            elif prop_type == "title":
                payload[prop_name] = {"title": self._rich_text(normalized_text)}
            else:
                payload[prop_name] = {"rich_text": self._rich_text(normalized_text)}
        return payload

    def update_page_properties(self, page_id: str, properties: dict[str, Any]) -> dict[str, Any]:
        response = requests.patch(
            f"https://api.notion.com/v1/pages/{page_id}",
            headers=self.file_headers,
            json={"properties": properties},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()

    def set_page_workflow_status(self, page_id: str, status_name: str) -> None:
        self.ensure_status_property()
        page = self.get_page(page_id)
        property_payload = self.build_property_payload(page, {"Status": status_name})
        if not property_payload:
            raise RuntimeError("Não foi possível atualizar a coluna Status no Notion.")
        self.update_page_properties(page_id, property_payload)

    def write_manifest(
        self,
        workspace: Path,
        page: dict[str, Any],
        source_property: str,
        source_file_name: str,
        execution_profile: str = "premium",
        run_id: str | None = None,
        optional_artifacts: list[str] | None = None,
    ) -> Path:
        page_date = self.extract_page_date(page)
        manifest = {
            "page_id": page["id"],
            "title": self.extract_title(page),
            "source_property": source_property,
            "source_file_name": source_file_name,
            "source_page_date": page_date.isoformat() if page_date else None,
            "database_id": self.config.database_id,
            "created_at": datetime.now().isoformat(),
            "execution_profile": execution_profile,
            "run_id": run_id or "",
            "optional_artifacts": optional_artifacts if optional_artifacts is not None else ["bonus", "cta", "landing", "metadata"],
            "files": {
                "raw_transcription": "01_raw_transcricao.txt",
                "corrected_transcription": "02_corrigido.txt",
                "sermon_summary": "03_resumo_sermao.md",
                "ebook_blueprint": "04_blueprint_ebook.md",
                "editorial_report": "05_relatorio_editorial.md",
                "ebook_markdown": "06_ebook.md",
                "landing_html": "07_landing.html",
                "bonus_markdown": "08_bonus.md",
                "kdp_metadata": "09_metadata_kdp.json",
                "cta_report": "10_relatorio_cta.json",
                "cta_subagent": "11_cta_subagent.json",
                "cta_subagent_brief": "12_cta_subagent_brief.md",
                "stage_strategy": "13_stage_strategy.md",
                "model_routing": "14_model_routing.json",
                "ebook_docx": "output/ebook.docx",
                "bonus_docx": "output/bonus.docx",
            },
        }
        manifest_path = workspace / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        return manifest_path

    @staticmethod
    def _extract_date_property(prop: dict[str, Any] | None) -> date | None:
        if not prop or prop.get("type") != "date":
            return None
        start = (prop.get("date") or {}).get("start")
        if not start:
            return None
        try:
            return date.fromisoformat(start[:10])
        except ValueError:
            return None

    @staticmethod
    def _guess_content_type(path: Path) -> str:
        suffix = path.suffix.lower()
        if suffix == ".docx":
            return "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        if suffix == ".txt":
            return "text/plain"
        if suffix == ".html":
            return "text/html"
        if suffix == ".json":
            return "application/json"
        if suffix == ".md":
            return "text/markdown"
        return "application/octet-stream"

    def list_block_children(self, block_id: str, *, start_cursor: str | None = None) -> dict[str, Any]:
        params: dict[str, Any] = {"page_size": 100}
        if start_cursor:
            params["start_cursor"] = start_cursor
        resp = requests.get(
            f"https://api.notion.com/v1/blocks/{block_id}/children",
            headers=self.headers,
            params=params,
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    def archive_block(self, block_id: str) -> None:
        resp = requests.patch(
            f"https://api.notion.com/v1/blocks/{block_id}",
            headers=self.headers,
            json={"archived": True},
            timeout=30,
        )
        resp.raise_for_status()

    def clear_page_content(self, page_id: str) -> int:
        """Archive all direct child blocks of a page. Returns count of archived blocks."""
        cursor: str | None = None
        archived = 0
        while True:
            result = self.list_block_children(page_id, start_cursor=cursor)
            for block in result.get("results", []):
                try:
                    self.archive_block(block["id"])
                    archived += 1
                except Exception:
                    pass
            if not result.get("has_more"):
                break
            cursor = result.get("next_cursor")
        return archived

    def append_page_blocks(self, page_id: str, children: list[dict[str, Any]]) -> None:
        """Append blocks to a page in batches of 100."""
        for i in range(0, len(children), 100):
            batch = children[i : i + 100]
            resp = requests.patch(
                f"https://api.notion.com/v1/blocks/{page_id}/children",
                headers=self.headers,
                json={"children": batch},
                timeout=90,
            )
            resp.raise_for_status()

    def write_markdown_to_page(self, page_id: str, markdown_text: str) -> None:
        """Clear existing page content and write markdown as Notion blocks."""
        self.clear_page_content(page_id)
        blocks = self._markdown_to_blocks(markdown_text)
        self.append_page_blocks(page_id, blocks)

    @staticmethod
    def _markdown_to_blocks(markdown_text: str) -> list[dict[str, Any]]:
        """Convert markdown headings and paragraphs to Notion block objects."""
        blocks: list[dict[str, Any]] = []
        normalized = _normalize_notion_text(markdown_text).replace("\r\n", "\n").replace("\r", "\n")
        current_paragraph_lines: list[str] = []

        def flush_paragraph() -> None:
            if current_paragraph_lines:
                text = " ".join(current_paragraph_lines).strip()
                for chunk in re.findall(r".{1,2000}", text, flags=re.DOTALL):
                    blocks.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {"rich_text": [{"type": "text", "text": {"content": chunk}}]},
                    })
                current_paragraph_lines.clear()

        for line in normalized.split("\n"):
            if line.startswith("# ") and not line.startswith("## "):
                flush_paragraph()
                text = line[2:].strip()[:2000]
                blocks.append({
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {"rich_text": [{"type": "text", "text": {"content": text}}]},
                })
            elif line.startswith("## ") and not line.startswith("### "):
                flush_paragraph()
                text = line[3:].strip()[:2000]
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {"rich_text": [{"type": "text", "text": {"content": text}}]},
                })
            elif line.startswith("### "):
                flush_paragraph()
                text = line[4:].strip()[:2000]
                blocks.append({
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": text}}]},
                })
            elif line.strip() == "":
                flush_paragraph()
            else:
                current_paragraph_lines.append(line)
        flush_paragraph()
        return blocks

    @staticmethod
    def _rich_text(text: str) -> list[dict[str, Any]]:
        chunks = []
        normalized = _normalize_notion_text(text)
        for piece in re.findall(r".{1,1900}", normalized, flags=re.DOTALL):
            chunks.append({"type": "text", "text": {"content": piece}})
        return chunks
