from __future__ import annotations

import os
from pathlib import Path


def detect_environment() -> str:
    if os.getenv("CODEX_ENV", "").lower() == "cloud":
        return "cloud"
    if os.getenv("OPENAI_ENV", "").lower() == "cloud":
        return "cloud"
    return "local"


def read_input_text(input_path: str) -> str:
    return Path(input_path).read_text(encoding="utf-8")


def write_output_bytes(output_path: str, payload: bytes) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return path


def default_output_dir(skill_root: Path) -> Path:
    preferred = os.getenv("SERMON_OUTPUT_DIR", "").strip()
    if preferred:
        return Path(preferred)
    return skill_root.parent / "outputs" if detect_environment() == "cloud" else skill_root.parent / "outputs"
