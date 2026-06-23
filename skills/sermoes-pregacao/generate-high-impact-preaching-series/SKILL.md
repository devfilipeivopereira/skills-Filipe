---
name: generate-high-impact-preaching-series
description: Generate complete high-impact preaching series plans using a multi-source planning system that combines Andy Stanley, Craig Groeschel, Ed Young Jr, Steven Furtick, Michael Todd, Rick Warren, Brian Jones, Eugene Lowry, Calvin Miller, Alyce McKenzie, Louie Giglio, and Lane Sebring. Use when the user asks to design a sermon series, preaching calendar arc, multi-week church teaching experience, high-impact series concept, launch plan, weekly preaching arc, series branding, or a church-wide teaching campaign based on a theme, calendar season, audience profile, or ministry context.
---

# Generate High Impact Preaching Series

## Overview

Generate a complete multi-week preaching series package, not just sermon topics. This skill builds a full series experience with title, arc, audience targeting, calendar positioning, weekly progression, creative identity, launch strategy, extension resources, and evaluation criteria. The default deliverable is a formatted Microsoft Word document.

Read [references/high_impact_preaching_series_method.md](references/high_impact_preaching_series_method.md) when planning or reviewing a series. Treat that file as the governing reference for audience strategy, annual planning logic, title testing, series arcs, creative packaging, launch timing, and critique questions.
Use [scripts/create_series_docx.py](scripts/create_series_docx.py) to convert the final series plan into a `.docx` file and enforce minimum word count before delivery.
Use [scripts/create_series_epub.py](scripts/create_series_epub.py) after the `.docx` is finalized to create the `.epub` file and clear the local working `outputs` folder.
Treat [scripts/core.py](scripts/core.py) as the portable document logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten this into a generic sermon-topic list. Preserve the transformation target, target listener, title testing, internal arc, launch logic, extension ecosystem, and evaluation cycle.
- If the user asks for a high-impact series, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the planning context:
   - proposed theme
   - church context
   - calendar season
   - congregation profile
   - special constraints
2. If the user did not provide those details, make reasonable assumptions and label them clearly.
3. Default to Brazilian Portuguese unless the user asks for another language.
4. Unless the user requests another output format, produce both `.docx` and `.epub`.
5. Unless the user explicitly requests another destination, save the source plan and the working `.docx` result inside [outputs/](outputs/) in this skill folder before copying the final `.docx` and creating the final `.epub`.

## Core Planning Rules

- Design a series as a journey, not a pile of related sermons.
- Build for at least four listener profiles:
  - seeker
  - returning
  - growing
  - established
- Give the seeker a front door and the established believer a ceiling for growth.
- Define one clear transformation for the person who completes the whole series.
- Ensure each week has a specific function in the arc.
- Make each week resolve something and leave a fresh tension for the next week.
- Match the series to the church calendar:
  - seeking season
  - settling season
  - high anticipation moments
  - summer or rotating attendance periods
- Create a title that works outside church culture.
- Extend the series beyond Sunday with a supporting ecosystem.
- If the user asks for a full series package and gives no shorter limit, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the detailed plan, explicitly declare:

1. The burden:
   - what truth or need is driving the series now
2. The target listener:
   - age
   - life stage
   - fears
   - hopes
   - distance from church or faith
3. The transformation:
   - `The listener who completes this series will be able to...`
4. The series title with the six title tests applied:
   - poster
   - invitation
   - search
   - clarity
   - uniqueness
   - repetition
5. The complete arc:
   - week-by-week titles
   - main texts
   - weekly function
   - closing tension
6. The series type:
   - felt-needs
   - expository
   - theological
   - missional
   - cultural
   - and how it fits an annual balanced menu
7. The calendar positioning:
   - which congregational season this series serves
   - how that changed the planning decisions
8. The visual anchor:
   - image
   - object
   - concept
   - or stage element that communicates before words
9. The "consistently inconsistent" feature:
   - what makes this series creatively different from recent ones
10. The extension ecosystem:
   - what will sustain the listener beyond Sunday

Then produce these sections:

1. Series concept document
2. Detailed weekly arc
3. Creative identity
4. Launch strategy
5. Evaluation plan

## Required Deliverables

### 1. Series Concept Document

Include:

- title
- subtitle or tagline
- duration with justification
- calendar positioning
- target listener profile
- transformation statement
- preacher burden
- arc summary in one sentence

