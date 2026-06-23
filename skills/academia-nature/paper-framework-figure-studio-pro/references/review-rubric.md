# Review Rubric

Version: 2.5.0

Check generated framework diagrams against:

- thesis clarity: can a reader understand the main point in 10 seconds?
- multi-label fit: were all applicable diagram labels considered before selecting the primary subtype?
- subtype fit: does the layout match the intended primary diagram role?
- paper fidelity: no invented modules, labels, metrics, or claims;
- hierarchy: proposed contribution is visually dominant;
- reading path: arrows and panels have a clear order;
- label quality: short, readable, and exact;
- density: enough detail for the paper slot without clutter;
- sample-image transfer: borrowed only requested attributes from each sample image;
- candidate-image bridge: text candidates were followed by P4 setup, P5 image-only direction-diverse candidate board, P6 current-best direction selection, P6b paper-local best-practice divergence setup, P6b-IMAGE image-only second-round variants, and P6c final direction lock before final prompt;
- visual-structure-as-image: text turns that explained layout skeleton, panel choreography, module topology, arrow grammar, candidate-board structure, second-round optimization geometry, or final content architecture embedded a saved reference or non-target visual-structure image instead of using prose/bullets only;
- rendering route: ChatGPT web used Create image / ChatGPT Images 2.0; Codex used `$imagegen` first or an approved API fallback;
- rendering safety: no watermark, fake UI, malformed text, or decorative clutter;
- response boundary: first trigger did not generate target-paper images, text turns did not embed target-paper candidate/final/revision images, required inline non-target concept/example images were displayed for abstract decisions and clearly recorded as references, and IMAGE_ONLY turns had no prose/state;
- state footer: every text turn listed all steps, current position, current artifacts, pending artifacts, and next prompts.

## Revision Routes

- If structure is wrong: revise layout skeleton before style.
- If text is wrong: reduce labels and specify exact text.
- If novelty is buried: increase contrast and visual weight on the proposed component.
- If too decorative: switch to formal architecture schematic or minimal line-art.
- If too sparse: add evidence cards or callouts, but only from provided paper material.
- If no candidate-board step occurred after text candidates: return to P4 and set up the direction-diverse first-round board before final prompt/final generation.
- If P6 selected a first-round current best but P6b/P6b-IMAGE/P6c did not occur: stop finalization, set up paper-local best-practice divergence, generate second-round variants, then lock the final direction.
- If an abstract decision turn lacks a displayed saved reference or non-target concept/modeling example image: record the missing concept state and repair it before proceeding.
- If a visual-structure turn explains structure only in text: stop, embed a saved structure/reference image or non-target visual-structure example, and record `visual_structure_image_*` state before proceeding.

