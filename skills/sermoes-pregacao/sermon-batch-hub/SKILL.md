---
name: sermon-batch-hub
description: Generate sermon batches for the same biblical reference using one, several, or all installed preacher-style sermon skills. Use when the user wants the same passage preached in multiple styles, wants to choose one preacher from a hub, compare sermon manuscripts across preachers, or generate many sermons at once from the same biblical text.
---

# Sermon Batch Hub

Use this skill as the entry point when the user wants one, some, or all preacher methodologies for the same biblical reference.

## Purpose

This hub does not replace the preacher skills. It selects the right installed sermon skills and orchestrates them in batch.

Read [references/preacher_skill_map.md](references/preacher_skill_map.md) to resolve preacher names to installed skills.

Every sermon generated through this hub must be newly written for the current request. Do not reuse pre-existing sermon manuscripts, prior generated files, cached sermon bodies, or old batch outputs as source content.

## Fidelity Rules

- This hub is an orchestrator, not a preacher methodology of its own.
- For each selected preacher, the preacher skill's linked reference file is the governing specification derived from the Notion methodology source.
- The hub must not standardize away preacher differences for the sake of convenience or speed.
- Shared research may overlap, but structure, rhetoric, sequencing, and delivery logic must remain preacher-specific.
- If a preacher skill and its reference file differ, the reference file wins for that preacher run.

## Activation Workflow

When this skill is triggered, determine these inputs first:

1. The biblical reference.
2. Which preachers to use:
   - one
   - some
   - all
3. Audience or ministry context.
4. Language.
5. Target length, if the user wants something other than the default full manuscript.

If the user does not specify audience, assume a general evangelical congregation.
If the user does not specify language, default to Brazilian Portuguese.
If the user does not specify length, default to a full sermon manuscript in each selected style.

## Research Requirement

Before orchestrating the batch, browse the internet to gather fresh and relevant material for the shared biblical reference and audience.

- Collect current illustrations, statistics, cultural references, historical details, ministry context, or recent events that could strengthen one or more preacher versions.
- Prefer recent and reputable sources. Use primary sources whenever possible.
- Share the same verified factual base across the batch when it helps consistency, then let each preacher skill adapt that material to its own method.
- Treat online material as support, not as the authority. Scripture and each preacher methodology remain primary.
- Keep source links available in case the user asks for attribution or verification.
- Do not reuse previously generated sermon text from other skills or earlier runs. Research may inform the sermon, but each manuscript must be freshly composed.

## Selection Rules

- If the user names one preacher, use only that preacher's installed sermon skill.
- If the user names multiple preachers, use only those preacher skills.
- If the user says `todos`, `all`, `lote`, or asks for comparison across preachers, use all installed `generate-*-sermons` skills listed in the map.
- Do not include `generate-high-impact-preaching-series` in sermon batches.
- Do not include `prepare-bob-smiley-messages` unless the user explicitly asks for Bob Smiley in the batch.

## Orchestration Rules

For each selected preacher:

1. Open that preacher skill's `SKILL.md`.
2. Open the linked reference file for that preacher when needed and follow its non-negotiables exactly.
3. Follow that skill's workflow exactly.
4. Reuse the same biblical reference, audience, context, and language across the entire batch unless the user explicitly requests variation.
5. Generate a new sermon manuscript from scratch for that preacher. Do not paraphrase, remix, translate, summarize, or lightly edit an existing sermon file.
6. Preserve that preacher skill's own style, structure, rhetoric, methodology, and delivery logic. Similar reference does not justify homogenizing the outputs.
7. Let the preacher skill save its own `.md`, `.docx`, and `.epub` according to its own delivery rules.
8. Keep the filename reference identical across the batch except for the preacher segment.

## Centralized File Flow

The hub must assume and preserve this final storage contract for every selected preacher skill:

