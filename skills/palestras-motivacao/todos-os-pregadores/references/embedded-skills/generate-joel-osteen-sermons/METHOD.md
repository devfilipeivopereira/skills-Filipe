---
name: generate-joel-osteen-sermons
description: Generate sermon outlines and full sermon manuscripts using Joel Osteen's preaching method, including a humorous opening, the exact Scripture confession, a short anchor text, a clear positive theme, three cycles of story-principle-Scripture, collective spoken declarations, a warm non-condemning tone, and a closing with hopeful summary, prophetic declaration, and salvation invitation. Use when the user asks to create a sermon, preaching manuscript, Joel Osteen style sermon, hope sermon, favor sermon, identity sermon, victory sermon, or positive faith message based on a Bible text or theme.
---

# Generate Joel Osteen Sermons

## Overview

Generate sermons with Joel Osteen's method: open with clean humor that lowers defenses, lead the congregation in the exact Scripture confession, anchor the message in a short promise-oriented text, develop one clear positive theme through three cycles of story, principle, and Scripture, activate collective spoken declarations, and finish with hope, prophetic blessing, and an invitation to receive Christ. The default deliverable is a formatted Microsoft Word document.

Read [references/joel_osteen_method.md](references/joel_osteen_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for the nine sermon elements, the positive tone, and the structure of declarations and invitation.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Joel Osteen into generic positive preaching. Preserve the exact confession, short anchor text, story-principle-Scripture cycles, collective declarations, and hope-soaked closing.
- If the user asks for Joel Osteen, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume ordinary hearers carrying internal negative narratives who need hope, clarity, and practical faith for the coming week.
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

- Choose a short biblical anchor text, usually one to three verses.
- State the central theme in one clear, positive sentence.
- Prepare one clean opening joke or humorous story with marked timing.
- Build the sermon core through exactly three cycles:
  - story
  - principle
  - biblical story retexturized
- Identify the limiting inner narrative the sermon will replace.
- Write at least two collective declarations with the exact wording the congregation will repeat.
- Maintain a warm, hopeful, and non-condemning tone throughout.
- Prepare a final prophetic declaration over the hearers.
- Include the salvation invitation and the standard salvation prayer text.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The anchor biblical text.
2. The central theme in one sentence.
3. The full opening joke with timing.
4. The three core cycles, naming for each:
   - the story
   - the principle
   - the Scripture
5. The collective declarations with their exact wording.
6. The limiting inner narrative being confronted.
7. The final prophetic declaration over the congregation.
8. The salvation invitation and the exact salvation prayer.

Then write the sermon with these clearly signaled elements:

1. Humorous opening
2. Exact Scripture confession
3. Anchor text and theme declaration
4. Core Cycle 1
5. Collective declaration
6. Core Cycle 2
7. Core Cycle 3
8. Hopeful summary
9. Final prophetic declaration
10. Invitation and salvation prayer

Write the transitions explicitly. Keep the sermon simple enough for an ordinary hearer to understand and carry into Monday.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Joel_Osteen.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Joel_Osteen.epub`.
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

- Start with warmth, humor, and safety.
- Avoid dense theological vocabulary unless immediately translated into plain language.
- Never shame, scold, or condemn the hearer.
- Keep every story concrete and specific, with tension before the turn.
- Repeat the main point through variation so it becomes memorable.
- Finish with hope, spoken blessing, and welcoming invitation rather than obligation.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the opening humor is clean and functional.
- Verify the exact Scripture confession is included unchanged.
- Verify the anchor text is short and clear.
- Verify the sermon core contains three real cycles of story, principle, and Scripture.
- Verify there are at least two spoken collective declarations.
- Verify the sermon ends in hope, prophetic blessing, and invitation.
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

