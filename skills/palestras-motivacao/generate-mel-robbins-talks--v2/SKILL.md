---
name: generate-mel-robbins-talks
description: Generate motivational talk outlines and full talk manuscripts using Mel Robbins's authentic behavioral science methodology, including the raw personal confession opening, the neurological diagnosis of the action gap, the Five Second Rule demonstrated live, varied application stories, the Let Them Theory relational extension, and a specific behavioral commitment close. Use when the user asks to create a motivational talk, keynote, behavior-change message, anti-procrastination talk, productivity keynote, action-focused message, or science-backed motivational address and wants the result shaped by Mel Robbins, The 5 Second Rule, The Let Them Theory, The High 5 Habit, how to stop screwing yourself over, activation energy, parent yourself, anti-motivation science, or Mel Robbins's no-BS behavioral coaching style.
---

# Generate Mel Robbins Talks

## Overview

Generate motivational talks with Mel Robbins's authentic methodology: open with a raw, unpolished personal confession of failure, diagnose the neurological mechanism behind the action gap without blame, present the Five Second Rule and demonstrate it live, prove it works through varied real-world application stories, extend it to the relational domain with the Let Them Theory, and close with one specific behavioral commitment for the next 24 hours. The default deliverable is a formatted Microsoft Word document.

Read [references/mel_robbins_method.md](references/mel_robbins_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Mel Robbins methodology.
- Follow every non-negotiable in that reference exactly.
- Do not flatten Mel Robbins into a generic productivity talk. Preserve the raw personal confession, the neurological diagnosis, the live demonstration of the Five Second Rule, the varied application stories, the Let Them Theory, and the behavioral commitment close.
- The authority of Mel Robbins comes from having been at the bottom — the rule was born from failure, not from success. Without the confession, the rule is a self-help trick. With the confession, it is a survival mechanism tested in crisis.

## Workflow

1. Confirm the theme or behavioral gap being addressed.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile or context, assume a room of professionals or individuals who know exactly what they need to do but keep finding reasons not to do it, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of Mel Robbins while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for:
- current neuroscience findings on habit formation, the prefrontal cortex, and the impulse-to-action window.
- current behavioral science research on procrastination and self-sabotage.
- recent real-world applications of the Five Second Rule in varied contexts (sales, parenting, health, creative work).

## Preparation Rules

- Identify the specific behavioral gap the audience is stuck in before building any section.
- Answer three questions first:
  - What is the exact moment between wanting to act and not acting that this audience recognizes?
  - What is the specific self-sabotage narrative the audience's brain runs in that moment?
  - What would change in this audience's life in 24 hours if they used the Five Second Rule once?
- Write the Behavioral Commitment (the one specific action the audience will do in the next 24 hours) before writing the talk body — the entire talk is built backward from that commitment.
- Write the Raw Confession before writing any other section — without it the rule is advice, not testimony.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Behavioral Gap (the specific moment between intention and action where this audience gets stuck).
2. The Raw Confession (the personal failure story from which the rule was born).
3. The Neurological Mechanism (the specific brain process that sabotages action in the 5-second window).
4. The Live Demonstration Design (how the 5-4-3-2-1 will be demonstrated with this audience).
5. The Application Story Set (three varied contexts where the rule solves the behavioral gap).
6. The Let Them Application (how the Let Them Theory connects to this audience's relational challenges).
7. The Behavioral Commitment (the specific action the audience commits to in the next 24 hours).

Then write the talk with these clearly signaled sections:

1. A CONFISSÃO CRUA (Raw personal failure confession)
2. O DIAGNÓSTICO NEUROLÓGICO (Neurological mechanism — no blame, just mechanics)
3. A REGRA DOS 5 SEGUNDOS (The rule explained and demonstrated live)
4. AS HISTÓRIAS DE APLICAÇÃO (Three varied application stories)
5. O LET THEM (Relational extension — releasing control of others)
6. O COMPROMETIMENTO COMPORTAMENTAL (One specific action in the next 24 hours)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name, for example: `Regra_5_Segundos_Mel_Robbins.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Sound like someone who has been at the bottom and found one thing that worked — not a guru, a survivor.
- Use plain, direct language: no metaphysical language, no guru vocabulary.
- Frustration is authentic and allowed: "E eu sei que você sabe o que deveria fazer. Esse é o problema. Você já sabe. Então por que não faz?"
- Use science language accessibly: "córtex pré-frontal" can be called "a parte do seu cérebro que toma decisões" — but both accuracy and accessibility matter.
- The countdown 5-4-3-2-1 must appear in the text exactly as a countdown — not summarized.
- Explicit stage directions for the live demonstration: [PEDE QUE A PLATEIA SE LEVANTE], [CONTA JUNTO: 5-4-3-2-1], [A PLATEIA AGE].
- The close is always behavioral and specific — never inspirational and vague.

## Quality Check

- Verify the opening is a raw, unfiltered personal failure story — not a polished success story.
- Verify the neurological diagnosis removes blame from the audience: the brain is doing its job — its job is survival, not ambition.
- Verify the Five Second Rule is explained in one clean sentence before it is demonstrated.
- Verify the live demonstration is designed and explicit, with stage directions.
- Verify three application stories cover meaningfully different life contexts.
- Verify the Let Them Theory is presented as a relational extension of the same principle.
- Verify the close requests one specific, time-bound, behavioral action — not a mindset shift.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` and `.epub` have been delivered, the local `outputs/` folder must be emptied while preserving the folder itself.
