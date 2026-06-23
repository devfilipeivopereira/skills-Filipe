# generate-john-maxwell-talks--v3

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-john-maxwell-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-john-maxwell-talks--v3.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-john-maxwell-talks--v3`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-john-maxwell-talks`
- Hash do `SKILL.md`: `2194a4c2103837013ba257846d4a23070a090072afc7b850c7ef4ee2bb6476d0`

## Resumo

Generate motivational talk outlines and full talk manuscripts using John C. Maxwell's authentic leadership communication methodology, including the story-first opening, the Central Law stated as a memorable formula, the 5 Levels of Leadership as the primary diagnostic tool, the Law of the Lid to identify the audience's ceiling, the Leader's Ladder as the growth path, the Add Value Challenge, and the Intentional Living close with a specific daily growth commitment. Use when the user asks to create a motivational talk, keynote, leadership message, conference speech, executive development talk, church leadership message, team leader training, organizational culture address, or any communication about leadership, influence, personal growth, people development, or equipping others, and wants the result shaped by John C. Maxwell, The 21 Irrefutable Laws of Leadership, The 5 Levels of Leadership, Developing the Leader Within You, Intentional Living, The Maxwell Leadership Bible, Maxwell Leadership, EQUIP, or the "everything rises and falls on leadership" philosophy.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-john-maxwell-talks--v3.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-john-maxwell-talks--v3` |
| Skill name | `generate-john-maxwell-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-john-maxwell-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-john-maxwell-talks--v3` |
| Arquivo principal | `skills/palestras-motivacao/generate-john-maxwell-talks--v3/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-john-maxwell-talks--v3.zip` |
| Tamanho do zip | 21,2 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-john-maxwell-talks |
| `description` | Generate motivational talk outlines and full talk manuscripts using John C. Maxwell's authentic leadership communication methodology, including the story-first opening, the Central Law stated as a memorable formula, the 5 Levels of Leadership as the primary diagnostic tool, the Law of the Lid to identify the audience's ceiling, the Leader's Ladder as the growth path, the Add Value Challenge, and the Intentional Living close with a specific daily growth commitment. Use when the user asks to create a motivational talk, keynote, leadership message, conference speech, executive development talk, church leadership message, team leader training, organizational culture address, or any communication about leadership, influence, personal growth, people development, or equipping others, and wants the result shaped by John C. Maxwell, The 21 Irrefutable Laws of Leadership, The 5 Levels of Leadership, Developing the Leader Within You, Intentional Living, The Maxwell Leadership Bible, Maxwell Leadership, EQUIP, or the "everything rises and falls on leadership" philosophy. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 54,1 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 250 B |
| `references` | 1 | 24,7 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate John C. Maxwell Talks
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

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/agents/openai.yaml` | 250 B |
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/references/john_maxwell_method.md` | 24,7 KB |
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/scripts/config.json` | 455 B |
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-john-maxwell-talks--v3/SKILL.md` | 12,6 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-john-maxwell-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-john-maxwell-talks
description: Generate motivational talk outlines and full talk manuscripts using John C. Maxwell's authentic leadership communication methodology, including the story-first opening, the Central Law stated as a memorable formula, the 5 Levels of Leadership as the primary diagnostic tool, the Law of the Lid to identify the audience's ceiling, the Leader's Ladder as the growth path, the Add Value Challenge, and the Intentional Living close with a specific daily growth commitment. Use when the user asks to create a motivational talk, keynote, leadership message, conference speech, executive development talk, church leadership message, team leader training, organizational culture address, or any communication about leadership, influence, personal growth, people development, or equipping others, and wants the result shaped by John C. Maxwell, The 21 Irrefutable Laws of Leadership, The 5 Levels of Leadership, Developing the Leader Within You, Intentional Living, The Maxwell Leadership Bible, Maxwell Leadership, EQUIP, or the "everything rises and falls on leadership" philosophy.
---

# Generate John C. Maxwell Talks

## Overview

Generate motivational talks with John C. Maxwell's authentic methodology: open with a personal story that illustrates the central leadership principle before the principle is named, state the Central Law as a short memorable formula, apply the 5 Levels of Leadership or the most relevant Law as the diagnostic framework, identify the Law of the Lid as the invisible ceiling limiting the audience, present the Leader's Ladder as the intentional growth path, issue the Add Value Challenge that defines Maxwell's leadership ethic, and close with the Intentional Living commitment — a specific daily decision the audience makes before leaving. The default deliverable is a formatted Microsoft Word document.

