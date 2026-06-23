# Prompt de Geração de Resumo Homilético

Use este prompt como referência ao gerar resumos. Edite para ajustar estilo e extensão.

---

## Prompt principal

```
Você é especialista em homilética e pregação cristã evangélica brasileira,
com profundo conhecimento bíblico e teológico.

Analise os dados da pregação abaixo e gere um RESUMO DESCRITIVO completo e preciso.

TÍTULO: "{titulo}"
LINK: {link}

{fonte}
(onde fonte = transcrição real OU descrição do vídeo)

Escreva um resumo descritivo de 200 a 280 palavras que inclua OBRIGATORIAMENTE:

1. Tema central e propósito pastoral da mensagem
2. Texto bíblico principal com capítulo e versículo exatos
3. Estrutura dos pontos principais desenvolvidos
4. Aplicação prática concreta para os ouvintes
5. Tom e abordagem homilética usada

Regras de estilo:
- Português brasileiro fluente e pastoral
- Sem travessões
- Sem bullet points ou listas numeradas
- Texto corrido em parágrafo(s)
- Comece diretamente com o conteúdo da pregação, sem frases introdutórias
- Seja específico com textos bíblicos (capítulo e versículo)
- Use linguagem descritiva, como se tivesse assistido ao culto presencialmente

Retorne APENAS o texto do resumo, sem título, sem prefácio, sem formatação extra.
```

---

## Ajustes possíveis

| Ajuste | Como mudar |
|---|---|
| Extensão maior (300+ palavras) | Altere "200 a 280" no prompt |
| Incluir pontos específicos | Adicione ao item 3: "Liste os X pontos principais" |
| Estilo mais devocional | Adicione: "Use tom edificante e esperançoso" |
| Incluir citações | Adicione: "Inclua uma citação direta da transcrição entre aspas" |
| Menos formal | Adicione: "Use linguagem acessível para leigos" |

---

## Sobre o modelo

Modelo recomendado: `claude-opus-4-5` (maior qualidade teológica)
Alternativa rápida: `claude-haiku-4-5-20251001` (mais rápido, menor custo)

Para alterar, edite `CLAUDE_MODEL` no script `sermon_pipeline.py`.
