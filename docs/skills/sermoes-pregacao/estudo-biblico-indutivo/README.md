# Estudo Bíblico Indutivo — Bauer e Traina

Skill em português brasileiro para conduzir estudos indutivos de passagens e livros bíblicos segundo David R. Bauer e Robert A. Traina, em *Inductive Bible Study: A Comprehensive Guide to the Practice of Hermeneutics*.

- Categoria: **Sermões e Pregação** (`sermoes-pregacao`).
- Nome de invocação: `$estudo-biblico-indutivo`.
- [Arquivo principal da skill](../../../../skills/sermoes-pregacao/estudo-biblico-indutivo/SKILL.md).
- [Pacote instalável com o EPUB](../../../../packages/sermoes-pregacao/estudo-biblico-indutivo.zip).
- [EPUB completo dentro da skill](../../../../skills/sermoes-pregacao/estudo-biblico-indutivo/references/fontes/inductive-bible-study-bauer-traina.epub).
- [Relatório de leitura, validação e testes](../../../estudo-biblico-indutivo/VALIDACAO.md).

## Quando usar

Use para estudo bíblico indutivo, exegese completa de uma passagem, levantamento de um livro, ensino do método ou revisão de um estudo por essa metodologia. Pedidos de simples citação de versículo ou de sermão sem estudo indutivo não exigem este fluxo completo.

## O que a skill faz

1. Identifica texto, tradução, objetivo, público, recorte e recursos disponíveis.
2. Levanta o livro como um todo: materiais predominantes, divisões, relações estruturais, perguntas, passagens estratégicas e dados históricos internos.
3. Examina as partes como totalidades e realiza observação focalizada ou análise do fluxo.
4. Formula perguntas definitivas, racionais e implicacionais, selecionadas por relevância.
5. Interpreta por evidências, premissas e inferências, com exame de alternativas e diálogo crítico com outros intérpretes.
6. Integra o sentido original e avalia legitimidade, alcance, força e grau de concessão antes de aplicar.
7. Propõe apropriação pessoal e comunitária e correlaciona o resultado com outras unidades, preservando sua contribuição própria.

Inclui o inventário de 17 relações estruturais, os quinze tipos de evidência interpretativa e auditorias das falácias de interpretação, apropriação e correlação. A extensão se adapta ao pedido sem confundir um resumo ou estudo provisório com investigação completa.

## Estrutura do pacote

```text
estudo-biblico-indutivo/
  SKILL.md
  agents/openai.yaml
  references/
    fundamentos.md
    observacao.md
    interpretacao.md
    avaliacao-apropriacao.md
    correlacao.md
    modelo-estudo.md
    fontes-e-fidelidade.md
    fontes/
      inductive-bible-study-bauer-traina.epub
```

O EPUB está dentro da pasta da skill e também no ZIP instalável. Sua consulta aprofundada é opcional para executar as instruções operacionais, mas permite conferir nuances e atribuições na fonte integral. Os capítulos, apêndices e notas estão mapeados em `references/fontes-e-fidelidade.md`.

## Instalação

Extraia o ZIP na pasta de skills do agente. No Codex para Windows, a instalação local utilizada é `C:\Users\filip\.codex\skills\estudo-biblico-indutivo`.

```powershell
Expand-Archive -LiteralPath 'packages\sermoes-pregacao\estudo-biblico-indutivo.zip' -DestinationPath 'C:\Users\filip\.codex\skills' -Force
```

Mantenha a árvore inteira do pacote, incluindo `references/fontes/`, para preservar os links e o acesso ao livro.

## Exemplos de uso

```text
Use $estudo-biblico-indutivo para estudar João 15:1–17
de forma completa para um grupo de adultos. Identifique a tradução,
justifique as interpretações e aplicações e cite as fontes consultadas.
```

```text
Use $estudo-biblico-indutivo para levantar a carta de Filipenses
como um todo e depois estudar cada unidade. Mantenha um registro
de cobertura para distinguir o que já foi estudado do que falta.
```

```text
Revise este estudo com $estudo-biblico-indutivo. Verifique contexto,
gênero, premissas, inferências, alternativas e a passagem do sentido
original à aplicação atual.
```

## Fonte e rastreabilidade

David R. Bauer e Robert A. Traina. *Inductive Bible Study: A Comprehensive Guide to the Practice of Hermeneutics*. Baker Academic, 2011; edição eletrônica criada em 2012. ISBN 978-1-4412-1451-5.

O EPUB foi fornecido pelo usuário e incluído a seu pedido. O nome foi simplificado para `inductive-bible-study-bauer-traina.epub`, preservando o conteúdo integral. Tamanho: 2.978.861 bytes. SHA-256: `6955c9959ae8e2453f498eb9bc04decad8b9f3a8e6d3c22710d6d448034c2d30`.

A elaboração cobriu vinte capítulos, seis apêndices, introduções, notas e diagramas pertinentes. A skill é uma síntese operacional original: mantém as distinções e os critérios da metodologia, sem transformar posições dos exemplos exegéticos em respostas obrigatórias.

## Verificação e limites

Foram verificados metadados, links, integridade do EPUB e do ZIP e correspondência entre repositório e instalação. Os testes locais incluem estudos preenchidos de Filipenses 4:13 e Salmo 1 e cenários sobre prosperidade automática, falas de personagens, etimologia e adaptação a um devocional breve.

Esses testes usaram recursos deliberadamente restritos. Não certificam toda exegese futura nem substituem pesquisa de texto original, variantes, comentários ou contexto histórico. A skill exige que cada execução declare o que realmente leu e consultou, apresente evidências e identifique suas pendências.
