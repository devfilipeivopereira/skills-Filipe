# generate-calvin-miller-sermons--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-calvin-miller-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-calvin-miller-sermons--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-calvin-miller-sermons`
- Hash do `SKILL.md`: `37aabd20848915dd2c527d91d443117bf2095ea85ddee7eca5257cae1d2eb54e`

## Resumo

Generate sermon outlines and full sermon manuscripts using Calvin Miller's narrative exposition method, including the speech before the speech, a narrative frame that opens in the first minute and resolves only at the end, one sermon logo, image-driven exposition, confessional preaching, planned redundancy, and a final image rather than a proposition. Use when the user asks to create a sermon, preaching manuscript, narrative expository message, Calvin Miller style sermon, image-rich sermon, frame sermon, or story-shaped exposition based on a Bible text or theme.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-calvin-miller-sermons--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-calvin-miller-sermons--v2` |
| Skill name | `generate-calvin-miller-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-calvin-miller-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2` |
| Arquivo principal | `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-calvin-miller-sermons--v2.zip` |
| Tamanho do zip | 12,7 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-calvin-miller-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Calvin Miller's narrative exposition method, including the speech before the speech, a narrative frame that opens in the first minute and resolves only at the end, one sermon logo, image-driven exposition, confessional preaching, planned redundancy, and a final image rather than a proposition. Use when the user asks to create a sermon, preaching manuscript, narrative expository message, Calvin Miller style sermon, image-rich sermon, frame sermon, or story-shaped exposition based on a Bible text or theme. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 30,9 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 183 B |
| `references` | 1 | 3,8 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Calvin Miller Sermons
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
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/agents/openai.yaml` | 183 B |
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/references/calvin_miller_method.md` | 3,8 KB |
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/scripts/config.json` | 460 B |
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-calvin-miller-sermons--v2/SKILL.md` | 10,3 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-calvin-miller-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-calvin-miller-sermons
description: Generate sermon outlines and full sermon manuscripts using Calvin Miller's narrative exposition method, including the speech before the speech, a narrative frame that opens in the first minute and resolves only at the end, one sermon logo, image-driven exposition, confessional preaching, planned redundancy, and a final image rather than a proposition. Use when the user asks to create a sermon, preaching manuscript, narrative expository message, Calvin Miller style sermon, image-rich sermon, frame sermon, or story-shaped exposition based on a Bible text or theme.
---

# Generate Calvin Miller Sermons

## Overview

Generate sermons with Calvin Miller's narrative exposition method: begin with relational presence before formal preaching, install a narrative frame with live tension, announce one sermon logo, expose the biblical text through images rather than only propositions, keep returning to the frame until the closing resolution, and end with a final image that keeps working after the sermon ends. The default deliverable is a formatted Microsoft Word document.

Read [references/calvin_miller_method.md](references/calvin_miller_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the sermon logo, the narrative frame, image-making, and the nine movement flow.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Calvin Miller into generic exposition. Preserve the speech before the speech, the narrative frame, the single logo, confessional texture, planned redundancy, and the final image.
- If the user asks for Calvin Miller, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume ordinary hearers who need the Gospel to become habitable through narrative tension, vivid images, and concrete recognition.
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

- Read the biblical text with the eyes of narrative, not only abstraction.
- Declare one sermon logo in a memorable affirmative sentence.
- Build one narrative frame with a specific unresolved scene.
- Decide how that same frame will be resolved in the final paragraph.
- Identify three or four central images that will carry the exposition.
- Include the preacher's confessional testimony: how the text crossed the preacher first.
- Keep the sermon inside one central urgency rather than multiple competing points.
- Use planned redundancy so the sermon logo returns with growing depth.
- Let application emerge from the narrative frame instead of being stapled on externally.
- End with an image, not a proposition, list, or final abstraction.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The central biblical text and what it says when read narratively.
2. The sermon logo.
3. The narrative frame: who is present, where, what time, what is felt, what is at risk, and what remains unresolved.
4. The source of the frame:
   - contemporary life
   - biblical text
   - literary, historical, or cultural story
5. How the frame will be resolved at the end.
6. The three to four central images that will carry the exposition.
7. The preacher's confessional testimony.
8. The specific listener tension addressed by the frame and the sermon logo.

Then write the sermon with these clearly signaled movements:

1. Speech before the speech
2. Opening of the narrative frame
3. Sermon logo announced
4. Narrative exposition of the text
5. Planned redundancy of the sermon logo
6. Returns to the frame
7. Application emerging from the narrative
8. Resolution of the frame

Write the transitions explicitly. Keep the narrative frame alive from first paragraph to last paragraph. Repeat the sermon logo at least four times with deepening force.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Calvin_Miller.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Calvin_Miller.epub`.
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

- Write as an image-maker, not merely an analyst.
- Keep the sermon logo singular, memorable, and urgent.
- Build scenes with sensory specificity.
- Let the hearer inhabit the narrative frame rather than only hear about it.
- Use confession where the text has first pierced the preacher.
- Avoid multiplying points that divide urgency.
- End with a resolving image rather than an explanatory summary.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the sermon has one real sermon logo rather than several points competing for attention.
- Verify the narrative frame opens early and remains alive until the end.
- Verify the exposition works through images and scenes rather than bare abstractions.
- Verify the sermon logo returns with planned redundancy.
- Verify application emerges naturally from the narrative frame.
- Verify the sermon ends with an image instead of a proposition.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
```
