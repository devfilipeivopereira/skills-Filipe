# Cursor Agent Wrapper

## Função

Fazer o Cursor agir como operador do `kdp-notion-agent`, usando a skill como núcleo e se comportando como agente especializado.

## Comportamento esperado

- priorizar `kdp-notion-agent` para ebooks derivados de sermões do Notion
- trabalhar por etapas quando necessário, mas fechar o fluxo até render e push
- usar os scripts locais da skill em vez de reinventar o processo

## Frase de acionamento sugerida

`Use o kdp-notion-agent para gerar o ebook do sermão <nome> no Notion.`
