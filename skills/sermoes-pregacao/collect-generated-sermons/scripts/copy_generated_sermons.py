from __future__ import annotations

import shutil
from pathlib import Path


SKILLS_ROOT = Path(r"C:\Users\filip\.codex\skills")
DESTINATION_DIR = Path(r"C:\Users\filip\OneDrive\Área de Trabalho\Sermoes_Gerados_Codex")


def target_name(skill_name: str, source_path: Path) -> str:
    base_name = skill_name.removeprefix("generate-") or skill_name
    return f"{base_name}{source_path.suffix.lower()}"


def iter_source_files(skills_root: Path) -> list[tuple[str, Path]]:
    sources: list[tuple[str, Path]] = []
    for skill_dir in sorted(skills_root.glob("generate-*")):
        if not skill_dir.is_dir():
            continue

        outputs_dir = skill_dir / "outputs"
        if not outputs_dir.is_dir():
            continue

        for docx_file in sorted(outputs_dir.glob("*.docx")):
            if docx_file.is_file():
                sources.append((skill_dir.name, docx_file))
    return sources


def main() -> int:
    DESTINATION_DIR.mkdir(parents=True, exist_ok=True)

    scanned_skills = [
        path for path in sorted(SKILLS_ROOT.glob("generate-*")) if path.is_dir()
    ]
    source_files = iter_source_files(SKILLS_ROOT)
    skills_with_files: list[str] = []
    skills_without_files: list[str] = []

    for skill_dir in scanned_skills:
        outputs_dir = skill_dir / "outputs"
        has_docx = outputs_dir.is_dir() and any(outputs_dir.glob("*.docx"))
        if has_docx:
            skills_with_files.append(skill_dir.name)
        else:
            skills_without_files.append(skill_dir.name)

    copied_count = 0
    skipped_count = 0

    print(f"Pastas de skills verificadas: {len(scanned_skills)}")
    print(f"Destino: {DESTINATION_DIR}")

    if not source_files:
        print("Nenhum arquivo .docx encontrado nas pastas outputs.")
        return 0

    for skill_name, source_path in source_files:
        destination_path = DESTINATION_DIR / target_name(skill_name, source_path)
        if destination_path.exists():
            skipped_count += 1
            print(f"[ignorado] {skill_name}: {source_path.name} -> {destination_path.name}")
            continue

        shutil.copy2(source_path, destination_path)
        copied_count += 1
        print(f"[copiado] {skill_name}: {source_path.name} -> {destination_path.name}")

    print("")
    print(f"Pastas com arquivos .docx: {len(skills_with_files)}")
    for skill_name in skills_with_files:
        print(f"  - {skill_name}")

    print(f"Pastas sem arquivos .docx: {len(skills_without_files)}")
    for skill_name in skills_without_files:
        print(f"  - {skill_name}")

    print("")
    print(f"Arquivos copiados: {copied_count}")
    print(f"Arquivos ignorados por já existirem: {skipped_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
