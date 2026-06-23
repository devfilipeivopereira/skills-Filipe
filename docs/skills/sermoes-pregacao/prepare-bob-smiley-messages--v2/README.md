# prepare-bob-smiley-messages--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `prepare-bob-smiley-messages`
- Pacote instalavel: `packages/sermoes-pregacao/prepare-bob-smiley-messages--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\prepare-bob-smiley-messages`
- Hash do `SKILL.md`: `ce76cf404230dc90f20de6fe6f791509533008a633a39545ecbf43ea561abd2e`

## Resumo

Prepare message outlines and full message manuscripts using Bob Smiley's humor-and-narrative communication method, including a real-life humorous story, practical bridge, contextual data, and a biblical punch ending that reveals the truth hidden in the story. Use when the user asks to prepare a message, sermon, talk, devotion, youth message, family message, humorous Christian message, story-first biblical message, or a Bob Smiley style communication based on a lived situation, audience need, or biblical theme.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/prepare-bob-smiley-messages--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `prepare-bob-smiley-messages--v2` |
| Skill name | `prepare-bob-smiley-messages` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\prepare-bob-smiley-messages` |
| Pasta no repositorio | `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2` |
| Arquivo principal | `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/prepare-bob-smiley-messages--v2.zip` |
| Tamanho do zip | 9,8 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | prepare-bob-smiley-messages |
| `description` | Prepare message outlines and full message manuscripts using Bob Smiley's humor-and-narrative communication method, including a real-life humorous story, practical bridge, contextual data, and a biblical punch ending that reveals the truth hidden in the story. Use when the user asks to prepare a message, sermon, talk, devotion, youth message, family message, humorous Christian message, story-first biblical message, or a Bob Smiley style communication based on a lived situation, audience need, or biblical theme. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 7 |
| Diretorios | 3 |
| Tamanho copiado | 22,3 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 222 B |
| `references` | 1 | 3,7 KB |
| `scripts` | 4 | 9,1 KB |

## Secoes internas detectadas

- Prepare Bob Smiley Messages
-   Overview
-   Activation Workflow
-   Originality Requirement
-   Research Requirement
-   Core Method
-   Preparation Sequence
-     1. Collect the Raw Story
-     2. Identify the Hidden Biblical Truth
-     3. Build the Escalation
-     4. Build the Practical Bridge
-     5. Add the Contextual Data Layer
-     6. Land the Biblical Punch
-     7. Write the Opening Last
-   Output Contract
-   Existing Draft Diagnosis
-   Style Rules
-   Document Delivery
-   Hybrid Environment Rules
-   Final Quality Check

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/agents/openai.yaml` | 222 B |
| `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/references/bob_smiley_method.md` | 3,7 KB |
| `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/scripts/config.json` | 457 B |
| `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/scripts/create_message_docx.py` | 1,6 KB |
| `skills/sermoes-pregacao/prepare-bob-smiley-messages--v2/SKILL.md` | 9,3 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\prepare-bob-smiley-messages`

## Conteudo integral do SKILL.md

```
markdown
---
name: prepare-bob-smiley-messages
description: Prepare message outlines and full message manuscripts using Bob Smiley's humor-and-narrative communication method, including a real-life humorous story, practical bridge, contextual data, and a biblical punch ending that reveals the truth hidden in the story. Use when the user asks to prepare a message, sermon, talk, devotion, youth message, family message, humorous Christian message, story-first biblical message, or a Bob Smiley style communication based on a lived situation, audience need, or biblical theme.
---

# Prepare Bob Smiley Messages

## Overview

Prepare messages using Bob Smiley's method: begin with a real-life story that immediately creates identification, escalate the humor through ordinary absurdity, bridge into practical wisdom, add one contextual or factual layer, and land in a biblical punch ending where the audience realizes the story was carrying the truth all along. The default deliverable is a formatted Microsoft Word document.

Read [references/bob_smiley_method.md](references/bob_smiley_method.md) when preparing or reviewing the message. Treat that file as the source of truth for the theology of joy, the four-part structure, the "Average Boy" identification principle, and the diagnostic tests for story, escalation, and punch ending.
Use [scripts/create_message_docx.py](scripts/create_message_docx.py) to convert the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Activation Workflow

When beginning a new preparation flow, immediately determine:

1. What real-life situation from the speaker's own life is available?
2. Who is the audience?
3. Are there any restrictions such as a required text, event, or series theme?

If the user already has a story, build from that story.
If the user does not have a story, help excavate one with prompts such as:

