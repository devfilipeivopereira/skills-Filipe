# Slides Cinematográficos para Sermões

Skill para transformar sermões e apresentações pastorais em um planejamento visual completo: cenas fotorrealistas, texto essencial, capa marcante, prompts de imagem e notas do apresentador.

**Identificador:** `planejar-slides-cinematograficos`

O objetivo é ajudar o pregador a lembrar o próximo movimento e a plateia a compreender e reter a mensagem. O planejamento acompanha a estrutura do sermão e preserva títulos, frases centrais e textos já aprovados.

## Como usar

Em um ambiente que tenha a skill disponível, invoque-a pelo nome e forneça o sermão:

```text
Use $planejar-slides-cinematograficos para planejar 30 slides do sermão
anexo, incluindo a capa. Use imagens cinematográficas fotorrealistas,
pouco texto, prompts completos e notas para uma apresentação de 45 minutos.
```

Se a interface não reconhecer a invocação pelo nome, peça ao assistente para ler o `SKILL.md` desta pasta e seguir suas instruções. A forma de cadastrar skills depende do ambiente utilizado. Os arquivos desta pasta, por si só, não confirmam uma instalação na conta do usuário.

### Informações de entrada

O material principal pode ser um manuscrito, esboço ou texto do sermão. Referências visuais e preferências ajudam a definir o resultado.

| Informação | Como é utilizada |
|---|---|
| Sermão ou conteúdo da apresentação | Define a sequência e o significado das imagens |
| Título aprovado | É preservado e usado em caixa alta na capa |
| Passagem e tradução bíblica | Orientam cenas e citações, quando fornecidas |
| Frase central / bottom line | É mantida sem alterações nas retomadas |
| Duração e quantidade de slides | Orientam o ritmo e a divisão do conteúdo |
| Público e contexto | Ajustam linguagem, ambientes e aplicações |
| Imagens ou links de referência | Orientam composição, fotografia e tipografia quando acessíveis |

O número solicitado inclui a capa como **slide 01**. Na ausência de quantidade ou duração, a skill adota premissas e as informa. Se receber apenas tema e passagem, identifica o resultado como plano preliminar. Se faltar conteúdo suficiente, solicita o material indispensável.

### Modelo de pedido

```text
Use $planejar-slides-cinematograficos.

Título aprovado:
Texto bíblico e tradução:
Frase central aprovada:
Duração:
Quantidade total de slides, incluindo a capa:
Público:
Referência visual ou preferência de estilo:
Restrições ou elementos obrigatórios:

Sermão:
[Cole o manuscrito ou indique o arquivo anexado.]
```

Preencha somente o que já souber. O assistente não precisa interromper o planejamento para perguntar por cada campo opcional.

## O que a skill entrega

1. Síntese da mensagem e premissas adotadas.
2. Direção de arte, progressão de luz e cor e regras de continuidade.
3. Proposta de capa com título maior em caixa alta e tratamento tipográfico próprio.
4. Mapa de todos os slides, relacionado à sequência do sermão.
5. Prompt mestre com os padrões visuais da apresentação.
6. Ficha de cada slide: texto exato, cena, composição, tipografia, prompt autossuficiente e notas do apresentador.
7. Ordem sugerida de produção e critérios de revisão.

As notas incluem o momento de entrada do slide, lembretes de fala, pausas quando úteis e transição. Elas ficam separadas do conteúdo projetado.

## Padrão visual

| Aspecto | Capa | Slides internos |
|---|---|---|
| Fotografia | Cinematográfica, fotorrealista e relacionada ao tema | Mesmo universo visual, com cenas específicas para cada ideia |
| Texto | Título principal maior e integralmente em CAIXA ALTA | Uma ideia por slide, com poucas palavras |
| Tipografia | Um efeito expressivo escolhido conforme o tema | Sistema limpo, consistente e legível |
| Ênfase | Título como protagonista | Uma palavra, expressão ou declaração principal |
| Caixa alta | Obrigatória no título principal | Usada quando favorecer o destaque e a leitura |
| Composição | Pode lembrar um pôster ou capa de série | Espaço negativo, margens seguras e foco na mensagem |

O formato padrão é **16:9**, com projeto em **1920 × 1080 ou superior**. A resolução efetivamente gerada depende da ferramenta de imagem e deve ser verificada durante a produção.

O efeito de capa pode usar profundidade com personagem, recorte fotográfico, relevo discreto, escala editorial ou textura ambiental sutil. A legibilidade tem prioridade. O efeito não se espalha automaticamente pelos slides internos.

### Texto e fidelidade

