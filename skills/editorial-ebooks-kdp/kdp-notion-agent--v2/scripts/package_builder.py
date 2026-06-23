from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from contracts import FinalPackage


MANDATORY_FILES = {
    "raw_transcription": "01_raw_transcricao.txt",
    "corrected_transcription": "02_corrigido.txt",
    "sermon_summary": "03_resumo_sermao.md",
    "ebook_blueprint": "04_blueprint_ebook.md",
    "editorial_report": "05_relatorio_editorial.md",
    "ebook_markdown": "06_ebook.md",
}
OPTIONAL_FILES = {
    "landing_html": "07_landing.html",
    "bonus_markdown": "08_bonus.md",
    "kdp_metadata": "09_metadata_kdp.json",
    "cta_report": "10_relatorio_cta.json",
}
ALL_ARTIFACT_KEYS = frozenset(OPTIONAL_FILES)
MIN_FRAMING_SECTION_WORDS = 501
MIN_CHAPTER_WORDS = 800
REQUIRED_FRAMING_SECTIONS = ("prefácio", "introdução", "conclusão")
DISALLOWED_EBOOK_SECTION_TOKENS = (
    "bônus",
    "bonus",
    "guia",
    "devocional",
    "devocionais",
    "desafio",
    "desafios",
    "apêndice",
    "apendice",
    "plano de leitura",
    "checklist",
)
COMMON_DEACCENTED_TOKENS = (
    " nao ",
    " sermao ",
    " capitulo ",
    " capitulos ",
    " introducao ",
    " conclusao ",
    " prefacio ",
    " voce ",
    " coracao ",
    " oracao ",
    " bencao ",
    " fisico ",
    " fisica ",
    " correcao ",
)
COMMON_CORRUPTED_PTBR_TOKENS = (
    " fsico ",
    " fisicao ",
    " correo ",
    " correes ",
    " correc ",
)

def load_manifest(workspace: Path) -> dict[str, Any]:
    return json.loads((workspace / "manifest.json").read_text(encoding="utf-8-sig"))


def build_final_package(workspace: Path) -> FinalPackage:
    manifest_path = workspace / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest não encontrado em {manifest_path}.")
    manifest = load_manifest(workspace)
    file_map = dict(manifest["files"])
    file_map.setdefault("cta_subagent", "11_cta_subagent.json")
    file_map.setdefault("cta_subagent_brief", "12_cta_subagent_brief.md")
    file_map.setdefault("stage_strategy", "13_stage_strategy.md")
    file_map.setdefault("model_routing", "14_model_routing.json")
    title = resolve_package_title(workspace, manifest)
    file_map["ebook_docx"] = str(Path("output") / build_named_docx_filename(title))
    file_map["bonus_docx"] = str(Path("output") / build_named_docx_filename(title, suffix="Bonus"))
    files = {name: workspace / rel_path for name, rel_path in file_map.items()}
    return FinalPackage(workspace=workspace, manifest_path=manifest_path, files=files, metadata=manifest)


def validate_workspace(workspace: Path, *, min_words: int = 15000) -> list[str]:
    package = build_final_package(workspace)
    issues: list[str] = []
    for key, expected_name in MANDATORY_FILES.items():
        file_path = package.files[key]
        if not file_path.exists():
            issues.append(f"Arquivo obrigatório ausente: {expected_name}")
    if issues:
        return issues

    corrected = package.files["corrected_transcription"].read_text(encoding="utf-8-sig").strip()
    ebook = package.files["ebook_markdown"].read_text(encoding="utf-8-sig").strip()
    editorial_report = package.files["editorial_report"].read_text(encoding="utf-8-sig").strip()
    if not corrected:
        issues.append("02_corrigido.txt está vazio.")
    issues.extend(_detect_possible_encoding_loss(corrected, file_label="02_corrigido.txt"))
    if not ebook.startswith("# "):
        issues.append("06_ebook.md precisa começar com `# Título`.")
    if "## " not in ebook:
        issues.append("06_ebook.md precisa conter headings `##` para as seções do livro.")
    issues.extend(_detect_possible_encoding_loss(ebook, file_label="06_ebook.md"))
    if not editorial_report:
        issues.append("05_relatorio_editorial.md está vazio.")
    issues.extend(_detect_possible_encoding_loss(editorial_report, file_label="05_relatorio_editorial.md"))
    word_count = count_words(ebook)
    if word_count < min_words:
        issues.append(f"06_ebook.md está abaixo do mínimo: {word_count} palavras úteis (mínimo {min_words}).")
    issues.extend(_find_disallowed_ebook_sections(ebook))
    issues.extend(_validate_has_body_chapters(ebook))
    framing_counts = extract_heading_word_counts(ebook)
    for section_name in REQUIRED_FRAMING_SECTIONS:
        words = framing_counts.get(section_name, 0)
        if words < MIN_FRAMING_SECTION_WORDS:
            issues.append(
                f"Seção '{section_name.title()}' precisa ter mais de 500 palavras (atual: {words})."
            )
    for section_name, words in framing_counts.items():
        if section_name in _FRAMING_AND_META_HEADINGS:
            continue
        if words < MIN_CHAPTER_WORDS:
            issues.append(
                f"Capítulo '{section_name.title()}' precisa ter no mínimo {MIN_CHAPTER_WORDS} palavras (atual: {words})."
            )
    kdp_path = package.files["kdp_metadata"]
    if kdp_path.exists() and not _looks_like_json(kdp_path):
        issues.append("09_metadata_kdp.json não contém JSON válido.")
    cta_path = package.files["cta_report"]
    if cta_path.exists() and not _looks_like_json(cta_path):
        issues.append("10_relatorio_cta.json não contém JSON válido.")
    return issues


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text, flags=re.UNICODE))


