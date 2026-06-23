#!/usr/bin/env python3
"""Create a formatted .docx preaching-series document and enforce a minimum word count.

Input is a UTF-8 text or markdown file with simple conventions:
- "# " for title
- "## " and "### " for headings
- "- " for bullets
- blank lines separate paragraphs
"""

import argparse
import shutil
import sys
from pathlib import Path

from adapters import read_input_text, write_output_bytes
from core import load_config, render_docx_bytes


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to UTF-8 text or markdown series plan")
    parser.add_argument("--output", required=True, help="Path to output .docx file")
    parser.add_argument("--min-words", type=int, default=0, help="Minimum allowed word count")
    parser.add_argument(
        "--config",
        default=str(Path(__file__).with_name("config.json")),
        help="Path to configuration json",
    )
    parser.add_argument(
        "--docs-dir",
        default=str(Path(__file__).resolve().parents[2] / "DOCS_Sermons"),
        help="Directory where the final .docx copy will be stored",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    text = read_input_text(args.input)
    config = load_config(Path(args.config))
    payload, word_count = render_docx_bytes(text, config)

    if word_count < args.min_words:
        print(
            f"Word count check failed: manuscript has {word_count} words, minimum is {args.min_words}.",
            file=sys.stderr,
        )
        return 1

    output_path = write_output_bytes(args.output, payload)

    docs_dir = Path(args.docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)
    final_docx_path = docs_dir / Path(output_path).name
    shutil.copy2(output_path, final_docx_path)

    print(f"Created {output_path} with {word_count} words.")
    print(f"Copied final docx to {final_docx_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
