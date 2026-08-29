#!/usr/bin/env python3
"""Create and validate a reflowable EPUB 3 plus an upload-ready KDP cover."""

from __future__ import annotations

import argparse
import re
import shutil
import tempfile
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

from docx import Document
from PIL import Image


LANGUAGE = "pt-BR"
CSS = """body { margin: 5%; font-family: serif; line-height: 1.5; }
h1 { font-size: 1.6em; margin: 1.6em 0 1em; break-before: page; page-break-before: always; }
h2 { font-size: 1.22em; margin: 1.35em 0 .7em; }
p { margin: 0 0 .85em; text-indent: 1.25em; }
h1 + p, h2 + p, .title-page p { text-indent: 0; }
.title-page { text-align: center; padding-top: 15%; }
.title-page h1 { break-before: auto; page-break-before: auto; font-size: 2em; }
.subtitle { font-size: 1.15em; }
.cover { margin: 0; padding: 0; text-align: center; }
.cover img { width: 100%; height: auto; }
nav ol { padding-left: 1.2em; }
"""


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def xhtml_page(title: str, body: str) -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{LANGUAGE}" lang="{LANGUAGE}">
<head><title>{escape(title)}</title><link rel="stylesheet" type="text/css" href="styles.css"/></head>
<body>{body}</body></html>
'''


def document_sections(path: Path) -> list[tuple[str, list[tuple[str, str]]]]:
    """Extract chapters and paragraphs from DOCX or plain text."""
    if path.suffix.lower() == ".txt":
        sections: list[tuple[str, list[tuple[str, str]]]] = []
        current_title, current = "Texto", []
        for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
            line = clean(raw_line)
            if not line:
                continue
            if line.startswith("#"):
                heading = clean(line.lstrip("#"))
                if current:
                    sections.append((current_title, current))
                current_title, current = heading or "Texto", []
            else:
                current.append(("p", line))
        if current:
            sections.append((current_title, current))
        return sections

    if path.suffix.lower() != ".docx":
        raise ValueError("O manuscrito deve ser um arquivo DOCX ou TXT.")

    sections: list[tuple[str, list[tuple[str, str]]]] = []
    current_title, current = "Texto", []
    for paragraph in Document(path).paragraphs:
        text = clean(paragraph.text)
        if not text:
            continue
        style = paragraph.style.name.casefold()
        if style.startswith("heading 1") or style.startswith("título 1"):
            if text.casefold() in {"sumário", "índice", "conteúdo"}:
                continue
            if current:
                sections.append((current_title, current))
            current_title, current = text, []
        elif style.startswith("heading 2") or style.startswith("título 2"):
            current.append(("h2", text))
        else:
            current.append(("p", text))
    if current:
        sections.append((current_title, current))
    if not sections:
        raise ValueError("Não foi possível extrair texto do manuscrito.")
    return sections


def make_cover(source: Path, destination: Path) -> None:
    if source.suffix.lower() not in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}:
        raise ValueError("A capa deve ser PNG, JPEG ou TIFF.")
    with Image.open(source) as image:
        rgb = image.convert("RGB")
        width, height = rgb.size
        if width < 1000:
            scale = 1000 / width
            rgb = rgb.resize((1000, round(height * scale)), Image.Resampling.LANCZOS)
        destination.parent.mkdir(parents=True, exist_ok=True)
        rgb.save(destination, "JPEG", quality=95, optimize=True)


def nav_page(entries: list[tuple[str, str]]) -> str:
    links = "".join(f'<li><a href="{href}">{escape(label)}</a></li>' for label, href in entries)
    return xhtml_page("Sumário", f'<nav epub:type="toc" id="toc" xmlns:epub="http://www.idpf.org/2007/ops"><h1>Sumário</h1><ol>{links}</ol></nav>')


def package_opf(sections: list[tuple[str, list[tuple[str, str]]]], title: str, author: str) -> str:
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>', '<item id="css" href="styles.css" media-type="text/css"/>', '<item id="cover-image" href="cover.jpg" media-type="image/jpeg" properties="cover-image"/>', '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>', '<item id="title" href="titlepage.xhtml" media-type="application/xhtml+xml"/>']
    spine = ['<itemref idref="cover" linear="no"/>', '<itemref idref="title"/>']
    for number, _ in enumerate(sections, 1):
        manifest.append(f'<item id="chapter-{number}" href="chapter-{number}.xhtml" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="chapter-{number}"/>')
    return f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">urn:uuid:{uuid.uuid4()}</dc:identifier><dc:title>{escape(title)}</dc:title><dc:creator>{escape(author)}</dc:creator><dc:language>{LANGUAGE}</dc:language><meta property="dcterms:modified">{modified}</meta></metadata>
<manifest>{''.join(manifest)}</manifest><spine>{''.join(spine)}</spine></package>'''


