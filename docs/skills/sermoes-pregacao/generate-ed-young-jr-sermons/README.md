# generate-ed-young-jr-sermons

- Categoria: **Sermoes e Pregacao** (`sermoes-pregacao`)
- Nome declarado: `generate-ed-young-jr-sermons`
- Pacote instalavel: `packages/sermoes-pregacao/generate-ed-young-jr-sermons.zip`
- Pasta copiada: `skills/sermoes-pregacao/generate-ed-young-jr-sermons`
- Fonte original: `C:\Users\filip\.codex\skills\generate-ed-young-jr-sermons`
- Hash do `SKILL.md`: `39409e952baf112b44dcc6f4c7ddd496388caa15e18496dee6c1788c74dfd032`

## Resumo

Generate sermon outlines and full sermon manuscripts using Ed Young Jr.'s creative preaching method, including Identification-Illustration-Application, a clear Big Idea, a creative series concept, a self-sustaining visual anchor, practical and verifiable application, direct address to unchurched listeners, and a clear point of decision. Use when the user asks to create a sermon, preaching manuscript, Ed Young Jr style sermon, creative church sermon, series-based sermon, seeker-aware sermon, or a highly creative evangelical message based on a Bible text or theme.

## Instalacao individual

```powershell
$zip = "packages/sermoes-pregacao/generate-ed-young-jr-sermons.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-ed-young-jr-sermons` |
| Skill name | `generate-ed-young-jr-sermons` |
| Categoria | `sermoes-pregacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-ed-young-jr-sermons` |
| Pasta no repositorio | `skills/sermoes-pregacao/generate-ed-young-jr-sermons` |
| Arquivo principal | `skills/sermoes-pregacao/generate-ed-young-jr-sermons/SKILL.md` |
| Zip | `packages/sermoes-pregacao/generate-ed-young-jr-sermons.zip` |
| Tamanho do zip | 13,8 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-ed-young-jr-sermons |
| `description` | Generate sermon outlines and full sermon manuscripts using Ed Young Jr.'s creative preaching method, including Identification-Illustration-Application, a clear Big Idea, a creative series concept, a self-sustaining visual anchor, practical and verifiable application, direct address to unchurched listeners, and a clear point of decision. Use when the user asks to create a sermon, preaching manuscript, Ed Young Jr style sermon, creative church sermon, series-based sermon, seeker-aware sermon, or a highly creative evangelical message based on a Bible text or theme. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 33,4 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 182 B |
| `references` | 1 | 3,8 KB |
| `scripts` | 5 | 16,6 KB |

## Secoes internas detectadas

- Generate Ed Young Jr Sermons
-   Overview
-   Method Fidelity Rules
-   Workflow
-   Originality Requirement
-   Research Requirement
-   Core Method Rules
-   Preparation Questions
-   Output Contract
-   Exposition Rules
-   Application Rules
-   Creative Delivery Rules
-   Document Delivery
-   Hybrid Environment Rules
-   Style Rules
-   Final Quality Check
-   Final Cleanup Rule
-   Final Output Override (MD Only)
-   Pergunta Inicial Obrigatoria (Escopo da Producao)

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/agents/openai.yaml` | 182 B |
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/references/ed_young_jr_method.md` | 3,8 KB |
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/scripts/adapters.py` | 848 B |
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/scripts/config.json` | 458 B |
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/scripts/core.py` | 6,2 KB |
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/scripts/create_sermon_docx.py` | 3,4 KB |
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/scripts/create_sermon_epub.py` | 5,7 KB |
| `skills/sermoes-pregacao/generate-ed-young-jr-sermons/SKILL.md` | 12,8 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-ed-young-jr-sermons`
- `C:\Users\filip\.agents\skills\generate-ed-young-jr-sermons`
- `C:\Users\filip\.claude\skills\generate-ed-young-jr-sermons`
- `C:\Users\filip\.cursor\skills\generate-ed-young-jr-sermons`
- `C:\Users\filip\.windsurf\skills\generate-ed-young-jr-sermons`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-ed-young-jr-sermons
description: Generate sermon outlines and full sermon manuscripts using Ed Young Jr.'s creative preaching method, including Identification-Illustration-Application, a clear Big Idea, a creative series concept, a self-sustaining visual anchor, practical and verifiable application, direct address to unchurched listeners, and a clear point of decision. Use when the user asks to create a sermon, preaching manuscript, Ed Young Jr style sermon, creative church sermon, series-based sermon, seeker-aware sermon, or a highly creative evangelical message based on a Bible text or theme.
---

# Generate Ed Young Jr Sermons

## Overview

Generate sermons using Ed Young Jr.'s method of creative evangelistic preaching: enter through the hearer's lived experience before opening the text, anchor the sermon in a memorable Big Idea, package the truth with a creative illustration or visual that can stand on its own, and drive the message toward a specific and verifiable response. The default deliverable is a formatted Microsoft Word document.

Read [references/ed_young_jr_method.md](references/ed_young_jr_method.md) when writing or reviewing the sermon. Treat that file as the source of truth for Ed Young Jr.'s theology of creativity, the Identification-Illustration-Application triad, the "consistently inconsistent" principle, and the evangelistic point-of-decision logic.
Use [scripts/create_sermon_docx.py](scripts/create_sermon_docx.py) to convert the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification derived from the Notion methodology source.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Ed Young Jr. into generic creative preaching. Preserve Identification-Illustration-Application, the Big Idea, the visual anchor test, the unchurched address, and the point of decision.
- If the user asks for Ed Young Jr., keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the biblical text or theme.
2. If the user did not provide a text or theme, ask for it directly.
3. If the user did not provide audience, context, or length, assume a mixed congregation that includes committed believers, nominal Christians, skeptical visitors, and people far from God.
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

