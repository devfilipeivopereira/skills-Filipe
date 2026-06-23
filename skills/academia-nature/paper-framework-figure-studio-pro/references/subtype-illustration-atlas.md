# Subtype Illustration Atlas

Version: 2.5.0

This atlas is a saved, package-local visual reference set for `paper-framework-figure-studio-pro`. It helps users compare framework-figure subtypes, layout grammars, reader-role/density choices, and visual communication styles before requesting live candidate generation.

Saved atlas images must be embedded in relevant `TEXT_ONLY` replies with actual Markdown image tags. They are already-generated reference assets and do not count as target-paper image generation. Text turns that explain or compare subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture must display a saved reference or non-target concept/modeling example image, or record missing state and repair action. Text turns that explain visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or final content architecture must display a saved reference or non-target visual-structure image; prose-only structure descriptions are not valid. Target-paper candidate, second-round variant, final, and revision figure generation still happens only in `IMAGE_ONLY` turns.

## Boards

| Board | Classification Angles | Path | Use |
|---|---|---|---|
| Framework Figure Subtypes | narrative role, subtype, paper slot | `assets/subtype-atlas/boards/subtype-overview.png` | Startup overview and subtype routing |
| Visual Grammar and Layout | visual grammar/layout, visual rhetoric | `assets/subtype-atlas/boards/visual-grammar-layout.png` | Layout and visual-grammar selection |
| Reader Role and Detail | reader question, logical gap, density/detail level, paper slot | `assets/subtype-atlas/boards/reader-role-detail.png` | Reader-effect, claim gap, density, and slot selection |
| Visual Communication Styles | visual communication art style | `assets/subtype-atlas/boards/visual-communication-styles.png` | Style-family selection |

## Startup Display

On the first reply, display all available atlas boards. In Codex desktop, use absolute filesystem paths resolved from the active installed skill root:

![Framework Figure Subtypes](C:/Users/qu_yw/.codex/skills/paper-framework-figure-studio-pro/assets/subtype-atlas/boards/subtype-overview.png)
![Visual Grammar and Layout](C:/Users/qu_yw/.codex/skills/paper-framework-figure-studio-pro/assets/subtype-atlas/boards/visual-grammar-layout.png)
![Reader Role and Detail](C:/Users/qu_yw/.codex/skills/paper-framework-figure-studio-pro/assets/subtype-atlas/boards/reader-role-detail.png)
![Visual Communication Styles](C:/Users/qu_yw/.codex/skills/paper-framework-figure-studio-pro/assets/subtype-atlas/boards/visual-communication-styles.png)

In ChatGPT web with this zip in Sources, use saved source asset display or package-relative Markdown image tags:

- `![Framework Figure Subtypes](assets/subtype-atlas/boards/subtype-overview.png)`
- `![Visual Grammar and Layout](assets/subtype-atlas/boards/visual-grammar-layout.png)`
- `![Reader Role and Detail](assets/subtype-atlas/boards/reader-role-detail.png)`
- `![Visual Communication Styles](assets/subtype-atlas/boards/visual-communication-styles.png)`

The startup reply must remain `STARTUP_PLAN_ONLY (TEXT_ONLY)`: no target-paper analysis and no target-paper image generation.

## Later Text Replies

When discussing subtype, candidate scheme differences, or narrative role, display `subtype-overview.png` with a Markdown image embed.

When discussing layout grammar, visual grammar, visual rhetoric, metaphor, modeling pattern, visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or final content architecture, display `visual-grammar-layout.png` with a Markdown image embed.

When discussing reader question, logical gap, paper slot, or density/detail level, display `reader-role-detail.png` with a Markdown image embed.

When discussing visual communication art style or visual style, display `visual-communication-styles.png` with a Markdown image embed.

If a board is missing, record the missing path in `missing_reference_images`, set `concept_example_required: true`, set `concept_example_status: generation_pending` or `missing_recorded`, set `visual_structure_image_required: true` when the missing board is needed for structure explanation, and recommend atlas repair or non-target concept/example generation before locking a direction. If the board exists but the host cannot render it, record `reference_display_render_status: attempted_host_blocked` and list the exact asset path; do not silently omit the atlas.

## Live Candidate Generation Still Required

These saved boards are reference aids. They do not replace P4/P5/P6 or P6b/P6b-IMAGE/P6c. After multi-option text choices, ask the user to generate/display normally 6 diverse first-round target-paper candidate images or schematic candidates. After P6 selects the first-round current best, run P6b/P6b-IMAGE/P6c for paper-local optimization before P7.
