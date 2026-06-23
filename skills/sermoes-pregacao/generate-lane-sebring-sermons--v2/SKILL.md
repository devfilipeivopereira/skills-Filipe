---
name: generate-lane-sebring-sermons
description: Generate sermon outlines and full sermon manuscripts using Lane Sebring's preaching framework, including objective and desired response, know-feel-do testing, problem-first structure, bottom line bridge, action-oriented points, Gospel pivot, and vision-casting conclusion. Use when the user asks to create a sermon, preaching manuscript, sermon outline, highly practical church message, or life-change sermon based on a Bible text or theme and wants the result shaped by Lane Sebring, Preaching Donkey, killer sermons, or the information plus inspiration plus application framework.
---

# Generate Lane Sebring Sermons

## Overview

Generate sermons with Lane Sebring's framework: define what the sermon does, what the listener does with it, pass the message through know-feel-do testing, build a real-life problem before the text, bridge with a memorable bottom line, solve the problem with Scripture, equip for action, pivot explicitly to the Gospel, and end by casting vision. The default deliverable is a formatted Microsoft Word document.

Read [references/lane_sebring_method.md](references/lane_sebring_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for movement, tone, pacing, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Lane Sebring into generic practical preaching. Preserve objective and response, know-feel-do testing, problem-first logic, bridge line, gospel pivot, and vision-casting ending.
- If the user asks for Lane Sebring, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a general evangelical congregation with mixed life stages and produce a complete sermon manuscript.
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

- Define the objective first: what the sermon does.
- Define the desired response second: what the listener does with it.
- Pass the sermon through the three tests:
  - know
  - feel
  - do
- Build the sermon from the formula:
  - information
  - inspiration
  - application
- Present the problem before the text.
- Reveal the bottom line before opening the biblical text.
- Keep the biblical context minimal and functional.
- Make every point action-oriented, not merely observational.
- Ensure each point includes:
  - explain
  - apply
  - illustrate
- Include the explicit Gospel pivot as step 3b so the message does not collapse into moralism.
- End with personal, congregational, and wider-world vision plus one clear next step.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The sermon objective.
2. The desired response.
3. The bottom line.
4. The know, feel, and do targets.
5. The specific action step for this week.

Then write the sermon with these clearly signaled sections:

1. Present the problem
2. Bottom line bridge
3. Solve the problem with the text
4. Equip the listener to apply it
5. Gospel pivot
6. Cast vision and inspire

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Lane_Sebring.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Lane_Sebring.epub`.
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

- Lead with relatable tension before biblical explanation.
- Move from light accessibility toward heavier reality in the opening.
- Keep the bottom line short, repeatable, and experience-oriented.
- Make the text the answer to a problem the audience already feels.
- Weave application through the whole message, not only at the end.
- Avoid artificial alliteration.
- End with specific vision and one concrete next step, not a vague wrap-up.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the objective and desired response are distinct and concrete.
- Verify the sermon passes the know, feel, and do tests.
- Verify the opening puts everyone on the hook for the solution.
- Verify the bottom line appears before the text.
- Verify every point is action-oriented and includes explanation, application, and illustration.
- Verify the Gospel pivot is explicit.
- Verify the ending paints vision for self, church, and world.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
