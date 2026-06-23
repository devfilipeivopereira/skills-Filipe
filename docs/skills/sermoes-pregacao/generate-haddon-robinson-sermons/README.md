# generate-haddon-robinson-sermons

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-haddon-robinson-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-haddon-robinson-sermons.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-haddon-robinson-sermons`
- Fonte original: `C:\Users\filip\.codex\skills\generate-haddon-robinson-sermons`
- Hash do `SKILL.md`: `79a12b4e3010889c991a59ab23ede7db43255ef41f0a8f0e7d43b21aa49a0f2e`

## Resumo

Generate sermon outlines and full expository sermon manuscripts using Haddon W. Robinson's Biblical Preaching methodology, including one Big Idea, exegesis to homiletics, purpose and outcomes, and the IDEA pattern of illustrate, defend, explain, and apply. Use when the user asks to create an expository sermon, preaching manuscript, sermon outline, passage-based sermon, or biblical preaching message based on a Bible text and wants the result shaped by Haddon Robinson, Biblical Preaching, Gordon-Conwell style expository preaching, or Big Idea preaching.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-haddon-robinson-sermons.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-haddon-robinson-sermons` |
| Skill name | `generate-haddon-robinson-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-haddon-robinson-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-haddon-robinson-sermons` |
| Arquivo principal | `skills/sermoes-pregacao/generate-haddon-robinson-sermons/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-haddon-robinson-sermons.zip` |
| Tamanho do zip | 13,1 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-haddon-robinson-sermons |
| `description` | Generate sermon outlines and full expository sermon manuscripts using Haddon W. Robinson's Biblical Preaching methodology, including one Big Idea, exegesis to homiletics, purpose and outcomes, and the IDEA pattern of illustrate, defend, explain, and apply. Use when the user asks to create an expository sermon, preaching manuscript, sermon outline, passage-based sermon, or biblical preaching message based on a Bible text and wants the result shaped by Haddon Robinson, Biblical Preaching, Gordon-Conwell style expository preaching, or Big Idea preaching. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 31,3 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 185 B |
| `references` | 1 | 3,7 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Haddon Robinson Sermons
-   Overview
-   Method Fidelity Rules
-   Workflow
-   Originality Requirement
-   Research Requirement
-   Preparation Rules
-   Output Contract
-   Document Delivery
-   Hybrid Environment Rules
-   Style Rules
-   Quality Check
-   Final Cleanup Rule
-   Final Output Override (MD Only)
-   Pergunta Inicial Obrigatoria (Escopo da Producao)

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/agents/openai.yaml` | 185 B |
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/references/haddon_robinson_method.md` | 3,7 KB |
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/scripts/config.json` | 462 B |
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-haddon-robinson-sermons/SKILL.md` | 10,8 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-haddon-robinson-sermons`
- `C:\Users\filip\.agents\skills\generate-haddon-robinson-sermons`
- `C:\Users\filip\.claude\skills\generate-haddon-robinson-sermons`
- `C:\Users\filip\.cursor\skills\generate-haddon-robinson-sermons`
- `C:\Users\filip\.windsurf\skills\generate-haddon-robinson-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-haddon-robinson-sermons
description: Generate sermon outlines and full expository sermon manuscripts using Haddon W. Robinson's Biblical Preaching methodology, including one Big Idea, exegesis to homiletics, purpose and outcomes, and the IDEA pattern of illustrate, defend, explain, and apply. Use when the user asks to create an expository sermon, preaching manuscript, sermon outline, passage-based sermon, or biblical preaching message based on a Bible text and wants the result shaped by Haddon Robinson, Biblical Preaching, Gordon-Conwell style expository preaching, or Big Idea preaching.
---

# Generate Haddon Robinson Sermons

## Overview

Generate expository sermons with Haddon Robinson's method: derive one biblical concept from serious study, translate it into a contemporary Big Idea, define purpose and expected outcomes, structure the sermon to serve that idea, and deliver it through the preacher's transformed personality. The default deliverable is a formatted Microsoft Word document.

