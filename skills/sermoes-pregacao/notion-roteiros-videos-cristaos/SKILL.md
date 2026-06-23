---
name: notion-roteiros-videos-cristaos
description: Use when the user wants to generate and insert five Christian short-video script ideas into the `🎬 Roteiros de Vídeo` Notion database, especially practical day-to-day themes for Christian leaders or members with `Tema`, `Tags`, `Texto bíblico`, `Ganchos`, `Conteúdo`, and `CTAs`.
---

# Notion Roteiros Videos Cristaos

## Overview

Usar esta skill para alimentar o banco `🎬 Roteiros de Vídeo` do Notion com lotes de `5` roteiros prontos para vídeo curto cristão.

Tratar cada lote como `5` novas páginas no banco, com `1` roteiro por linha e foco em dores práticas do dia a dia do líder cristão, do membro cristão ou de um cenário misto entre ambos.

## Banco Alvo

Usar este banco como destino padrão:

- database URL: `https://www.notion.so/c03bb992a72740dfbbfc8cfa420c96df`
- data source: `collection://d6f033d4-9a3b-4acd-9b53-de1f1a4881bd`
- view principal: `view://355bef33-1e9e-41a8-8bf1-25e24fc552e3`

Confirmar o schema com `notion_fetch` antes de escrever. No momento, as colunas esperadas são:

- `Tema`
- `Tags`
- `Texto bíblico`
- `Ganchos`
- `Conteúdo`
- `CTAs`

Se qualquer uma dessas propriedades estiver ausente, renomeada ou com uso incompatível, parar e avisar o usuário antes de criar páginas.

## Workflow

1. Fazer `notion_fetch` no banco para confirmar que o destino continua sendo `🎬 Roteiros de Vídeo`.
2. Ler [references/output-contract.md](references/output-contract.md) antes de redigir o lote.
3. Gerar `5` ideias distintas.
4. Criar `5` páginas com `notion_create_pages`, usando `data_source_id = d6f033d4-9a3b-4acd-9b53-de1f1a4881bd`.
5. Preencher cada página com `Tema`, `Tags`, `Texto bíblico`, `Ganchos`, `Conteúdo` e `CTAs`.
6. Responder ao usuário com um resumo curto dos `5` temas criados e citar qualquer suposição feita.

## Regras Do Lote

Manter o lote diverso e útil:

- Produzir exatamente `5` roteiros por execução, salvo pedido explícito diferente do usuário.
- Criar `1` roteiro por página do Notion.
- Priorizar problemas concretos do cotidiano cristão, não temas abstratos demais.
- Misturar, por padrão, `2` roteiros para liderança cristã, `2` para membro cristão e `1` híbrido.
- Variar dores, cenários e passagens bíblicas dentro do mesmo lote.
- Evitar repetir a mesma ideia com título reescrito.

## Regras Editoriais

Escrever sempre em `pt-BR`, com tom pastoral, direto, bíblico e aplicável.

Seguir estas diretrizes:

- Preferir temas específicos como cansaço, desânimo, disciplina, oração, caráter, serviço, família, igreja local, trabalho, finanças, pureza, conflitos, influência e constância espiritual.
- Evitar títulos genéricos como `fé`, `oração` ou `chamado` sem um conflito concreto.
- Preencher `Tags` com palavras únicas, em minúsculas, separadas por vírgulas.
- Usar normalmente entre `4` e `6` tags por roteiro.
- Fazer as tags classificarem assunto, dor, contexto ou ênfase espiritual do vídeo.
- Evitar tags com espaço; preferir `vida`, `familia`, `lideranca`, `cansaco`, `graca`, `perdao`.
- Usar normalmente `1` versículo principal em `Texto bíblico`; usar mais de um só quando realmente necessário.
- Fazer o `Conteúdo` soar como roteiro pronto para gravação de aproximadamente `90` segundos.
- Manter interpretação bíblica segura e fiel ao texto.
- Fechar cada roteiro com aplicação prática e chamada de ação útil para engajamento.

## Quando O Pedido Vier Vago

Se o usuário disser apenas algo como:

- `gere ideias para meus roteiros`
- `alimente meu banco do notion`
- `crie cinco roteiros cristãos`

Assumir o padrão desta skill:

- banco `🎬 Roteiros de Vídeo`
- `5` novas páginas
- foco no dia a dia do líder cristão ou membro cristão
- `1` versículo principal por roteiro
- `4` a `6` tags de uma palavra por roteiro
- `7` ganchos
- `1` conteúdo de `90` segundos
- `7` CTAs

## Falhas E Segurança

- Não afirmar sucesso se a criação das páginas falhar.
- Se a escrita no Notion falhar parcialmente, informar quantas páginas foram criadas e quais temas ficaram pendentes.
- Não mudar de banco automaticamente.
- Não inventar colunas fora do schema confirmado.
