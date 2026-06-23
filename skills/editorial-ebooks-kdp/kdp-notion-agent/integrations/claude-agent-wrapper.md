# Claude Agent Wrapper

## Função

Fazer o Claude usar `kdp-notion-agent` como agente dedicado para:

- ler sermões no Notion
- gerar `Corrigido`
- estruturar ebook
- redigir ebook
- gerar artefatos
- renderizar DOCX
- publicar no Notion

## Comportamento esperado

- tratar `kdp-notion-agent` como fluxo principal para pedidos de ebook via Notion
- preferir busca por título do sermão no Notion quando o usuário não fornecer `page_id`
- executar o pipeline completo sem parar no meio
- seguir o padrão fixo do DOCX, CTA, links e `Sobre o Autor`

## Frase de acionamento sugerida

`Use a skill kdp-notion-agent e gere o ebook do sermão <nome> no Notion.`
