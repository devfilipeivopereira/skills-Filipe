#!/usr/bin/env python3
"""Convert a sermon .docx file into a minimal .epub file."""

from __future__ import annotations

import argparse
import html
import shutil
import re
import uuid
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


WORD_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def parse_args() -> argparse.Namespace:
    skill_dir = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-docx", required=True, help="Path to input .docx sermon")
    parser.add_argument("--reference", required=True, help="Biblical reference used in the sermon")
    parser.add_argument("--preacher", required=True, help="Preacher name used by the skill")
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parents[2] / "EPUB_TALKS"),
        help="Directory where the .epub file will be written",
    )
    parser.add_argument(
        "--cleanup-dir",
        default=str(skill_dir / "outputs"),
        help="Directory to empty after the epub is successfully written",
    )
    parser.add_argument("--title", default="", help="Optional EPUB title override")
    return parser.parse_args()


def sanitize_filename_part(value: str) -> str:
    cleaned = re.sub(r"[^\w]+", "_", value.strip(), flags=re.UNICODE)
    cleaned = re.sub(r"_+", "_", cleaned, flags=re.UNICODE).strip("_")
    return cleaned or "Sem_Referencia"


def read_docx_paragraphs(docx_path: Path) -> list[str]:
    with zipfile.ZipFile(docx_path) as zf:
        xml_bytes = zf.read("word/document.xml")

    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for paragraph in root.findall(".//w:p", WORD_NS):
        texts = [node.text or "" for node in paragraph.findall(".//w:t", WORD_NS)]
        text = "".join(texts).strip()
        if text:
            paragraphs.append(text)
    return paragraphs


def build_xhtml(title: str, paragraphs: list[str]) -> str:
    body_parts = [f"<h1>{html.escape(title)}</h1>"]
    for paragraph in paragraphs[1:]:
        body_parts.append(f"<p>{html.escape(paragraph)}</p>")
    body = "\n    ".join(body_parts)
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-BR">
  <head>
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" type="text/css" href="styles.css"/>
  </head>
  <body>
    {body}
  </body>
</html>
"""


def build_epub(docx_path: Path, output_dir: Path, reference: str, preacher: str, title_override: str = "") -> Path:
    paragraphs = read_docx_paragraphs(docx_path)
    if not paragraphs:
        raise ValueError("The .docx file does not contain readable paragraphs.")

    title = title_override.strip() or paragraphs[0]
    book_id = str(uuid.uuid4())
    file_name = f"{sanitize_filename_part(reference)}_{sanitize_filename_part(preacher)}.epub"
    reference_dir = output_dir / sanitize_filename_part(reference)
    reference_dir.mkdir(parents=True, exist_ok=True)
    output_path = reference_dir / file_name

    chapter_xhtml = build_xhtml(title, paragraphs)
    nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="pt-BR">
  <head><title>Navigation</title></head>
  <body>
    <nav epub:type="toc" id="toc">
      <h1>Sumario</h1>
      <ol>
        <li><a href="chapter1.xhtml">{html.escape(title)}</a></li>
      </ol>
    </nav>
  </body>
</html>
"""
    content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="3.0" xml:lang="pt-BR">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{book_id}</dc:identifier>
    <dc:title>{html.escape(title)}</dc:title>
    <dc:language>pt-BR</dc:language>
    <dc:creator>{html.escape(preacher)}</dc:creator>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="chapter1" href="chapter1.xhtml" media-type="application/xhtml+xml"/>
    <item id="css" href="styles.css" media-type="text/css"/>
  </manifest>
  <spine>
    <itemref idref="chapter1"/>
  </spine>
</package>
"""
    container_xml = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""
    stylesheet = """body { font-family: serif; line-height: 1.5; margin: 5%; }\nh1 { margin-bottom: 1.2em; }\np { margin: 0 0 1em 0; }\n"""

    with zipfile.ZipFile(output_path, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", container_xml)
        zf.writestr("OEBPS/content.opf", content_opf)
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml)
        zf.writestr("OEBPS/chapter1.xhtml", chapter_xhtml)
        zf.writestr("OEBPS/styles.css", stylesheet)

    return output_path


def empty_directory(path: Path) -> None:
    if not path.exists() or not path.is_dir():
        return
    for child in path.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def main() -> int:
    args = parse_args()
    output_path = build_epub(
        docx_path=Path(args.input_docx),
        output_dir=Path(args.output_dir),
        reference=args.reference,
        preacher=args.preacher,
        title_override=args.title,
    )
    empty_directory(Path(args.cleanup_dir))
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
