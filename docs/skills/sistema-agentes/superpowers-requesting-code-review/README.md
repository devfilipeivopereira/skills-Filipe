# superpowers-requesting-code-review

- Categoria: **Sistema e Agentes** (`sistema-agentes`)
- Nome declarado: `requesting-code-review`
- Pacote instalavel: `packages/sistema-agentes/superpowers-requesting-code-review.zip`
- Pasta copiada: `skills/sistema-agentes/superpowers-requesting-code-review`
- Fonte original: `C:\Users\filip\.codex\superpowers\skills\requesting-code-review`
- Hash do `SKILL.md`: `a5ff68586ccf62d1803cedeb71d60fd96ec05591d29c8d123196117eefd34cd0`

## Resumo

Use when completing tasks, implementing major features, or before merging to verify work meets requirements

## Instalacao individual

```powershell
$zip = "packages/sistema-agentes/superpowers-requesting-code-review.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `superpowers-requesting-code-review` |
| Skill name | `requesting-code-review` |
| Categoria | `sistema-agentes` |
| Namespace | `superpowers` |
| Tipo da fonte | Superpowers |
| Fonte original | `C:\Users\filip\.codex\superpowers\skills\requesting-code-review` |
| Pasta no repositorio | `skills/sistema-agentes/superpowers-requesting-code-review` |
| Arquivo principal | `skills/sistema-agentes/superpowers-requesting-code-review/SKILL.md` |
| Zip | `packages/sistema-agentes/superpowers-requesting-code-review.zip` |
| Tamanho do zip | 3,4 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | requesting-code-review |
| `description` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 2 |
| Diretorios | 0 |
| Tamanho copiado | 6,2 KB |

## Secoes internas detectadas

- Requesting Code Review
-   When to Request Review
-   How to Request
-   Example
-   Integration with Workflows
-   Red Flags

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sistema-agentes/superpowers-requesting-code-review/code-reviewer.md` | 3,3 KB |
| `skills/sistema-agentes/superpowers-requesting-code-review/SKILL.md` | 2,9 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\superpowers\skills\requesting-code-review`

## Conteudo integral do SKILL.md

````
markdown
---
name: requesting-code-review
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
---

# Requesting Code Review

Dispatch superpowers:code-reviewer subagent to catch issues before they cascade. The reviewer gets precisely crafted context for evaluation — never your session's history. This keeps the reviewer focused on the work product, not your thought process, and preserves your own context for continued work.

**Core principle:** Review early, review often.

## When to Request Review

**Mandatory:**
- After each task in subagent-driven development
- After completing major feature
- Before merge to main

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## How to Request

**1. Get git SHAs:**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. Dispatch code-reviewer subagent:**

Use Task tool with superpowers:code-reviewer type, fill template at `code-reviewer.md`

**Placeholders:**
- `{WHAT_WAS_IMPLEMENTED}` - What you just built
- `{PLAN_OR_REQUIREMENTS}` - What it should do
- `{BASE_SHA}` - Starting commit
- `{HEAD_SHA}` - Ending commit
- `{DESCRIPTION}` - Brief summary

**3. Act on feedback:**
- Fix Critical issues immediately
- Fix Important issues before proceeding
- Note Minor issues for later
- Push back if reviewer is wrong (with reasoning)

## Example

```
[Just completed Task 2: Add verification function]

You: Let me request code review before proceeding.

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[Dispatch superpowers:code-reviewer subagent]
  WHAT_WAS_IMPLEMENTED: Verification and repair functions for conversation index
  PLAN_OR_REQUIREMENTS: Task 2 from docs/superpowers/plans/deployment-plan.md
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661
  DESCRIPTION: Added verifyIndex() and repairIndex() with 4 issue types

[Subagent returns]:
  Strengths: Clean architecture, real tests
  Issues:
    Important: Missing progress indicators
    Minor: Magic number (100) for reporting interval
  Assessment: Ready to proceed

You: [Fix progress indicators]
[Continue to Task 3]
```

## Integration with Workflows

**Subagent-Driven Development:**
- Review after EACH task
- Catch issues before they compound
- Fix before moving to next task

**Executing Plans:**
- Review after each batch (3 tasks)
- Get feedback, apply, continue

**Ad-Hoc Development:**
- Review before merge
- Review when stuck

## Red Flags

**Never:**
- Skip review because "it's simple"
- Ignore Critical issues
- Proceed with unfixed Important issues
- Argue with valid technical feedback

**If reviewer wrong:**
- Push back with technical reasoning
- Show code/tests that prove it works
- Request clarification

See template at: requesting-code-review/code-reviewer.md
````
