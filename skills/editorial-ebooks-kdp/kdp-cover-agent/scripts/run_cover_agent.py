from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont, ImageOps


TARGET_SIZE = (1536, 2208)
MAX_COVER_BYTES = 5 * 1024 * 1024
DEFAULT_AUTHOR = "Filipe Ivo Pereira"
DEFAULT_OUTPUT_ROOT = Path(r"C:\Users\filip\DEV\capas")
SKILL_ROOT = Path(__file__).resolve().parents[1]
TITLE_FONT_CANDIDATES = (
    r"C:\Windows\Fonts\ariblk.ttf",
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\bahnschrift.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
)
SUBTITLE_FONT_CANDIDATES = (
    r"C:\Windows\Fonts\georgia.ttf",
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\times.ttf",
)
AUTHOR_FONT_CANDIDATES = (
    r"C:\Windows\Fonts\arial.ttf",
    r"C:\Windows\Fonts\georgia.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
)


@dataclass
class CoverSpec:
    workspace: Path
    prompt_path: Path
    output_path: Path
    title: str
    subtitle: str
    author: str


@dataclass
class TextBlock:
    lines: list[str]
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont
    tracking: int
    line_height: int
    gap: int
    width: int
    height: int


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "prepare":
        prompt_path = prepare_cover_artifacts(Path(args.workspace))
        print(prompt_path)
        return 0

    if args.command == "import-generated":
        output_path = import_generated_cover(Path(args.workspace), Path(args.source) if args.source else None)
        print(output_path)
        return 0

    if args.command == "healthcheck":
        issues = run_healthcheck()
        if issues:
            for issue in issues:
                print(f"- {issue}")
            return 1
        print("Healthcheck OK.")
        return 0

    raise SystemExit(f"Comando nao suportado: {args.command}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fluxo independente de capa para ebooks KDP.")
    sub = parser.add_subparsers(dest="command", required=True)

    prepare = sub.add_parser("prepare", help="Gera o briefing operacional da capa para a conversa.")
    prepare.add_argument("--workspace", required=True)

    import_generated = sub.add_parser("import-generated", help="Importa a imagem mais recente gerada na conversa.")
    import_generated.add_argument("--workspace", required=True)
    import_generated.add_argument("--source")

    sub.add_parser("healthcheck", help="Valida a estrutura basica da skill.")
    return parser


def prepare_cover_artifacts(workspace: Path) -> Path:
    spec = resolve_cover_spec(workspace)
    spec.output_path.parent.mkdir(parents=True, exist_ok=True)
    spec.prompt_path.write_text(build_prompt_document(spec), encoding="utf-8")
    return spec.prompt_path


