# Skills Filipe

Biblioteca organizada de skills locais encontradas nas pastas de IAs do notebook, atualizada em 2026-10-08.

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
| sermoes-pregacao | 61 |
| sistema-agentes | 24 |

## Romance adulto 30K para KDP

A skill `romance-adulto-30k` cria romances adultos originais em português brasileiro com exatamente 30.000 palavras de prosa ficcional e entrega EPUB 3 responsivo para Amazon KDP, capa JPEG incorporada e separada, metadados editoriais de Kang Arin e relatório de validação.

- Skill: `skills/editorial-ebooks-kdp/romance-adulto-30k`
- Pacote instalável: `packages/editorial-ebooks-kdp/romance-adulto-30k.zip`
- Documentação: `docs/skills/editorial-ebooks-kdp/romance-adulto-30k/README.md`

## Sermão de 1 Ponto (Andy Stanley-Talbot Davis)

A skill `sermao-de-1-ponto-andy-stanley-talbot-davis` cria, reescreve e audita sermões bíblicos de uma ideia central. Ela mantém o mapa EU–NÓS–DEUS–VOCÊS–NÓS de Andy Stanley e Lane Jones e acrescenta os aprofundamentos de Talbot Davis para exegese, jornada de descoberta, escrita oral, séries, internalização, funerais e centralidade de Cristo. Cada criação apresenta cinco alternativas de bottom line e cinco de frase-refrão, usa história, ilustração e analogia e termina em uma aplicação focal.

- Skill: `skills/sermoes-pregacao/sermao-de-1-ponto-andy-stanley-talbot-davis`
- Pacote instalável: `packages/sermoes-pregacao/sermao-de-1-ponto-andy-stanley-talbot-davis.zip`
- Documentação: `docs/skills/sermoes-pregacao/sermao-de-1-ponto-andy-stanley-talbot-davis/README.md`

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
