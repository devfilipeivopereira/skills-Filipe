---
name: notion-ebook-from-corrigido
description: Ler um banco do Notion, localizar a coluna corrigido, extrair apenas a parte da pregação de cada página, transformar esse texto em um ebook conversacional em português e gravar o resultado na coluna ebook. Use quando o usuário pedir para processar transcrições ou textos corrigidos no Notion e devolver um ebook por página no próprio banco.
---

# Notion Ebook From Corrigido

Use esta skill para processar um banco do Notion de ponta a ponta: localizar páginas pendentes, extrair o texto da coluna `corrigido`, escrever um ebook pastoral em português com acabamento de livro cristão e salvar o resultado na coluna `ebook`.

## Fluxo

1. Defina as credenciais no shell atual.
2. Inspecione o banco se houver dúvida sobre nomes de colunas.
3. Liste páginas candidatas com `list`, sem baixar o texto completo.
4. Priorize candidatas com material local mais rico antes de escrever.
5. Escolha uma única página e use `pull --page-id` para baixar só ela.
6. Se houver uma pasta local de `corrigidos`, prefira `--local-source-dir` para evitar baixar o `.txt` do Notion novamente.
7. Limpe o material para manter apenas a pregação.
8. Faça um mapa curto da mensagem antes de redigir:
   ideia central
   textos bíblicos usados
   movimentos principais do argumento
   aplicações pastorais legítimas
9. Escreva o ebook em blocos, não de uma vez só, para manter qualidade e evitar repetição estrutural.
10. Valide o arquivo local para garantir 10.000 palavras mínimas e baixa repetição.
11. Grave o resultado na coluna `ebook`.

## Setup

Defina as variáveis de ambiente no PowerShell antes de rodar o script:

```powershell
$env:NOTION_TOKEN = 'seu_token'
$env:NOTION_DATABASE_ID = 'seu_database_id'
```

Se o usuário já tiver fornecido os valores, use-os no shell atual. Evite gravar o token dentro do `SKILL.md`, em prompts, ou em arquivos versionáveis.

## Comandos

Inspecionar o esquema:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" inspect
```

Exportar páginas candidatas para processamento:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" pull --out pending.json
```

Listar candidatas sem baixar `corrigido_text`:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" list --max-pages 10 --local-source-dir "C:\Users\filip\Downloads\notion_corrigidos" --out candidates.json
```

Listar candidatas já priorizando fontes mais fortes:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" list --max-pages 10 --min-local-source-words 6000 --local-source-dir "C:\Users\filip\Downloads\notion_corrigidos" --out candidates.json
```

Baixar apenas um resumo da fonte, sem carregar o texto inteiro:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" pull --page-id "<page_id>" --summary-only --local-source-dir "C:\Users\filip\Downloads\notion_corrigidos" --out pending-summary.json
```

Nesse modo, o script também tenta devolver `sermon_start_hint`, com um trecho do provável início da mensagem bíblica.

Exportar apenas uma página específica:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" pull --page-id "<page_id>" --out pending.json
```

Exportar uma página específica reutilizando `corrigidos` locais:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" pull --page-id "<page_id>" --local-source-dir "C:\Users\filip\Downloads\notion_corrigidos" --out pending.json
```

Exportar poucas candidatas por título:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" pull --title-contains "Jesus transforma" --max-pages 3 --out pending.json
```