def import_generated_cover(workspace: Path, source_path: Path | None = None) -> Path:
    spec = resolve_cover_spec(workspace)
    selected_source = source_path or find_latest_generated_image()
    if not selected_source.exists():
        raise FileNotFoundError(f"Arquivo de imagem nao encontrado: {selected_source}")
    spec.output_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(selected_source) as source:
        base = ImageOps.fit(
            source.convert("RGB"),
            TARGET_SIZE,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
    composed = apply_cover_layout(base, spec)
    save_cover_jpeg(composed, spec.output_path)
    return spec.output_path


def run_healthcheck() -> list[str]:
    issues: list[str] = []
    required = [
        SKILL_ROOT / "SKILL.md",
        SKILL_ROOT / "references" / "gpt-image-2-operating-rules.md",
        SKILL_ROOT / "references" / "cover-design-playbook.md",
        SKILL_ROOT / "scripts" / "run_cover_agent.py",
    ]
    for path in required:
        if not path.exists():
            issues.append(f"Arquivo obrigatorio ausente: {path}")
    if not any(Path(candidate).exists() for candidate in TITLE_FONT_CANDIDATES):
        issues.append("Nenhuma fonte forte para titulo foi encontrada nas fontes padrao do Windows.")
    try:
        ensure_output_root()
    except Exception as exc:
        issues.append(f"Nao foi possivel preparar a pasta de saida das capas: {exc}")
    return issues


def resolve_cover_spec(workspace: Path) -> CoverSpec:
    workspace = workspace.resolve()
    manifest = load_json(workspace / "manifest.json")
    metadata = load_json(workspace / "09_metadata_kdp.json")
    title = (
        str(metadata.get("titulo") or metadata.get("title") or "").strip()
        or read_markdown_title(workspace / "06_ebook.md")
        or str(manifest.get("title") or "").strip()
        or "ebook"
    )
    subtitle = str(metadata.get("subtitulo") or metadata.get("subtitle") or "").strip()
    author = DEFAULT_AUTHOR
    output_name = f"{sanitize_windows_filename(title)} - Capa.jpg"
    output_root = ensure_output_root()
    return CoverSpec(
        workspace=workspace,
        prompt_path=workspace / "16_capa_prompt.md",
        output_path=output_root / output_name,
        title=title,
        subtitle=subtitle,
        author=author,
    )


def build_prompt_document(spec: CoverSpec) -> str:
    return (
        "# Prompt da Capa\n\n"
        "Use a ferramenta `image_gen` nesta conversa para gerar a arte-base da capa. Nao use API.\n\n"
        "## Contrato operacional GPT Image\n\n"
        "- seguir o fluxo conversacional, com refinamentos incrementais quando necessario\n"
        "- pedir uma arte vertical em `1536x2208`\n"
        "- manter fundo opaco\n"
        "- tratar como capa `digital-first`\n"
        "- assumir sempre que este projeto e de nao ficcao\n"
        "- tratar explicitamente como capa de nao ficcao crista / espiritualidade pratica\n"
        "- seguir linguagem visual de capas best sellers da categoria, com acabamento comercial premium\n"
        "- nao renderizar texto, letras, palavras, titulo ou nome do autor na imagem\n"
        "- reservar espaco negativo para tipografia no topo e na base\n"
        "- priorizar 1 foco visual dominante e contraste forte\n\n"
        "## Texto final aplicado localmente\n\n"
        f"- Titulo: {spec.title.upper()}\n"
        f"- Subtitulo: {normalize_subtitle_case(spec.subtitle) or '(sem subtitulo)'}\n"
        f"- Autor fixo da skill: {spec.author}\n\n"
        "## Direcao visual obrigatoria\n\n"
        "- a capa deve parecer livro que vende, nao experimento artistico isolado\n"
        "- usar convencoes visuais de best sellers sem copiar capa especifica\n"
        "- priorizar leitura imediata, categoria clara e impacto comercial em thumbnail\n\n"
        "## Regras de nao ficcao incorporadas\n\n"
        "- titulo e subtitulo sao o centro da comunicacao da capa\n"
        "- o titulo deve parecer dominante e memoravel, com peso visual de best seller\n"
        "- se houver subtitulo, ele deve soar explicativo e orientado a beneficio\n"
        "- preferir simbolo unico, metafora visual forte ou imagem simples com muito espaco negativo\n"
        "- evitar cena complexa, colagem e excesso de detalhes que somem em miniatura\n"
        "- a imagem precisa continuar legivel mentalmente em algo proximo de `120-160 px` de altura\n\n"
        "## Prompt base para a arte\n\n"
        f"{build_cover_image_prompt(spec)}\n\n"
        "## Prompts de refinamento\n\n"
        "- Preserve a composicao principal e aumente o contraste para thumbnail, com cara de best seller premium.\n"
        "- Mantenha o simbolo central e abra mais espaco negativo no topo e no rodape para tipografia forte.\n"
        "- Mantenha a paleta e a atmosfera, mas simplifique o fundo para leitura comercial imediata de nao ficcao.\n\n"
        "## Saida esperada\n\n"
        f"- Pasta final das capas: `{spec.output_path.parent}`\n"
        f"- Arquivo final local: `{spec.output_path}`\n"
        "- Formato final: `JPEG`\n"
        "- Limite final: `5 MB`\n"
    )


def build_cover_image_prompt(spec: CoverSpec) -> str:
    subtitle = normalize_subtitle_case(spec.subtitle)
    subtitle_clause = f" Subtitulo editorial de apoio: {subtitle}." if subtitle else ""
    return (
        "Arte de fundo premium para capa vertical de ebook cristao de nao ficcao em portugues, sempre tratada como "
        "nao ficcao e nunca como ficcao, pensada para conversao "
        "digital-first em thumbnail. A direcao visual deve seguir a linguagem de best sellers da categoria, com "
        "acabamento comercial premium, categoria legivel em segundos, autoridade percebida e impacto forte de vitrine. "
        "A capa deve comunicar assunto, promessa e genero de forma imediata. Interpretar o "
        "titulo do livro de forma simbolica, emocional e comercial, "
        "com um unico foco visual dominante, contraste forte, profundidade real e espaco negativo utilizavel para "
        "tipografia. Nao renderizar nenhuma letra, palavra, assinatura, logotipo ou texto. "
        "A imagem precisa comunicar categoria em segundos e sustentar a promessa do livro sem poluicao visual. "
        "Aplicar o framework CROWN, a hierarquia 60/25/15, paleta controlada e leitura clara em miniatura. "
        "Preferir simbolo unico ou metafora visual forte em vez de cena complexa. "
        "Evitar visual de arte conceitual vaga, capa amadora, excesso de elementos ou composicao sem categoria clara. "
        "A imagem deve parecer vendavel ao lado de outros best sellers de nao ficcao do nicho. "
        f"Titulo editorial: {spec.title}.{subtitle_clause} Autor fixo impresso depois: {spec.author}. "
        "Tema cristao, atmosfera contemporanea, acabamento premium."
    )


def apply_cover_layout(image: Image.Image, spec: CoverSpec) -> Image.Image:
    canvas = add_readability_overlay(image)
    draw = ImageDraw.Draw(canvas)
    width, height = canvas.size

    title_text = spec.title.upper().strip()
    subtitle_text = normalize_subtitle_case(spec.subtitle)
    author_text = spec.author.strip()

    title_block = fit_text_block(
        draw,
        text=title_text,
        font_candidates=TITLE_FONT_CANDIDATES,
        max_width=int(width * 0.78),
        max_height=int(height * 0.30),
        min_size=86,
        max_size=220,
        max_lines=4,
        tracking=8,
        gap_ratio=0.22,
    )
    title_top = int(height * 0.15)
    draw_text_block(
        canvas,
        title_block,
        top=title_top,
        fill=(248, 245, 238, 255),
        stroke_fill=(18, 18, 18, 255),
        stroke_width=5,
        shadow_offset=5,
        shadow_fill=(0, 0, 0, 150),
    )

    current_top = title_top + title_block.height + int(height * 0.035)
    if subtitle_text:
        subtitle_block = fit_text_block(
            draw,
            text=subtitle_text,
            font_candidates=SUBTITLE_FONT_CANDIDATES,
            max_width=int(width * 0.72),
            max_height=int(height * 0.15),
            min_size=34,
            max_size=70,
            max_lines=3,
            tracking=0,
            gap_ratio=0.28,
        )
        draw_text_block(
            canvas,
            subtitle_block,
            top=current_top,
            fill=(245, 240, 230, 255),
            stroke_fill=(20, 20, 20, 255),
            stroke_width=2,
            shadow_offset=3,
            shadow_fill=(0, 0, 0, 120),
        )

    author_block = fit_text_block(
        draw,
        text=author_text,
        font_candidates=AUTHOR_FONT_CANDIDATES,
        max_width=int(width * 0.72),
        max_height=int(height * 0.06),
        min_size=28,
        max_size=52,
        max_lines=1,
        tracking=1,
        gap_ratio=0.20,
    )
    author_top = height - int(height * 0.12)
    draw_text_block(
        canvas,
        author_block,
        top=author_top,
        fill=(240, 235, 225, 255),
        stroke_fill=(15, 15, 15, 255),
        stroke_width=2,
        shadow_offset=2,
        shadow_fill=(0, 0, 0, 110),
    )
    return canvas


def add_readability_overlay(image: Image.Image) -> Image.Image:
    width, height = image.size
    alpha = Image.new("L", (1, height))
    for y in range(height):
        top_strength = max(0.0, 1.0 - (y / (height * 0.42)))
        bottom_anchor = (y - height * 0.60) / (height * 0.40)
        bottom_strength = max(0.0, bottom_anchor)
        value = int(min(230, top_strength * 150 + bottom_strength * 195))
        alpha.putpixel((0, y), value)
    alpha = alpha.resize((width, height))
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay.putalpha(alpha)
    base = image.convert("RGBA")
    return Image.alpha_composite(base, overlay)


def fit_text_block(
    draw: ImageDraw.ImageDraw,
    *,
    text: str,
    font_candidates: tuple[str, ...],
    max_width: int,
    max_height: int,
    min_size: int,
    max_size: int,
    max_lines: int,
    tracking: int,
    gap_ratio: float,
) -> TextBlock:
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        raise ValueError("Texto vazio nao pode virar bloco tipografico.")
    for size in range(max_size, min_size - 1, -2):
        font = load_font(font_candidates, size)
        lines = wrap_text(draw, cleaned, font, max_width=max_width, tracking=tracking)
        if len(lines) > max_lines:
            continue
        line_heights = [measure_line_height(draw, line, font) for line in lines]
        gap = max(4, int(size * gap_ratio))
        total_height = sum(line_heights) + gap * (len(lines) - 1)
        total_width = max(measure_line_width(draw, line, font, tracking) for line in lines)
        if total_width <= max_width and total_height <= max_height:
            return TextBlock(
                lines=lines,
                font=font,
                tracking=tracking,
                line_height=max(line_heights),
                gap=gap,
                width=total_width,
                height=total_height,
            )
    font = load_font(font_candidates, min_size)
    lines = wrap_text(draw, cleaned, font, max_width=max_width, tracking=tracking)
    lines = lines[:max_lines]
    line_heights = [measure_line_height(draw, line, font) for line in lines]
    gap = max(4, int(min_size * gap_ratio))
    total_height = sum(line_heights) + gap * (len(lines) - 1)
    total_width = max(measure_line_width(draw, line, font, tracking) for line in lines)
    return TextBlock(
        lines=lines,
        font=font,
        tracking=tracking,
        line_height=max(line_heights),
        gap=gap,
        width=total_width,
        height=total_height,
    )


def draw_text_block(
    image: Image.Image,
    block: TextBlock,
    *,
    top: int,
    fill: tuple[int, int, int, int],
    stroke_fill: tuple[int, int, int, int],
    stroke_width: int,
    shadow_offset: int,
    shadow_fill: tuple[int, int, int, int],
) -> None:
    draw = ImageDraw.Draw(image)
    y = top
    for line in block.lines:
        line_width = measure_line_width(draw, line, block.font, block.tracking)
        x = int((image.width - line_width) / 2)
        draw_tracked_text(
            draw,
            x=x + shadow_offset,
            y=y + shadow_offset,
            text=line,
            font=block.font,
            fill=shadow_fill,
            tracking=block.tracking,
            stroke_width=0,
            stroke_fill=None,
        )
        draw_tracked_text(
            draw,
            x=x,
            y=y,
            text=line,
            font=block.font,
            fill=fill,
            tracking=block.tracking,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        y += measure_line_height(draw, line, block.font) + block.gap


def draw_tracked_text(
    draw: ImageDraw.ImageDraw,
    *,
    x: int,
    y: int,
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: tuple[int, int, int, int],
    tracking: int,
    stroke_width: int,
    stroke_fill: tuple[int, int, int, int] | None,
) -> None:
    cursor = x
    for char in text:
        bbox = draw.textbbox((cursor, y), char, font=font, stroke_width=stroke_width)
        draw.text(
            (cursor, y),
            char,
            font=font,
            fill=fill,
            stroke_width=stroke_width,
            stroke_fill=stroke_fill,
        )
        char_width = bbox[2] - bbox[0]
        cursor += char_width + tracking


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    *,
    max_width: int,
    tracking: int,
) -> list[str]:
    words = text.split()
    if not words:
        return []
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if measure_line_width(draw, candidate, font, tracking) <= max_width:
            current = candidate
            continue
        lines.append(current)
        current = word
    lines.append(current)
    return lines


def measure_line_width(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    tracking: int,
) -> int:
    if not text:
        return 0
    total = 0
    for index, char in enumerate(text):
        bbox = draw.textbbox((0, 0), char, font=font)
        total += bbox[2] - bbox[0]
        if index < len(text) - 1:
            total += tracking
    return total


def measure_line_height(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
) -> int:
    bbox = draw.textbbox((0, 0), text or "Ag", font=font)
    return bbox[3] - bbox[1]


def load_font(candidates: tuple[str, ...], size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def save_cover_jpeg(image: Image.Image, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rgb = image.convert("RGB")
    for quality in (92, 88, 84, 80, 76, 72, 68, 64, 60, 56, 52):
        buffer = BytesIO()
        rgb.save(
            buffer,
            format="JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
            subsampling=0,
        )
        payload = buffer.getvalue()
        if len(payload) <= MAX_COVER_BYTES:
            output_path.write_bytes(payload)
            return output_path
    raise RuntimeError("Nao foi possivel comprimir a capa final para menos de 5 MB.")


def find_latest_generated_image() -> Path:
    candidates = list_generated_image_candidates(limit=1)
    if not candidates:
        raise RuntimeError(
            "Nenhuma imagem gerada foi encontrada em generated_images. Gere a arte aqui na conversa antes do import."
        )
    return candidates[0]


def list_generated_image_candidates(*, limit: int = 10) -> list[Path]:
    roots = candidate_generated_image_roots()
    extensions = {".png", ".jpg", ".jpeg", ".webp"}
    candidates: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in extensions:
                candidates.append(path)
    candidates.sort(key=lambda item: item.stat().st_mtime, reverse=True)
    return candidates[:limit]


def candidate_generated_image_roots() -> list[Path]:
    roots: list[Path] = []
    env_root = os.environ.get("CODEX_HOME")
    if env_root:
        roots.append(Path(env_root) / "generated_images")
    roots.append(Path.home() / ".codex" / "generated_images")
    roots.append(Path.home() / ".Codex" / "generated_images")
    deduped: list[Path] = []
    seen: set[str] = set()
    for root in roots:
        key = str(root).casefold()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(root)
    return deduped


def normalize_subtitle_case(text: str) -> str:
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return ""
    if cleaned.isupper():
        cleaned = cleaned.casefold()
    return cleaned[0].upper() + cleaned[1:]


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def read_markdown_title(path: Path) -> str:
    if not path.exists():
        return ""
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def sanitize_windows_filename(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\\\|?*]+', " ", value).strip().rstrip(".")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "ebook"


def ensure_output_root() -> Path:
    raw_root = os.environ.get("KDP_COVER_OUTPUT_DIR")
    output_root = Path(raw_root) if raw_root else DEFAULT_OUTPUT_ROOT
    output_root.mkdir(parents=True, exist_ok=True)
    return output_root.resolve()


if __name__ == "__main__":
    raise SystemExit(main())
