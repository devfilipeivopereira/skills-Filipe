#!/usr/bin/env python3
"""
Prepare an EPUB for assistant-driven chunk-by-chunk translation.

This script:
1. Extracts the EPUB into a workspace folder.
2. Replaces translatable XHTML text nodes with stable tokens.
3. Writes chunk files (JSONL + Markdown) for manual/assistant translation.
4. Saves a node map so translated chunks can be re-applied later.
"""

from __future__ import annotations

import argparse
import json
import shutil
import zipfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from lxml import etree

SKIP_TAGS = {"script", "style", "noscript"}
TEXT_EXTS = {".xhtml", ".html", ".htm"}


def _localname(tag: str) -> str:
    if not isinstance(tag, str):
        return ""
    if "}" in tag:
        return tag.split("}", 1)[1].lower()
    return tag.lower()


def _parse_xml(path: Path) -> Tuple[etree._Element, bool]:
    raw = path.read_bytes()
    has_xml_decl = raw.lstrip().startswith(b"<?xml")
    parser = etree.XMLParser(recover=True, huge_tree=True, remove_blank_text=False)
    root = etree.fromstring(raw, parser=parser)
    return root, has_xml_decl


def _opf_and_spine(extracted_root: Path) -> Tuple[Path, List[Path]]:
    container = extracted_root / "META-INF" / "container.xml"
    if not container.exists():
        return extracted_root, []

    croot, _ = _parse_xml(container)
    ns = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
    rootfile_nodes = croot.xpath(
        "/c:container/c:rootfiles/c:rootfile/@full-path", namespaces=ns
    )
    if not rootfile_nodes:
        return extracted_root, []

    opf_rel = rootfile_nodes[0]
    opf_path = extracted_root / opf_rel
    if not opf_path.exists():
        return extracted_root, []

    opf_root, _ = _parse_xml(opf_path)
    opf_ns_uri = opf_root.nsmap.get(None, "http://www.idpf.org/2007/opf")
    ns_opf = {"opf": opf_ns_uri}

    manifest: Dict[str, Path] = {}
    for item in opf_root.xpath("//opf:manifest/opf:item", namespaces=ns_opf):
        item_id = item.get("id")
        href = item.get("href")
        if not item_id or not href:
            continue
        manifest[item_id] = (opf_path.parent / href).resolve()

    spine_paths: List[Path] = []
    for itemref in opf_root.xpath("//opf:spine/opf:itemref", namespaces=ns_opf):
        item_idref = itemref.get("idref")
        if item_idref and item_idref in manifest:
            spine_paths.append(manifest[item_idref])

    return opf_path.parent, spine_paths


def _iter_xhtml_files(extracted_root: Path) -> List[Path]:
    opf_dir, spine = _opf_and_spine(extracted_root)
    spine_set = {p.resolve() for p in spine}

    all_html = sorted(
        [p for p in extracted_root.rglob("*") if p.suffix.lower() in TEXT_EXTS]
    )

    ordered: List[Path] = []
    for p in spine:
        if p.exists() and p.suffix.lower() in TEXT_EXTS:
            ordered.append(p)
    for p in all_html:
        if p.resolve() not in spine_set:
            ordered.append(p)
    return ordered


def _split_whitespace(text: str) -> Tuple[str, str, str]:
    leading_len = len(text) - len(text.lstrip())
    trailing_len = len(text) - len(text.rstrip())
    leading = text[:leading_len]
    trailing = text[len(text) - trailing_len :] if trailing_len else ""
    core = text[leading_len : len(text) - trailing_len if trailing_len else len(text)]
    return leading, core, trailing


def _serialize_xml(root: etree._Element, has_xml_decl: bool, path: Path) -> None:
    data = etree.tostring(
        root,
        encoding="utf-8",
        xml_declaration=has_xml_decl,
        pretty_print=False,
    )
    path.write_bytes(data)


def _chunk_entries(entries: List[dict], chunk_chars: int) -> List[List[dict]]:
    chunks: List[List[dict]] = []
    current: List[dict] = []
    size = 0
    for item in entries:
        text_size = len(item["source_core"])
        if current and size + text_size > chunk_chars:
            chunks.append(current)
            current = []
            size = 0
        current.append(item)
        size += text_size
    if current:
        chunks.append(current)
    return chunks


