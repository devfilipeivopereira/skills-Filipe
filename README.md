# Skills Filipe

Biblioteca organizada de skills locais encontradas nas pastas de IAs do notebook em 2026-06-23T12:12:36.0916036-03:00.

## O que tem aqui

- skills/: copia organizada das skills instalaveis, separadas por categoria.
- packages/: um .zip individual por skill para instalacao manual.
- docs/CATALOGO.md: catalogo navegavel com nome, categoria, origem e pacote.
- docs/FONTES.md: fontes escaneadas e estrategia de deduplicacao.
- docs/manifest.json e docs/manifest.csv: inventario estruturado.
- scripts/organize-skills.ps1: script para regenerar tudo.
- Tokens conhecidos sao redigidos durante a copia para evitar publicar secrets acidentais.

## Resumo por categoria

| Categoria | Skills |
|---|---:|
| academia-nature | 8 |
| desenvolvimento-devops | 5 |
| design-figma-frontend | 10 |
| documentos-dados-midia | 2 |
| editorial-ebooks-kdp | 10 |
| notion-produtividade | 14 |
| palestras-motivacao | 34 |
| sermoes-pregacao | 60 |
| sistema-agentes | 24 |

## Como regenerar

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/organize-skills.ps1 -Clean
```

## Instalacao rapida

Escolha um pacote em `packages/<categoria>/<skill>.zip` e extraia em uma pasta de skills, por exemplo `C:\Users\filip\.codex\skills`.

Veja mais detalhes em `INSTALL.md`.

