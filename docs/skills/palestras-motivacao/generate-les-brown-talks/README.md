# generate-les-brown-talks

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-les-brown-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-les-brown-talks.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-les-brown-talks`
- Fonte original: `C:\Users\filip\.codex\skills\generate-les-brown-talks`
- Hash do `SKILL.md`: `ab650d55d152c05cb88c1d806bb7e235cec04d0f2b9e93fbe3030b4fbf497c37`

## Resumo

Generate motivational talk outlines and full talk manuscripts using Les Brown's authentic hunger-and-possibility methodology, including the collective affirmation opening, the origin story of being discarded, the graveyard of unfulfilled dreams, the hunger diagnosis, the Three Cs framework, and the prophetic personal challenge close. Use when the user asks to create a motivational talk, keynote, community speech, overcoming adversity message, possibility talk, hunger-driven motivational address, or high-energy transformational keynote and wants the result shaped by Les Brown, You Gotta Be Hungry, IT'S POSSIBLE, greatness within you, live full die empty, Don't let someone's opinion become your reality, the graveyard speech, or Les Brown's full-voltage oratory style.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-les-brown-talks.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-les-brown-talks` |
| Skill name | `generate-les-brown-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-les-brown-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-les-brown-talks` |
| Arquivo principal | `skills/palestras-motivacao/generate-les-brown-talks/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-les-brown-talks.zip` |
| Tamanho do zip | 14,9 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-les-brown-talks |
| `description` | Generate motivational talk outlines and full talk manuscripts using Les Brown's authentic hunger-and-possibility methodology, including the collective affirmation opening, the origin story of being discarded, the graveyard of unfulfilled dreams, the hunger diagnosis, the Three Cs framework, and the prophetic personal challenge close. Use when the user asks to create a motivational talk, keynote, community speech, overcoming adversity message, possibility talk, hunger-driven motivational address, or high-energy transformational keynote and wants the result shaped by Les Brown, You Gotta Be Hungry, IT'S POSSIBLE, greatness within you, live full die empty, Don't let someone's opinion become your reality, the graveyard speech, or Les Brown's full-voltage oratory style. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 34,8 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 225 B |
| `references` | 1 | 9,3 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate Les Brown Talks
-   Overview
-   Method Fidelity Rules
-   Workflow
-   Originality Requirement
-   Research Requirement
-   Preparation Rules
-   Output Contract
-   Document Delivery
-   Style Rules
-   Quality Check
-   Final Cleanup Rule
-   Final Output Override (MD Only)
-   Pergunta Inicial Obrigatoria (Escopo da Producao)

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/palestras-motivacao/generate-les-brown-talks/agents/openai.yaml` | 225 B |
| `skills/palestras-motivacao/generate-les-brown-talks/references/les_brown_method.md` | 9,3 KB |
| `skills/palestras-motivacao/generate-les-brown-talks/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-les-brown-talks/scripts/config.json` | 452 B |
| `skills/palestras-motivacao/generate-les-brown-talks/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-les-brown-talks/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-les-brown-talks/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-les-brown-talks/SKILL.md` | 8,7 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-les-brown-talks`
- `C:\Users\filip\.agents\skills\generate-les-brown-talks`
- `C:\Users\filip\.claude\skills\generate-les-brown-talks`
- `C:\Users\filip\.cursor\skills\generate-les-brown-talks`
- `C:\Users\filip\.windsurf\skills\generate-les-brown-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-les-brown-talks
description: Generate motivational talk outlines and full talk manuscripts using Les Brown's authentic hunger-and-possibility methodology, including the collective affirmation opening, the origin story of being discarded, the graveyard of unfulfilled dreams, the hunger diagnosis, the Three Cs framework, and the prophetic personal challenge close. Use when the user asks to create a motivational talk, keynote, community speech, overcoming adversity message, possibility talk, hunger-driven motivational address, or high-energy transformational keynote and wants the result shaped by Les Brown, You Gotta Be Hungry, IT'S POSSIBLE, greatness within you, live full die empty, Don't let someone's opinion become your reality, the graveyard speech, or Les Brown's full-voltage oratory style.
---

# Generate Les Brown Talks

## Overview

Generate motivational talks with Les Brown's authentic methodology: open with a collective affirmation that activates the audience's participation, tell the origin story of being labeled and discarded and the teacher who reversed it, deliver the graveyard passage as the philosophical pivot, diagnose the death of hunger as the central problem, present the Three Cs as the remedy, and close with a direct, prophetic personal challenge to each member of the audience. The default deliverable is a formatted Microsoft Word document.

Read [references/les_brown_method.md](references/les_brown_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Les Brown methodology.
- Follow every non-negotiable in that reference exactly.
- Do not flatten Les Brown into a generic motivational speech. Preserve the collective affirmation, the origin story, the graveyard passage, the hunger diagnosis, the Three Cs, and the prophetic personal challenge close.
- The authority of Les Brown is entirely biographical — it comes from having been labeled, discarded, and proved wrong. Without the origin story, it is generic motivation, not Les Brown.

## Workflow

1. Confirm the theme or audience challenge.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile or context, assume a mixed room of people who have experienced failure, been told their dreams are too big, or who have allowed comfort to replace hunger, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of Les Brown while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for stories of people who overcame circumstances worse than those of the audience — and succeeded not through resources but through hunger. These stories serve the proof phase of the talk.

## Preparation Rules

- Identify what killed the audience's hunger (comfort, approval-seeking, fear of failure, labels from others).
- Answer three questions first:
  - What label has this audience accepted that is not their own truth?
  - What music are they carrying inside that has not yet been sung?
  - What would they do if they knew they couldn't fail?
- Write the Battle Cry (the collective affirmation the audience will shout at the opening) before writing the talk body.
- Write the graveyard passage with care — it is the philosophical heart of the entire talk and must be delivered with full weight.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Battle Cry (the collective affirmation the audience will shout with the speaker).
2. The Label Being Reversed (the specific limiting belief imposed by others that the talk dismantles).
3. The Hunger Death Cause (what specifically killed the audience's hunger).
4. The Graveyard Application (how the unfulfilled dreams metaphor connects to this specific audience).
5. The Three Cs Application (how Conviction, Commitment, and Consistency apply to the audience's challenge).
6. The Music Inside (the specific unfulfilled potential the speaker challenges the audience to release).
7. The Prophetic Challenge (the direct, personal declaration the speaker makes to each audience member).

Then write the talk with these clearly signaled sections:

1. O GRITO (Battle Cry opening — collective affirmation)
2. A ORIGEM (Origin story of being labeled and discarded)
3. O CEMITÉRIO (Graveyard of unfulfilled dreams — philosophical pivot)
4. O DIAGNÓSTICO DA FOME (Death of hunger — naming what killed it)
5. OS TRÊS CS (Conviction, Commitment, Consistency as the remedy)
6. AS HISTÓRIAS DE PROVA (Stories of people who came from worse and won)
7. O DESAFIO PROFÉTICO (Direct, prophetic personal challenge close)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name, for example: `Grandeza_Dentro_de_Voce_Les_Brown.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- High voltage from the first word — Les Brown never begins quietly.
- Speak in the language of the street, not the boardroom: vivid, direct, unpolished in the best sense.
- Use collective participation throughout: [A PLATEIA RESPONDE: ___________].
- Use anaphora aggressively: repeat the opening phrase of successive sentences.
- The word FOME (hunger) must appear at least fifteen times — it is not just a concept, it is a drumbeat.
- The graveyard passage must be delivered slowly, with pauses, at lower volume — in contrast to the high energy of the rest of the talk.
- The close must be direct, personal, prophetic — not warm, not gentle. Les Brown stares into the audience's eyes and declares what he sees in them.

## Quality Check

- Verify the opening includes a collective affirmation that the audience shouts back.
- Verify the origin story includes Mr. Washington's declaration: "Don't let someone's opinion become your reality."
- Verify the graveyard passage is present and delivered at lower volume with explicit stage direction.
- Verify FOME is the diagnostic concept and the drumbeat of the talk.
- Verify all Three Cs are explained with concrete behavioral meaning.
- Verify at least two proof stories of people from worse circumstances who won by hunger alone.
- Verify the close is a prophetic personal declaration — not a summary, not a generic encouragement.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` and `.epub` have been delivered, the local `outputs/` folder must be emptied while preserving the folder itself.

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