- Preferir manchetes de 3–9 palavras, com flexibilidade para preservar sentido e frases aprovadas.
- Manter uma única ideia e uma ênfase dominante em cada slide.
- Preservar a frase central nas repetições.
- Distinguir citação bíblica, trecho, paráfrase e síntese do sermão.
- Não inventar tradução bíblica nem transformar paráfrases em citações literais.
- Colocar explicações e detalhes nas notas, sem sobrecarregar a tela.
- Para leituras longas, dividir por unidades de sentido em vez de reduzir excessivamente a fonte.

### Escolha das cenas

| Momento | Direção preferencial |
|---|---|
| Narração bíblica | Reconstituição plausível da época e do acontecimento |
| Aplicação ao ouvinte | Cena contemporânea, brasileira quando pertinente |
| História ou ilustração | Ação, ambiente ou objeto relacionado à história |
| Conceito abstrato | Metáfora visual simples e compreensível |

Não há proporção fixa entre cenas bíblicas e modernas. A quantidade de atos, a paleta e o arco visual mudam de acordo com a mensagem. Personagens, objetos e enquadramentos podem reaparecer para reforçar continuidade e transformação.

## Exemplos de uso

### Sermão completo

```text
Use $planejar-slides-cinematograficos para planejar 30 slides deste sermão
de 45 minutos. Preserve o título e a frase central. Inclua o texto exato
de cada imagem e as notas do apresentador. Entregue apenas o planejamento.
```

### Sermão de um ponto

```text
Use $planejar-slides-cinematograficos neste sermão de um ponto.
Mantenha a progressão do manuscrito e retome a bottom line sem alterar
sua redação. Escolha uma quantidade de slides adequada a 35 minutos.
```

### Revisão de um plano existente

```text
Use $planejar-slides-cinematograficos para revisar este planejamento.
Reduza o texto dos slides, preserve as frases aprovadas e dê à capa
um título maior em caixa alta, com profundidade tipográfica e boa leitura.
```

### Planejamento e produção de imagens

```text
Use $planejar-slides-cinematograficos para planejar 12 slides e depois
gerar as imagens uma a uma. Integre o texto exato a cada imagem.
Se a ferramenta não reproduzir a escrita corretamente, prepare a foto
sem texto e indique a aplicação tipográfica em uma camada editável.
```

Esse último pedido depende de uma ferramenta de geração de imagens disponível. A skill é um conjunto de instruções; não inclui um gerador de imagens, não fornece uma API e não monta um PPTX automaticamente. Imagens e apresentações são produzidas quando solicitadas e quando o ambiente oferece as ferramentas necessárias.

## Arquivos

| Arquivo | Finalidade |
|---|---|
| [SKILL.md](SKILL.md) | Instruções principais e fluxo de planejamento |
| [agents/openai.yaml](agents/openai.yaml) | Nome de exibição, descrição curta e exemplo de invocação |
| [references/modelo-de-plano.md](references/modelo-de-plano.md) | Estrutura de entrega e modelo de ficha por slide |
| [references/referencias-visuais.md](references/referencias-visuais.md) | Critérios de estilo, tratamentos de capa e exemplos |
| [README.md](README.md) | Documentação de uso e escopo |

Para transportar a skill, mantenha essa pasta e seus arquivos juntos. As referências são relativas ao `SKILL.md` e não devem ser separadas.

## Revisão do resultado

Antes de usar o plano, conferir:

- Total de slides correto, incluindo a capa.
- Sequência coerente com o sermão e sem antecipar suas viradas.
- Título da capa em caixa alta, maior e legível.
- Mesmo texto no mapa geral, na ficha e no prompt correspondente.
- Frases aprovadas e referências bíblicas preservadas.
- Cenas relacionadas ao conteúdo e com continuidade visual.
- Notas do apresentador separadas do texto da imagem.
- Prompts completos, sem instruções vagas como “igual ao anterior”.

Na produção, conferir também os acentos, a proporção, a resolução real, o contraste e a ausência de inscrições acidentais. Não considerar uma revisão em tela como teste de projeção no ambiente do evento.

## Referências e limites

A direção inicial foi inspirada no planejamento visual “O que a água não apaga”, fornecido pelo usuário, e em sua preferência por capas de sermões com tipografia expressiva. A skill não depende desse documento para funcionar e não transporta automaticamente seus personagens, cores ou quantidade de slides para outras mensagens.

A [busca de capas de sermões indicada no Pinterest](https://br.pinterest.com/search/pins/?q=cover%20sermons) não pôde ser inspecionada na criação. O endereço é uma referência opcional; nenhum design específico dessa página é apresentado como analisado.

As cenas bíblicas são reconstituições artísticas plausíveis, não fotografias documentais nem afirmações de certeza arqueológica. A skill preserva o conteúdo recebido e não substitui a revisão bíblica, pastoral e editorial do autor.
