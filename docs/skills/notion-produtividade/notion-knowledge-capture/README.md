# notion-knowledge-capture

- Categoria: **Notion e Produtividade** (`notion-produtividade`)
- Nome declarado: `notion-knowledge-capture`
- Pacote instalavel: `packages/notion-produtividade/notion-knowledge-capture.zip`
- Pasta copiada: `skills/notion-produtividade/notion-knowledge-capture`
- Fonte original: `C:\Users\filip\.codex\skills\notion-knowledge-capture`
- Hash do `SKILL.md`: `8bdbd77915e79bcd6b7ffff5ad16fabfda3742fe3e67ece0b666d399e80116a8`

## Resumo

Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

## Instalacao individual

```powershell
$zip = "packages/notion-produtividade/notion-knowledge-capture.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `notion-knowledge-capture` |
| Skill name | `notion-knowledge-capture` |
| Categoria | `notion-produtividade` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\notion-knowledge-capture` |
| Pasta no repositorio | `skills/notion-produtividade/notion-knowledge-capture` |
| Arquivo principal | `skills/notion-produtividade/notion-knowledge-capture/SKILL.md` |
| Zip | `packages/notion-produtividade/notion-knowledge-capture.zip` |
| Tamanho do zip | 42,7 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | notion-knowledge-capture |
| `description` | Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking. |
| `metadata` |  |
| `short-description` | Capture conversations into structured Notion pages |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 18 |
| Diretorios | 5 |
| Tamanho copiado | 72,2 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 526 B |
| `assets` | 2 | 23,7 KB |
| `evaluations` | 3 | 7,7 KB |
| `examples` | 3 | 22,6 KB |
| `reference` | 7 | 13,3 KB |

## Secoes internas detectadas

- Knowledge Capture
-   Quick start
-   Workflow
-     0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
-     1) Define the capture
-     2) Locate destination
-     3) Extract and structure
-     4) Create/update in Notion
-     5) Link and surface
-   References and examples

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/notion-produtividade/notion-knowledge-capture/agents/openai.yaml` | 526 B |
| `skills/notion-produtividade/notion-knowledge-capture/assets/notion.png` | 8,3 KB |
| `skills/notion-produtividade/notion-knowledge-capture/assets/notion-small.svg` | 15,4 KB |
| `skills/notion-produtividade/notion-knowledge-capture/evaluations/conversation-to-wiki.json` | 2,0 KB |
| `skills/notion-produtividade/notion-knowledge-capture/evaluations/decision-record.json` | 2,2 KB |
| `skills/notion-produtividade/notion-knowledge-capture/evaluations/README.md` | 3,5 KB |
| `skills/notion-produtividade/notion-knowledge-capture/examples/conversation-to-faq.md` | 16,1 KB |
| `skills/notion-produtividade/notion-knowledge-capture/examples/decision-capture.md` | 3,6 KB |
| `skills/notion-produtividade/notion-knowledge-capture/examples/how-to-guide.md` | 2,9 KB |
| `skills/notion-produtividade/notion-knowledge-capture/LICENSE.txt` | 1,0 KB |
| `skills/notion-produtividade/notion-knowledge-capture/reference/database-best-practices.md` | 2,9 KB |
| `skills/notion-produtividade/notion-knowledge-capture/reference/decision-log-database.md` | 2,0 KB |
| `skills/notion-produtividade/notion-knowledge-capture/reference/documentation-database.md` | 2,8 KB |
| `skills/notion-produtividade/notion-knowledge-capture/reference/faq-database.md` | 2,0 KB |
| `skills/notion-produtividade/notion-knowledge-capture/reference/how-to-guide-database.md` | 1,2 KB |
| `skills/notion-produtividade/notion-knowledge-capture/reference/learning-database.md` | 1,3 KB |
| `skills/notion-produtividade/notion-knowledge-capture/reference/team-wiki-database.md` | 954 B |
| `skills/notion-produtividade/notion-knowledge-capture/SKILL.md` | 3,3 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\notion-knowledge-capture`
- `C:\Users\filip\.agents\skills\notion-knowledge-capture`
- `C:\Users\filip\.claude\skills\notion-knowledge-capture`
- `C:\Users\filip\.gemini\skills\notion-knowledge-capture`
- `C:\Users\filip\.windsurf\skills\notion-knowledge-capture`

## Conteudo integral do SKILL.md

```
markdown
---
name: notion-knowledge-capture
description: Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.
metadata:
  short-description: Capture conversations into structured Notion pages
---

# Knowledge Capture

Convert conversations and notes into structured, linkable Notion pages for easy reuse.

## Quick start
1) Clarify what to capture (decision, how-to, FAQ, learning, documentation) and target audience.
2) Identify the right database/template in `reference/` (team wiki, how-to, FAQ, decision log, learning, documentation).
3) Pull any prior context from Notion with `Notion:notion-search` → `Notion:notion-fetch` (existing pages to update/link).
4) Draft the page with `Notion:notion-create-pages` using the database’s schema; include summary, context, source links, and tags/owners.
5) Link from hub pages and related records; update status/owners with `Notion:notion-update-page` as the source evolves.

## Workflow
### 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
1. Add the Notion MCP:
   - `codex mcp add notion --url https://mcp.notion.com/mcp`
2. Enable remote MCP client:
   - Set `[features].rmcp_client = true` in `config.toml` **or** run `codex --enable rmcp_client`
3. Log in with OAuth:
   - `codex mcp login notion`

After successful login, the user will have to restart codex. You should finish your answer and tell them so when they try again they can continue with Step 1.

### 1) Define the capture
- Ask purpose, audience, freshness, and whether this is new or an update.
- Determine content type: decision, how-to, FAQ, concept/wiki entry, learning/note, documentation page.

### 2) Locate destination
- Pick the correct database using `reference/*-database.md` guides; confirm required properties (title, tags, owner, status, date, relations).
- If multiple candidate databases, ask the user which to use; otherwise, create in the primary wiki/documentation DB.

### 3) Extract and structure
- Extract facts, decisions, actions, and rationale from the conversation.
- For decisions, record alternatives, rationale, and outcomes.
- For how-tos/docs, capture steps, pre-reqs, links to assets/code, and edge cases.
- For FAQs, phrase as Q&A with concise answers and links to deeper docs.

### 4) Create/update in Notion
- Use `Notion:notion-create-pages` with the correct `data_source_id`; set properties (title, tags, owner, status, dates, relations).
- Use templates in `reference/` to structure content (section headers, checklists).
- If updating an existing page, fetch then edit via `Notion:notion-update-page`.

### 5) Link and surface
- Add relations/backlinks to hub pages, related specs/docs, and teams.
- Add a short summary/changelog for future readers.
- If follow-up tasks exist, create tasks in the relevant database and link them.

## References and examples
- `reference/` — database schemas and templates (e.g., `team-wiki-database.md`, `how-to-guide-database.md`, `faq-database.md`, `decision-log-database.md`, `documentation-database.md`, `learning-database.md`, `database-best-practices.md`).
- `examples/` — capture patterns in practice (e.g., `decision-capture.md`, `how-to-guide.md`, `conversation-to-faq.md`).
```
