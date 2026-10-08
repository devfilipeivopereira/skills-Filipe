# Fontes, rastreabilidade e limites de atribuição

Use ao conferir uma regra, explicar uma exceção ou revisar a fidelidade desta skill ao material fornecido.

## 1. Fontes primárias usadas

### Stanley e Jones

- **Obra:** *Communicating for a Change: Seven Keys to Irresistible Communication*.
- **Autores:** Andy Stanley e Lane Jones. O expediente registra Andy Stanley e Ronald Lane Jones; a folha de rosto exibe Andy Stanley e Lane Jones.
- **Editora:** Multnomah Books.
- **Copyright da obra:** 2006, conforme o expediente.
- **Metadado de data do EPUB:** 2008-08-19. Não confundir com o copyright.
- **eISBN:** 978-1-60142-214-9; ISBN impresso no expediente: 978-1-59052-514-2.
- **Arquivo lido:** `Communicating for a Change_ Seven Keys to Irresistible Communication.epub`.
- **Local original:** `C:/DEV/SERMÃO 1 PONTO - ANDY/Communicating for a Change_ Seven Keys to Irresistible Communication.epub`.
- **SHA-256:** `020ae42372c5f7c16b2c811f8ec57f2133d4507ec2b0ece039d3457f84cdc098`.
- **Conferência inicial:** 7 de outubro de 2026.

O campo `dc:creator` desse EPUB lista somente Andy, mas a folha de rosto, a introdução e o expediente confirmam a coautoria. A introdução atribui a parábola a Lane. Não omita o coautor por confiar somente nos metadados.

A elaboração considerou o texto da introdução, dos dez capítulos da parábola, dos sete capítulos explicativos, da conclusão, do Q&A, do quadro final e das notas. As imagens de folha de rosto, aberturas das partes e faixa de resumo foram inspecionadas. Dedicação, agradecimentos, endossos e publicidade final foram distinguidos do ensino metodológico.

A sistematização inicial foi construída a partir do EPUB, sem preencher lacunas por resumos da internet. Na atualização, o usuário forneceu dois resumos e uma proposta de configuração; seus acréscimos foram distinguidos do ensino do livro. A skill contém síntese em palavras próprias e instrumentos de aplicação; não inclui cópia integral do livro.

### Talbot Davis

- **Obra:** *Simplify the Message: Multiply the Impact*.
- **Autor:** Talbot Davis.
- **Editora e data indicadas na citação embutida:** Abingdon Press, Nashville, 2020.
- **Arquivo lido:** `Simplify the Message_ Multiply the Impact - TALBOT DAVIS.rtf`.
- **Local original:** `C:/DEV/SERMÃO 1 PONTO - ANDY/Simplify the Message_ Multiply the Impact - TALBOT DAVIS.rtf`.
- **SHA-256:** `762030d68aa585a80b6b1d2e035822224a96801a8cd7c5f5b549493d5610eb7b`.
- **Conferência inicial:** 8 de outubro de 2026.

Foram lidos introdução e capítulos 1–9. A integração usa síntese própria e mantém separados os relatos da igreja de Davis, suas interpretações particulares, sua rotina pessoal e os princípios transferíveis. Davis reconhece explicitamente sua adaptação da abordagem de Stanley; ele não é coautor de *Communicating for a Change*.

## 2. Convenção de localização

`C12` significa **capítulo 12 do livro**, não o arquivo `chapter-012.xhtml`. Neste EPUB, os capítulos 1–17 ocupam `chapter-009.xhtml` até `chapter-026.xhtml`.

`§043` significa o **43º bloco textual não vazio**, contando em ordem os elementos XHTML `p`, `h1`, `h2`, `h3`, `h4` e `li`, com texto interno unido e espaços normalizados. Os títulos também contam. Essa numeração foi criada para conferência técnica e **não é numeração de parágrafos impressa pelos autores**.

