---
name: generate-simon-sinek-talks
description: Generate motivational talk outlines and full talk manuscripts using Simon Sinek's authentic Golden Circle methodology, including the unanswered question opening, the Why-How-What contrast, case-based proof, limbic brain neuroscience, the inspiring human story, and a quiet invitation close. Use when the user asks to create a motivational talk, keynote, leadership message, conference talk, corporate speech, or purpose-driven communication based on a theme, leadership challenge, or organizational problem and wants the result shaped by Simon Sinek, Start With Why, The Golden Circle, Leaders Eat Last, The Infinite Game, limbic brain communication, purpose-driven leadership, or North Star leadership culture.
---

# Generate Simon Sinek Talks

## Overview

Generate motivational talks with Simon Sinek's authentic methodology: open with a clean question no one has asked, contrast two real-world cases (one inspiring, one not), present the Golden Circle as a neurological and organizational framework, legitimate it with limbic brain science, build to an emotionally resonant story of sacrifice and purpose, and close with a quiet, unhurried invitation to find the Why. The default deliverable is a formatted Microsoft Word document.

Read [references/simon_sinek_method.md](references/simon_sinek_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Simon Sinek methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Simon Sinek into a generic leadership speech. Preserve the unanswered-question opening, the Golden Circle, the contrasting cases, the limbic brain explanation, the human story of sacrifice, and the quiet invitation close.
- If the user asks for Simon Sinek, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or leadership/organizational problem.
2. If the user did not provide a theme or problem, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a room of leaders, managers, or professionals seeking meaning and direction in their work, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every talk must be newly written for the current request.

- Do not reuse pre-existing talk manuscripts or prior outputs.
- Preserve the distinctive style, structure, and methodology of Simon Sinek while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet to gather fresh, relevant material connected to the theme and audience.

- Collect current examples of organizations or leaders that demonstrate Why-first vs. What-first behavior.
- Prefer recent and reputable sources.
- Verified neuroscience claims about the limbic brain and decision-making must be attributable.

## Preparation Rules

- Identify the unanswered question before building any section.
- Answer two questions first:
  - What pattern of behavior does the audience recognize but has never been able to explain?
  - What contrasting case makes the Golden Circle immediately visible?
- Write the Central Why (the single articulation of purpose the talk argues for) before writing the talk body.
- Identify the human story that will serve as the emotional peak — it must be a story of sacrifice, not success.
- Identify the contrasting case pair (one inspiring, one not) before writing the talk.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Unanswered Question (the clean opening question that creates the cognitive gap).
2. The Golden Circle Application (What / How / Why for the specific context).
3. The Contrasting Case Pair (inspiring case and non-inspiring case).
4. The Central Why (the purpose statement the talk argues for).
5. The Human Story (the sacrifice or purpose story used as the emotional peak).
6. The Limbic Brain Bridge (the specific neuroscience point used to legitimate the framework).
7. The Quiet Invitation (the exact phrasing of the unhurried close).

Then write the talk with these clearly signaled sections:

1. A PERGUNTA (The unanswered question — clean opening)
2. O CONTRASTE (Two real cases demonstrating the pattern)
3. O MODELO (The Golden Circle presented visually and explained)
4. A NEUROCIÊNCIA (Limbic brain legitimation)
5. A HISTÓRIA (Human story of sacrifice or purpose under pressure)
6. O CONVITE (Quiet, unhurried invitation to find the Why)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_talk_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete talk and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- Name the `.docx` using the theme plus the speaker name, for example: `Lideranca_Inspiradora_Simon_Sinek.docx`.
- After saving the `.docx`, copy it to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- After the `.docx` is created, run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user.
- After delivery, empty [outputs/](outputs/) while preserving the folder.

## Style Rules

- Calm, unhurried delivery tone on the page — no exclamation marks in explanatory sections.
- Sound like someone who has just discovered something obvious that no one had noticed.
- Use clean, declarative sentences: short, direct, free of jargon.
- Build tension through contrast, not through emotional escalation.
- Let the cases do the work — the framework explains why the cases are what they are.
- Explicit transitions between all six sections.
- The close must never apply pressure. It must feel like an open door, not a command.

## Quality Check

- Verify the opening is a clean question that creates a cognitive gap.
- Verify the contrasting cases are real and specific.
- Verify the Golden Circle is drawn and explained in lay terms.
- Verify the limbic brain explanation makes the framework scientific, not merely rhetorical.
- Verify the human story is about sacrifice or purpose — not about ROI or success metrics.
- Verify the close is an invitation, not a call-to-action with urgency.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` and `.epub` have been delivered, the local `outputs/` folder must be emptied while preserving the folder itself.

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

