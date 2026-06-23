# generate-paul-scott-wilson-sermons

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-paul-scott-wilson-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-paul-scott-wilson-sermons.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons`
- Fonte original: `C:\Users\filip\.codex\skills\generate-paul-scott-wilson-sermons`
- Hash do `SKILL.md`: `2abdcf8859c19724a44636ecd38d546e28c60429e5a2545f058d551e3c923d80`

## Resumo

Generate sermon outlines and full sermon manuscripts using Paul Scott Wilson's Four Pages methodology, including the OCMAIM preparation process, a God-centered theme sentence, the four pages of problem in the text, problem in the world, grace in the text, and grace in the world, a dominant image, and grace-driven mission. Use when the user asks to create a sermon, preaching manuscript, sermon outline, grace-centered expository message, Four Pages sermon, law-and-gospel sermon, or Paul Scott Wilson style sermon based on a Bible text or theme.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-paul-scott-wilson-sermons.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-paul-scott-wilson-sermons` |
| Skill name | `generate-paul-scott-wilson-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-paul-scott-wilson-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons` |
| Arquivo principal | `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-paul-scott-wilson-sermons.zip` |
| Tamanho do zip | 13,3 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-paul-scott-wilson-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Paul Scott Wilson's Four Pages methodology, including the OCMAIM preparation process, a God-centered theme sentence, the four pages of problem in the text, problem in the world, grace in the text, and grace in the world, a dominant image, and grace-driven mission. Use when the user asks to create a sermon, preaching manuscript, sermon outline, grace-centered expository message, Four Pages sermon, law-and-gospel sermon, or Paul Scott Wilson style sermon based on a Bible text or theme. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 32,1 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 187 B |
| `references` | 1 | 4,3 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Paul Scott Wilson Sermons
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
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/agents/openai.yaml` | 187 B |
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/references/paul_scott_wilson_method.md` | 4,3 KB |
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/scripts/config.json` | 464 B |
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-paul-scott-wilson-sermons/SKILL.md` | 11,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-paul-scott-wilson-sermons`
- `C:\Users\filip\.agents\skills\generate-paul-scott-wilson-sermons`
- `C:\Users\filip\.claude\skills\generate-paul-scott-wilson-sermons`
- `C:\Users\filip\.cursor\skills\generate-paul-scott-wilson-sermons`
- `C:\Users\filip\.windsurf\skills\generate-paul-scott-wilson-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-paul-scott-wilson-sermons
description: Generate sermon outlines and full sermon manuscripts using Paul Scott Wilson's Four Pages methodology, including the OCMAIM preparation process, a God-centered theme sentence, the four pages of problem in the text, problem in the world, grace in the text, and grace in the world, a dominant image, and grace-driven mission. Use when the user asks to create a sermon, preaching manuscript, sermon outline, grace-centered expository message, Four Pages sermon, law-and-gospel sermon, or Paul Scott Wilson style sermon based on a Bible text or theme.
---

# Generate Paul Scott Wilson Sermons

## Overview

Generate sermons using Paul Scott Wilson's Four Pages method: complete the OCMAIM preparation work first, identify the trouble in the text and in the world, proclaim grace in the text and in the world, keep God as the active subject of the sermon, and make sure the sermon ends in grace rather than law. The default deliverable is a formatted Microsoft Word document.

Read [references/paul_scott_wilson_method.md](references/paul_scott_wilson_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, tone, transitions, and the grace-centered logic of the method.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Paul Scott Wilson into generic grace preaching. Preserve OCMAIM, the four pages, God as hero, the dominant image, and the grace-shaped mission ending.
- If the user asks for Paul Scott Wilson, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a general Christian congregation with real contemporary needs and produce a complete sermon manuscript.
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

- Complete the OCMAIM work before drafting any page of the sermon.
- Use one main biblical text as the central literary unit.
- Write one theme sentence with God as the grammatical subject and a strong verb of divine action.
- Identify one doctrine that undergirds the theme sentence.
- Identify one real congregational need that the theme sentence answers.
- Choose one dominant image rich enough to appear in all four pages under both trouble and grace.
- Define one mission response that flows from grace rather than guilt.
- Make sure the sermon follows law, law, grace, grace:
  - problem in the text
  - problem in the world
  - grace in the text
  - grace in the world
- Do not let application collapse back into duty at the end.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The central text and the literary unit it represents.
2. The full theme sentence.
3. The doctrine that supports the theme sentence.
4. The congregational need answered by the theme sentence.
5. The dominant image and how it connects to the text.
6. The concrete mission invited by the sermon.
7. The existential question the text answers from the listener's point of view.

Then write the sermon with these clearly signaled sections:

1. Introduction
2. Page 1: Problem in the Text
3. Page 2: Problem in the World
4. Page 3: Grace in the Text
5. Page 4: Grace in the World

Write the transitions between pages explicitly. Repeat the theme sentence at least four times across the manuscript. Weave the dominant image through all four pages with changing significance.

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Paul_Scott_Wilson.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Paul_Scott_Wilson.epub`.
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

- Keep God, not the human hearer, as the protagonist of the sermon.
- Make the problem concrete enough that grace feels like real news.
- Keep Page 1 in the biblical world and Page 2 in the contemporary world.
- Use proclamation, not mere explanation, especially in Pages 3 and 4.
- End with grace, hope, and divine action rather than a moralistic demand.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the OCMAIM section is complete before the sermon proper begins.
- Verify the theme sentence has God as subject and no conditional structure.
- Verify each of the four pages is distinct and in the correct theological role.
- Verify the dominant image appears in all four pages.
- Verify the mission flows from grace and not obligation.
- Verify the sermon ends in grace, not law.
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