def validate_epub(path: Path) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype" or archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise ValueError("EPUB inválido: mimetype precisa ser o primeiro item sem compressão.")
        if archive.read("mimetype") != b"application/epub+zip":
            raise ValueError("EPUB inválido: mimetype incorreto.")
        required = {"META-INF/container.xml", "OEBPS/content.opf", "OEBPS/nav.xhtml", "OEBPS/cover.xhtml", "OEBPS/cover.jpg"}
        missing = required - set(names)
        if missing:
            raise ValueError("EPUB inválido: faltam " + ", ".join(sorted(missing)))
        for item in [name for name in names if name.endswith((".xhtml", ".opf", ".xml"))]:
            ET.fromstring(archive.read(item))


def build(manuscript: Path, cover: Path, output: Path, title: str, author: str, subtitle: str) -> Path:
    if not title or not author:
        raise ValueError("Título e autor são obrigatórios.")
    sections = document_sections(manuscript)
    cover_output = output.with_name(output.stem + "_cover_kdp.jpg")
    make_cover(cover, cover_output)
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        oebps, meta = root / "OEBPS", root / "META-INF"
        oebps.mkdir(); meta.mkdir()
        (root / "mimetype").write_bytes(b"application/epub+zip")
        (meta / "container.xml").write_text('<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>', encoding="utf-8")
        shutil.copyfile(cover_output, oebps / "cover.jpg")
        (oebps / "styles.css").write_text(CSS, encoding="utf-8")
        (oebps / "cover.xhtml").write_text(xhtml_page(title, f'<div class="cover"><img src="cover.jpg" alt="Capa de {escape(title)}"/></div>'), encoding="utf-8")
        subtitle_html = f'<p class="subtitle">{escape(subtitle)}</p>' if subtitle else ""
        (oebps / "titlepage.xhtml").write_text(xhtml_page(title, f'<section class="title-page"><h1>{escape(title)}</h1>{subtitle_html}<p>{escape(author)}</p></section>'), encoding="utf-8")
        entries = [("Capa", "cover.xhtml"), (title, "titlepage.xhtml")]
        for number, (heading, elements) in enumerate(sections, 1):
            body = '<section><h1>' + escape(heading) + '</h1>' + ''.join(f'<{tag}>{escape(text)}</{tag}>' for tag, text in elements) + '</section>'
            filename = f"chapter-{number}.xhtml"
            (oebps / filename).write_text(xhtml_page(heading, body), encoding="utf-8")
            entries.append((heading, filename))
        (oebps / "nav.xhtml").write_text(nav_page(entries), encoding="utf-8")
        (oebps / "content.opf").write_text(package_opf(sections, title, author), encoding="utf-8")
        output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(output, "w") as archive:
            archive.write(root / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
            for file in sorted(root.rglob("*")):
                if file.is_file() and file.name != "mimetype":
                    archive.write(file, file.relative_to(root).as_posix(), compress_type=zipfile.ZIP_DEFLATED)
    validate_epub(output)
    return cover_output


def main() -> None:
    parser = argparse.ArgumentParser(description="Cria EPUB 3 refluível para KDP a partir de DOCX ou TXT.")
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("cover", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--subtitle", default="")
    args = parser.parse_args()
    cover = build(args.manuscript, args.cover, args.output, args.title, args.author, args.subtitle)
    print(f"EPUB criado e validado: {args.output}")
    print(f"Capa JPEG para o KDP: {cover}")


if __name__ == "__main__":
    main()
