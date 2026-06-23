# pdf

- Categoria: **Documentos, Dados e Midia** (`documentos-dados-midia`)
- Nome declarado: `pdf`
- Pacote instalavel: `packages/documentos-dados-midia/pdf.zip`
- Pasta copiada: `skills/documentos-dados-midia/pdf`
- Fonte original: `C:\Users\filip\.codex\skills\pdf`
- Hash do `SKILL.md`: `724b72c932053fd87133144405b00fbeec30285ee770168328c8f591ec89c134`

## Resumo

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

## Instalacao individual

```powershell
$zip = "packages/documentos-dados-midia/pdf.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `pdf` |
| Skill name | `pdf` |
| Categoria | `documentos-dados-midia` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\pdf` |
| Pasta no repositorio | `skills/documentos-dados-midia/pdf` |
| Arquivo principal | `skills/documentos-dados-midia/pdf/SKILL.md` |
| Zip | `packages/documentos-dados-midia/pdf.zip` |
| Tamanho do zip | 6,9 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | pdf |
| `description` | Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 4 |
| Diretorios | 2 |
| Tamanho copiado | 14,7 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 224 B |
| `assets` | 1 | 1,3 KB |

## Secoes internas detectadas

- PDF Skill
-   When to use
-   Workflow
-   Temp and output conventions
-   Dependencies (install if missing)
- macOS (Homebrew)
- Ubuntu/Debian
-   Environment
-   Rendering command
-   Quality expectations
-   Final checks

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/documentos-dados-midia/pdf/agents/openai.yaml` | 224 B |
| `skills/documentos-dados-midia/pdf/assets/pdf.png` | 1,3 KB |
| `skills/documentos-dados-midia/pdf/LICENSE.txt` | 10,7 KB |
| `skills/documentos-dados-midia/pdf/SKILL.md` | 2,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\pdf`

## Conteudo integral do SKILL.md

````
markdown
---
name: "pdf"
description: "Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction."
---


# PDF Skill

## When to use
- Read or review PDF content where layout and visuals matter.
- Create PDFs programmatically with reliable formatting.
- Validate final rendering before delivery.

## Workflow
1. Prefer visual review: render PDF pages to PNGs and inspect them.
   - Use `pdftoppm` if available.
   - If unavailable, install Poppler or ask the user to review the output locally.
2. Use `reportlab` to generate PDFs when creating new documents.
3. Use `pdfplumber` (or `pypdf`) for text extraction and quick checks; do not rely on it for layout fidelity.
4. After each meaningful update, re-render pages and verify alignment, spacing, and legibility.

## Temp and output conventions
- Use `tmp/pdfs/` for intermediate files; delete when done.
- Write final artifacts under `output/pdf/` when working in this repo.
- Keep filenames stable and descriptive.

## Dependencies (install if missing)
Prefer `uv` for dependency management.

Python packages:
```
uv pip install reportlab pdfplumber pypdf
```
If `uv` is unavailable:
```
python3 -m pip install reportlab pdfplumber pypdf
```
System tools (for rendering):
```
# macOS (Homebrew)
brew install poppler

# Ubuntu/Debian
sudo apt-get install -y poppler-utils
```

If installation isn't possible in this environment, tell the user which dependency is missing and how to install it locally.

## Environment
No required environment variables.

## Rendering command
```
pdftoppm -png $INPUT_PDF $OUTPUT_PREFIX
```

## Quality expectations
- Maintain polished visual design: consistent typography, spacing, margins, and section hierarchy.
- Avoid rendering issues: clipped text, overlapping elements, broken tables, black squares, or unreadable glyphs.
- Charts, tables, and images must be sharp, aligned, and clearly labeled.
- Use ASCII hyphens only. Avoid U+2011 (non-breaking hyphen) and other Unicode dashes.
- Citations and references must be human-readable; never leave tool tokens or placeholder strings.

## Final checks
- Do not deliver until the latest PNG inspection shows zero visual or formatting defects.
- Confirm headers/footers, page numbering, and section transitions look polished.
- Keep intermediate files organized or remove them after final approval.
````