O EPUB contém marcadores de página e localização. O leitor auxiliar mostra o marcador de página e a âncora mais recentes, quando disponíveis, mas a skill usa capítulos/seções/blocos como referência principal para evitar confusão entre edição e posição de leitura.

Use [consultar_fonte.py](../scripts/consultar_fonte.py) com Python 3 e a cópia do EPUB. Exemplos executados a partir da pasta desta skill:

```powershell
python scripts/consultar_fonte.py --epub 'C:/DEV/SERMÃO 1 PONTO - ANDY/Communicating for a Change_ Seven Keys to Irresistible Communication.epub' --indice
python scripts/consultar_fonte.py --epub 'C:/DEV/SERMÃO 1 PONTO - ANDY/Communicating for a Change_ Seven Keys to Irresistible Communication.epub' --capitulo 13 --inicio 59 --fim 64
python scripts/consultar_fonte.py --epub 'C:/DEV/SERMÃO 1 PONTO - ANDY/Communicating for a Change_ Seven Keys to Irresistible Communication.epub' --capitulo 14 --buscar 'five-minute'
```

O script lê o ZIP sem extrair seus arquivos e não modifica o EPUB. Confere a identidade do arquivo antes de usar as referências específicas desta edição. Se o EPUB estiver ausente, a skill ainda pode aplicar sua síntese, mas deve ser honesta sobre não ter reconferido a fonte primária naquela execução. Não reconstrua citações literais pela memória nem invente paginação.

Para Davis, `D4` significa capítulo 4 e `L276–371` significa linhas do texto extraído do RTF em ordem de leitura. A conversão foi feita no Windows com `System.Windows.Forms.RichTextBox`, preservando os parágrafos como linhas; esses números são localizadores técnicos desta cópia, não páginas impressas. Como alternativa mais portátil, cite capítulo e título de seção. Os hyperlinks internos do RTF apresentam alguns destinos bíblicos desalinhados com o texto visível; confira a referência bíblica na própria passagem antes de reutilizá-la.

Se o arquivo de Davis estiver ausente, use a síntese de [aprofundamentos](09-talbot-davis-aprofundamentos.md) e [funerais](10-funerais-e-memoriais.md), declarando que não houve reconferência do RTF naquela execução. Não inclua o livro integral no pacote da skill.

## 3. Mapa da obra

| Parte/seção | Arquivo interno | Uso na skill |
|---|---|---|
| Introdução | `OEBPS/text/chapter-007.xhtml` | Origem do método, função de Lane, um ponto e diferença entre pregação e treinamento. |
| Cap. 1–2 | `chapter-009.xhtml`–`chapter-010.xhtml`, sob `OEBPS/text/` | Problema da desconexão; avaliação e contexto da parábola. |
| Cap. 3 — Go for the Goal | `chapter-011.xhtml` | Objetivo antes da técnica. |
| Cap. 4 — The End of the Road | `chapter-012.xhtml` | Destino único, unidade, retenção e desvios. |
| Cap. 5 — A Map to Remember | `chapter-013.xhtml` | Oração, mapa relacional e promessa de aplicação. |
| Cap. 6 — Load Up Before You Leave | `chapter-014.xhtml` | Domínio pessoal do percurso. |
| Cap. 7 — Crucial Connections | `chapter-015.xhtml` | Necessidade percebida, conexão, perspectivas e transições. |
| Cap. 8 — Show Me Some Identification | `chapter-016.xhtml` | Voz autêntica e avaliação da própria fala. |
| Cap. 9 — Stuck in the Middle of Nowhere | `chapter-017.xhtml` | Oração, quatro perguntas e *Find Some Traction*. |
| Cap. 10 — A New Attitude | `chapter-018.xhtml` | Mudança de vida e aprendizagem gradual. |
| Introdução à parte II | `chapter-019.xhtml` | Importância pastoral e disposição para mudar a comunicação. |
| Cap. 11 — Determine Your Goal | `chapter-020.xhtml` | Finalidade da comunicação. |
| Cap. 12 — Pick a Point | `chapter-021.xhtml` | Descoberta, organização, frase e encargo. |
| Cap. 13 — Create a Map | `chapter-022.xhtml` | Funções e desenvolvimento dos cinco movimentos. |
| Cap. 14 — Internalize the Message | `chapter-023.xhtml` | Marcos, memória, notas e ensaio. |
| Cap. 15 — Engage Your Audience | `chapter-024.xhtml` | Abertura e cinco orientações de condução. |
| Cap. 16 — Find Your Voice | `chapter-025.xhtml` | Autenticidade, princípios, tempo e avaliação. |
| Cap. 17 — Start All Over | `chapter-026.xhtml` | Recomeço, dependência espiritual e cinco perguntas. |
| Conclusão | `chapter-027.xhtml` | Aplicação como força organizadora e crescimento do comunicador. |
| Q&A with Andy | `chapter-028.xhtml` | Práticas pessoais de agenda e planejamento. |
| Me-We-God-You-We | `chapter-029.xhtml` | Quadro das cinco perguntas e suas funções. |
| Notes | `chapter-030.xhtml` | Referências bíblicas e atribuições. |
| Copyright | `chapter-034.xhtml` | Dados bibliográficos. |