1. Temporary source files may be created inside that skill's local `outputs/` folder.
2. The final `.docx` must be placed in `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\`.
3. The final `.epub` must be placed in `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`.
4. The filename must follow `Referencia_Biblica_Pregador`.
5. After the `.docx` and `.epub` are successfully delivered, the selected preacher skill should leave its local `outputs/` folder empty, preserving only the folder itself.
6. After the batch finishes, the hub must generate a spreadsheet summary inside `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` by running [scripts/create_batch_spreadsheet.py](scripts/create_batch_spreadsheet.py).
7. The spreadsheet base filename should be ASCII-safe, for example `batch_summary`, `joao_9_resumo_pregadores`, or another stable slug chosen by the orchestrator.

Do not route final batch outputs to per-skill `DOCS_Sermons` or `EPUB_SERMONS` folders. The final delivery location is always the central skills directory.

## Output Rules

After batch generation, report:

1. Which preachers were used.
2. Which sermon skill produced each manuscript.
3. The final `.docx` path for each preacher.
4. The final `.epub` path for each preacher.
5. The final spreadsheet `.csv` path.
6. The final spreadsheet `.xlsx` path when available.
7. Any preacher that was skipped and why.

When possible, report the centralized final paths under `DOCS_Sermons\<Referencia_Biblica>\` and `EPUB_SERMONS\<Referencia_Biblica>\`, not temporary working paths.

Use a compact grouped summary, one preacher per line when possible.

When useful, explicitly note that the batch was generated as fresh material for this request.

## Spreadsheet Contract

The hub spreadsheet is part of the batch deliverable, not an optional extra.

- Generate both `.csv` and `.xlsx` when the environment supports `openpyxl`.
- Always include these columns in the spreadsheet:
  - `Pregador`
  - `Skill`
  - `Titulo`
  - `Tese_Central`
  - `Recurso_Distintivo`
  - `Min_Palavras`
  - `Total_Palavras`
  - `DOCX`
  - `EPUB`
- `Total_Palavras` must be counted from the delivered final `.docx`, not from an earlier draft or estimate.
- If the orchestrator has preacher metadata such as sermon title, thesis, or distinctive resource, write a JSON row file and pass it to `scripts/create_batch_spreadsheet.py` via `--rows-json`.
- If preacher metadata is unavailable, still generate the spreadsheet from the centralized output folders so the batch at least reports preacher names, word counts, and final file paths.

## Installed Skill Policy

- Prefer only installed local preacher skills from the map.
- If a requested preacher is not installed, say so briefly and continue with the remaining ones.
- If the user asks for `all`, skip missing preacher skills silently unless the omission matters.

## Originality Rules

- Never treat a prior generated sermon as a template body for a new batch run.
- Never collapse multiple preachers into one blended draft and rename the outputs.
- Shared facts, historical context, and online research may overlap across the batch, but the actual manuscript language, structure, and movement must be newly generated per preacher.
- If the user asks for one preacher, some preachers, or all preachers on the same reference, produce distinct manuscripts that still feel faithful to each preacher's method.

## Default Batch Order

Use this order unless the user requests a specific order:

1. Rick Warren
2. John MacArthur
3. Steven Furtick
4. Michael Todd
5. Andy Stanley
6. Timothy Keller
7. Craig Groeschel
8. John Stott
9. Haddon Robinson
10. Calvin Miller
11. Eugene Lowry
12. Fred Craddock
13. Paul Scott Wilson
14. Rick Blackwood
15. T.D. Jakes
16. Joyce Meyer
17. Joel Osteen
18. Louie Giglio
19. Lane Sebring
20. Brian Jones
21. Alyce McKenzie
22. Ed Young Jr.
23. Sticky Sermons
24. Integrated Sermons

## Quick Examples

- `Use $sermon-batch-hub para gerar um sermao em Joao 9 com Rick Warren, John MacArthur e Steven Furtick.`
- `Use $sermon-batch-hub para gerar em lote todos os pregadores para Romanos 8:1-11.`
- `Use $sermon-batch-hub para comparar Joao 9 em Rick Warren versus Timothy Keller.`

## Final Output Override (MD Only)

- Esta skill deve entregar exatamente um unico arquivo final `.md`.
- Nao gerar `.docx`, `.epub`, `.pdf`, `.csv`, `.xlsx` ou qualquer outro artefato final.
- Salvar o arquivo final `.md` em `C:\Users\filip\Dropbox\Obsidian_Filipe\Ministério\Sermões\Skill_Revisar`.
- Entregar ao usuario apenas o caminho absoluto desse `.md` salvo.
- Se qualquer instrucao deste arquivo conflitar com esta secao, esta secao prevalece.

## Pergunta Inicial Obrigatoria (Escopo da Producao)

Antes de iniciar qualquer producao, esta skill deve sempre perguntar ao usuario:

`Voce quer apenas o esboco ou a versao completa (sermao/palestra)?`

Opcoes e regras:

- `Esboco`: gerar somente a estrutura (titulo, tese central, pontos principais, transicoes, aplicacoes e conclusao resumida), sem manuscrito completo.
- `Completa`: gerar o manuscrito completo.
- Se a resposta nao estiver clara, pausar e pedir confirmacao antes de escrever.
- Esta pergunta e obrigatoria e deve acontecer antes de qualquer etapa de redacao.
- Em fluxos em lote, fazer a pergunta uma vez no inicio e aplicar a resposta a todos os itens, salvo instrucao contraria do usuario.

