---
name: notion-ebook-from-corrigido
description: Ler um banco do Notion, localizar a coluna corrigido, extrair apenas a parte da pregação, transformar esse texto em um ebook conversacional em português e gravar o resultado na coluna ebook.
---

# Notion Ebook From Corrigido

Use esta skill para processar um banco do Notion de ponta a ponta: localizar páginas pendentes, extrair o texto da coluna `Corrigido`, transformar em um ebook pastoral em português (acabamento de livro cristão) e salvar o resultado na coluna `Ebook`.

Esta skill é operacional: ela otimiza o fluxo para não gerar JSONs enormes, reaproveitar arquivos locais e garantir **10.000 palavras** com **baixa repetição** usando validação automática.

## Fluxo recomendado (prático)

1. Defina credenciais no shell atual.
2. Liste candidatas com `list` usando cache local (`--local-source-dir`) e filtro de tamanho (`--min-local-source-words`).
3. Para cada página escolhida:
   1) Gere um ebook local com `draft` (limpeza + capítulos + validação).
   2) Faça upload com `push` (valida de novo e bloqueia se falhar).

## Ordem de processamento obrigatória

Antes de corrigir o português e antes de escrever o ebook, normalize o texto bruto nesta ordem:

1. Remova quebras de linha ruins e consolide o conteúdo em blocos legíveis.
2. Remova símbolos soltos, caracteres invisíveis, tabs excessivos e ruídos de transcrição.
3. Padronize aspas, travessões, bullets e espaços.
4. Só então faça a limpeza em pt-BR e a transformação em ebook.

## Setup

Defina as variáveis de ambiente no PowerShell antes de rodar o script:

```powershell
$env:NOTION_TOKEN = 'seu_token'
$env:NOTION_DATABASE_ID = 'seu_database_id'
```

Notas:

- Não grave token em arquivos versionáveis.
- O script já força `stdout/stderr` em UTF-8 para evitar `UnicodeEncodeError` no PowerShell ao imprimir títulos com acentos.

## Comandos

Inspecionar o esquema (use apenas se houver dúvida de nomes/colunas):

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" inspect
```

Listar candidatas (sem baixar `corrigido_text`):

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" list --max-pages 10 --local-source-dir "C:\Users\filip\Downloads\notion_corrigidos" --out candidates.json
```

Listar candidatas já priorizando fontes mais fortes:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" list --max-pages 10 --min-local-source-words 6000 --local-source-dir "C:\Users\filip\Downloads\notion_corrigidos" --out candidates.json
```

Baixar apenas um resumo da fonte (sem carregar texto inteiro):

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" pull --page-id "<page_id>" --summary-only --local-source-dir "C:\Users\filip\Downloads\notion_corrigidos" --out pending-summary.json
```

## Novo: gerar ebook local automaticamente (`draft`)

Gera um `.md` com estrutura de livro cristão a partir de um `.txt` corrigido local, com:

- normalização inicial do texto bruto
- limpeza de ruídos (avisos, pedidos de like, pix, etc.)
- reconstrução de parágrafos quando o texto vem “em bloco”
- dedupe de trechos repetidos
- capítulos + pausas para prática
- validação (10.000 palavras + baixa repetição)

Exemplo:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" draft --title "Meu título" --source-file "C:\Users\filip\Downloads\notion_corrigidos\_MEU_ARQUIVO.txt" --out "ebook.md"
```

## Validar antes do upload

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" validate --input-file "ebook.md"
```

## Upload para o Notion (`push`)

Atualizar a coluna `Ebook` de uma página específica com um arquivo `.md`:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" push --page-id "<page_id>" --input-file "ebook.md"
```

O `push` roda validação por padrão. Se falhar (menos de 10.000 palavras ou repetição acima do limite), ele bloqueia o upload.

## Regras de escrita

Leia [references/ebook-format.md](references/ebook-format.md) antes de redigir ou ajustar ebooks.

Mesmo usando `draft`, revise rapidamente o resultado quando o objetivo for publicação (KDP/ebook final), para garantir:

- fidelidade ao conteúdo
- progressão real do argumento
- linguagem pastoral e bíblica
- fechamento forte

## Heurística para separar a pregação

Comece procurando o trecho em que a mensagem bíblica realmente começa. Sinais comuns:

- leitura do texto bíblico
- frase como “abra sua Bíblia”, “vamos ler”, “a mensagem de hoje”
- início claro de exposição, argumento ou aplicação

Pare de considerar material útil quando o texto migrar para:

- avisos da igreja
- pedido de inscrição no canal
- ofertas, PIX, agenda, recados
- despedida técnica, créditos, equipe, anúncios
