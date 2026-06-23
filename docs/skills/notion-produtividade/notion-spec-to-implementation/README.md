# notion-spec-to-implementation

- Categoria: **Notion e Produtividade** (`notion-produtividade`)
- Nome declarado: `notion-spec-to-implementation`
- Pacote instalavel: `packages/notion-produtividade/notion-spec-to-implementation.zip`
- Pasta copiada: `skills/notion-produtividade/notion-spec-to-implementation`
- Fonte original: `C:\Users\filip\.codex\skills\notion-spec-to-implementation`
- Hash do `SKILL.md`: `491d631a76ac5279d9a6ed7b2c59b8bef4d283cee0c16248581fb6bf0c291cc5`

## Resumo

Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

## Instalacao individual

```powershell
$zip = "packages/notion-produtividade/notion-spec-to-implementation.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `notion-spec-to-implementation` |
| Skill name | `notion-spec-to-implementation` |
| Categoria | `notion-produtividade` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\notion-spec-to-implementation` |
| Pasta no repositorio | `skills/notion-produtividade/notion-spec-to-implementation` |
| Arquivo principal | `skills/notion-produtividade/notion-spec-to-implementation/SKILL.md` |
| Zip | `packages/notion-produtividade/notion-spec-to-implementation.zip` |
| Tamanho do zip | 46,7 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | notion-spec-to-implementation |
| `description` | Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them. |
| `metadata` |  |
| `short-description` | Turn Notion specs into implementation plans, tasks, and progress tracking |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 19 |
| Diretorios | 5 |
| Tamanho copiado | 86,0 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 538 B |
| `assets` | 2 | 23,7 KB |
| `evaluations` | 3 | 9,4 KB |
| `examples` | 3 | 17,9 KB |
| `reference` | 8 | 30,0 KB |

## Secoes internas detectadas

- Spec to Implementation
-   Quick start
-   Workflow
-     0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
-     1) Locate and read the spec
-     2) Choose plan depth
-     3) Create tasks
-     4) Link artifacts
-     5) Track progress
-   References and examples

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/notion-produtividade/notion-spec-to-implementation/agents/openai.yaml` | 538 B |
| `skills/notion-produtividade/notion-spec-to-implementation/assets/notion.png` | 8,3 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/assets/notion-small.svg` | 15,4 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/evaluations/basic-spec-implementation.json` | 2,4 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/evaluations/README.md` | 4,4 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/evaluations/spec-to-tasks.json` | 2,5 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/examples/api-feature.md` | 13,7 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/examples/database-migration.md` | 2,5 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/examples/ui-component.md` | 1,7 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/LICENSE.txt` | 1,0 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/milestone-summary-template.md` | 483 B |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/progress-tracking.md` | 9,3 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/progress-update-template.md` | 445 B |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/quick-implementation-plan.md` | 506 B |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/spec-parsing.md` | 7,2 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/standard-implementation-plan.md` | 3,4 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/task-creation.md` | 8,2 KB |
| `skills/notion-produtividade/notion-spec-to-implementation/reference/task-creation-template.md` | 631 B |
| `skills/notion-produtividade/notion-spec-to-implementation/SKILL.md` | 3,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\notion-spec-to-implementation`
- `C:\Users\filip\.agents\skills\notion-spec-to-implementation`
- `C:\Users\filip\.claude\skills\notion-spec-to-implementation`
- `C:\Users\filip\.gemini\skills\notion-spec-to-implementation`
- `C:\Users\filip\.windsurf\skills\notion-spec-to-implementation`

## Conteudo integral do SKILL.md

```
markdown
---
name: notion-spec-to-implementation
description: Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.
metadata:
  short-description: Turn Notion specs into implementation plans, tasks, and progress tracking
---

# Spec to Implementation

Convert a Notion spec into linked implementation plans, tasks, and ongoing status updates.

## Quick start
1) Locate the spec with `Notion:notion-search`, then fetch it with `Notion:notion-fetch`.
2) Parse requirements and ambiguities using `reference/spec-parsing.md`.
3) Create a plan page with `Notion:notion-create-pages` (pick a template: quick vs. full).
4) Find the task database, confirm schema, then create tasks with `Notion:notion-create-pages`.
5) Link spec ↔ plan ↔ tasks; keep status current with `Notion:notion-update-page`.

## Workflow

### 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
1. Add the Notion MCP:
   - `codex mcp add notion --url https://mcp.notion.com/mcp`
2. Enable remote MCP client:
   - Set `[features].rmcp_client = true` in `config.toml` **or** run `codex --enable rmcp_client`
3. Log in with OAuth:
   - `codex mcp login notion`

After successful login, the user will have to restart codex. You should finish your answer and tell them so when they try again they can continue with Step 1.

### 1) Locate and read the spec
- Search first (`Notion:notion-search`); if multiple hits, ask the user which to use.
- Fetch the page (`Notion:notion-fetch`) and scan for requirements, acceptance criteria, constraints, and priorities. See `reference/spec-parsing.md` for extraction patterns.
- Capture gaps/assumptions in a clarifications block before proceeding.

### 2) Choose plan depth
- Simple change → use `reference/quick-implementation-plan.md`.
- Multi-phase feature/migration → use `reference/standard-implementation-plan.md`.
- Create the plan via `Notion:notion-create-pages`, include: overview, linked spec, requirements summary, phases, dependencies/risks, and success criteria. Link back to the spec.

### 3) Create tasks
- Find the task database (`Notion:notion-search` → `Notion:notion-fetch` to confirm the data source and required properties). Patterns in `reference/task-creation.md`.
- Size tasks to 1–2 days. Use `reference/task-creation-template.md` for content (context, objective, acceptance criteria, dependencies, resources).
- Set properties: title/action verb, status, priority, relations to spec + plan, due date/story points/assignee if provided.
- Create pages with `Notion:notion-create-pages` using the database’s `data_source_id`.

### 4) Link artifacts
- Plan links to spec; tasks link to both plan and spec.
- Optionally update the spec with a short “Implementation” section pointing to the plan and tasks using `Notion:notion-update-page`.

### 5) Track progress
- Use the cadence in `reference/progress-tracking.md`.
- Post updates with `reference/progress-update-template.md`; close phases with `reference/milestone-summary-template.md`.
- Keep checklists and status fields in plan/tasks in sync; note blockers and decisions.

## References and examples
- `reference/` — parsing patterns, plan/task templates, progress cadence (e.g., `spec-parsing.md`, `standard-implementation-plan.md`, `task-creation.md`, `progress-tracking.md`).
- `examples/` — end-to-end walkthroughs (e.g., `ui-component.md`, `api-feature.md`, `database-migration.md`).
```
