---
name: generate-robin-sharma-talks
description: Generate motivational talk outlines and full talk manuscripts using Robin Sharma's authentic personal mastery and leadership communication methodology, including the Lawyer-to-Leader origin story, the Leadership Without a Title premise, the Four Interior Empires as the holistic mastery framework, the Four Focuses of History Makers as the performance diagnostic, the Victory Hour and 20/20/20 Formula as the morning architecture, the 66-Day Habit Installation Protocol, the 90/90/1 Rule and Tight Bubble of Total Focus as the deep work tools, and a specific Daily Mastery Commitment at the close. Use when the user asks to create a motivational talk, keynote, leadership message, conference speech, personal development address, high-performance culture talk, morning routine keynote, everyday hero message, or any communication about personal leadership, daily mastery, morning rituals, peak performance, self-mastery, leadership without title, inner empire development, or elevating daily life, and wants the result shaped by Robin Sharma, The 5 AM Club, The Monk Who Sold His Ferrari, The Leader Who Had No Title, The Everyday Hero Manifesto, The Greatness Guide, the Victory Hour, the 20/20/20 Formula, the Four Interior Empires, the 66-Day Habit Protocol, the 90/90/1 Rule, or the philosophy of small daily improvements compounding into extraordinary results.
---

# Generate Robin Sharma Talks

## Overview

Generate talks with Robin Sharma's authentic personal mastery methodology: open with the Forgotten Giant provocation — the idea that most people are living far below their native genius — and anchor it with the personal story of leaving a successful legal career to pursue a calling; establish that leadership is not a title but a behavior available to everyone; present the Four Interior Empires as the holistic mastery framework the world's top performers balance; apply the Four Focuses of History Makers as the performance diagnostic; teach the Victory Hour and 20/20/20 Formula as the morning architecture that owns the day before the world intrudes; walk through the 66-Day Habit Installation Protocol to set realistic expectations for transformation; present the 90/90/1 Rule and Tight Bubble of Total Focus as the deep work tools for elite daily output; and close with a specific Daily Mastery Commitment the audience designs before leaving. The default deliverable is a formatted Microsoft Word document.