Nos nomes abreviados da tabela, a pasta interna continua sendo `OEBPS/text/`.

### Mapa de Talbot Davis

| Parte | Linhas do RTF convertido | Uso na skill |
|---|---:|---|
| Introdução | L033–072 | Clutter versus clareza; origem de sua adoção do sermão de um ponto. |
| D1 — From Clutter to Clarity | L073–125 | Envolver–Encontrar–Capacitar, refrão e três formas de frase central. |
| D2 — From InterestED to InterestING | L126–200 | Exegese, forma literária, observação anterior aos comentários. |
| D3 — The Pastoral Sherlock Holmes | L201–275 | Observação pastoral, cultura, memória, ficção e confidencialidade. |
| D4 — Keep Me Awake, Please | L276–371 | Aventura, tensão, aberturas, dilema, descoberta e experiência. |
| D5 — Play It by Ear | L372–454 | Manuscrito, escrita oral e lapidação da frase central. |
| D6 — Who Shot J. R.? | L455–541 | Continuidade, conceito, missão e resposta comunitária em séries. |
| D7 — Special Delivery | L542–594 | Internalização, ensaio e preferência por entrega sem notas. |
| D8 — An Overlooked Opportunity | L595–692 | Funerais, expressão, permissão, pessoa antes da promessa e esperança. |
| D9 — Simply Irresistible | L693–747 | Voz, centralidade de Cristo, crítica ao moralismo e convite. |

## 4. Matriz de rastreabilidade dos princípios

