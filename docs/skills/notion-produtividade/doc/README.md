# doc

- Categoria: **Notion e Produtividade** (`notion-produtividade`)
- Nome declarado: `doc`
- Pacote instalavel: `packages/notion-produtividade/doc.zip`
- Pasta copiada: `skills/notion-produtividade/doc`
- Fonte original: `C:\Users\filip\.codex\skills\doc`
- Hash do `SKILL.md`: `2dd628afc3f9217d88bba8f61454b964aa25921f55f69e8d4d923b2ab092c54f`

## Resumo

Use when the task involves reading, creating, or editing `.docx` documents, especially when formatting or layout fidelity matters; prefer `python-docx` plus the bundled `scripts/render_docx.py` for visual checks.

## Instalacao individual

```powershell
$zip = "packages/notion-produtividade/doc.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `doc` |
| Skill name | `doc` |
| Categoria | `notion-produtividade` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\doc` |
| Pasta no repositorio | `skills/notion-produtividade/doc` |
| Arquivo principal | `skills/notion-produtividade/doc/SKILL.md` |
| Zip | `packages/notion-produtividade/doc.zip` |
| Tamanho do zip | 11,1 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | doc |
| `description` | Use when the task involves reading, creating, or editing `.docx` documents, especially when formatting or layout fidelity matters; prefer `python-docx` plus the bundled `scripts/render_docx.py` for visual checks. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 6 |
| Diretorios | 3 |
| Tamanho copiado | 26,6 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 277 B |
| `assets` | 2 | 2,8 KB |
| `scripts` | 1 | 9,8 KB |

## Secoes internas detectadas

- DOCX Skill
-   When to use
-   Workflow
-   Temp and output conventions
-   Dependencies (install if missing)
- macOS (Homebrew)
- Ubuntu/Debian
-   Environment
-   Rendering commands
-   Quality expectations
-   Final checks

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/notion-produtividade/doc/agents/openai.yaml` | 277 B |
| `skills/notion-produtividade/doc/assets/doc.png` | 1,2 KB |
| `skills/notion-produtividade/doc/assets/doc-small.svg` | 1,6 KB |
| `skills/notion-produtividade/doc/LICENSE.txt` | 10,7 KB |
| `skills/notion-produtividade/doc/scripts/render_docx.py` | 9,8 KB |
| `skills/notion-produtividade/doc/SKILL.md` | 3,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\doc`

## Conteudo integral do SKILL.md

````
markdown
---
name: "doc"
description: "Use when the task involves reading, creating, or editing `.docx` documents, especially when formatting or layout fidelity matters; prefer `python-docx` plus the bundled `scripts/render_docx.py` for visual checks."
---


# DOCX Skill

## When to use
- Read or review DOCX content where layout matters (tables, diagrams, pagination).
- Create or edit DOCX files with professional formatting.
- Validate visual layout before delivery.

## Workflow
1. Prefer visual review (layout, tables, diagrams).
   - If `soffice` and `pdftoppm` are available, convert DOCX -> PDF -> PNGs.
   - Or use `scripts/render_docx.py` (requires `pdf2image` and Poppler).
   - If these tools are missing, install them or ask the user to review rendered pages locally.
2. Use `python-docx` for edits and structured creation (headings, styles, tables, lists).
3. After each meaningful change, re-render and inspect the pages.
4. If visual review is not possible, extract text with `python-docx` as a fallback and call out layout risk.
5. Keep intermediate outputs organized and clean up after final approval.

## Temp and output conventions
- Use `tmp/docs/` for intermediate files; delete when done.
- Write final artifacts under `output/doc/` when working in this repo.
- Keep filenames stable and descriptive.

## Dependencies (install if missing)
Prefer `uv` for dependency management.

Python packages:
```
uv pip install python-docx pdf2image
```
If `uv` is unavailable:
```
python3 -m pip install python-docx pdf2image
```
System tools (for rendering):
```
# macOS (Homebrew)
brew install libreoffice poppler

# Ubuntu/Debian
sudo apt-get install -y libreoffice poppler-utils
```

If installation isn't possible in this environment, tell the user which dependency is missing and how to install it locally.

## Environment
No required environment variables.

## Rendering commands
DOCX -> PDF:
```
soffice -env:UserInstallation=file:///tmp/lo_profile_$$ --headless --convert-to pdf --outdir $OUTDIR $INPUT_DOCX
```

PDF -> PNGs:
```
pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME
```

Bundled helper:
```
python3 scripts/render_docx.py /path/to/file.docx --output_dir /tmp/docx_pages
```

## Quality expectations
- Deliver a client-ready document: consistent typography, spacing, margins, and clear hierarchy.
- Avoid formatting defects: clipped/overlapping text, broken tables, unreadable characters, or default-template styling.
- Charts, tables, and visuals must be legible in rendered pages with correct alignment.
- Use ASCII hyphens only. Avoid U+2011 (non-breaking hyphen) and other Unicode dashes.
- Citations and references must be human-readable; never leave tool tokens or placeholder strings.

## Final checks
- Re-render and inspect every page at 100% zoom before final delivery.
- Fix any spacing, alignment, or pagination issues and repeat the render loop.
- Confirm there are no leftovers (temp files, duplicate renders) unless the user asks to keep them.
````
