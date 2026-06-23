from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class RawTranscript:
    page_id: str
    title: str
    source_file_name: str
    text: str


@dataclass
class CorrectedTranscript:
    text: str
    word_count: int


@dataclass
class SermonScope:
    thesis: str
    main_text: str
    audience: str
    in_scope: list[str] = field(default_factory=list)
    out_of_scope: list[str] = field(default_factory=list)


@dataclass
class MessageMap:
    summary_path: Path
    blueprint_path: Path


@dataclass
class BookBlueprint:
    title: str
    subtitle: str
    chapters: list[str]


@dataclass
class CritiqueReport:
    approved: bool
    notes: str


@dataclass
class FinalPackage:
    workspace: Path
    manifest_path: Path
    files: dict[str, Path]
    metadata: dict[str, Any]


@dataclass
class StageRoute:
    stage: str
    model: str
    reasoning_effort: str
    context_files: list[str]
    justification: str
    execution_mode: str = "single-agent"
    profile: str = "premium"
    checkpoint: dict[str, str] = field(default_factory=lambda: {"type": "approve"})
    max_feedback_cycles: int = 2
