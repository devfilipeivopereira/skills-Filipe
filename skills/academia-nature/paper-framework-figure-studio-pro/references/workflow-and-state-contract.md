# Workflow and State Contract

Version: 2.5.0

This skill was regenerated with `research-paper-figure-skill-factory` v2.0.5. It uses saved subtype/style atlas boards, required abstract-decision concept/reference display, required image-embedded visual-structure explanation, target-paper image isolation, a diverse first-round candidate-image bridge, and a mandatory P6b/P6b-IMAGE/P6c paper-local best-practice second round.

Saved atlas images, non-target concept/modeling example images, and non-target visual-structure examples appear as Markdown image embeds in relevant `TEXT_ONLY` replies. Target-paper candidate images, second-round variants, draft figures, final figures, and revisions remain `IMAGE_ONLY`.

## Required Workflow

| Step | Mode | Purpose | Output |
|---|---|---|---|
| S0 | STARTUP_PLAN_ONLY (TEXT_ONLY) | Startup plan plus saved atlas Markdown image display only | Startup plan + rendered saved atlas boards |
| P1 | TEXT_ONLY | Intake target-paper material, slot, constraints, optional sample images, and display saved atlas boards with Markdown embeds when available | Material status + rendered atlas references |
| P2 | TEXT_ONLY | Diagnose framework-figure need and multi-label subtype routing with required relevant atlas/concept/structure display | Subtype candidates + rendered references |
| P3 | TEXT_ONLY | Define reader effect and produce 4-6 text candidates, normally 6; display saved style/layout boards or non-target concept/structure examples when abstract decisions or visual structures are discussed | Text candidate schemes + rendered references |
| P4 | TEXT_ONLY | Set up diverse first-round visual candidate board with embedded generic structure/reference image when structure is discussed | First-round candidate-board brief + structure image embed |
| P5 | IMAGE_ONLY | Generate/display 4-6 diverse target-paper candidate images or schematic candidates, normally 6 | First-round target-paper image candidates only |
| P6 | TEXT_ONLY | Record first-round candidate batch, compare, and select current best direction | First-round selected direction + required P6b next action |
| P6b | TEXT_ONLY | Set up 4-6 paper-local best-practice optimization axes, normally 6, with embedded generic optimization-structure image when structure is discussed | Second-round setup + structure image embed |
| P6b-IMAGE | IMAGE_ONLY | Generate/display 4-6 second-round target-paper variants, normally 6 | Second-round target-paper variants only |
| P6c | TEXT_ONLY | Record second-round batch, compare variants, and lock final direction | Final selected direction |
| P7 | TEXT_ONLY | Build final image brief after P6c; embed only non-target structure/reference images when explaining final architecture | Final image brief |
| P8 | IMAGE_ONLY | Generate formal target-paper figure candidate or revision batch | Formal target-paper images only |
| P9 | TEXT_ONLY | Review, refine, caption, legend, and body text | Final paper text package |

## Required Saved And Concept Reference Display

Display all available saved atlas boards on first startup with Markdown image embeds. In Codex desktop, use absolute filesystem paths; in ChatGPT Sources, use saved asset display or package-relative embeds:

- `assets/subtype-atlas/boards/subtype-overview.png`
- `assets/subtype-atlas/boards/visual-grammar-layout.png`
- `assets/subtype-atlas/boards/reader-role-detail.png`
- `assets/subtype-atlas/boards/visual-communication-styles.png`

When a later text turn explains or compares subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture, display the relevant saved board or a non-target concept/modeling example with Markdown image syntax. If missing, record `concept_example_required`, `concept_example_status`, `concept_example_role`, `concept_example_trigger_reason`, and the repair action. A plain path list is not valid display.

