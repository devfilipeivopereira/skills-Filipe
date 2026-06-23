---
name: todos-os-pregadores
description: Use when generating sermons or talks across many preacher/speaker styles, producing one Markdown file per style and a final ZIP package.
---

# Todos os Pregadores

## Overview

Use this skill as the single uploadable hub for the embedded sermon, preaching, message, and motivational talk skills. It generates fresh Markdown outputs for each selected preacher or speaker style, then packages those `.md` files into one ZIP deliverable.

This skill is self-contained. Do not depend on external installed skills; use the embedded copies under `references/embedded-skills/`.

## Required First Question

Before writing any sermon or talk, ask once:

`Voce quer apenas o esboco ou a versao completa (sermao/palestra)?`

Rules:

- `Esboco`: generate only title, thesis, main movements, transitions, applications, and compact conclusion.
- `Completa`: generate the full manuscript according to each embedded method.
- If unclear, pause and confirm before drafting.
- In a batch, apply the answer to every selected style unless the user says otherwise.

## Inputs

Resolve these before drafting:

1. Source material:
   - Sermons: biblical reference, passage, theme, or sermon idea.
   - Talks: theme, audience, transformation goal, and delivery context.
2. Style scope:
   - If the user says `todos`, use every applicable individual style in `references/style_catalog.md`.
   - If the user names styles, use only those styles.
   - If the source is biblical, default to sermon/preacher styles.
   - If the source is motivational, corporate, leadership, training, or keynote, default to speaker/talk styles.
3. Audience and context. If missing, assume a general evangelical congregation for sermons or a mixed adult audience for talks.
4. Language. If missing, default to Brazilian Portuguese.
5. Length. If missing, use each embedded method's default for complete manuscripts; keep outlines compact.

## Embedded Method Use

Open `references/style_catalog.md` first. For each selected style:

1. Open the linked embedded `METHOD.md`.
2. Open the linked method/reference file when the embedded skill points to one.
3. Follow that method's structure, rhetoric, sequencing, and quality checks.
4. Preserve differences between styles. Do not flatten everything into one generic sermon or talk.
5. Generate fresh wording for the current request. Do not reuse old outputs, cached manuscripts, or prior drafts.

Use each source as a methodology reference, not as a script for impersonation. Do not claim the output is written by the real person; do not copy long distinctive passages from books, sermons, talks, or copyrighted material.

## Output Override

This top-level skill overrides conflicting delivery instructions inside embedded skills.

- Final deliverables are Markdown files plus one ZIP only.
- Do not create final `.docx`, `.epub`, `.pdf`, `.csv`, or `.xlsx` files unless the user explicitly asks after the Markdown batch is done.
- If an embedded skill references scripts for `.docx`, `.epub`, spreadsheets, cleanup, or local delivery folders, ignore those script and delivery steps.
- Create one `.md` file per selected style.
- Package all generated `.md` files and `manifest.json` into one final `.zip`.
- Do not include old outputs from embedded skills.

## Markdown File Contract

Each generated file must use this naming pattern:

`<source_slug>__<style_slug>.md`

Each file must contain:

```markdown
---
title: "<generated title>"
style: "<preacher or speaker style>"
source: "<biblical reference, passage, or talk theme>"
scope: "esboco" or "completa"
language: "<language>"
audience: "<audience/context>"
---

# <Title>

## Metodo aplicado
Briefly name the governing embedded method and the style-specific logic used.

## Preparacao
Declare thesis, central need/problem, transformation target, main movements, and any method-required setup.

## Conteudo
Write the outline or full manuscript according to the selected method.

## Checklist
- Freshly written for this request
- Method-specific structure preserved
- Applications are concrete
- No old output reused
```

## Packaging Workflow

1. Create a working folder under `outputs/<source_slug>/`.
2. Save every generated `.md` file into that folder.
3. Write `manifest.json` with source, scope, language, audience, selected styles, file names, skipped styles, and creation timestamp.
4. Run:

```bash
python scripts/package_markdown_batch.py --source outputs/<source_slug> --zip outputs/<source_slug>.zip
```

5. If script execution is unavailable, create the ZIP manually with only the generated `.md` files and `manifest.json`.
6. Report the absolute or downloadable path to the ZIP, the number of Markdown files, and any skipped style with a short reason.

## Quality Rules

- Produce distinct files, not one combined Markdown document.
- If a style is a helper/hub rather than an individual output style, use it for guidance but do not create a duplicate output unless the user asks.
- For all-current statistics, news, or contemporary illustrations, use available web research and keep source links in the working notes or in the relevant Markdown file.
- If the batch is too large for one response, continue file by file until the ZIP is complete.
- The task is complete only when the ZIP exists and contains the expected `.md` files.

## Useful References

- Style catalog: `references/style_catalog.md`
- Embedded original skills: `references/embedded-skills/`
- ZIP helper: `scripts/package_markdown_batch.py`
