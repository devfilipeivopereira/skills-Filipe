# Instalacao Individual das Skills

Cada `.zip` em `packages/` contem uma pasta de skill pronta para copiar ou extrair.

## Instalar no Codex

```powershell
$zip = "packages\categoria\nome-da-skill.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Instalar em outra pasta

Troque `$destino` pela pasta de skills da IA desejada, como `.agents\skills`, `.claude\skills`, `.cursor\skills`, `.gemini\skills` ou `.windsurf\skills`.

## Observacoes

- O nome do pacote pode ter prefixos como `vercel-`, `figma-`, `system-` ou `superpowers-` para evitar colisao.
- Pacotes com sufixo `--v2`, `--v3` etc. representam variantes reais com `SKILL.md` diferente.
- A origem exata de cada pacote esta em `docs/manifest.json`.

