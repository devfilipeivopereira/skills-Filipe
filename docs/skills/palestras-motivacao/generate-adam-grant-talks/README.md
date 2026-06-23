# generate-adam-grant-talks

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-adam-grant-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-adam-grant-talks.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-adam-grant-talks`
- Fonte original: `C:\Users\filip\.codex\skills\generate-adam-grant-talks`
- Hash do `SKILL.md`: `65271d083d118ef3e23ce45502faf091832b35df9f203b8f4bcb3d6ad33ac750`

## Resumo

Generate talk outlines and manuscripts in Adam Grant's org-psych style: counterintuitive research opening, Preacher/Prosecutor/Politician diagnostic, Scientist Mode, Confident Humility, psychological safety, Challenge Network, Rethinking Cycle, and an intellectual commitment close. Use for leadership, innovation, learning-culture, or rethinking talks in the Think Again/Originals style.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-adam-grant-talks.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-adam-grant-talks` |
| Skill name | `generate-adam-grant-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-adam-grant-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-adam-grant-talks` |
| Arquivo principal | `skills/palestras-motivacao/generate-adam-grant-talks/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-adam-grant-talks.zip` |
| Tamanho do zip | 20,2 KB |
| Duplicatas consolidadas | 2 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-adam-grant-talks |
| `description` | Generate talk outlines and manuscripts in Adam Grant's org-psych style: counterintuitive research opening, Preacher/Prosecutor/Politician diagnostic, Scientist Mode, Confident Humility, psychological safety, Challenge Network, Rethinking Cycle, and an intellectual commitment close. Use for leadership, innovation, learning-culture, or rethinking talks in the Think Again/Originals style. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 51,4 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 243 B |
| `references` | 1 | 24,1 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate Adam Grant Talks
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
| `skills/palestras-motivacao/generate-adam-grant-talks/agents/openai.yaml` | 243 B |
| `skills/palestras-motivacao/generate-adam-grant-talks/references/adam_grant_method.md` | 24,1 KB |
| `skills/palestras-motivacao/generate-adam-grant-talks/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-adam-grant-talks/scripts/config.json` | 453 B |
| `skills/palestras-motivacao/generate-adam-grant-talks/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-adam-grant-talks/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-adam-grant-talks/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-adam-grant-talks/SKILL.md` | 10,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-adam-grant-talks`
- `C:\Users\filip\.cursor\skills\generate-adam-grant-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-adam-grant-talks
description: "Generate talk outlines and manuscripts in Adam Grant's org-psych style: counterintuitive research opening, Preacher/Prosecutor/Politician diagnostic, Scientist Mode, Confident Humility, psychological safety, Challenge Network, Rethinking Cycle, and an intellectual commitment close. Use for leadership, innovation, learning-culture, or rethinking talks in the Think Again/Originals style."
---

# Generate Adam Grant Talks

## Overview

Generate talks with Adam Grant's authentic organizational psychology methodology: open with a surprising research finding that contradicts what the audience believes (the counterintuitive reveal), apply the Preacher-Prosecutor-Politician diagnostic to show the three cognitive modes that prevent rethinking, prescribe Scientist Mode as the alternative (holding beliefs as hypotheses and updating them based on evidence), introduce Confident Humility as the leadership identity that makes rethinking possible, apply psychological safety as the organizational lever that enables collective rethinking, present the Challenge Network as the structural alternative to echo chambers, walk through the Rethinking Cycle, and close with a specific intellectual commitment about one belief the audience will scrutinize differently. The default deliverable is a formatted Microsoft Word document.

