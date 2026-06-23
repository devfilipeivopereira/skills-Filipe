# generate-james-clear-talks

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-james-clear-talks`
- Pacote instalavel: `packages/palestras-motivacao/generate-james-clear-talks.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-james-clear-talks`
- Fonte original: `C:\Users\filip\.codex\skills\generate-james-clear-talks`
- Hash do `SKILL.md`: `a06e6033250084e2e22521ae700143fab01b9896dc0ad2e5a87bf698a8911cb3`

## Resumo

Generate talk outlines and manuscripts in James Clear's habits systems style: baseball injury origin, marginal gains, 3 layers of behavior change, 4 laws, plateau of latent potential, environment design, two-minute rule, never miss twice, and a systems commitment close. Use for habits, productivity, or behavior change talks.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-james-clear-talks.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-james-clear-talks` |
| Skill name | `generate-james-clear-talks` |
| Categoria | `palestras-motivacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-james-clear-talks` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-james-clear-talks` |
| Arquivo principal | `skills/palestras-motivacao/generate-james-clear-talks/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-james-clear-talks.zip` |
| Tamanho do zip | 21,3 KB |
| Duplicatas consolidadas | 2 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-james-clear-talks |
| `description` | Generate talk outlines and manuscripts in James Clear's habits systems style: baseball injury origin, marginal gains, 3 layers of behavior change, 4 laws, plateau of latent potential, environment design, two-minute rule, never miss twice, and a systems commitment close. Use for habits, productivity, or behavior change talks. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 8 |
| Diretorios | 3 |
| Tamanho copiado | 52,4 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 242 B |
| `references` | 1 | 25,1 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate James Clear Talks
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
| `skills/palestras-motivacao/generate-james-clear-talks/agents/openai.yaml` | 242 B |
| `skills/palestras-motivacao/generate-james-clear-talks/references/james_clear_method.md` | 25,1 KB |
| `skills/palestras-motivacao/generate-james-clear-talks/scripts/adapters.py` | 848 B |
| `skills/palestras-motivacao/generate-james-clear-talks/scripts/config.json` | 454 B |
| `skills/palestras-motivacao/generate-james-clear-talks/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-james-clear-talks/scripts/create_talk_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-james-clear-talks/scripts/create_talk_epub.py` | 5,7 KB |
| `skills/palestras-motivacao/generate-james-clear-talks/SKILL.md` | 10,5 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-james-clear-talks`
- `C:\Users\filip\.cursor\skills\generate-james-clear-talks`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-james-clear-talks
description: "Generate talk outlines and manuscripts in James Clear's habits systems style: baseball injury origin, marginal gains, 3 layers of behavior change, 4 laws, plateau of latent potential, environment design, two-minute rule, never miss twice, and a systems commitment close. Use for habits, productivity, or behavior change talks."
---

# Generate James Clear Talks

## Overview

Generate talks with James Clear's authentic methodology: open with the personal baseball injury and recovery that produced the habit system he would later teach the world, establish that small habits compound into extraordinary results via the 1% Better math and the Plateau of Latent Potential, demonstrate that goals are insufficient and systems are the real mechanism of change, present the Three Layers of Behavior Change as the diagnostic framework for why most change efforts fail, teach the Four Laws of Behavior Change as the precise prescriptive toolkit, apply Environment Design as the most underrated lever, introduce Habit Stacking and the Two-Minute Rule as implementation bridges, and close with a system-design commitment the audience builds before leaving. The default deliverable is a formatted Microsoft Word document.

Read [references/james_clear_method.md](references/james_clear_method.md) when writing or reviewing the talk. Treat that file as the source of truth for structure, timing, tone, checkpoints, and required output sections.
Use [scripts/create_talk_docx.py](scripts/create_talk_docx.py) to turn the final manuscript into a `.docx` file and enforce minimum word count before delivery.
Treat [scripts/core.py](scripts/core.py) as the portable logic layer, [scripts/adapters.py](scripts/adapters.py) as the environment adapter layer, and [scripts/config.json](scripts/config.json) as runtime defaults.

## Method Fidelity Rules

- The linked reference file is the governing specification for the James Clear methodology.
- Follow every non-negotiable in that reference exactly, even when this `SKILL.md` summarizes the method more briefly.
- If this `SKILL.md` and the reference file ever differ, the reference file wins.
- Do not flatten James Clear into a generic productivity talk. Preserve the personal baseball injury narrative, the 1% Better compounding math, the Three Layers of Behavior Change, the Four Laws in sequence (Obvious â†’ Attractive â†’ Easy â†’ Satisfying), the Plateau of Latent Potential, Environment Design, Habit Stacking, the Two-Minute Rule, and the system-design close.
- James Clear does not shout, does not use high-energy activation, and does not speak as a motivational guru. He speaks as a researcher-practitioner who has personally tested everything he teaches. Any manuscript that sounds like Tony Robbins or Les Brown has failed the fidelity test.
- If the user asks for James Clear, keep the methodology intact unless the user explicitly asks to depart from it.

## Workflow

