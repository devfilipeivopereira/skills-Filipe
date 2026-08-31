#!/usr/bin/env python3
"""Validate the EPUB structure, KDP-oriented cover/nav rules, and word target."""

from __future__ import annotations

import argparse
import posixpath
import sys
import zipfile
from io import BytesIO
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

from count_words import count_words

AUTHOR = "Kang Arin"
NS = {
    "container": "urn:oasis:names:tc:opendocument:xmlns:container",
    "opf": "http://www.idpf.org/2007/opf",
    "dc": "http://purl.org/dc/elements/1.1/",
    "xhtml": "http://www.w3.org/1999/xhtml",
}
EPUB_TYPE = "{http://www.idpf.org/2007/ops}type"


def join_from(base_file: str, href: str) -> str:
    base = str(PurePosixPath(base_file).parent)
    return posixpath.normpath(posixpath.join(base, href.split("#", 1)[0]))


def parse_xml(data: bytes, label: str, errors: list[str]) -> ET.Element | None:
    try:
        return ET.fromstring(data)
    except ET.ParseError as exc:
        errors.append(f"XML inválido em {label}: {exc}")
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida EPUB 3 para o fluxo editorial KDP desta skill.")
    parser.add_argument("epub", type=Path)
    parser.add_argument("--manuscript", type=Path)
    parser.add_argument("--target", type=int, default=30000)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    checks: list[str] = []

    try:
        archive = zipfile.ZipFile(args.epub, "r")
    except (OSError, zipfile.BadZipFile) as exc:
        print(f"FALHOU: EPUB ilegível: {exc}", file=sys.stderr)
        return 2

    with archive:
        infos = archive.infolist()
        names = {info.filename for info in infos}
        if not infos or infos[0].filename != "mimetype":
            errors.append("mimetype não é o primeiro item do ZIP")
        else:
            if infos[0].compress_type != zipfile.ZIP_STORED:
                errors.append("mimetype está comprimido")
            if archive.read("mimetype") != b"application/epub+zip":
                errors.append("conteúdo de mimetype incorreto")
            else:
                checks.append("mimetype EPUB correto e sem compressão")

        container_path = "META-INF/container.xml"
        if container_path not in names:
            errors.append("META-INF/container.xml ausente")
            opf_path = ""
        else:
            container = parse_xml(archive.read(container_path), container_path, errors)
            rootfile = container.find("container:rootfiles/container:rootfile", NS) if container is not None else None
            opf_path = rootfile.get("full-path", "") if rootfile is not None else ""
            if not opf_path or opf_path not in names:
                errors.append("container.xml não aponta para um OPF existente")

        if opf_path and opf_path in names:
            opf = parse_xml(archive.read(opf_path), opf_path, errors)
        else:
            opf = None

        if opf is not None:
            title = opf.findtext("opf:metadata/dc:title", default="", namespaces=NS).strip()
            creator = opf.findtext("opf:metadata/dc:creator", default="", namespaces=NS).strip()
            language = opf.findtext("opf:metadata/dc:language", default="", namespaces=NS).strip()
            identifier = opf.findtext("opf:metadata/dc:identifier", default="", namespaces=NS).strip()
            if not title:
                errors.append("dc:title vazio")
            if creator != AUTHOR:
                errors.append(f'dc:creator deve ser exatamente "{AUTHOR}"')
            if language != "pt-BR":
                errors.append('dc:language deve ser "pt-BR"')
            if not identifier:
                errors.append("dc:identifier vazio")
            if title and creator == AUTHOR and language == "pt-BR" and identifier:
                checks.append(f'metadados essenciais presentes: "{title}", {AUTHOR}, pt-BR')

            manifest: dict[str, tuple[str, str]] = {}
            cover_ids: list[str] = []
            nav_ids: list[str] = []
            for item in opf.findall("opf:manifest/opf:item", NS):
                item_id = item.get("id", "")
                href = item.get("href", "")
                properties = item.get("properties", "").split()
                manifest[item_id] = (href, item.get("media-type", ""))
                full_path = join_from(opf_path, href)
                if full_path not in names:
                    errors.append(f"item do manifesto ausente no ZIP: {full_path}")
                if "cover-image" in properties:
                    cover_ids.append(item_id)
                if "nav" in properties:
                    nav_ids.append(item_id)

            if len(cover_ids) != 1:
                errors.append(f"esperado 1 cover-image; encontrado(s) {len(cover_ids)}")
            if len(nav_ids) != 1:
                errors.append(f"esperado 1 documento nav; encontrado(s) {len(nav_ids)}")

            spine_ids = [item.get("idref", "") for item in opf.findall("opf:spine/opf:itemref", NS)]
            for item_id in spine_ids:
                if item_id not in manifest:
                    errors.append(f"spine referencia id inexistente: {item_id}")
            if cover_ids and cover_ids[0] in spine_ids:
                errors.append("imagem de capa entrou no spine; isso pode duplicar a capa no Kindle")
            else:
                checks.append("capa não possui página HTML duplicada no spine")

            if cover_ids and cover_ids[0] in manifest:
                cover_href, cover_media = manifest[cover_ids[0]]
                cover_path = join_from(opf_path, cover_href)
                if cover_media != "image/jpeg":
                    errors.append("cover-image não está declarada como image/jpeg")
                if cover_path in names:
                    cover_data = archive.read(cover_path)
                    if not cover_data.startswith(b"\xff\xd8"):
                        errors.append("cover-image não contém JPEG válido")
                    elif Image is None:
                        warnings.append("Pillow ausente: dimensões e modo de cor da capa não foram verificados")
                    else:
                        try:
                            with Image.open(BytesIO(cover_data)) as image:
                                if image.size != (1600, 2560):
                                    errors.append(f"capa mede {image.width}x{image.height}; esperado 1600x2560")
                                if image.mode != "RGB":
                                    errors.append(f"capa está em modo {image.mode}; esperado RGB")
                            size_mb = len(cover_data) / (1024 * 1024)
                            if size_mb > 5:
                                warnings.append(f"capa tem {size_mb:.2f} MB; prefira até 5 MB")
                            checks.append("capa JPEG RGB 1600x2560 incorporada")
                        except OSError as exc:
                            errors.append(f"não foi possível decodificar a capa: {exc}")

            if nav_ids and nav_ids[0] in manifest:
                nav_href = manifest[nav_ids[0]][0]
                nav_path = join_from(opf_path, nav_href)
                if nav_path in names:
                    nav = parse_xml(archive.read(nav_path), nav_path, errors)
                    toc_navs = [] if nav is None else [
                        node for node in nav.findall(".//xhtml:nav", NS)
                        if "toc" in node.get(EPUB_TYPE, "").split()
                    ]
                    if not toc_navs:
                        errors.append("documento nav não contém nav epub:type=toc")
                    else:
                        links = toc_navs[0].findall(".//xhtml:a", NS)
                        if not links:
                            errors.append("sumário lógico está vazio")
                        for link in links:
                            href = link.get("href", "")
                            target = join_from(nav_path, href)
                            if not href or target not in names:
                                errors.append(f"link de sumário inválido: {href or '[vazio]'}")
                        checks.append(f"sumário lógico com {len(links)} links válidos")

            for item_id, (href, media_type) in manifest.items():
                if media_type == "application/xhtml+xml":
                    full_path = join_from(opf_path, href)
                    if full_path in names:
                        parse_xml(archive.read(full_path), full_path, errors)
            if not any("XML inválido" in error for error in errors):
                checks.append("documentos XML/XHTML bem formados")

    if args.manuscript:
        try:
            actual = count_words(args.manuscript.read_text(encoding="utf-8-sig"))
            if actual != args.target:
                errors.append(f"manuscrito tem {actual} palavras; esperado {args.target}")
            else:
                checks.append(f"manuscrito com exatamente {actual} palavras de prosa")
        except OSError as exc:
            errors.append(f"não foi possível ler o manuscrito: {exc}")

    if warnings:
        for warning in warnings:
            print(f"AVISO: {warning}")
    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        print(f"FALHOU: {len(errors)} erro(s), {len(warnings)} aviso(s)", file=sys.stderr)
        return 1
    for check in checks:
        print(f"OK: {check}")
    print(f"PASSOU: {args.epub.resolve()} — {len(checks)} verificações, {len(warnings)} aviso(s)")
    print("OBSERVAÇÃO: ainda é necessária inspeção de renderização no Kindle Previewer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
