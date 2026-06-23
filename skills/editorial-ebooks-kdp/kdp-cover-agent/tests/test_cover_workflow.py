from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from run_cover_agent import (
    TARGET_SIZE,
    import_generated_cover,
    normalize_subtitle_case,
    prepare_cover_artifacts,
    resolve_cover_spec,
)


class CoverWorkflowTests(unittest.TestCase):
    def test_prepare_cover_artifacts_writes_prompt_with_gpt_image_rules(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            (workspace / "output").mkdir()
            output_dir = workspace / "capas"
            (workspace / "manifest.json").write_text(
                json.dumps({"title": "Titulo original", "page_id": "page-1"}, ensure_ascii=False),
                encoding="utf-8",
            )
            (workspace / "09_metadata_kdp.json").write_text(
                json.dumps(
                    {
                        "titulo": "Quando o desespero bate a porta",
                        "subtitulo": "UM GUIA BIBLICO E PRATICO PARA RESPIRAR DE NOVO",
                        "autor": "Filipe Ivo Pereira",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (workspace / "06_ebook.md").write_text("# Fallback", encoding="utf-8")

            with patch.dict("os.environ", {"KDP_COVER_OUTPUT_DIR": str(output_dir)}):
                prompt_path = prepare_cover_artifacts(workspace)
                prompt = prompt_path.read_text(encoding="utf-8")

            self.assertEqual(prompt_path.name, "16_capa_prompt.md")
            self.assertIn("1536x2208", prompt)
            self.assertIn("Nao use API", prompt)
            self.assertIn("nao renderizar texto", prompt.casefold())
            self.assertIn("QUANDO O DESESPERO BATE A PORTA", prompt)
            self.assertIn(str(output_dir), prompt)
            self.assertIn("Autor fixo da skill: Filipe Ivo Pereira", prompt)
            self.assertIn("best sellers", prompt)
            self.assertIn("nao ficcao", prompt)
            self.assertIn("assumir sempre que este projeto e de nao ficcao", prompt)
            self.assertIn("120-160 px", prompt)
            self.assertIn("simbolo unico", prompt)

    def test_import_generated_cover_creates_jpeg_with_target_size(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            (workspace / "output").mkdir()
            output_dir = workspace / "capas"
            (workspace / "manifest.json").write_text(
                json.dumps({"title": "Titulo original", "page_id": "page-1"}, ensure_ascii=False),
                encoding="utf-8",
            )
            (workspace / "09_metadata_kdp.json").write_text(
                json.dumps(
                    {
                        "titulo": "Quando o desespero bate a porta",
                        "subtitulo": "Um guia biblico e pratico para respirar de novo",
                        "autor": "Filipe Ivo Pereira",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (workspace / "06_ebook.md").write_text("# Fallback", encoding="utf-8")
            source = workspace / "source.png"
            Image.new("RGB", (1200, 1800), color=(44, 62, 87)).save(source, format="PNG")

            with patch.dict("os.environ", {"KDP_COVER_OUTPUT_DIR": str(output_dir)}):
                output_path = import_generated_cover(workspace, source)

            self.assertTrue(output_path.exists())
            self.assertLessEqual(output_path.stat().st_size, 5 * 1024 * 1024)
            self.assertEqual(output_path.parent, output_dir.resolve())
            with Image.open(output_path) as rendered:
                self.assertEqual(rendered.size, TARGET_SIZE)
                self.assertEqual(rendered.format, "JPEG")

    def test_resolve_cover_spec_uses_metadata_title_and_default_author(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            output_dir = workspace / "capas"
            (workspace / "manifest.json").write_text(
                json.dumps({"title": "Titulo original", "page_id": "page-1"}, ensure_ascii=False),
                encoding="utf-8",
            )
            (workspace / "09_metadata_kdp.json").write_text(
                json.dumps(
                    {
                        "titulo": "Abrigo para dias de incerteza",
                        "autor": "Outro Autor",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (workspace / "06_ebook.md").write_text("# Outro titulo", encoding="utf-8")

            with patch.dict("os.environ", {"KDP_COVER_OUTPUT_DIR": str(output_dir)}):
                spec = resolve_cover_spec(workspace)

            self.assertEqual(spec.title, "Abrigo para dias de incerteza")
            self.assertEqual(spec.author, "Filipe Ivo Pereira")
            self.assertTrue(spec.output_path.name.endswith("Capa.jpg"))
            self.assertEqual(spec.output_path.parent, output_dir.resolve())
            self.assertEqual(
                normalize_subtitle_case("UM GUIA BIBLICO E PRATICO PARA RESPIRAR"),
                "Um guia biblico e pratico para respirar",
            )


if __name__ == "__main__":
    unittest.main()
