# sermon-pipeline--v3

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `sermon-pipeline`
- Pacote instalavel: `packages/sermoes-pregacao/sermon-pipeline--v3.zip`
- Pasta copiada: `skills/sermoes-pregacao/sermon-pipeline--v3`
- Fonte original: `C:\Users\filip\.gemini\skills\sermon-pipeline-skill`
- Hash do `SKILL.md`: `2c89e736250b6740afef49839aa468ece123724eb36d6f887fdb605ceeee3c92`

## Resumo

Pipeline completo para pregações do Pr. Filipe Ivo Pereira: busca vídeos de uma playlist ou canal do YouTube, baixa transcrições reais, gera resumos homiléticos detalhados com Claude e atualiza automaticamente o banco de dados de pregações no Notion. Use esta skill sempre que o usuário pedir para processar pregações do YouTube, gerar resumos de sermões, atualizar o Notion com descrições de vídeos, baixar transcrições de pregações, ou qualquer variação de "processar a playlist", "resumir as pregações", "atualizar o banco de sermões".

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/sermon-pipeline--v3.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `sermon-pipeline--v3` |
| Skill name | `sermon-pipeline` |
| Categoria | `sermoes-pregacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\sermon-pipeline-skill` |
| Pasta no repositorio | `skills/sermoes-pregacao/sermon-pipeline--v3` |
| Arquivo principal | `skills/sermoes-pregacao/sermon-pipeline--v3/SKILL.md` |
| Zip | `packages/sermoes-pregacao/sermon-pipeline--v3.zip` |
| Tamanho do zip | 9,4 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | sermon-pipeline |
| `description` | Pipeline completo para pregações do Pr. Filipe Ivo Pereira: busca vídeos de uma playlist ou canal do YouTube, baixa transcrições reais, gera resumos homiléticos detalhados com Claude e atualiza automaticamente o banco de dados de pregações no Notion. Use esta skill sempre que o usuário pedir para processar pregações do YouTube, gerar resumos de sermões, atualizar o Notion com descrições de vídeos, baixar transcrições de pregações, ou qualquer variação de "processar a playlist", "resumir as pregações", "atualizar o banco de sermões". |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 4 |
| Diretorios | 2 |
| Tamanho copiado | 24,1 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `references` | 2 | 2,7 KB |
| `scripts` | 1 | 17,2 KB |

## Secoes internas detectadas

- Sermon Pipeline — Pr. Filipe Ivo Pereira
-   Configurações fixas do projeto
-   Fluxo de execução
-     1. Verificar dependências
-     2. Obter parâmetros do usuário
-     3. Executar o script principal
-     4. Após execução — atualizar Notion com novos vídeos
-     5. Apresentar relatório final
-   Modos de operação
-   Atualização manual do Notion via tool
-   Formato do resumo homilético
-   Arquivos de referência

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/sermon-pipeline--v3/references/notion_map.json` | 792 B |
| `skills/sermoes-pregacao/sermon-pipeline--v3/references/prompt_resumo.md` | 1,9 KB |
| `skills/sermoes-pregacao/sermon-pipeline--v3/scripts/sermon_pipeline.py` | 17,2 KB |
| `skills/sermoes-pregacao/sermon-pipeline--v3/SKILL.md` | 4,2 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\sermon-pipeline-skill`

## Conteudo integral do SKILL.md

````
markdown
---
name: sermon-pipeline
description: >
  Pipeline completo para pregações do Pr. Filipe Ivo Pereira: busca vídeos de uma playlist ou canal do YouTube, baixa transcrições reais, gera resumos homiléticos detalhados com Claude e atualiza automaticamente o banco de dados de pregações no Notion. Use esta skill sempre que o usuário pedir para processar pregações do YouTube, gerar resumos de sermões, atualizar o Notion com descrições de vídeos, baixar transcrições de pregações, ou qualquer variação de "processar a playlist", "resumir as pregações", "atualizar o banco de sermões".
---

# Sermon Pipeline — Pr. Filipe Ivo Pereira

Pipeline end-to-end: YouTube → Transcrições → Resumos (Claude) → Notion.

