---
name: generate-louie-giglio-sermons
description: Generate sermon outlines and full sermon manuscripts using Louie Giglio's preaching method, including a horizon-expanding opening, a named giant diagnosed with compassion, a God-centered reading of the biblical text, an indescribable moment of divine greatness, personal vulnerability before breakthrough, a transition into worship, and an integrated invitation to respond to Jesus. Use when the user asks to create a sermon, preaching manuscript, Louie Giglio style sermon, Passion style message, worship-centered sermon, giant-fighting sermon, or glory-to-heart sermon based on a Bible text or theme.
---

# Generate Louie Giglio Sermons

## Overview

Generate sermons with Louie Giglio's method: start by widening the hearer's horizon beyond the immediate, name the giant with honesty and pastoral specificity, enter the text asking what it reveals about who God is, dramatize the biblical moment until God's greatness becomes visceral, connect that greatness to the hearer's actual struggle, and let the sermon dissolve naturally into worship and invitation. The default deliverable is a formatted Microsoft Word document.

Read [references/louie_giglio_method.md](references/louie_giglio_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the eight phases, the three theological anchors, and the movement from greatness to proximity.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Louie Giglio into generic worship preaching. Preserve the horizon-expanding opening, compassionate giant diagnosis, God-centered text reading, indescribable moment, vulnerability, worship turn, and invitation to Jesus.
- If the user asks for Louie Giglio, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume hearers whose vision has shrunk around their own struggle and who need to see God become greater than the giant in front of them.
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

- Decide what "larger world" will expand the horizon in Phase 1:
  - cosmos
  - creation
  - sharp cultural observation
  - personal vulnerability
- Name the giant precisely and pastorally.
- Enter the text with the controlling question:
  - what does this reveal about who God is?
- Identify the exact revelatory moment where God's character becomes unmistakable in the text.
- Build the sermon's governing equation:
  - the greatness of God revealed in this text is greater than the hearer's giant
- Include one honest personal narrative with the breaking point before the turn.
- Decide how the sermon will move into worship:
  - music
  - prayer
  - silence
  - declaration
- Include invitation for both:
  - the one who does not know Jesus
  - the one who knows Jesus but has let the giant dominate the field of vision
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The larger world of Phase 1 and the specific image or data point that will be used.
2. The named giant of Phase 2.
3. The central question for the text: what does this reveal about who God is?
4. The revelatory moment in the biblical narrative where God appears as the transforming agent.
5. The sermon's equation: how God's greatness in this text is greater than the named giant.
6. The personal vulnerability narrative and its breaking point.
7. How the sermon will dissolve into worship.
8. The invitation to commitment for both the unconverted and the distant believer.

Then write the sermon with these clearly signaled phases:

1. Phase 1: Establishing the larger world
2. Phase 2: Honest diagnosis of the human condition
3. Phase 3: Entering the text with God as the greatest character
4. Phase 4: The encounter from giant to Shepherd
5. Phase 5: Personal narrative as evidence
6. Phase 6: Resolution in one capturing sentence
7. Phase 7: Transition to worship
8. Phase 8: Invitation to commitment

Write the transitions explicitly. Keep the whole sermon ordered toward the fame of Jesus and toward worship rather than mere improvement.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Louie_Giglio.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Louie_Giglio.epub`.
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

- Always begin by making God bigger in the hearer's sight before shrinking the giant.
- Diagnose the giant with compassion, not accusation.
- Keep God as the main actor in the biblical scene.
- Include one real "indescribable" moment where God's greatness becomes visceral.
- Let personal testimony function as evidence, never as self-heroics.
- End in worship and encounter rather than in a task list.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the opening expands the hearer's horizon.
- Verify the giant is specific and pastorally named.
- Verify the text is read through the question of who God is.
- Verify the sermon's equation between God's greatness and the giant is explicit.
- Verify a real worship transition is present.
- Verify the invitation is integrated with the sermon's theology.
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

