# vercel-deploy

- Categoria: **Desenvolvimento e DevOps** (`desenvolvimento-devops`)
- Nome declarado: `vercel-deploy`
- Pacote instalavel: `packages/desenvolvimento-devops/vercel-deploy.zip`
- Pasta copiada: `skills/desenvolvimento-devops/vercel-deploy`
- Fonte original: `C:\Users\filip\.codex\skills\vercel-deploy`
- Hash do `SKILL.md`: `afac6b5b71952af08f8dcd19c01ec1d80a040240cc50929e3add8200b3fcd459`

## Resumo

Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

## Instalacao individual

```powershell
$zip = "packages/desenvolvimento-devops/vercel-deploy.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `vercel-deploy` |
| Skill name | `vercel-deploy` |
| Categoria | `desenvolvimento-devops` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\vercel-deploy` |
| Pasta no repositorio | `skills/desenvolvimento-devops/vercel-deploy` |
| Arquivo principal | `skills/desenvolvimento-devops/vercel-deploy/SKILL.md` |
| Zip | `packages/desenvolvimento-devops/vercel-deploy.zip` |
| Tamanho do zip | 6,4 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | vercel-deploy |
| `description` | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment". |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 6 |
| Diretorios | 3 |
| Tamanho copiado | 14,0 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 312 B |
| `assets` | 2 | 1,0 KB |
| `scripts` | 1 | 9,0 KB |

## Secoes internas detectadas

- Vercel Deploy
-   Prerequisites
-   Quick Start
-   Fallback (No Auth)
- Deploy current directory
- Deploy specific project
- Deploy existing tarball
-   Production Deploys
-   Output
-   Troubleshooting
-     Escalated Network Access

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/desenvolvimento-devops/vercel-deploy/agents/openai.yaml` | 312 B |
| `skills/desenvolvimento-devops/vercel-deploy/assets/vercel.png` | 788 B |
| `skills/desenvolvimento-devops/vercel-deploy/assets/vercel-small.svg` | 248 B |
| `skills/desenvolvimento-devops/vercel-deploy/LICENSE.txt` | 1,1 KB |
| `skills/desenvolvimento-devops/vercel-deploy/scripts/deploy.sh` | 9,0 KB |
| `skills/desenvolvimento-devops/vercel-deploy/SKILL.md` | 2,7 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\vercel-deploy`
- `C:\Users\filip\.agents\skills\vercel-deploy`
- `C:\Users\filip\.claude\skills\vercel-deploy`
- `C:\Users\filip\.gemini\skills\vercel-deploy`
- `C:\Users\filip\.windsurf\skills\vercel-deploy`

## Conteudo integral do SKILL.md

````
markdown
---
name: vercel-deploy
description: Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".
---

# Vercel Deploy

Deploy any project to Vercel instantly. **Always deploy as preview** (not production) unless the user explicitly asks for production.

## Prerequisites

- Check whether the Vercel CLI is installed **without** escalated permissions (for example, `command -v vercel`).
- Only escalate the actual deploy command if sandboxing blocks the deployment network calls (`sandbox_permissions=require_escalated`).
- The deployment might take a few minutes. Use appropriate timeout values.

## Quick Start

1. Check whether the Vercel CLI is installed (no escalation for this check):

```bash
command -v vercel
```

2. If `vercel` is installed, run this (with a 10 minute timeout):
```bash
vercel deploy [path] -y
```

**Important:** Use a 10 minute (600000ms) timeout for the deploy command since builds can take a while.

3. If `vercel` is not installed, or if the CLI fails with "No existing credentials found", use the fallback method below.

## Fallback (No Auth)

If CLI fails with auth error, use the deploy script:

```bash
skill_dir="<path-to-skill>"

# Deploy current directory
bash "$skill_dir/scripts/deploy.sh"

# Deploy specific project
bash "$skill_dir/scripts/deploy.sh" /path/to/project

# Deploy existing tarball
bash "$skill_dir/scripts/deploy.sh" /path/to/project.tgz
```

The script handles framework detection, packaging, and deployment. It waits for the build to complete and returns JSON with `previewUrl` and `claimUrl`.

**Tell the user:** "Your deployment is ready at [previewUrl]. Claim it at [claimUrl] to manage your deployment."

## Production Deploys

Only if user explicitly asks:
```bash
vercel deploy [path] --prod -y
```

## Output

Show the user the deployment URL. For fallback deployments, also show the claim URL.

**Do not** curl or fetch the deployed URL to verify it works. Just return the link.

## Troubleshooting

### Escalated Network Access

If deployment fails due to network issues (timeouts, DNS errors, connection resets), rerun the actual deploy command with escalated permissions (use `sandbox_permissions=require_escalated`). Do not escalate the `command -v vercel` installation check. The deploy requires escalated network access when sandbox networking blocks outbound requests.

Example guidance to the user:

```
The deploy needs escalated network access to deploy to Vercel. I can rerun the command with escalated permissions—want me to proceed?
```
````
