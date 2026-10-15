# Skills Filipe

Biblioteca organizada de skills locais encontradas nas pastas de IAs do notebook, atualizada em 2026-10-15.

## O que tem aqui

- skills/: copia organizada das skills instalaveis, separadas por categoria.
- packages/: um .zip individual por skill para instalacao manual.
- docs/CATALOGO.md: catalogo navegavel com nome, categoria, origem e pacote.
- docs/INDICE_DETALHADO.md: indice mestre com links para a ficha completa de cada skill.
- docs/skills/: documentacao detalhada individual de cada skill.
- docs/FONTES.md: fontes escaneadas e estrategia de deduplicacao.
- docs/manifest.json e docs/manifest.csv: inventario estruturado.
- docs/skill-docs.csv: indice estruturado das paginas de documentacao individual.
- scripts/organize-skills.ps1: script para regenerar tudo.
- scripts/generate-skill-docs.ps1: script para regenerar a documentacao detalhada.
- Tokens conhecidos sao redigidos durante a copia para evitar publicar secrets acidentais.

## Resumo por categoria

| Categoria | Skills |
|---|---:|
| academia-nature | 8 |
| desenvolvimento-devops | 5 |
| design-figma-frontend | 10 |
| documentos-dados-midia | 2 |
| editorial-ebooks-kdp | 11 |
| notion-produtividade | 14 |
| palestras-motivacao | 34 |
| sermoes-pregacao | 63 |
| sistema-agentes | 24 |


## Sermão de 1 Ponto (Andy Stanley-Talbot Davis)

A skill `sermao-de-1-ponto-andy-stanley-talbot-davis` cria, reescreve e audita sermões bíblicos de uma ideia central. Ela mantém o mapa EU–NÓS–DEUS–VOCÊS–NÓS de Andy Stanley e Lane Jones e acrescenta os aprofundamentos de Talbot Davis para exegese, jornada de descoberta, escrita oral, séries, internalização, funerais e centralidade de Cristo. Cada criação apresenta cinco alternativas de bottom line e cinco de frase-refrão, usa história, ilustração e analogia e termina em uma aplicação focal.

- Skill: `skills/sermoes-pregacao/sermao-de-1-ponto-andy-stanley-talbot-davis`
- Pacote instalável: `packages/sermoes-pregacao/sermao-de-1-ponto-andy-stanley-talbot-davis.zip`
- Documentação: `docs/skills/sermoes-pregacao/sermao-de-1-ponto-andy-stanley-talbot-davis/README.md`

## Sermões segundo Talbot Davis

A skill `sermao-talbot-davis` aplica a metodologia dos nove capítulos de *Simplify the Message, Multiply the Impact*. Organiza a mensagem em Engage–Encounter–Empower, com descoberta exegética, frase central como refrão, aplicações concretas e proclamação de Cristo. Inclui orientações para séries, internalização e funerais, distinguindo princípios do autor e adaptações operacionais.

- [Skill](skills/sermoes-pregacao/sermao-talbot-davis/SKILL.md)
- [Pacote instalável](packages/sermoes-pregacao/sermao-talbot-davis.zip)
- [Documentação](docs/skills/sermoes-pregacao/sermao-talbot-davis/README.md)

## Estudo Bíblico Indutivo — Bauer e Traina

A skill `estudo-biblico-indutivo` conduz o estudo de passagens e livros pelo método de David R. Bauer e Robert A. Traina. Inclui sete referências operacionais, modelo de relatório, critérios de revisão e o EPUB integral de referência dentro da pasta da skill e do ZIP instalável.

- [Skill](skills/sermoes-pregacao/estudo-biblico-indutivo/SKILL.md)
- [Documentação](docs/skills/sermoes-pregacao/estudo-biblico-indutivo/README.md)
- [Pacote com EPUB](packages/sermoes-pregacao/estudo-biblico-indutivo.zip)
- [Livro de referência](skills/sermoes-pregacao/estudo-biblico-indutivo/references/fontes/inductive-bible-study-bauer-traina.epub)

## Como regenerar

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/organize-skills.ps1 -Clean
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/generate-skill-docs.ps1 -Clean
```

## Documentacao

- Indice detalhado: `docs/INDICE_DETALHADO.md`
- Catalogo resumido: `docs/CATALOGO.md`
- Fichas individuais: `docs/skills/<categoria>/<skill>/README.md`

## Instalacao rapida

Escolha um pacote em `packages/<categoria>/<skill>.zip` e extraia em uma pasta de skills, por exemplo `C:\Users\filip\.codex\skills`.

Veja mais detalhes em `INSTALL.md`.
