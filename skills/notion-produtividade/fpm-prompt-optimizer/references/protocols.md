# Anti-Hallucination Protocols (FPM)

These protocols must be embedded into the optimized prompt whenever the task involves factual, analytical, legal, financial, scientific, technical, medical, historical, or otherwise truth-sensitive output.

## Protocol 1: Ambiguity Gate
- Detect underspecified terms, missing scope, unclear entities, and unresolved references before optimization.
- If ambiguity materially affects correctness, require clarification or insert explicit placeholders.
- Do not silently guess when multiple plausible interpretations exist.

## Protocol 2: False-Premise Check
- Test whether the source prompt contains assumptions that may be false, outdated, contradictory, or impossible.
- If a false premise is suspected, instruct the model to identify it explicitly before answering.
- Prefer correction, qualification, or refusal over fluent continuation from a false premise.

## Protocol 3: Evidence Boundary
- Distinguish clearly between:
  a) facts supported by provided evidence,
  b) inferences drawn from evidence,
  c) assumptions made due to missing information.
- The optimized prompt must require the model to label these categories when factual accuracy matters.

## Protocol 4: Grounding Requirement
- For factual claims, require grounding in supplied materials, retrieved sources, or explicitly stated evidence.
- If no grounding source exists, require the model to say that confidence is limited.
- Do not allow unsupported specifics such as dates, figures, names, citations, or causal claims to be presented as certain.

## Protocol 5: Atomic-Claim Discipline
- In truth-sensitive tasks, require the model to decompose important conclusions into discrete claims and check whether each claim is supported.
- If some claims are supported and others are not, the optimized prompt must require partial acceptance rather than all-or-nothing overclaiming.

## Protocol 6: Verification Loop
- Before finalizing an answer, require a self-audit against the prompt’s constraints, evidence, and success criteria.
- The self-audit must check for unsupported assertions, invented details, hidden leaps, and instruction drift.
- If verification fails, the model must revise, qualify, or reduce scope.

## Protocol 7: Confidence Calibration
- Require calibrated confidence labels when certainty varies.
- High confidence may be used only when the answer is directly supported by evidence or well-established knowledge in context.
- Medium or low confidence must be used when the answer relies on incomplete evidence, inference, or uncertain assumptions.

## Protocol 8: Graceful Refusal and Safe Fallback
- When evidence is insufficient, contradictory, or absent, the optimized prompt must instruct the model to:
  a) say what cannot be established,
  b) provide the most defensible partial answer,
  c) identify what additional information would resolve the issue.
- Never reward fabrication for completeness.

## Protocol 9: Minimal-Speculation Rule
- When the task does not require creativity, minimize speculation.
- Prefer omission, qualification, or bounded alternatives over invented detail.

## Protocol 10: Source Priority Rule
- In grounded tasks, prioritize user-provided sources, authoritative references, and directly retrieved evidence over general model priors.
- If sources conflict, note the conflict rather than collapsing it into a single asserted answer.