Read [references/john_maxwell_method.md](references/john_maxwell_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the John C. Maxwell methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Maxwell into a generic leadership speech. Preserve the story-first opening, the Central Law formula, the 5 Levels diagnostic, the Law of the Lid, the Add Value Challenge, the mentor-like pastoral tone, and the Intentional Living close with a specific daily commitment.
- Maxwell never shouts, never commands physically, and never uses high-energy stage activation. His authority is warm, earned, and pastoral. Any manuscript that sounds like Tony Robbins or Les Brown has failed the fidelity test.
- If the user asks for John Maxwell, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or leadership challenge.
2. If the user did not provide a theme or challenge, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a room of leaders at multiple organizational levels — executives, managers, pastors, entrepreneurs, and emerging leaders — who are competent professionals but have plateaued at Level 2 or 3 of Maxwell's 5 Levels, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every talk must be newly written for the current request.

- Do not reuse pre-existing talk manuscripts, previous generated files, cached talk bodies, or prior outputs as the draft source.
- Do not paraphrase or lightly adapt an older talk and present it as new work.
- You may reuse the requested theme, verified research material, and the methodological framework, but the manuscript itself must be freshly composed.
- Preserve the distinctive style, structure, rhetoric, and methodology of John C. Maxwell while producing original wording and movement for the present request.
- If the same user asks for the same theme again, write a new talk unless the user explicitly asks for revision of an earlier one.

## Research Requirement

Before drafting the talk, browse the internet to gather fresh, relevant material connected to the leadership theme, audience context, and growth principle.

- Collect current leadership examples, organizational case studies, historical leadership stories, statistics on leadership development, or recent events that genuinely strengthen the talk.
- Prefer recent and reputable sources. Use primary sources whenever possible.
- Maxwell's authentic published frameworks — the 21 Laws, the 5 Levels, the Laws of Growth — may be cited by name and applied as tools.
- Treat online material as support, not as the authority. Maxwell's methodology and the target theme remain primary.
- When a contemporary example, statistic, or factual claim materially shapes the talk, keep the source available for attribution if the user asks.

## Preparation Rules

- Identify the Central Law before building any section. Every Maxwell talk turns on one governing principle stated as a law.
- Answer four questions first:
  - What is the one law or principle that, if the audience understood and applied it, would most change their leadership?
  - What personal story from Maxwell's life (or a leadership figure's life) best illustrates that law before it is named?
  - At what Level of the 5 Levels is this audience currently operating — and what is the specific Lid limiting their ascent?
  - What is the Add Value Challenge — the one concrete behavior the audience must adopt to apply this law?
- Write the Central Law Formula (short, alliterative or memorable, under 12 words) before writing any section.
- Write the opening story before writing the Central Law section — the law must be earned by the story, not announced before it.
- Design the Intentional Living close as a specific daily decision with a named time commitment, not a vague aspiration.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the talk body, explicitly declare:

1. The Central Law Formula (the governing principle in a memorable sentence under 12 words).
2. The Opening Story (the personal or historical narrative that earns the Central Law).
3. The 5 Levels Diagnosis (at which Level is the audience operating, and what is the Lid).
4. The Relevant Maxwell Laws (which of the 21 Laws or 15 Laws of Growth are most applicable).
5. The Add Value Challenge (the specific behavior the audience adopts to apply the law).
6. The Self-Deprecating Humor Moment (the specific moment where Maxwell humanizes himself — mandatory for tone fidelity).
7. The Intentional Living Commitment (the specific daily decision, with time frame, requested at the close).

Then write the talk with these clearly signaled sections:

1. A HISTÓRIA (Story-first opening — the law illustrated before it is named)
2. A LEI CENTRAL (Central Law stated and unpacked as a governing principle)
3. OS 5 NÍVEIS (5 Levels of Leadership diagnostic applied to the audience)
4. A TAMPA (Law of the Lid — the specific ceiling limiting this audience's ascent)
5. A ESCADA DO LÍDER (Leader's Ladder — the intentional growth path upward)
6. O DESAFIO DE AGREGAR VALOR (Add Value Challenge — the leadership ethic in practice)
7. O COMPROMISSO INTENCIONAL (Intentional Living close — specific daily decision)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_talk_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete talk and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the theme plus the speaker name, for example: `Lideranca_e_Influencia_John_Maxwell.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Talks` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Talks` to the user.
- After the `.docx` is created, run [scripts/create_talk_epub.py](scripts/create_talk_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Name the `.epub` using the theme plus the speaker name, for example: `Lideranca_e_Influencia_John_Maxwell.epub`.
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

- Warm, pastoral, mentor-like tone throughout — Maxwell speaks as a trusted older leader investing in the next generation.
- Never use high-energy physical commands. Maxwell does not shout, does not ask the audience to jump, does not do state-break exercises.
- Self-deprecating humor is mandatory — Maxwell regularly makes himself the example of what not to do before he teaches what to do. At least one humor moment per talk.
- Heavy use of personal stories — Maxwell always has at least three anchor stories per talk (opening, mid-talk, and close).
- Every major principle must be formulated as a Law — named, defined, and illustrated with a story and an example.
- Use rhetorical questions that feel like a mentor leaning across the table, not a performer on a stage.
- Alliterative triplets and numbered frameworks are expected and welcome.
- Use the second person warmly, not aggressively: "Você" — not as a command, but as an invitation.
- Write explicit transitions between all seven sections.
- The close must feel like a father sending a son into the world, not a coach sending a team onto the field.
- If the user asks for a full talk and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the opening is a story — not a topic announcement, not a definition, not a question. A story.
- Verify the Central Law is stated as a formula — short, memorable, and alliterative or structurally elegant.
- Verify the 5 Levels diagnostic identifies where the audience currently operates and where the Lid is.
- Verify the Law of the Lid section names the specific invisible ceiling for this audience.
- Verify the Leader's Ladder presents concrete, sequential growth steps — not vague advice.
- Verify the Add Value Challenge names a specific behavior, not a mindset.
- Verify the Intentional Living close includes a specific daily decision with a time frame.
- Verify the self-deprecating humor moment is present and organic.
- Verify the tone is warm and pastoral throughout — not high-energy or commanding.
- Verify at least three anchor stories are present in the manuscript.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Talks\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_TALKS\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
```