def _write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def prepare(input_epub: Path, workspace: Path, chunk_chars: int) -> None:
    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True, exist_ok=True)

    extracted = workspace / "extracted_tokenized"
    extracted.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(input_epub, "r") as zf:
        zf.extractall(extracted)

    html_files = _iter_xhtml_files(extracted)
    if not html_files:
        raise RuntimeError("No XHTML/HTML files found inside EPUB.")

    nodes: List[dict] = []
    next_id = 1

    for html_file in html_files:
        root, has_xml_decl = _parse_xml(html_file)
        tree = root.getroottree()
        changed = False

        for text_node in root.xpath("//text()"):
            parent = text_node.getparent()
            if parent is None:
                continue
            if _localname(parent.tag) in SKIP_TAGS:
                continue

            source = str(text_node)
            if not source.strip():
                continue

            leading_ws, source_core, trailing_ws = _split_whitespace(source)
            if not source_core:
                continue

            token_id = f"T{next_id:06d}"
            token = f"__CDX_{token_id}__"
            next_id += 1

            if getattr(text_node, "is_text", False):
                parent.text = token
                slot = "text"
            elif getattr(text_node, "is_tail", False):
                parent.tail = token
                slot = "tail"
            else:
                continue

            changed = True
            rel_path = html_file.relative_to(extracted).as_posix()
            nodes.append(
                {
                    "id": token_id,
                    "token": token,
                    "file": rel_path,
                    "xpath": tree.getpath(parent),
                    "slot": slot,
                    "source": source,
                    "source_core": source_core,
                    "leading_ws": leading_ws,
                    "trailing_ws": trailing_ws,
                }
            )

        if changed:
            _serialize_xml(root, has_xml_decl, html_file)

    if not nodes:
        raise RuntimeError("No translatable text nodes were detected.")

    chunks = _chunk_entries(nodes, chunk_chars)

    chunks_dir = workspace / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    translations_dir = workspace / "translations"
    translations_dir.mkdir(parents=True, exist_ok=True)

    for idx, chunk in enumerate(chunks, start=1):
        chunk_name = f"chunk_{idx:04d}"
        jsonl_path = chunks_dir / f"{chunk_name}.jsonl"
        md_path = chunks_dir / f"{chunk_name}.md"

        _write_jsonl(
            jsonl_path,
            ({"id": n["id"], "source": n["source_core"], "file": n["file"]} for n in chunk),
        )

        with md_path.open("w", encoding="utf-8", newline="\n") as md:
            md.write(f"# {chunk_name}\n\n")
            md.write("Translate each source to the target language.\n")
            md.write("Return JSONL lines in this exact format:\n")
            md.write('{"id":"T000001","target":"..."}\n\n')
            for n in chunk:
                md.write(f'ID: {n["id"]}\n')
                md.write(f'SOURCE: {n["source_core"]}\n\n')

    manifest = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "input_epub": str(input_epub),
        "workspace": str(workspace),
        "tokenized_root": str(extracted),
        "chunk_chars": chunk_chars,
        "total_files": len(html_files),
        "total_nodes": len(nodes),
        "total_chunks": len(chunks),
        "instructions": {
            "translation_format": "JSONL with {id,target}",
            "apply_command_example": (
                "python apply-assistant-epub-workflow.py "
                "--workspace <workspace> --translations <jsonl-or-dir> --output <output.epub> --lang-tag pt-BR"
            ),
        },
    }

    (workspace / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    _write_jsonl(workspace / "nodes.jsonl", nodes)
    _write_jsonl(
        translations_dir / "translations_template.jsonl",
        ({"id": n["id"], "target": ""} for n in nodes),
    )

    print("ASSISTANT_WORKFLOW_READY")
    print(f"WORKSPACE={workspace}")
    print(f"TOTAL_FILES={len(html_files)}")
    print(f"TOTAL_NODES={len(nodes)}")
    print(f"TOTAL_CHUNKS={len(chunks)}")
    print(f"FIRST_CHUNK={chunks_dir / 'chunk_0001.md'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare EPUB for assistant chunk workflow.")
    parser.add_argument("--input", required=True, help="Input EPUB path.")
    parser.add_argument(
        "--workspace",
        required=True,
        help="Workspace directory where tokenized EPUB and chunks will be written.",
    )
    parser.add_argument(
        "--chunk-chars",
        type=int,
        default=1800,
        help="Approximate total source characters per chunk file.",
    )
    args = parser.parse_args()

    input_epub = Path(args.input).expanduser().resolve()
    workspace = Path(args.workspace).expanduser().resolve()

    if not input_epub.exists():
        raise FileNotFoundError(f"Input EPUB not found: {input_epub}")
    if input_epub.suffix.lower() != ".epub":
        raise ValueError(f"Input must be .epub: {input_epub}")
    if args.chunk_chars < 200:
        raise ValueError("--chunk-chars must be >= 200")

    prepare(input_epub, workspace, args.chunk_chars)


if __name__ == "__main__":
    main()
