# Pitch, descrição e metadados

## Logline

Construa uma frase com:

- herói específico e falho;
- evento/decisão que rompe a estase;
- objetivo externo;
- parceiro ou força romântica;
- obstáculo e risco;
- ironia emocional ligada ao tema.

Teste a logline com seis âncoras: estase que equivale à morte, falha, entrada no ato 2, ponto médio, tema e tudo está perdido. A frase não precisa enumerá-las, mas deve nascer delas.

Modelo auxiliar, a ser reescrito com voz própria:

“Quando [catalisador], uma/um [protagonista + falha] precisa [objetivo] ao lado de [par romântico/contraste], mas [barreira] ameaça [risco], obrigando-a/o a escolher entre [defesa antiga] e [necessidade].”

## Sinopse curta de trabalho

Use três parágrafos:

1. mundo, protagonista, falha, desejo e catalisador;
2. entrada no ato 2, promessa da premissa, relação e complicações;
3. ponto médio, escalada, tema, ameaça de perda e pergunta final sem revelar todo o clímax.

## Descrição comercial

Escreva 150–250 palavras, sem resenhas inventadas, superlativos não verificáveis ou comparação enganosa. Abra com gancho, apresente os dois polos do casal, nomeie a barreira e termine com dilema. Preserve surpresas do terço final.

## `metadata.json`

Exemplo:

```json
{
  "title": "Título",
  "subtitle": "",
  "author": "Kang Arin",
  "language": "pt-BR",
  "publisher": "Kang Arin",
  "description": "Descrição comercial sem marcação HTML.",
  "subjects": ["Fiction / Romance / Contemporary"],
  "keywords": ["romance contemporâneo", "proximidade forçada"],
  "publication_date": "2026-08-31",
  "rights": "Copyright © 2026 Kang Arin. Todos os direitos reservados.",
  "identifier": "urn:uuid:00000000-0000-4000-8000-000000000000",
  "author_bio": ""
}
```

O construtor gera um UUID quando o campo estiver vazio. Não use ISBN inexistente. `keywords` servem ao pacote editorial; `subjects` entram como `dc:subject` no EPUB.

## Consistência para KDP

- Título, subtítulo, nome da autora e série devem coincidir letra por letra entre capa e metadados.
- Não ponha palavras-chave, preço, promoção, ranking ou “bestseller” no título/capa.
- Não declare edição ou série inexistente.
- A autora é sempre Kang Arin neste fluxo.
- O eBook não requer ISBN; use ISBN apenas se o usuário fornecer um válido e autorizado.

## Pacote editorial

`pacote-editorial.md` deve reunir:

- título/subtítulo e nome da autora;
- logline;
- descrição comercial;
- subgênero, tropos e nível de calor;
- público e diferencial;
- 3 assuntos/categorias sugeridos, sem prometer disponibilidade exata no painel;
- até 7 frases-chave honestas;
- avisos de conteúdo;
- HEA ou HFN;
- dados técnicos: idioma, 30.000 palavras, formato EPUB responsivo.
