---
name: kdp-notion-agent
description: Agente editorial ponta a ponta para ler uma página do Notion com arquivo na coluna `Transcrições`, corrigir cognitivamente o sermão em pt-BR, isolar a mensagem útil, planejar e redigir um ebook KDP fiel ao conteúdo original, gerar artefatos auxiliares e salvar tudo no Notion como rascunho revisável. Use quando o usuário pedir para transformar sermões transcritos em ebooks, migrar ou substituir a skill `kdp-notion-publisher`, produzir `Corrigido` a partir de `Transcrições`, montar pacote KDP completo ou operar um fluxo editorial Notion para ebook com alto rigor de qualidade.
---

# KDP Notion Agent

## Overview

Use esta skill quando a origem do projeto for uma transcrição de sermão no Notion e o resultado esperado for um ebook KDP com acabamento real de livro, sem perder fidelidade à mensagem pregada.

Esta skill separa o trabalho em duas camadas:

- `cognitiva`: correção editorial da transcrição, delimitação do sermão, blueprint, redação, crítica e reescrita
- `determinística`: busca e upload no Notion, montagem `.docx`, validação e persistência dos artefatos

## Workflow

### 1. Preparar o caso no workspace

Use o script principal para baixar a página do Notion, escolher automaticamente a fonte editorial e criar a pasta de trabalho do caso:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" pull --page-id "<page_id>" --workspace-root "C:\Users\filip\Downloads\kdp-agent" --profile premium
```

Para selecionar automaticamente o próximo sermão elegível no banco e já preparar o caso:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" pull-next --workspace-root "C:\Users\filip\Downloads\kdp-agent" --profile premium
```