When a text turn explains or defines visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, final image-brief structure, or content architecture, display the relevant saved board or a non-target visual-structure concept/modeling example with Markdown image syntax. Do not use prose, bullets, ASCII, Mermaid, SVG, or code-rendered sketches as the only structure representation. If missing, record `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, `visual_structure_image_trigger_reason`, and the repair action.

If the only useful structure preview would contain target-paper-specific modules, claims, data, or final labels, defer that preview to P5, P6b-IMAGE, or P8 `IMAGE_ONLY`, and use only a generic structure/reference image in the text reply.

Inline reference images must not:

- represent the user's target paper;
- be offered as target-paper candidate directions;
- set or reuse `candidate_image_batch_id` or `second_round_candidate_batch_id`;
- satisfy P5, P6b-IMAGE, P8, or the candidate-image bridge.

Pure state synchronization, caption/body text, simple confirmation, and ordinary restatement of an already registered image batch do not require a new concept/example image.

## Candidate-Image Bridge And Second Round

After any target-paper text reply with multiple schemes, layouts, styles, metaphors, density levels, subtypes, or prompt alternatives:

1. The first recommended next prompt must ask to generate/display diverse first-round target-paper candidate images or schematic candidates, normally 6.
2. P4 must set up a broad first-round board unless the user already supplied count, varied axis, fixed elements, route, and comparison criteria.
3. P5 must be `IMAGE_ONLY` and produce 4-6 diverse first-round candidates, normally 6.
4. P6 must record `candidate_image_batch_id`, compare candidates, and select the current best direction.
5. P6 must not move directly to P7/P8.
6. P6b must define 4-6 paper-local best-practice optimization axes, normally 6, around the selected first-round direction.
7. P6b-IMAGE must be `IMAGE_ONLY` and produce 4-6 second-round variants, normally 6, with `second_round_candidate_batch_id`.
8. P6c must record the second-round batch and set `selected_second_round_candidate` before P7.

The first round maximizes direction-level diversity across subtype, layout grammar, metaphor, density, panel rhythm, or style family. The second round optimizes selected direction details: module relationships, evidence/case anchor, label economy, panel transitions, color semantics, callout placement, and reviewer readability.

Skipping first-round image candidates is allowed only when the user explicitly says to stay text-only. Record `visual_candidate_board_skipped_by_user: true`. Once P6 selects a first-round current-best direction, P6b/P6b-IMAGE/P6c are mandatory before P7.

## Every Text Reply

Every `TEXT_ONLY` reply must include:

- `当前执行计划`
- substantive work
- `默认推荐`
- `当前状态与产物`
- `下一步你可以这样问`

The footer must list current mode/step, all steps plus current position, current-turn outputs, cumulative outputs, pending outputs, material/sample-image status, saved reference images displayed, saved reference Markdown embeds rendered, inline reference image role/images, concept example requirement/status/role/trigger reason, visual-structure image requirement/status/role/trigger reason, target-paper images embedded in text turn, reference display render status, missing reference images, first-round candidate-board state, candidate image batch ID, selected visual candidate, second-round status, second-round batch ID, selected second-round candidate, previous `IMAGE_ONLY` output recording status, interpreted user action, workflow step before the request, workflow step after handling it, transition reason, off-recommended prompt handling, and next recommended action.

## Off-Recommended-Prompt Handling

Users may ask in free form. The skill must not rely on recommended prompt wording. For every text reply:

1. Interpret the user's actual requested action.
2. Execute valid work that fits the current response mode.
3. Map the result to the closest workflow step.
4. Record `user_request_interpreted_action`, `workflow_step_before_user_request`, `workflow_step_after_user_request`, `state_transition_reason`, `off_recommended_prompt_handling`, and missing/inferred prerequisites.

If the user asks for target-paper image generation during a text reply, map the request to P4, P6b, or P7 setup/confirmation and make P5, P6b-IMAGE, or P8 the next `IMAGE_ONLY` step. Do not generate or embed target-paper images in the same text reply.

## Image-Only Turns

P5, P6b-IMAGE, and P8 are target-paper image-only turns. They contain only native image generation/artifacts. No prose, no state footer, no caption, no critique.
