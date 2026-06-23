---
name: generate-alyce-mckenzie-sermons
description: Generate sermon outlines and full sermon manuscripts using Alyce McKenzie's scenic preaching method, including scenic immersion, the three scapes of inscape, landscape, and textscape, the knack for noticing, scene-building through pulse, purpose, plot, and point of view, doctrine as stage direction, and a closing scene that equips hearers for the coming week. Use when the user asks to create a sermon, preaching manuscript, scenic sermon, vivid sermon, Alyce McKenzie style sermon, wisdom-shaped sermon, or scene-based biblical message from a Bible text or theme.
---

# Generate Alyce McKenzie Sermons

## Overview

Generate sermons with Alyce McKenzie's scenic preaching method: open by immersing the hearer inside a scene, read Scripture with the knack for noticing, cross inscape, landscape, and textscape with authenticity, let doctrine function as stage direction inside scenes, and close with a transformed scene that equips the hearer for the next week's lived moments. The default deliverable is a formatted Microsoft Word document.

Read [references/alyce_mckenzie_method.md](references/alyce_mckenzie_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for scenic structure, the three scapes, and the four elements of live scene construction.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten this preacher into a generic evangelical sermon. Preserve the preacher's own sequencing, naming, pacing, tone, and required declarations.
- If the user asks for this preacher, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume contemporary hearers shaped by visual culture who need to inhabit truth through scenes rather than only receive propositions.
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

- Read the text with the knack for noticing before moving to formal analysis.
- Identify the textscape through characters, space, conflict, sensory detail, timing, and movement.
- Build an opening scene with:
  - pulse
  - purpose
  - plot
  - point of view
- Name the exact crossing point of inscape, landscape, and textscape.
- Decide the structural form:
  - single expanded scene
  - multiple scenes in dialogue
  - opening scene with transformed closing scene
- Identify the detail that carries the scene and will stay with the hearer.
- Treat doctrine as stage direction rather than as detached abstraction.
- Close with a scene that equips the hearer for greater kindness, justice, or courage in next week's scenes.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The central biblical text read with the knack for noticing: characters, space, conflict, sensory details, specific moment, and what changes.
2. The opening scene, its source scape, and its four elements:
   - pulse
   - purpose
   - plot
   - point of view
3. The crossing of scapes: where inscape, landscape, and textscape meet.
4. The structural form chosen and the pastoral reason for choosing it.
5. The detail that carries the scene.
6. The theological purpose that will emerge from the scenic architecture.
7. The closing scene and how the opening space returns transformed.
8. What the hearer will be equipped to do in next week's scenes.

Then write the sermon with these clearly signaled moments:

1. Scenic opening
2. Development of the opening scene
3. Scenic reading of the text
4. Crossing of scapes
5. Integrated theological-wisdom development
6. Closing scenic return

Write the transitions explicitly. Keep characters textured like real people, not abstract types. Let scenes do theological work without overexplaining them.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Alyce_McKenzie.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Alyce_McKenzie.epub`.
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

- Open in scene, not in abstraction.
- Use sensory specificity strong enough to deposit the hearer inside the scene.
- Keep the crossing of scapes discovered rather than forced.
- Let doctrine guide the scene rather than sit above it as detached explanation.
- End in a transformed scene rather than in an abstract exhortation.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the sermon begins with real scenic immersion.
- Verify the opening scene contains pulse, purpose, plot, and point of view.
- Verify inscape, landscape, and textscape genuinely intersect.
- Verify the detail that carries the scene is memorable and concrete.
- Verify doctrine functions as stage direction within scenes.
- Verify the ending equips the hearer for next week's scenes through a final image.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.
