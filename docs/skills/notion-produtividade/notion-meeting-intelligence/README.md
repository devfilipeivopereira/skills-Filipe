# notion-meeting-intelligence

- Categoria: **Notion e Produtividade** (`notion-produtividade`)
- Nome declarado: `notion-meeting-intelligence`
- Pacote instalavel: `packages/notion-produtividade/notion-meeting-intelligence.zip`
- Pasta copiada: `skills/notion-produtividade/notion-meeting-intelligence`
- Fonte original: `C:\Users\filip\.codex\skills\notion-meeting-intelligence`
- Hash do `SKILL.md`: `e987b7afcd790dabeceebce945481408b325278f5e4626de4fe890231872f914`

## Resumo

Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

## Instalacao individual

```powershell
$zip = "packages/notion-produtividade/notion-meeting-intelligence.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `notion-meeting-intelligence` |
| Skill name | `notion-meeting-intelligence` |
| Categoria | `notion-produtividade` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\notion-meeting-intelligence` |
| Pasta no repositorio | `skills/notion-produtividade/notion-meeting-intelligence` |
| Arquivo principal | `skills/notion-produtividade/notion-meeting-intelligence/SKILL.md` |
| Zip | `packages/notion-produtividade/notion-meeting-intelligence.zip` |
| Tamanho do zip | 41,9 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | notion-meeting-intelligence |
| `description` | Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees. |
| `metadata` |  |
| `short-description` | Prep meetings with Notion context and tailored agendas |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 19 |
| Diretorios | 5 |
| Tamanho copiado | 69,8 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 526 B |
| `assets` | 2 | 23,7 KB |
| `evaluations` | 3 | 10,6 KB |
| `examples` | 4 | 20,4 KB |
| `reference` | 7 | 10,0 KB |

## Secoes internas detectadas

- Meeting Intelligence
-   Quick start
-   Workflow
-     0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
-     1) Gather inputs
-     2) Choose format
-     3) Build the agenda/pre-read
-     4) Enrich with research
-     5) Finalize and share
-   References and examples

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/notion-produtividade/notion-meeting-intelligence/agents/openai.yaml` | 526 B |
| `skills/notion-produtividade/notion-meeting-intelligence/assets/notion.png` | 8,3 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/assets/notion-small.svg` | 15,4 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/evaluations/decision-meeting-prep.json` | 3,4 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/evaluations/README.md` | 4,0 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/evaluations/status-meeting-prep.json` | 3,3 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/examples/customer-meeting.md` | 3,2 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/examples/executive-review.md` | 2,2 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/examples/project-decision.md` | 13,0 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/examples/sprint-planning.md` | 2,1 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/LICENSE.txt` | 1,0 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/reference/brainstorming-template.md` | 1,5 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/reference/decision-meeting-template.md` | 1,9 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/reference/one-on-one-template.md` | 990 B |
| `skills/notion-produtividade/notion-meeting-intelligence/reference/retrospective-template.md` | 998 B |
| `skills/notion-produtividade/notion-meeting-intelligence/reference/sprint-planning-template.md` | 1,3 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/reference/status-update-template.md` | 1,4 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/reference/template-selection-guide.md` | 2,0 KB |
| `skills/notion-produtividade/notion-meeting-intelligence/SKILL.md` | 3,4 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\notion-meeting-intelligence`
- `C:\Users\filip\.agents\skills\notion-meeting-intelligence`
- `C:\Users\filip\.claude\skills\notion-meeting-intelligence`
- `C:\Users\filip\.gemini\skills\notion-meeting-intelligence`
- `C:\Users\filip\.windsurf\skills\notion-meeting-intelligence`

## Conteudo integral do SKILL.md

```
markdown
---
name: notion-meeting-intelligence
description: Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.
metadata:
  short-description: Prep meetings with Notion context and tailored agendas
---

# Meeting Intelligence

Prep meetings by pulling Notion context, tailoring agendas/pre-reads, and enriching with Codex research.

## Quick start
1) Confirm meeting goal, attendees, date/time, and decisions needed.
2) Gather context: search with `Notion:notion-search`, then fetch with `Notion:notion-fetch` (prior notes, specs, OKRs, decisions).
3) Pick the right template via `reference/template-selection-guide.md` (status, decision, planning, retro, 1:1, brainstorming).
4) Draft agenda/pre-read in Notion with `Notion:notion-create-pages`, embedding source links and owner/timeboxes.
5) Enrich with Codex research (industry insights, benchmarks, risks) and update the page with `Notion:notion-update-page` as plans change.

## Workflow
### 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
1. Add the Notion MCP:
   - `codex mcp add notion --url https://mcp.notion.com/mcp`
2. Enable remote MCP client:
   - Set `[features].rmcp_client = true` in `config.toml` **or** run `codex --enable rmcp_client`
3. Log in with OAuth:
   - `codex mcp login notion`

After successful login, the user will have to restart codex. You should finish your answer and tell them so when they try again they can continue with Step 1.

### 1) Gather inputs
- Ask for objective, desired outcomes/decisions, attendees, duration, date/time, and prior materials.
- Search Notion for relevant docs, past notes, specs, and action items (`Notion:notion-search`), then fetch key pages (`Notion:notion-fetch`).
- Capture blockers/risks and open questions up front.

### 2) Choose format
- Status/update → status template.
- Decision/approval → decision template.
- Planning (sprint/project) → planning template.
- Retro/feedback → retrospective template.
- 1:1 → one-on-one template.
- Ideation → brainstorming template.
- Use `reference/template-selection-guide.md` to confirm.

### 3) Build the agenda/pre-read
- Start from the chosen template in `reference/` and adapt sections (context, goals, agenda, owner/time per item, decisions, risks, prep asks).
- Include links to pulled Notion pages and any required pre-reading.
- Assign owners for each agenda item; call out timeboxes and expected outputs.

### 4) Enrich with research
- Add concise Codex research where helpful: market/industry facts, benchmarks, risks, best practices.
- Keep claims cited with source links; separate fact from opinion.

### 5) Finalize and share
- Add next steps and owners for follow-ups.
- If tasks arise, create/link tasks in the relevant Notion database.
- Update the page via `Notion:notion-update-page` when details change; keep a brief changelog if multiple edits.

## References and examples
- `reference/` — template picker and meeting templates (e.g., `template-selection-guide.md`, `status-update-template.md`, `decision-meeting-template.md`, `sprint-planning-template.md`, `one-on-one-template.md`, `retrospective-template.md`, `brainstorming-template.md`).
- `examples/` — end-to-end meeting preps (e.g., `executive-review.md`, `project-decision.md`, `sprint-planning.md`, `customer-meeting.md`).
```
