# Planejar slides cinematográficos

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `planejar-slides-cinematograficos`
- [Arquivo principal](../../../../skills/sermoes-pregacao/planejar-slides-cinematograficos/SKILL.md)
- [Pacote instalável](../../../../packages/sermoes-pregacao/planejar-slides-cinematograficos.zip)
- [README da skill](../../../../skills/sermoes-pregacao/planejar-slides-cinematograficos/README.md)
- Fonte original: Claude skills sincronizadas (`anthropic-skills:planejar-slides-cinematograficos`)
- SHA-256 do `SKILL.md`: `f04d069a99e63b3d489f117160c2e5b8bf9317f8d1c8ea363dad42edf455e793`

## Resumo

Planejar imagens e slides de sermões, mensagens bíblicas e apresentações pastorais com fotografia cinematográfica realista, pouco texto, capa em caixa alta com tipografia diferenciada, prompts completos e notas do apresentador. Usar quando o usuário pedir planejamento visual, roteiro de slides, storyboard, imagens para uma pregação ou uma apresentação no estilo de capas de sermões. Adaptar a sermões de um ponto e a outras estruturas, preservando a mensagem e a frase central.

## Uso

> Use $planejar-slides-cinematograficos para planejar os slides deste sermão, com capa em caixa alta e prompts de imagem.

## Instalação individual

Extraia o ZIP na pasta de skills, preservando a pasta `planejar-slides-cinematograficos`. No Codex, por padrão: `~/.codex/skills`, ou `$CODEX_HOME/skills` quando configurado.

## Arquivos do pacote

| Arquivo | Bytes |
|---|---:|
| `README.md` | 9516 |
| `SKILL.md` | 12759 |
| `agents/openai.yaml` | 337 |
| `references/modelo-de-plano.md` | 4583 |
| `references/referencias-visuais.md` | 4495 |

## Conteúdo integral do SKILL.md

````markdown
---
name: planejar-slides-cinematograficos
description: Planejar imagens e slides de sermões, mensagens bíblicas e apresentações pastorais com fotografia cinematográfica realista, pouco texto, capa em caixa alta com tipografia diferenciada, prompts completos e notas do apresentador. Usar quando o usuário pedir planejamento visual, roteiro de slides, storyboard, imagens para uma pregação ou uma apresentação no estilo de capas de sermões. Adaptar a sermões de um ponto e a outras estruturas, preservando a mensagem e a frase central.
---

# Planejar slides cinematográficos

Transformar o sermão em uma experiência visual que ajude o pregador a lembrar o próximo movimento e a plateia a compreender e reter a mensagem. Fazer cada slide funcionar como uma pista visual, sem transformá-lo em manuscrito projetado.

## 1. Ler e definir o escopo

- Ler o sermão e as referências visuais disponíveis antes de planejar. Quando o material estiver em um arquivo conhecido, ler sua versão atual; não reconstruí-lo de memória.
- Priorizar instruções atuais do usuário, depois o sermão e textos aprovados, depois referências visuais e os padrões desta skill.
- Extrair: título, passagem, frase central ou bottom line, sequência do argumento, histórias, tensão, virada, aplicações e conclusão. Preservar a estrutura existente; não forçar todo sermão a um método único.
- Usar o português do Brasil. Preservar frases aprovadas, mesmo quando ultrapassem as metas de concisão.
- Se não houver sermão nem conteúdo suficiente, solicitar o material indispensável. Se houver apenas tema e passagem, produzir um plano preliminar claramente identificado; não fingir que deriva de um manuscrito.
- Não bloquear o trabalho por duração, quantidade ou paleta ausentes. Escolher e declarar brevemente premissas razoáveis. Manter o número exato de slides quando informado, incluindo a capa como slide 01.
- Sem quantidade definida, escolher a partir das mudanças reais de ideia: como referência ajustável, 12–18 slides para 20–30 minutos, 20–30 para 40–50 minutos e 28–40 para cerca de 60 minutos. Evitar preencher uma cota com repetições.
- Adotar 16:9 horizontal, projeto em 1920 × 1080 ou superior, salvo orientação diferente.
- Entregar planejamento. Gerar imagens ou montar PPTX somente quando a solicitação também incluir essa produção; nesse caso prosseguir no escopo já autorizado, sem nova confirmação obrigatória.

## 2. Construir o percurso visual

- Mapear os movimentos do sermão antes de escrever prompts. Cobrir as ideias essenciais na mesma ordem, sem revelar uma virada antes da fala.
- Relacionar cada imagem a um trecho, uma ideia ou uma ação concreta do sermão. Evitar fotografias bonitas que não ajudam a lembrar a mensagem.
- Escolher o tipo de cena pela função:

| Conteúdo | Cena preferencial |
|---|---|
| Narração ou leitura sobre personagens e acontecimentos bíblicos | Reconstituição bíblica plausível |
| Aplicação ao ouvinte, pergunta, dilema ou oração | Vida contemporânea, em contexto brasileiro quando pertinente |
| História ou ilustração específica | Local, objeto e ação correspondentes à história |
| Conceito abstrato ou transição | Metáfora visual simples, compreensível e ligada ao argumento |

- Não impor uma proporção fixa entre cenas bíblicas e modernas. Não inventar episódios, evidências históricas ou falas para tornar a imagem dramática.
- Planejar um arco de luz e cor que acompanhe a mensagem. Usar a passagem do frio ao quente apenas quando fizer sentido; não transformar todo sermão em tempestade seguida de amanhecer.
- Variar planos gerais, médios e detalhes, posição do assunto e profundidade. Manter coerência de fotografia e tipografia. Repetir um enquadramento quando o retorno mostrar transformação ou reforçar o refrão.
- Definir fichas textuais curtas para personagens, objetos e cenários recorrentes. Manter aparência, roupa, proporções e época. Planejar referências visuais apenas quando úteis; não gerar fichas automaticamente.
- Não transportar Noé, arca, personagens, paleta ou número de slides do exemplo para sermões de outros temas.

## 3. Reduzir o texto sem perder a mensagem

- Trabalhar uma ideia principal por slide.
- Preferir 3–9 palavras na manchete; aceitar até cerca de 12 quando necessário. Tratar isso como meta editorial, não motivo para mutilar frases aprovadas ou citações.
- Reservar a tela para frase central, pergunta decisiva, contraste, palavra-chave, ação ou trecho bíblico indispensável. Colocar explicações, histórias completas e detalhes nas notas.
- Usar CAIXA ALTA nos pontos principais quando aumentar a força e a leitura: uma palavra, uma expressão ou uma declaração curta. Usar caixa normal para apoio. Não aplicar caixa alta indiscriminadamente.
- Definir exatamente acentos, pontuação e quebras de linha. Mostrar o texto final em bloco próprio; não deixar alternativas dentro do prompt de produção.
- Usar uma única ênfase dominante por slide, por peso, escala ou cor. Evitar destacar todas as palavras.
- Preservar a redação da tradução bíblica fornecida. Distinguir citação literal, trecho e paráfrase. Não colocar aspas de citação em texto adaptado nem atribuir uma paráfrase como versículo literal.
- Para leituras longas, dividir por unidades de sentido. Aceitar excepcionalmente 18–35 palavras por slide de leitura, desde que legível; nunca reduzir muito a fonte para encaixar tudo.
- Manter a frase central idêntica nas retomadas. Repeti-la em momentos estratégicos, sem inventar variações silenciosamente.
- Permitir um slide sem texto apenas se a pausa ou a imagem tiver função clara. Identificar explicitamente “SEM TEXTO”.

## 4. Dar tratamento próprio à capa

O slide 01 deve parecer a capa de uma série de sermões ou um pôster cinematográfico, distinguindo-se dos slides internos.

- Usar o título principal MAIOR e INTEGRALMENTE EM CAIXA ALTA. Manter título aprovado, acentos e palavras essenciais.
- Tornar o título protagonista, com 2–4 linhas bem compostas quando necessário; admitir uma linha para títulos curtos.
- Usar somente título e, se pertinente, referência bíblica ou nome da série em escala secundária. Incluir pregador, igreja e data apenas se pedidos ou fornecidos como necessários.
- Escolher UM efeito tipográfico autoral que combine com o tema: profundidade por sobreposição com o personagem, recorte revelando a fotografia, relevo discreto com luz coerente, deslocamento controlado, textura sutil do ambiente ou escala editorial expressiva.
- Evitar brilho gratuito, néon, excesso de efeitos, deformação, letras ilegíveis e aparência de template genérico. Fotografias devem continuar realistas mesmo com tipografia expressiva.
- Permitir letras atrás de elementos da cena apenas se o título continuar totalmente reconhecível. Não encobrir partes críticas de palavras.
- Apresentar uma direção recomendada de capa e, brevemente, até duas alternativas conceituais. Desenvolver o prompt completo da recomendada sem exigir escolha prévia. Se o usuário pedir uma única proposta, entregar só ela.
- Consultar [referencias-visuais.md](references/referencias-visuais.md) para tratamentos e critérios. Ao receber um link visual, tentar inspecioná-lo; se inacessível, informar a limitação sem atribuir ao link características não observadas. Prosseguir com a descrição disponível.

## 5. Definir fotografia e legibilidade