def extract_heading_word_counts(markdown_text: str) -> dict[str, int]:
    normalized = markdown_text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.split("\n")
    counts: dict[str, int] = {}
    current_heading: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        nonlocal current_heading, buffer
        if current_heading:
            counts[current_heading] = count_words("\n".join(buffer))
        current_heading = None
        buffer = []

    for line in lines:
        if line.startswith("## "):
            flush()
            current_heading = normalize_heading(line[3:].strip())
            continue
        # Also accept level-1 headings for framing sections (Prefácio, Introdução, Conclusão)
        if line.startswith("# ") and not line.startswith("## "):
            candidate = normalize_heading(line[2:].strip())
            # Only treat as section boundary if it's a known framing section
            framing_keys = {"prefácio", "introdução", "conclusão", "sobre o autor"}
            candidate_base = candidate.split(":")[0].strip()
            if candidate_base in framing_keys:
                flush()
                current_heading = candidate_base
                continue
        if current_heading is not None:
            buffer.append(line)
    flush()
    return counts


def normalize_heading(text: str) -> str:
    lowered = text.casefold()
    lowered = lowered.replace("prefacio", "prefácio")
    lowered = lowered.replace("introducao", "introdução")
    lowered = lowered.replace("conclusao", "conclusão")
    lowered = lowered.replace("capitulo", "capítulo")
    return lowered.strip()


def _looks_like_json(path: Path) -> bool:
    try:
        json.loads(path.read_text(encoding="utf-8-sig"))
        return True
    except Exception:
        return False


def build_named_docx_filename(title: str, *, suffix: str | None = None) -> str:
    safe_title = sanitize_windows_filename(title)
    if suffix:
        safe_suffix = sanitize_windows_filename(suffix)
        return f"{safe_title} - {safe_suffix}.docx"
    return f"{safe_title}.docx"


def resolve_package_title(workspace: Path, manifest: dict[str, Any]) -> str:
    metadata_title = _read_metadata_title(workspace / "09_metadata_kdp.json")
    if metadata_title:
        return metadata_title
    markdown_title = _read_markdown_title(workspace / "06_ebook.md")
    if markdown_title:
        return markdown_title
    return str(manifest.get("title") or "ebook").strip()


def sanitize_windows_filename(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\\\|?*]+', " ", value).strip().rstrip(".")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "ebook"


def _read_metadata_title(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return ""
    return str(payload.get("title") or "").strip()


def _read_markdown_title(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except Exception:
        return ""
    return ""


def _detect_possible_encoding_loss(text: str, *, file_label: str) -> list[str]:
    normalized = f" {text.casefold()} "
    suspicious_hits = [token.strip() for token in COMMON_DEACCENTED_TOKENS if token in normalized]
    suspicious_hits.extend(token.strip() for token in COMMON_CORRUPTED_PTBR_TOKENS if token in normalized)
    accent_chars = re.findall(r"[áàãâéêíóôõúç]", normalized, flags=re.IGNORECASE)
    if not suspicious_hits:
        return []
    if accent_chars and len(suspicious_hits) < 3 and not any(hit in {"fsico", "correo", "correc", "fisico", "correcao"} for hit in suspicious_hits):
        return []
    return [
        f"{file_label} parece ter perdido acentos/caracteres especiais de PT-BR. "
        f"Tokens suspeitos encontrados: {', '.join(sorted(set(suspicious_hits))[:8])}."
    ]


def _find_disallowed_ebook_sections(ebook_text: str) -> list[str]:
    for line in ebook_text.splitlines():
        if not line.startswith("## "):
            continue
        heading = line[3:].strip().casefold()
        for token in DISALLOWED_EBOOK_SECTION_TOKENS:
            if token in heading:
                return [
                    "06_ebook.md não pode conter seções de bônus/guia/devocional/desafio/apêndice; use 08_bonus.md."
                ]
    return []


_FRAMING_AND_META_HEADINGS = frozenset({"prefácio", "introdução", "conclusão", "sobre o autor"})


def _validate_has_body_chapters(ebook_text: str) -> list[str]:
    for line in ebook_text.splitlines():
        if not line.startswith("## "):
            continue
        heading = normalize_heading(line[3:].strip())
        if heading not in _FRAMING_AND_META_HEADINGS:
            return []
    return [
        "06_ebook.md precisa conter ao menos um capítulo de conteúdo além das seções de enquadramento "
        "(Prefácio, Introdução, Conclusão) para que o sumário do Word tenha títulos dos capítulos."
    ]

