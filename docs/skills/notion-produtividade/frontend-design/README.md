# frontend-design

- Categoria: **Notion e Produtividade** (`notion-produtividade`)
- Nome declarado: `frontend-design`
- Pacote instalavel: `packages/notion-produtividade/frontend-design.zip`
- Pasta copiada: `skills/notion-produtividade/frontend-design`
- Fonte original: `C:\Users\filip\.codex\skills\frontend-design`
- Hash do `SKILL.md`: `9658539d5561cb37db5bd87104e069425ef580be8b5ce2eec51a47aad0896d10`

## Resumo

Create distinctive, production-grade frontend interfaces with a strong visual point of view. Use when Codex needs to design or build web pages, app screens, UI components, landing pages, dashboards, or polished frontend interactions, especially when the user wants something creative, memorable, premium, bold, or explicitly non-generic.

## Instalacao individual

```powershell
$zip = "packages/notion-produtividade/frontend-design.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `frontend-design` |
| Skill name | `frontend-design` |
| Categoria | `notion-produtividade` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\frontend-design` |
| Pasta no repositorio | `skills/notion-produtividade/frontend-design` |
| Arquivo principal | `skills/notion-produtividade/frontend-design/SKILL.md` |
| Zip | `packages/notion-produtividade/frontend-design.zip` |
| Tamanho do zip | 2,3 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | frontend-design |
| `description` | Create distinctive, production-grade frontend interfaces with a strong visual point of view. Use when Codex needs to design or build web pages, app screens, UI components, landing pages, dashboards, or polished frontend interactions, especially when the user wants something creative, memorable, premium, bold, or explicitly non-generic. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 2 |
| Diretorios | 1 |
| Tamanho copiado | 4,3 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `agents` | 1 | 241 B |

## Secoes internas detectadas

- Frontend Design
-   Workflow
-   Design Rules
-   Anti-Patterns
-   Implementation Notes
-   Finish Line

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/notion-produtividade/frontend-design/agents/openai.yaml` | 241 B |
| `skills/notion-produtividade/frontend-design/SKILL.md` | 4,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\frontend-design`

## Conteudo integral do SKILL.md

```
markdown
---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with a strong visual point of view. Use when Codex needs to design or build web pages, app screens, UI components, landing pages, dashboards, or polished frontend interactions, especially when the user wants something creative, memorable, premium, bold, or explicitly non-generic.
---

# Frontend Design

Build real working frontend code with a clear aesthetic thesis. Avoid default "AI template" decisions and make the result feel intentionally designed for the product, audience, and context.

## Workflow

1. Inspect the existing codebase, stack, and design language before changing the UI.
2. Identify the interface purpose, target audience, technical constraints, and emotional tone.
3. Commit to one strong direction before coding. Choose a concrete aesthetic such as editorial, brutalist, retro-futurist, organic, luxury, industrial, playful, or ultra-minimal.
4. Define the memorable hook that gives the interface character: typography, composition, color contrast, motion, texture, or a specific visual device.
5. Implement production-grade code that is responsive, accessible, and consistent with the chosen framework and repo conventions.
6. Refine spacing, interaction states, empty/loading/error cases, and mobile behavior before finishing.

If the user underspecifies the design, choose a bold direction that fits the request and state the assumption after implementing it.

## Design Rules

- Commit to a specific aesthetic instead of averaging several styles together.
- Respect existing product patterns when working inside an established design system; add distinctiveness through composition, hierarchy, motion, and detail rather than arbitrary inconsistency.
- Use typography intentionally. Prefer distinctive pairings over defaults. Avoid generic choices such as Arial, Inter, Roboto, or system fonts unless the codebase or brand already requires them.
- Use CSS variables or the project's token system for color, spacing, radius, shadow, and motion values.
- Prefer dominant colors with deliberate accents over timid, evenly distributed palettes.
- Build atmosphere with gradients, meshes, texture, noise, transparency, borders, or shadows that match the concept.
- Use asymmetry, overlap, scale contrast, negative space, or grid-breaking moments when they strengthen the concept.
- Use motion sparingly but meaningfully. Favor a few high-impact transitions or staggered reveals over many weak micro-interactions.
- Preserve accessibility with contrast, keyboard reachability, semantic structure, reduced-motion fallbacks, and visible focus states.
- Match implementation complexity to the aesthetic. Minimalism needs restraint and precision; maximalism needs full follow-through.

## Anti-Patterns

- Do not produce cookie-cutter hero sections, generic SaaS cards, or interchangeable dashboard shells.
- Do not default to purple-on-white gradient aesthetics unless the brand explicitly calls for them.
- Do not reuse the same font, palette, or layout pattern across unrelated requests.
- Do not add motion everywhere; animation should support hierarchy, clarity, or delight.
- Do not ship unfinished polish such as uneven spacing, inconsistent radii, broken mobile layouts, or missing hover and focus states.

## Implementation Notes

- Start by shaping layout and content hierarchy before tuning decorative details.
- Prefer maintainable HTML, CSS, and component code over fragile visual tricks.
- Follow repo conventions and reuse existing primitives before inventing new abstractions.
- Make desktop and mobile both feel intentional, not merely compressed versions of the same layout.
- Add comments only when an interaction or design choice would otherwise be hard to understand from the code alone.

## Finish Line

Before returning work, verify that:

- the interface has one recognizable visual idea
- typography and color feel intentional
- relevant interaction states are covered
- spacing, alignment, and responsiveness are polished
- the result feels tailored to the request rather than boilerplate
```
