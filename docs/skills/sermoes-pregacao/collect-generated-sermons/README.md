# collect-generated-sermons

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `collect-generated-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/collect-generated-sermons.zip`
- Pasta copiada: `skills/sermoes-pregacao/collect-generated-sermons`
- Fonte original: `C:\Users\filip\.codex\skills\collect-generated-sermons`
- Hash do `SKILL.md`: `dab42f05d9bec269a27577d7af1de9e8314bbc9779fc8c62343e18cfcb1d536a`

## Resumo

Copy generated sermon `.docx` files from the `outputs` folders inside sermon skills whose names start with `generate-` under `C:\Users\filip\.codex\skills` into `C:\Users\filip\OneDrive\Área de Trabalho\Sermoes_Gerados_Codex`. Use when the user asks to gather, consolidate, export, collect, or centralize Word sermon files created by the `generate-*` skills into one desktop folder.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/collect-generated-sermons.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `collect-generated-sermons` |
| Skill name | `collect-generated-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\collect-generated-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/collect-generated-sermons` |
| Arquivo principal | `skills/sermoes-pregacao/collect-generated-sermons/SKILL.md` |
| Zip | `packages/sermoes-pregacao/collect-generated-sermons.zip` |
| Tamanho do zip | 3,0 KB |
| Duplicatas consolidadas | 5 |

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
| Tamanho copiado | 6,0 KB |

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
-   Final Output Override (MD Only)
-   Pergunta Inicial Obrigatoria (Escopo da Producao)

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/collect-generated-sermons/agents/openai.yaml` | 272 B |
| `skills/sermoes-pregacao/collect-generated-sermons/scripts/copy_generated_sermons.py` | 2,7 KB |
| `skills/sermoes-pregacao/collect-generated-sermons/SKILL.md` | 3,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\collect-generated-sermons`
- `C:\Users\filip\.agents\skills\collect-generated-sermons`
- `C:\Users\filip\.claude\skills\collect-generated-sermons`
- `C:\Users\filip\.cursor\skills\collect-generated-sermons`
- `C:\Users\filip\.windsurf\skills\collect-generated-sermons`

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

## Final Output Override (MD Only)

- Esta skill deve entregar exatamente um unico arquivo final `.md`.
- Nao gerar `.docx`, `.epub`, `.pdf`, `.csv`, `.xlsx` ou qualquer outro artefato final.
- Salvar o arquivo final `.md` em `C:\Users\filip\Dropbox\Obsidian_Filipe\Ministério\Sermões\Skill_Revisar`.
- Entregar ao usuario apenas o caminho absoluto desse `.md` salvo.
- Se qualquer instrucao deste arquivo conflitar com esta secao, esta secao prevalece.

## Pergunta Inicial Obrigatoria (Escopo da Producao)

Antes de iniciar qualquer producao, esta skill deve sempre perguntar ao usuario:

`Voce quer apenas o esboco ou a versao completa (sermao/palestra)?`

Opcoes e regras:

- `Esboco`: gerar somente a estrutura (titulo, tese central, pontos principais, transicoes, aplicacoes e conclusao resumida), sem manuscrito completo.
- `Completa`: gerar o manuscrito completo.
- Se a resposta nao estiver clara, pausar e pedir confirmacao antes de escrever.
- Esta pergunta e obrigatoria e deve acontecer antes de qualquer etapa de redacao.
- Em fluxos em lote, fazer a pergunta uma vez no inicio e aplicar a resposta a todos os itens, salvo instrucao contraria do usuario.
```
