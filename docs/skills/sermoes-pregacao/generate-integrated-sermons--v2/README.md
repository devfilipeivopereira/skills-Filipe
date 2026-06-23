# generate-integrated-sermons--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-integrated-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-integrated-sermons--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-integrated-sermons--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-integrated-sermons`
- Hash do `SKILL.md`: `bfea28a9ce2b25f4fa679c9546e91c85c6d6ebef28b2c07b5ac8d5e982be4bd1`

## Resumo

Generate sermon outlines and full sermon manuscripts using an integrated six-layer preaching system that combines Andy Stanley's Me-We-God-You-We structure, Carmine Gallo's communication principles, Steven Furtick's delivery style and title wordplay, John MacArthur's exegetical rigor, Joseph Prince's grace-centered application, and Jim Edwards style opening connection. Use when the user asks to create a sermon, preaching manuscript, hybrid sermon, integrated method sermon, multiple-method sermon, or a message that must combine communication rigor with theological fidelity from a Bible text or theme.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-integrated-sermons--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-integrated-sermons--v2` |
| Skill name | `generate-integrated-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-integrated-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-integrated-sermons--v2` |
| Arquivo principal | `skills/sermoes-pregacao/generate-integrated-sermons--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-integrated-sermons--v2.zip` |
| Tamanho do zip | 12,6 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-integrated-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using an integrated six-layer preaching system that combines Andy Stanley's Me-We-God-You-We structure, Carmine Gallo's communication principles, Steven Furtick's delivery style and title wordplay, John MacArthur's exegetical rigor, Joseph Prince's grace-centered application, and Jim Edwards style opening connection. Use when the user asks to create a sermon, preaching manuscript, hybrid sermon, integrated method sermon, multiple-method sermon, or a message that must combine communication rigor with theological fidelity from a Bible text or theme. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 30,3 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 180 B |
| `references` | 1 | 2,6 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Integrated Sermons
-   Overview
-   Method Fidelity Rules
-   Workflow
-   Absolute Format Restrictions
-   Originality Requirement
-   Research Requirement
-   Preparation Rules
-   Output Contract
-   Document Delivery
-   Hybrid Environment Rules
-   Style Rules
-   Audit Rules
-   Quality Check
-   Final Cleanup Rule

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/agents/openai.yaml` | 180 B |
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/references/integrated_sermon_method.md` | 2,6 KB |
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/scripts/config.json` | 457 B |
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-integrated-sermons--v2/SKILL.md` | 11,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-integrated-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-integrated-sermons
description: Generate sermon outlines and full sermon manuscripts using an integrated six-layer preaching system that combines Andy Stanley's Me-We-God-You-We structure, Carmine Gallo's communication principles, Steven Furtick's delivery style and title wordplay, John MacArthur's exegetical rigor, Joseph Prince's grace-centered application, and Jim Edwards style opening connection. Use when the user asks to create a sermon, preaching manuscript, hybrid sermon, integrated method sermon, multiple-method sermon, or a message that must combine communication rigor with theological fidelity from a Bible text or theme.
---

# Generate Integrated Sermons

## Overview

Generate sermons with a six-layer integrated method: build the sermon around one point and one Bottom Line, open by naming the hearer's real pain before the text appears, expose the biblical text with real historical and lexical rigor, deliver it with a memorable title and congregational participation, apply it through identity and grace rather than legalism, and close with a practical call plus an audit report. The default deliverable is a formatted Microsoft Word document.

Read [references/integrated_sermon_method.md](references/integrated_sermon_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the six layers, the integrated structure, and the audit protocol.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten the integrated method into a generic blended sermon. Preserve all six layers, the 12 pre-sermon declarations, the strict restrictions, the GOD subpoint rules, and the final audit protocol.
- If the user asks for the integrated method, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a mixed audience that includes believers, strugglers, skeptical listeners, and people carrying real pain who need both deep biblical substance and clear communication.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Absolute Format Restrictions

- Never use em dash style punctuation in the sermon.
- Never mention storms, foundations, or any allusion to the house on rock and sand unless the user explicitly requests it.
- Never use that parable unless the user explicitly requests it.

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

- Build one point only:
  - one thing to know
  - one thing to do
- Create one Bottom Line with fewer than 10 words.
- Derive the title wordplay from the text, not from marketing instinct.
- Open with real audience pain before unveiling the biblical answer.
- Keep the `GOD` section exegetically serious:
  - historical-literary context
  - 1 to 3 decisive original-language terms
  - 1 to 3 illuminating cross-references
- Let Christ and grace govern the application before any imperative.
- Include at least four congregational participation moments across the sermon.
- Include one S.T.A.R. moment that the hearer will remember.
- End with a short memorable line and a formal audit report.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The chosen biblical text and the delimited literary unit.
2. The single sermon point: one thing to know and one thing to do.
3. The Bottom Line.
4. The title wordplay.
5. The specific active dilemma of the `ME`.
6. The `WE` tension and the listener profiles inside it.
7. The exegetical result of the `GOD` section, including original-language terms and cross-references.
8. The Christ-centered identity that grounds the `YOU` application.
9. The specific and verifiable `YOU` application.
10. The S.T.A.R. moment.
11. The specific `WE FINAL` vision-casting image.
12. The planned congregational participation moments.

Then write the sermon with these clearly signaled sections:

1. Title and short description
2. ME
3. WE
4. GOD
5. YOU
6. WE FINAL
7. Final memorable line
8. Closing prayer or invitation
9. Audit report

In the `GOD` section, include four subpoints that each:

- begin with a verb
- emerge from the text
- include one illustration
- include three practical applications
- include one teaching suggestion or sensory teaching aid

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher label for this skill, for example: `JoÃ£o_9_Integrated_Method.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher label for this skill, for example: `JoÃ£o_9_Integrated_Method.epub`.
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

- Keep one point only.
- Make the opening emotionally exact and immediately recognizable.
- Use at least one strong analogy or mental image in each major section.
- Let the title, Bottom Line, and final line feel memorable without becoming gimmicky.
- Keep original-language material pastoral and useful.
- Put identity in Christ before obligation.
- Keep the sermon free of the forbidden imagery unless explicitly requested by the user.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Audit Rules

At the end of the sermon, include:

- the required checklist report with `Ok` or `Revisar`
- the audit score table from 0 to 2 for each required criterion
- automatic revision before completion if any criterion would clearly fall below 2

## Quality Check

- Verify the sermon contains one point and one Bottom Line.
- Verify the opening follows the pain-first logic.
- Verify the `GOD` section is genuinely exegetical.
- Verify the `YOU` section is grace-based before it is imperative.
- Verify at least four participation moments are included.
- Verify the final audit report is present.
- Verify the forbidden formatting and imagery constraints are respected.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
```
