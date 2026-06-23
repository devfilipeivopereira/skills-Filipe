---
name: generate-joyce-meyer-sermons
description: Generate sermon outlines and full sermon manuscripts using Joyce Meyer's practical teaching method, including naming the specific mental pattern behind the struggle, Scripture as practical instruction, honest testimony with the breaking point before the process of change, concrete numbered tools for daily life, identity in Christ declarations, and a grace-based closing challenge for the week. Use when the user asks to create a sermon, preaching manuscript, Joyce Meyer style sermon, Battlefield of the Mind sermon, practical transformation sermon, identity sermon, emotional healing sermon, or mind-renewal message based on a Bible text or theme.
---

# Generate Joyce Meyer Sermons

## Overview

Generate sermons with Joyce Meyer's practical transformation method: begin with real-life identification through vulnerability, humor, or provocation, name the specific mental pattern behind the hearer's struggle, anchor the teaching in direct practical Scripture, show the preacher's process and breaking point honestly, deliver numbered tools for the week, confront lovingly, declare identity in Christ, and close with grace, action, and spoken declaration. The default deliverable is a formatted Microsoft Word document.

Read [references/joyce_meyer_method.md](references/joyce_meyer_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the eight phases, the six thematic pillars, and the practical, mind-renewing logic of the method.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Joyce Meyer into generic practical teaching. Preserve the exact mind pattern diagnosis, testimony arc, numbered tools, identity declarations, and grace-based challenge.
- If the user asks for Joyce Meyer, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume hearers carrying real emotional pain, destructive thought patterns, and ordinary weekly struggles who need practical tools more than abstract theory.
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

- Identify which of the six Joyce Meyer pillars is central to the sermon.
- Name the exact thought pattern, not only the outward behavior or emotion.
- Choose an opening form:
  - personal vulnerability
  - situational humor
  - provocative statement
- Select anchor Scriptures that answer the named pattern directly.
- Include one honest testimony that shows the breaking point before the process of change.
- Prepare concrete numbered tools the hearer can use this week.
- Write at least one spoken collective declaration with the exact wording.
- End with grace-based encouragement, a specific weekly action, and direct prayer.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The central thematic pillar or pillars.
2. The exact thought pattern being named.
3. The form of the opening and the specific opening story or statement.
4. The anchor Scriptures and how each answers the named pattern.
5. The specific personal testimony including the breaking point.
6. The practical numbered tools for the hearer.
7. The exact wording of the collective declaration.
8. The specific and verifiable action challenge for this week.

Then write the sermon with these clearly signaled phases:

1. Phase 1: Opening with vulnerability, humor, or provocation
2. Phase 2: Naming the real struggle
3. Phase 3: Biblical anchoring
4. Phase 4: Personal testimony as evidence
5. Phase 5: Practical tools and numbered steps
6. Phase 6: Strategic humor
7. Phase 7: Direct but loving confrontation
8. Phase 8: Grace-based encouragement, action, declaration, and prayer

Write the transitions explicitly. Keep every phase practical enough that the hearer knows what to do on Monday, not just what to admire on Sunday.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Joyce_Meyer.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Joyce_Meyer.epub`.
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

- Speak directly, warmly, and plainly.
- Never start with abstract theology detached from lived pain.
- Name the struggle precisely enough that the hearer feels seen.
- Use Scripture as practical instruction, not as distant theory.
- Let humor increase receptivity, not replace the hard truth.
- Confront directly, but always with explicit affection and solidarity.
- End with grace, identity, and a specific step for the week.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the sermon names a specific mental pattern rather than only general emotion.
- Verify the Scripture directly addresses that pattern.
- Verify the testimony includes the breaking point and process, not only the victory.
- Verify practical tools are specific, numbered, and usable this week.
- Verify confrontation is balanced by affection and grace.
- Verify the ending includes declaration and prayer, not diagnosis only.
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

