# generate-brian-jones-sermons--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-brian-jones-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-brian-jones-sermons--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-brian-jones-sermons--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-brian-jones-sermons`
- Hash do `SKILL.md`: `1745bd1330318c611e5931326a025aff3f3e7087baeab42feeaef8672f858406`

## Resumo

Generate sermon outlines and full sermon manuscripts using Brian Jones's Introduction-Explanation-Application preaching method, conversion-focused audience targeting, and story-driven sermon construction. Use when the user asks to create a sermon, preaching manuscript, sermon outline, sermon series message, action step, or commitment response based on a Bible text or theme and wants the result shaped by Brian Jones, CCV, unchurched audience preaching, conversion growth, or the Introduction-Explanation-Application structure.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-brian-jones-sermons--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-brian-jones-sermons--v2` |
| Skill name | `generate-brian-jones-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-brian-jones-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-brian-jones-sermons--v2` |
| Arquivo principal | `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-brian-jones-sermons--v2.zip` |
| Tamanho do zip | 12,8 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-brian-jones-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Brian Jones's Introduction-Explanation-Application preaching method, conversion-focused audience targeting, and story-driven sermon construction. Use when the user asks to create a sermon, preaching manuscript, sermon outline, sermon series message, action step, or commitment response based on a Bible text or theme and wants the result shaped by Brian Jones, CCV, unchurched audience preaching, conversion growth, or the Introduction-Explanation-Application structure. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 30,8 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 181 B |
| `references` | 1 | 4,1 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Brian Jones Sermons
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
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/agents/openai.yaml` | 181 B |
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/references/brian_jones_method.md` | 4,1 KB |
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/scripts/config.json` | 459 B |
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-brian-jones-sermons--v2/SKILL.md` | 9,9 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-brian-jones-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-brian-jones-sermons
description: Generate sermon outlines and full sermon manuscripts using Brian Jones's Introduction-Explanation-Application preaching method, conversion-focused audience targeting, and story-driven sermon construction. Use when the user asks to create a sermon, preaching manuscript, sermon outline, sermon series message, action step, or commitment response based on a Bible text or theme and wants the result shaped by Brian Jones, CCV, unchurched audience preaching, conversion growth, or the Introduction-Explanation-Application structure.
---

# Generate Brian Jones Sermons

## Overview

Generate sermons with a Brian Jones-style workflow: define the target unchurched listener, distill one concrete action, build an introduction around three jabs plus a right hook, explain the biblical text in a tight arc, and land in direct application with a clear response. The default deliverable is a formatted Microsoft Word document.

Read [references/brian_jones_method.md](references/brian_jones_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Brian Jones into a generic practical sermon. Preserve the `Unchurched John` target, the Jab structure, the explanation cap, the response pressure, and the story-first logic.
- If the user asks for Brian Jones, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a general unchurched or dechurched audience and a complete sermon manuscript.
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

- Define the target listener before outlining. Use a concrete `Unchurched John` profile.
- Mentally picture the listener's emotional and mental state on arrival.
- Distill the sermon into one action statement with an imperative verb.
- Make the action specific, verifiable, and time-bound or time-implied.
- Build the sermon around one idea and one action. Cut anything that does not serve them.
- Structure the introduction as Jab 1, Jab 2, Jab 3, then Right Hook.
- Limit explanation to three central truths from the text.
- Build application around direct obedience, objections, concrete examples, and a closing response.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 10,000 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The target `Unchurched John` profile for this message.
2. The listener's expected emotional and mental state on arrival.
3. The sermon action statement in one imperative sentence.
4. The introduction flow: Jab 1, Jab 2, Jab 3, Right Hook.
5. The up to three explanatory truths from the text.
6. The specific weekly response or decision step.

Then write the sermon with this sequence:

1. Introduction:
   - Jab 1
   - Jab 2
   - Jab 3
   - Right Hook
2. Explanation:
   - present the biblical text
   - announce up to three truths
   - explain only what serves the action statement
3. Application:
   - state the action directly
   - show personal honesty and vulnerability
   - give specific replicable examples
   - anticipate objections
   - interleave stories and pressure lines
   - call for action without ambiguity
   - end with concrete response and strongest closing story

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `10000` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Brian_Jones.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Brian_Jones.epub`.
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

- Prefer clarity, urgency, and emotional momentum over polished abstraction.
- Write for an unchurched or dechurched listener first.
- Open with stories, not exposition.
- Never open by reading the biblical text, asking people to open the Bible, or front-loading context.
- Keep the introduction hot, the explanation tight, and the application concrete.
- Use at least four strong stories across the sermon: opening, closing, and two in the body.
- Keep the message aligned to one idea and one action.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 10,000 words while preserving a spoken 25-minute structure.

## Quality Check

- Verify the target listener is concrete, not generic.
- Verify the action statement starts with an imperative verb and is specific.
- Verify the introduction contains Jab 1, Jab 2, Jab 3, and Right Hook.
- Verify explanation stays at three truths or fewer.
- Verify application drives obedience, not vague reflection.
- Verify the ending closes with the strongest story, not a flat recap.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
```
