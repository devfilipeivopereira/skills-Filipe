# generate-td-jakes-sermons--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-td-jakes-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-td-jakes-sermons--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-td-jakes-sermons--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-td-jakes-sermons`
- Hash do `SKILL.md`: `221716a895bd8ee449803abe909da6de37975a988df9f279fe9953eed4bb81eb`

## Resumo

Generate sermon outlines and full sermon manuscripts using T.D. Jakes's documented preaching method, including personal feeding from the text, GPS turns in the passage, the narrative framework of person-problem-prescription, extended interpretive metaphor, and a prophetic proclamation ending. Use when the user asks to create a sermon, preaching manuscript, sermon outline, Pentecostal narrative message, suffering-to-destiny sermon, or prophetic pastoral message based on a Bible text or theme and wants the result shaped by T.D. Jakes, The Potter's House style preaching, person-problem-prescription preaching, or whooping-influenced proclamation.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-td-jakes-sermons--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-td-jakes-sermons--v2` |
| Skill name | `generate-td-jakes-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-td-jakes-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-td-jakes-sermons--v2` |
| Arquivo principal | `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-td-jakes-sermons--v2.zip` |
| Tamanho do zip | 12,3 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-td-jakes-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using T.D. Jakes's documented preaching method, including personal feeding from the text, GPS turns in the passage, the narrative framework of person-problem-prescription, extended interpretive metaphor, and a prophetic proclamation ending. Use when the user asks to create a sermon, preaching manuscript, sermon outline, Pentecostal narrative message, suffering-to-destiny sermon, or prophetic pastoral message based on a Bible text or theme and wants the result shaped by T.D. Jakes, The Potter's House style preaching, person-problem-prescription preaching, or whooping-influenced proclamation. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 29,7 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 180 B |
| `references` | 1 | 3,4 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate T.D. Jakes Sermons
-   Overview
-   Method Fidelity Rules
-   Workflow
-   Originality Requirement
-   Research Requirement
-   Preparation Rules
-   Output Contract
-   Document Delivery
-   Hybrid Environment Rules
-   Style Rules
-   Quality Check
-   Final Cleanup Rule

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/agents/openai.yaml` | 180 B |
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/references/td_jakes_method.md` | 3,4 KB |
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/scripts/config.json` | 455 B |
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-td-jakes-sermons--v2/SKILL.md` | 9,6 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-td-jakes-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-td-jakes-sermons
description: Generate sermon outlines and full sermon manuscripts using T.D. Jakes's documented preaching method, including personal feeding from the text, GPS turns in the passage, the narrative framework of person-problem-prescription, extended interpretive metaphor, and a prophetic proclamation ending. Use when the user asks to create a sermon, preaching manuscript, sermon outline, Pentecostal narrative message, suffering-to-destiny sermon, or prophetic pastoral message based on a Bible text or theme and wants the result shaped by T.D. Jakes, The Potter's House style preaching, person-problem-prescription preaching, or whooping-influenced proclamation.
---

# Generate T.D. Jakes Sermons

## Overview

Generate sermons with T.D. Jakes's preaching method: go to the text for personal feeding first, think through the text until it is clear, pray until the message is hot, and then preach through the narrative arc of person, problem, and prescription with extended metaphor and prophetic proclamation. The default deliverable is a formatted Microsoft Word document.

Read [references/td_jakes_method.md](references/td_jakes_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for preparation, structure, tone, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten T.D. Jakes into generic Pentecostal preaching. Preserve personal feeding from the text, GPS turns, person-problem-prescription, interpretive metaphor, and prophetic proclamation.
- If the user asks for T.D. Jakes, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a broad congregation carrying real pain, delay, and spiritual hunger, and produce a complete sermon manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every sermon or message must be newly written for the current request.

- Do not reuse pre-existing sermon manuscripts, previous generated files, cached sermon bodies, or prior outputs as the draft source.
- Do not paraphrase or lightly adapt an older sermon and present it as new work.
- You may reuse the biblical reference, the requested theme, and verified research material, but the manuscript itself must be freshly composed.
- Preserve the distinctive style, structure, rhetoric, and methodology of this preacher skill while still producing original wording and movement for the present request.
- If the same user asks for the same biblical reference again, write a new sermon unless the user explicitly asks for revision of an earlier one.

## Research Requirement

Before drafting the sermon, browse the internet to gather fresh, relevant material connected to the biblical text, audience, and theme.

- Collect current illustrations, statistics, cultural references, historical details, ministry context, or recent events only when they genuinely strengthen the sermon.
- Prefer recent and reputable sources. Use primary sources whenever possible.
- Treat online material as support, not as the authority. Scripture and the target preaching methodology remain primary.
- Keep only the most useful researched material. Do not overload the sermon with internet findings.
- When a contemporary example, statistic, quotation, or factual claim materially shapes the sermon, keep the source link available for attribution if the user asks.
- If the request is time-sensitive or depends on current events, verify the information online before finalizing the manuscript.

## Preparation Rules

- Go to the text first for personal nourishment, not merely sermon production.
- Identify the GPS turns in the text: where the passage changes direction, emphasis, or revelation.
- Think the text through until the message is clear.
- Use the person-problem-prescription framework:
  - person
  - problem
  - prescription
- Humanize the biblical character emotionally before prescribing anything.
- Build the sermon around one dominant metaphor that interprets suffering, pressure, or process.
- Show God's perspective inside the process, not just after it.
- Let the sermon rise naturally from conversation to proclamation.
- End with prophetic blessing and destiny language rather than summary.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. What the text fed in the preacher personally.
2. The GPS turns in the passage.
3. The person, problem, and prescription.
4. The dominant metaphor that will interpret the sermon.
5. The prophetic declaration that will close the sermon.

Then write the sermon with these clearly signaled sections:

1. Opening: humanization
2. Body: exegesis and reframing of pain
3. Climax: proclamation of destiny

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_TD_Jakes.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_TD_Jakes.epub`.
- Deliver the final `.epub` path to the user alongside the `.docx` path.

- Only after the final `.docx` has been copied to `C:\Users\filip\.codex\skills\DOCS_Sermons` and the final `.epub` has been saved in `C:\Users\filip\.codex\skills\EPUB_SERMONS`, delete all contents inside [outputs/](outputs/) while preserving the `outputs` folder itself.

## Hybrid Environment Rules

- Keep the sermon-generation workflow portable between local and cloud environments.
- Put filesystem reads and writes behind `scripts/adapters.py`.
- Keep parsing, word-count enforcement, and `.docx` rendering in `scripts/core.py`.
- Keep defaults such as minimum words and document styles in `scripts/config.json`.
- Prefer relative or configurable paths over machine-specific absolute paths.
- Prefer [outputs/](outputs/) in this skill folder as the default writable destination.
- If the environment blocks writing to the user-requested workspace, fall back to [outputs/](outputs/) in this skill folder and report the final path clearly.

## Style Rules

- Feed yourself in the text before speaking to the audience.
- Preach for real people carrying real suffering.
- Humanize the character before diagnosing the problem.
- Use one extended metaphor as interpretive framework, not as decoration.
- Let exegesis stay primary so the emotional force grows from the text.
- Build toward proclamation rather than starting there.
- End with faith-transfer language, not tidy recap language.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the preacher was personally fed by the text.
- Verify the GPS turns are clear and shape the outline.
- Verify person, problem, and prescription are all explicit.
- Verify the central metaphor reinterprets the listener's suffering.
- Verify the perspective shift comes from the text rather than imported sentiment.
- Verify the ending sounds like prophetic blessing, not summary.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
```
