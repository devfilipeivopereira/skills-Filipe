# notion-research-documentation

- Categoria: **Notion e Produtividade** (`notion-produtividade`)
- Nome declarado: `notion-research-documentation`
- Pacote instalavel: `packages/notion-produtividade/notion-research-documentation.zip`
- Pasta copiada: `skills/notion-produtividade/notion-research-documentation`
- Fonte original: `C:\Users\filip\.codex\skills\notion-research-documentation`
- Hash do `SKILL.md`: `c4d7466c789ad987151a292fce3e042581082fc8193bd1940ca4fdfe15f98e5e`

## Resumo

Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

## Instalacao individual

```powershell
$zip = "packages/notion-produtividade/notion-research-documentation.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `notion-research-documentation` |
| Skill name | `notion-research-documentation` |
| Categoria | `notion-produtividade` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\notion-research-documentation` |
| Pasta no repositorio | `skills/notion-produtividade/notion-research-documentation` |
| Arquivo principal | `skills/notion-produtividade/notion-research-documentation/SKILL.md` |
| Zip | `packages/notion-produtividade/notion-research-documentation.zip` |
| Tamanho do zip | 46,3 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | notion-research-documentation |
| `description` | Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations. |
| `metadata` |  |
| `short-description` | Research Notion content and produce briefs/reports |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 23 |
| Diretorios | 5 |
| Tamanho copiado | 77,2 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 511 B |
| `assets` | 2 | 23,7 KB |
| `evaluations` | 3 | 7,6 KB |
| `examples` | 4 | 20,6 KB |
| `reference` | 11 | 20,2 KB |

## Secoes internas detectadas

- Research & Documentation
-   Quick start
-   Workflow
-     0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
-     1) Gather sources
-     2) Select the format
-     3) Synthesize
-     4) Create the doc
-     5) Finalize & handoff
-   References and examples

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/notion-produtividade/notion-research-documentation/agents/openai.yaml` | 511 B |
| `skills/notion-produtividade/notion-research-documentation/assets/notion.png` | 8,3 KB |
| `skills/notion-produtividade/notion-research-documentation/assets/notion-small.svg` | 15,4 KB |
| `skills/notion-produtividade/notion-research-documentation/evaluations/basic-research.json` | 1,7 KB |
| `skills/notion-produtividade/notion-research-documentation/evaluations/README.md` | 4,3 KB |
| `skills/notion-produtividade/notion-research-documentation/evaluations/research-to-database.json` | 1,7 KB |
| `skills/notion-produtividade/notion-research-documentation/examples/competitor-analysis.md` | 8,3 KB |
| `skills/notion-produtividade/notion-research-documentation/examples/market-research.md` | 1,9 KB |
| `skills/notion-produtividade/notion-research-documentation/examples/technical-investigation.md` | 6,6 KB |
| `skills/notion-produtividade/notion-research-documentation/examples/trip-planning.md` | 3,8 KB |
| `skills/notion-produtividade/notion-research-documentation/LICENSE.txt` | 1,0 KB |
| `skills/notion-produtividade/notion-research-documentation/reference/advanced-search.md` | 4,7 KB |
| `skills/notion-produtividade/notion-research-documentation/reference/citations.md` | 5,2 KB |
| `skills/notion-produtividade/notion-research-documentation/reference/comparison-format.md` | 907 B |
| `skills/notion-produtividade/notion-research-documentation/reference/comparison-template.md` | 955 B |
| `skills/notion-produtividade/notion-research-documentation/reference/comprehensive-report-format.md` | 1,1 KB |
| `skills/notion-produtividade/notion-research-documentation/reference/comprehensive-report-template.md` | 1,3 KB |
| `skills/notion-produtividade/notion-research-documentation/reference/format-selection-guide.md` | 2,8 KB |
| `skills/notion-produtividade/notion-research-documentation/reference/quick-brief-format.md` | 804 B |
| `skills/notion-produtividade/notion-research-documentation/reference/quick-brief-template.md` | 498 B |
| `skills/notion-produtividade/notion-research-documentation/reference/research-summary-format.md` | 874 B |
| `skills/notion-produtividade/notion-research-documentation/reference/research-summary-template.md` | 1,2 KB |
| `skills/notion-produtividade/notion-research-documentation/SKILL.md` | 3,4 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\notion-research-documentation`
- `C:\Users\filip\.agents\skills\notion-research-documentation`
- `C:\Users\filip\.claude\skills\notion-research-documentation`
- `C:\Users\filip\.gemini\skills\notion-research-documentation`
- `C:\Users\filip\.windsurf\skills\notion-research-documentation`

## Conteudo integral do SKILL.md

```
markdown
---
name: notion-research-documentation
description: Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.
metadata:
  short-description: Research Notion content and produce briefs/reports
---

# Research & Documentation

Pull relevant Notion pages, synthesize findings, and publish clear briefs or reports (with citations and links to sources).

## Quick start
1) Find sources with `Notion:notion-search` using targeted queries; confirm scope with the user.
2) Fetch pages via `Notion:notion-fetch`; note key sections and capture citations (`reference/citations.md`).
3) Choose output format (brief, summary, comparison, comprehensive report) using `reference/format-selection-guide.md`.
4) Draft in Notion with `Notion:notion-create-pages` using the matching template (quick, summary, comparison, comprehensive).
5) Link sources and add a references/citations section; update as new info arrives with `Notion:notion-update-page`.

## Workflow
### 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
1. Add the Notion MCP:
   - `codex mcp add notion --url https://mcp.notion.com/mcp`
2. Enable remote MCP client:
   - Set `[features].rmcp_client = true` in `config.toml` **or** run `codex --enable rmcp_client`
3. Log in with OAuth:
   - `codex mcp login notion`

After successful login, the user will have to restart codex. You should finish your answer and tell them so when they try again they can continue with Step 1.

### 1) Gather sources
- Search first (`Notion:notion-search`); refine queries, and ask the user to confirm if multiple results appear.
- Fetch relevant pages (`Notion:notion-fetch`), skim for facts, metrics, claims, constraints, and dates.
- Track each source URL/ID for later citation; prefer direct quotes for critical facts.

### 2) Select the format
- Quick readout → quick brief.
- Single-topic dive → research summary.
- Option tradeoffs → comparison.
- Deep dive / exec-ready → comprehensive report.
- See `reference/format-selection-guide.md` for when to pick each.

### 3) Synthesize
- Outline before writing; group findings by themes/questions.
- Note evidence with source IDs; flag gaps or contradictions.
- Keep user goal in view (decision, summary, plan, recommendation).

### 4) Create the doc
- Pick the matching template in `reference/` (brief, summary, comparison, comprehensive) and adapt it.
- Create the page with `Notion:notion-create-pages`; include title, summary, key findings, supporting evidence, and recommendations/next steps when relevant.
- Add citations inline and a references section; link back to source pages.

### 5) Finalize & handoff
- Add highlights, risks, and open questions.
- If the user needs follow-ups, create tasks or a checklist in the page; link any task database entries if applicable.
- Share a short changelog or status using `Notion:notion-update-page` when updating.

## References and examples
- `reference/` — search tactics, format selection, templates, and citation rules (e.g., `advanced-search.md`, `format-selection-guide.md`, `research-summary-template.md`, `comparison-template.md`, `citations.md`).
- `examples/` — end-to-end walkthroughs (e.g., `competitor-analysis.md`, `technical-investigation.md`, `market-research.md`, `trip-planning.md`).
```
