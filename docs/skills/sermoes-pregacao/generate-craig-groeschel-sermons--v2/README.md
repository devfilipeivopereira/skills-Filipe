# generate-craig-groeschel-sermons--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-craig-groeschel-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-craig-groeschel-sermons--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-craig-groeschel-sermons`
- Hash do `SKILL.md`: `69d69b1857dec1e448dee3e64d2eb301dbba1e2210666aa90824cc5677b81a7d`

## Resumo

Generate sermon outlines and full sermon manuscripts using Craig Groeschel's authentic communication style, including one core idea, a repeated mantra line, numbered full-sentence points, emotional connection, vulnerable storytelling, and science plus Scripture integration. Use when the user asks to create a sermon, preaching manuscript, sermon outline, multi-site message, behavior-change message, or seeker-accessible talk based on a Bible text or theme and wants the result shaped by Craig Groeschel, Life.Church style preaching, vulnerable leadership communication, neuroscience plus Bible framing, or practical emotionally driven preaching.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-craig-groeschel-sermons--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-craig-groeschel-sermons--v2` |
| Skill name | `generate-craig-groeschel-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-craig-groeschel-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2` |
| Arquivo principal | `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-craig-groeschel-sermons--v2.zip` |
| Tamanho do zip | 13,0 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-craig-groeschel-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Craig Groeschel's authentic communication style, including one core idea, a repeated mantra line, numbered full-sentence points, emotional connection, vulnerable storytelling, and science plus Scripture integration. Use when the user asks to create a sermon, preaching manuscript, sermon outline, multi-site message, behavior-change message, or seeker-accessible talk based on a Bible text or theme and wants the result shaped by Craig Groeschel, Life.Church style preaching, vulnerable leadership communication, neuroscience plus Bible framing, or practical emotionally driven preaching. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 31,0 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 185 B |
| `references` | 1 | 4,4 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Craig Groeschel Sermons
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
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/agents/openai.yaml` | 185 B |
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/references/craig_groeschel_method.md` | 4,4 KB |
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/scripts/config.json` | 462 B |
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-craig-groeschel-sermons--v2/SKILL.md` | 9,8 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-craig-groeschel-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-craig-groeschel-sermons
description: Generate sermon outlines and full sermon manuscripts using Craig Groeschel's authentic communication style, including one core idea, a repeated mantra line, numbered full-sentence points, emotional connection, vulnerable storytelling, and science plus Scripture integration. Use when the user asks to create a sermon, preaching manuscript, sermon outline, multi-site message, behavior-change message, or seeker-accessible talk based on a Bible text or theme and wants the result shaped by Craig Groeschel, Life.Church style preaching, vulnerable leadership communication, neuroscience plus Bible framing, or practical emotionally driven preaching.
---

# Generate Craig Groeschel Sermons

## Overview

Generate sermons with Craig Groeschel's communication method: define one core idea, one action, one repeated phrase-mantra, and build the message through numbered full-sentence points that are practical, personal, memorable, and emotional. The default deliverable is a formatted Microsoft Word document.

Read [references/craig_groeschel_method.md](references/craig_groeschel_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, tone, timing, checkpoints, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Craig Groeschel into generic practical preaching. Preserve the one idea, 4 Ps, numbered full-sentence points, resistant-listener filter, science-plus-Scripture integration, and vulnerable momentum.
- If the user asks for Craig Groeschel, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a mixed audience across in-person, online, committed Christian, skeptical, and unchurched listeners, and produce a complete sermon manuscript.
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

- Determine the one central idea before writing anything else.
- Answer two questions first:
  - what is one thing the audience must know?
  - what should they do with it?
- Create the phrase-mantra before writing the body.
- Build 3 to 5 numbered points as complete, memorable sentences that all support the same central idea.
- Ensure each point is practical, personal, memorable, and emotional.
- Apply the resistant-listener filter to each point:
  - why does this matter?
  - so what changes?
  - why might someone think this does not apply to them?
- Integrate science plus Scripture at least once per sermon.
- Build the opening around recent, specific, risky vulnerability.
- Include at least three audience interaction moments.
- Date the application: today, this week, next 30 days.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The one core idea of the sermon.
2. The central phrase-mantra.
3. The numbered points as full sentences.
4. The main biblical text.
5. The specific next step for this week.

Then write the sermon with these clearly signaled sections:

1. Opening: high-specificity vulnerability
2. Central idea and phrase-mantra
3. Point 1: diagnosis
4. Point 2: revelation
5. Point 3: activation
6. Additional points if needed
7. Climax: declaration of faith
8. Ending: application and next step

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Craig_Groeschel.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Craig_Groeschel.epub`.
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

- Prefer emotionally connected truth over information density.
- Write as a one-on-one conversation that scales to a large room.
- Use specific, recent vulnerability rather than generic confession.
- Use numbered points written as full statements, not topic labels.
- Repeat the phrase-mantra at least three or four times naturally.
- Bridge science and Scripture without making the sermon feel academic.
- Include explicit interaction cues for live, multi-site, and online listeners.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the message has one core idea only.
- Verify the phrase-mantra is memorable, repeatable, and central.
- Verify every point is a complete sentence and supports the same idea.
- Verify at least one science plus Scripture bridge is present.
- Verify the resistant-listener filter is answered across the message.
- Verify the application is time-bound and concrete.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
```
