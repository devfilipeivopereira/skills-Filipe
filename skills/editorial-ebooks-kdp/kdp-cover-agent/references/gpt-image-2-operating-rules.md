# GPT Image 2 Operating Rules

Resumo operacional da documentacao enviada para esta skill.

## Modo desta skill

- a skill nao usa OpenAI API
- a geracao acontece na conversa, com a ferramenta de imagem do ambiente
- o fluxo deve imitar o contrato operacional de `gpt-image-2`

## Regras obrigatorias

- use geracao conversacional e iterativa
- primeiro gere uma arte-base
- depois refine na mesma conversa quando necessario
- nunca dependa do modelo para renderizar titulo, subtitulo ou autor
- texto final da capa e aplicado localmente

## Tamanho e saida

- usar tamanho valido `1536x2208`
- ambas as bordas precisam ser multiplas de `16`
- manter orientacao vertical
- usar JPEG final
- manter arquivo final com ate `5 MB`
- fundo deve ser opaco

## O que nao pedir ao modelo

- fundo transparente
- composicoes que dependam de texto pequeno
- layouts com posicionamento milimetrico de letras
- capas cujo entendimento dependa de microdetalhes

## Limites que mudam o workflow

- renderizacao de texto ainda pode falhar
- consistencia e posicionamento exato podem variar
- por isso a skill separa:
  - geracao de arte na conversa
  - composicao tipografica local no import

## Multi-turn

Quando a primeira imagem nao estiver boa:

- reuse a imagem gerada na propria conversa
- peca mudancas incrementais, nao rebriefing completo
- preserve foco visual, paleta e atmosfera sempre que eles ja estiverem bons