- what happened this week that was absurd, funny, irritating, or unexpectedly revealing
- what recent situation would you retell to a friend because it was ridiculous
- what is your most recent ordinary failure at home, parenting, travel, work, or relationships

If the user brings an existing sermon or talk draft, diagnose it first instead of rewriting blindly.

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

## Core Method

Every message should move through four parts:

1. Humorous story
2. Above-average advice
3. Did-you-know contextual layer
4. Biblical punch ending

The story is not decoration. It is the main vehicle.

The audience should:

- identify before they admire
- laugh before they feel preached at
- recognize the truth at the punch ending

## Preparation Sequence

### 1. Collect the Raw Story

- Use the speaker's own life whenever possible.
- Prefer ordinary situations over dramatic ones.
- Choose stories with built-in absurdity and room for escalation.

### 2. Identify the Hidden Biblical Truth

- Ask what biblical truth the story naturally illustrates.
- Generate several truth candidates if needed.
- Select the truth that emerges most organically from the story.

### 3. Build the Escalation

Shape the story through:

- recognizable starting point
- absurd complication
- escalating absurdity
- unexpected turn

### 4. Build the Practical Bridge

Add one or two practical observations that still sound conversational and story-adjacent.

### 5. Add the Contextual Data Layer

Add one fact, study, cultural observation, or biblical-historical detail that expands the story without interrupting it.

### 6. Land the Biblical Punch

Reveal:

- what the story was really about
- the biblical text that names it
- the deeper truth the audience is now ready to receive
- the specific invitation or response

### 7. Write the Opening Last

The first line should begin in the action, not in topic announcement.

## Output Contract

Before the message body, explicitly declare:

1. The real-life story source:
   - this week
   - recent memory
   - recurring life pattern
   - pastoral experience narrated personally
2. The audience profile:
   - age
   - spiritual maturity
   - main need
   - what would make them resist
3. Any imposed restriction:
   - biblical text
   - theme
   - series
   - event context
4. The four movements:
   - story
   - practical bridge
   - contextual data
   - biblical punch
5. The hidden biblical truth candidates and the chosen one.
6. The escalation plan:
   - situation
   - complication
   - escalation
   - turn
7. The practical bridge statements.
8. The contextual fact or data point and why it helps.
9. The biblical punch text and the invitation.
10. The opening in medias res line.

Then write the message with these clearly signaled sections:

1. Humorous Story
2. Above-Average Advice
3. Did You Know
4. God's Guide
5. Invitation or response

If helpful, add a short final self-review checklist at the end.

## Existing Draft Diagnosis

When reviewing a prewritten message, test it for:

- presence of one central narrative rather than scattered illustrations
- personal identification and vulnerability
- comedic or emotional escalation
- organic connection between story and text
- strength of the punch ending
- specific invitation
- atmosphere of joy instead of defensive seriousness

If the story is missing, rebuild from story first.
If the text is glued on, rebuild the connection.
If the ending works without the story, the story is ornamental and should be strengthened or replaced.

## Style Rules

- Start inside the action.
- Keep the tone clean, warm, and inclusive.
- Use self-deprecation rather than mockery of others.
- Let the story do most of the heavy lifting.
- Prefer lived detail over abstract explanation.
- Keep joy visible even when the message is born from pain.
- Make the biblical ending deeper than the audience expected.
- End with a concrete invitation.
- If the user asks for a full message manuscript and gives no shorter limit, target at least 7,500 words.

## Document Delivery

- Write the message manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_message_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a full message and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the `.docx` result inside [outputs/](outputs/) in this skill folder.
- Deliver the final `.docx` path to the user.

## Hybrid Environment Rules

- Keep the workflow portable between local and cloud environments.
- Put filesystem reads and writes behind `scripts/adapters.py`.
- Keep parsing, word-count enforcement, and `.docx` rendering in `scripts/core.py`.
- Keep defaults such as minimum words and document styles in `scripts/config.json`.
- Prefer relative or configurable paths over machine-specific absolute paths.
- Prefer [outputs/](outputs/) in this skill folder as the default writable destination.
- If the environment blocks writing to the user-requested workspace, fall back to [outputs/](outputs/) in this skill folder and report the final path clearly.

## Final Quality Check

Before delivery, verify:

- the audience identifies with the story immediately
- the story escalates instead of staying flat
- the humor includes rather than wounds
- the bridge grows naturally from the story
- the contextual layer deepens rather than interrupts
- the biblical punch depends on the story for its force
- the invitation is concrete
- the overall atmosphere reflects joy as a pastoral tool
```
