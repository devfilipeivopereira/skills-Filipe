# notion-corrigido-from-transcricoes

- Categoria: **Editorial, Ebooks e KDP** (`editorial-ebooks-kdp`)
- Nome declarado: `notion-corrigido-from-transcricoes`
- Pacote instalavel: `packages/editorial-ebooks-kdp/notion-corrigido-from-transcricoes.zip`
- Pasta copiada: `skills/editorial-ebooks-kdp/notion-corrigido-from-transcricoes`
- Fonte original: `C:\Users\filip\.codex\skills\notion-corrigido-from-transcricoes`
- Hash do `SKILL.md`: `1b56d1b5b6ffd74678b28f3d5835f286d53461e873c3bf7095c11b71b48b19e3`

## Resumo

Ler um banco do Notion, baixar o arquivo .txt da coluna Transcrições, corrigir o texto em português preservando o sermão e gravar o resultado na coluna Corrigido com nome de arquivo iniciado por underscore. Use quando o usuário pedir para corrigir transcrições no Notion, limpar texto bruto de pregação ou preencher a coluna Corrigido a partir de Transcrições.

## Instalacao individual

```powershell
$zip = "packages/editorial-ebooks-kdp/notion-corrigido-from-transcricoes.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `notion-corrigido-from-transcricoes` |
| Skill name | `notion-corrigido-from-transcricoes` |
| Categoria | `editorial-ebooks-kdp` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\notion-corrigido-from-transcricoes` |
| Pasta no repositorio | `skills/editorial-ebooks-kdp/notion-corrigido-from-transcricoes` |
| Arquivo principal | `skills/editorial-ebooks-kdp/notion-corrigido-from-transcricoes/SKILL.md` |
| Zip | `packages/editorial-ebooks-kdp/notion-corrigido-from-transcricoes.zip` |
| Tamanho do zip | 7,0 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | notion-corrigido-from-transcricoes |
| `description` | Ler um banco do Notion, baixar o arquivo .txt da coluna Transcrições, corrigir o texto em português preservando o sermão e gravar o resultado na coluna Corrigido com nome de arquivo iniciado por underscore. Use quando o usuário pedir para corrigir transcrições no Notion, limpar texto bruto de pregação ou preencher a coluna Corrigido a partir de Transcrições. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 4 |
| Diretorios | 3 |
| Tamanho copiado | 19,2 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 339 B |
| `references` | 1 | 921 B |
| `scripts` | 1 | 14,4 KB |

## Secoes internas detectadas

- Notion Corrigido From Transcricoes
-   Fluxo
-   Setup
-   Comandos
-   Regras de correção
-   Escopo do texto
-   Nome do arquivo
-   Observações

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/editorial-ebooks-kdp/notion-corrigido-from-transcricoes/agents/openai.yaml` | 339 B |
| `skills/editorial-ebooks-kdp/notion-corrigido-from-transcricoes/references/correction-guidelines.md` | 921 B |
| `skills/editorial-ebooks-kdp/notion-corrigido-from-transcricoes/scripts/notion_corrigido_pipeline.py` | 14,4 KB |
| `skills/editorial-ebooks-kdp/notion-corrigido-from-transcricoes/SKILL.md` | 3,6 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\notion-corrigido-from-transcricoes`
- `C:\Users\filip\.agents\skills\notion-corrigido-from-transcricoes`
- `C:\Users\filip\.claude\skills\notion-corrigido-from-transcricoes`
- `C:\Users\filip\.gemini\skills\notion-corrigido-from-transcricoes`
- `C:\Users\filip\.windsurf\skills\notion-corrigido-from-transcricoes`

## Conteudo integral do SKILL.md

````
markdown
---
name: notion-corrigido-from-transcricoes
description: Ler um banco do Notion, baixar o arquivo .txt da coluna Transcrições, corrigir o texto em português preservando o sermão e gravar o resultado na coluna Corrigido com nome de arquivo iniciado por underscore. Use quando o usuário pedir para corrigir transcrições no Notion, limpar texto bruto de pregação ou preencher a coluna Corrigido a partir de Transcrições.
---

# Notion Corrigido From Transcricoes

Use esta skill para transformar o arquivo bruto da coluna `Transcrições` em um texto corrigido e salvar o resultado em `Corrigido`, mantendo o fluxo dentro do banco do Notion.

## Fluxo

1. Defina `NOTION_TOKEN` e `NOTION_DATABASE_ID` no shell.
2. Rode `inspect` se precisar confirmar o schema do banco.
3. Rode `pull` para exportar páginas com `Transcrições` preenchido e `Corrigido` vazio.
4. Corrija o texto localmente.
5. Salve o corrigido em `.txt`.
6. Rode `push` para anexar o arquivo na coluna `Corrigido` com nome iniciado por `_`.

## Setup

```powershell
$env:NOTION_TOKEN = 'seu_token'
$env:NOTION_DATABASE_ID = 'seu_database_id'
```

## Comandos

Inspecionar o schema:

```powershell
python "C:\Users\filip\.codex\skills\notion-corrigido-from-transcricoes\scripts\notion_corrigido_pipeline.py" inspect
```

Exportar páginas pendentes:

```powershell
python "C:\Users\filip\.codex\skills\notion-corrigido-from-transcricoes\scripts\notion_corrigido_pipeline.py" pull --out pending-corrigido.json
```

Enviar o arquivo corrigido para a coluna `Corrigido`:

```powershell
python "C:\Users\filip\.codex\skills\notion-corrigido-from-transcricoes\scripts\notion_corrigido_pipeline.py" push --page-id "<page_id>" --input-file "corrigido.txt"
```

## Regras de correção

Leia [references/correction-guidelines.md](references/correction-guidelines.md) antes de corrigir.

Ao corrigir o conteúdo de `Transcrições`:

- Preserve o conteúdo da pregação.
- Corrija ortografia, acentuação, pontuação e quebras de frase.
- Normalize nomes bíblicos, referências e vocabulário cristão quando estiverem claramente identificáveis no áudio transcrito.
- Remova ruído de ASR que não agrega sentido.
- Preserve o sentido original do pregador.
- Não transforme a transcrição em ebook.
- Não adicione conteúdo novo além do necessário para corrigir e clarificar.
- Mantenha o texto em português do Brasil.
- Quando houver dúvida real de audição, prefira manter formulação conservadora em vez de inventar.

## Escopo do texto

O objetivo desta skill é produzir uma transcrição corrigida, não ainda o material final de publicação. Portanto:

- Mantenha a mensagem pregada.
- Pode manter abertura e encerramento do sermão se fizerem parte da fala principal.
- Pode remover sujeira técnica evidente, como ruídos, marcas repetidas, sobras sem sentido e duplicações geradas pela transcrição automática.
- Não inclua avisos administrativos, blocos musicais completos ou partes posteriores do culto se estiverem claramente fora do sermão principal, quando o usuário quiser apenas a pregação.

## Nome do arquivo

Ao enviar para `Corrigido`, o arquivo precisa:

- manter extensão `.txt`
- usar o nome original como base quando possível
- começar com `_`

Exemplo:

- origem: `ACENDA AS LUZES NESSE NATAL.txt`
- destino: `_ACENDA AS LUZES NESSE NATAL.txt`

## Observações

- No banco do usuário, `Transcrições` e `Corrigido` podem ser colunas do tipo `files`.
- O script localiza propriedades por nome de forma tolerante a acentos e maiúsculas.
- O script baixa o `.txt` de `Transcrições` e sobe o corrigido pronto em `Corrigido`.
- A correção textual continua sendo responsabilidade do agente usando esta skill.
````
