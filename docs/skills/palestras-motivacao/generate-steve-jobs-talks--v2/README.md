# generate-steve-jobs-talks--v2

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-steve-jobs-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-steve-jobs-talks--v2.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-steve-jobs-talks--v2`
- Fonte original: `C:\Users\filip\.agents\skills\generate-steve-jobs-talks`
- Hash do `SKILL.md`: `0737f92d68e9f1b5b037e49adae22fa5a5f9f4802b15ee8fca3c982801684b5b`

## Resumo

Generate motivational talk outlines and full talk manuscripts using Steve Jobs's authentic communication methodology — operating in two distinct modes that mirror his two greatest communication legacies. Mode 1 (Stanford Mode): the three-story biographical framework drawn from the 2005 Stanford commencement speech — Connecting the Dots, Love and Loss, and Death as the clarifier — closing with Stay Hungry, Stay Foolish. Mode 2 (Keynote Mode): the visionary product-launch architecture — the villain-hero narrative, the Rule of Three, the Reality Distortion Field construction, the demo as theater, and One More Thing. Both modes share the Jobs signature elements: radical simplicity of expression, the intersection of technology and the humanities, and the conviction that the people crazy enough to think they can change the world are the ones who do. Use when the user asks to create a motivational talk, keynote, vision speech, innovation address, leadership keynote, commencement-style talk, product or idea launch presentation, or any communication about following your passion, connecting unexpected dots, embracing loss as liberation, using mortality as a clarifier, building what the world doesn't yet know it needs, pursuing great work over convenient work, or the philosophy that simplicity is the ultimate sophistication, and wants the result shaped by Steve Jobs, the Stanford commencement speech, the iPhone keynote, the Think Different campaign, the Reality Distortion Field, Stay Hungry Stay Foolish, Connecting the Dots, the intersection of technology and the liberal arts, or the Jobs philosophy of design, focus, and insanely great work.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-steve-jobs-talks--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-steve-jobs-talks--v2` |
| Skill name | `generate-steve-jobs-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `agents` |
| Tipo da fonte | Agents local |
| Fonte original | `C:\Users\filip\.agents\skills\generate-steve-jobs-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-steve-jobs-talks--v2` |
| Arquivo principal | `skills/palestras-motivacao/generate-steve-jobs-talks--v2/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-steve-jobs-talks--v2.zip` |
| Tamanho do zip | 25,2 KB |
| Duplicatas consolidadas | 3 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-steve-jobs-talks |
| `description` | Generate motivational talk outlines and full talk manuscripts using Steve Jobs's authentic communication methodology — operating in two distinct modes that mirror his two greatest communication legacies. Mode 1 (Stanford Mode): the three-story biographical framework drawn from the 2005 Stanford commencement speech — Connecting the Dots, Love and Loss, and Death as the clarifier — closing with Stay Hungry, Stay Foolish. Mode 2 (Keynote Mode): the visionary product-launch architecture — the villain-hero narrative, the Rule of Three, the Reality Distortion Field construction, the demo as theater, and One More Thing. Both modes share the Jobs signature elements: radical simplicity of expression, the intersection of technology and the humanities, and the conviction that the people crazy enough to think they can change the world are the ones who do. Use when the user asks to create a motivational talk, keynote, vision speech, innovation address, leadership keynote, commencement-style talk, product or idea launch presentation, or any communication about following your passion, connecting unexpected dots, embracing loss as liberation, using mortality as a clarifier, building what the world doesn't yet know it needs, pursuing great work over convenient work, or the philosophy that simplicity is the ultimate sophistication, and wants the result shaped by Steve Jobs, the Stanford commencement speech, the iPhone keynote, the Think Different campaign, the Reality Distortion Field, Stay Hungry Stay Foolish, Connecting the Dots, the intersection of technology and the liberal arts, or the Jobs philosophy of design, focus, and insanely great work. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 64,4 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 350 B |
| `references` | 1 | 32,0 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate Steve Jobs Talks
-   Overview
-   Method Fidelity Rules
-   Mode Selection Logic
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
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/agents/openai.yaml` | 350 B |
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/references/steve_jobs_method.md` | 32,0 KB |
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/scripts/config.json` | 453 B |
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-steve-jobs-talks--v2/SKILL.md` | 15,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.agents\skills\generate-steve-jobs-talks`
- `C:\Users\filip\.claude\skills\generate-steve-jobs-talks`
- `C:\Users\filip\.windsurf\skills\generate-steve-jobs-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-steve-jobs-talks
description: Generate motivational talk outlines and full talk manuscripts using Steve Jobs's authentic communication methodology — operating in two distinct modes that mirror his two greatest communication legacies. Mode 1 (Stanford Mode): the three-story biographical framework drawn from the 2005 Stanford commencement speech — Connecting the Dots, Love and Loss, and Death as the clarifier — closing with Stay Hungry, Stay Foolish. Mode 2 (Keynote Mode): the visionary product-launch architecture — the villain-hero narrative, the Rule of Three, the Reality Distortion Field construction, the demo as theater, and One More Thing. Both modes share the Jobs signature elements: radical simplicity of expression, the intersection of technology and the humanities, and the conviction that the people crazy enough to think they can change the world are the ones who do. Use when the user asks to create a motivational talk, keynote, vision speech, innovation address, leadership keynote, commencement-style talk, product or idea launch presentation, or any communication about following your passion, connecting unexpected dots, embracing loss as liberation, using mortality as a clarifier, building what the world doesn't yet know it needs, pursuing great work over convenient work, or the philosophy that simplicity is the ultimate sophistication, and wants the result shaped by Steve Jobs, the Stanford commencement speech, the iPhone keynote, the Think Different campaign, the Reality Distortion Field, Stay Hungry Stay Foolish, Connecting the Dots, the intersection of technology and the liberal arts, or the Jobs philosophy of design, focus, and insanely great work.
---

# Generate Steve Jobs Talks

## Overview

Generate talks with Steve Jobs's authentic communication methodology in two distinct modes that reflect his two greatest communication legacies.

**Mode 1 — Stanford Mode** (for inspirational, personal, or commencement-style talks): the three-story biographical framework from the 2005 Stanford address. Story 1: Connecting the Dots (the retrospective pattern — how seemingly useless experiences become essential). Story 2: Love and Loss (finding what you love, losing it, and the unexpected liberation of starting again). Story 3: Death as the Clarifier (mortality as the most powerful tool for making decisions that matter). Close: Stay Hungry, Stay Foolish.

**Mode 2 — Keynote Mode** (for vision, product, innovation, or leadership launches): the visionary presentation architecture of Apple's landmark keynotes. The villain-hero narrative (the world has a problem that no one has solved elegantly). The Rule of Three (three products, three benefits, three reasons). The Reality Distortion Field construction (the vision made so vivid and concrete that the audience cannot imagine the world without it). The demo as theater (showing the thing working, in real time, with drama). One More Thing (the unexpected revelation that reframes everything). Close: the intersection of technology and the liberal arts.

Both modes share the Jobs signature: radical simplicity of expression, the conviction that great work requires love, and the philosophy that the people crazy enough to think they can change the world are the ones who do.

The default deliverable is a formatted Microsoft Word document.

Read [references/steve_jobs_method.md](references/steve_jobs_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Steve Jobs methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- The user must specify or the skill must determine which mode is appropriate before writing. If the talk is personal, biographical, and inspirational — use Stanford Mode. If the talk is about launching a vision, idea, product, or change initiative — use Keynote Mode. If the theme warrants both, combine them in the order: Stanford Mode arc + Keynote Mode close.
- Do not flatten Jobs into a generic inspirational speech. Stanford Mode must preserve the three-story structure in sequence (Dots → Loss → Death) and close with Stay Hungry Stay Foolish. Keynote Mode must preserve the villain-hero narrative, the Rule of Three, the demo moment, and One More Thing.
- Jobs's tone is specific and mandatory: deceptively casual yet precisely controlled. He sounds like he is thinking aloud — "Today I want to tell you three stories. That's it. No big deal. Just three stories." But every word was chosen deliberately. The apparent simplicity conceals extraordinary craft.
- Jobs never uses bullet points, complex slides, or lists of features as the organizing principle. He uses story, demonstration, and the progressive revelation of a single big idea.
- Jobs's vocabulary is specific and must appear throughout: "insanely great," "stay hungry, stay foolish," "one more thing," "the most [superlative] ever," "this changes everything," "connecting the dots," "don't settle," "you are already naked," "put a dent in the universe," "the intersection of technology and the liberal arts," "think different," "the reality distortion field" (this last one is described but never named in the talk itself).
- If the user asks for Steve Jobs, keep the methodology intact unless the user explicitly asks to depart from it.

## Mode Selection Logic

Before writing, declare the mode explicitly:

- **Stanford Mode**: The audience is about to begin something significant — a new phase, a difficult path, or they need the courage to follow their instincts against conventional wisdom.
- **Keynote Mode**: The audience needs to believe in a vision — a new idea, initiative, product, direction, or change — that currently does not exist or that they have not yet accepted.
- **Combined Mode**: The talk uses personal biographical story (Stanford) to establish credibility and emotional connection, then pivots to a specific vision (Keynote) — the most powerful configuration for leadership keynotes.

## Workflow

1. Confirm the theme, audience, and purpose of the talk.
2. Determine and declare the mode (Stanford / Keynote / Combined) before writing.
3. If the user did not provide audience profile or context, assume a room of ambitious professionals, entrepreneurs, or creators who are talented but playing it too safe — staying in comfortable mediocrity when they have the capacity for something genuinely remarkable.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of Steve Jobs while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for:
- Specific details from Jobs's biography that are most relevant to the theme (Walter Isaacson's biography is the primary source).
- Contemporary examples of the intersection of technology and the humanities that reinforce the specific talk's theme.
- The most recent innovations or cultural moments that can serve as the "villain" in Keynote Mode.

## Preparation Rules

**For Stanford Mode:**
- Identify the three dots before writing: which experiences, failures, or apparently useless choices will form the retrospective pattern?
- Write the lesson of each story before writing the story itself: the story must earn the lesson, not announce it in advance.
- Write the Death passage before the rest: it is the emotional and philosophical heart of the entire speech.

**For Keynote Mode:**
- Identify the villain clearly before writing: what specific, concrete problem is the world suffering from that the idea/vision/product solves?
- Write the "One More Thing" before writing anything else: the whole talk is the setup for this revelation.
- Design the demo moment: where in the talk does the idea become real, tangible, undeniable?

- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

**Stanford Mode** — before the talk body, declare:

1. The Three Dots (the three specific biographical experiences that form the retrospective pattern).
2. The Core Lesson of Each Story (what the audience must take away from each).
3. The Death Passage Application (how the mortality argument connects to the specific audience's situation).
4. The Stay Hungry Stay Foolish Close (the exact final phrase and its application to this audience).
5. The Rule of Three Application (what three things are organized in the talk).
6. The Signature Phrase (the one sentence from this talk that the audience will remember).
7. The Unexpected Connection (the calligraphy moment — the thing that seemed useless and turned out to be essential).

Then write the talk with these clearly signaled sections:

1. A ABERTURA CASUAL E PRECISA (Deceptively casual opening — "Today I want to tell you X. That's it.")
2. HISTÓRIA 1: CONECTANDO OS PONTOS (Connecting the Dots — the retrospective pattern of unexpected value)
3. HISTÓRIA 2: AMOR E PERDA (Love and Loss — finding what you love, losing it, the liberation of starting again)
4. HISTÓRIA 3: A MORTE COMO CLARIFICADORA (Death as the Clarifier — mortality as the most powerful decision tool)
5. STAY HUNGRY. STAY FOOLISH. (The close — the simplest and most powerful instruction)

**Keynote Mode** — before the talk body, declare:

1. The Villain (the specific, concrete problem the world is suffering from).
2. The Hero (the idea, vision, or initiative that solves it, described as if from the future).
3. The Rule of Three Structure (the three things that organize the talk).
4. The Demo Moment (where and how the idea becomes real and tangible in the talk).
5. One More Thing (the unexpected revelation that reframes everything that came before).
6. The Intersection Argument (how this idea sits at the intersection of technology and the humanities).
7. The Reality Distortion Anchor (the single image or phrase that makes the vision undeniable).

Then write the talk with these clearly signaled sections:

1. A ABERTURA DE IMPACTO (High-impact opening — the problem stated in its most visceral form)
2. O VILÃO (The Villain — the world as it is, with the problem made undeniable)
3. A REGRA DE TRÊS (The Rule of Three — the three things that structure the solution)
4. A DEMONSTRAÇÃO (The Demo — the idea made real, in real time, with theater)
5. A INTERSEÇÃO (The Intersection of technology and the humanities — the deeper argument)
6. UMA COISA A MAIS (One More Thing — the unexpected revelation)
7. O FECHAMENTO VISIONÁRIO (The visionary close — the world as it will be)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name and mode: `Conectando_os_Pontos_Steve_Jobs_Stanford.docx` or `Lancamento_da_Visao_Steve_Jobs_Keynote.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Deceptively casual and precisely controlled — sounds spontaneous, was rehearsed for weeks.
- Simple sentences. Short paragraphs. Never a list of bullet points as the organizational principle.
- Use the rule of three obsessively: three stories, three products, three reasons, three things.
- Jobs's pauses must be written as stage directions: [PAUSA] for the moment the audience absorbs something.
- The superlative is Jobs's natural register: "the most," "the best," "revolutionary," "insanely great."
- Never explain the emotion — produce it. Jobs does not say "this is exciting." He says "isn't that cool?" and lets the thing speak.
- The demo must be written as if it is happening live: present tense, immediacy, theater.
- The intersection of technology and the liberal arts must appear in Keynote Mode — it is Jobs's most important philosophical claim about why Apple matters and why this idea matters.
- "Stay Hungry. Stay Foolish." must close Stanford Mode. Period. Nothing after it.
- "One More Thing" must arrive as a surprise in Keynote Mode — the talk must not telegraph it.

## Quality Check

**Stanford Mode:**
- Verify the opening is deceptively casual: "Just three stories. That's it."
- Verify Story 1 (Connecting the Dots) uses a specific unexpected experience that turned out to be essential — not a generic wisdom claim.
- Verify Story 2 (Love and Loss) includes both finding love for the work AND losing something significant — and the liberation that followed.
- Verify Story 3 (Death) includes the mirror question ("If today were the last day of my life, would I want to do what I am about to do today?") and the "You are already naked" principle.
- Verify "Stay Hungry. Stay Foolish." closes the talk — with nothing after it.
- Verify the Rule of Three is present structurally.
- Verify "Don't Settle" appears at least once.

**Keynote Mode:**
- Verify the opening names the villain concretely — not abstractly.
- Verify the Rule of Three organizes the talk.
- Verify the demo moment is written as theater — present tense, immediate, visceral.
- Verify the intersection of technology and the liberal arts appears.
- Verify "One More Thing" arrives unexpectedly.
- Verify the close paints the world as it will be — not how it is.

**Both Modes:**
- Verify the tone is simple and precise — never corporate, never academic.
- Verify the superlative appears appropriately: the most, the best, insanely great.
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
