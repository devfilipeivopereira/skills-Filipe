#!/usr/bin/env python3
"""Create a formatted .docx motivational talk document and enforce a minimum word count.

Input is a UTF-8 text or markdown file with simple conventions:
- "# " for title
- "## " and "### " for headings
- "- " for bullets
- blank lines separate paragraphs
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

from adapters import read_input_text, write_output_bytes
from core import load_config, render_docx_bytes


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to UTF-8 text or markdown talk manuscript")
    parser.add_argument("--output", required=True, help="Path to output .docx file")
    parser.add_argument("--min-words", type=int, default=0, help="Minimum allowed word count")
    parser.add_argument(
        "--config",
        default=str(Path(__file__).with_name("config.json")),
        help="Path to configuration json",
    )
    parser.add_argument(
        "--docs-dir",
        default=str(Path(__file__).resolve().parents[2] / "DOCS_Talks"),
        help="Directory where the final .docx copy will be stored",
    )
    parser.add_argument(
        "--reference",
        default="",
        help="Theme or reference for the talk; used to organize the final docx into a subfolder",
    )
    return parser.parse_args(argv)


def sanitize_filename_part(value: str) -> str:
    cleaned = re.sub(r"[^\w]+", "_", value.strip(), flags=re.UNICODE)
    cleaned = re.sub(r"_+", "_", cleaned, flags=re.UNICODE).strip("_")
    return cleaned or "Sem_Referencia"


def infer_reference_from_output(output_path: Path) -> str:
    stem_tokens = [token for token in output_path.stem.split("_") if token]
    skill_name = Path(__file__).resolve().parents[1].name
    slug = skill_name.removeprefix("generate-").removesuffix("-talks")
    speaker_tokens = [token for token in slug.replace("-", "_").split("_") if token]
    if stem_tokens and speaker_tokens:
        normalized_stem = [token.lower() for token in stem_tokens]
        normalized_speaker = [token.lower() for token in speaker_tokens]
        if len(normalized_stem) > len(normalized_speaker) and normalized_stem[-len(normalized_speaker):] == normalized_speaker:
            return "_".join(stem_tokens[:-len(speaker_tokens)])
    return output_path.stem


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
    reference_folder = sanitize_filename_part(args.reference or infer_reference_from_output(Path(output_path)))
    final_docs_dir = docs_dir / reference_folder
    final_docs_dir.mkdir(parents=True, exist_ok=True)
    final_docx_path = final_docs_dir / Path(output_path).name
    shutil.copy2(output_path, final_docx_path)

    print(f"Created {output_path} with {word_count} words.")
    print(f"Copied final docx to {final_docx_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
