#!/usr/bin/env python3
"""Compose an exact-text 1600x2560 RGB JPEG cover over generated artwork."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError:  # pragma: no cover
    print("ERRO: Pillow é necessário. Instale com: python -m pip install Pillow", file=sys.stderr)
    raise SystemExit(2)

WIDTH, HEIGHT = 1600, 2560
AUTHOR = "Kang Arin"


def find_font(explicit: str | None, bold: bool) -> str:
    if explicit:
        path = Path(explicit)
        if not path.is_file():
            raise FileNotFoundError(f"fonte não encontrada: {path}")
        return str(path)
    windows = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
    names = (
        ["georgiab.ttf", "timesbd.ttf", "arialbd.ttf", "DejaVuSerif-Bold.ttf"]
        if bold
        else ["georgia.ttf", "times.ttf", "arial.ttf", "DejaVuSerif.ttf"]
    )
    for name in names:
        candidate = windows / name
        if candidate.is_file():
            return str(candidate)
        try:
            ImageFont.truetype(name, 24)
            return name
        except OSError:
            pass
    raise FileNotFoundError("nenhuma fonte TrueType adequada foi encontrada")


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=font, stroke_width=0)
    return box[2] - box[0]


def wrap_words(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.strip().split()
    if not words:
        return []
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        trial = f"{current} {word}"
        if text_width(draw, trial, font) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def fit_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_path: str,
    max_size: int,
    min_size: int,
    max_width: int,
    max_height: int,
    max_lines: int,
) -> tuple[ImageFont.FreeTypeFont, list[str], int]:
    for size in range(max_size, min_size - 1, -2):
        font = ImageFont.truetype(font_path, size)
        lines = wrap_words(draw, text, font, max_width)
        spacing = max(14, int(size * 0.18))
        line_height = draw.textbbox((0, 0), "Ágj", font=font, stroke_width=2)[3]
        height = len(lines) * line_height + max(0, len(lines) - 1) * spacing
        if len(lines) <= max_lines and height <= max_height and all(
            text_width(draw, line, font) <= max_width for line in lines
        ):
            return font, lines, spacing
    raise ValueError("o texto não cabe na capa; encurte título/subtítulo ou informe outra fonte")


def add_readability_gradient(image: Image.Image) -> Image.Image:
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(HEIGHT):
        top_alpha = int(178 * max(0.0, 1.0 - y / 1120.0) ** 1.65)
        bottom_alpha = int(150 * max(0.0, (y - 1760.0) / 800.0) ** 1.35)
        alpha = max(top_alpha, bottom_alpha)
        if alpha:
            for x in range(WIDTH):
                pixels[x, y] = (0, 0, 0, alpha)
    return Image.alpha_composite(image.convert("RGBA"), overlay)


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    start_y: int,
    spacing: int,
    fill: str,
    stroke_width: int,
) -> int:
    y = start_y
    for line in lines:
        box = draw.textbbox((0, 0), line, font=font, stroke_width=stroke_width)
        w, h = box[2] - box[0], box[3] - box[1]
        x = (WIDTH - w) // 2
        draw.text(
            (x, y - box[1]),
            line,
            font=font,
            fill=fill,
            stroke_width=stroke_width,
            stroke_fill="#111111",
        )
        y += h + spacing
    return y


def main() -> int:
    parser = argparse.ArgumentParser(description="Cria capa JPEG 1600x2560 com texto exato para KDP.")
    parser.add_argument("artwork", type=Path, help="arte de fundo sem texto")
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--author", default=AUTHOR)
    parser.add_argument("--font", help="fonte TrueType/OpenType do título")
    parser.add_argument("--author-font", help="fonte TrueType/OpenType de subtítulo/autora")
    parser.add_argument("--text-color", default="#FFF9ED")
    args = parser.parse_args()

    if args.author.strip() != AUTHOR:
        print(f'ERRO: a autora desta skill deve ser exatamente "{AUTHOR}".', file=sys.stderr)
        return 2
    if not args.title.strip():
        print("ERRO: título vazio.", file=sys.stderr)
        return 2

    try:
        with Image.open(args.artwork) as source:
            source.load()
            base = ImageOps.fit(source.convert("RGB"), (WIDTH, HEIGHT), method=Image.Resampling.LANCZOS)
        cover = add_readability_gradient(base)
        draw = ImageDraw.Draw(cover)
        title_font_path = find_font(args.font, bold=True)
        secondary_font_path = find_font(args.author_font, bold=False)

        title_font, title_lines, title_spacing = fit_block(
            draw, args.title.strip(), title_font_path, 220, 72, 1360, 760, 4
        )
        title_height = sum(
            draw.textbbox((0, 0), line, font=title_font, stroke_width=4)[3]
            for line in title_lines
        ) + max(0, len(title_lines) - 1) * title_spacing
        title_y = max(170, 690 - title_height // 2)
        end_y = draw_centered_lines(
            draw, title_lines, title_font, title_y, title_spacing, args.text_color, 4
        )

        if args.subtitle.strip():
            subtitle_font, subtitle_lines, subtitle_spacing = fit_block(
                draw, args.subtitle.strip(), secondary_font_path, 74, 38, 1280, 260, 3
            )
            draw_centered_lines(
                draw,
                subtitle_lines,
                subtitle_font,
                end_y + 56,
                subtitle_spacing,
                args.text_color,
                2,
            )

        author_font, author_lines, author_spacing = fit_block(
            draw, AUTHOR.upper(), title_font_path, 104, 58, 1250, 170, 2
        )
        author_box = draw.textbbox((0, 0), "Ágj", font=author_font, stroke_width=3)
        author_h = len(author_lines) * (author_box[3] - author_box[1]) + max(0, len(author_lines) - 1) * author_spacing
        draw_centered_lines(
            draw,
            author_lines,
            author_font,
            HEIGHT - 190 - author_h,
            author_spacing,
            args.text_color,
            3,
        )

        args.output.parent.mkdir(parents=True, exist_ok=True)
        rgb = cover.convert("RGB")
        quality = 94
        while True:
            rgb.save(args.output, "JPEG", quality=quality, optimize=True, progressive=True, dpi=(300, 300))
            if args.output.stat().st_size <= 5 * 1024 * 1024 or quality <= 78:
                break
            quality -= 4
    except (OSError, ValueError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 2

    size_mb = args.output.stat().st_size / (1024 * 1024)
    print(f"PASSOU: {args.output.resolve()} — {WIDTH}x{HEIGHT}px, RGB JPEG, {size_mb:.2f} MB, autora {AUTHOR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