## Configurações fixas do projeto

```
Playlist principal : PL8TZC9PmmYq5_4UGM_guQm-SSXHFNwLfj
Notion Database ID : 31146d0421844d08b273b907c49a2195
Coluna de resumo   : "Resumo da Pregação" (tipo RICH_TEXT)
Idiomas preferidos : pt, pt-BR, en
Modelo de resumo   : claude-opus-4-5
```

## Fluxo de execução

Quando o usuário acionar esta skill, siga exatamente esta ordem:

### 1. Verificar dependências

```bash
pip install google-api-python-client youtube-transcript-api anthropic pandas openpyxl --quiet
```

### 2. Obter parâmetros do usuário

Pergunte (ou extraia da conversa) apenas o que estiver faltando:

| Parâmetro | Padrão / Onde encontrar |
|---|---|
| `YOUTUBE_API_KEY` | Chave já conhecida: `AIzaSyDtguB5J_9GNijAngVR7LGQ4tsPDe_ealQ` |
| `ANTHROPIC_API_KEY` | Pedir ao usuário ou ler de `~/.anthropic/key` |
| `NOTION_TOKEN` | Pedir ao usuário (integration token) |
| `PLAYLIST_ID` | Padrão acima; aceita outro se o usuário informar |
| `MODO` | `completo` (tudo), `so-resumos` (pula transcrição), `so-excel` (sem Notion) |

### 3. Executar o script principal

```bash
python /caminho/para/sermon_pipeline.py \
  --youtube-key "CHAVE" \
  --anthropic-key "CHAVE" \
  --notion-token "TOKEN" \
  --playlist-id "PLAYLIST_ID" \
  --modo "completo"
```

Leia `scripts/sermon_pipeline.py` para ver a implementação completa.

### 4. Após execução — atualizar Notion com novos vídeos

Se houver vídeos na playlist que ainda **não estão** no banco Notion, pergunte ao usuário se quer criar entradas novas. Se sim, use o mapeamento em `references/notion_map.json` e crie as páginas com a tool Notion.

### 5. Apresentar relatório final

Mostre ao usuário:
- Total de vídeos processados
- Quantos tiveram transcrição disponível
- Quantos resumos foram gerados
- Quantas páginas do Notion foram atualizadas
- Caminho dos arquivos gerados (Excel, TXT, JSON)

---

## Modos de operação

| Modo | O que faz |
|---|---|
| `completo` | Baixa vídeos → transcrições → gera resumos → atualiza Notion → salva Excel/TXT/JSON |
| `so-resumos` | Usa apenas título + descrição (sem transcrição) → gera resumos → atualiza Notion |
| `so-excel` | Só lista vídeos e salva Excel, sem Claude nem Notion |
| `novos-apenas` | Processa apenas vídeos sem resumo no Notion (compara com `references/notion_map.json`) |
| `video-unico` | Processa um único video_id informado pelo usuário |

---

## Atualização manual do Notion via tool

Se o usuário quiser atualizar o Notion diretamente (sem rodar o script), use a tool `notion-update-page` com:

```json
{
  "command": "update_properties",
  "page_id": "PAGE_ID_AQUI",
  "properties": {
    "Resumo da Pregação": "TEXTO DO RESUMO AQUI"
  }
}
```

O mapeamento completo de `video_id → page_id` está em `references/notion_map.json`.

---

## Formato do resumo homilético

Todo resumo gerado deve ter 200 a 280 palavras e incluir obrigatoriamente:

1. Tema central e propósito pastoral da mensagem
2. Texto bíblico principal com capítulo e versículo exatos
3. Estrutura dos pontos principais desenvolvidos
4. Aplicação prática concreta para os ouvintes
5. Tom e abordagem homilética usada

Escrever em português brasileiro, sem travessões, sem bullet points, em texto corrido.

---

## Arquivos de referência

- `scripts/sermon_pipeline.py` — Script Python completo, pronto para rodar
- `references/notion_map.json` — Mapeamento video_id → page_id Notion (atualize após cada sessão)
- `references/prompt_resumo.md` — Prompt completo para geração de resumos (edite para ajustar o estilo)
````
