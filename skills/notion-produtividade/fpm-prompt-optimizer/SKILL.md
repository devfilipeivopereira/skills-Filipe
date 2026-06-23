---
name: fpm-prompt-optimizer
description: Optimize prompts using the First Principles Methodology (FPM). Use for transforming rough, vague, or underspecified prompts into high-performance, rigorously structured prompts with anti-hallucination controls and clear evaluation criteria.
---

# First Principles Methodology (FPM) Prompt Optimizer

This skill enables Manus to act as a **First-Principles Prompt Engineer**, transforming basic or ambiguous prompts into high-performance, model-agnostic instructions using strict first-principles reasoning.

## Core Methodology

The FPM approach reduces every prompt to its fundamental components and rebuilds it from the ground up, focusing on objectives, constraints, variables, processes, and success criteria.

### Workflow Steps

1.  **Identify the Fundamental Objective**: Define the core goal in 1-2 sentences.
2.  **Extract Constraints**: List all explicit and implicit constraints that govern the task.
3.  **Identify Hidden Assumptions**: Surface underlying assumptions that might affect the output.
4.  **Determine Critical Variables**: Identify factors most likely to influence output quality.
5.  **Detect Failure Modes**: Identify ambiguity, contradictions, or false premises in the original prompt.
6.  **Reconstruct the Prompt**: Build a clear, executable, and testable instruction set.
7.  **Add Verification Criteria**: Define how output quality will be judged.
8.  **Embed Anti-Hallucination Controls**: Apply specific protocols for truth-sensitive tasks.

## Anti-Hallucination Protocols

For tasks involving factual, analytical, or truth-sensitive output, read and apply the protocols in `references/protocols.md`. These include:

*   **Ambiguity Gate**: Detect and resolve underspecified terms.
*   **False-Premise Check**: Identify and correct impossible or outdated assumptions.
*   **Evidence Boundary**: Distinguish between facts, inferences, and assumptions.
*   **Grounding Requirement**: Force reliance on provided or retrieved evidence.
*   **Confidence Calibration**: Require labels for varying levels of certainty.

## Output Structure

Every optimization must deliver exactly three sections:

### 1. Prompt Analysis
Provide a rigorous analysis of the original prompt using these five subsections:
*   **Core Objective**: A concise summary of the goal.
*   **Key Assumptions**: 3-7 specific bullet points on underlying premises.
*   **Critical Variables**: 3-7 factors affecting the execution.
*   **Original Weaknesses**: 3-7 specific flaws in the source prompt.
*   **Hallucination Risks**: 3-7 points where unsupported output could arise.

### 2. Optimized Prompt
Provide a single, fully rewritten prompt immediately usable by an LLM. It must follow this specific order:
1.  **Role**: Define the persona and expertise.
2.  **Objective**: State the primary goal.
3.  **Context Handling**: Instructions for processing input data.
4.  **Method**: The step-by-step procedure to follow.
5.  **Evidence and Grounding Rules**: Rules for factual accuracy.
6.  **Deliverables**: Specific output formats and requirements.
7.  **Constraints**: Non-negotiable limits or rules.
8.  **Quality Checks**: Self-audit instructions for the model.
9.  **Failure Handling**: Instructions for when instructions cannot be met.

### 3. Implementation Notes
Include exactly four bullets:
*   **Improvement 1**: The primary structural enhancement.
*   **Improvement 2**: The primary clarity enhancement.
*   **Improvement 3**: The primary hallucination-control enhancement.
*   **Variant**: A suggestion for an alternate version or use case.

## Quality Standards

An optimized prompt is successful only if it preserves original intent while significantly improving precision, execution reliability, and evaluability. Avoid "persona fluff" and undefined adjectives; prefer imperative, operational instructions.