Read [references/haddon_robinson_method.md](references/haddon_robinson_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for stages, language, tone, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Haddon Robinson into generic expository preaching. Preserve the exegetical idea, homiletical idea, purpose, outcomes, and the IDEA movement.
- If the user asks for Haddon Robinson, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical passage.
2. If the user did not provide a passage, ask for it directly.
3. If the user did not provide audience, context, or length, assume a general evangelical congregation and produce a complete expository sermon manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every sermon or message must be newly written for the current request.

- Do not reuse pre-existing sermon manuscripts, previous generated files, cached sermon bodies, or prior outputs as the draft source.
- Do not paraphrase or lightly adapt an older sermon and present it as new work.
- You may reuse the biblical reference, the requested theme, and verified research material, but the manuscript itself must be freshly composed.
- Preserve the distinctive style, structure, rhetoric, and methodology of this preacher skill while still producing original wording and movement for the present request.
- If the same user asks for the same biblical reference again, write a new sermon unless the user explicitly asks for revision of an earlier one.

## Research Requirement

Before drafting the sermon, browse the internet to gather fresh, relevant material connected to the biblical text, audience, and theme.

- Collect current illustrations, statistics, cultural references, historical details, ministry context, or recent events only when they genuinely strengthen the sermon.
- Prefer recent and reputable sources. Use primary sources whenever possible.
- Treat online material as support, not as the authority. Scripture and the target preaching methodology remain primary.
- Keep only the most useful researched material. Do not overload the sermon with internet findings.
- When a contemporary example, statistic, quotation, or factual claim materially shapes the sermon, keep the source link available for attribution if the user asks.
- If the request is time-sensitive or depends on current events, verify the information online before finalizing the manuscript.

## Preparation Rules

- Choose a complete unit of thought, not an isolated verse fragment.
- Wrestle with the text before consulting commentaries.
- Form the Exegetical Idea in subject plus complement form.
- Test the Exegetical Idea before translating it.
- Translate the Exegetical Idea into a present-tense Homiletical Idea or Big Idea.
- State the sermon purpose clearly.
- Define expected outcomes in cognitive, affective, and volitional terms.
- Choose the sermon structure that best serves the Big Idea:
  - deductive
  - inductive
  - semi-inductive
- Build every point as a logical subdivision of the Big Idea.
- Use the IDEA pattern throughout the body:
  - illustrate
  - defend
  - explain
  - apply
- Connect every imperative to the indicative of the Gospel.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The Exegetical Idea in past-tense technical language.
2. The Homiletical Idea or Big Idea in present-tense contemporary language.
3. The Subject and the Complement separately.
4. The sermon purpose.
5. The expected outcomes:
   - cognitive
   - affective
   - volitional
6. The chosen structure and why it best serves the passage and the listeners.

Then write the complete sermon manuscript.

The sermon must include:

1. Introduction
2. Body with points subordinated to the Big Idea
3. Conclusion

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Haddon_Robinson.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Haddon_Robinson.epub`.
- Deliver the final `.epub` path to the user alongside the `.docx` path.

- Only after the final `.docx` has been copied to `C:\Users\filip\.codex\skills\DOCS_Sermons` and the final `.epub` has been saved in `C:\Users\filip\.codex\skills\EPUB_SERMONS`, delete all contents inside [outputs/](outputs/) while preserving the `outputs` folder itself.

## Hybrid Environment Rules

- Keep the sermon-generation workflow portable between local and cloud environments.
- Put filesystem reads and writes behind `scripts/adapters.py`.
- Keep parsing, word-count enforcement, and `.docx` rendering in `scripts/core.py`.
- Keep defaults such as minimum words and document styles in `scripts/config.json`.
- Prefer relative or configurable paths over machine-specific absolute paths.
- Prefer [outputs/](outputs/) in this skill folder as the default writable destination.
- If the environment blocks writing to the user-requested workspace, fall back to [outputs/](outputs/) in this skill folder and report the final path clearly.

## Style Rules

- Keep the sermon governed by one Big Idea.
- Let the text control the sermon rather than using the text as decoration.
- Write as a transformed person, not as a detached information pipeline.
- Be concrete whenever possible by moving down the ladder of abstraction.
- Integrate illustration, defense, explanation, and application through the whole message.
- Make the introduction create need before naming the full idea.
- Make the conclusion land a verdict, not a vague reflection.
- Repeat the Big Idea at least three times in natural ways.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the passage is a complete thought unit.
- Verify the Exegetical Idea and Homiletical Idea are distinct where needed.
- Verify each point is truly subordinate to the Big Idea.
- Verify the purpose is specific and not generic.
- Verify the body uses IDEA beyond explanation alone.
- Verify applications trace imperatives back to Gospel indicatives.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` has been delivered to `C:\Users\filip\.codex\skills\DOCS_Sermons\<Referencia_Biblica>\` and the final `.epub` has been delivered to `C:\Users\filip\.codex\skills\EPUB_SERMONS\<Referencia_Biblica>\`, the local `outputs/` folder for this skill must be emptied completely while preserving the folder itself.

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
```
