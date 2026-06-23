# KDP Notion Agent

Agente editorial ponta a ponta para transformar sermões transcritos no Notion em ebooks KDP com padrão editorial alto em PT-BR, mantendo fidelidade ao conteúdo original e publicando o pacote final no Notion como `Rascunho revisável`.

## O que este agente faz

- lê `Corrigido` ou `Transcrições` de uma página do Notion como fonte editorial inicial
- prepara o workspace do caso
- trata a transcrição como fonte editorial, não como texto já pronto
- organiza artefatos intermediários para resumo, blueprint, crítica e ebook
- renderiza `.docx` com padrão fixo para Kindle Create
- publica ebook, bônus e metadados de volta no Notion

## Princípios editoriais

- fidelidade ao sermão original
- zero divagação para temas paralelos
- expansão apenas por desdobramento legítimo do conteúdo-base
- PT-BR natural, pastoral, claro e memorável
- qualidade editorial antes de volume

## Arquitetura

O projeto separa duas camadas:

- `cognitiva`: correção da transcrição, delimitação do sermão, resumo, blueprint, escrita, crítica e reescrita
- `determinística`: integração com Notion, validação do pacote, renderização DOCX e upload

## Estrutura do projeto

```text
kdp-notion-agent/
  agents/
    openai.yaml
  references/
    artifact-spec.md
    cta-subagent-spec.md
    master-conformity-checklist.md
    model-routing-policy.json
    model-routing.md
    quality-gates.md
    sermon-to-book-playbook.md
    token-optimization-playbook.md
    transcription-editorial-guidelines.md
  scripts/
    contracts.py
    docx_renderer.py
    notion_client.py
    package_builder.py
    run_agent.py
  SKILL.md
  README.md
  requirements.txt
  config.example.json
```

## Requisitos

- Python 3.11+
- acesso ao banco do Notion
- ambiente Codex para execução cognitiva das etapas editoriais

Instalação local:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuração

Use variáveis de ambiente:

```powershell
$env:NOTION_TOKEN="seu_token"
$env:NOTION_DATABASE_ID="seu_database_id"
```

Ou crie um arquivo local não versionado chamado `config.local.json` a partir de `config.example.json`.

## Como usar

### Modo natural no Codex

Você pode pedir em linguagem natural:

- `gere o ebook do sermão Superando a impulsividade no Notion`
- `rode o agente completo para esta página do Notion`
- `processe os próximos sermões sem ebook no banco`

### Modo script por etapas

Preparar workspace:

```powershell
python ".\scripts\run_agent.py" pull --page-id "<PAGE_ID>" --profile premium
```

Selecionar automaticamente o próximo sermão elegível:

```powershell
python ".\scripts\run_agent.py" pull-next --profile premium
```

Filtrar por título:

```powershell
python ".\scripts\run_agent.py" pull-next --title-contains "finanças"
```

Regra de fonte editorial:

- `Corrigido` tem prioridade quando existir
- `Transcrições` pode ser usada automaticamente para sermões anteriores a `2024-10-01`
- o mínimo de `15.000` palavras é exigido do ebook final, não do texto-fonte
- `pull-next` escolhe o próximo sermão elegível ignorando itens já processados
- para “novo ebook”, `pull-next` também ignora workspaces locais já preparados

Validar:

```powershell
python ".\scripts\run_agent.py" validate --workspace "<WORKSPACE>"
```

Gerar estratégia curta por etapa:

```powershell
python ".\scripts\run_agent.py" prepare-stage-strategy --workspace "<WORKSPACE>"
```

Gerar roteamento automático de modelo:

```powershell
python ".\scripts\run_agent.py" prepare-model-routing --workspace "<WORKSPACE>" --profile premium
```

Gerar o plano operacional do Codex com subagentes por etapa:

```powershell
python ".\scripts\run_agent.py" prepare-codex-orchestration --workspace "<WORKSPACE>" --profile premium
```

Gerar packet de capítulo:

```powershell
python ".\scripts\run_agent.py" prepare-chapter-packet --workspace "<WORKSPACE>" --chapter "Capítulo 4"
```

Gerar job operacional da etapa:

```powershell
python ".\scripts\run_agent.py" run-editorial-stage --workspace "<WORKSPACE>" --stage "chapter_writing" --chapter "Capítulo 4" --profile premium
```

Enviar feedback para reexecução apenas da etapa atual:

```powershell
python ".\scripts\run_agent.py" run-editorial-stage --workspace "<WORKSPACE>" --stage "book_blueprint" --feedback "A tese central ficou ampla; foque no eixo do capítulo base."
```

Regra fixa no Codex:

- o agente principal funciona como orquestrador
- cada etapa editorial roda via subagente
- o subagente usa o modelo fixo definido em `references/model-routing-policy.json`
- `prefácio`, `introdução` e `conclusão` são tratados por último na etapa `framing_sections`
- `prefácio`, `introdução` e `conclusão` devem ter mais de 500 palavras cada
- a execução consolidada do caso pode ser inspecionada em `15_codex_orchestration.json`