| Ensino ou ressalva | Local conferível |
|---|---|
| Abordagem orientada pelo objetivo; três objetivos possíveis | C11 §011–039 |
| Mudança envolve prática; responder à relevância e ao próximo passo | C11 §028–049 |
| A meta na parábola é vida que reflita o amor de Cristo | C10 §005–012 |
| O método proposto não é o único que Deus utiliza | C5 §035–037; C12 §015–016 |
| Ponto como aplicação, percepção ou princípio | C12 §018–024 |
| Saber e fazer como perguntas centrais | C12 §025–033; §103 |
| Uma frase central não elimina outras observações subordinadas | C12 §033 |
| Descoberta pode ocorrer tarde na preparação | C12 §035–044 |
| Três etapas: descobrir, organizar, tornar memorável | C12 §037–068; §105–108 |
| A ideia pode partir da vida, mas o texto a corrige | C12 §045–057 |
| Seleção do material; guardar boas ideias periféricas | C12 §061–064; C14 §047–051 |
| Frase curta e memorável sem obrigação de rima | C12 §066–068 |
| Palavra bíblica ou pergunta como ponto | C12 §082–084 |
| Encargo pastoral e convicção do comunicador | C12 §087–094 |
| Organização e ação do Espírito não se excluem | C12 §095–100 |
| Mapa relacional e cinco funções | C13 §004–019; C5 §041–066 |
| EU estabelece conexão; público novo/recorrente importa | C13 §029–038 |
| NÓS amplia a tensão e dá razão para escutar | C13 §040–047 |
| Aplicação como contexto de toda a mensagem | C13 §048–049; conclusão §002 |
| Não levantar necessidades sem tratamento posterior | C5 §054–062 |
| Iluminação pode resolver parte da tensão | C13 §051–060 |
| Uma aplicação focal, com adaptações e horizonte praticável | C13 §061–081 |
| Categorias de aplicação não devem ser todas recitadas | C13 §065–080, especialmente §077 |
| Cristãos, não cristãos e pessoas ausentes | C13 §078–081 |
| NÓS final como visão, não obrigatoriedade de grande história | C13 §082–087 |
| Marcar o mapa no esboço existente e reorganizar | C13 §088–096 |
| Versão conversacional de cinco minutos | C14 §012–016 |
| Cinco ou seis blocos, não pontos concorrentes | C14 §019–030 |
| Possibilidade de abrir com o texto | C14 §024–029 |
| Notas, cartões e monitor podem ser usados | C14 §031–040; §052 |
| Ensaio de histórias, introdução e conclusão | C14 §041–043 |
| Apresentação e interesse prévio | C15 §007–043 |
| Pergunta, tensão ou mistério como abertura | C15 §044–060 |
| Velocidade: evitar lentidão e pressa | C15 §063–068 |
| Transições escritas e desaceleradas | C15 §069–076; C7 §077–104 |
| Uma passagem para abrir, com auxiliares possíveis | C15 §079 |
| Leitura comentada, termos e dificuldades | C15 §080–087 |
| Antecipação, contraste alterado e participação oral | C15 §088–099 |
| Síntese do texto, visuais e seleção | C15 §100–110 |
| Elementos inesperados e colaboração criativa | C15 §111–116 |
| Rota direta; ressalva sobre abordagem indireta | C15 §117–123 |
| Autenticidade não desculpa maus hábitos | C16 §004–018; §039–043 |
| Encerramento gradual e pausa antes da oração | C16 §028–032 |
| Respeito ao tempo combinado | C16 §033–038 |
| Não há estilo único; avaliar o que funciona e funciona para si | C16 §050–062 |
| Autor não garante resultados da aplicação do livro | C16 §045 |
| Escutar diversos comunicadores e a própria gravação | C8 §043–056; C16 §059–061 |
| Recomeçar não é descartar toda a pesquisa | C17 §019 |
| Oração e ação de Deus, não poder autônomo da técnica | C17 §011–015; C9 §031–034 |
| Saber / por que saber / fazer / por que fazer | C9 §040–044; C17 §020–049 |
| Lembrança como quinta pergunta; não sempre há recurso | C17 §050–053 |
| Cinco funções: informação, motivação, aplicação, inspiração, reiteração | C17 §054–070; quadro final |
| Ideia da série e ponto de cada mensagem | C12 §018–024 |
| Uma aplicação pode continuar ao longo da série | C17 §042 |
| Agenda, duração e planejamento são práticas relatadas | C14 §044–048; Q&A §002–019 |
| Treinamento informativo pode usar outra abordagem | Introdução §026–027 |

### Princípios acrescentados a partir de Davis

