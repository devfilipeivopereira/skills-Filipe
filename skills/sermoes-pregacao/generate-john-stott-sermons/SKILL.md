---
name: generate-john-stott-sermons
description: Generate sermon outlines and full sermon manuscripts using John Stott's expositional preaching method, including faithful exposition of a single biblical text, the dominant thought, double listening to Scripture and the contemporary world, explicit engagement with the listener's silent objections, pastoral bridge-building between the two worlds, and a clear concluding appeal to the will. Use when the user asks to create a sermon, preaching manuscript, expository message, Bible exposition, John Stott style sermon, Langham style sermon, or bridge sermon based on a Bible text or theme.
---

# Generate John Stott Sermons

## Overview

Generate sermons with John Stott's expositional method: stand with one foot in the biblical text and one foot in the contemporary world, identify the text's dominant thought, build a real bridge between the two worlds, answer the hearer's silent objections, and finish with a clear appeal to the will. The default deliverable is a formatted Microsoft Word document.

Read [references/john_stott_method.md](references/john_stott_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, tone, double listening, and the five portraits of the preacher.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten John Stott into generic exposition. Preserve the dominant thought, double listening, dialogue with silent objections, bridge-building, and appeal to the will.
- If the user asks for John Stott, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a mixed evangelical congregation that needs both faithful exposition and pastoral bridge-building into contemporary life.
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

- Work from one main biblical text and treat it as a complete unit of thought.
- Distill the sermon into one dominant thought in a single sentence.
- State clearly the exegetical idea and how it becomes the present-tense dominant thought.
- Practice double listening:
  - listen carefully to the biblical world
  - listen carefully to the modern world of the hearers
- Identify the dominant pastoral question the hearers are really asking.
- Decide which portrait of the preacher this sermon most demands:
  - steward
  - herald
  - witness
  - father
  - servant
- Anticipate and answer the listener's silent objections inside the sermon.
- Keep the structure emerging from the text instead of imposing a template onto the text.
- End with a clear appeal to the will rather than mere reflection.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The central biblical text and the literary unit it represents.
2. The dominant thought in one sentence.
3. The exegetical idea: what the biblical author said to the original hearers.
4. The difference between the exegetical idea and the dominant thought for today.
5. The purpose of the sermon.
6. The expected results in three dimensions:
   - cognitive
   - affective
   - volitional
7. The existential question the text answers from the hearer's point of view.
8. The portrait of the preacher this sermon most requires and the vice to avoid.
9. The dominant portrait of the hearer in this message.

Then write the sermon with these clearly signaled sections:

1. Introduction
2. Exposition of the text
3. Bridge building and silent dialogue
4. Contemporary application
5. Conclusion with appeal

Write the transitions between sections explicitly. Repeat the dominant thought at least four times across the sermon. Make the sermon genuinely disturbing and genuinely consoling, as the text requires.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_John_Stott.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_John_Stott.epub`.
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

- Let the text govern the sermon from beginning to end.
- Write with clarity, seriousness, and pastoral warmth rather than platform intensity.
- Keep one dominant thought controlling the whole manuscript.
- Show real knowledge of the listener's world, pressures, and objections.
- Use illustrations only when they serve the dominant thought.
- Keep the conclusion aimed at the will with a specific response.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the sermon is genuinely expository and text-governed.
- Verify the dominant thought is singular, clear, and repeated.
- Verify the sermon demonstrates double listening to text and world.
- Verify the hearer's silent objections are answered within the sermon.
- Verify the preacher's portrait and hearer's profile affect tone and application.
- Verify the conclusion contains a specific appeal rather than summary alone.
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

