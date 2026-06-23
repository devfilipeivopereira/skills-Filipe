# generate-david-goggins-talks

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-david-goggins-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-david-goggins-talks.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-david-goggins-talks`
- Fonte original: `C:\Users\filip\.codex\skills\generate-david-goggins-talks`
- Hash do `SKILL.md`: `5edb4f0295f4e659503950244f5614fe9405d124bba00e0010fb9b290dd09e95`

## Resumo

Generate talk outlines and manuscripts in David Goggins's mental toughness style: Buffalo origin story, motivation is a lie, 40% rule, callousing the mind, accountability mirror, cookie jar, taking souls, and a Stay Hard challenge. Use for resilience, discipline, or performance-under-pressure talks.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-david-goggins-talks.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-david-goggins-talks` |
| Skill name | `generate-david-goggins-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-david-goggins-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-david-goggins-talks` |
| Arquivo principal | `skills/palestras-motivacao/generate-david-goggins-talks/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-david-goggins-talks.zip` |
| Tamanho do zip | 24,8 KB |
| Duplicatas consolidadas | 2 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-david-goggins-talks |
| `description` | Generate talk outlines and manuscripts in David Goggins's mental toughness style: Buffalo origin story, motivation is a lie, 40% rule, callousing the mind, accountability mirror, cookie jar, taking souls, and a Stay Hard challenge. Use for resilience, discipline, or performance-under-pressure talks. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 64,0 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 263 B |
| `references` | 1 | 34,1 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate David Goggins Talks
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
| `skills/palestras-motivacao/generate-david-goggins-talks/agents/openai.yaml` | 263 B |
| `skills/palestras-motivacao/generate-david-goggins-talks/references/david_goggins_method.md` | 34,1 KB |
| `skills/palestras-motivacao/generate-david-goggins-talks/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-david-goggins-talks/scripts/config.json` | 456 B |
| `skills/palestras-motivacao/generate-david-goggins-talks/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-david-goggins-talks/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-david-goggins-talks/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-david-goggins-talks/SKILL.md` | 13,1 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-david-goggins-talks`
- `C:\Users\filip\.cursor\skills\generate-david-goggins-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-david-goggins-talks
description: "Generate talk outlines and manuscripts in David Goggins's mental toughness style: Buffalo origin story, motivation is a lie, 40% rule, callousing the mind, accountability mirror, cookie jar, taking souls, and a Stay Hard challenge. Use for resilience, discipline, or performance-under-pressure talks."
---

# Generate David Goggins Talks

## Overview

Generate talks with David Goggins's authentic anti-guru methodology: open with the Buffalo Origin â€” the raw biographical testimony of a childhood defined by abuse, poverty, obesity, and failure that produced the most mentally tough human being alive â€” then confront the audience with the single truth they most want to avoid: motivation is a lie, and they have been using it as an excuse to stay comfortable. Introduce the Governor as the neurological mechanism that stops people at 40% of their real capacity. Teach Callousing the Mind as the only legitimate path to mental toughness. Present the Accountability Mirror as the tool for radical self-honesty. Install the Cookie Jar as the mental fuel reserve for moments of maximum difficulty. Explain Taking Souls as the psychology of performing so hard under pressure that the obstacle or opponent psychologically breaks first. Unpack Armoring the Mind as the long-term discipline of voluntary suffering. Close with the Stay Hard Challenge â€” a specific act of deliberate discomfort the audience will perform within 24 hours, chosen by them, announced in the room. The default deliverable is a formatted Microsoft Word document.