### 2. Detailed Weekly Arc

For each week include:

- week title
- main biblical text
- function in the arc
- weekly Big Idea
- opening tension
- partial resolution
- closing tension
- demand level:
  - cognitive
  - emotional
  - volitional
  - commitment
- creative element
- verifiable application

### 3. Creative Identity

Include:

- visual concept
- stage anchor
- bumper video concept
- language tone and how it shifts across weeks

### 4. Launch Strategy

Include:

- four-week promotion calendar
- teaser announcement for the previous Sunday
- extension resources
- standard invitation line members can use

### 5. Evaluation Plan

Include:

- success criteria
- five critique questions for the team after the series

## Planning Standards

- Each weekly title must feel related to the series title without being repetitive.
- Each week must advance the stakes.
- Week one must be optimized for first-time visitors.
- Do not let the series run longer than the arc can carry.
- Use the language of real people, not internal church jargon, especially in titles and invitations.
- Favor clarity over cleverness when the two conflict.
- Treat design and launch as ministry decisions, not decoration.

## Document Delivery

- Write the series plan to a UTF-8 text or markdown file first.
- By default, write that source plan inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_series_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete package and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the `.docx` result inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the series title or a user-approved slug, for example: `Vida_Em_4_Semanas.docx`.
- After saving the `.docx` in [outputs/](outputs/), let `scripts/create_series_docx.py` copy the final `.docx` into `C:\Users\filip\.codex\skills\DOCS_Sermons`.
- After the `.docx` is created, run [scripts/create_series_epub.py](scripts/create_series_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the same series title or slug as the `.docx`, for example: `Vida_Em_4_Semanas.epub`.
- Only after the final `.docx` has been copied to `C:\Users\filip\.codex\skills\DOCS_Sermons` and the final `.epub` has been saved in `C:\Users\filip\.codex\skills\EPUB_SERMONS`, delete all contents inside [outputs/](outputs/) while preserving the `outputs` folder itself.
- Deliver both the final `.docx` path and the final `.epub` path to the user.

## Hybrid Environment Rules

- Keep the workflow portable between local and cloud environments.
- Put filesystem reads and writes behind `scripts/adapters.py`.
- Keep parsing, word-count enforcement, and `.docx` rendering in `scripts/core.py`.
- Keep defaults such as minimum words and document styles in `scripts/config.json`.
- Prefer relative or configurable paths over machine-specific absolute paths.
- Prefer [outputs/](outputs/) in this skill folder as the default writable destination.
- If the environment blocks writing to the user-requested workspace, fall back to [outputs/](outputs/) in this skill folder and report the final path clearly.

## Final Quality Check

Before delivery, verify:

- the series is built as an arc, not a list
- the target listener is concrete and plausible
- the transformation can be described with a verb and observed outcome
- the series title passed all six tests
- each week escalates the journey
- the opening week works for guests
- the extension ecosystem keeps the topic alive between Sundays
- the launch calendar starts before the first sermon
- the evaluation questions are specific enough to improve the next series

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.

## Final Output Override (MD Only)

- Esta skill deve entregar exatamente um unico arquivo final `.md`.
- Nao gerar `.docx`, `.epub`, `.pdf`, `.csv`, `.xlsx` ou qualquer outro artefato final.
- Salvar o arquivo final `.md` em `C:\Users\filip\Dropbox\Obsidian_Filipe\Ministério\Sermões\Skill_Revisar`.
- Entregar ao usuario apenas o caminho absoluto desse `.md` salvo.
- Se qualquer instrucao deste arquivo conflitar com esta secao, esta secao prevalece.

## Pergunta Inicial Obrigatoria (Escopo da Producao)

Antes de iniciar qualquer producao, esta skill deve sempre perguntar ao usuario:

`Voce quer apenas o esboco ou a versao completa (sermao/palestra)?`

Opcoes e regras:

- `Esboco`: gerar somente a estrutura (titulo, tese central, pontos principais, transicoes, aplicacoes e conclusao resumida), sem manuscrito completo.
- `Completa`: gerar o manuscrito completo.
- Se a resposta nao estiver clara, pausar e pedir confirmacao antes de escrever.
- Esta pergunta e obrigatoria e deve acontecer antes de qualquer etapa de redacao.
- Em fluxos em lote, fazer a pergunta uma vez no inicio e aplicar a resposta a todos os itens, salvo instrucao contraria do usuario.

