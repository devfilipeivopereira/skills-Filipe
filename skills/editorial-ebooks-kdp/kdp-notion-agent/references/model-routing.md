# Model Routing

## Objetivo

Permitir que o agente escolha autonomamente o melhor modelo e o nível de raciocínio para cada etapa do pipeline, sem intervenção manual do usuário.

## Como funciona

- a política base fica em `references/model-routing-policy.json`
- o agente gera uma versão aplicada ao caso em `14_model_routing.json`
- para uma etapa específica, o comando `route-stage` devolve:
  - `model`
  - `reasoning_effort`
  - `profile`
  - `checkpoint`
  - `max_feedback_cycles`
  - `context_files`
  - `execution_mode`
  - `justification`

## Regras

- etapas editoriais nobres usam modelo mais forte
- etapas de empacotamento usam modelo mais barato
- escrita e revisão trabalham por capítulo, com packet enxuto
- toda etapa editorial roda em `execution_mode = subagent`
- no Codex, o agente principal só orquestra e integra
- o contrato operacional completo dessa delegação deve ser salvo em `15_codex_orchestration.json`
- profile padrão é `premium`; se omitido no CLI, a skill usa esse profile automaticamente
- profile `economico` reduz `reasoning_effort` e ciclos de feedback, mantendo gates mínimos

## Política fixa atual

- `gpt-5.2-codex`: `transcription_correction`, `book_blueprint`, `chapter_writing`, `chapter_revision`, `framing_sections`, `final_critique`
- `gpt-5.2`: `sermon_summary`, `cta_subagent`, `metadata_kdp`, `landing_page`, `bonus_asset`
- `framing_sections` deve escrever `Prefácio`, `Introdução` e `Conclusão` somente no fim e com mais de 500 palavras cada

## Regra de execução no Codex

- abrir a sessão em qualquer modelo não muda a policy da skill
- a skill deve delegar cada etapa para um subagente com o modelo fixo daquela etapa
- o agente principal nunca deve executar localmente uma etapa que esteja marcada como `subagent`
- os jobs em `stage-runs/*.json` e o artefato `15_codex_orchestration.json` são a fonte de verdade para a delegação

## Etapas previstas

- `transcription_correction`
- `sermon_summary`
- `book_blueprint`
- `chapter_writing`
- `chapter_revision`
- `framing_sections`
- `final_critique`
- `cta_subagent`
- `metadata_kdp`
- `landing_page`
- `bonus_asset`