Preparar e consolidar subagente de CTA:

```powershell
python ".\scripts\run_agent.py" prepare-cta-subagent --workspace "<WORKSPACE>"
python ".\scripts\run_agent.py" consolidate-cta-subagent --workspace "<WORKSPACE>"
```

Renderizar:

```powershell
python ".\scripts\run_agent.py" render --workspace "<WORKSPACE>"
```

Publicar no Notion:

```powershell
python ".\scripts\run_agent.py" push --workspace "<WORKSPACE>"
```

## Profiles e checkpoints

- `premium` (padrão): maior profundidade de raciocínio e mais ciclos de feedback
- `economico`: menor custo com gates mínimos preservados
- checkpoints por etapa:
  - `approve`: `transcription_correction`, `book_blueprint`, `framing_sections`, `final_critique`
  - `select`: `cta_subagent`
  - `skip`: `chapter_writing`, `chapter_revision`, `metadata_kdp`, `landing_page`, `bonus_asset`

## Observabilidade de runs

Cada execução usa `run_id` e salva em `runs/<run_id>/`:

- `state.json`: status, etapa atual, início/fim, erro, profile e IA agente
- `events.jsonl`: eventos (`stage_started`, `stage_completed`, `checkpoint_waiting`, `checkpoint_feedback`, `run_failed`, `run_completed`)

Listar histórico:

```powershell
python ".\scripts\run_agent.py" runs --workspace-root "C:\Users\filip\Downloads\kdp-agent" --limit 20
```

## Governança e sync

Validar saúde do agente:

```powershell
python ".\scripts\run_agent.py" healthcheck
```

Sincronizar para instalações locais (`.codex`, `.claude`, `.gemini`, `.cursor`, `.windsurf`) com relatório e hashes:

```powershell
python ".\scripts\run_agent.py" sync-skills
```

Rollback para o último backup:

```powershell
python ".\scripts\run_agent.py" rollback-sync
```

Rollback para backup específico:

```powershell
python ".\scripts\run_agent.py" rollback-sync --backup-id "<YYYYMMDD-HHMMSS>"
```

## Padrão fixo do DOCX

- página 1 com título
- página 2 com copyright
- página 3 com sumário automático do Word (TOC) baseado em Títulos 1-3
- prefácio, corpo do livro e página final de `Sobre o Autor`
- capítulos devem seguir o padrão `Capítulo N: Nome do Capítulo`
- frases de efeito entre capítulos principais
- cada frase de efeito deve ter no máximo 200 caracteres
- não incluir apêndice, bônus, guias, devocionais ou desafios no ebook
- as 15k palavras são exclusivas do ebook; não inflar com listas ou materiais paralelos
- letra capitular no primeiro parágrafo de cada capítulo principal `##`
- sem letra capitular em prefácio, introdução e `Sobre o Autor`
- entrelinha `1,25`
- recuo da primeira linha em `8 mm`
- fonte preta em todo o documento
- subtítulos `###` renderizados como subtítulos reais de Word
- subtítulos com espaçamento `2,00` e respiro consistente antes/depois
- `www.filipeivopereira.com` como hyperlink real

## Artefatos gerados

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

## Uploads esperados no Notion

- `Corrigido`
- `Ebook_HTML`
- `Bonus_PDF`
- `Nome_Ebook`
- `Data_Criacao`
- `Palavras_Ebook`
- `Landing_HTML`
- `Metadata_KDP`
- `Relatorio_CTA`
- `Resumo_Sermao`
- `Blueprint_Ebook`
- `Relatorio_Editorial`
- `Score_Qualidade`
- `Falhas_QA`
- `IA Agente`
- `Status`

## Regra de concorrência multi-IA

- o agente garante a coluna `Status` no banco do Notion
- quando uma IA inicia um caso (`pull` ou `pull-next`), o item é marcado como `Executando`
- itens com `Status = Executando` ou `Status = Pronto` não são elegíveis para novo `pull-next`
- ao finalizar o `push`, o item é marcado como `Pronto`

## Qualidade e governança

As regras obrigatórias estão em:

- [SKILL.md](./SKILL.md)
- [references/artifact-spec.md](./references/artifact-spec.md)
- [references/master-conformity-checklist.md](./references/master-conformity-checklist.md)
- [references/quality-gates.md](./references/quality-gates.md)

## Segurança

- não versione `config.local.json`
- não publique tokens do Notion
- mantenha o repositório privado se o fluxo, os prompts ou a integração forem sensíveis

## Status

Este agente foi testado com fluxo real no Notion, incluindo geração de ebook com mais de 15 mil palavras, renderização DOCX e publicação de rascunho revisável.
