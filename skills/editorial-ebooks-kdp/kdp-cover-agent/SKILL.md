---
name: kdp-cover-agent
description: Skill independente para criar, refinar e compor capas de ebooks KDP de nao ficcao em workspaces locais, salvando os JPGs finais em `C:\Users\filip\DEV\capas`. Use quando o pedido envolver capa de ebook, capa KDP, `16_capa_prompt.md`, refacao de capas, autor fixo `Filipe Ivo Pereira`, ou quando a capa precisar sair do `kdp-notion-agent` e virar um pipeline separado.
---

# KDP Cover Agent

## Overview

Use esta skill para tratar capa como fluxo independente. Ela prepara o briefing da capa a partir do workspace do ebook, gera o prompt para a imagem aqui na conversa, aplica a tipografia localmente e salva a capa final em `C:\Users\filip\DEV\capas`.

Esta skill nao chama `images.generate` nem `responses.create` da API. A geracao acontece aqui comigo, na conversa, usando a ferramenta de imagem embutida. O contrato operacional segue a documentacao de GPT Image / `gpt-image-2`: iteracao conversacional, arte sem texto, fundo opaco, tamanho valido e JPEG final.

Esta skill parte de uma premissa editorial fixa: nossas capas sao sempre de nao ficcao. Nao use este fluxo para ficcao.

Tres contratos sao fixos nesta skill:

- o nome do autor final e sempre `Filipe Ivo Pereira`
- toda capa e tratada como capa de nao ficcao
- a direcao visual deve buscar linguagem de best sellers da categoria, com foco comercial real

## Quando usar

- quando o ebook ja foi gerado e falta a capa
- quando voce quiser refazer capas antigas sem tocar no pipeline editorial
- quando a capa precisar de iteracoes visuais aqui na conversa
- quando o arquivo final precisar ficar centralizado na pasta `C:\Users\filip\DEV\capas`

## Workflow

### 1. Preparar o briefing da capa

Leia [references/gpt-image-2-operating-rules.md](references/gpt-image-2-operating-rules.md), [references/cover-design-playbook.md](references/cover-design-playbook.md) e [references/non-fiction-bestseller-cover-principles.md](references/non-fiction-bestseller-cover-principles.md).

Depois gere o prompt operacional:

```powershell
python "C:\Users\filip\.Codex\skills\kdp-cover-agent\scripts\run_cover_agent.py" prepare --workspace "<workspace>"
```

O comando le:

- `09_metadata_kdp.json`
- `06_ebook.md`
- `manifest.json`

E gera:

- `16_capa_prompt.md`
- caminho final esperado em `C:\Users\filip\DEV\capas\<Titulo do Ebook> - Capa.jpg`

### 2. Gerar a arte aqui na conversa

Use o texto de `16_capa_prompt.md` como base.

Regras fixas:

- gerar a imagem aqui comigo, nao por API
- pedir arte de fundo, nao texto final
- tratar a geracao como `digital-first`
- usar resolucao operacional `1536x2208`, que respeita as constraints do fluxo `gpt-image-2`
- manter fundo opaco
- se a primeira tentativa nao ficar boa, editar a imagem anterior na propria conversa

### 3. Importar e compor a capa final

Depois de gerar a arte na conversa, importe a imagem mais recente:

```powershell
python "C:\Users\filip\.Codex\skills\kdp-cover-agent\scripts\run_cover_agent.py" import-generated --workspace "<workspace>"
```

Esse passo:

- localiza a imagem mais recente em `$CODEX_HOME/generated_images`
- ajusta a arte para `1536x2208`
- aplica a tipografia localmente
- salva em JPEG
- cria `C:\Users\filip\DEV\capas` se a pasta ainda nao existir
- garante arquivo com ate `5 MB`

Contrato tipografico:

- titulo em CAIXA ALTA
- subtitulo com a primeira letra maiuscula
- autor sempre `Filipe Ivo Pereira` na parte inferior, mesmo se o metadata trouxer outro nome

## Regras editoriais e tecnicas

- a imagem gerada deve evitar qualquer texto renderizado pelo modelo
- a tipografia final sempre e aplicada localmente no import
- a capa deve se comportar como capa de nao ficcao que vende: promessa clara, categoria clara e transformacao percebida
- a skill assume nao ficcao sempre; nao precisa decidir entre ficcao e nao ficcao
- a capa precisa comunicar categoria e promessa em thumbnail
- a capa deve parecer best seller da categoria, nao experimento artistico sem mercado
- titulo e subtitulo precisam concentrar a hierarquia visual da capa
- priorize 1 foco visual dominante
- respeite a regra `60/25/15`
- use contraste forte e espaco negativo real
- nao use fundo transparente

## Comandos

```powershell
python "C:\Users\filip\.Codex\skills\kdp-cover-agent\scripts\run_cover_agent.py" prepare --workspace "<workspace>"
python "C:\Users\filip\.Codex\skills\kdp-cover-agent\scripts\run_cover_agent.py" import-generated --workspace "<workspace>"
python "C:\Users\filip\.Codex\skills\kdp-cover-agent\scripts\run_cover_agent.py" healthcheck
```

## Notes

- a skill espera um workspace compativel com o padrao do `kdp-notion-agent`
- se `09_metadata_kdp.json` nao existir, ela usa o `#` principal de `06_ebook.md`
- a saida padrao sempre vai para `C:\Users\filip\DEV\capas`
- para testes ou override local, a skill aceita `KDP_COVER_OUTPUT_DIR`
- se o ambiente nao expuser selecao explicita de modelo na ferramenta de imagem, mantenha o fluxo guiado pelas regras operacionais do `gpt-image-2` em vez de chamar a API
