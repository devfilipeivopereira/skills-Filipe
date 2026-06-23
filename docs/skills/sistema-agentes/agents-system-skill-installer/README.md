# agents-system-skill-installer

- Categoria: **Sistema e Agentes** (`sistema-agentes`)
- Nome declarado: `skill-installer`
- Pacote instalavel: `packages/sistema-agentes/agents-system-skill-installer.zip`
- Pasta copiada: `skills/sistema-agentes/agents-system-skill-installer`
- Fonte original: `C:\Users\filip\.agents\skills\.system\skill-installer`
- Hash do `SKILL.md`: `2d3be2289274cbffb9eb632b25a1038aa7f369df6aaa0964077c77648547e01d`

## Resumo

Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

## Instalacao individual

```powershell
$zip = "packages/sistema-agentes/agents-system-skill-installer.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `agents-system-skill-installer` |
| Skill name | `skill-installer` |
| Categoria | `sistema-agentes` |
| Namespace | `agents-system` |
| Tipo da fonte | Agents system |
| Fonte original | `C:\Users\filip\.agents\skills\.system\skill-installer` |
| Pasta no repositorio | `skills/sistema-agentes/agents-system-skill-installer` |
| Arquivo principal | `skills/sistema-agentes/agents-system-skill-installer/SKILL.md` |
| Zip | `packages/sistema-agentes/agents-system-skill-installer.zip` |
| Tamanho do zip | 12,8 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | skill-installer |
| `description` | Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos). |
| `metadata` |  |
| `short-description` | Install curated skills from openai/skills or other repos |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 30,6 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 226 B |
| `assets` | 2 | 2,0 KB |
| `scripts` | 3 | 13,8 KB |

## Secoes internas detectadas

- Skill Installer
-   Communication
-   Scripts
-   Behavior and Options
-   Notes

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sistema-agentes/agents-system-skill-installer/agents/openai.yaml` | 226 B |
| `skills/sistema-agentes/agents-system-skill-installer/assets/skill-installer.png` | 1,1 KB |
| `skills/sistema-agentes/agents-system-skill-installer/assets/skill-installer-small.svg` | 926 B |
| `skills/sistema-agentes/agents-system-skill-installer/LICENSE.txt` | 11,3 KB |
| `skills/sistema-agentes/agents-system-skill-installer/scripts/github_utils.py` | 680 B |
| `skills/sistema-agentes/agents-system-skill-installer/scripts/install-skill-from-github.py` | 10,2 KB |
| `skills/sistema-agentes/agents-system-skill-installer/scripts/list-skills.py` | 3,0 KB |
| `skills/sistema-agentes/agents-system-skill-installer/SKILL.md` | 3,3 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.agents\skills\.system\skill-installer`

## Conteudo integral do SKILL.md

```
markdown
---
name: skill-installer
description: Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).
metadata:
  short-description: Install curated skills from openai/skills or other repos
---

# Skill Installer

Helps install skills. By default these are from https://github.com/openai/skills/tree/main/skills/.curated, but users can also provide other locations. Experimental skills live in https://github.com/openai/skills/tree/main/skills/.experimental and can be installed the same way.

Use the helper scripts based on the task:
- List skills when the user asks what is available, or if the user uses this skill without specifying what to do. Default listing is `.curated`, but you can pass `--path skills/.experimental` when they ask about experimental skills.
- Install from the curated list when the user provides a skill name.
- Install from another repo when the user provides a GitHub repo/path (including private repos).

Install skills with the helper scripts.

## Communication

When listing skills, output approximately as follows, depending on the context of the user's request. If they ask about experimental skills, list from `.experimental` instead of `.curated` and label the source accordingly:
"""
Skills from {repo}:
1. skill-1
2. skill-2 (already installed)
3. ...
Which ones would you like installed?
"""

After installing a skill, tell the user: "Restart Codex to pick up new skills."

## Scripts

All of these scripts use network, so when running in the sandbox, request escalation when running them.

- `scripts/list-skills.py` (prints skills list with installed annotations)
- `scripts/list-skills.py --format json`
- Example (experimental list): `scripts/list-skills.py --path skills/.experimental`
- `scripts/install-skill-from-github.py --repo <owner>/<repo> --path <path/to/skill> [<path/to/skill> ...]`
- `scripts/install-skill-from-github.py --url https://github.com/<owner>/<repo>/tree/<ref>/<path>`
- Example (experimental skill): `scripts/install-skill-from-github.py --repo openai/skills --path skills/.experimental/<skill-name>`

## Behavior and Options

- Defaults to direct download for public GitHub repos.
- If download fails with auth/permission errors, falls back to git sparse checkout.
- Aborts if the destination skill directory already exists.
- Installs into `$CODEX_HOME/skills/<skill-name>` (defaults to `~/.codex/skills`).
- Multiple `--path` values install multiple skills in one run, each named from the path basename unless `--name` is supplied.
- Options: `--ref <ref>` (default `main`), `--dest <path>`, `--method auto|download|git`.

## Notes

- Curated listing is fetched from `https://github.com/openai/skills/tree/main/skills/.curated` via the GitHub API. If it is unavailable, explain the error and exit.
- Private GitHub repos can be accessed via existing git credentials or optional `GITHUB_TOKEN`/`GH_TOKEN` for download.
- Git fallback tries HTTPS first, then SSH.
- The skills at https://github.com/openai/skills/tree/main/skills/.system are preinstalled, so no need to help users install those. If they ask, just explain this. If they insist, you can download and overwrite.
- Installed annotations come from `$CODEX_HOME/skills`.
```
