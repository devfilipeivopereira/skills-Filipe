# Guia de Estilo Obrigatorio - Generate Persuasive Ebooks

Este arquivo define o contrato editorial que o `kdp-notion-agent` deve seguir
ao transformar sermoes em ebooks. O objetivo nao e apenas produzir um bom ebook
cristao, mas reproduzir a logica, a cadencia, a arquitetura e a voz editorial
da skill `generate-persuasive-ebooks`, especialmente no padrao dos modelos
aprovados pelo usuario.

## Regra mestra

Quando o `kdp-notion-agent` estiver escrevendo o ebook principal, deve:

- tratar a skill `generate-persuasive-ebooks` como padrao editorial canonico
- tratar os modelos cristaos aprovados pelo usuario como referencia de forma,
  tom, estrutura, ritmo e logica de progressao
- preservar a fidelidade ao sermao sem abrir mao da engenharia persuasiva da
  skill de referencia

Em caso de conflito:

1. fidelidade biblica e ao sermao
2. arquitetura e voz da `generate-persuasive-ebooks`
3. preferencias cosmeticas secundarias

## O que precisa ser herdado da skill de referencia

### 1. Arquitetura global do ebook

O livro deve operar como jornada unica:

- hook: reconhecimento imediato da dor ou conflito do leitor
- tensao: aprofundamento do custo invisivel e quebra de crencas
- revelacao: nova lente biblica e psicologica para interpretar o problema
- transformacao: caminho pratico, acessivel e pastoral para uma nova forma de viver

### 2. Estrutura preferencial para ebooks cristaos longos

Salvo impedimento real do sermao, o padrao preferencial e:

- titulo forte e memoravel
- subtitulo no espirito de `Um guia biblico e pratico para...`
- introducao confessional/pastoral
- 8 capitulos
- capitulo 5 com a logica `O que a Biblia realmente diz sobre...`
- um capitulo dedicado a crencas erradas, mentiras aprendidas ou erro de abordagem
- um capitulo com framework pratico numerado
- capitulo 7 com aplicacao diferenciada para membros, lideres e pastores
- fechamento pastoral com esperanca, graca e proposta concreta de pratica
- secao `Sobre o Autor`

Se o sermao nao sustentar exatamente oito capitulos, o agente pode ajustar. Mas
qualquer desvio precisa ser justificado no blueprint e no relatorio editorial.

### 2.1 Arquitetura fixa por capitulo

Quando o sermao sustentar oito capitulos, o agente deve usar esta funcao fixa:

- Capitulo 1: identificacao profunda + dor latente + loop mental aberto
- Capitulo 2: causa raiz + quebra de crencas + momento AHA
- Capitulo 3: virada cognitiva + reposicionamento de identidade + acao inicial
- Capitulo 4: aprofundamento biblico e emocional da nova lente
- Capitulo 5: `O que a Biblia realmente diz sobre...`
- Capitulo 6: framework pratico numerado
- Capitulo 7: aplicacao para membros, lideres e pastores
- Capitulo 8: custo de continuar igual + convite implicito a agir + fechamento pastoral

Cada capitulo precisa nascer com funcao estrategica. Nao basta ser "mais um subtema".

### 2.2 Template obrigatorio de blueprint

O `04_blueprint_ebook.md` deve descrever por capitulo:

- objetivo neuroemocional
- crenca ou leitura defeituosa a quebrar
- dor latente a amplificar
- nova identidade, lente ou modelo mental a propor
- ancora biblica
- trecho do sermao que ancora
- ganho do leitor ao final
- transicao para o proximo capitulo

Campos adicionais obrigatorios:

- Capitulo 2: analogia principal
- Capitulo 6: passos numerados
- Capitulo 7: aplicacao separada para membros, lideres e pastores
- Capitulo 8: custo invisivel de continuar igual e chamada implicita

### 3. Forma de abrir capitulos

E obrigatorio comecar com reconhecimento e nao com abstracao. A abertura deve
usar uma destas entradas:

- cena cotidiana reconhecivel
- pergunta desconfortavel que o leitor ja carrega
- tensao existencial nomeada com precisao
- imagem biblica ou humana forte

E proibido abrir com:

