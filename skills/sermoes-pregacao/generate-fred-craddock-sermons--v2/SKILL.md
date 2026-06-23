---
name: generate-fred-craddock-sermons
description: Generate sermon outlines and full sermon manuscripts using Fred B. Craddock's inductive preaching method, including the three movements of Knot, Shock, and New Hearing, the instruments of shuttle, spiral, and shock, one distilled sermon sentence, and an intentionally open ending. Use when the user asks to create a sermon, preaching manuscript, sermon outline, narrative homiletic message, discovery-based sermon, or New Homiletic style message based on a Bible text or theme and wants the result shaped by Fred Craddock, inductive preaching, New Homiletics, discovery preaching, or sermon-as-journey communication.
---

# Generate Fred Craddock Sermons

## Overview

Generate sermons with Fred Craddock's inductive preaching method: begin in shared human recognition, move through genuine complication, and let the listener arrive at the Gospel as discovery rather than packaged conclusion. The default deliverable is a formatted Microsoft Word document.

Read [references/fred_craddock_method.md](references/fred_craddock_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for movement, tone, pacing, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Fred Craddock into generic narrative exposition. Preserve inductive discovery, knot-shock-new hearing, shuttle and spiral movement, and the open ending.
- If the user asks for Fred Craddock, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a general congregation of mixed maturity and produce a complete sermon manuscript.
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

- Read the text inductively before imposing a sermon theme.
- Distill the whole sermon into one sermon-sentence before writing the body.
- Build the sermon as a journey rather than a lecture.
- Move through three internal movements:
  - Knot
  - Shock
  - New Hearing
- Use the three core instruments:
  - Shuttle
  - Spiral
  - Shock
- Start where the listener already is.
- Delay the conclusion until the listener is ready to discover it.
- Keep one central question and one central insight only.
- Preserve an intentionally open ending that leaves space for the Spirit and the listener's conscience.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The distilled sermon-sentence.
2. The Knot for this congregation.
3. The Shock for this congregation.
4. The New Hearing the sermon is moving toward.
5. How Shuttle, Spiral, and Shock will function in the message.

Then write the sermon as a continuous inductive journey with these clearly signaled internal stages:

1. Knot
2. Shock
3. New Hearing

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Fred_Craddock.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Fred_Craddock.epub`.
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

- Prefer discovery over direct proposition.
- Use concrete experience before abstract conclusion.
- Move back and forth between the world of the text and the world of the congregation.
- Return to the same central insight repeatedly from different angles.
- Narrate the complication rather than arguing it like a debate brief.
- Avoid announcing the thesis in the opening.
- End with openness rather than a fully sealed summary.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the sermon sentence is singular and central.
- Verify the opening starts with recognition, not conclusion.
- Verify the Shock genuinely complicates what the listener assumed.
- Verify Shuttle appears repeatedly between text-world and congregation-world.
- Verify Spiral deepens the same insight rather than multiplying ideas.
- Verify the ending stays open enough for the listener to complete the sermon inwardly.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
