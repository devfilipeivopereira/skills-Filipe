# generate-robin-sharma-talks

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-robin-sharma-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-robin-sharma-talks.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-robin-sharma-talks`
- Fonte original: `C:\Users\filip\.codex\skills\generate-robin-sharma-talks`
- Hash do `SKILL.md`: `43febc52216f5b3f37cb50dc5d6e78d9f9cf3b56052c2c59fe612e2b2e1194eb`

## Resumo

Generate talk outlines and manuscripts in Robin Sharma's personal mastery style: origin story, leadership without a title, four interior empires, four focuses, victory hour 20/20/20, 66-day habit protocol, 90/90/1, and a daily mastery commitment close.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-robin-sharma-talks.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-robin-sharma-talks` |
| Skill name | `generate-robin-sharma-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-robin-sharma-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-robin-sharma-talks` |
| Arquivo principal | `skills/palestras-motivacao/generate-robin-sharma-talks/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-robin-sharma-talks.zip` |
| Tamanho do zip | 25,2 KB |
| Duplicatas consolidadas | 2 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-robin-sharma-talks |
| `description` | Generate talk outlines and manuscripts in Robin Sharma's personal mastery style: origin story, leadership without a title, four interior empires, four focuses, victory hour 20/20/20, 66-day habit protocol, 90/90/1, and a daily mastery commitment close. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 64,1 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 262 B |
| `references` | 1 | 34,3 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate Robin Sharma Talks
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
| `skills/palestras-motivacao/generate-robin-sharma-talks/agents/openai.yaml` | 262 B |
| `skills/palestras-motivacao/generate-robin-sharma-talks/references/robin_sharma_method.md` | 34,3 KB |
| `skills/palestras-motivacao/generate-robin-sharma-talks/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-robin-sharma-talks/scripts/config.json` | 455 B |
| `skills/palestras-motivacao/generate-robin-sharma-talks/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-robin-sharma-talks/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-robin-sharma-talks/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-robin-sharma-talks/SKILL.md` | 13,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-robin-sharma-talks`
- `C:\Users\filip\.cursor\skills\generate-robin-sharma-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-robin-sharma-talks
description: "Generate talk outlines and manuscripts in Robin Sharma's personal mastery style: origin story, leadership without a title, four interior empires, four focuses, victory hour 20/20/20, 66-day habit protocol, 90/90/1, and a daily mastery commitment close."
---

# Generate Robin Sharma Talks

## Overview

Generate talks with Robin Sharma's authentic personal mastery methodology: open with the Forgotten Giant provocation â€” the idea that most people are living far below their native genius â€” and anchor it with the personal story of leaving a successful legal career to pursue a calling; establish that leadership is not a title but a behavior available to everyone; present the Four Interior Empires as the holistic mastery framework the world's top performers balance; apply the Four Focuses of History Makers as the performance diagnostic; teach the Victory Hour and 20/20/20 Formula as the morning architecture that owns the day before the world intrudes; walk through the 66-Day Habit Installation Protocol to set realistic expectations for transformation; present the 90/90/1 Rule and Tight Bubble of Total Focus as the deep work tools for elite daily output; and close with a specific Daily Mastery Commitment the audience designs before leaving. The default deliverable is a formatted Microsoft Word document.

