# generate-michael-todd-sermons--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-michael-todd-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-michael-todd-sermons--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-michael-todd-sermons--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-michael-todd-sermons`
- Hash do `SKILL.md`: `0697384525cf3da17922d61d728b0bdf490bd72a98e6a67f51a792a6f46f8872`

## Resumo

Generate sermon outlines and full sermon manuscripts using Michael Todd's authentic preaching style, including cultural series branding, dual-part sermon titles, numbered alliterative points, extended everyday analogies, call-and-response, vulnerable autobiography, and prophetic closing declaration. Use when the user asks to create a sermon, preaching manuscript, sermon outline, youth-oriented church message, culturally resonant sermon, or transformation-focused talk based on a Bible text or theme and wants the result shaped by Michael Todd, Transformation Church style preaching, TC Nation tone, Black church call-and-response, or progression-not-perfection messaging.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-michael-todd-sermons--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-michael-todd-sermons--v2` |
| Skill name | `generate-michael-todd-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-michael-todd-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-michael-todd-sermons--v2` |
| Arquivo principal | `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-michael-todd-sermons--v2.zip` |
| Tamanho do zip | 12,8 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-michael-todd-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Michael Todd's authentic preaching style, including cultural series branding, dual-part sermon titles, numbered alliterative points, extended everyday analogies, call-and-response, vulnerable autobiography, and prophetic closing declaration. Use when the user asks to create a sermon, preaching manuscript, sermon outline, youth-oriented church message, culturally resonant sermon, or transformation-focused talk based on a Bible text or theme and wants the result shaped by Michael Todd, Transformation Church style preaching, TC Nation tone, Black church call-and-response, or progression-not-perfection messaging. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 30,5 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 182 B |
| `references` | 1 | 3,7 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Michael Todd Sermons
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
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/agents/openai.yaml` | 182 B |
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/references/michael_todd_method.md` | 3,7 KB |
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/scripts/config.json` | 459 B |
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-michael-todd-sermons--v2/SKILL.md` | 10,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-michael-todd-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-michael-todd-sermons
description: Generate sermon outlines and full sermon manuscripts using Michael Todd's authentic preaching style, including cultural series branding, dual-part sermon titles, numbered alliterative points, extended everyday analogies, call-and-response, vulnerable autobiography, and prophetic closing declaration. Use when the user asks to create a sermon, preaching manuscript, sermon outline, youth-oriented church message, culturally resonant sermon, or transformation-focused talk based on a Bible text or theme and wants the result shaped by Michael Todd, Transformation Church style preaching, TC Nation tone, Black church call-and-response, or progression-not-perfection messaging.
---

# Generate Michael Todd Sermons

## Overview

Generate sermons with Michael Todd's communication method: build the message around a culturally branded series, a two-part sermon title, a repeated anchor phrase, numbered alliterative points, extended analogies from daily life, strong congregation participation, and a prophetic closing declaration. The default deliverable is a formatted Microsoft Word document.

Read [references/michael_todd_method.md](references/michael_todd_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, tone, movement, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Michael Todd into generic youth-oriented preaching. Preserve cultural series branding, dual titles, numbered alliterative points, extended analogy, call-and-response, vulnerable autobiography, and prophetic close.
- If the user asks for Michael Todd, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a young, multi-ethnic, online-aware, trauma-conscious congregation and produce a complete sermon manuscript.
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

- Define the series name as a cultural product, not a generic theme.
- Create the sermon title in dual format:
  - provocative declaration
  - contextual subtitle
- Determine one central anchor phrase that the congregation can repeat.
- Build 3 to 5 numbered points with alliterative or strongly parallel phrasing.
- Give each point:
  - a full title
  - an extended analogy
  - a biblical text
  - a practical application
  - a participation moment
- Include at least one pop-culture reference per point when it serves the truth naturally.
- Include at least one strong recent autobiographical vulnerability in the opening.
- Use HHOT moments where personal application needs honest engagement.
- Mark call-and-response moments explicitly.
- End with a prophetic declaration and one immediate next step.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The series name and sermon title in dual format.
2. The alliterative titles of the 3 to 5 points.
3. The extended analogy for each point.
4. The anchor phrase for group repetition.
5. The prophetic declaration for the ending.

Then write the sermon with these clearly signaled sections:

1. Opening: autobiographical narrative plus series context
2. Point 1
3. Point 2
4. Point 3
5. Additional points if needed
6. Visual climax if used
7. Ending: prophetic proclamation plus call to action

Use explicit markers such as:

- `[CONGREGACAO REPETE]`
- `[PARTICIPACAO ONLINE]`
- `[PAUSA]`
- `[OLHA PARA A CAMERA]`
- `[VOZ QUEBRADA]`

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Michael_Todd.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Michael_Todd.epub`.
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

- Favor progression over perfection in every application.
- Sound energetic, current, and direct without becoming vague.
- Mix pastoral authority with radical relatability.
- Use short punch lines around high-impact statements.
- Let analogies run long enough to carry emotional and conceptual weight.
- Integrate Black church call-and-response and online audience participation.
- Move toward a faith-transfer ending, not a flat summary.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the title and series feel culturally alive and memorable.
- Verify every point is numbered and alliterative or strongly parallel.
- Verify each point contains analogy, text, application, and participation.
- Verify at least one pop-culture reference is present where useful.
- Verify the sermon has at least five marked participation moments.
- Verify the ending includes prophetic declaration plus one concrete next step.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
```
