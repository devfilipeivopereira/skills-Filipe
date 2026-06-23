# collect-generated-sermons--v2

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `collect-generated-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/collect-generated-sermons--v2.zip`
- Pasta copiada: `skills/sermoes-pregacao/collect-generated-sermons--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\collect-generated-sermons`
- Hash do `SKILL.md`: `b7b454365f0b97b213a4235fd6be598f055366ff3afe9244f3a921518197af9d`

## Resumo

Copy generated sermon `.docx` files from the `outputs` folders inside sermon skills whose names start with `generate-` under `C:\Users\filip\.codex\skills` into `C:\Users\filip\OneDrive\Área de Trabalho\Sermoes_Gerados_Codex`. Use when the user asks to gather, consolidate, export, collect, or centralize Word sermon files created by the `generate-*` skills into one desktop folder.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/collect-generated-sermons--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `collect-generated-sermons--v2` |
| Skill name | `collect-generated-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\collect-generated-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/collect-generated-sermons--v2` |
| Arquivo principal | `skills/sermoes-pregacao/collect-generated-sermons--v2/SKILL.md` |
| Zip | `packages/sermoes-pregacao/collect-generated-sermons--v2.zip` |
| Tamanho do zip | 2,4 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | collect-generated-sermons |
| `description` | Copy generated sermon `.docx` files from the `outputs` folders inside sermon skills whose names start with `generate-` under `C:\Users\filip\.codex\skills` into `C:\Users\filip\OneDrive\Área de Trabalho\Sermoes_Gerados_Codex`. Use when the user asks to gather, consolidate, export, collect, or centralize Word sermon files created by the `generate-*` skills into one desktop folder. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 3 |
| Diretorios | 2 |
| Tamanho copiado | 4,9 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 272 B |
| `scripts` | 1 | 2,7 KB |

## Secoes internas detectadas

- Collect Generated Sermons
-   Workflow
-   Notes
-   Script

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/collect-generated-sermons--v2/agents/openai.yaml` | 272 B |
| `skills/sermoes-pregacao/collect-generated-sermons--v2/scripts/copy_generated_sermons.py` | 2,7 KB |
| `skills/sermoes-pregacao/collect-generated-sermons--v2/SKILL.md` | 1,9 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\collect-generated-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: collect-generated-sermons
description: Copy generated sermon `.docx` files from the `outputs` folders inside sermon skills whose names start with `generate-` under `C:\Users\filip\.codex\skills` into `C:\Users\filip\OneDrive\Área de Trabalho\Sermoes_Gerados_Codex`. Use when the user asks to gather, consolidate, export, collect, or centralize Word sermon files created by the `generate-*` skills into one desktop folder.
---

# Collect Generated Sermons

Use `scripts/copy_generated_sermons.py` to gather `.docx` files from sermon-generating skills into a single desktop folder.

## Workflow

1. Run `python scripts/copy_generated_sermons.py`.
2. Let the script create `C:\Users\filip\OneDrive\Área de Trabalho\Sermoes_Gerados_Codex` if it does not exist.
3. Scan only skill folders matching `generate-*` inside `C:\Users\filip\.codex\skills`.
4. For each matching skill, inspect only its `outputs` folder.
5. Copy every `.docx` file found there into the desktop destination folder using the skill name as the base filename, removing the `generate-` prefix.
6. Skip the copy when the destination filename already exists. Do not overwrite and do not create renamed duplicates.
7. Report how many skill folders were checked, which skill folders had `.docx` files in `outputs`, which did not, how many files were copied, and which source files were skipped.

## Notes

- Treat missing `outputs` folders as normal; skip them silently unless reporting is useful.
- Treat the desktop folder as the canonical consolidated location for the user.
- Keep the scope limited to `.docx` files. Do not move, modify, or delete source files.
- Treat an existing destination file as already collected content and skip it.
- If the user asks for a different destination folder later, update the script and this skill accordingly.

## Script

- `scripts/copy_generated_sermons.py`: perform the collection and copy operation.
```