Opcionalmente, filtre pelo título:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" pull-next --title-contains "finanças"
```

O script cria:

- `01_raw_transcricao.txt`
- `02_corrigido.txt`
- `03_resumo_sermao.md`
- `04_blueprint_ebook.md`
- `05_relatorio_editorial.md`
- `06_ebook.md`
- `07_landing.html`
- `08_bonus.md`
- `09_metadata_kdp.json`
- `10_relatorio_cta.json`
- `11_cta_subagent.json`
- `12_cta_subagent_brief.md`
- `13_stage_strategy.md`
- `14_model_routing.json`
- `15_codex_orchestration.json`
- `manifest.json`

Regra de fonte editorial:

- priorizar `Corrigido` quando houver arquivo disponível
- permitir `Transcrições` como fonte automática para sermões anteriores a `2024-10-01`
- preencher `02_corrigido.txt` imediatamente quando a fonte escolhida já for `Corrigido`
- aplicar o mínimo de `15.000` palavras apenas ao ebook final em `06_ebook.md`, nunca ao texto-fonte
- o comando `pull-next` deve ignorar itens já processados e escolher o próximo sermão elegível pela própria regra da skill
- quando o pedido for “novo ebook”, `pull-next` também deve ignorar páginas que já tenham workspace local preparado no diretório alvo
- o agente deve garantir a coluna `Status` no Notion
- ao iniciar um caso (`pull` ou `pull-next`), deve marcar `Status = Executando`
- ao finalizar o `push`, deve marcar `Status = Pronto`
- páginas com `Status = Executando` ou `Status = Pronto` não podem ser escolhidas no `pull-next`

### 2. Corrigir a transcrição como agente

Leia [references/transcription-editorial-guidelines.md](references/transcription-editorial-guidelines.md) antes de editar `02_corrigido.txt`.

Regras centrais:

- corrigir ortografia, acentuação, pontuação e sintaxe
- unir frases quebradas artificialmente
- remover ruído de ASR e duplicações mecânicas
- preservar o sermão, sem inventar conteúdo novo
- manter o eixo temático original

O texto corrigido deve soar como uma transcrição humana de alta qualidade, não como ebook e nem como texto cru.

### 3. Delimitar o sermão e mapear a mensagem

Leia [references/sermon-to-book-playbook.md](references/sermon-to-book-playbook.md).
Leia tambem [references/persuasive-ebook-style-guide.md](references/persuasive-ebook-style-guide.md).

Preencha:

- `03_resumo_sermao.md` com tese central, texto-base, movimentos argumentativos e riscos de extrapolação
- `04_blueprint_ebook.md` com promessa do livro, público, sumário e função de cada capítulo
- `04_blueprint_ebook.md` deve auditar `titulo` e `subtitulo` com [references/title-positioning-playbook.md](references/title-positioning-playbook.md)

### 4. Redigir e criticar

Redija o livro em `06_ebook.md` e registre a crítica em `05_relatorio_editorial.md`.

Leia [references/quality-gates.md](references/quality-gates.md) antes de considerar o material pronto.
Leia [references/persuasive-ebook-style-guide.md](references/persuasive-ebook-style-guide.md) como contrato editorial obrigatorio.

Exigências:

- PT-BR natural, elegante e pastoral
- seguir obrigatoriamente a arquitetura, o tom, a voz, a logica persuasiva e a cadencia editorial da skill `generate-persuasive-ebooks`, especialmente no padrao dos modelos cristaos de referencia do usuario
- estrutura de livro, não de transcrição inchada
- expansão apenas por desdobramento legítimo do sermão
- conexão contínua com o texto bíblico de origem; o livro não pode soar como opinião autônoma do autor, mas como interação fiel e viva com a passagem base
- sempre que o contexto do argumento estiver explicando, fundamentando ou aplicando uma afirmação bíblica, citar o versículo completo em pt-BR NVI, em vez de apenas resumir a ideia do autor ou aludir vagamente ao texto
- no manuscrito markdown, todo texto bíblico citado integralmente deve vir em itálico com `*...*`; no `.docx` final, essas citações devem aparecer em itálico e em Times New Roman
- zero divagação para temas paralelos
- capítulos com função própria
- nenhuma menção direta ao sermão de origem: proibido usar "no sermão", "o sermão diz", "como foi pregado", "na pregação", "o pregador disse" ou qualquer expressão que revele que o conteúdo nasceu de uma transcrição; o leitor não sabe que existe um sermão e não precisa saber
- coesão e coerência contínua entre parágrafos: cada parágrafo deve nascer do anterior e preparar o seguinte por transição natural de ideia; proibido blocos independentes colados; a prosa deve fluir como livro, não como lista de pontos disfarçada de prosa; conectores mecânicos ("além disso", "por outro lado", "portanto") não substituem transição real de pensamento
- títulos de capítulos devem seguir `Capítulo N: Nome do Capítulo`
- prefácio, introdução e conclusão devem ser escritos por último, após os capítulos principais
- prefácio, introdução e conclusão devem ter mais de 500 palavras cada
- salvo limitação real do sermão, o blueprint e o manuscrito devem preferir a espinha dorsal da `generate-persuasive-ebooks`: introdução confessional, 8 capítulos, capítulo de crenças erradas, capítulo `O que a Bíblia realmente diz`, capítulo de framework prático, capítulo 7 com aplicação para membros/líderes/pastores e fechamento pastoral
- salvo limitacao real do sermao, a logica por capitulo deve ficar fixa: capitulo 1 identificacao + loop, capitulo 2 causa raiz + AHA, capitulo 3 virada de identidade + acao, capitulo 4 aprofundamento da nova lente, capitulo 5 `o que a Biblia realmente diz`, capitulo 6 framework numerado, capitulo 7 membros/lideres/pastores, capitulo 8 custo de continuar igual + convite implicito
- o `04_blueprint_ebook.md` deve registrar por capitulo: objetivo neuroemocional, crenca quebrada, dor latente, nova identidade ou lente, ancora biblica, trecho do sermao e transicao
- não incluir apêndice, bônus, guias, devocionais ou desafios no ebook
- as 15k palavras são exclusivas do ebook; não inflar com listas ou materiais paralelos
- o nome final do `.docx` principal e do bônus deve seguir o título editorial do ebook, priorizando `09_metadata_kdp.json.title` e, na falta dele, o `#` principal de `06_ebook.md`; o título original do caso no Notion vira apenas fallback
- reescrita obrigatória se qualquer gate falhar

### 4.1. Economizar tokens sem perder qualidade

Antes de escrever ou revisar, gere a estratégia curta do caso:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" prepare-stage-strategy --workspace "<workspace>"
```

Para escrever ou revisar um capítulo sem mandar o livro inteiro, gere um pacote enxuto:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" prepare-chapter-packet --workspace "<workspace>" --chapter "Capítulo 4"
```

Use esse pacote como contexto principal da rodada, junto com um checklist editorial curto.

Para o agente escolher o modelo da etapa automaticamente:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" prepare-model-routing --workspace "<workspace>" --profile premium
```

Para resolver uma etapa específica de forma autônoma:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" route-stage --workspace "<workspace>" --stage "chapter_writing" --chapter "Capítulo 4"
```

Leia [references/model-routing.md](references/model-routing.md) para a política de roteamento.

Para gerar um job operacional completo da etapa, já com modelo, contexto, instrução e saída esperada:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" run-editorial-stage --workspace "<workspace>" --stage "chapter_writing" --chapter "Capítulo 4" --profile premium
```

Esse comando cria um arquivo em `stage-runs/` para execução autônoma da etapa.

Quando houver feedback humano, a reexecução deve ocorrer apenas na etapa atual:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" run-editorial-stage --workspace "<workspace>" --stage "book_blueprint" --feedback "A tese ficou ampla, mantenha foco no tema principal."
```

