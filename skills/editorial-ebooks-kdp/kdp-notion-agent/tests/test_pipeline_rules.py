from __future__ import annotations

import json
import sys
import tempfile
from datetime import date
from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from docx_renderer import Section, _extract_effect_phrase, render_markdown_docx
from notion_client import NotionClient, NotionConfig
from package_builder import build_final_package, resolve_package_title, validate_workspace
from run_agent import (
    apply_profile_reasoning,
    build_checkpoint,
    build_push_updates_preview,
    count_stage_feedback_attempts,
    duration_seconds,
    list_runs,
)


class PipelineRulesTests(unittest.TestCase):
    def test_source_selection_prefers_corrigido(self) -> None:
        client = NotionClient(NotionConfig(token="x", database_id="y"))
        page = {
            "properties": {
                "Corrigido": {"files": [{"name": "a.txt"}]},
                "Transcrições": {"files": [{"name": "b.txt"}]},
                "DATA": {"type": "date", "date": {"start": "2025-01-01"}},
            }
        }
        self.assertEqual(client.select_editorial_source(page, requested_property="AUTO"), "Corrigido")

    def test_page_with_status_executando_or_pronto_is_not_eligible(self) -> None:
        client = NotionClient(NotionConfig(token="x", database_id="y"))
        page_executando = {
            "properties": {
                "Status": {"type": "select", "select": {"name": "Executando"}},
                "Corrigido": {"files": [{"name": "a.txt"}]},
            }
        }
        eligible_exec, _ = client.is_page_eligible_for_next_ebook(page_executando)
        self.assertFalse(eligible_exec)

        page_pronto = {
            "properties": {
                "Status": {"type": "select", "select": {"name": "Pronto"}},
                "Corrigido": {"files": [{"name": "a.txt"}]},
            }
        }
        eligible_pronto, _ = client.is_page_eligible_for_next_ebook(page_pronto)
        self.assertFalse(eligible_pronto)

    def test_source_selection_allows_transcricoes_only_before_cutoff(self) -> None:
        client = NotionClient(NotionConfig(token="x", database_id="y"))
        page_old = {
            "properties": {
                "Transcrições": {"files": [{"name": "b.txt"}]},
                "DATA": {"type": "date", "date": {"start": "2024-09-30"}},
            }
        }
        self.assertEqual(
            client.select_editorial_source(page_old, requested_property="AUTO", cutoff_date=date(2024, 10, 1)),
            "Transcrições",
        )

        page_new = {
            "properties": {
                "Transcrições": {"files": [{"name": "b.txt"}]},
                "DATA": {"type": "date", "date": {"start": "2024-10-15"}},
            }
        }
        with self.assertRaises(ValueError):
            client.select_editorial_source(page_new, requested_property="AUTO", cutoff_date=date(2024, 10, 1))

    def test_checkpoint_policy_changes_with_profile(self) -> None:
        self.assertEqual(build_checkpoint("book_blueprint", "premium")["type"], "approve")
        self.assertEqual(build_checkpoint("transcription_correction", "economico")["type"], "skip")
        self.assertEqual(build_checkpoint("chapter_writing", "premium")["type"], "skip")
        self.assertEqual(build_checkpoint("cta_subagent", "premium")["type"], "select")
        self.assertEqual(apply_profile_reasoning("high", "economico"), "medium")

    def test_validate_workspace_requires_framing_sections_above_500_words(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "output").mkdir()
            manifest = {
                "title": "Teste",
                "files": {
                    "raw_transcription": "01_raw_transcricao.txt",
                    "corrected_transcription": "02_corrigido.txt",
                    "sermon_summary": "03_resumo_sermao.md",
                    "ebook_blueprint": "04_blueprint_ebook.md",
                    "editorial_report": "05_relatorio_editorial.md",
                    "ebook_markdown": "06_ebook.md",
                    "landing_html": "07_landing.html",
                    "bonus_markdown": "08_bonus.md",
                    "kdp_metadata": "09_metadata_kdp.json",
                    "cta_report": "10_relatorio_cta.json",
                },
            }
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            (ws / "01_raw_transcricao.txt").write_text("base", encoding="utf-8")
            (ws / "02_corrigido.txt").write_text("corrigido", encoding="utf-8")
            (ws / "03_resumo_sermao.md").write_text("# Resumo", encoding="utf-8")
            (ws / "04_blueprint_ebook.md").write_text("# Blueprint", encoding="utf-8")
            (ws / "05_relatorio_editorial.md").write_text("# Relatorio", encoding="utf-8")
            long_block = " ".join(["palavra"] * 550)
            short_block = " ".join(["palavra"] * 300)
            ebook = (
                "# Teste\n\n"
                f"## Prefácio\n\n{short_block}\n\n"
                f"## Introdução\n\n{long_block}\n\n"
                f"## Capítulo 1\n\n{long_block}\n\n"
                f"## Conclusão\n\n{long_block}\n"
            )
            (ws / "06_ebook.md").write_text(ebook, encoding="utf-8")
            (ws / "07_landing.html").write_text("<html></html>", encoding="utf-8")
            (ws / "08_bonus.md").write_text("# Bonus", encoding="utf-8")
            (ws / "09_metadata_kdp.json").write_text("{}", encoding="utf-8")
            (ws / "10_relatorio_cta.json").write_text("{}", encoding="utf-8")

            issues = validate_workspace(ws, min_words=1500)
            self.assertTrue(any("Prefácio" in issue for issue in issues))

    def test_validate_workspace_rejects_appendix_in_ebook(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "output").mkdir()
            manifest = {
                "title": "Teste",
                "files": {
                    "raw_transcription": "01_raw_transcricao.txt",
                    "corrected_transcription": "02_corrigido.txt",
                    "sermon_summary": "03_resumo_sermao.md",
                    "ebook_blueprint": "04_blueprint_ebook.md",
                    "editorial_report": "05_relatorio_editorial.md",
                    "ebook_markdown": "06_ebook.md",
                    "landing_html": "07_landing.html",
                    "bonus_markdown": "08_bonus.md",
                    "kdp_metadata": "09_metadata_kdp.json",
                    "cta_report": "10_relatorio_cta.json",
                },
            }
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            (ws / "01_raw_transcricao.txt").write_text("base", encoding="utf-8")
            (ws / "02_corrigido.txt").write_text("corrigido", encoding="utf-8")
            (ws / "03_resumo_sermao.md").write_text("# Resumo", encoding="utf-8")
            (ws / "04_blueprint_ebook.md").write_text("# Blueprint", encoding="utf-8")
            (ws / "05_relatorio_editorial.md").write_text("# Relatorio", encoding="utf-8")
            block = " ".join(["palavra"] * 550)
            ebook = (
                "# Teste\n\n"
                f"## Prefácio\n\n{block}\n\n"
                f"## Introdução\n\n{block}\n\n"
                f"## Capítulo 1: Base\n\n{block}\n\n"
                f"## Conclusão\n\n{block}\n\n"
                f"## Apêndice\n\n{block}\n"
            )
            (ws / "06_ebook.md").write_text(ebook, encoding="utf-8")
            (ws / "07_landing.html").write_text("<html></html>", encoding="utf-8")
            (ws / "08_bonus.md").write_text("# Bonus", encoding="utf-8")
            (ws / "09_metadata_kdp.json").write_text("{}", encoding="utf-8")
            (ws / "10_relatorio_cta.json").write_text("{}", encoding="utf-8")

            issues = validate_workspace(ws, min_words=1500)
            self.assertTrue(any("bônus/guia/devocional/desafio/apêndice" in issue for issue in issues))

    def test_validate_workspace_rejects_chapter_below_800_words(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "output").mkdir()
            manifest = {
                "title": "Teste",
                "files": {
                    "raw_transcription": "01_raw_transcricao.txt",
                    "corrected_transcription": "02_corrigido.txt",
                    "sermon_summary": "03_resumo_sermao.md",
                    "ebook_blueprint": "04_blueprint_ebook.md",
                    "editorial_report": "05_relatorio_editorial.md",
                    "ebook_markdown": "06_ebook.md",
                    "landing_html": "07_landing.html",
                    "bonus_markdown": "08_bonus.md",
                    "kdp_metadata": "09_metadata_kdp.json",
                    "cta_report": "10_relatorio_cta.json",
                },
            }
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            (ws / "01_raw_transcricao.txt").write_text("base", encoding="utf-8")
            (ws / "02_corrigido.txt").write_text("corrigido", encoding="utf-8")
            (ws / "03_resumo_sermao.md").write_text("# Resumo", encoding="utf-8")
            (ws / "04_blueprint_ebook.md").write_text("# Blueprint", encoding="utf-8")
            (ws / "05_relatorio_editorial.md").write_text("# Relatorio", encoding="utf-8")
            long_block = " ".join(["palavra"] * 550)
            short_chapter = " ".join(["palavra"] * 400)
            ebook = (
                "# Teste\n\n"
                f"## Prefácio\n\n{long_block}\n\n"
                f"## Introdução\n\n{long_block}\n\n"
                f"## Capítulo 1: Curto\n\n{short_chapter}\n\n"
                f"## Conclusão\n\n{long_block}\n"
            )
            (ws / "06_ebook.md").write_text(ebook, encoding="utf-8")
            (ws / "07_landing.html").write_text("<html></html>", encoding="utf-8")
            (ws / "08_bonus.md").write_text("# Bonus", encoding="utf-8")
            (ws / "09_metadata_kdp.json").write_text("{}", encoding="utf-8")
            (ws / "10_relatorio_cta.json").write_text("{}", encoding="utf-8")

            issues = validate_workspace(ws, min_words=1500)
            self.assertTrue(any("Capítulo 'Capítulo 1: Curto'" in issue or "Capítulo 1: Curto" in issue for issue in issues))

    def test_validate_workspace_rejects_generic_title_and_weak_subtitle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "output").mkdir()
            manifest = {
                "title": "Teste",
                "files": {
                    "raw_transcription": "01_raw_transcricao.txt",
                    "corrected_transcription": "02_corrigido.txt",
                    "sermon_summary": "03_resumo_sermao.md",
                    "ebook_blueprint": "04_blueprint_ebook.md",
                    "editorial_report": "05_relatorio_editorial.md",
                    "ebook_markdown": "06_ebook.md",
                    "landing_html": "07_landing.html",
                    "bonus_markdown": "08_bonus.md",
                    "kdp_metadata": "09_metadata_kdp.json",
                    "cta_report": "10_relatorio_cta.json",
                },
            }
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            (ws / "01_raw_transcricao.txt").write_text("base", encoding="utf-8")
            (ws / "02_corrigido.txt").write_text("corrigido", encoding="utf-8")
            (ws / "03_resumo_sermao.md").write_text("# Resumo", encoding="utf-8")
            (ws / "04_blueprint_ebook.md").write_text("# Blueprint", encoding="utf-8")
            (ws / "05_relatorio_editorial.md").write_text("# Relatorio", encoding="utf-8")
            block = " ".join(["palavra"] * 550)
            ebook = (
                "# Guia de oração prática\n\n"
                f"## Prefácio\n\n{block}\n\n"
                f"## Introdução\n\n{block}\n\n"
                f"## Capítulo 1: Base\n\n{block}\n\n"
                f"## Conclusão\n\n{block}\n"
            )
            (ws / "06_ebook.md").write_text(ebook, encoding="utf-8")
            (ws / "07_landing.html").write_text("<html></html>", encoding="utf-8")
            (ws / "08_bonus.md").write_text("# Bonus", encoding="utf-8")
            (ws / "09_metadata_kdp.json").write_text(
                json.dumps(
                    {
                        "titulo": "Guia de oração prática",
                        "subtitulo": "Como viver melhor",
                        "autor": "Filipe Ivo Pereira",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (ws / "10_relatorio_cta.json").write_text("{}", encoding="utf-8")

            issues = validate_workspace(ws, min_words=1500)
            self.assertTrue(any("parece genérico" in issue for issue in issues))
            self.assertTrue(any("Subtítulo do ebook precisa ter entre" in issue for issue in issues))
            self.assertTrue(any("Subtítulo do ebook deve seguir" in issue for issue in issues))

    def test_validate_workspace_rejects_title_mismatch_between_metadata_and_h1(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "output").mkdir()
            manifest = {
                "title": "Teste",
                "files": {
                    "raw_transcription": "01_raw_transcricao.txt",
                    "corrected_transcription": "02_corrigido.txt",
                    "sermon_summary": "03_resumo_sermao.md",
                    "ebook_blueprint": "04_blueprint_ebook.md",
                    "editorial_report": "05_relatorio_editorial.md",
                    "ebook_markdown": "06_ebook.md",
                    "landing_html": "07_landing.html",
                    "bonus_markdown": "08_bonus.md",
                    "kdp_metadata": "09_metadata_kdp.json",
                    "cta_report": "10_relatorio_cta.json",
                },
            }
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            (ws / "01_raw_transcricao.txt").write_text("base", encoding="utf-8")
            (ws / "02_corrigido.txt").write_text("corrigido", encoding="utf-8")
            (ws / "03_resumo_sermao.md").write_text("# Resumo", encoding="utf-8")
            (ws / "04_blueprint_ebook.md").write_text("# Blueprint", encoding="utf-8")
            (ws / "05_relatorio_editorial.md").write_text("# Relatorio", encoding="utf-8")
            block = " ".join(["palavra"] * 550)
            ebook = (
                "# Outro título\n\n"
                f"## Prefácio\n\n{block}\n\n"
                f"## Introdução\n\n{block}\n\n"
                f"## Capítulo 1: Base\n\n{block}\n\n"
                f"## Conclusão\n\n{block}\n"
            )
            (ws / "06_ebook.md").write_text(ebook, encoding="utf-8")
            (ws / "07_landing.html").write_text("<html></html>", encoding="utf-8")
            (ws / "08_bonus.md").write_text("# Bonus", encoding="utf-8")
            (ws / "09_metadata_kdp.json").write_text(
                json.dumps(
                    {
                        "titulo": "Quando o desespero bate à porta",
                        "subtitulo": "Um guia bíblico e prático para conduzir sua casa pela fé",
                        "autor": "Filipe Ivo Pereira",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (ws / "10_relatorio_cta.json").write_text("{}", encoding="utf-8")

            issues = validate_workspace(ws, min_words=1500)
            self.assertTrue(any("diverge do título editorial" in issue for issue in issues))

    def test_validate_workspace_accepts_strong_title_and_subtitle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "output").mkdir()
            manifest = {
                "title": "Teste",
                "files": {
                    "raw_transcription": "01_raw_transcricao.txt",
                    "corrected_transcription": "02_corrigido.txt",
                    "sermon_summary": "03_resumo_sermao.md",
                    "ebook_blueprint": "04_blueprint_ebook.md",
                    "editorial_report": "05_relatorio_editorial.md",
                    "ebook_markdown": "06_ebook.md",
                    "landing_html": "07_landing.html",
                    "bonus_markdown": "08_bonus.md",
                    "kdp_metadata": "09_metadata_kdp.json",
                    "cta_report": "10_relatorio_cta.json",
                },
            }
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            (ws / "01_raw_transcricao.txt").write_text("base", encoding="utf-8")
            (ws / "02_corrigido.txt").write_text("corrigido", encoding="utf-8")
            (ws / "03_resumo_sermao.md").write_text("# Resumo", encoding="utf-8")
            (ws / "04_blueprint_ebook.md").write_text("# Blueprint", encoding="utf-8")
            (ws / "05_relatorio_editorial.md").write_text("# Relatorio", encoding="utf-8")
            block = " ".join(["palavra"] * 550)
            title = "Quando o desespero bate à porta"
            ebook = (
                f"# {title}\n\n"
                f"## Prefácio\n\n{block}\n\n"
                f"## Introdução\n\n{block}\n\n"
                f"## Capítulo 1: Base\n\n{block}\n\n"
                f"## Conclusão\n\n{block}\n"
            )
            (ws / "06_ebook.md").write_text(ebook, encoding="utf-8")
            (ws / "07_landing.html").write_text("<html></html>", encoding="utf-8")
            (ws / "08_bonus.md").write_text("# Bonus", encoding="utf-8")
            (ws / "09_metadata_kdp.json").write_text(
                json.dumps(
                    {
                        "titulo": title,
                        "subtitulo": "Um guia bíblico e prático para conduzir sua casa pela fé quando o medo parece ter a última palavra",
                        "autor": "Filipe Ivo Pereira",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (ws / "10_relatorio_cta.json").write_text("{}", encoding="utf-8")

            issues = validate_workspace(ws, min_words=1500)
            joined = "\n".join(issues)
            self.assertNotIn("Título do ebook", joined)
            self.assertNotIn("Subtítulo do ebook", joined)

    def test_docx_contains_word_toc_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "test.docx"
            block = " ".join(["texto"] * 550)
            md = (
                "# Teste\n\n"
                f"## Prefácio\n\n{block}\n\n"
                f"## Introdução\n\n{block}\n\n"
                f"## Capítulo 1\n\n{block}\n\n"
                f"### Subtitulo\n\n{block}\n\n"
                f"## Conclusão\n\n{block}\n"
            )
            render_markdown_docx(md, out, fallback_title="Teste")
            with zipfile.ZipFile(out) as docx:
                xml = docx.read("word/document.xml").decode("utf-8", errors="ignore")
            self.assertIn('TOC \\o "1-3"', xml)

    def test_docx_renders_markdown_italics_as_times_new_roman_for_biblical_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "test-italico.docx"
            block = " ".join(["texto"] * 550)
            md = (
                "# Teste\n\n"
                f"## Prefácio\n\n{block}\n\n"
                f"## Introdução\n\n{block}\n\n"
                "## Capítulo 1\n\n"
                f"Antes da citação {block}.\n\n"
                'Como afirma Paulo em Romanos 8.28: *"Sabemos que em todas as coisas Deus age para o bem daqueles que o amam."*\n\n'
                f"Depois da citação {block}.\n\n"
                f"## Conclusão\n\n{block}\n"
            )
            render_markdown_docx(md, out, fallback_title="Teste")
            with zipfile.ZipFile(out) as docx:
                xml = docx.read("word/document.xml").decode("utf-8", errors="ignore")
            self.assertIn("Times New Roman", xml)
            self.assertIn("<w:i/>", xml)

    def test_effect_phrase_max_200_chars(self) -> None:
        section = Section(
            "Capítulo 1: Teste",
            ['<!-- EFEITO: A graça encontra você na dor, quebra o medo, reposiciona sua fé e chama você a agir agora. -->'],
        )
        _, phrase = _extract_effect_phrase(section)
        self.assertLessEqual(len(phrase), 200)

    def test_push_preview_contains_ia_agente(self) -> None:
        preview = build_push_updates_preview()
        self.assertIn("IA Agente", preview)
        self.assertIn("Status", preview)

    def test_feedback_cycle_count_uses_events(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "runs" / "run-1").mkdir(parents=True)
            (ws / "manifest.json").write_text(json.dumps({"run_id": "run-1"}, ensure_ascii=False), encoding="utf-8")
            events = [
                {"event_type": "stage_started", "details": {"stage": "book_blueprint"}},
                {"event_type": "checkpoint_feedback", "details": {"stage": "book_blueprint"}},
                {"event_type": "checkpoint_feedback", "details": {"stage": "book_blueprint", "chapter": "Capítulo 1"}},
            ]
            (ws / "runs" / "run-1" / "events.jsonl").write_text(
                "\n".join(json.dumps(item, ensure_ascii=False) for item in events),
                encoding="utf-8",
            )
            self.assertEqual(count_stage_feedback_attempts(ws, "book_blueprint", chapter_name=None), 2)
            self.assertEqual(count_stage_feedback_attempts(ws, "book_blueprint", chapter_name="Capítulo 1"), 1)

    def test_list_runs_parses_state_and_duration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ws = root / "ebook-a"
            (ws / "runs" / "run-1").mkdir(parents=True)
            manifest = {"page_id": "pg-1", "execution_profile": "premium", "run_id": "run-1"}
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            state = {
                "run_id": "run-1",
                "page_id": "pg-1",
                "status": "completed",
                "stage_current": "push",
                "execution_profile": "premium",
                "ia_agente": "codex",
                "started_at": "2026-03-21T10:00:00",
                "ended_at": "2026-03-21T10:01:00",
            }
            (ws / "runs" / "run-1" / "state.json").write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")

            report = list_runs(root, page_id="pg-1", limit=10)
            self.assertEqual(report["count"], 1)
            self.assertEqual(report["items"][0]["duration_seconds"], 60)
            self.assertEqual(duration_seconds("2026-03-21T10:00:00", "2026-03-21T10:00:00"), 0)

    def test_resolve_package_title_accepts_titulo_and_builds_docx_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            (ws / "output").mkdir()
            manifest = {
                "title": "Titulo original",
                "files": {
                    "raw_transcription": "01_raw_transcricao.txt",
                    "corrected_transcription": "02_corrigido.txt",
                    "sermon_summary": "03_resumo_sermao.md",
                    "ebook_blueprint": "04_blueprint_ebook.md",
                    "editorial_report": "05_relatorio_editorial.md",
                    "ebook_markdown": "06_ebook.md",
                },
            }
            (ws / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
            (ws / "09_metadata_kdp.json").write_text(
                json.dumps({"titulo": "Quando o desespero bate à porta"}, ensure_ascii=False),
                encoding="utf-8",
            )

            title = resolve_package_title(ws, manifest)
            package = build_final_package(ws)

            self.assertEqual(title, "Quando o desespero bate à porta")
            self.assertTrue(package.files["ebook_docx"].name.endswith(".docx"))
            self.assertTrue(package.files["bonus_docx"].name.endswith("Bonus.docx"))
            self.assertIn("Quando o desespero bate à porta", package.files["ebook_docx"].name)


if __name__ == "__main__":
    unittest.main()