Read [references/robin_sharma_method.md](references/robin_sharma_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Robin Sharma methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Sharma into a generic productivity talk. Preserve the poetic-aphoristic language register, the Lawyer-to-Leader origin story, the Leadership Without a Title premise, all Four Interior Empires named precisely, all Four Focuses named precisely, the Victory Hour, the 20/20/20 Formula with its three segments (Move, Reflect, Grow) in exactly that order, the three-phase 66-Day Protocol (Destruction/Installation/Integration), the 90/90/1 Rule with its exact name, the Tight Bubble of Total Focus with its exact name, and the Daily Mastery Commitment close.
- Robin Sharma is not a motivational shouter, not a data-driven academic, and not a pastoral mentor. He is a wisdom teacher — combining Eastern philosophy, Western performance science, and literary storytelling in a warm, elevated, somewhat spiritual register. Any manuscript that sounds like Tony Robbins or Adam Grant has failed the fidelity test.
- Sharma's vocabulary is distinctive and must appear: "heroic performer," "daily mastery," "world-class," "genius," "the top 5%," "Victory Hour," "everyday hero," "mediocrity is a habit, so is excellence," "all change is hard at first, messy in the middle, and gorgeous at the end," "own your morning, elevate your life."
- If the user asks for Robin Sharma, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or performance/leadership challenge.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a room of ambitious professionals — executives, entrepreneurs, athletes, creatives — who are achieving by conventional standards but feel they are not operating at their full capacity, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of Robin Sharma while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for:
- Current neuroscience findings on morning routines, cortisol cycles, and cognitive performance peaks.
- Contemporary examples of elite performers (athletes, CEOs, artists) who use morning disciplines.
- Recent research on deep work, focus, and distraction in modern professional environments.
- Robin Sharma's most recent content from his podcast, social media, or books relevant to the theme.

## Preparation Rules

- Identify the specific dimension of the audience's underperformance before building any section — which of the Four Interior Empires is most neglected?
- Answer four questions first:
  - What is the Forgotten Giant argument for this specific audience — in what way are they living below their native potential?
  - Which of the Four Focuses of History Makers is most violated in this audience's context?
  - What is the specific Victory Hour design most relevant to this audience's schedule and challenges?
  - What is the one Daily Mastery Commitment the audience should leave with?
- Write the Central Mantra (the Sharma-style aphorism that encapsulates the talk's transformation) before writing any section.
- The Central Mantra must be short (under 10 words), poetic, and feel like something worth writing on a wall: "Own your morning. Elevate your life." "All change is hard at first, messy in the middle, and gorgeous at the end."
- Design the Daily Mastery Commitment as a specific morning ritual protocol the audience can begin tomorrow — not a vague aspiration.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Central Mantra (the Sharma-style aphoristic phrase that encapsulates the talk).
2. The Forgotten Giant Application (the specific way this audience is living below their native potential).
3. The Neglected Interior Empire (which of the four — Mindset, Heartset, Healthset, Soulset — is most neglected by this audience).
4. The Violated Focus (which of the Four Focuses of History Makers this audience most violates).
5. The Victory Hour Design (the specific 20/20/20 configuration most relevant to this audience).
6. The Historical Figure Anchor (the historical genius, leader, or artist whose morning discipline will be used as proof).
7. The Daily Mastery Commitment (the specific ritual protocol the audience designs at the close).

Then write the talk with these clearly signaled sections:

1. O GIGANTE ESQUECIDO (The Forgotten Giant — the provocation that most people are living far below their native genius)
2. O ADVOGADO QUE VENDEU A FERRARI (Lawyer-to-Leader origin story — the personal calling that required leaving security)
3. LIDERANÇA SEM TÍTULO (Leadership Without a Title — the democratic premise that every person can lead)
4. OS QUATRO IMPÉRIOS INTERIORES (The Four Interior Empires — Mindset, Heartset, Healthset, Soulset)
5. OS QUATRO FOCOS DOS FAZEDORES DA HISTÓRIA (The Four Focuses of History Makers)
6. A HORA DA VITÓRIA E A FÓRMULA 20/20/20 (The Victory Hour and 20/20/20 Formula — Move, Reflect, Grow)
7. O PROTOCOLO DE 66 DIAS (The 66-Day Habit Installation Protocol — Destruction, Installation, Integration)
8. A BOLHA DE FOCO TOTAL E A REGRA 90/90/1 (Tight Bubble of Total Focus + 90/90/1 Rule)
9. O COMPROMISSO DE MAESTRIA DIÁRIA (The Daily Mastery Commitment close)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name, for example: `Maestria_Diaria_Robin_Sharma.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Elevated, poetic, aphoristic register — every key insight must sound like it belongs on a wall or a journal page.
- Use rhetorical parallelism and repetition: triplets, anaphoras, and rhythmic sentence pairs are expected and welcome.
- Reference historical figures: Da Vinci, Churchill, Mandela, Einstein, Marcus Aurelius, Picasso, Mozart, Beethoven as exemplars of the principles being taught.
- Blend Eastern philosophy (Stoicism, Zen, Vedic wisdom) with Western performance neuroscience naturally — not as a gimmick but as the authentic intellectual tradition Sharma draws from.
- Sharma's Aphorism Register: short, declarative, poetic sentences that feel inevitable after they are said.
  - "Mediocrity is a habit. So is excellence."
  - "Your mornings shape your days, and your days shape your life."
  - "The moments of your days become the biography of your life."
  - "All change is hard at first, messy in the middle, and gorgeous at the end."
  - "Leadership is not a title. It's a behavior. Live it now."
  - "Own your morning. Elevate your life."
  - "Small daily improvements over time lead to stunning results."
- Never use motivational-shouter energy (not Tony Robbins). Never use corporate-researcher dryness (not Adam Grant). Never use pure pastoral warmth (not Maxwell). Sharma's register is the wise teacher — warm, demanding, poetic, philosophically grounded.
- The close is a ritual design exercise — specific, morning-anchored, starting tomorrow.

## Quality Check

- Verify the opening is the Forgotten Giant provocation — not a topic announcement.
- Verify the Lawyer-to-Leader story includes the legal career, the calling, and the first Ferrari book.
- Verify Leadership Without a Title is presented as a democratic premise available to everyone regardless of position.
- Verify all Four Interior Empires are named precisely: Mindset, Heartset, Healthset, Soulset.
- Verify all Four Focuses of History Makers are named: talent cultivation, distraction elimination, mastery pursuit, day stacking.
- Verify the Victory Hour is presented as the period 5:00–6:00 AM with its exact name.
- Verify the 20/20/20 Formula presents the three segments in exact order: Move (exercise, 5:00–5:20), Reflect (meditation/journaling, 5:20–5:40), Grow (learning, 5:40–6:00).
- Verify the 66-Day Protocol presents all three phases: Destruction (days 1–22), Installation (days 23–44), Integration (days 45–66).
- Verify the 90/90/1 Rule is named exactly and described correctly (first 90 minutes of workday on the one most important project, for 90 consecutive days).
- Verify the Tight Bubble of Total Focus is named and the five assets of genius are listed: mental focus, physical energy, willpower, original talent, daily time.
- Verify at least three historical figures are referenced as exemplars.
- Verify the Central Mantra appears at least twice in the manuscript.
- Verify the Daily Mastery Commitment is a specific morning ritual protocol — not a vague aspiration.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` and `.epub` have been delivered, the local `outputs/` folder must be emptied while preserving the folder itself.