- Fazer cada slide parecer um frame de cinema: pele, tecido, madeira, pedra e água com textura física; luz com origem plausível; interpretação natural; profundidade e cores controladas.
- Usar imagem de página inteira, sem bordas ou barras de cinema. Evitar pintura, aquarela, ilustração, desenho, render 3D, CGI aparente, pele plástica, HDR excessivo e poses de banco de imagens.
- Para cenas bíblicas, respeitar a época e a geografia de modo plausível; não apresentar escolha artística como certeza arqueológica. Evitar anacronismos, fantasia e símbolos não pedidos.
- Reservar espaço negativo para o texto ao compor a cena. Separar o assunto principal do bloco de leitura; não escrever sobre rostos ou detalhes essenciais.
- Usar margens seguras de aproximadamente 7–8%, inclusive no rodapé. Admitir blocos laterais e centralizados conforme a cena; não impor sempre o mesmo lado.
- Nos slides internos, adotar uma família tipográfica limpa, com dois ou três pesos e bom contraste. Evitar pesos muito finos para projeção. Usar uma fonte expressiva adicional na capa se necessário.
- Em 1920 × 1080, considerar como ponto de partida manchetes internas de 80–130 px, título de capa de 140–220 px e referências de 32–44 px. Adaptar ao tamanho real das palavras, sem confundir px de imagem com pt do PowerPoint.
- Definir paleta e um pequeno conjunto de layouts: declaração, pergunta/contraste, trecho bíblico, número ou palavra, refrão. Fazer a capa pertencer à mesma série sem copiar o layout interno.
- Preferir contraste natural e composição limpa. Usar sombra discreta ou ajuste local de luminosidade somente se indispensável; evitar tarjas, caixas e degradês pesados como solução padrão.
- Não usar logos, marcas-d'água ou inscrições acidentais. Só incluir marcas e nomes pedidos.

## 6. Entregar um plano completo e executável

Ler [modelo-de-plano.md](references/modelo-de-plano.md) e preencher seu formato adaptável.

Entregar, nesta ordem:

1. **Síntese:** título, passagem, frase central, público quando conhecido, duração informada ou estimada, quantidade, formato e premissas.
2. **Direção visual:** conceito, arco de cor/luz, padrões tipográficos, fichas de continuidade necessárias e proposta de capa.
3. **Mapa geral:** número, momento/trecho do sermão, função, tipo de cena e texto exato na tela.
4. **Prompt mestre:** padrões reutilizáveis de fotografia, continuidade e tipografia, diferenciando capa e slides internos.
5. **Fichas de todos os slides:** texto final, cena/composição, tratamento tipográfico, prompt pronto e notas do apresentador.
6. **Ordem de produção e revisão:** quais referências reutilizar, quais slides calibram o estilo e como verificar o resultado.

- Dar a cada slide um gatilho de entrada ligado ao sermão e notas concisas: intenção, 2–4 lembretes de fala, pausa quando útil e transição. Não inventar citações do manuscrito; identificar gatilho aproximado quando não for literal.
- Manter notas e instruções técnicas fora do texto projetado. Não antecipar a resposta de uma história ou pergunta.
- Escrever cada prompt de forma autossuficiente: formato, cena, ação, época, enquadramento, luz, paleta, espaço vazio, tipografia, texto exato e restrições pertinentes. Repetir os parâmetros críticos; não usar apenas “igual ao anterior”.
- Quando houver imagem de referência efetivamente disponível, identificá-la e explicar sua função. Não alegar referência “aprovada” que nunca foi aprovada.
- No prompt de imagem final, incluir o TEXTO EXATO do slide, com quebras de linha. Por padrão, planejar fotografia e texto integrados na mesma imagem.
- Oferecer como alternativa de acabamento a fotografia sem texto com espaço reservado e aplicação tipográfica em editor. Usar essa alternativa se a ferramenta falhar na escrita, sem tratá-la como requisito para começar.
- Se o pedido incluir produção de imagens, usar a ferramenta de geração disponível e verificar proporção e resolução reais. Não prometer tamanho, modelo ou fidelidade que a ferramenta não confirme.
- Entregar o plano inteiro. Não parar depois da capa ou de uma amostra pedindo “posso continuar?”. Para planos extensos, fornecer um arquivo Markdown completo e um resumo na conversa, observando as regras de salvamento do ambiente.

## 7. Revisar antes de entregar

Conferir:

- Número total correto; capa no slide 01; nenhuma numeração ausente.
- Todas as ideias essenciais representadas, na ordem do sermão.
- Capa com título maior em caixa alta e efeito tipográfico especificado.
- Texto curto, legível e idêntico no mapa, na ficha e no prompt.
- Referências e citações fiéis; paráfrases sinalizadas; frases aprovadas preservadas.
- Cenas relacionadas à fala; variedade sem perda de continuidade.
- Notas úteis ao apresentador e ausentes da imagem.
- Prompts completos, sem placeholders pendentes, salvo espaços deliberados de participação.
- Nenhuma afirmação de imagem gerada, referência vista, arquivo salvo ou apresentação testada sem que isso tenha ocorrido.

Corrigir problemas antes de apresentar o resultado.
````