## Core Method Rules

- Build the sermon through `Identification -> Illustration -> Application`.
- Start in the life of the hearer before moving to the text.
- Make the text arrive as an answer to a tension that already exists in the room.
- State one Big Idea as a full sentence.
- Create a creative title and, when relevant, a series concept that would attract someone far from church.
- Use a visual or creative anchor only if it passes the self-sufficiency test:
  - it communicates before explanation
  - it does not feel forced
  - it serves the biblical truth instead of competing with it
- Keep the message evangelistically aware:
  - directly address the unchurched listener
  - call for a real decision, not vague reflection
- If the request is for a complete sermon and no shorter limit is given, enforce at least 7,500 words in the final manuscript.

## Preparation Questions

Before drafting the sermon, answer these three questions:

1. What do I need to know from the text?
2. What does this audience need to know from the text?
3. What do they need to do this week?

Do not start with title gimmicks, stage visuals, or format ideas before those answers are clear.

## Output Contract

Before the sermon body, explicitly declare:

1. The biblical text and the series type:
   - expository
   - topical
   - felt-needs
   - character
   - cultural
2. The series title and the sermon title, with a brief justification for why they can attract people far from God without extra explanation.
3. The Big Idea as one complete memorable sentence.
4. The answers to the three preparation questions:
   - what I need to know
   - what the audience needs to know
   - what they need to do
5. The visual or creative anchor for the sermon, plus the self-sufficiency test result.
6. The identification story or everyday situation and where it came from:
   - personal observation
   - recent lived experience
   - pastoral encounter
   - ongoing idea journal
7. The verifiable application and how the hearer will know by Friday whether they obeyed.
8. The exact moment where the non-Christian listener will be directly addressed.
9. The "consistently inconsistent" feature:
   - what is deliberately different from the previous message style or expected format
10. The closing phrase or image that should persist into Monday.

Then write the sermon with clearly signaled movement through these phases:

1. Identification
2. Biblical anchoring and Big Idea
3. Creative illustration
4. Exposition points
5. Consolidated application
6. Decision
7. Closing image or line

## Exposition Rules

- Let the biblical text carry the authority.
- Use 2 to 4 points as needed. Do not force a fixed number.
- Each point must include:
  - a clear textual anchor
  - one illustration or concrete angle
  - a partial application tied to that point
  - a return to the Big Idea
- Use original-language detail only when it materially clarifies the meaning.
- Keep the exposition understandable to someone with no theological training.

## Application Rules

- The application must be specific, practical, and verifiable.
- Give it an implied or explicit deadline such as:
  - today
  - before tomorrow morning
  - this week
- Include believers and skeptical listeners in the room.
- Include one direct call to the non-Christian hearer.
- Move beyond admiration to decision.

## Creative Delivery Rules

- Creativity is theological, not decorative.
- Avoid forced visuals.
- Use surprise strategically, not constantly.
- Simplicity can be the creative move if prior messages were highly produced.
- The sermon should feel fresh without changing the gospel.

## Document Delivery

- Write the manuscript to a UTF-8 text or markdown file first.
- By default, write that source manuscript inside [outputs/](outputs/) in this skill folder.
- Run `scripts/create_sermon_docx.py` with `--min-words` set to the requested minimum.
- Default `--min-words` to `7500` when the user asked for a complete sermon and did not lower the requirement.
- Do not claim the document is complete until the script confirms the word count requirement is satisfied.
- By default, write the working `.docx` file inside [outputs/](outputs/) in this skill folder.
- Name the `.docx` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Ed_Young_Jr.docx`.
- After saving the `.docx` in [outputs/](outputs/), copy that same file into `C:\Users\filip\.codex\skills\DOCS_Sermons` using the same filename.
- Deliver the copied final `.docx` path from `C:\Users\filip\.codex\skills\DOCS_Sermons` to the user.
- After the `.docx` is created, run [scripts/create_sermon_epub.py](scripts/create_sermon_epub.py) to convert it into `.epub`.
- Save the `.epub` inside `C:\Users\filip\.codex\skills\EPUB_SERMONS`.
- Name the `.epub` using the biblical reference plus the preacher name, for example: `JoÃ£o_9_Ed_Young_Jr.epub`.
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

- Sound warm, direct, creative, and evangelistically awake.
- Let the sermon begin in the hearer's world, not in abstract doctrine.
- Keep the Big Idea easy to repeat.
- Let the illustration make the truth tangible without taking over the message.
- Push toward a decision with clarity, not manipulation.
- End with a line or image that can stay with the hearer into the week.

## Final Quality Check

Before delivery, verify:

- the message begins with identification before exposition
- the text arrives as an answer to real tension
- the Big Idea is one full sentence and easy to remember
- the creative anchor passes the self-sufficiency test
- every point has text plus illustration plus application
- the application is verifiable by the end of the week
- the non-Christian listener is addressed directly
- the sermon calls for a decision
- the ending leaves a memorable phrase or image

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
