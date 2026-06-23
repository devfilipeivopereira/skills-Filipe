# gh-fix-ci

- Categoria: **Notion e Produtividade** (`notion-produtividade`)
- Nome declarado: `gh-fix-ci`
- Pacote instalavel: `packages/notion-produtividade/gh-fix-ci.zip`
- Pasta copiada: `skills/notion-produtividade/gh-fix-ci`
- Fonte original: `C:\Users\filip\.codex\skills\gh-fix-ci`
- Hash do `SKILL.md`: `2e45c71cdf8690b54639c1b7aa6e4401f5db557c45b283e213d4f793cc570661`

## Resumo

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

## Instalacao individual

```powershell
$zip = "packages/notion-produtividade/gh-fix-ci.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `gh-fix-ci` |
| Skill name | `gh-fix-ci` |
| Categoria | `notion-produtividade` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\gh-fix-ci` |
| Pasta no repositorio | `skills/notion-produtividade/gh-fix-ci` |
| Arquivo principal | `skills/notion-produtividade/gh-fix-ci/SKILL.md` |
| Zip | `packages/notion-produtividade/gh-fix-ci.zip` |
| Tamanho do zip | 12,5 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | gh-fix-ci |
| `description` | Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 6 |
| Diretorios | 3 |
| Tamanho copiado | 32,6 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 308 B |
| `assets` | 2 | 2,6 KB |
| `scripts` | 1 | 15,4 KB |

## Secoes internas detectadas

- Gh Pr Checks Plan Fix
-   Overview
-   Inputs
-   Quick start
-   Workflow
-   Bundled Resources
-     scripts/inspect_pr_checks.py

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/notion-produtividade/gh-fix-ci/agents/openai.yaml` | 308 B |
| `skills/notion-produtividade/gh-fix-ci/assets/github.png` | 1,8 KB |
| `skills/notion-produtividade/gh-fix-ci/assets/github-small.svg` | 856 B |
| `skills/notion-produtividade/gh-fix-ci/LICENSE.txt` | 10,7 KB |
| `skills/notion-produtividade/gh-fix-ci/scripts/inspect_pr_checks.py` | 15,4 KB |
| `skills/notion-produtividade/gh-fix-ci/SKILL.md` | 3,6 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\gh-fix-ci`
- `C:\Users\filip\.agents\skills\gh-fix-ci`
- `C:\Users\filip\.claude\skills\gh-fix-ci`
- `C:\Users\filip\.gemini\skills\gh-fix-ci`
- `C:\Users\filip\.windsurf\skills\gh-fix-ci`

## Conteudo integral do SKILL.md

```
markdown
---
name: "gh-fix-ci"
description: "Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL."
---


# Gh Pr Checks Plan Fix

## Overview

Use gh to locate failing PR checks, fetch GitHub Actions logs for actionable failures, summarize the failure snippet, then propose a fix plan and implement after explicit approval.
- If a plan-oriented skill (for example `create-plan`) is available, use it; otherwise draft a concise plan inline and request approval before implementing.

Prereq: authenticate with the standard GitHub CLI once (for example, run `gh auth login`), then confirm with `gh auth status` (repo + workflow scopes are typically required).

## Inputs

- `repo`: path inside the repo (default `.`)
- `pr`: PR number or URL (optional; defaults to current branch PR)
- `gh` authentication for the repo host

## Quick start

- `python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "<number-or-url>"`
- Add `--json` if you want machine-friendly output for summarization.

## Workflow

1. Verify gh authentication.
   - Run `gh auth status` in the repo.
   - If unauthenticated, ask the user to run `gh auth login` (ensuring repo + workflow scopes) before proceeding.
2. Resolve the PR.
   - Prefer the current branch PR: `gh pr view --json number,url`.
   - If the user provides a PR number or URL, use that directly.
3. Inspect failing checks (GitHub Actions only).
   - Preferred: run the bundled script (handles gh field drift and job-log fallbacks):
     - `python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "<number-or-url>"`
     - Add `--json` for machine-friendly output.
   - Manual fallback:
     - `gh pr checks <pr> --json name,state,bucket,link,startedAt,completedAt,workflow`
       - If a field is rejected, rerun with the available fields reported by `gh`.
     - For each failing check, extract the run id from `detailsUrl` and run:
       - `gh run view <run_id> --json name,workflowName,conclusion,status,url,event,headBranch,headSha`
       - `gh run view <run_id> --log`
     - If the run log says it is still in progress, fetch job logs directly:
       - `gh api "/repos/<owner>/<repo>/actions/jobs/<job_id>/logs" > "<path>"`
4. Scope non-GitHub Actions checks.
   - If `detailsUrl` is not a GitHub Actions run, label it as external and only report the URL.
   - Do not attempt Buildkite or other providers; keep the workflow lean.
5. Summarize failures for the user.
   - Provide the failing check name, run URL (if any), and a concise log snippet.
   - Call out missing logs explicitly.
6. Create a plan.
   - Use the `create-plan` skill to draft a concise plan and request approval.
7. Implement after approval.
   - Apply the approved plan, summarize diffs/tests, and ask about opening a PR.
8. Recheck status.
   - After changes, suggest re-running the relevant tests and `gh pr checks` to confirm.

## Bundled Resources

### scripts/inspect_pr_checks.py

Fetch failing PR checks, pull GitHub Actions logs, and extract a failure snippet. Exits non-zero when failures remain so it can be used in automation.

Usage examples:
- `python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "123"`
- `python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "https://github.com/org/repo/pull/123" --json`
- `python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --max-lines 200 --context 40`
```