- definicao de dicionario
- explicacao conceitual fria
- contexto historico generico
- estatistica decorativa
- frase pronta de autoajuda

### 4. Forma de desenvolver

Cada capitulo deve seguir esta dinamica:

- nomear a dor ou confusao do leitor com precisao cirurgica
- mostrar o custo silencioso de permanecer no mesmo padrao
- desmontar pelo menos uma crenca equivocada
- apresentar uma nova perspectiva que faca o leitor pensar `agora isso faz sentido`
- integrar Biblia, psicologia e aplicacao real sem academicismo
- terminar com loop aberto, pergunta carregavel ou ponte forte para o proximo capitulo

### 4.1 Engenharia neuroemocional obrigatoria

Durante toda a escrita, o agente precisa ativar simultaneamente:

- reptiliano: seguranca vs risco, ganho vs perda, urgencia implicita, status ou consequencia
- limbico: historias plausiveis, conflito interno, pertencimento, frustracao silenciosa, alivio e esperanca
- neocortex: explicacao clara, estrutura organizada, causa -> efeito -> solucao, linguagem racional depois do impacto emocional

O objetivo nao e manipular. E construir um argumento que o leitor sinta, entenda e aceite.

### 5. Voz e tom

A voz esperada combina ao mesmo tempo:

- pastoral
- didatica
- psicologica
- confessional
- estrategicamente persuasiva

O texto precisa:

- validar a dor antes de corrigir a interpretacao
- trocar culpa por diagnostico
- trocar simplificacao por precisao
- usar segunda pessoa com frequencia
- soar caloroso, firme e inteligente
- conduzir o leitor a uma conclusao, sem parecer propaganda

### 6. Ritmo frasal

O texto deve reproduzir o contraste recorrente dos modelos:

- paragrafos fluidos de livro, nao blocos esquematicos
- frases curtas para impacto e definicao
- repeticao deliberada quando isso reforcar a tese
- cada paragrafo precisa ganhar o direito ao proximo

### 7. Integracao entre Biblia e psicologia

O padrao nao e teologia abstrata nem autoajuda espiritualizada. O ebook precisa:

- fazer a Biblia estruturar o argumento
- usar psicologia e ciencia para clarificar mecanismos humanos
- evitar jargao tecnico sem traducao
- evitar empilhar versiculos sem desenvolvimento
- explicar o texto biblico de modo pastoral e acessivel

### 8. Titulos e subtitulos

Favorecer padroes como:

- `A [coisa ruim] que voce nao precisa carregar`
- `A [coisa boa] que voce ainda nao teve`
- `O [recurso] que voce tem e o suficiente`
- `Voce e o que voce [verbo de habito]`
- `Voce nao e o que voce sente`

Subtitulo preferencial:

- `Um guia biblico e pratico para...`

Regra adicional obrigatoria:

- usar `references/title-positioning-playbook.md` para auditar forca comercial, formato e risco de genericidade
- preferir titulo principal com `1 a 7 palavras`
- nao usar `:` no titulo principal
- evitar no titulo principal formulas genericas como `guia`, `manual`, `introducao`, `estudo` e `reflexoes`

### 9. Reposicionamento de identidade

O leitor nao deve sair apenas instruido. Deve sair reposicionado.

### 10. Fechamento

O ultimo capitulo deve:

- fechar os loops abertos
- mostrar o custo real de continuar igual
- oferecer uma proposta pratica, simples e executavel
- terminar com esperanca pastoral, nao com pressao comercial

## Guardrails de conformidade

O ebook esta fora do padrao se:

- soar como sermao transcrito em vez de livro arquitetado
- soar como devocional generico que poderia ser escrito por qualquer autor
- perder a cadencia dor -> diagnostico -> revelacao -> pratica -> esperanca
- usar Biblia apenas como ornamento
- usar psicologia como verniz superficial
- abandonar o padrao estrutural e tonal dos modelos sem justificativa clara

## Como conciliar isso com a fidelidade ao sermao

O sermao continua sendo a fonte. A skill de referencia define a forma.

Portanto:

- o sermao define tese, imagens, limites e eixo biblico
- a `generate-persuasive-ebooks` define arquitetura, voz, progressao e logica editorial
- o `kdp-notion-agent` deve fundir os dois sem denunciar a origem transcrita
