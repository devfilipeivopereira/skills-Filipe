---
name: romance-adulto-30k
description: "Cria do início ao fim romances adultos originais em português brasileiro, com exatamente 30.000 palavras de prosa ficcional, estrutura narrativa em 15 batidas, arco romântico completo e final HEA/HFN. Planeja, redige, revisa, cria capa, incorpora metadados da autora Kang Arin e entrega EPUB responsivo validado para publicação no Amazon KDP. Use quando o usuário pedir um romance, novela romântica, livro de romance adulto, manuscrito de 30 mil palavras ou arquivo EPUB/KDP de ficção romântica."
---

# Romance Adulto 30K para KDP

Produza uma obra completa e publicável, não apenas sinopse, amostra ou esqueleto. A autoria editorial e os metadados são sempre de **Kang Arin**. O romance final deve conter **exatamente 30.000 palavras de prosa ficcional**, contadas pelo script desta skill, e ser entregue como EPUB responsivo com capa incorporada e também como JPEG separado para o cadastro no KDP.

## Princípios obrigatórios

- Escrever por padrão em português brasileiro; respeitar outro idioma somente quando solicitado.
- Tratar “adulto” como público, complexidade e protagonistas adultos, não como obrigação de erotismo.
- Todos os participantes de romance ou sexo devem ser adultos. Para conteúdo sexual explícito, declarar no planejamento que têm 21 anos ou mais.
- Definir antes da escrita o nível de calor de 0 a 4, conforme `references/romance-adulto.md`.
- Entregar uma história original. Não copiar passagens, personagens, mundos, títulos distintivos ou voz reconhecível do livro-fonte ou de autores vivos.
- Preservar agência, consentimento, consequências emocionais e coerência psicológica.
- Fechar o arco central com HEA ou HFN. Só usar final trágico quando o usuário pedir expressamente ficção amorosa trágica; nesse caso, não rotular o livro como romance de gênero.
- Não alegar que o EPUB foi aprovado pela Amazon. Informar apenas as verificações realmente executadas.

## Descoberta da encomenda

Extraia da solicitação, quando existirem: subgênero, premissa, casal ou configuração romântica, cenário, época, ponto de vista, pessoa verbal, nível de calor, tropos desejados/proibidos, sensibilidades, final e título.

Quando faltarem dados não essenciais, não interrompa o trabalho. Use estes padrões:

- subgênero: romance contemporâneo;
- protagonistas: adultos de 25 a 40 anos;
- estrutura afetiva: um casal central;
- ponto de vista: terceira pessoa limitada alternada entre os protagonistas;
- tempo verbal: passado;
- nível de calor: 2, sensual sem descrição gráfica;
- final: HEA;
- extensão: 12 capítulos, aproximadamente 2.500 palavras de prosa cada;
- autora: Kang Arin;
- idioma/metadado: `pt-BR`.

Pergunte apenas se uma escolha ausente mudaria materialmente a obra ou envolveria um limite de conteúdo que não possa ser inferido com segurança.

## Fluxo completo

Siga as etapas na ordem. Mantenha no diretório do projeto uma pasta `romances/<slug-do-titulo>/` com os artefatos intermediários e finais.

### 1. Criar a bíblia narrativa

Leia `references/metodo-estrutural.md`, `references/generos-de-historia.md` e `references/romance-adulto.md`. Produza `planejamento.md` com:

- promessa emocional, subgênero, público, nível de calor e HEA/HFN;
- logline e sinopse curta;
- ficha dos protagonistas e antagonismo;
- para cada protagonista: problema/falha, desejo mensurável, necessidade/verdade e ferida emocional;
- dinâmica romântica, fonte da atração, incompatibilidade aparente, barreira real, vulnerabilidades, marcos de intimidade e prova final de amor;
- gênero estrutural principal e seus três ingredientes;
- mapa das 15 batidas com metas cumulativas de palavras;
- lista de 30 a 40 cenas, cada uma com POV, objetivo, conflito, virada e consequência;
- cronologia, lugares, fatos sensíveis, nomes e detalhes que exigirão controle de continuidade.

O romance pode usar “Buddy Love” como história A. Se outro gênero estrutural for dominante, use o relacionamento como história B transformadora. Nunca deixe a trama externa substituir a progressão afetiva.

### 2. Planejar exatamente 30.000 palavras

Leia `references/producao-30000.md`. Distribua a prosa entre capítulos e cenas antes de redigir. Use as metas de batidas como bússola, não como pontos matemáticos rígidos, mas faça o total final ser exato.

Conte somente a prosa ficcional de `manuscrito.md`. Título, cabeçalhos de capítulo, front matter, divisores e metadados não entram na meta. Use:

`python scripts/count_words.py <caminho-do-manuscrito> --target 30000`

O contador desta skill é a autoridade operacional. Não estime pelo editor ou pelo modelo.

### 3. Redigir o manuscrito integral

Escreva `manuscrito.md` do começo ao fim, com `# Título` e `## Capítulo N — Nome`.

