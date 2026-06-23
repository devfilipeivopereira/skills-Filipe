# Skills Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consolidar as skills instalaveis das pastas locais de IAs em uma biblioteca versionada com categorias, documentacao e pacotes `.zip` individuais.

**Architecture:** Um script PowerShell reexecutavel descobre diretorios com `SKILL.md`, prioriza `C:\Users\filip\.codex\skills`, deduplica por identificador e hash do `SKILL.md`, copia cada skill para `skills/<categoria>/<pacote>/` e gera `packages/<categoria>/<pacote>.zip`. A documentacao e os manifestos sao derivados do mesmo inventario para evitar divergencia manual.

**Tech Stack:** PowerShell, Git, Markdown, JSON, CSV e `Compress-Archive`.

---

### Task 1: Repository Bootstrap

**Files:**
- Create: `.gitignore`
- Create: `docs/superpowers/plans/2026-06-23-skills-library.md`

- [x] **Step 1: Connect the workspace to GitHub**

Run: `git clone https://github.com/devfilipeivopereira/skills-Filipe.git .`

Expected: repository cloned locally, even if the remote is empty.

- [x] **Step 2: Add generated-file ignores**

Create `.gitignore` with temporary build output ignored:

```gitignore
.tmp-skill-build/
*.tmp
Thumbs.db
.DS_Store
```

### Task 2: Skill Discovery and Packaging Script

**Files:**
- Create: `scripts/organize-skills.ps1`
- Generate: `skills/<categoria>/<pacote>/...`
- Generate: `packages/<categoria>/<pacote>.zip`
- Generate: `README.md`
- Generate: `INSTALL.md`
- Generate: `docs/CATALOGO.md`
- Generate: `docs/FONTES.md`
- Generate: `docs/manifest.json`
- Generate: `docs/manifest.csv`

- [ ] **Step 1: Discover installable skill roots**

Scan direct children with `SKILL.md` under:

```powershell
C:\Users\filip\.codex\skills
C:\Users\filip\.codex\skills\.system
C:\Users\filip\.codex\superpowers\skills
C:\Users\filip\.agents\skills
C:\Users\filip\.agents\skills\.system
C:\Users\filip\.claude\skills
C:\Users\filip\.cursor\skills
C:\Users\filip\.gemini\skills
C:\Users\filip\.windsurf\skills
C:\Users\filip\.codex-2\skills
C:\Users\filip\.codex-3\skills
C:\Users\filip\.codex-4\skills
C:\Users\filip\.codex-5\skills
```

Also scan plugin cache folders named `skills` under `.codex\plugins\cache` and `.agents\plugins\cache`.

- [ ] **Step 2: Deduplicate and categorize**

Use frontmatter `name` and `description` from `SKILL.md`, prioritize `.codex\skills`, preserve lower-priority variants when their `SKILL.md` hash differs, and assign categories by name/description heuristics.

- [ ] **Step 3: Copy installable packages**

Copy each selected skill to `skills/<categoria>/<package_id>/`, skipping nested descendant directories that contain their own `SKILL.md` so backup skill trees do not explode package size.

- [ ] **Step 4: Generate install zips**

Create one `.zip` per package in `packages/<categoria>/`.

- [ ] **Step 5: Generate documentation and manifest files**

Write `README.md`, `INSTALL.md`, `docs/CATALOGO.md`, `docs/FONTES.md`, `docs/manifest.json`, and `docs/manifest.csv` from the selected manifest.

### Task 3: Verification and Publication

**Files:**
- Verify: generated docs, generated zips, Git status

- [ ] **Step 1: Run the organizer**

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/organize-skills.ps1 -Clean
```

Expected: script reports discovered candidates, selected packages, copied skills, and generated zips.

- [ ] **Step 2: Verify counts**

Run:

```powershell
$manifest = Get-Content -Raw docs/manifest.json | ConvertFrom-Json
$zipCount = (Get-ChildItem packages -Recurse -Filter *.zip | Measure-Object).Count
"skills=$($manifest.skills.Count); zips=$zipCount"
```

Expected: `skills` and `zips` counts match.

- [ ] **Step 3: Commit and push**

Run:

```powershell
git add .
git commit -m "Organize local AI skills library"
git push -u origin main
```

Expected: commit created and pushed to `devfilipeivopereira/skills-Filipe`.
