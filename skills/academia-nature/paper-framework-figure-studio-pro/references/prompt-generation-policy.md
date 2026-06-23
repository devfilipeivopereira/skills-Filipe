# Prompt Generation Policy

Version: 2.5.0

## Prompt Types

This skill uses three target-paper generation prompt stages:

- **P4 first-round candidate-board brief:** low-commitment board for choosing a broad direction after text candidates. It should maximize diversity across subtype, layout grammar, metaphor, density, panel rhythm, or style family.
- **P6b second-round optimization brief:** paper-local best-practice variants around the selected first-round winner. It should keep the chosen direction fixed and vary module relationships, evidence/case anchors, label economy, panel transitions, color semantics, callout placement, and reviewer readability.
- **P7 final image brief:** formal prompt for the selected direction after P6c second-round review.

Do not use P7 as a substitute for P4/P5/P6 or P6b/P6b-IMAGE/P6c. After 4-6 text candidates, the target-paper candidate-board bridge must happen unless explicitly skipped by the user. After P6 selects the first-round current best, P6b/P6b-IMAGE/P6c must happen before P7.

## Required Saved Atlas And Concept References Before Prompting

Before writing a candidate-board, second-round optimization, or final image brief, check whether the turn explains or compares subtype, layout grammar, visual style, density, metaphor, modeling pattern, candidate scheme differences, or final content architecture. If so, display a relevant saved atlas board or non-target concept/modeling example in the text turn with an actual Markdown image embed:

- `assets/subtype-atlas/boards/subtype-overview.png`
- `assets/subtype-atlas/boards/visual-grammar-layout.png`
- `assets/subtype-atlas/boards/reader-role-detail.png`
- `assets/subtype-atlas/boards/visual-communication-styles.png`

Displaying saved atlas or non-target concept/example images is allowed in `TEXT_ONLY`; target-paper candidate/final generation is not. In Codex desktop, resolve package-local paths to absolute filesystem paths before embedding. In ChatGPT Sources, use source asset display or package-relative Markdown embeds. A plain path list is not sufficient when the asset exists.

Non-target concept diagrams or skill-modeling example images must be recorded as `non_target_reference` or `concept_example`; do not set `candidate_image_batch_id` or `second_round_candidate_batch_id`.

If a required reference image is unavailable, record `concept_example_required: true`, `concept_example_status: generation_pending` or `missing_recorded`, `concept_example_role`, `concept_example_trigger_reason`, and the next repair action.

## Required Visual-Structure Image Display Before Prompting

Before writing a candidate-board, second-round optimization, or final image brief, check whether the turn explains visual structure, layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or final content architecture. If so, display a relevant saved atlas board or non-target visual-structure concept/modeling example with an actual Markdown image embed.

Do not use prose, bullets, ASCII, Mermaid, SVG, or code-rendered sketches as the only visual-structure representation. If the useful preview would be target-paper-specific, defer it to P5, P6b-IMAGE, or P8 `IMAGE_ONLY`, and show only a generic structure/reference image in the text reply.

Record `visual_structure_image_required`, `visual_structure_image_status`, `visual_structure_image_role`, and `visual_structure_image_trigger_reason` whenever this gate applies.

## P4 First-Round Candidate-Board Brief

```text
Board purpose:
Generate diverse target-paper candidate images or schematic candidates for choosing a framework-figure direction, not a final figure.

Candidate count:
6 by default, allowed 4-6.

Saved atlas/reference images displayed:
<actual Markdown image embeds used, or missing images recorded if needed>

Inline non-target concept/example references:
<actual Markdown image embeds used, role=non_target_reference/concept_example, or none>

Visual-structure image displayed:
<actual Markdown image embed for generic layout skeleton / panel choreography / arrow grammar reference, or missing/repair state>

Hold fixed:
<paper thesis, target slot, required modules, exact labels, sample-image transfer hard constraints>

Vary broadly:
<subtype / scheme / layout grammar / style family / metaphor / density / panel rhythm>

Compare:
<what the user should decide by looking at the first-round target-paper candidate images>

Rendering route:
ChatGPT web: Create image through ChatGPT Images 2.0.
Codex: $imagegen first; if unavailable, ChatGPT Images 2.0 API or another approved image-generation API.
```

## P6b Second-Round Optimization Brief

```text
Second-round purpose:
Optimize the selected first-round framework direction around paper-local details and best practices.

Second-round count:
6 by default, allowed 4-6.

Keep fixed from first-round winner:
<subtype, main layout grammar, core metaphor, major panel order, style family>

Vary locally:
<module relationships / evidence or case anchor / label economy / panel transition / color semantics / callout placement / reviewer readability>

Saved atlas/reference or concept image displayed:
<actual Markdown image embeds used, or missing/repair state>

Visual-structure image displayed:
<actual Markdown image embed for generic second-round optimization geometry, or missing/repair state>

Compare:
<which variant communicates the paper's local mechanism with the least ambiguity and best reviewer-facing clarity>

Rendering route:
ChatGPT web: Create image through ChatGPT Images 2.0.
Codex: $imagegen first; if unavailable, ChatGPT Images 2.0 API or another approved image-generation API.
```

## P7 Final Image Brief

```text
Create a publication-ready research-paper framework diagram as a raster image.

Goal:
<figure thesis>

Paper slot and audience:
<slot and audience>

Final direction source:
<P6c selected_second_round_candidate and which first-round direction it preserves>

Diagram subtype and layout:
<subtype, canvas, panel count, reading order>

Required content:
<modules/entities/stages/evidence>

Labels:
Use only these exact labels: <labels>.

Sample-image transfer:
<per-image transfer rules or "none">

Saved atlas guidance:
<which saved atlas board influenced subtype/layout/style, or none>

Visual-structure reference in this TEXT_ONLY prompt explanation:
<actual Markdown image embed for saved atlas/reference or non-target structure concept if explaining final architecture; otherwise refer to P6c selected_second_round_candidate instead of restating paper-specific structure in prose>

Style and color semantics:
<style, palette, what colors mean>

Candidate variation:
Generate <4/5/6> target-paper formal candidates, usually 6. Vary only <minor polish/rendering axis>.

Avoid:
long paragraphs, microscopic labels, fake metrics, fake UI, logos, watermarks, decorative clutter, SVG/Mermaid/TikZ/Graphviz/code-rendered diagram instructions.
```

## Rendering Route

- ChatGPT web: use Create image through ChatGPT Images 2.0.
- Codex: use `$imagegen` first.
- Codex fallback: ChatGPT Images 2.0 API or another approved image-generation API.

Allowed bitmap outputs: PNG, JPG, JPEG, WebP.

Forbidden target-paper visual outputs/fallbacks: SVG, Mermaid, TikZ, Graphviz, HTML/CSS, canvas, matplotlib, filesystem code drawing, or code-rendered/exported images.
