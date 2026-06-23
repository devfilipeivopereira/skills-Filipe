#!/usr/bin/env python3
"""
Apply assistant-produced chunk translations back into a tokenized EPUB workspace
and build a final EPUB output.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import zipfile
from pathlib import Path
from typing import Dict, Iterable, List

from lxml import etree

TEXT_EXTS = {".xhtml", ".html", ".htm"}
PTBR_TITLE_EXACT = {
    "Table of Contents": "Sumário",
    "Acknowledgments": "Agradecimentos",
    "Introduction": "Introdução",
    "Conclusion": "Conclusão",
    "Notes": "Notas",
    "Scripture Index": "Índice de Escrituras",
    "Epigraph": "Epígrafe",
    "Excursus": "Excurso",
    "1 The Family That Disciples": "1 A Família Que Discipula",
    "2 The Foundation": "2 O Alicerce",
    "3 Modeling": "3 Exemplo",
    "4 Time": "4 Tempo",
    "5 Moments": "5 Momentos",
    "6 Milestones": "6 Marcos",
    "Appendix A Word to Church and School Leaders": "Apêndice A Uma Palavra aos Líderes da Igreja e da Escola",
}
PTBR_COPY_EXACT = {
    "Modeling": "Exemplo",
    "sua filhos": "seus filhos",
    "seu filhos": "seus filhos",
    "Quanto a às": "Quanto às",
    "Quanto a os": "Quanto aos",
}
PTBR_COPY_REGEX = [
    (re.compile(r"\bAlmeja\b"), "Quer"),
    (re.compile(r"\balmeja\b"), "quer"),
    (re.compile(r"\bAlmejam\b"), "Querem"),
    (re.compile(r"\balmejam\b"), "querem"),
    (re.compile(r"\bAlmejar\b"), "Querer"),
    (re.compile(r"\balmejar\b"), "querer"),
    (re.compile(r"\bAlmejamos\b"), "Queremos"),
    (re.compile(r"\balmejamos\b"), "queremos"),
    (re.compile(r"\bAlmejo\b"), "Quero"),
    (re.compile(r"\balmejo\b"), "quero"),
    (re.compile(r"\bFidedigno\b"), "Confiável"),
    (re.compile(r"\bfidedigno\b"), "confiável"),
    (re.compile(r"\bFidedigna\b"), "Confiável"),
    (re.compile(r"\bfidedigna\b"), "confiável"),
]


def _parse_xml(path: Path):
    raw = path.read_bytes()
    has_xml_decl = raw.lstrip().startswith(b"<?xml")
    parser = etree.XMLParser(recover=True, huge_tree=True, remove_blank_text=False)
    root = etree.fromstring(raw, parser=parser)
    return root, has_xml_decl


def _serialize_xml(root: etree._Element, has_xml_decl: bool, path: Path) -> None:
    data = etree.tostring(
        root,
        encoding="utf-8",
        xml_declaration=has_xml_decl,
        pretty_print=False,
    )
    path.write_bytes(data)


def _read_jsonl(path: Path) -> Iterable[dict]:
    # utf-8-sig allows JSONL files saved with BOM by some editors on Windows.
    with path.open("r", encoding="utf-8-sig") as f:
        for line_num, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                yield json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at {path}:{line_num}: {exc}") from exc


def _localname(tag: str) -> str:
    if not isinstance(tag, str):
        return ""
    if "}" in tag:
        return tag.split("}", 1)[1].lower()
    return tag.lower()


def _split_ws(text: str) -> tuple[str, str, str]:
    leading_len = len(text) - len(text.lstrip())
    trailing_len = len(text) - len(text.rstrip())
    leading = text[:leading_len]
    trailing = text[len(text) - trailing_len :] if trailing_len else ""
    core = text[leading_len : len(text) - trailing_len if trailing_len else len(text)]
    return leading, core, trailing


def _normalize_ptbr_core_text(text: str) -> str:
    out = text
    for old, new in PTBR_COPY_EXACT.items():
        out = out.replace(old, new)
    for pattern, repl in PTBR_COPY_REGEX:
        out = pattern.sub(repl, out)
    out = re.sub(r"\s+([,.;:?!])", r"\1", out)
    out = re.sub(r"([,.;:?!])([A-Za-zÀ-ÖØ-öø-ÿ])", r"\1 \2", out)
    return out


def _normalize_ptbr_text(text: str, exact_title_map: dict[str, str]) -> str:
    if not text:
        return text
    leading, core, trailing = _split_ws(text)
    if not core:
        return text
    mapped = exact_title_map.get(core, core)
    normalized = _normalize_ptbr_core_text(mapped)
    return f"{leading}{normalized}{trailing}"


def _apply_ptbr_natural_pass(extracted_root: Path) -> int:
    updated = 0
    files = sorted(
        [
            p
            for p in extracted_root.rglob("*")
            if p.is_file() and (p.suffix.lower() in TEXT_EXTS or p.suffix.lower() == ".ncx")
        ]
    )

    for file_path in files:
        root, has_decl = _parse_xml(file_path)
        changed = False

        for text_node in root.xpath("//text()"):
            parent = text_node.getparent()
            if parent is None:
                continue

            slot_text = str(text_node)
            if not slot_text.strip():
                continue

            parent_name = _localname(parent.tag)
            title_map: dict[str, str] = {}
            if parent_name == "title":
                title_map = PTBR_TITLE_EXACT
            elif file_path.suffix.lower() == ".ncx" and parent_name == "text":
                title_map = PTBR_TITLE_EXACT

            replacement = _normalize_ptbr_text(slot_text, title_map)
            if replacement != slot_text:
                if getattr(text_node, "is_text", False):
                    parent.text = replacement
                elif getattr(text_node, "is_tail", False):
                    parent.tail = replacement
                changed = True

        if changed:
            _serialize_xml(root, has_decl, file_path)
            updated += 1

    return updated


def _load_translations(translations_arg: Path) -> Dict[str, str]:
    files: List[Path] = []
    if translations_arg.is_dir():
        files = sorted(translations_arg.rglob("*.jsonl"))
    else:
        files = [translations_arg]

    if not files:
        raise RuntimeError(f"No translation files found in: {translations_arg}")

    out: Dict[str, str] = {}
    for file_path in files:
        for row in _read_jsonl(file_path):
            text_id = row.get("id")
            target = row.get("target")
            if not text_id:
                continue
            if target is None:
                continue
            out[text_id] = str(target)
    return out


def _apply_lang_tag(extracted_root: Path, lang_tag: str) -> int:
    updated = 0

    # 1) Update OPF dc:language
    for opf in extracted_root.rglob("*.opf"):
        root, has_decl = _parse_xml(opf)
        ns = root.nsmap.copy()
        if None in ns:
            ns["opf"] = ns.pop(None)
        if "dc" not in ns:
            ns["dc"] = "http://purl.org/dc/elements/1.1/"

        lang_nodes = root.xpath("//dc:language", namespaces=ns)
        changed = False
        if lang_nodes:
            for node in lang_nodes:
                if (node.text or "").strip() != lang_tag:
                    node.text = lang_tag
                    changed = True
        if changed:
            _serialize_xml(root, has_decl, opf)
            updated += 1

    # 2) Update html/xml:lang in XHTML files
    for html_file in extracted_root.rglob("*"):
        if html_file.suffix.lower() not in TEXT_EXTS:
            continue
        root, has_decl = _parse_xml(html_file)
        changed = False
        # Root is expected to be <html ...>
        if isinstance(root.tag, str) and root.tag.lower().endswith("html"):
            if root.get("{http://www.w3.org/XML/1998/namespace}lang") != lang_tag:
                root.set("{http://www.w3.org/XML/1998/namespace}lang", lang_tag)
                changed = True
            if root.get("lang") != lang_tag:
                root.set("lang", lang_tag)
                changed = True
        if changed:
            _serialize_xml(root, has_decl, html_file)
            updated += 1

    return updated


def _build_epub_from_dir(extracted_root: Path, output_epub: Path) -> None:
    if output_epub.exists():
        output_epub.unlink()
    output_epub.parent.mkdir(parents=True, exist_ok=True)

    mimetype_path = extracted_root / "mimetype"
    all_files = sorted([p for p in extracted_root.rglob("*") if p.is_file()])

    with zipfile.ZipFile(output_epub, "w") as zf:
        if mimetype_path.exists():
            zf.write(
                mimetype_path,
                arcname="mimetype",
                compress_type=zipfile.ZIP_STORED,
            )

        for file_path in all_files:
            if mimetype_path.exists() and file_path.resolve() == mimetype_path.resolve():
                continue
            arcname = file_path.relative_to(extracted_root).as_posix()
            zf.write(file_path, arcname=arcname, compress_type=zipfile.ZIP_DEFLATED)


def apply_translations(
    workspace: Path,
    translations_path: Path,
    output_epub: Path,
    lang_tag: str | None,
    ptbr_natural_pass_mode: str,
) -> None:
    manifest_path = workspace / "manifest.json"
    nodes_path = workspace / "nodes.jsonl"
    extracted_root = workspace / "extracted_tokenized"

    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest.json not found in workspace: {workspace}")
    if not nodes_path.exists():
        raise FileNotFoundError(f"nodes.jsonl not found in workspace: {workspace}")
    if not extracted_root.exists():
        raise FileNotFoundError(f"extracted_tokenized not found in workspace: {workspace}")

    translations = _load_translations(translations_path)
    if not translations:
        raise RuntimeError("No usable translations found (id + target).")

    nodes = list(_read_jsonl(nodes_path))
    if not nodes:
        raise RuntimeError("nodes.jsonl is empty.")

    missing_ids = [n["id"] for n in nodes if n["id"] not in translations]
    if missing_ids:
        preview = ", ".join(missing_ids[:10])
        raise RuntimeError(
            f"Missing translations for {len(missing_ids)} ids. Example: {preview}"
        )

    by_file: Dict[str, List[dict]] = {}
    for node in nodes:
        by_file.setdefault(node["file"], []).append(node)

    updated_nodes = 0
    for rel_file, file_nodes in by_file.items():
        target_file = extracted_root / rel_file
        if not target_file.exists():
            raise FileNotFoundError(f"Expected file not found in tokenized EPUB: {target_file}")

        root, has_decl = _parse_xml(target_file)
        changed = False

        for node in file_nodes:
            xpath = node["xpath"]
            slot = node["slot"]
            text_id = node["id"]
            leading_ws = node.get("leading_ws", "")
            trailing_ws = node.get("trailing_ws", "")

            parents = root.xpath(xpath)
            if not parents:
                raise RuntimeError(
                    f"XPath not found while applying translation: file={rel_file} xpath={xpath}"
                )
            parent = parents[0]

            target_text = translations[text_id].strip()
            final_text = f"{leading_ws}{target_text}{trailing_ws}"

            if slot == "text":
                parent.text = final_text
            elif slot == "tail":
                parent.tail = final_text
            else:
                raise ValueError(f"Unsupported slot '{slot}' for id {text_id}")

            changed = True
            updated_nodes += 1

        if changed:
            _serialize_xml(root, has_decl, target_file)

    lang_updates = 0
    if lang_tag:
        lang_updates = _apply_lang_tag(extracted_root, lang_tag)

    mode = ptbr_natural_pass_mode.lower().strip()
    if mode not in {"auto", "on", "off"}:
        raise ValueError("--ptbr-natural-pass must be one of: auto, on, off")

    do_natural_pass = False
    if mode == "on":
        do_natural_pass = True
    elif mode == "auto":
        do_natural_pass = bool(lang_tag and lang_tag.lower().startswith("pt"))

    natural_updates = 0
    if do_natural_pass:
        natural_updates = _apply_ptbr_natural_pass(extracted_root)

    _build_epub_from_dir(extracted_root, output_epub)

    print("ASSISTANT_WORKFLOW_APPLIED")
    print(f"WORKSPACE={workspace}")
    print(f"UPDATED_NODES={updated_nodes}")
    print(f"LANG_UPDATES={lang_updates}")
    print(f"NATURAL_PASS_MODE={mode}")
    print(f"NATURAL_UPDATES={natural_updates}")
    print(f"OUTPUT_EPUB={output_epub}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply assistant JSONL translations and rebuild EPUB."
    )
    parser.add_argument("--workspace", required=True, help="Workspace directory from prepare step.")
    parser.add_argument(
        "--translations",
        required=True,
        help="Path to a JSONL file or directory containing JSONL files with {id,target}.",
    )
    parser.add_argument("--output", required=True, help="Output EPUB path.")
    parser.add_argument(
        "--lang-tag",
        default="",
        help="Optional language tag to apply in OPF/XHTML (e.g. pt-BR).",
    )
    parser.add_argument(
        "--ptbr-natural-pass",
        default="auto",
        help="Naturalness post-pass mode: auto|on|off (default: auto).",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).expanduser().resolve()
    translations = Path(args.translations).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    lang_tag = args.lang_tag.strip() or None

    if not workspace.exists():
        raise FileNotFoundError(f"Workspace not found: {workspace}")
    if not translations.exists():
        raise FileNotFoundError(f"Translations path not found: {translations}")

    apply_translations(
        workspace,
        translations,
        output,
        lang_tag,
        args.ptbr_natural_pass,
    )


if __name__ == "__main__":
    main()
