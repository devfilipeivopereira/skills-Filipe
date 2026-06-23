# generate-rick-warren-sermons

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-rick-warren-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-rick-warren-sermons.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-rick-warren-sermons`
- Fonte original: `C:\Users\filip\.codex\skills\generate-rick-warren-sermons`
- Hash do `SKILL.md`: `931701a5fe2f96ff2f31f55754914f2c8043ccc7cca7f0166e8d78e36e4a4e8f`

## Resumo

Generate sermon outlines and full sermon manuscripts using Rick Warren's CRAFT methodology, Saddleback-style structure, and application-focused preaching principles. Use when the user asks to create a sermon, preaching manuscript, sermon outline, sermon series message, commitment prayer, or weekly homework based on a Bible text or theme and wants the result shaped by Rick Warren, Saddleback, CRAFT, purpose-driven preaching, or strong practical application.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-rick-warren-sermons.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-rick-warren-sermons` |
| Skill name | `generate-rick-warren-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-rick-warren-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-rick-warren-sermons` |
| Arquivo principal | `skills/sermoes-pregacao/generate-rick-warren-sermons/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-rick-warren-sermons.zip` |
| Tamanho do zip | 13,2 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-rick-warren-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Rick Warren's CRAFT methodology, Saddleback-style structure, and application-focused preaching principles. Use when the user asks to create a sermon, preaching manuscript, sermon outline, sermon series message, commitment prayer, or weekly homework based on a Bible text or theme and wants the result shaped by Rick Warren, Saddleback, CRAFT, purpose-driven preaching, or strong practical application. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 31,3 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 181 B |
| `references` | 1 | 4,1 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Rick Warren Sermons
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
| `skills/sermoes-pregacao/generate-rick-warren-sermons/agents/openai.yaml` | 181 B |
| `skills/sermoes-pregacao/generate-rick-warren-sermons/references/rick_warren_method.md` | 4,1 KB |
| `skills/sermoes-pregacao/generate-rick-warren-sermons/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-rick-warren-sermons/scripts/config.json` | 458 B |
| `skills/sermoes-pregacao/generate-rick-warren-sermons/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-rick-warren-sermons/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-rick-warren-sermons/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-rick-warren-sermons/SKILL.md` | 10,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-rick-warren-sermons`
- `C:\Users\filip\.agents\skills\generate-rick-warren-sermons`
- `C:\Users\filip\.claude\skills\generate-rick-warren-sermons`
- `C:\Users\filip\.cursor\skills\generate-rick-warren-sermons`
- `C:\Users\filip\.windsurf\skills\generate-rick-warren-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-rick-warren-sermons
description: Generate sermon outlines and full sermon manuscripts using Rick Warren's CRAFT methodology, Saddleback-style structure, and application-focused preaching principles. Use when the user asks to create a sermon, preaching manuscript, sermon outline, sermon series message, commitment prayer, or weekly homework based on a Bible text or theme and wants the result shaped by Rick Warren, Saddleback, CRAFT, purpose-driven preaching, or strong practical application.
---

# Generate Rick Warren Sermons

## Overview

Generate sermons with a Rick Warren-style workflow: identify the human need, define the transformation target, arrange persuasive action points, and end with a commitment prayer plus verifiable homework. The default deliverable is a formatted Microsoft Word document.

Read [references/rick_warren_method.md](references/rick_warren_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, tone, checkpoints, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Rick Warren into generic practical preaching. Preserve CRAFT, the human-need hook, the convictions-character-conduct target, action-verb points, commitment prayer, and weekly homework.
- If the user asks for Rick Warren, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the input.
2. If the user did not provide a biblical text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a general evangelical congregation and a complete sermon manuscript.
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

- Start by identifying the central human need.
- Run the preparation through CRAFT: collect and compare, research and reflect, apply and arrange, fashion and flavor, trim and tie together.
- Choose one primary transformation target: convictions, character, or conduct.
- Write the main idea as one sentence that uses `voce`.
- Build 3 to 5 application points, preferably 4.
- Start each point with an action verb. Rewrite noun-based headings.
- Arrange points for persuasion and listener reception, not merely in verse order.
- Keep every point tied to thinking, feeling, or acting more like Christ.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The central human need.
2. The primary transformation target.
3. The sermon main point in one sentence with `voce`.
4. The 3 to 5 application points with action verbs.
5. The specific, verifiable, time-bound homework.

Then write the sermon with this sequence:

1. Hook grounded in a real human need without opening on the biblical text.
2. Bridge from the need to the biblical answer.
3. Application points, each with:
   - point title
   - biblical support in accessible language
   - explanation
   - illustration
   - personal application using `voce` and `seu`
4. Commitment prayer tied to the message theme.
5. Weekly homework that is specific, verifiable, and deadline-bound.

Use fill-in markers in the outline portions:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Rick_Warren.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Rick_Warren.epub`.
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

- Prefer clarity over sophistication.
- Use contemporary, accessible language and avoid unnecessary church jargon.
- Use `voce` for individual application. Reserve `nos` for corporate church application only.
- Add tension, release, and movement across the sermon.
- Trim redundancy aggressively.
- Use category transitions such as `o segundo passo` or `o terceiro beneficio`.
- Include at least one concrete illustration per point.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify each point starts with a verb.
- Verify every point contains biblical support, explanation, illustration, and application.
- Verify the sermon clearly drives transformation, not mere information.
- Verify the homework answers: what will you do differently this week?
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
