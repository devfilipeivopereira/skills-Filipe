#!/usr/bin/env python3
"""Build a compact, reflowable EPUB 3 package suitable for KDP upload."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import uuid
import zipfile
from datetime import date, datetime, timezone
from pathlib import Path

AUTHOR = "Kang Arin"
CHAPTER_RE = re.compile(r"^##\s+(.+?)\s*$")
H1_RE = re.compile(r"^#\s+(.+?)\s*$")
DIVIDER_RE = re.compile(r"^\s*(?:(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,})$")


def xml(value: object) -> str:
    return html.escape(str(value), quote=True)


def inline_markdown(value: str) -> str:
    safe = xml(value)
    safe = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", safe)
    safe = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", safe)
    return safe


def strip_frontmatter(lines: list[str]) -> list[str]:
    if not lines or lines[0].strip() != "---":
        return lines
    for index in range(1, len(lines)):
        if lines[index].strip() in {"---", "..."}:
            return lines[index + 1 :]
    raise ValueError("front matter iniciado, mas não encerrado")


def parse_manuscript(markdown: str) -> tuple[str | None, list[tuple[str, list[tuple[str, str]]]]]:
    lines = strip_frontmatter(markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n"))
    manuscript_title: str | None = None
    chapters: list[tuple[str, list[tuple[str, str]]]] = []
    current_title: str | None = None
    blocks: list[tuple[str, str]] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(("p", " ".join(part.strip() for part in paragraph if part.strip())))
            paragraph = []

    def flush_chapter() -> None:
        nonlocal blocks
        flush_paragraph()
        if current_title is not None:
            if not any(kind == "p" and text.strip() for kind, text in blocks):
                raise ValueError(f'capítulo sem prosa: "{current_title}"')
            chapters.append((current_title, blocks))
            blocks = []

    for raw_line in lines:
        line = raw_line.rstrip()
        h1 = H1_RE.match(line)
        chapter = CHAPTER_RE.match(line)
        if h1 and not chapter:
            if manuscript_title is None:
                manuscript_title = h1.group(1).strip()
            continue
        if chapter:
            flush_chapter()
            current_title = chapter.group(1).strip()
            continue
        if current_title is None:
            if line.strip():
                continue
            continue
        if DIVIDER_RE.match(line):
            flush_paragraph()
            if not blocks or blocks[-1][0] != "scene":
                blocks.append(("scene", "⁂"))
        elif not line.strip():
            flush_paragraph()
        elif line.lstrip().startswith("#"):
            raise ValueError(f"cabeçalho inesperado dentro do capítulo: {line}")
        else:
            paragraph.append(line)
    flush_chapter()

    if not chapters:
        raise ValueError("nenhum capítulo '## ...' encontrado")
    return manuscript_title, chapters


def xhtml_shell(title: str, body: str, language: str, epub_ns: bool = False) -> str:
    extra = ' xmlns:epub="http://www.idpf.org/2007/ops"' if epub_ns else ""
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"{extra} xml:lang="{xml(language)}" lang="{xml(language)}">
<head>
  <meta charset="utf-8"/>
  <title>{xml(title)}</title>
  <link rel="stylesheet" type="text/css" href="styles/book.css"/>
</head>
<body>
{body}
</body>
</html>
'''


def chapter_xhtml(title: str, blocks: list[tuple[str, str]], language: str) -> str:
    rendered: list[str] = [f'<section epub:type="chapter" role="doc-chapter">', f"<h1>{xml(title)}</h1>"]
    first = True
    for kind, text in blocks:
        if kind == "scene":
            rendered.append('<div class="scene-break" aria-label="Quebra de cena">⁂</div>')
            first = True
        else:
            class_attr = ' class="first"' if first else ""
            rendered.append(f"<p{class_attr}>{inline_markdown(text)}</p>")
            first = False
    rendered.append("</section>")
    return xhtml_shell(title, "\n".join(rendered), language, epub_ns=True)


CSS = """@charset "UTF-8";
html { -webkit-text-size-adjust: 100%; }
body { margin: 0 5%; padding: 0; line-height: 1.45; orphans: 2; widows: 2; }
p { margin: 0; text-indent: 1.25em; }
p.first, h1 + p, .scene-break + p { text-indent: 0; }
h1 { margin: 18% 0 12%; text-align: center; font-size: 1.45em; font-weight: normal; page-break-before: always; break-before: page; }
.title-page { text-align: center; padding-top: 28%; page-break-after: always; break-after: page; }
.book-title { font-size: 2em; margin: 0 0 1em; }
.subtitle { font-size: 1.15em; margin: 0 0 3em; }
.author { font-size: 1.2em; text-indent: 0; }
.copyright { padding-top: 20%; font-size: .9em; }
.copyright p, nav p, .about p { text-indent: 0; margin: 0 0 .8em; }
nav ol { list-style-type: none; padding-left: 0; }
nav li { margin: .55em 0; }
nav a { text-decoration: none; }
.scene-break { text-align: center; margin: 1.15em 0; text-indent: 0; }
.about { padding-top: 10%; }
"""


def metadata_values(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("metadata.json deve conter um objeto JSON")
    title = str(data.get("title", "")).strip()
    author = str(data.get("author", AUTHOR)).strip()
    if not title:
        raise ValueError("metadata.json não contém título")
    if author != AUTHOR:
        raise ValueError(f'a autora deve ser exatamente "{AUTHOR}"')
    language = str(data.get("language", "pt-BR")).strip() or "pt-BR"
    publication_date = str(data.get("publication_date", date.today().isoformat())).strip()
    try:
        date.fromisoformat(publication_date)
    except ValueError as exc:
        raise ValueError("publication_date deve usar AAAA-MM-DD") from exc
    identifier = str(data.get("identifier", "")).strip()
    if not identifier:
        identifier = f"urn:uuid:{uuid.uuid4()}"
    elif not identifier.startswith(("urn:uuid:", "urn:isbn:")):
        identifier = f"urn:uuid:{identifier}"
    subjects = data.get("subjects", [])
    if isinstance(subjects, str):
        subjects = [subjects]
    if not isinstance(subjects, list):
        raise ValueError("subjects deve ser uma lista de textos")
    year = publication_date[:4]
    return {
        **data,
        "title": title,
        "subtitle": str(data.get("subtitle", "")).strip(),
        "author": AUTHOR,
        "language": language,
        "publisher": str(data.get("publisher", AUTHOR)).strip() or AUTHOR,
        "description": str(data.get("description", "")).strip(),
        "rights": str(data.get("rights", f"Copyright © {year} {AUTHOR}. Todos os direitos reservados.")).strip(),
        "publication_date": publication_date,
        "identifier": identifier,
        "subjects": [str(subject).strip() for subject in subjects if str(subject).strip()],
        "author_bio": str(data.get("author_bio", "")).strip(),
    }


def build_opf(meta: dict, chapter_files: list[str], include_about: bool) -> str:
    subtitle_xml = ""
    if meta["subtitle"]:
        subtitle_xml = f'''  <dc:title id="subtitle">{xml(meta["subtitle"])}</dc:title>
  <meta refines="#subtitle" property="title-type">subtitle</meta>
'''
    subject_xml = "\n".join(f"  <dc:subject>{xml(subject)}</dc:subject>" for subject in meta["subjects"])
    chapter_manifest = "\n".join(
        f'  <item id="chap-{i:03d}" href="{xml(filename)}" media-type="application/xhtml+xml"/>'
        for i, filename in enumerate(chapter_files, 1)
    )
    chapter_spine = "\n".join(f'  <itemref idref="chap-{i:03d}"/>' for i in range(1, len(chapter_files) + 1))
    about_manifest = '  <item id="about" href="about.xhtml" media-type="application/xhtml+xml"/>' if include_about else ""
    about_spine = '  <itemref idref="about"/>' if include_about else ""
    modified = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="{xml(meta['language'])}" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
  <dc:identifier id="book-id">{xml(meta['identifier'])}</dc:identifier>
  <dc:title id="title">{xml(meta['title'])}</dc:title>
  <meta refines="#title" property="title-type">main</meta>
{subtitle_xml}  <dc:creator id="creator">{xml(AUTHOR)}</dc:creator>
  <meta refines="#creator" property="role" scheme="marc:relators">aut</meta>
  <dc:language>{xml(meta['language'])}</dc:language>
  <dc:publisher>{xml(meta['publisher'])}</dc:publisher>
  <dc:date>{xml(meta['publication_date'])}</dc:date>
  <dc:rights>{xml(meta['rights'])}</dc:rights>
  <dc:description>{xml(meta['description'])}</dc:description>
{subject_xml}
  <meta property="dcterms:modified">{modified}</meta>
  <meta property="rendition:layout">reflowable</meta>
  <meta name="cover" content="cover-image"/>
</metadata>
<manifest>
  <item id="cover-image" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>
  <item id="css" href="styles/book.css" media-type="text/css"/>
  <item id="titlepage" href="titlepage.xhtml" media-type="application/xhtml+xml"/>
  <item id="copyright" href="copyright.xhtml" media-type="application/xhtml+xml"/>
  <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
  <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
{chapter_manifest}
{about_manifest}
</manifest>
<spine toc="ncx">
  <itemref idref="titlepage"/>
  <itemref idref="copyright"/>
  <itemref idref="nav"/>
{chapter_spine}
{about_spine}
</spine>
</package>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description="Monta um EPUB 3 responsivo com capa e metadados para KDP.")
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("metadata", type=Path)
    parser.add_argument("cover", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    try:
        meta = metadata_values(args.metadata)
        manuscript_title, chapters = parse_manuscript(args.manuscript.read_text(encoding="utf-8-sig"))
        if manuscript_title and manuscript_title.casefold() != meta["title"].casefold():
            raise ValueError("o título H1 do manuscrito não coincide com metadata.json")
        cover_bytes = args.cover.read_bytes()
        if not cover_bytes.startswith(b"\xff\xd8"):
            raise ValueError("a capa deve ser JPEG")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 2

    chapter_files = [f"chapter-{i:03d}.xhtml" for i in range(1, len(chapters) + 1)]
    toc_items = "\n".join(
        f'      <li><a href="{filename}">{xml(title)}</a></li>'
        for filename, (title, _) in zip(chapter_files, chapters)
    )
    about_item = '      <li><a href="about.xhtml">Sobre a autora</a></li>\n' if meta["author_bio"] else ""
    nav_body = f'''<nav epub:type="toc" id="toc" role="doc-toc">
  <h1>Sumário</h1>
  <ol>
{toc_items}
{about_item}  </ol>
</nav>
<nav epub:type="landmarks" hidden="hidden">
  <ol>
    <li><a epub:type="toc" href="nav.xhtml#toc">Sumário</a></li>
    <li><a epub:type="bodymatter" href="{chapter_files[0]}">Início</a></li>
  </ol>
</nav>'''

    subtitle_line = f'<p class="subtitle">{xml(meta["subtitle"])}</p>' if meta["subtitle"] else ""
    title_body = f'''<section class="title-page" epub:type="titlepage">
  <h1 class="book-title">{xml(meta['title'])}</h1>
  {subtitle_line}
  <p class="author">{xml(AUTHOR)}</p>
</section>'''
    copyright_body = f'''<section class="copyright" epub:type="copyright-page">
  <p>{xml(meta['rights'])}</p>
  <p>Esta é uma obra de ficção. Nomes, personagens, lugares e acontecimentos são produto da imaginação da autora ou usados ficcionalmente.</p>
  <p>Todos os direitos reservados.</p>
</section>'''

    navpoints = []
    for index, (filename, (title, _)) in enumerate(zip(chapter_files, chapters), 1):
        navpoints.append(
            f'''    <navPoint id="navPoint-{index}" playOrder="{index}">
      <navLabel><text>{xml(title)}</text></navLabel>
      <content src="{filename}"/>
    </navPoint>'''
        )
    ncx = f'''<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head><meta name="dtb:uid" content="{xml(meta['identifier'])}"/></head>
  <docTitle><text>{xml(meta['title'])}</text></docTitle>
  <navMap>
{chr(10).join(navpoints)}
  </navMap>
</ncx>
'''
    container = '''<?xml version="1.0" encoding="utf-8"?>
<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
  <rootfiles><rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
'''

    files: dict[str, bytes] = {
        "META-INF/container.xml": container.encode("utf-8"),
        "EPUB/package.opf": build_opf(meta, chapter_files, bool(meta["author_bio"])).encode("utf-8"),
        "EPUB/nav.xhtml": xhtml_shell("Sumário", nav_body, meta["language"], epub_ns=True).encode("utf-8"),
        "EPUB/toc.ncx": ncx.encode("utf-8"),
        "EPUB/titlepage.xhtml": xhtml_shell(meta["title"], title_body, meta["language"], epub_ns=True).encode("utf-8"),
        "EPUB/copyright.xhtml": xhtml_shell("Direitos autorais", copyright_body, meta["language"], epub_ns=True).encode("utf-8"),
        "EPUB/styles/book.css": CSS.encode("utf-8"),
        "EPUB/images/cover.jpg": cover_bytes,
    }
    for filename, (title, blocks) in zip(chapter_files, chapters):
        files[f"EPUB/{filename}"] = chapter_xhtml(title, blocks, meta["language"]).encode("utf-8")
    if meta["author_bio"]:
        about_body = f'''<section class="about" epub:type="contributors">
  <h1>Sobre a autora</h1>
  <p>{inline_markdown(meta['author_bio'])}</p>
</section>'''
        files["EPUB/about.xhtml"] = xhtml_shell("Sobre a autora", about_body, meta["language"], epub_ns=True).encode("utf-8")

    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.output, "w") as archive:
            archive.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
            for name, content in files.items():
                archive.writestr(name, content, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    except OSError as exc:
        print(f"ERRO: não foi possível gravar o EPUB: {exc}", file=sys.stderr)
        return 2

    print(f"PASSOU: {args.output.resolve()} — EPUB 3 responsivo, {len(chapters)} capítulos, capa incorporada, autora {AUTHOR}")
    print(f"IDENTIFICADOR: {meta['identifier']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
