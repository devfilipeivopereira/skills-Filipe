# Fontes Escaneadas

Gerado em: `2026-06-23T12:12:36.0916036-03:00`

## Estrategia

- Fonte primaria: `C:\Users\filip\.codex\skills`.
- Tambem foram consideradas pastas `skills` de `.agents`, `.claude`, `.cursor`, `.gemini`, `.windsurf`, backups `.codex-*`, `superpowers` e caches de plugins.
- Apenas filhos diretos de uma pasta `skills` com `SKILL.md` entram como pacotes instalaveis.
- Diretorios descendentes que contem outro `SKILL.md` sao tratados como sub-skills/backups e nao entram recursivamente dentro do pacote pai.
- Duplicatas com mesmo pacote base e mesmo hash de `SKILL.md` foram consolidadas; variantes com hash diferente foram mantidas com `--v2`, `--v3` etc.
- Padroes conhecidos de tokens e cookies sao substituidos por placeholders `REDACTED_*` antes de copiar e compactar.

## Raizes

| Raiz | Namespace | Tipo | Skills diretas |
|---|---|---|---:|
| `C:\Users\filip\.agents\skills` | `agents` | Agents local | 62 |
| `C:\Users\filip\.agents\skills\.system` | `agents-system` | Agents system | 3 |
| `C:\Users\filip\.claude\skills` | `claude` | Claude local | 73 |
| `C:\Users\filip\.codex\skills` | `local` | Codex local | 83 |
| `C:\Users\filip\.codex\skills\.system` | `system` | Codex system | 5 |
| `C:\Users\filip\.codex\superpowers\skills` | `superpowers` | Superpowers | 14 |
| `C:\Users\filip\.codex-2\skills` | `codex-2` | Codex backup | 0 |
| `C:\Users\filip\.cursor\skills` | `cursor` | Cursor local | 43 |
| `C:\Users\filip\.gemini\skills` | `gemini` | Gemini local | 56 |
| `C:\Users\filip\.windsurf\skills` | `windsurf` | Windsurf local | 55 |

## Contagens

- Candidatos descobertos: `394`
- Pacotes selecionados: `167`
- Zips gerados: `167`

