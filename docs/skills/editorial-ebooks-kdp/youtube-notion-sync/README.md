# youtube-notion-sync

- Categoria: **Editorial, Ebooks e KDP** (`editorial-ebooks-kdp`)
- Nome declarado: `youtube-notion-sync`
- Pacote instalavel: `packages/editorial-ebooks-kdp/youtube-notion-sync.zip`
- Pasta copiada: `skills/editorial-ebooks-kdp/youtube-notion-sync`
- Fonte original: `C:\Users\filip\.codex\skills\youtube-notion-sync`
- Hash do `SKILL.md`: `495a0d497205f4d193d24186ed0b107f0b7e58560ff93fb700303640597de03d`

## Resumo

Sincroniza transcricoes do YouTube com o Notion. Use para extrair legendas de videos ou playlists, atualizar transcricoes no Notion e cadastrar novos videos automaticamente.

## Instalacao individual

```powershell
$zip = "packages/editorial-ebooks-kdp/youtube-notion-sync.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `youtube-notion-sync` |
| Skill name | `youtube-notion-sync` |
| Categoria | `editorial-ebooks-kdp` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\youtube-notion-sync` |
| Pasta no repositorio | `skills/editorial-ebooks-kdp/youtube-notion-sync` |
| Arquivo principal | `skills/editorial-ebooks-kdp/youtube-notion-sync/SKILL.md` |
| Zip | `packages/editorial-ebooks-kdp/youtube-notion-sync.zip` |
| Tamanho do zip | 8,4 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | youtube-notion-sync |
| `description` | Sincroniza transcricoes do YouTube com o Notion. Use para extrair legendas de videos ou playlists, atualizar transcricoes no Notion e cadastrar novos videos automaticamente. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 5 |
| Diretorios | 1 |
| Tamanho copiado | 20,6 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `scripts` | 3 | 18,5 KB |

## Secoes internas detectadas

- YouTube Notion Sync
-   Quando usar
-   Requisitos
-   Fluxo
-   Scripts
-   Observacoes

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/editorial-ebooks-kdp/youtube-notion-sync/README.md` | 420 B |
| `skills/editorial-ebooks-kdp/youtube-notion-sync/scripts/download_all_transcripts.py` | 6,0 KB |
| `skills/editorial-ebooks-kdp/youtube-notion-sync/scripts/fix_missing_with_cookies.py` | 7,7 KB |
| `skills/editorial-ebooks-kdp/youtube-notion-sync/scripts/sync_youtube_notion.py` | 4,8 KB |
| `skills/editorial-ebooks-kdp/youtube-notion-sync/SKILL.md` | 1,7 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\youtube-notion-sync`
- `C:\Users\filip\.agents\skills\youtube-notion-sync`
- `C:\Users\filip\.claude\skills\youtube-notion-sync`
- `C:\Users\filip\.gemini\skills\youtube-notion-sync`
- `C:\Users\filip\.windsurf\skills\youtube-notion-sync`

## Conteudo integral do SKILL.md

```
markdown
---
name: youtube-notion-sync
description: Sincroniza transcricoes do YouTube com o Notion. Use para extrair legendas de videos ou playlists, atualizar transcricoes no Notion e cadastrar novos videos automaticamente.
---

# YouTube Notion Sync

Esta skill automatiza a extracao de transcricoes do YouTube e a atualizacao de bancos de dados no Notion. Ela serve para manter um acervo de pregacoes, palestras ou aulas com titulo, link e transcricao.

## Quando usar

Use esta skill quando o usuario pedir para:

- baixar ou extrair transcricoes de videos do YouTube;
- processar playlists inteiras;
- preencher linhas sem transcricao em um banco do Notion;
- criar ou atualizar paginas de videos em um banco do Notion.

## Requisitos

- Token de integracao do Notion;
- ID do banco de dados do Notion;
- Colunas compativeis no banco, incluindo um titulo, uma URL do video e uma propriedade de arquivos para a transcricao;
- Python com dependencias como `requests` e `yt-dlp`.

## Fluxo

1. Ler o banco do Notion para localizar paginas existentes e links de video.
2. Extrair legendas do YouTube, incluindo tentativas com cookies do navegador quando necessario.
3. Limpar a transcricao para texto legivel.
4. Enviar o arquivo para o Notion e associar a pagina correspondente.

## Scripts

- `scripts/sync_youtube_notion.py`: fluxo principal de sincronizacao.
- `scripts/fix_missing_with_cookies.py`: tenta recuperar transcricoes com cookies do navegador.
- `scripts/download_all_transcripts.py`: processamento em lote.

## Observacoes

- Se um video nao tiver legenda disponivel, isso deve ser reportado claramente.
- Antes de executar em lote, confirme que as propriedades do banco do Notion correspondem ao que os scripts esperam.
```
