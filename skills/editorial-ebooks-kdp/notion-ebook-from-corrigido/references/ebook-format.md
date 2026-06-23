# Ebook Format

Use este formato como padrão ao escrever o conteúdo que será salvo na coluna `ebook`.

## Objetivo

Transformar a transcrição corrigida da pregação em um ebook conversacional, fluido e substancioso, com mínimo de 10.000 palavras, leitura agradável, estrutura clara e acabamento real de livro cristão.

## Estrutura sugerida

1. Título forte e claro
2. Abertura curta conectando o leitor ao problema, tensão ou pergunta central
3. 5 a 8 capítulos ou seções com subtítulos nítidos
4. Progressão real do argumento ao longo do livro
5. Conclusão pastoral e prática
6. Encerramento breve chamando o leitor à reflexão, resposta e entrega

## Estrutura editorial recomendada

- `Abertura`: entrar direto no tema humano e espiritual da mensagem
- `Capítulos centrais`: cada um desenvolve um movimento novo do argumento
- `Aterrissagem pastoral`: ao fim de cada capítulo, uma aplicação curta e limpa
- `Conclusão`: reunir o argumento e levar o leitor à resposta diante de Deus

Evite capítulos que apenas renomeiam a mesma ideia.

## Voz

- Conversacional
- Pastoral
- Clara
- Direta
- Sem jargão técnico desnecessário
- Com acabamento literário forte, como um bom livro devocional e formativo cristão
- Com calor humano e reverência bíblica
- Sem soar como aula, ata de culto, devocional raso ou “sermão inflado”

## Faça

- Fale com o leitor usando “você”
- Reorganize a lógica para leitura contínua
- Preserve o coração da mensagem
- Destaque aplicações concretas
- Simplifique repetições típicas de fala ao vivo
- Expanda com fidelidade até ultrapassar 10.000 palavras sem inventar fatos ou temas externos
- Garanta que cada bloco acrescente conteúdo novo
- Desenvolva melhor o que já está no sermão em vez de reapresentar a mesma ideia em outra ordem
- Use NVI pt-BR como versão bíblica padrão
- Transforme oralidade em prosa pastoral limpa
- Prefira frases firmes e fluídas a parágrafos excessivamente explicativos
- Faça transições elegantes entre capítulos
- Preserve o centro espiritual da mensagem mais do que a ordem exata da fala original
- Use imagens, contrastes e aplicações que já estão legitimamente implícitos na mensagem
- Faça o texto respirar como livro: abertura forte, corpo progressivo, fechamento memorável

## Não faça

- Não escreva como transcrição
- Não inclua timestamps
- Não inclua observações de palco, plateia ou produção
- Não copie blocos desnecessariamente longos do original
- Não transforme o texto em estudo acadêmico
- Não use repetição disfarçada para bater meta de palavras
- Não recicle parágrafos, listas ou explicações dentro do mesmo ebook
- Não encha o texto com frases meta como “neste capítulo veremos”
- Não abra capítulos recapitulando longamente o que o capítulo anterior já disse
- Não use linguagem genérica de autoajuda desconectada da mensagem bíblica
- Não troque densidade pastoral por volume verbal

## Critério de fidelidade

O ebook deve soar melhor do que a transcrição, mas continuar claramente derivado dela. Melhorar a forma é esperado. Inventar conteúdo não é.

Ele deve soar como um livro cristão que nasceu daquela mensagem, não como uma transcrição alongada daquela mensagem.

## Regra de expansão

Quando a transcrição for mais curta do que o necessário para sustentar um ebook de 10.000 palavras:

- Desdobre argumentos já presentes
- Explique implicações pastorais do que foi dito
- Conecte blocos da mensagem com transições mais claras
- Aprofunde aplicações, convites à reflexão e exemplos já sugeridos no sermão
- Trate cada seção como avanço real do argumento, não como reforço redundante
- Extraia consequências espirituais, afetivas e práticas do texto bíblico já trabalhado na pregação
- Dê espaço para contemplação e aplicação, mas sem girar em círculos
- Prefira aprofundar menos ideias com mais densidade a multiplicar tópicos superficiais

Evite expansão artificial. Repetição disfarçada, paráfrase redundante e reapresentação do mesmo bloco em outra ordem continuam sendo repetição.

Não acrescente histórias, doutrinas, citações ou episódios que não possam ser justificados pelo material de origem.

## Ordem de limpeza do texto bruto

Antes de iniciar a redação final, aplique esta ordem ao material de origem:

1. Normalizar quebras de linha, espaços, aspas, travessões e caracteres invisíveis.
2. Remover símbolos e ruídos que pertencem à transcrição, não ao texto final.
3. Reunir o conteúdo em blocos de leitura contínua.
4. Só então fazer a correção em pt-BR e transformar em ebook.

Se a fonte for curta demais para sustentar um livro bom, não force volume. Em fluxo operacional normal, prefira outra página com mais material antes de escrever.

## Checklist de qualidade literária

Antes de considerar o ebook pronto, confira:

- A abertura prende o leitor sem parecer introdução escolar
- O título e os subtítulos soam como livro, não como pauta de sermão
- Cada capítulo tem função própria
- A voz está pastoral, bíblica e calorosa
- O texto não depende do contexto do culto para fazer sentido
- O fechamento deixa convicção, consolo ou chamado claro
- O livro está mais limpo, mais profundo e mais legível do que a transcrição

## Observação prática

Em muitas fontes, a transcrição começa com culto, avisos, louvor, oração inicial ou anúncios. Sempre procure o primeiro movimento expositivo real da mensagem antes de mapear capítulos.

## Validação operacional

Antes do upload no Notion, o arquivo deve passar na validação local do script:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" validate --input-file "ebook.md"
```

Por padrão, a validação exige:

- Mínimo de 10.000 palavras
- Zero parágrafos longos duplicados
- Taxa baixa de frases longas repetidas

Se o arquivo não passar, ele deve ser reescrito e aprofundado antes do `push`.
