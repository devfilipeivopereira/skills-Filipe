# Visual Style and Candidate-Board Protocol

Version: 2.5.0

The target-paper visual candidate board is mandatory after multi-option text decisions. Saved atlas boards and inline non-target concept/example images help the user understand choices, but they are not target-paper candidate figures and do not replace target-paper first-round candidate generation or P6b-IMAGE second-round variant generation.

## Saved Atlas And Required Concept Use

When discussing subtype, layout grammar, density, reader role, visual grammar, visual rhetoric, metaphor, modeling pattern, candidate scheme differences, final content architecture, or visual communication style in a `TEXT_ONLY` reply, display the relevant saved board or a non-target concept/modeling example with Markdown image syntax:

- subtype/narrative role: `assets/subtype-atlas/boards/subtype-overview.png`
- layout/visual grammar/visual rhetoric: `assets/subtype-atlas/boards/visual-grammar-layout.png`
- reader question/logical gap/paper slot/density: `assets/subtype-atlas/boards/reader-role-detail.png`
- visual communication art style: `assets/subtype-atlas/boards/visual-communication-styles.png`

If the relevant board is missing, record `concept_example_required`, `concept_example_status`, `concept_example_role`, `concept_example_trigger_reason`, and `missing_reference_images`, then recommend atlas repair or concept/example generation. If an asset exists, a plain path list is not enough; use `![alt](...)`. In Codex desktop, resolve package-local assets to absolute filesystem paths before embedding.

Pure state synchronization, caption/body text, simple confirmation, and ordinary restatement of an already registered image batch do not require a new concept/example image.

## Required Visual-Structure Image Use

When a text reply explains visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or content architecture, display a relevant saved board or non-target visual-structure concept/modeling example with Markdown image syntax. The default saved board for structure is `assets/subtype-atlas/boards/visual-grammar-layout.png`.

Do not describe structure with prose, bullets, ASCII, Mermaid, SVG, or code-rendered sketches only. If a paper-specific structure preview is needed, defer that preview to P5, P6b-IMAGE, or P8 `IMAGE_ONLY`, and embed only a generic structure/reference image in the text reply. Record `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, and `visual_structure_image_trigger_reason`.

## Inline Non-Target Concept/Example References

When an abstract-decision text turn needs visual explanation beyond saved atlas boards, embed a non-target concept diagram or skill-modeling example image. The image must be detached from the user's target paper, recorded as `non_target_reference` or `concept_example`, and must not set `candidate_image_batch_id` or `second_round_candidate_batch_id`.

These inline references do not satisfy P5, P6b-IMAGE, P8, or the candidate-image bridge and cannot be used to lock a target-paper visual direction.

## P4 First-Round Board Setup

In P4, state:

- board type: subtype / scheme / layout / style / metaphor / density / prompt;
- candidate count: 4, 5, or 6, default 6;
- varied axis: high-level direction diversity across subtype, layout grammar, metaphor, density, panel rhythm, or style family;
- fixed elements: paper thesis, target slot, required modules, labels, sample-image hard constraints;
- saved atlas/reference images displayed with Markdown image embeds or missing;
- inline non-target concept/example references displayed, if required;
- visual-structure image displayed for layout skeleton, panel choreography, module topology, or arrow grammar; prose-only structure setup is invalid;
- rendering route: ChatGPT web Create image / ChatGPT Images 2.0; Codex `$imagegen` first; fallback ChatGPT Images 2.0 API or approved image API;
- comparison criteria: what the user should choose by looking at first-round target-paper candidate images.

Then stop before target-paper generation. P4 is text-only.

## P5 First-Round Board Generation

P5 is `IMAGE_ONLY`:

- generate/display 4-6 diverse target-paper candidate images or schematic candidates, normally 6;
- no prose or state footer;
- no caption or critique.

## P6 First-Round Review

P6 is text-only and must:

1. record `candidate_image_batch_id`;
2. compare target-paper candidates;
3. select the strongest current direction;
4. identify risks and fixes;
5. set `best_practice_divergence_status: required_after_first_selection`;
6. ask the user to proceed to P6b or request another diverse first-round board.

P6 must not proceed directly to P7.

## P6b Second-Round Setup

P6b is text-only and must:

- define 4-6 paper-local optimization axes, normally 6;
- keep the first-round direction mostly fixed;
- vary local module relationships, evidence/case anchors, label economy, panel transitions, color semantics, callout placement, and reviewer readability;
- display a saved reference or non-target concept/modeling example image when explaining the optimization grammar, or record missing/repair state;
- display a saved reference or non-target optimization-structure image when explaining second-round geometry, or record missing/repair state;
- set `best_practice_divergence_status: setup_ready`.

## P6b-IMAGE Second-Round Generation

P6b-IMAGE is `IMAGE_ONLY`:

- generate/display 4-6 second-round target-paper variants, normally 6;
- use a new `second_round_candidate_batch_id`;
- no prose or state footer;
- no caption or critique.

## P6c Second-Round Review

P6c is text-only and must:

1. record `second_round_candidate_batch_id`;
2. compare target-paper variants by paper-local axes;
3. select or combine the final direction;
4. set `selected_second_round_candidate`;
5. set `best_practice_divergence_status: final_locked`;
6. make P7 final image brief the next allowed step.

## Style Families

Use 4-6 style choices when style is live, normally 6:

- clean editorial flat;
- formal architecture schematic;
- minimal line-art schematic;
- blueprint / technical drawing;
- mechanism snapshot;
- premium scientific illustration;
- isometric / soft 3D;
- dashboard / interface metaphor;
- mini-evidence infographic;
- storyboard panels;
- tile/card/mosaic board.

If style choices are visibly different, display the saved style atlas first with a Markdown image embed, then proceed through P4/P5/P6/P6b/P6b-IMAGE/P6c rather than locking style from prose alone.
