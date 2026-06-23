---
name: generate-sticky-sermons
description: Generate sermon outlines and full sermon manuscripts using the Sticky Sermons methodology by Brandon Kelley and Joe Hoagland, including double exegesis, Gospel Gold, a single Bottom Line, and the six-movement narrative arc. Use when the user asks to create a sermon, preaching manuscript, sermon outline, sermon series message, discussion guide, or action-focused message based on a Bible text or theme and wants the result shaped by Sticky Sermons, Brandon Kelley, Joe Hoagland, RookiePreacher, Preach and Lead, or the Engage-Tension-Truth-Application-Inspiration/Reflection-Action structure.
---

# Generate Sticky Sermons

## Overview

Generate sermons with the Sticky Sermons system: exegete the text and the people, identify Gospel Gold, define one Bottom Line, build the sermon as a six-movement story arc, and land in one clear action. The default deliverable is a formatted Microsoft Word document.

Read [references/sticky_sermons_method.md](references/sticky_sermons_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Sticky Sermons into generic story preaching. Preserve double exegesis, Gospel Gold, one Bottom Line, the six-movement arc, and one concrete action step.
- If the user asks for Sticky Sermons, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a general evangelical audience that includes seekers, skeptics, and church regulars, and produce a complete sermon manuscript.
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

- Start with double exegesis: the text and the people.
- Identify the listener's real tension before outlining the sermon.
- Define the Gospel Gold with `Lie`, `Longing`, and `Light` before drafting.
- Write the Bottom Line before writing the body of the sermon.
- Keep the whole sermon built around one idea and one action.
- Use the six movements in order: Engage, Tension, Truth, Application, Inspiration or Reflection, Action.
- Do not resolve tension before Truth.
- Let Application emerge from Truth, but still give it a distinct landing.
- Choose only one form for movement 5: Inspiration or Reflection.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The exegeted listener tension in one sentence.
2. The Gospel Gold:
   - Lie
   - Longing
   - Light
3. The final Bottom Line.
4. The type of movement 5: Inspiration or Reflection.
5. The specific Action step.

Then write the sermon with this sequence:

1. Engage
2. Tension
3. Truth
4. Application
5. Inspiration or Reflection
6. Action

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher label for this skill, for example: `JoÃ£o_9_Sticky_Sermons.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher label for this skill, for example: `JoÃ£o_9_Sticky_Sermons.epub`.
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

- Prefer clarity, movement, and memorability over volume.
- Write in a conversational voice, not an essay voice.
- Open with a story, question, fact, quote, or daily-life scene, not the text.
- Keep the sermon moving like a story arc rather than a static outline.
- Repeat the Bottom Line two or three times after its first appearance.
- Make the Gospel Gold feel organic to the sermon, not bolted on.
- End with one clear action, not a vague reflection cloud.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the listener tension is real, not artificial.
- Verify the Gospel Gold is explicit and connected to Christ.
- Verify the Bottom Line is short, declarative, memorable, and central.
- Verify each movement does its own job and stays in order.
- Verify Inspiration or Reflection is chosen intentionally and not merged into generic explanation.
- Verify the final action is singular, specific, and doable this week.
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