| Ensino ou ressalva | Local conferível |
|---|---|
| Envolver–Encontrar–Capacitar e correspondência com o mapa de Stanley | D1 L078–095 |
| História pessoal como observador/peregrino; possibilidade de abrir com o texto | D1 L083–089 |
| Aplicar o mesmo ponto a fases da vida e usar a frase como refrão | D1 L090–101 |
| Frases declarativas, imperativas e interrogativas | D1 L102–124 |
| Interesse do pregador, recepção oral, gênero e agenda do texto | D2 L129–160 |
| Repetição, interrogação, contraste e arte literária | D2 L161–189 |
| Observação própria antes dos comentários; pesquisa para confirmar/corrigir | D2 L190–200 |
| Observação pastoral, memória, cultura e ficção como material | D3 L201–275 |
| Proteção de anonimato e pedido de permissão | D3 L246–258 |
| Sermão como aventura: tensão, descoberta, resolução e experiência | D4 L276–371 |
| Cinco tipos de abertura, inclusive a própria Escritura | D4 L303–318 |
| Frase central não é a frase final; desenvolver aplicação | D4 L351–367 |
| Manuscrito completo e escrita para o ouvido | D5 L381–400 |
| Lapidação por jogo de palavras, contraste, ritmo e som | D5 L401–443 |
| Continuidade e resposta comunitária em séries | D6 L455–541 |
| Internalização em vez de recitação; ensaio oral e contato | D7 L542–594 |
| Funeral: memória, consolo, expressão, permissão e pessoa antes da promessa | D8 L595–657 |
| Cuidados em situações fúnebres e limites de afirmação | D8 L658–692 |
| Voz própria, criatividade orgânica e centralidade de Cristo | D9 L693–731 |
| Convite adaptado a necessidades reconhecíveis | D9 L731–747 |

## 5. O que pertence à sistematização desta skill

São adaptações operacionais, coerentes com o propósito, mas não regras literalmente ensinadas no livro:

- Levantamento de público, duração, formato e versão bíblica em uma ficha.
- Rubricas resumidas para documentar contexto e limites da interpretação.
- Modelos de entrega, tabelas de auditoria e estados “atende/ajustar/não verificável”.
- Verificação de citações, identificação de hipóteses e proibição de inventar a biografia do usuário.
- Marcação editorial explícita e correção imediata quando se propõe o contraste por leitura alterada.
- Distinção entre rascunho preparado e internalização ainda dependente do pregador.
- Leitor técnico do EPUB, hash e localização de blocos.
- Exemplos em português criados para demonstrar a aplicação.
- Tabela de observação, inferência e questão a verificar.
- Correspondência operacional entre os dois mapas e checklists integrados.
- Folha de internalização por objetivo, imagem, verdade, transição e palavra-gatilho.
- Adaptação PESSOA–NÓS–DEUS–VOCÊS–NÓS para funerais.

Não acrescente a essa lista métodos externos de homilética como se fossem etapas de Stanley/Jones. Ferramentas adicionais podem ser utilizadas a pedido do usuário, desde que distinguidas da metodologia-fonte.

## 6. Preferências que não viram mandamentos

Não é exigência dos autores para toda situação: falar quarenta minutos; preparar três semanas à frente; fazer séries de quatro a seis encontros; estudar em determinados dias; usar rima; ter humor; retirar o púlpito; pregar sentado; levar objetos; sempre distribuir lembranças; praticar uma ação exatamente por sete dias; nunca olhar notas; usar somente um versículo; jamais começar pela Bíblia; dar porcentagens fixas de tempo aos cinco movimentos.

Também não há no livro: nota mínima numérica, fórmula de contagem de palavras para o ponto, quantidade obrigatória de repetições, garantia de crescimento de audiência ou prova de transformação de todos. “Fidelidade” aqui significa correspondência verificável ao ensino e às ressalvas, não garantia matemática de resultado.

Em Davis, também são preferências e práticas pessoais: manuscrito integral toda semana; pregar sempre sem notas; determinada quantidade de ensaios e contatos com o manuscrito; percentuais de tipos de frase; uso frequente de séries; títulos baseados em cultura popular; campanhas e estratégias da Good Shepherd Church; estilo enfático; formas específicas de apelo. Transfira o princípio pertinente sem copiar a rotina ou a persona.

## 7. Cuidados de leitura

