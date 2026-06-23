---
name: generate-eugene-lowry-sermons
description: Generate sermon outlines and full sermon manuscripts using Eugene Lowry's narrative preaching method, including the Lowry Loop, a sensed discrepancy, deepened complication, an unexpected Gospel reversal, experiential Good News, and open-ended consequences grounded in grace rather than moralism. Use when the user asks to create a sermon, preaching manuscript, Eugene Lowry style sermon, narrative sermon, Lowry Loop sermon, New Homiletic sermon, or conflict-to-Gospel message based on a Bible text or theme.
---

# Generate Eugene Lowry Sermons

## Overview

Generate sermons with Eugene Lowry's narrative method: upset the equilibrium, deepen the discrepancy until the hearer is genuinely stuck, reveal the Gospel clue as an unexpected reversal, let the hearer experience the Good News rather than merely hear about it, and end by opening possibilities rather than assigning tasks. The default deliverable is a formatted Microsoft Word document.

Read [references/eugene_lowry_method.md](references/eugene_lowry_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the Lowry Loop, the five stages, and the distinction between Gospel reversal and moralism.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Eugene Lowry into generic narrative preaching. Preserve the Lowry Loop, delayed disclosure, discrepancy, reversal, experiential gospel, and open-ended consequence.
- If the user asks for Eugene Lowry, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume hearers who need to be taken through a real temporal journey of tension, reversal, and Gospel possibility rather than a deductive list of points.
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

- Identify where the text itself contains an unexpected reversal that can feed Stage 3.
- Define the homiletical conflict as a lived discrepancy, not merely an intellectual question.
- Make clear why the obvious human solution does not work.
- Distinguish sharply between Gospel reversal and any moralistic counterfeit.
- Decide what possibilities Stage 5 opens instead of which tasks it imposes.
- Identify the specific `Aha!` sentence or turn that will mark the pivot of the loop.
- Keep the sermon temporal and narrative; do not announce the destination too early.
- Let the sermon sound like language for the ear: short sentences, real rhythm, audible images, and implied pauses.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The central biblical text and where it contains its own unexpected reversal.
2. The homiletical conflict.
3. Why the obvious solution does not work.
4. The Gospel reversal: what God has done or is doing.
5. How this differs from moralism that may sound similar.
6. The possibilities opened in Stage 5.
7. The image, question, or vision with which the sermon will end.
8. The specific `Aha!` moment or sentence.

Then write the sermon with these clearly signaled stages:

1. Stage 1: Upsetting the equilibrium
2. Stage 2: Analyzing the discrepancy
3. Stage 3: Disclosing the clue to resolution
4. Stage 4: Experiencing the Gospel
5. Stage 5: Anticipating the consequences

Write the transitions explicitly. Keep Stage 2 substantial enough that the resolution has proportional weight. End open-handedly with possibility rather than a list of tasks.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Eugene_Lowry.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Eugene_Lowry.epub`.
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

- Never reveal the destination too early.
- Keep the conflict experiential, not merely conceptual.
- Let the Gospel reversal come as surprising gift rather than self-help advice.
- Give real room for Stage 4 so the hearer can inhabit the Good News.
- Let Stage 5 open horizons instead of assigning burdens.
- Write for the ear, with implied pauses around the sermon's weightiest moments.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the opening creates a real bind rather than just introducing a topic.
- Verify Stage 2 deepens the problem and disproves the obvious fix.
- Verify the Stage 3 turn is truly Gospel and not disguised moralism.
- Verify Stage 4 lets the hearer experience the Good News concretely.
- Verify Stage 5 opens possibilities, not duty lists.
- Verify the sermon remains a temporal journey rather than a deductive outline.
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

