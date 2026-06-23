# Contrato de Saida

## Estrutura de cada pagina

Cada pagina criada no Notion representa `1` roteiro completo.

Preencher as propriedades assim:

- `Tema`: titulo curto, especifico e publicavel
- `Tags`: lista curta de tags em minusculas, separadas por virgulas, com uma palavra por tag
- `Texto bíblico`: referencia principal e pequeno trecho do versiculo
- `Ganchos`: `7` linhas numeradas
- `Conteúdo`: roteiro pronto para video curto de cerca de `90` segundos
- `CTAs`: `7` linhas numeradas

## Formato recomendado

### Tema

Usar uma frase curta e clara.

Exemplos de formato:

- `Quando o lider cuida de todos, mas nao cuida da propria alma`
- `Como vencer a culpa de nunca fazer o suficiente para Deus`
- `O perigo de servir na igreja sem permanecer em Jesus`

### Texto bíblico

Preferir `1` versiculo principal no formato:

`Livro capitulo:versiculo - "trecho curto do versiculo"`

Exemplo:

`Provérbios 4:23 - "Acima de tudo, guarde o seu coração..."`

### Tags

Usar normalmente entre `4` e `6` tags.

Regras:

- cada tag deve ser uma palavra
- escrever em minusculas
- separar por virgulas
- misturar classificacao de assunto, dor, contexto e resposta espiritual
- evitar frases, hashtags e tags redundantes

Exemplo:

`lideranca, cansaco, coracao, ministerio, secreto`

## Ganchos

Escrever exatamente `7` ganchos, um por linha, numerados de `1.` a `7.`.

Regras:

- Abrir curiosidade, dor, confronto ou identificação.
- Variar entre pergunta, afirmação forte, contraste, alerta e promessa.
- Evitar repetir a mesma estrutura nas sete linhas.
- Fazer o gancho funcionar sozinho como abertura de reels, shorts ou story em vídeo.

Exemplo:

```text
1. Tem gente servindo tanto na igreja que já nem percebe quando secou por dentro.
2. Nem todo cansaço é falta de descanso; às vezes é distância de Deus.
3. Você pode estar fazendo a obra de Deus e ainda assim negligenciando a presença de Deus.
4. O ativismo espiritual pode parecer zelo e ainda ser um sinal de alerta.
5. Quem cuida de todos também precisa vigiar o próprio coração.
6. O problema não é servir muito; é servir vazio.
7. Há líderes cercados de gente, mas internamente isolados de Deus.
```

## Conteudo

Escrever um texto pronto para gravação em cerca de `90` segundos.

Metas:

- Aproximadamente `170` a `240` palavras.
- Soar natural em voz alta.
- Conter abertura, tensão, verdade bíblica, aplicação e fechamento.
- Ficar prático para o dia a dia.

Formato recomendado:

```text
Abertura: ...

Desenvolvimento: ...

Fechamento: ...
```

Ou, se ficar melhor, usar texto corrido desde que a progressão continue clara.

## CTAs

Escrever exatamente `7` CTAs, um por linha, numerados de `1.` a `7.`.

Regras:

- Misturar comentário, compartilhamento, salvamento, oração, reflexão e engajamento.
- Manter coerência com o tema do roteiro.
- Evitar CTAs genéricos demais como sete variações de `comente amém`.

Exemplo:

```text
1. Comente "eu preciso voltar ao secreto" se essa mensagem falou com você.
2. Envie este vídeo para um líder que está precisando respirar em Deus.
3. Salve este roteiro para lembrar que servir não substitui permanecer.
4. Escreva nos comentários qual área da sua vida espiritual mais precisa de cuidado hoje.
5. Compartilhe com alguém que está cansado de carregar tudo sozinho.
6. Tire cinco minutos hoje e ore usando esse versículo.
7. Se essa verdade te confrontou, volte aqui depois do culto e me conte o que Deus tratou no seu coração.
```

## Matriz de diversidade para cada lote

Ao montar `5` roteiros, variar entre:

- liderança
- membresia
- vida devocional
- família
- igreja local
- trabalho e testemunho
- cansaço emocional
- pecado oculto
- constância espiritual
- discernimento

Evitar:

- `5` títulos com o mesmo conflito
- `5` versículos do mesmo bloco temático
- `5` roteiros com a mesma promessa rasa

## Modelo de payload

Usar o parent fixo:

```json
{
  "data_source_id": "d6f033d4-9a3b-4acd-9b53-de1f1a4881bd"
}
```

Cada page deve seguir este formato:

```json
{
  "properties": {
    "Tema": "Quando o líder cuida de todos, mas não cuida da própria alma",
    "Tags": "lideranca, coracao, ministerio, secreto, cuidado",
    "Texto bíblico": "Provérbios 4:23 - \"Acima de tudo, guarde o seu coração...\"",
    "Ganchos": "1. ...\n2. ...\n3. ...\n4. ...\n5. ...\n6. ...\n7. ...",
    "Conteúdo": "Abertura: ...\n\nDesenvolvimento: ...\n\nFechamento: ...",
    "CTAs": "1. ...\n2. ...\n3. ...\n4. ...\n5. ...\n6. ...\n7. ..."
  }
}
```