Há humor, exagero retórico, diálogos ficcionais e comentários pessoais. Não transforme piadas em procedimentos — por exemplo, mentir para proteger o ego do pregador ou entregar uma reescrita não solicitada ao orador. A parábola ilustra o método; não é um conjunto de depoimentos históricos sobre Ray e Will.

Não importe toda opinião social, exemplo denominacional ou conclusão doutrinária particular de uma ilustração como requisito de todas as mensagens. O livro ensina deixar a Escritura governar o ponto; o usuário ainda precisa fornecer ou escolher o contexto teológico da aplicação.

O EPUB contém pequenas irregularidades textuais e seus paratextos não constituem orientação metodológica. Preserve a diferença entre o argumento central, exemplos, atribuições em notas e publicidade de outros títulos. Se uma formulação permanecer ambígua, consulte o contexto e descreva a incerteza em vez de fortalecer a regra além do que a fonte permite.

O RTF de Davis contém campos `HYPERLINK` visíveis e alguns destinos automáticos incorretos. Há formulações retóricas, generalizações psicológicas, interpretações próprias e exemplos denominacionais. Não transforme isso em dado científico, exegese obrigatória ou doutrina universal. No capítulo 9, a centralidade de Cristo corrige moralismo, mas não autoriza alegorizar cada detalhe bíblico. No capítulo 8, sua escatologia pastoral deve ser adaptada à tradição informada pelo usuário.

## 8. Sugestões fornecidas pelo usuário e configuração de uso

O usuário solicitou explicitação obrigatória das cinco perguntas, do teste do ponto em uma frase e da aplicação concreta. Também sugeriu VOCÊS como rótulo, tempos por movimento, aplicação semanal, limites de ilustrações, três repetições e tabela Antes / Agora. Posteriormente, tornou obrigatória a abertura da entrega com exatamente cinco variações de bottom line e cinco alternativas de frase-refrão, com um par recomendado já aplicado ao sermão. As cinco perguntas têm respaldo em C17 e no quadro final; os números, a quantidade de alternativas e o formato de entrega são configurações do usuário. A proposta mais recente de EU 2–4 minutos substitui a anterior de 1–2 minutos; o tempo total informado prevalece sobre faixas sugeridas.

No resumo fornecido, foram consultadas as páginas [Seminário Batista do Sul — sermão de um ponto](https://semibsul.com.br/sermao-de-um-ponto-como-preparar/), [Allen Vaz — Comunicação que Transforma](https://allenvaz.blogspot.com/2010/03/andy-stanley-comunicacao-que-transforma.html) e [Didymus Lab — one-point sermon](https://didymuslab.com/en/blog/one-point-sermon). São fontes secundárias; não substituem o EPUB para atribuições aos autores. Os demais links do resumo não constituem fonte primária verificada nesta atualização.

Na publicação de 8 de outubro de 2026, o nome técnico passou a ser `sermao-de-1-ponto-andy-stanley-talbot-davis` e o nome de exibição, **Sermão de 1 Ponto (Andy Stanley-Talbot Davis)**, conforme solicitação do usuário. A coautoria de Lane Jones e sua contribuição metodológica permanecem explícitas no conteúdo e na documentação, embora o nome de exibição siga a forma pedida.

### Obrigatoriedade de histórias, ilustrações e analogias

Em atualização posterior, o usuário determinou que a skill inclua obrigatoriamente histórias, ilustrações e analogias para reforçar o ponto e iluminar a mensagem. A exigência aplica-se à geração e à reescrita de sermões completos e esboços desenvolvidos. Está operacionalizada no SKILL.md, no guia de engajamento, nos modelos e na auditoria.

O emprego de recursos a serviço do ponto se relaciona a C12 §061–064, C14 §041–043 e C15. A exigência simultânea das três funções, seu registro na ficha e o limite de quatro peças são configurações do usuário, não uma fórmula numérica publicada pelos autores. Um único recurso pode exercer mais de uma função quando isso estiver desenvolvido. A abertura não exige autobiografia e o encerramento não exige uma história nova.
