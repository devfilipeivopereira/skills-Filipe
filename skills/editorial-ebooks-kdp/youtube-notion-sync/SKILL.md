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
