---
name: generate-rick-blackwood-sermons
description: Generate sermon outlines and full sermon manuscripts using Rick Blackwood's multisensory preaching method, including a clear Big Idea, pre-sermon environment design, sensory anchors for each expositional point, a progressive listening guide with fill-in participation, a surprise sensory element, and a concrete written and spoken application that produces hearers who become doers. Use when the user asks to create a sermon, preaching manuscript, multisensory sermon, Rick Blackwood style sermon, Big Idea sermon, listening guide sermon, or attention-comprehension-retention message based on a Bible text or theme.
---

# Generate Rick Blackwood Sermons

## Overview

Generate sermons with Rick Blackwood's multisensory method: expose the biblical text faithfully, formulate one clear Big Idea early, prepare the room before the sermon begins, anchor each major point with a visual or interactive reinforcement, guide the congregation with a listening guide they actively fill in, use a memorable surprise element responsibly, and finish with a specific action the hearer says, writes, and prays. The default deliverable is a formatted Microsoft Word document.

Read [references/rick_blackwood_method.md](references/rick_blackwood_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the three communication channels, the eight sermon phases, and the listening-guide centered design.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Rick Blackwood into generic practical preaching. Preserve the Big Idea, pre-sermon environment, sensory anchors, listening guide, surprise element, and concrete doing application.
- If the user asks for Rick Blackwood, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a congregation that needs strong retention, active participation, and a concrete step of obedience this week.
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

- Begin with the exegetical result of the text in its original context.
- Formulate one Big Idea in ordinary language that any hearer can repeat.
- Decide what the congregation will see before the sermon begins:
  - object
  - staging element
  - projected image
  - sound cue
- Plan a multisensory opening that creates curiosity without revealing everything too soon.
- Assign a sensory anchor to each main point of the exposition.
- Design a listening guide with:
  - fill-in blanks
  - application questions
  - final written commitment
- Choose one surprise element that serves the truth rather than spectacle.
- Make the weekly application specific, written, verbalized, and prayed.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The biblical text and the exegetical result.
2. The Big Idea in one sentence.
3. The pre-sermon environment already in place when the congregation arrives.
4. The multisensory opening and how it creates the hearer's unspoken question.
5. The main prop or visual tool for each major point.
6. The surprise element and what truth it anchors.
7. The complete structure of the listening guide.
8. The concrete and verifiable application for this week.

Then write the sermon with these clearly signaled phases:

1. Phase 0: Pre-sermon sensory environment
2. Phase 1: Multisensory opening
3. Phase 2: Big Idea announced
4. Phase 3: Verse-by-verse exposition with sensory anchors
5. Phase 4: Multisensory illustrations
6. Phase 5: Surprise element
7. Phase 6: Concrete application
8. Phase 7: Congregational interaction
9. Phase 8: Multisensory closing review and call to action

Write the transitions explicitly. Make clear what the congregation sees, hears, writes, says, or touches at each key moment.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Rick_Blackwood.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Rick_Blackwood.epub`.
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

- Keep the Bible expositionally primary and the sensory tools functionally secondary.
- Make each sensory element directly serve a biblical truth.
- State the Big Idea early and repeat it clearly.
- Design for attention, comprehension, and retention, not novelty alone.
- Let the congregation participate actively throughout the sermon.
- End with concrete obedience rather than general inspiration.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the Big Idea is clear and memorable.
- Verify the environment begins communicating before the sermon starts.
- Verify each major point has a sensory anchor.
- Verify the listening guide requires active writing, not passive reading.
- Verify the surprise element serves truth rather than gimmick.
- Verify the application is specific, written, spoken, and prayed.
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

