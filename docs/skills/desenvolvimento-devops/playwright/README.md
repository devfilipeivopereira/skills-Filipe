# playwright

- Categoria: **Desenvolvimento e DevOps** (`desenvolvimento-devops`)
- Nome declarado: `playwright`
- Pacote instalavel: `packages/desenvolvimento-devops/playwright.zip`
- Pasta copiada: `skills/desenvolvimento-devops/playwright`
- Fonte original: `C:\Users\filip\.codex\skills\playwright`
- Hash do `SKILL.md`: `c52cc95125b720cdc3c9829b0294c2752d4ae9b85a5282aa153da8bba929af87`

## Resumo

Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

## Instalacao individual

```powershell
$zip = "packages/desenvolvimento-devops/playwright.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `playwright` |
| Skill name | `playwright` |
| Categoria | `desenvolvimento-devops` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\playwright` |
| Pasta no repositorio | `skills/desenvolvimento-devops/playwright` |
| Arquivo principal | `skills/desenvolvimento-devops/playwright/SKILL.md` |
| Zip | `packages/desenvolvimento-devops/playwright.zip` |
| Tamanho do zip | 11,2 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | playwright |
| `description` | Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 9 |
| Diretorios | 4 |
| Tamanho copiado | 22,7 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 319 B |
| `assets` | 2 | 2,5 KB |
| `references` | 2 | 3,8 KB |
| `scripts` | 1 | 551 B |

## Secoes internas detectadas

- Playwright CLI Skill
-   Prerequisite check (required)
- Verify Node/npm are installed
- If missing, install Node.js/npm, then:
-   Skill path (set once)
-   Quick start
-   Core workflow
-   When to snapshot again
-   Recommended patterns
-     Form fill and submit
-     Debug a UI flow with traces
- ...interactions...
-     Multi-tab work
-   Wrapper script
-   References
-   Guardrails

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/desenvolvimento-devops/playwright/agents/openai.yaml` | 319 B |
| `skills/desenvolvimento-devops/playwright/assets/playwright.png` | 1,7 KB |
| `skills/desenvolvimento-devops/playwright/assets/playwright-small.svg` | 831 B |
| `skills/desenvolvimento-devops/playwright/LICENSE.txt` | 11,3 KB |
| `skills/desenvolvimento-devops/playwright/NOTICE.txt` | 417 B |
| `skills/desenvolvimento-devops/playwright/references/cli.md` | 1,9 KB |
| `skills/desenvolvimento-devops/playwright/references/workflows.md` | 1,9 KB |
| `skills/desenvolvimento-devops/playwright/scripts/playwright_cli.sh` | 551 B |
| `skills/desenvolvimento-devops/playwright/SKILL.md` | 3,8 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\playwright`

## Conteudo integral do SKILL.md

````
markdown
---
name: "playwright"
description: "Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script."
---


# Playwright CLI Skill

Drive a real browser from the terminal using `playwright-cli`. Prefer the bundled wrapper script so the CLI works even when it is not globally installed.
Treat this skill as CLI-first automation. Do not pivot to `@playwright/test` unless the user explicitly asks for test files.

## Prerequisite check (required)

Before proposing commands, check whether `npx` is available (the wrapper depends on it):

```bash
command -v npx >/dev/null 2>&1
```

If it is not available, pause and ask the user to install Node.js/npm (which provides `npx`). Provide these steps verbatim:

```bash
# Verify Node/npm are installed
node --version
npm --version

# If missing, install Node.js/npm, then:
npm install -g @playwright/cli@latest
playwright-cli --help
```

Once `npx` is present, proceed with the wrapper script. A global install of `playwright-cli` is optional.

## Skill path (set once)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export PWCLI="$CODEX_HOME/skills/playwright/scripts/playwright_cli.sh"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Quick start

Use the wrapper script:

```bash
"$PWCLI" open https://playwright.dev --headed
"$PWCLI" snapshot
"$PWCLI" click e15
"$PWCLI" type "Playwright"
"$PWCLI" press Enter
"$PWCLI" screenshot
```

If the user prefers a global install, this is also valid:

```bash
npm install -g @playwright/cli@latest
playwright-cli --help
```

## Core workflow

1. Open the page.
2. Snapshot to get stable element refs.
3. Interact using refs from the latest snapshot.
4. Re-snapshot after navigation or significant DOM changes.
5. Capture artifacts (screenshot, pdf, traces) when useful.

Minimal loop:

```bash
"$PWCLI" open https://example.com
"$PWCLI" snapshot
"$PWCLI" click e3
"$PWCLI" snapshot
```

## When to snapshot again

Snapshot again after:

- navigation
- clicking elements that change the UI substantially
- opening/closing modals or menus
- tab switches

Refs can go stale. When a command fails due to a missing ref, snapshot again.

## Recommended patterns

### Form fill and submit

```bash
"$PWCLI" open https://example.com/form
"$PWCLI" snapshot
"$PWCLI" fill e1 "user@example.com"
"$PWCLI" fill e2 "password123"
"$PWCLI" click e3
"$PWCLI" snapshot
```

### Debug a UI flow with traces

```bash
"$PWCLI" open https://example.com --headed
"$PWCLI" tracing-start
# ...interactions...
"$PWCLI" tracing-stop
```

### Multi-tab work

```bash
"$PWCLI" tab-new https://example.com
"$PWCLI" tab-list
"$PWCLI" tab-select 0
"$PWCLI" snapshot
```

## Wrapper script

The wrapper script uses `npx --package @playwright/cli playwright-cli` so the CLI can run without a global install:

```bash
"$PWCLI" --help
```

Prefer the wrapper unless the repository already standardizes on a global install.

## References

Open only what you need:

- CLI command reference: `references/cli.md`
- Practical workflows and troubleshooting: `references/workflows.md`

## Guardrails

- Always snapshot before referencing element ids like `e12`.
- Re-snapshot when refs seem stale.
- Prefer explicit commands over `eval` and `run-code` unless needed.
- When you do not have a fresh snapshot, use placeholder refs like `eX` and say why; do not bypass refs with `run-code`.
- Use `--headed` when a visual check will help.
- When capturing artifacts in this repo, use `output/playwright/` and avoid introducing new top-level artifact folders.
- Default to CLI commands and workflows, not Playwright test specs.
````
