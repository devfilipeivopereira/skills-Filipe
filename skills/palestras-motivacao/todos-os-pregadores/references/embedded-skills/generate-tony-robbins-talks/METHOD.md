---
name: generate-tony-robbins-talks
description: Generate motivational talk outlines and full talk manuscripts using Tony Robbins's authentic peak-state methodology, including state-break opening, the Triad (Physiology, Language, Focus), the Six Human Needs diagnosis, pattern interrupt, live intervention, incantation, and a commitment-driven close. Use when the user asks to create a motivational talk, keynote, conference message, leadership speech, team training, or high-energy transformational message based on a theme, audience problem, or transformation goal and wants the result shaped by Tony Robbins, Unleash the Power Within, Date With Destiny, peak performance, state management, the Six Human Needs, NLP-based communication, or Tony Robbins style energy-driven persuasion.
---

# Generate Tony Robbins Talks

## Overview

Generate motivational talks with Tony Robbins's authentic methodology: engineer the audience's emotional state before delivering any content, diagnose the invisible pattern keeping people stuck, present the Triad and Six Human Needs as diagnostic tools, demonstrate the pattern-break live, install a new language pattern through incantation, cast a vivid sensory vision of the transformed future, and close with a specific public commitment. The default deliverable is a formatted Microsoft Word document.

Read [references/tony_robbins_method.md](references/tony_robbins_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Tony Robbins methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Tony Robbins into a generic motivational speech. Preserve the state-break opening, the Triad, the Six Human Needs, live demonstration, incantation, vision sequence, and public commitment close.
- If the user asks for Tony Robbins, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or audience problem.
2. If the user did not provide a theme or problem, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a mixed room of professionals, entrepreneurs, and high achievers who are stuck between knowing and doing, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every talk must be newly written for the current request.

- Do not reuse pre-existing talk manuscripts, previous generated files, cached talk bodies, or prior outputs as the draft source.
- Do not paraphrase or lightly adapt an older talk and present it as new work.
- You may reuse the requested theme, verified research material, and the methodological framework, but the manuscript itself must be freshly composed.
- Preserve the distinctive style, structure, rhetoric, and methodology of Tony Robbins while still producing original wording and movement for the present request.

## Research Requirement

Before drafting the talk, browse the internet to gather fresh, relevant material connected to the theme, audience, and transformation goal.

- Collect current illustrations, statistics, neuroscience findings, cultural references, or recent events only when they genuinely strengthen the talk.
- Prefer recent and reputable sources. Use primary sources whenever possible.
- Keep only the most useful researched material. Do not overload the talk with internet findings.
- Verified scientific claims about neurology, behavior, or motivation must be sourced and available for attribution if the user asks.

## Preparation Rules

- Identify the specific invisible pattern keeping the audience stuck before building any section.
- Answer three questions first:
  - What is the gap between what the audience knows and what they do?
  - Which Human Need is most active in maintaining the stuck pattern?
  - What specific state-break will shift the audience physiology in the first 3 minutes?
- Write the Anchor Idea (the single memorable phrase that encapsulates the talk's transformation) before writing the talk body.
- Keep the Anchor Idea under 10 words.
- Build the state-break before building any content — Robbins never delivers content to a passive audience.
- Design the incantation before writing the talk — it must reinforce the Anchor Idea.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the talk body, explicitly declare:

1. The Anchor Idea (the single memorable phrase that encapsulates the transformation).
2. The Invisible Pattern being diagnosed (the specific mechanism keeping the audience stuck).
3. The Primary Human Need being reoriented.
4. The State-Break Method for the opening (specific physical command or question).
5. The Incantation (the phrase the audience will repeat aloud with physical movement).
6. The Vision Sequence target (what the audience will vividly experience during the future visualization).
7. The Public Commitment requested at the close.

Then write the talk with these clearly signaled sections:

1. RUPTURA DE ESTADO (State Break — first 3–5 minutes)
2. DIAGNÓSTICO (Pattern Identification — naming the invisible mechanism)
3. IDENTIFICAÇÃO (Personal story of failure, not triumph)
4. MODELO (The Triad + Six Human Needs as diagnostic tools)
5. DEMONSTRAÇÃO (Live pattern-break with audience)
6. INCANTAÇÃO (New language pattern installed collectively)
7. VISÃO (Sensory future visualization)
8. COMPROMETIMENTO (Specific public commitment close)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_talk_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete talk and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the theme plus the speaker name, for example: `Mudanca_de_Padrao_Tony_Robbins.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Talks` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Talks` to the user.
- After the `.docx` is created, run [scripts/create_talk_epub.py](scripts/create_talk_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Name the `.epub` using the theme plus the speaker name, for example: `Mudanca_de_Padrao_Tony_Robbins.epub`.
- Deliver the final `.epub` path to the user alongside the `.docx` path.
- Only after both files are delivered, delete all contents inside [outputs/](outputs/) while preserving the folder itself.

## Hybrid Environment Rules

- Keep the talk-generation workflow portable between local and cloud environments.
- Put filesystem reads and writes behind `scripts/adapters.py`.
- Keep parsing, word-count enforcement, and `.docx` rendering in `scripts/core.py`.
- Keep defaults such as minimum words and document styles in `scripts/config.json`.
- Prefer relative or configurable paths over machine-specific absolute paths.
- If the environment blocks writing to the user-requested workspace, fall back to [outputs/](outputs/) and report the final path clearly.

## Style Rules

- High physical energy must be felt on the page — use short punchy sentences, sudden tonal shifts, CAPS for incantations.
- Sound like someone who believes this with their whole body, not just their mind.
- Use the second person aggressively: "você", "seu", "você vai".
- Use rhetorical repetition as a device (anaphora, escalating triplets).
- Write explicit stage directions for the speaker: [PAUSE], [RAISE VOICE], [WALK INTO AUDIENCE], [LOWER VOICE TO NEAR WHISPER].
- Include collective response cues: [A PLATEIA RESPONDE: ___________].
- Treat the talk as a live intervention, not a speech delivery.
- If the user asks for a full talk and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the talk opens with a physical state-break in the first paragraph.
- Verify the Anchor Idea is short, visceral, and actionable.
- Verify DIAGNÓSTICO names the invisible mechanism — not the surface symptom.
- Verify IDENTIFICAÇÃO contains a story of failure and vulnerability, not triumph.
- Verify MODELO explains the Triad and at least two relevant Human Needs.
- Verify DEMONSTRAÇÃO involves live audience interaction.
- Verify INCANTAÇÃO is a short phrase repeated with physical movement.
- Verify VISÃO uses all five senses in the future visualization.
- Verify COMPROMETIMENTO requests a specific, audible, immediate commitment.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Talks\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_TALKS\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.

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

