# Deployment Notes

## Sincronização local das plataformas

Sempre que o core do `kdp-notion-agent` mudar, sincronize a instalação local da skill em:

- `C:\Users\filip\.claude\skills\kdp-notion-agent`
- `C:\Users\filip\.gemini\skills\kdp-notion-agent`
- `C:\Users\filip\.cursor\skills\kdp-notion-agent`
- `C:\Users\filip\.cursor\skills-cursor\kdp-notion-agent`
- `C:\Users\filip\.windsurf\skills\kdp-notion-agent`

## Regra atual de fonte editorial

- priorizar `Corrigido` quando existir no Notion
- usar `Transcrições` automaticamente apenas para sermões anteriores a `2024-10-01`
- nunca reprovar um caso pelo tamanho do texto-fonte
- exigir o mínimo de `15.000` palavras apenas do ebook final

## Objetivo da sincronização

Garantir que todas as plataformas trabalhem com o mesmo comportamento editorial e com o mesmo padrão fixo de DOCX, CTA, hyperlinks e publicação no Notion.
