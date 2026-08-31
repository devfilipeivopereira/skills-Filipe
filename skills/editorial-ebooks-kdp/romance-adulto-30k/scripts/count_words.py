#!/usr/bin/env python3
"""Count fictional prose words in a Markdown manuscript deterministically."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WORD_RE = re.compile(r"[^\W_]+(?:[’'\-][^\W_]+)*", re.UNICODE)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}(?:\s+|$)")
DIVIDER_RE = re.compile(r"^\s{0,3}(?:(?:\*\s*){3,}|(?:-\s*){3,}|(?:_\s*){3,})$")
FENCE_RE = re.compile(r"^\s{0,3}(```+|~~~+)")


def prose_text(markdown: str) -> str:
    """Return only countable prose, excluding Markdown scaffolding."""
    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    kept: list[str] = []
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_fence = False
    fence_marker = ""

    for index, line in enumerate(lines):
        stripped = line.strip()
        if in_frontmatter:
            if index > 0 and stripped in {"---", "..."}:
                in_frontmatter = False
            continue

        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence or HEADING_RE.match(line) or DIVIDER_RE.match(line):
            continue
        kept.append(line)

    return "\n".join(kept)


def count_words(markdown: str) -> int:
    return len(WORD_RE.findall(prose_text(markdown)))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Conta apenas as palavras de prosa ficcional de um manuscrito Markdown."
    )
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("--target", type=int, default=30000)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    try:
        raw = args.manuscript.read_text(encoding="utf-8-sig")
    except OSError as exc:
        print(f"ERRO: não foi possível ler {args.manuscript}: {exc}", file=sys.stderr)
        return 2

    actual = count_words(raw)
    difference = actual - args.target
    passed = difference == 0
    result = {
        "file": str(args.manuscript.resolve()),
        "words": actual,
        "target": args.target,
        "difference": difference,
        "passed": passed,
        "rule": "prosa; exclui front matter, cabeçalhos Markdown, divisores e blocos de código",
    }
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "PASSOU" if passed else "FALHOU"
        sign = "+" if difference > 0 else ""
        print(f"{status}: {actual:,} palavras; alvo {args.target:,}; diferença {sign}{difference}".replace(",", "."))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
