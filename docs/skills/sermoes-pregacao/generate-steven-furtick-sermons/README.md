# generate-steven-furtick-sermons

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-steven-furtick-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-steven-furtick-sermons.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-steven-furtick-sermons`
- Fonte original: `C:\Users\filip\.codex\skills\generate-steven-furtick-sermons`
- Hash do `SKILL.md`: `7b5bd34ea21645811759b1a4a07f54fdd2ba81a592ada463e4b3db986808ad00`

## Resumo

Generate sermon outlines and full sermon manuscripts using Steven Furtick's authentic preaching style, including title wordplay, autobiographical opening story, congregation participation, three-speed rhythm, biblical character dramatization, perspective reframe, and proclamation-driven activation. Use when the user asks to create a sermon, preaching manuscript, sermon outline, emotionally charged narrative sermon, perspective-shift message, or church message based on a Bible text or theme and wants the result shaped by Steven Furtick, Elevation Church style preaching, wordplay sermon titles, narrative reframe preaching, or proclamation-heavy participatory communication.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-steven-furtick-sermons.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-steven-furtick-sermons` |
| Skill name | `generate-steven-furtick-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-steven-furtick-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-steven-furtick-sermons` |
| Arquivo principal | `skills/sermoes-pregacao/generate-steven-furtick-sermons/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-steven-furtick-sermons.zip` |
| Tamanho do zip | 13,2 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-steven-furtick-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Steven Furtick's authentic preaching style, including title wordplay, autobiographical opening story, congregation participation, three-speed rhythm, biblical character dramatization, perspective reframe, and proclamation-driven activation. Use when the user asks to create a sermon, preaching manuscript, sermon outline, emotionally charged narrative sermon, perspective-shift message, or church message based on a Bible text or theme and wants the result shaped by Steven Furtick, Elevation Church style preaching, wordplay sermon titles, narrative reframe preaching, or proclamation-heavy participatory communication. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 31,5 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 184 B |
| `references` | 1 | 3,7 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Steven Furtick Sermons
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
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/agents/openai.yaml` | 184 B |
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/references/steven_furtick_method.md` | 3,7 KB |
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/scripts/config.json` | 461 B |
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-steven-furtick-sermons/SKILL.md` | 11,1 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-steven-furtick-sermons`
- `C:\Users\filip\.agents\skills\generate-steven-furtick-sermons`
- `C:\Users\filip\.claude\skills\generate-steven-furtick-sermons`
- `C:\Users\filip\.cursor\skills\generate-steven-furtick-sermons`
- `C:\Users\filip\.windsurf\skills\generate-steven-furtick-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-steven-furtick-sermons
description: Generate sermon outlines and full sermon manuscripts using Steven Furtick's authentic preaching style, including title wordplay, autobiographical opening story, congregation participation, three-speed rhythm, biblical character dramatization, perspective reframe, and proclamation-driven activation. Use when the user asks to create a sermon, preaching manuscript, sermon outline, emotionally charged narrative sermon, perspective-shift message, or church message based on a Bible text or theme and wants the result shaped by Steven Furtick, Elevation Church style preaching, wordplay sermon titles, narrative reframe preaching, or proclamation-heavy participatory communication.
---

# Generate Steven Furtick Sermons

## Overview

Generate sermons with Steven Furtick's communication method: open with a personal recent story, build toward a text-born wordplay title, dramatize the biblical character, reframe the listener's perspective, escalate into proclamation, and close with concrete activation. The default deliverable is a formatted Microsoft Word document.

Read [references/steven_furtick_method.md](references/steven_furtick_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for structure, tone, pacing, and required output sections.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults. Keep environment-specific assumptions out of the core logic.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Steven Furtick into generic high-energy preaching. Preserve title wordplay, autobiographical opening, three speeds, distributed participation, perspective reframe, and proclamation-driven activation.
- If the user asks for Steven Furtick, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a mixed congregation of churchgoers, seekers, and online listeners and produce a complete sermon manuscript.
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

- Find the sermon title through wordplay that emerges from the text or from a closely related common phrase.
- Build the sermon around one perspective shift or reframe.
- Start with a recent, sensory, autobiographical story.
- Mark at least six participation moments across the message.
- Use three communication speeds:
  - conversation
  - teaching
  - proclamation
- Dramatically narrate the biblical character's inner world without leaving the text's faithfulness.
- Use the language of the enemy to name lies or intimidation where fitting.
- Tie the sermon into a series name when appropriate.
- End with proclamation, activation, and a slower practical landing.
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Output Contract

Before the sermon body, explicitly declare:

1. The series name and the sermon title with its wordplay.
2. The perspective reframe at the heart of the message.
3. The planned participation moments.
4. The phrase-mantra that will be repeated during the week.
5. The practical activation step for this week.

Then write the sermon with these clearly signaled sections:

1. Opening: personal story
2. Transition: title and wordplay reveal
3. Context of the text
4. Dramatization of the biblical character
5. Perspective reframe
6. Climax: proclamation
7. Ending: application and activation

Use explicit markers such as:

- `[TOQUE O SEU VIZINHO E DIGA]`
- `[ALGUEM GRITE]`
- `[DIGA DE NOVO]`
- `[PAUSA]`
- `[DESACELERA]`
- `[VOLUME SOBE]`

Use fill-in markers in outline portions when helpful:

`[ESPACO PARA PREENCHIMENTO: ______________]`

## Document Delivery

- Write the sermon manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Steven_Furtick.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Steven_Furtick.epub`.
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

- Favor casual storytelling before spiritual intensity.
- Use humor and self-awareness early.
- Build toward the title reveal rather than explaining it immediately.
- Let the sermon pivot around a strong `you call it this, God calls it that` reframe.
- Alternate low-intensity storytelling with medium teaching and high-intensity proclamation.
- Repeat the title or phrase-mantra naturally throughout the sermon.
- Slow down before the final activation so the application lands personally.
- If the user asks for a full sermon and gives no length, target a long-form manuscript around 7,500 words.

## Quality Check

- Verify the title wordplay feels discovered, not gimmicky.
- Verify the opening story is recent, specific, and sensory.
- Verify there are at least six marked participation moments.
- Verify the biblical character is dramatized in a text-faithful way.
- Verify the reframe is clear and central.
- Verify the ending includes both proclamation and a practical step.
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