Read [references/robin_sharma_method.md](references/robin_sharma_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Robin Sharma methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Sharma into a generic productivity talk. Preserve the poetic-aphoristic language register, the Lawyer-to-Leader origin story, the Leadership Without a Title premise, all Four Interior Empires named precisely, all Four Focuses named precisely, the Victory Hour, the 20/20/20 Formula with its three segments (Move, Reflect, Grow) in exactly that order, the three-phase 66-Day Protocol (Destruction/Installation/Integration), the 90/90/1 Rule with its exact name, the Tight Bubble of Total Focus with its exact name, and the Daily Mastery Commitment close.
- Robin Sharma is not a motivational shouter, not a data-driven academic, and not a pastoral mentor. He is a wisdom teacher â€” combining Eastern philosophy, Western performance science, and literary storytelling in a warm, elevated, somewhat spiritual register. Any manuscript that sounds like Tony Robbins or Adam Grant has failed the fidelity test.
- Sharma's vocabulary is distinctive and must appear: "heroic performer," "daily mastery," "world-class," "genius," "the top 5%," "Victory Hour," "everyday hero," "mediocrity is a habit, so is excellence," "all change is hard at first, messy in the middle, and gorgeous at the end," "own your morning, elevate your life."
- If the user asks for Robin Sharma, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or performance/leadership challenge.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a room of ambitious professionals â€” executives, entrepreneurs, athletes, creatives â€” who are achieving by conventional standards but feel they are not operating at their full capacity, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of Robin Sharma while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for:
- Current neuroscience findings on morning routines, cortisol cycles, and cognitive performance peaks.
- Contemporary examples of elite performers (athletes, CEOs, artists) who use morning disciplines.
- Recent research on deep work, focus, and distraction in modern professional environments.
- Robin Sharma's most recent content from his podcast, social media, or books relevant to the theme.

## Preparation Rules

- Identify the specific dimension of the audience's underperformance before building any section â€” which of the Four Interior Empires is most neglected?
- Answer four questions first:
  - What is the Forgotten Giant argument for this specific audience â€” in what way are they living below their native potential?
  - Which of the Four Focuses of History Makers is most violated in this audience's context?
  - What is the specific Victory Hour design most relevant to this audience's schedule and challenges?
  - What is the one Daily Mastery Commitment the audience should leave with?
- Write the Central Mantra (the Sharma-style aphorism that encapsulates the talk's transformation) before writing any section.
- The Central Mantra must be short (under 10 words), poetic, and feel like something worth writing on a wall: "Own your morning. Elevate your life." "All change is hard at first, messy in the middle, and gorgeous at the end."
- Design the Daily Mastery Commitment as a specific morning ritual protocol the audience can begin tomorrow â€” not a vague aspiration.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Central Mantra (the Sharma-style aphoristic phrase that encapsulates the talk).
2. The Forgotten Giant Application (the specific way this audience is living below their native potential).
3. The Neglected Interior Empire (which of the four â€” Mindset, Heartset, Healthset, Soulset â€” is most neglected by this audience).
4. The Violated Focus (which of the Four Focuses of History Makers this audience most violates).
5. The Victory Hour Design (the specific 20/20/20 configuration most relevant to this audience).
6. The Historical Figure Anchor (the historical genius, leader, or artist whose morning discipline will be used as proof).
7. The Daily Mastery Commitment (the specific ritual protocol the audience designs at the close).

Then write the talk with these clearly signaled sections:

1. O GIGANTE ESQUECIDO (The Forgotten Giant â€” the provocation that most people are living far below their native genius)
2. O ADVOGADO QUE VENDEU A FERRARI (Lawyer-to-Leader origin story â€” the personal calling that required leaving security)
3. LIDERANÃ‡A SEM TÃTULO (Leadership Without a Title â€” the democratic premise that every person can lead)
4. OS QUATRO IMPÃ‰RIOS INTERIORES (The Four Interior Empires â€” Mindset, Heartset, Healthset, Soulset)
5. OS QUATRO FOCOS DOS FAZEDORES DA HISTÃ“RIA (The Four Focuses of History Makers)
6. A HORA DA VITÃ“RIA E A FÃ“RMULA 20/20/20 (The Victory Hour and 20/20/20 Formula â€” Move, Reflect, Grow)
7. O PROTOCOLO DE 66 DIAS (The 66-Day Habit Installation Protocol â€” Destruction, Installation, Integration)
8. A BOLHA DE FOCO TOTAL E A REGRA 90/90/1 (Tight Bubble of Total Focus + 90/90/1 Rule)
9. O COMPROMISSO DE MAESTRIA DIÃRIA (The Daily Mastery Commitment close)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name, for example: `Maestria_Diaria_Robin_Sharma.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Elevated, poetic, aphoristic register â€” every key insight must sound like it belongs on a wall or a journal page.
- Use rhetorical parallelism and repetition: triplets, anaphoras, and rhythmic sentence pairs are expected and welcome.
- Reference historical figures: Da Vinci, Churchill, Mandela, Einstein, Marcus Aurelius, Picasso, Mozart, Beethoven as exemplars of the principles being taught.
- Blend Eastern philosophy (Stoicism, Zen, Vedic wisdom) with Western performance neuroscience naturally â€” not as a gimmick but as the authentic intellectual tradition Sharma draws from.
- Sharma's Aphorism Register: short, declarative, poetic sentences that feel inevitable after they are said.
  - "Mediocrity is a habit. So is excellence."
  - "Your mornings shape your days, and your days shape your life."
  - "The moments of your days become the biography of your life."
  - "All change is hard at first, messy in the middle, and gorgeous at the end."
  - "Leadership is not a title. It's a behavior. Live it now."
  - "Own your morning. Elevate your life."
  - "Small daily improvements over time lead to stunning results."
- Never use motivational-shouter energy (not Tony Robbins). Never use corporate-researcher dryness (not Adam Grant). Never use pure pastoral warmth (not Maxwell). Sharma's register is the wise teacher â€” warm, demanding, poetic, philosophically grounded.
- The close is a ritual design exercise â€” specific, morning-anchored, starting tomorrow.

## Quality Check

- Verify the opening is the Forgotten Giant provocation â€” not a topic announcement.
- Verify the Lawyer-to-Leader story includes the legal career, the calling, and the first Ferrari book.
- Verify Leadership Without a Title is presented as a democratic premise available to everyone regardless of position.
- Verify all Four Interior Empires are named precisely: Mindset, Heartset, Healthset, Soulset.
- Verify all Four Focuses of History Makers are named: talent cultivation, distraction elimination, mastery pursuit, day stacking.
- Verify the Victory Hour is presented as the period 5:00â€“6:00 AM with its exact name.
- Verify the 20/20/20 Formula presents the three segments in exact order: Move (exercise, 5:00â€“5:20), Reflect (meditation/journaling, 5:20â€“5:40), Grow (learning, 5:40â€“6:00).
- Verify the 66-Day Protocol presents all three phases: Destruction (days 1â€“22), Installation (days 23â€“44), Integration (days 45â€“66).
- Verify the 90/90/1 Rule is named exactly and described correctly (first 90 minutes of workday on the one most important project, for 90 consecutive days).
- Verify the Tight Bubble of Total Focus is named and the five assets of genius are listed: mental focus, physical energy, willpower, original talent, daily time.
- Verify at least three historical figures are referenced as exemplars.
- Verify the Central Mantra appears at least twice in the manuscript.
- Verify the Daily Mastery Commitment is a specific morning ritual protocol â€” not a vague aspiration.
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
