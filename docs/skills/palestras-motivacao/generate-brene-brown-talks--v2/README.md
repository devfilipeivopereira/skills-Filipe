# generate-brene-brown-talks--v2

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-brene-brown-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-brene-brown-talks--v2.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-brene-brown-talks--v2`
- Fonte original: `C:\Users\filip\.gemini\skills\generate-brene-brown-talks`
- Hash do `SKILL.md`: `6a13e97067f87d39e334f785fa59b8084c13c036e874c14c847846e028190a77`

## Resumo

Generate motivational talk outlines and full talk manuscripts using Brené Brown's authentic research-based methodology, including the researcher's confession opening, operational definitions, counterintuitive data reveal, the arena metaphor from Roosevelt, the BRAVING framework, and a quiet courage invitation close. Use when the user asks to create a motivational talk, keynote, leadership message, conference speech, vulnerability talk, shame resilience message, wholehearted living talk, or courage-based communication and wants the result shaped by Brené Brown, The Power of Vulnerability, Daring Greatly, Dare to Lead, Rising Strong, Braving the Wilderness, shame resilience research, wholehearted living, armored versus daring leadership, or research-based emotional intelligence.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-brene-brown-talks--v2.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-brene-brown-talks--v2` |
| Skill name | `generate-brene-brown-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `gemini` |
| Tipo da fonte | Gemini local |
| Fonte original | `C:\Users\filip\.gemini\skills\generate-brene-brown-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-brene-brown-talks--v2` |
| Arquivo principal | `skills/palestras-motivacao/generate-brene-brown-talks--v2/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-brene-brown-talks--v2.zip` |
| Tamanho do zip | 14,6 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-brene-brown-talks |
| `description` | Generate motivational talk outlines and full talk manuscripts using Brené Brown's authentic research-based methodology, including the researcher's confession opening, operational definitions, counterintuitive data reveal, the arena metaphor from Roosevelt, the BRAVING framework, and a quiet courage invitation close. Use when the user asks to create a motivational talk, keynote, leadership message, conference speech, vulnerability talk, shame resilience message, wholehearted living talk, or courage-based communication and wants the result shaped by Brené Brown, The Power of Vulnerability, Daring Greatly, Dare to Lead, Rising Strong, Braving the Wilderness, shame resilience research, wholehearted living, armored versus daring leadership, or research-based emotional intelligence. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 34,6 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 225 B |
| `references` | 1 | 10,4 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate Brené Brown Talks
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

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/agents/openai.yaml` | 225 B |
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/references/brene_brown_method.md` | 10,4 KB |
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/scripts/config.json` | 454 B |
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-brene-brown-talks--v2/SKILL.md` | 7,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.gemini\skills\generate-brene-brown-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-brene-brown-talks
description: Generate motivational talk outlines and full talk manuscripts using Brené Brown's authentic research-based methodology, including the researcher's confession opening, operational definitions, counterintuitive data reveal, the arena metaphor from Roosevelt, the BRAVING framework, and a quiet courage invitation close. Use when the user asks to create a motivational talk, keynote, leadership message, conference speech, vulnerability talk, shame resilience message, wholehearted living talk, or courage-based communication and wants the result shaped by Brené Brown, The Power of Vulnerability, Daring Greatly, Dare to Lead, Rising Strong, Braving the Wilderness, shame resilience research, wholehearted living, armored versus daring leadership, or research-based emotional intelligence.
---

# Generate Brené Brown Talks

## Overview

Generate motivational talks with Brené Brown's authentic methodology: open as a researcher who found data she didn't want to find, define terms with research precision, reveal a counterintuitive finding that contradicts the audience's dominant belief, use Roosevelt's arena metaphor as the emotional peak, ground the transformation in the BRAVING framework or wholehearted living principles, and close with a quiet, honest invitation to courage. The default deliverable is a formatted Microsoft Word document.

Read [references/brene_brown_method.md](references/brene_brown_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Brené Brown methodology.
- Follow every non-negotiable in that reference exactly.
- Do not flatten Brené Brown into a generic vulnerability talk. Preserve the research foundation, the operational definitions, the counterintuitive data reveal, the shame-vs-guilt distinction, the arena metaphor, and the quiet courage close.
- The researcher identity is non-negotiable: Brown speaks as a scientist who was confronted by her own data, not as a motivational speaker.

## Workflow

1. Confirm the theme or emotional/leadership challenge.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile or context, assume a room of leaders, professionals, or high-achievers who have built armor against vulnerability and are paying the cost in connection, creativity, and meaning, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of Brené Brown while producing original wording and movement for the present request.

## Research Requirement

Before drafting the talk, browse the internet for current research findings, organizational examples, or cultural illustrations that support the theme being addressed. Verify any neuroscience or social science claims before using them.

## Preparation Rules

- Identify the dominant cultural belief the audience holds that the data contradicts.
- Answer three questions first:
  - What does the audience believe about vulnerability, courage, or shame that the research disproves?
  - What is the operationally precise definition of the central concept that the talk turns on?
  - What is the researcher's confession — the personal moment when the data confronted Brown herself?
- Write the Counterintuitive Finding (the single sentence that reverses the audience's assumption) before writing the talk body.
- Identify which BRAVING elements or Wholehearted living practices are most relevant to the audience's specific challenge.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Dominant Belief Being Challenged (what the audience currently assumes about the central concept).
2. The Counterintuitive Finding (the single data-based sentence that reverses the assumption).
3. The Researcher's Confession (the personal moment when the data confronted Brown).
4. The Operational Definition (the precise definition of the central concept).
5. The BRAVING or Wholehearted Framework Application (which elements apply to this audience).
6. The Arena Metaphor Application (how Roosevelt's quote connects to the specific audience's challenge).
7. The Courage Invitation (the exact phrasing of the quiet close).

Then write the talk with these clearly signaled sections:

1. A CONFISSÃO DA PESQUISADORA (Researcher confession — data she didn't want to find)
2. A DEFINIÇÃO (Operational definition of the central concept)
3. OS DADOS (The counterintuitive research finding)
4. A DISTINÇÃO (Shame vs. guilt distinction, or the key conceptual separation this talk turns on)
5. A ARENA (Roosevelt's arena metaphor as emotional peak)
6. A FERRAMENTA (BRAVING framework or Wholehearted practices)
7. O CONVITE À CORAGEM (Quiet courage invitation)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name, for example: `Vulnerabilidade_e_Coragem_Brene_Brown.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Sound like a researcher sitting across the kitchen table from the audience — not performing, confessing.
- Never use motivational-speaker language: no "you can do it", no empty affirmations.
- Every claim about human behavior must feel data-grounded, even if not explicitly cited.
- Use precise vocabulary: do not conflate shame and guilt, vulnerability and weakness, courage and recklessness.
- Self-deprecating humor is allowed — and expected. Brown is authentically imperfect on stage.
- Never use exclamation marks for emphasis in analytical sections.
- The close is always a quiet, honest invitation — never a command, never an urgency-driven call-to-action.

## Quality Check

- Verify the opening positions Brown as a researcher surprised by her own findings, not as a motivational speaker.
- Verify the central concept is operationally defined, not assumed.
- Verify the counterintuitive finding contradicts what the audience believes.
- Verify shame and guilt are clearly distinguished (or the equivalent conceptual separation for the specific topic).
- Verify the Roosevelt arena metaphor is included as the emotional peak.
- Verify the BRAVING framework or Wholehearted practices are used as the practical tool.
- Verify the close is a quiet invitation to specific courage, not a generic inspirational close.
- Verify the generated `.docx` meets the minimum word count.

## Final Cleanup Rule

After the final `.docx` and `.epub` have been delivered, the local `outputs/` folder must be emptied while preserving the folder itself.
```
