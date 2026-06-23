---
name: translate-epubs-with-tbl
description: Use when the user asks to translate EPUB books with the local TranslateBooksWithLLMs installation and expects operational execution end-to-end.
---

# Translate EPUBs with TBL

## Overview
Use this skill to run EPUB translation with `hydropix/TranslateBooksWithLLMs` installed at `C:\Users\filip\TranslateBooksWithLLMs`.

## When to Use
- User asks to translate `.epub` files.
- User wants local translation with Ollama.
- User wants a repeatable translation command with consistent defaults.

## Preconditions
- Input file exists and has `.epub` extension.
- Project path exists: `C:\Users\filip\TranslateBooksWithLLMs`.
- Python venv exists: `C:\Users\filip\TranslateBooksWithLLMs\venv\Scripts\python.exe`.
- For local mode, Ollama endpoint is online: `http://127.0.0.1:11434`.

## Default Profile
- Provider: `ollama`
- Model: `qwen3:0.6b`
- API endpoint: `http://127.0.0.1:11434/api/generate`
- Source language: `English`
- Target language: `Portuguese`
- Quality defaults (always on unless explicitly disabled): `--text-cleanup` + `--refine`
- Assistant apply defaults: PT-BR naturalness post-pass enabled automatically when `LangTag` starts with `pt` (e.g. `pt-BR`)

## Command Template
```powershell
$env:PYTHONUTF8='1'
& "C:\Users\filip\TranslateBooksWithLLMs\venv\Scripts\python.exe" `
  "C:\Users\filip\TranslateBooksWithLLMs\translate.py" `
  -i "<INPUT_EPUB>" -sl "<SOURCE_LANG>" -tl "<TARGET_LANG>" `
  --provider ollama -m qwen3:0.6b `
  --api_endpoint http://127.0.0.1:11434/api/generate
```

## Optional Quality Flags
- `--text-cleanup` for OCR and punctuation cleanup.
- `--refine` for a second polish pass.
- `--glossary <path.json|path.csv>` for term consistency.
- `-SkipDefaultQualityFlags` to disable default quality flags in the fast runner when you need raw speed.

## Fast Runner Script
Use:
```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\filip\.gemini\skills\translate-epubs-with-tbl\scripts\run-epub-translation.ps1" `
  -InputFile "C:\path\book.epub" -SourceLang "English" -TargetLang "Portuguese"
```

Notes:
- This runner now applies `--text-cleanup` and `--refine` by default.
- Use `-SkipDefaultQualityFlags` only when explicitly requested.

## Assistant Chunk Workflow (No direct translation API call in this step)
Use this mode when you want the agent (chat) to translate in batches and then rebuild the EPUB.

### 1) Prepare tokenized workspace + chunks
```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\filip\.gemini\skills\translate-epubs-with-tbl\scripts\prepare-epub-assistant-workflow.ps1" `
  -InputFile "C:\path\book.epub" -ChunkChars 1800
```

This creates:
- `..._assistant_workflow_<timestamp>\chunks\chunk_0001.md` (chat-friendly batch)
- `..._assistant_workflow_<timestamp>\chunks\chunk_0001.jsonl` (structured source)
- `..._assistant_workflow_<timestamp>\nodes.jsonl` (node map)
- `..._assistant_workflow_<timestamp>\translations\translations_template.jsonl`

### 2) Translate each chunk in chat
For each chunk, return JSONL lines in this exact format:
```json
{"id":"T000001","target":"Texto traduzido"}
{"id":"T000002","target":"Outro texto traduzido"}
```

Save batch outputs as one or multiple `.jsonl` files in a folder, for example:
- `...\my_translations\chunk_0001.translated.jsonl`
- `...\my_translations\chunk_0002.translated.jsonl`

### 3) Apply translations and rebuild EPUB
```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\filip\.gemini\skills\translate-epubs-with-tbl\scripts\apply-epub-assistant-workflow.ps1" `
  -Workspace "C:\path\book_assistant_workflow_YYYYMMDD-HHMMSS" `
  -TranslationsPath "C:\path\my_translations" `
  -OutputFile "C:\path\book_ptBR_assistant.epub" `
  -LangTag "pt-BR" `
  -PtBrNaturalPass "auto"
```

Notes:
- `TranslationsPath` accepts either a single `.jsonl` file or a directory with multiple `.jsonl` files.
- The apply step fails fast if any `id` is missing.
- `PtBrNaturalPass` options: `auto|on|off`. Use `auto` as default. For `pt-*`, the pass is applied automatically.
- PT-BR natural pass normalizes common title/TOC leftovers in English and applies conservative fluency cleanup.

## Verification Checklist
- Confirm command exits with code `0`.
- Confirm output file exists.
- Confirm output file size is greater than zero.
- Confirm apply output reports `NATURAL_UPDATES` when PT-BR natural pass is enabled.
- Report the output path and elapsed duration.

## Troubleshooting
- Unicode error in Windows terminal: set `PYTHONUTF8=1` before running Python.
- `model not found`: run `C:\Users\filip\AppData\Local\Programs\Ollama\ollama.exe pull qwen3:0.6b`.
- Ollama offline: test `http://127.0.0.1:11434/api/tags` and restart Ollama.
