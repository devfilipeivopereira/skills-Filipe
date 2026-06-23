# gh-address-comments

- Categoria: **Desenvolvimento e DevOps** (`desenvolvimento-devops`)
- Nome declarado: `gh-address-comments`
- Pacote instalavel: `packages/desenvolvimento-devops/gh-address-comments.zip`
- Pasta copiada: `skills/desenvolvimento-devops/gh-address-comments`
- Fonte original: `C:\Users\filip\.codex\skills\gh-address-comments`
- Hash do `SKILL.md`: `947b0bcea8f1649d46b07dcdeeff6e0b294002093e7d2ce39aa026e05bb5add6`

## Resumo

Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

## Instalacao individual

```powershell
$zip = "packages/desenvolvimento-devops/gh-address-comments.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `gh-address-comments` |
| Skill name | `gh-address-comments` |
| Categoria | `desenvolvimento-devops` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\gh-address-comments` |
| Pasta no repositorio | `skills/desenvolvimento-devops/gh-address-comments` |
| Arquivo principal | `skills/desenvolvimento-devops/gh-address-comments/SKILL.md` |
| Zip | `packages/desenvolvimento-devops/gh-address-comments.zip` |
| Tamanho do zip | 9,9 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | gh-address-comments |
| `description` | Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in. |
| `metadata` |  |
| `short-description` | Address comments in a GitHub PR review |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 6 |
| Diretorios | 3 |
| Tamanho copiado | 22,1 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 309 B |
| `assets` | 2 | 2,6 KB |
| `scripts` | 1 | 6,6 KB |

## Secoes internas detectadas

- PR Comment Handler
-   1) Inspect comments needing attention
-   2) Ask the user for clarification
-   3) If user chooses comments

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/desenvolvimento-devops/gh-address-comments/agents/openai.yaml` | 309 B |
| `skills/desenvolvimento-devops/gh-address-comments/assets/github.png` | 1,8 KB |
| `skills/desenvolvimento-devops/gh-address-comments/assets/github-small.svg` | 856 B |
| `skills/desenvolvimento-devops/gh-address-comments/LICENSE.txt` | 11,3 KB |
| `skills/desenvolvimento-devops/gh-address-comments/scripts/fetch_comments.py` | 6,6 KB |
| `skills/desenvolvimento-devops/gh-address-comments/SKILL.md` | 1,3 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\gh-address-comments`
- `C:\Users\filip\.agents\skills\gh-address-comments`
- `C:\Users\filip\.claude\skills\gh-address-comments`
- `C:\Users\filip\.gemini\skills\gh-address-comments`
- `C:\Users\filip\.windsurf\skills\gh-address-comments`

## Conteudo integral do SKILL.md

```
markdown
---
name: gh-address-comments
description: Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.
metadata:
  short-description: Address comments in a GitHub PR review
---

# PR Comment Handler

Guide to find the open PR for the current branch and address its comments with gh CLI. Run all `gh` commands with elevated network access.

Prereq: ensure `gh` is authenticated (for example, run `gh auth login` once), then run `gh auth status` with escalated permissions (include workflow/repo scopes) so `gh` commands succeed. If sandboxing blocks `gh auth status`, rerun it with `sandbox_permissions=require_escalated`.

## 1) Inspect comments needing attention
- Run scripts/fetch_comments.py which will print out all the comments and review threads on the PR

## 2) Ask the user for clarification
- Number all the review threads and comments and provide a short summary of what would be required to apply a fix for it
- Ask the user which numbered comments should be addressed

## 3) If user chooses comments
- Apply fixes for the selected comments

Notes:
- If gh hits auth/rate issues mid-run, prompt the user to re-authenticate with `gh auth login`, then retry.
```