- Abrir cenas tarde e encerrá-las cedo.
- Dar a cada cena desejo local, resistência, mudança e consequência.
- Manter causalidade: a decisão de uma cena cria o problema da seguinte.
- Alternar tensão externa, vulnerabilidade e aproximação sem repetir a mesma conversa.
- Fazer atração, confiança e compromisso evoluírem por ações observáveis.
- Inserir o tema organicamente; não discursar.
- Usar detalhes sensoriais específicos e diálogo com subtexto.
- Evitar infodumps, coincidências resolutivas, conflito sustentado apenas por falta de comunicação facilmente sanável e reconciliação sem mudança demonstrada.
- Usar `***` sozinho em uma linha para quebras de cena.
- Não inserir capa, ficha catalográfica, sumário manual, contagem de palavras, notas do processo ou comentários no arquivo de prosa.

### 4. Revisar em passagens separadas

Leia `references/controle-de-qualidade.md` e execute, nesta ordem:

1. estrutura e causalidade;
2. arco romântico e consentimento;
3. continuidade e cronologia;
4. cenas e ritmo;
5. voz, diálogo e prosa;
6. correção linguística em PT-BR;
7. remoção de clichês involuntários, repetições e sinais de texto automatizado;
8. ajuste fino para exatamente 30.000 palavras.

Ao cortar ou acrescentar palavras, preserve voz, lógica e cadência. Nunca complete a meta com enchimento. Rode o contador após cada passagem final e registre o resultado em `relatorio-validacao.md`.

### 5. Preparar metadados editoriais

Leia `references/pitch-e-metadados.md`. Crie `metadata.json` em UTF-8 com, no mínimo:

- `title`, `subtitle` quando houver e `author: "Kang Arin"`;
- `language: "pt-BR"`;
- `publisher: "Kang Arin"`, salvo selo informado pelo usuário;
- `description`, `subjects`, `keywords` e data de publicação;
- direitos autorais de Kang Arin para o ano de publicação;
- identificador UUID. Não inventar ISBN.

Título, subtítulo e autora devem coincidir exatamente no manuscrito, na capa, no EPUB e no cadastro sugerido para KDP.

### 6. Criar a capa

Leia `references/capa-kdp.md`. Use a ferramenta de geração de imagens para criar **somente a arte de fundo**, sem texto, logotipos, preço, selo, moldura, código de barras ou marca-d'água. Baseie o briefing no romance já concluído, escolhendo símbolos e atmosfera próprios da obra. Evite rostos reconhecíveis e elementos protegidos de outras franquias.

Depois componha tipografia determinística para evitar erros ortográficos:

`python scripts/make_kdp_cover.py arte-gerada.png capa.jpg --title "Título exato" --author "Kang Arin" [--subtitle "Subtítulo"]`

O resultado deve ser JPEG RGB vertical, 1600 × 2560 px, sem lombada ou quarta capa, legível em miniatura e preferencialmente com até 5 MB. Inspecione visualmente a imagem final. Se a arte ou legibilidade falhar, gere/recomponha; não aceite texto truncado, mãos deformadas, artefatos ou contraste insuficiente.

### 7. Montar o EPUB responsivo para KDP

Leia `references/kdp-epub.md`. Gere o arquivo:

`python scripts/build_kdp_epub.py manuscrito.md metadata.json capa.jpg romance.epub`

O construtor deve incluir página de rosto, copyright, sumário HTML e lógico, capítulos, CSS responsivo, navegação EPUB 3, metadados Dublin Core e a capa como `cover-image`. Ele não deve criar uma página HTML adicional para a capa, evitando duplicação no Kindle.

### 8. Validar antes da entrega

Execute:

`python scripts/validate_epub.py romance.epub --manuscript manuscrito.md --target 30000`

Corrija todos os erros. Quando Kindle Previewer ou EPUBCheck estiver disponível, abra/valide também nele e registre versão e resultado. Faça uma inspeção visual em modos de fonte pequena/grande, claro/escuro e, se possível, telefone/tablet.

O pacote final deve conter:

- `<slug>.epub` — arquivo principal para upload do eBook;
- `capa.jpg` — a mesma capa para upload separado no KDP;
- `metadata.json` — dados para cadastro;
- `pacote-editorial.md` — título, logline, descrição, categorias/assuntos, palavras-chave, avisos de conteúdo e resumo comercial;
- `relatorio-validacao.md` — contagem exata, verificações técnicas executadas e limitações restantes.

Entregue primeiro os links para o EPUB e a capa. Informe explicitamente: “30.000 palavras de prosa ficcional pelo contador da skill”, se a validação passar.

## Referências de uso seletivo

- `references/metodo-estrutural.md`: herói, 15 batidas, customizações e arco de transformação.
- `references/generos-de-historia.md`: escolher e executar um dos dez gêneros estruturais.
- `references/romance-adulto.md`: progressão afetiva, calor, consentimento, HEA/HFN e subgêneros.
- `references/producao-30000.md`: orçamento de palavras, cenas e ajuste exato.
- `references/controle-de-qualidade.md`: listas de revisão narrativa e linguística.
- `references/pitch-e-metadados.md`: logline, sinopse e pacote comercial.
- `references/capa-kdp.md`: briefing visual, composição e inspeção da capa.
- `references/kdp-epub.md`: estrutura, metadados e requisitos atuais de publicação.