Atualizar a coluna `ebook` de uma página específica com um arquivo `.md` ou `.txt`:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" push --page-id "<page_id>" --input-file "ebook.md"
```

Validar antes do upload:

```powershell
python "C:\Users\filip\.codex\skills\notion-ebook-from-corrigido\scripts\notion_ebook_pipeline.py" validate --input-file "ebook.md"
```

## Regras de escrita

Leia [references/ebook-format.md](references/ebook-format.md) antes de redigir o ebook.

Ao transformar o `corrigido` em ebook:

- Preserve somente a parte da pregação.
- Remova abertura de culto, avisos, ofertas, chamadas de inscrição, propaganda, créditos, vinhetas, timestamps e conversa lateral.
- Mantenha a linha teológica e o argumento do pregador.
- Escreva em português do Brasil.
- Entregue no mínimo 10.000 palavras por ebook. Se o material for curto, expanda apenas por desenvolvimento fiel das ideias, explicações, transições, aplicações e aprofundamento pastoral derivados da própria pregação.
- Fale com o leitor de forma direta e pastoral, como uma conversa guiada, com qualidade literária alta e acabamento de livro cristão contemporâneo.
- O texto final deve soar como livro devocional-formativo, não como palestra transcrita nem como artigo inflado.
- Prefira capítulos com progressão clara de raciocínio. Cada capítulo deve levar o leitor adiante.
- Abra com tensão, pergunta, dor, necessidade ou tema humano real. Não comece com explicação meta sobre o que o ebook fará.
- Feche capítulos com aterrissagem pastoral curta, não com repetição do mesmo argumento.
- Mantenha a voz calorosa, bíblica, sóbria e pastoral. Evite tom excessivamente acadêmico, mecânico ou autoparafrástico.
- Não repita blocos, argumentos ou parágrafos apenas para alcançar a meta de palavras. Cada seção precisa acrescentar desenvolvimento real, único e inédito dentro dos limites do sermão original.
- Reestruture para formato de ebook, não de transcrição.
- Use a Bíblia em português brasileiro na versão NVI como padrão quando precisar citar ou normalizar referências bíblicas.
- Não invente ilustrações, citações bíblicas ou aplicações que não estejam sustentadas pelo texto-base.
- Se a transcrição estiver confusa, prefira resumir com fidelidade a preencher lacunas com suposição.

## Processo de redação

Para sair melhor na prática, use esta sequência:

1. Faça `list`.
2. Se houver `local_source_word_count`, prefira materiais com 6.000+ palavras para sustentar um ebook melhor.
3. Faça `pull --page-id ... --summary-only` para identificar o eixo da mensagem sem abrir um JSON gigante.
4. Use `sermon_start_hint` para pular mais rápido a abertura de culto, avisos e transições.
5. Leia o `.txt` local completo apenas da página escolhida.
6. Monte um mapa de 5 itens:
   título provisório
   tese central
   textos bíblicos principais
   5 a 8 capítulos possíveis
   aplicações centrais que de fato vieram da mensagem
7. Escreva o ebook em blocos de capítulos.
8. Depois de 2 ou 3 capítulos, releia o conjunto para cortar ecos e reapresentações.
9. Só no fim rode `validate`.

Se o texto começar a soar como "a mesma ideia em novas palavras", pare e reestruture os capítulos antes de continuar expandindo.
Se o `corrigido` local for muito curto, não tente compensar isso com expansão artificial. Escolha outra página, a menos que o usuário peça explicitamente essa.

## Heurística para separar a pregação

Comece procurando o trecho em que a mensagem bíblica realmente começa. Sinais comuns:

- leitura do texto bíblico
- frase como "abra sua Bíblia", "vamos ler", "a mensagem de hoje", "o texto diz"
- início claro da exposição, argumento ou aplicação do sermão

Pare de considerar material útil quando o texto migrar para:

- avisos da igreja
- pedido de inscrição no canal
- ofertas, PIX, agenda, recados
- despedida técnica, créditos, equipe, trilha, anúncios

Se houver dúvida entre manter ou cortar um trecho, mantenha apenas o que pertence ao desenvolvimento da mensagem.

## Processo recomendado

1. Rode `inspect` apenas se houver qualquer dúvida sobre os nomes das colunas.
2. Para trabalho operacional do dia a dia, prefira:
   `list --max-pages 10 --min-local-source-words 6000` para descobrir pendências já priorizando fontes mais fortes.
   `pull --page-id "<page_id>"` quando o alvo já é conhecido.
3. Se existir cache local de `corrigidos`, sempre tente `--local-source-dir` primeiro para reduzir I/O com o Notion.
4. O matching local agora deve ser exato por nome de arquivo. Só use `--allow-title-fallback` se houver um caso real de nomes divergentes.
5. Use `pull --summary-only` se ainda quiser revisar a fonte sem carregar um JSON enorme.
6. Quando disponível, use `sermon_start_hint` para localizar rapidamente o começo provável da pregação.
7. Trabalhe uma página por vez para manter qualidade.
8. Antes de escrever, extraia a tese e os movimentos reais da mensagem.
9. Gere o ebook em um arquivo local `.md`, em blocos, para evitar perda de qualidade e problemas operacionais com arquivos grandes.
10. Rode `validate --input-file "ebook.md"` e só prossiga se o arquivo passar.
11. Rode `push --page-id "<page_id>" --input-file "ebook.md"` para gravar na coluna `ebook`.
12. Se o banco já tiver `ebook` preenchido e o usuário não pedir overwrite, preserve o conteúdo existente.
13. Em bancos com `Ebook` do tipo `files`, preserve um nome de arquivo legível e estável.

## Observações

- O script faz I/O com o Notion; a escrita do ebook é responsabilidade do agente usando esta skill.
- O principal ganho de qualidade vem do método de escrita, não de tentar expandir o texto bruto imediatamente.
- O script localiza propriedades por nome de forma tolerante a maiúsculas, minúsculas e acentos.
- O script usa a API atual do Notion baseada em `data_sources` e também aceita um `database_id`, resolvendo automaticamente o primeiro data source do banco.
- Esta skill suporta colunas `files`. No banco do usuário, `Corrigido` e `Ebook` podem ser arquivos; nesse caso o script baixa o `.txt` de origem e sobe o ebook final como arquivo na coluna `Ebook`.
- O comando `list` existe para descoberta operacional:
  - retorna candidatas sem `corrigido_text`
  - informa se há arquivo local correspondente
  - informa `local_source_word_count` e `local_source_char_count` quando houver cache local
  - ordena candidatas com mais material primeiro quando essa contagem está disponível
  - aceita `--min-local-source-words` para eliminar fontes curtas demais antes da escrita
  - evita JSONs enormes quando o objetivo ainda é só escolher a próxima página
- O comando `pull` agora aceita:
  - `--page-id` para processar uma única página.
  - `--title-contains` para filtrar por trecho do título.
  - `--local-source-dir` para reutilizar um `.txt` corrigido já salvo localmente.
- `pull --summary-only` devolve apenas `corrigido_summary.head` e `corrigido_summary.tail`, sem despejar o texto inteiro.
- `pull --summary-only` também tenta devolver `sermon_start_hint`, para reduzir o tempo gasto procurando o início real da mensagem.
- Por padrão, `pull` bloqueia exportação de texto completo de múltiplas páginas. Para forçar isso, use `--allow-multi-page-text`.
- Quando `--local-source-dir` encontra o arquivo correspondente, o script usa o arquivo local em vez de baixar novamente o anexo do Notion.
- O fallback por título agora é opcional via `--allow-title-fallback`, para reduzir risco de casar uma página com o arquivo local errado.
- O comando `validate` verifica:
  - mínimo de 10.000 palavras
  - ausência de parágrafos longos duplicados
  - taxa baixa de frases longas repetidas
- O comando `push` roda essa validação por padrão antes do upload. Se falhar, o upload é bloqueado.
- Mesmo quando a validação passar, releia o texto para checar:
  - se está soando como livro e não como sermão expandido artificialmente
  - se cada capítulo realmente avança o argumento
  - se a abertura e o encerramento têm peso pastoral real