Read [references/david_goggins_method.md](references/david_goggins_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the David Goggins methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten Goggins into a generic motivational speech. Preserve the anti-motivational stance, the raw biographical testimony, the Governor and 40% Rule with their precise mechanical description, all named tools (Accountability Mirror, Cookie Jar, Taking Souls, Callousing the Mind, Armoring the Mind), the confrontational direct-address tone, and the Stay Hard Challenge close.
- Goggins is the only speaker in this skill library who explicitly argues against motivation as a concept. This is non-negotiable. Any manuscript that positions Goggins as "motivating" the audience has fundamentally misrepresented his methodology. He does not motivate. He confronts.
- Goggins does not use frameworks with elegant names, Eastern philosophy, or neuroscience citations. His authority is entirely experiential and biographical. Every claim he makes is backed by what he has done to his own body and mind â€” not by research papers or other people's stories.
- Goggins's vocabulary is specific and must appear throughout the manuscript: "Stay Hard," "the Governor," "calloused mind," "cookie jar," "accountability mirror," "taking souls," "embrace the suck," "motivation is a lie," "uncommon among the uncommon," "the mental lab," "no finish line," "armor your mind," "be uncommon."
- Corporate-context sensitivity: when producing for a corporate audience, the manuscript must preserve the core confrontational energy and the raw biographical content, but may reduce profanity to near-zero while keeping the unfiltered directness of the message intact. The absence of the F-word does not mean the absence of Goggins's confrontational force.
- If the user asks for David Goggins, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or performance/resilience challenge.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a corporate audience â€” professionals, managers, or teams who are performing adequately but not at their full capacity, using comfort and busyness as excuses to avoid the harder work their potential demands â€” and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of David Goggins while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for:
- Current neuroscience findings on the Governor concept and voluntary effort limitation.
- Contemporary research on deliberate discomfort and its effects on mental resilience and high-performance behavior.
- Recent examples of teams or individuals who applied Goggins-style mental toughness in corporate, athletic, or military contexts.
- The most recent verified details from Goggins's biography (Navy SEAL training, BUDS classes, endurance records, Guinness World Record pull-ups).

## Preparation Rules

- Identify the specific comfortable lie the audience is telling itself before writing any section. This is the core of the confrontation.
- Answer four questions first:
  - What is the specific comfortable excuse this audience uses to justify operating below their capacity?
  - At what percentage of their potential is this audience operating â€” and what does the Governor look like in their specific context?
  - What specific act of deliberate discomfort most directly targets the audience's most comfortable avoidance pattern?
  - What is the one cookie jar entry the speaker (Goggins) draws on that most mirrors the audience's specific challenge?
- Write the Confrontation Thesis before any section: the single sentence that names the specific lie the audience has been telling itself.
- Design the Stay Hard Challenge as a specific, time-bound, uncomfortable act the audience commits to before leaving â€” chosen by them, announced aloud.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Confrontation Thesis (the specific lie the audience is telling itself).
2. The Governor Manifestation (what the audience's 40% cutoff looks like in their specific context).
3. The Callousing Prescription (what type of deliberate discomfort is most relevant for this audience).
4. The Cookie Jar Entry (which Goggins biographical moment most mirrors the audience's challenge).
5. The Taking Souls Application (how the audience can apply this psychology in their specific environment).
6. The Accountability Mirror Questions (the three specific honest questions this audience needs to answer).
7. The Stay Hard Challenge (the specific act of deliberate discomfort the audience commits to in the next 24 hours).

Then write the talk with these clearly signaled sections:

1. A ORIGEM: BUFFALO (Buffalo Origin Story â€” the biographical testimony that earns the right to confront)
2. A MENTIRA DA MOTIVAÃ‡ÃƒO (Motivation Is a Lie â€” the confrontation that defines everything that follows)
3. O GOVERNADOR E A REGRA DOS 40% (The Governor and the 40% Rule â€” the mechanical diagnosis)
4. CALEJAR A MENTE (Callousing the Mind â€” deliberate discomfort as the only legitimate path to toughness)
5. O ESPELHO DA RESPONSABILIDADE (Accountability Mirror â€” radical self-audit tool)
6. O POTE DE COOKIES (Cookie Jar â€” the mental fuel reserve for maximum difficulty)
7. TOMAR ALMAS (Taking Souls â€” performing so hard that the obstacle breaks first)
8. ARMAR A MENTE (Armoring the Mind â€” the long-term discipline of voluntary suffering)
9. O DESAFIO STAY HARD (Stay Hard Challenge â€” the specific commitment to discomfort before leaving)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name, for example: `Resiliencia_Mental_David_Goggins.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Raw, direct, confrontational â€” every sentence must feel like it was spoken by someone who has earned the right to say it through physical and psychological suffering of the highest order.
- First person throughout â€” Goggins speaks entirely from his own experience. He never says "research shows." He says "I know because I've been there."
- Direct-address dominant: "VocÃª estÃ¡ confortÃ¡vel demais." "VocÃª estÃ¡ mentindo para si mesmo." "Eu sei porque jÃ¡ menti para mim mesmo por anos."
- No metaphors from Eastern philosophy, no aphorisms, no poetic register. Goggins's language is blunt, concrete, and earned â€” not elegant.
- The word "motivaÃ§Ã£o" must appear in the context of its rejection: "MotivaÃ§Ã£o Ã© uma mentira."
- "Stay Hard" must appear multiple times â€” as a mantra, as a close, as a refrain.
- The biographical details must be specific and verified: the exact race where he ran 100 miles with broken bones, the specific SEAL training classes, the exact pull-up world record numbers.
- No gentle transitions. Goggins moves abruptly from one point to the next, just as pain arrives without warning.
- The tone is never warm, never pastoral, never poetic. It is the tone of someone who has been through hell and is not going to lie to you about what's there.

## Quality Check

- Verify the opening is the Buffalo Origin Story â€” not a topic announcement, not a definition, not an inspirational quote.
- Verify "MotivaÃ§Ã£o Ã© uma mentira" is stated explicitly and defended with the discipline argument.
- Verify the Governor is described mechanically as the brain's self-imposed limiter, distinct from actual physical capacity.
- Verify the 40% Rule is stated precisely: "Quando a sua mente diz que vocÃª acabou, vocÃª estÃ¡ a apenas 40% da sua capacidade real."
- Verify Callousing the Mind uses deliberate discomfort â€” not general advice about being tough.
- Verify the Accountability Mirror section includes the specific sticky-note-on-the-mirror practice with concrete questions.
- Verify the Cookie Jar section describes the practice of mentally reaching back to past victories during current maximum difficulty.
- Verify Taking Souls is presented as the psychology of performing harder when someone expects you to quit.
- Verify Armoring the Mind is the long-term cumulative practice, distinguished from single acts of toughness.
- Verify the Stay Hard Challenge is specific, uncomfortable, time-bound, and announced aloud by the audience before leaving.
- Verify the tone is confrontational throughout â€” never warm, never encouraging in the conventional sense.
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
