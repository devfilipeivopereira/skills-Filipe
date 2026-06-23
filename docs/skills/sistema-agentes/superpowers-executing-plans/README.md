# superpowers-executing-plans

- Categoria: **Sistema e Agentes** (`sistema-agentes`)
- Nome declarado: `executing-plans`
- Pacote instalavel: `packages/sistema-agentes/superpowers-executing-plans.zip`
- Pasta copiada: `skills/sistema-agentes/superpowers-executing-plans`
- Fonte original: `C:\Users\filip\.codex\superpowers\skills\executing-plans`
- Hash do `SKILL.md`: `a711f83fb762e2ea0fa151f598893da9911a408895c91cc7a7e0770dd59a27b3`

## Resumo

Use when you have a written implementation plan to execute in a separate session with review checkpoints

## Instalacao individual

```powershell
$zip = "packages/sistema-agentes/superpowers-executing-plans.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `superpowers-executing-plans` |
| Skill name | `executing-plans` |
| Categoria | `sistema-agentes` |
| Namespace | `superpowers` |
| Tipo da fonte | Superpowers |
| Fonte original | `C:\Users\filip\.codex\superpowers\skills\executing-plans` |
| Pasta no repositorio | `skills/sistema-agentes/superpowers-executing-plans` |
| Arquivo principal | `skills/sistema-agentes/superpowers-executing-plans/SKILL.md` |
| Zip | `packages/sistema-agentes/superpowers-executing-plans.zip` |
| Tamanho do zip | 1,3 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | executing-plans |
| `description` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 1 |
| Diretorios | 0 |
| Tamanho copiado | 2,4 KB |

## Secoes internas detectadas

- Executing Plans
-   Overview
-   The Process
-     Step 1: Load and Review Plan
-     Step 2: Execute Tasks
-     Step 3: Complete Development
-   When to Stop and Ask for Help
-   When to Revisit Earlier Steps
-   Remember
-   Integration

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sistema-agentes/superpowers-executing-plans/SKILL.md` | 2,4 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\superpowers\skills\executing-plans`

## Conteudo integral do SKILL.md

```
markdown
---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

**Note:** Tell your human partner that Superpowers works much better with access to subagents. The quality of its work will be significantly higher if run on a platform with subagent support (such as Claude Code or Codex). If subagents are available, use superpowers:subagent-driven-development instead of this skill.

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Create TodoWrite and proceed

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow each step exactly (plan has bite-sized steps)
3. Run verifications as specified
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verified:
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Follow that skill to verify tests, present options, execute choice

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Remember
- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan says to
- Stop when blocked, don't guess
- Never start implementation on main/master branch without explicit user consent

## Integration

**Required workflow skills:**
- **superpowers:using-git-worktrees** - REQUIRED: Set up isolated workspace before starting
- **superpowers:writing-plans** - Creates the plan this skill executes
- **superpowers:finishing-a-development-branch** - Complete development after all tasks
```