Para preparar a orquestração completa do Codex com subagentes fixos por etapa:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" prepare-codex-orchestration --workspace "<workspace>" --profile premium
```

Regra fixa de execução no Codex:

- o agente principal atua apenas como orquestrador
- cada etapa editorial deve ser delegada a um subagente
- o subagente deve usar exatamente o `model` e o `reasoning_effort` definidos na policy
- o agente principal integra, valida e segue para a próxima etapa
- `prefácio`, `introdução` e `conclusão` devem ser concluídos na etapa `framing_sections`, depois da escrita/revisão dos capítulos
- o artefato `15_codex_orchestration.json` é o contrato operacional dessa delegação

### 5. Gerar os artefatos auxiliares

Preencha manualmente pelo agente:

- `07_landing.html`
- `08_bonus.md`
- `09_metadata_kdp.json`
- `10_relatorio_cta.json`

Siga [references/artifact-spec.md](references/artifact-spec.md) para formatos e limites.

### 5.1. Usar um subagente para curadoria de CTA

Quando a parte comercial precisar ficar mais coerente com o sermão, use um subagente dedicado logo após `04_blueprint_ebook.md`.

Antes de acionar o subagente, gere o briefing:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" prepare-cta-subagent --workspace "<workspace>"
```

Função do subagente:

- ler `03_resumo_sermao.md` e `04_blueprint_ebook.md`
- ler `12_cta_subagent_brief.md`
- sugerir apenas ofertas que nasçam do eixo temático do livro
- indicar âncoras curtas, discretas e naturais para hyperlinks no corpo do ebook
- apontar riscos de incoerência comercial

Regra de ouro:

- o subagente nunca escreve direto em `06_ebook.md`
- o subagente escreve somente em `11_cta_subagent.json`
- o agente principal valida, promove e consolida isso em `10_relatorio_cta.json`
- só depois disso os links são inseridos no ebook durante o `render`

Para consolidar a saída do subagente antes do render:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" consolidate-cta-subagent --workspace "<workspace>"
```

Leia [references/cta-subagent-spec.md](references/cta-subagent-spec.md) para o contrato completo do subagente.

### 6. Validar, renderizar e publicar rascunho

Validar o pacote:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" validate --workspace "<workspace>"
```

Gerar `.docx`:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" render --workspace "<workspace>"
```

Padrão fixo do `.docx`:

- entrelinha `1,25`
- recuo da primeira linha em `8 mm`
- fonte preta em todo o documento
- sumário automático do Word (TOC) usando Títulos 1, 2 e 3
- `###` renderizado como subtítulo real de Word
- letra capitular no primeiro parágrafo de cada capítulo principal `##`
- sem letra capitular em prefácio, introdução e `Sobre o Autor`
- subtítulos com espaçamento `2,00` e respiro consistente antes/depois no padrão do Word
- `www.filipeivopereira.com` como hyperlink real sempre que aparecer no arquivo final
- frases de efeito devem ser derivadas do capítulo anterior (não podem introduzir tema novo)
- cada frase de efeito deve condensar conflito humano, verdade espiritual, virada de perspectiva e chamado final
- frase de efeito deve sair entre aspas e com formatação de negrito + itálico
- frase de efeito deve ter no máximo 200 caracteres

Fazer upload para o Notion como rascunho revisável:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" push --workspace "<workspace>"
```

No `push`, o agente deve preencher automaticamente a coluna `IA Agente` no Notion com o runtime detectado (`codex`, `antigravity`, `claude`, `cursor` ou `windsurf`).

### Profiles, observabilidade e governança

- profile padrão: `premium`
- profile alternativo: `economico`
- checkpoints:
  - `approve`: `transcription_correction`, `book_blueprint`, `framing_sections`, `final_critique`
  - `select`: `cta_subagent`
  - `skip`: `chapter_writing`, `chapter_revision`, `metadata_kdp`, `landing_page`, `bonus_asset`
- cada run salva:
  - `runs/<run_id>/state.json`
  - `runs/<run_id>/events.jsonl`

Comandos operacionais:

```powershell
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" runs --workspace-root "C:\Users\filip\Downloads\kdp-agent" --limit 20
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" healthcheck
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" sync-skills
python "C:\Users\filip\DEV\Agente_Ebook\kdp-notion-agent\scripts\run_agent.py" rollback-sync
```

## Notes

- A skill aceita `NOTION_TOKEN` e `NOTION_DATABASE_ID` por variável de ambiente.
- Se as variáveis não estiverem definidas, o pipeline usa `config.local.json` na raiz da skill.
- Quando o material-fonte não sustentar um livro forte sem extrapolação, registre isso no relatório editorial e não force volume.
- O checklist mestre de conformidade está em [references/master-conformity-checklist.md](references/master-conformity-checklist.md).
