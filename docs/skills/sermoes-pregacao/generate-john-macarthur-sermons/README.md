# generate-john-macarthur-sermons

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-john-macarthur-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-john-macarthur-sermons.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-john-macarthur-sermons`
- Fonte original: `C:\Users\filip\.codex\skills\generate-john-macarthur-sermons`
- Hash do `SKILL.md`: `5c962049d8fd299f57c45baef454072c74bd2997fa70e2bf4bdc583190ac1a60`

## Resumo

Generate sermon outlines and full sermon manuscripts using John MacArthur's expository preaching method, including strict textual delimitation, original authorial intent, verse-by-verse exposition, careful lexical and grammatical analysis, Scripture interpreting Scripture, doctrinal precision, theological implications, and direct expository exhortation with gravitas. Use when the user asks to create a sermon, preaching manuscript, John MacArthur style sermon, verse-by-verse exposition, expository sermon, doctrinal sermon, or sufficiency-of-Scripture message based on a Bible text or theme.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-john-macarthur-sermons.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-john-macarthur-sermons` |
| Skill name | `generate-john-macarthur-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-john-macarthur-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-john-macarthur-sermons` |
| Arquivo principal | `skills/sermoes-pregacao/generate-john-macarthur-sermons/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-john-macarthur-sermons.zip` |
| Tamanho do zip | 12,9 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-john-macarthur-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using John MacArthur's expository preaching method, including strict textual delimitation, original authorial intent, verse-by-verse exposition, careful lexical and grammatical analysis, Scripture interpreting Scripture, doctrinal precision, theological implications, and direct expository exhortation with gravitas. Use when the user asks to create a sermon, preaching manuscript, John MacArthur style sermon, verse-by-verse exposition, expository sermon, doctrinal sermon, or sufficiency-of-Scripture message based on a Bible text or theme. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 30,9 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 184 B |
| `references` | 1 | 2,5 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate John MacArthur Sermons
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
-   Final Output Override (MD Only)
-   Pergunta Inicial Obrigatoria (Escopo da Producao)

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/agents/openai.yaml` | 184 B |
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/references/john_macarthur_method.md` | 2,5 KB |
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/scripts/config.json` | 461 B |
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-john-macarthur-sermons/SKILL.md` | 11,7 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-john-macarthur-sermons`
- `C:\Users\filip\.agents\skills\generate-john-macarthur-sermons`
- `C:\Users\filip\.claude\skills\generate-john-macarthur-sermons`
- `C:\Users\filip\.cursor\skills\generate-john-macarthur-sermons`
- `C:\Users\filip\.windsurf\skills\generate-john-macarthur-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-john-macarthur-sermons
description: Generate sermon outlines and full sermon manuscripts using John MacArthur's expository preaching method, including strict textual delimitation, original authorial intent, verse-by-verse exposition, careful lexical and grammatical analysis, Scripture interpreting Scripture, doctrinal precision, theological implications, and direct expository exhortation with gravitas. Use when the user asks to create a sermon, preaching manuscript, John MacArthur style sermon, verse-by-verse exposition, expository sermon, doctrinal sermon, or sufficiency-of-Scripture message based on a Bible text or theme.
---

# Generate John MacArthur Sermons

## Overview

Generate sermons with John MacArthur's expository method: delimit a coherent biblical unit, discover the text's original meaning before consulting secondary helps, identify the dominant idea of the passage, expose the text verse by verse, explain decisive Greek or Hebrew terms pastorally, illuminate the passage with other Scriptures, articulate its doctrine and implications precisely, and conclude with direct expository exhortation. The default deliverable is a formatted Microsoft Word document.

Read [references/john_macarthur_method.md](references/john_macarthur_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the eight sermon phases, the relation between exegesis and application, and the controlling theological commitments of the method.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten John MacArthur into generic exposition. Preserve textual delimitation, authorial intent, verse-by-verse movement, lexical discipline, Scripture interpreting Scripture, doctrinal precision, and gravitas.
- If the user asks for John MacArthur, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a congregation that needs strong confidence in the authority, sufficiency, and clarity of Scripture through careful verse-by-verse exposition.
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

- Delimit one coherent literary unit and justify why it stands as a sermon unit.
- State the original authorial intention before moving to present-tense preaching.
- Formulate one dominant idea in a complete sentence.
- Identify only those original-language terms that are truly determinative for the argument.
- Select cross-references that interpret the passage rather than merely decorate a theme.
- Name which theological pillars especially emerge from the text.
- Articulate implications that arise from the exegesis before moving to exhortation.
- Keep the sermon text-governed and resistant to ornamental rhetorical devices.
- Let the Spirit make specific application through the force of the text's implications rather than through fabricated case studies.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The delimited biblical text and why it forms a coherent literary unit.
2. The original authorial intent.
3. The dominant idea of the passage.
4. The decisive original-language terms and why they matter.
5. The Scripture cross-references and how they illuminate the passage.
6. The relevant theological pillars emerging from the text.
7. The theological implications for God, humanity, sin, grace, or obedience.
8. The specific imperative or expository exhortation contained in the text.

Then write the sermon with these clearly signaled phases:

1. Phase 2: Reading of the text and contextual orientation
2. Phase 3: Functional historical-literary introduction
3. Phase 4: Verse-by-verse exposition
4. Phase 5: Lexical and grammatical explanation
5. Phase 6: Cross-scriptural illumination
6. Phase 7: Doctrine and implications
7. Phase 8: Exhortation with gravitas
8. Phase 9: Brief synthetic conclusion

Write the transitions explicitly. Keep the tone serious, text-governed, and theologically precise rather than rhetorically ornamental.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_John_MacArthur.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_John_MacArthur.epub`.
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

- Let the text determine both structure and message.
- Use careful doctrinal language without apology, but explain it clearly.
- Avoid entertainment-driven openings and sentiment-driven conclusions.
- Treat original-language analysis as pastoral illumination, not academic display.
- Keep exhortation tethered to the text's own demands.
- End briefly and forcefully, with a clear call rooted in the passage itself.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the text truly governs the sermon.
- Verify the dominant idea emerges from exegesis rather than theme selection.
- Verify the lexical analysis is necessary and argument-serving.
- Verify cross-references clarify the passage instead of becoming side excursions.
- Verify doctrine arises from the text and implications flow from doctrine.
- Verify the exhortation is text-rooted and weighty.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.

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
```