1. Confirm the theme or behavioral/performance challenge.
2. If the user did not provide a theme, ask for it directly.
3. If the user did not provide audience profile, context, or length, assume a room of high-achieving professionals â€” executives, athletes, creatives, educators â€” who are goal-oriented but stuck in a cycle of trying and failing because they focus on outcomes instead of systems, and produce a complete talk manuscript.
4. Default to Brazilian Portuguese unless the user asks for another language.
5. Unless the user requests another output format, produce a `.docx` file.
6. Unless the user explicitly requests another destination, save both the manuscript source file and the `.docx` result inside [outputs/](outputs/) in this skill folder.

## Originality Requirement

Every talk must be newly written for the current request. Preserve the distinctive methodology of James Clear while producing original wording for the present request.

## Research Requirement

Before drafting the talk, browse the internet for:
- Current research in behavioral science, habit formation, or neuroscience relevant to the theme.
- Contemporary examples of the 1% Better principle applied in sports, business, medicine, or culture.
- Current statistics on human behavior change success rates â€” they reliably support the argument that goals-only approaches fail.

## Preparation Rules

- Identify the specific behavioral gap the audience faces before building any section.
- Answer four questions first:
  - What is the audience trying to achieve â€” and why their current approach (goal-focused) is failing?
  - At which of the Three Layers are they operating (Outcome, Process, or Identity)?
  - Which of the Four Laws is the most violated in their specific context?
  - What is the specific Two-Minute version of the habit the audience needs to build?
- Write the Core Sentence (the single memorable assertion the talk builds toward) before writing any section: "You do not rise to the level of your goals. You fall to the level of your systems."
- Design the system-design close as a specific, written habit formula the audience fills in before leaving.
- If the request is for a complete talk and no shorter limit is given, enforce at least 7,500 words.

## Output Contract

Before the talk body, explicitly declare:

1. The Core Sentence (the single memorable assertion the talk turns on).
2. The Audience's Behavioral Gap (what they are trying to do, why the current approach fails).
3. The Layer Diagnosis (at which of the Three Layers the audience is currently stuck).
4. The Violated Law (which of the Four Laws is most broken in this audience's context).
5. The 1% Compounding Entry Point (which domain â€” professional, personal, health â€” will anchor the compounding math).
6. The Environment Design Application (the specific environmental change most relevant to this audience).
7. The System-Design Commitment (the exact habit formula the audience writes at the close).

Then write the talk with these clearly signaled sections:

1. O ACIDENTE (Baseball Injury origin story â€” the personal collapse and the system born from it)
2. O PODER DO 1% (Aggregation of Marginal Gains + Plateau of Latent Potential)
3. SISTEMAS, NÃƒO METAS (Goals vs. Systems â€” the counterintuitive reframe)
4. AS TRÃŠS CAMADAS (Three Layers of Behavior Change â€” Outcome, Process, Identity)
5. AS QUATRO LEIS (Four Laws of Behavior Change as the prescriptive toolkit)
6. O DESIGN DO AMBIENTE (Environment Design as the silent architect of behavior)
7. A REGRA DOS DOIS MINUTOS (Two-Minute Rule + Habit Stacking as implementation bridges)
8. O SISTEMA QUE VOCÃŠ VAI CONSTRUIR (System-design close â€” specific written commitment)

## Document Delivery

- Write the talk manuscript to a UTF-8 text or markdown file first inside [outputs/](outputs/).
- Run `scripts/create_talk_docx.py` with `--min-words 7500`.
- Name the `.docx` using the theme plus the speaker name, for example: `Habitos_Atomicos_James_Clear.docx`.
- Copy the `.docx` to `C:\Users\filip\.codex\skills\DOCS_Talks`.
- Run `scripts/create_talk_epub.py` and save the `.epub` to `C:\Users\filip\.codex\skills\EPUB_TALKS`.
- Deliver both file paths to the user, then empty [outputs/](outputs/).

## Style Rules

- Calm, precise, researcher-practitioner tone â€” never motivational guru register.
- Every major claim must be supported by a study, a documented case, or personal experimental evidence.
- Use data as narrative: numbers tell stories. The 1% Better math (1.01^365 = 37.78) must appear and be dramatized, not just stated.
- Simple declarative sentences dominate â€” Clear is famous for one-line insights that feel inevitable after he says them.
- No exclamation marks in analytical sections.
- The Four Laws must always appear in sequence and always with their exact names: Make It Obvious, Make It Attractive, Make It Easy, Make It Satisfying.
- The inversion of each law for breaking bad habits must appear alongside the law.
- Rhetorical questions feel like a scientist leaning across a whiteboard, not a performer on a stage.
- The close is a design exercise, not an emotional peak.

## Quality Check

- Verify the opening is the Baseball Injury story â€” not a generic anecdote about habits.
- Verify the 1% Better compounding math appears with the actual formula (1.01^365 = 37.78 and 0.99^365 = 0.03).
- Verify the Plateau of Latent Potential appears as the patience argument.
- Verify the Systems vs. Goals reframe is counterintuitive and specific â€” not a generic "focus on the process."
- Verify all Three Layers are named and the Identity Layer is presented as the deepest and most powerful.
- Verify all Four Laws appear in sequence with their exact names and inversions.
- Verify Environment Design includes the specific principle: environment is the invisible architect.
- Verify the Two-Minute Rule is stated precisely: any new habit should take less than two minutes to start.
- Verify Habit Stacking uses the exact formula: "After [CURRENT HABIT], I will [NEW HABIT]."
- Verify the close includes a written system-design commitment the audience fills out.
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