Read [references/adam_grant_method.md](references/adam_grant_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the Adam Grant methodology.
- Follow every non-negotiable in that reference exactly.
- Do not flatten Grant into a generic critical thinking talk. Preserve the counterintuitive research opening, the Preacher-Prosecutor-Politician diagnostic with all three modes described precisely, Scientist Mode, Confident Humility, psychological safety as an organizational lever, the Challenge Network, the Rethinking Cycle, and the intellectual commitment close.
- Grant's humor is dry, self-deprecating, and data-adjacent â€” he makes jokes about research findings and about his own overconfidence. Any manuscript without at least one of these moments has failed the tone fidelity test.
- Grant is a professor-practitioner. His authority is academic first, applied second. Citations and studies must appear â€” not as footnotes, but as stories. The research is the narrative, not the footnote.
- If the user asks for Adam Grant, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or organizational/intellectual challenge.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a room of intelligent, accomplished professionals â€” executives, senior managers, academics, knowledge workers â€” who are good at thinking and precisely because of that, worse at rethinking. Produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of Adam Grant while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for:
- Current organizational psychology research relevant to the theme.
- Recent studies on psychological safety, intellectual humility, or learning cultures.
- Contemporary examples of organizations that practiced or failed to practice collective rethinking.
- Grant's most recent publications, talks, or newsletter content related to the theme.

## Preparation Rules

- Identify the counterintuitive research finding that will anchor the opening before writing any section.
- Answer four questions first:
  - What does the audience currently believe that the research contradicts?
  - In which of the three modes (Preacher, Prosecutor, or Politician) is this audience most often operating?
  - What is the specific organizational or personal context where Scientist Mode would most change their outcomes?
  - What is the one belief the audience holds â€” about leadership, innovation, learning, people, or organizations â€” that they should scrutinize before leaving?
- Write the Counterintuitive Opening Finding before writing any section.
- Design the intellectual commitment close as a specific belief examination, not a behavior change.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Counterintuitive Research Finding (the specific finding that contradicts the audience's assumption).
2. The Dominant Mode Diagnosis (which of the three modes â€” Preacher, Prosecutor, Politician â€” this audience most often uses).
3. The Scientist Mode Application (the specific domain where Scientist Mode would most change this audience's outcomes).
4. The Psychological Safety Application (the specific organizational behavior or cultural norm this audience needs to change).
5. The Challenge Network Design (the specific type of critic this audience is missing).
6. The Self-Deprecating Humor Moment (where Grant humanizes himself through his own overconfidence or error).
7. The Intellectual Commitment (the specific belief the audience commits to scrutinizing differently).

Then write the talk with these clearly signaled sections:

1. A DESCOBERTA SURPREENDENTE (Counterintuitive research finding â€” the opening that reverses assumption)
2. OS TRÃŠS MODOS (Preacher-Prosecutor-Politician diagnostic)
3. O MODO CIENTISTA (Scientist Mode as the prescriptive alternative)
4. A HUMILDADE CONFIANTE (Confident Humility as the leadership identity)
5. A SEGURANÃ‡A PSICOLÃ“GICA (Psychological safety as the organizational lever)
6. A REDE DE DESAFIO (Challenge Network as the structural alternative to echo chambers)
7. O CICLO DE REPENSAR (The Rethinking Cycle â€” recognizing ignorance, feeling surprised, curiosity, opening the mind)
8. O COMPROMISSO INTELECTUAL (Specific intellectual commitment at the close)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name: `Repensar_Organizacoes_Adam_Grant.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Professor-practitioner tone: intellectually serious, with dry humor, never condescending.
- Research findings are stories, not footnotes. Name the researchers, describe the context, reveal the surprising result.
- Dry humor about research findings and about Grant's own overconfidence is mandatory.
- Never emotional activation without evidence. Grant earns the emotional moment through data first.
- Rhetorical questions feel like a Wharton seminar â€” the professor genuinely wants the answer, not just the effect.
- The Preacher-Prosecutor-Politician framework must be described with behavioral precision â€” not as vague archetypes but as specific cognitive patterns the audience recognizes in themselves.
- Psychological safety must be distinguished from comfort and from niceness â€” Grant explicitly corrects these confusions.
- The close is an intellectual commitment, not an emotional high or a behavior prescription.

## Quality Check

- Verify the opening is a counterintuitive research finding â€” not a question, not an anecdote, not a definition.
- Verify all three modes (Preacher, Prosecutor, Politician) are named and described with behavioral precision.
- Verify Scientist Mode is presented as the prescriptive alternative with a specific organizational example.
- Verify Confident Humility is distinguished from both arrogance and imposter syndrome.
- Verify psychological safety is distinguished from comfort, niceness, and conflict-avoidance.
- Verify the Challenge Network is presented as a structural design, not just a suggestion to find critics.
- Verify the Rethinking Cycle includes all four steps: recognizing ignorance, feeling surprised, feeling curious, opening the mind.
- Verify at least one self-deprecating humor moment is present.
- Verify the close is an intellectual commitment about a specific belief â€” not a behavioral habit prescription.
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
