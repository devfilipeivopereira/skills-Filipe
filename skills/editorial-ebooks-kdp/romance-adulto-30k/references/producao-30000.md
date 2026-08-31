# Produção de exatamente 30.000 palavras

## Unidade de contagem

A meta cobre somente a prosa ficcional do manuscrito. O contador ignora front matter YAML, cabeçalhos Markdown, divisores e cercas de código. Palavras com hífen ou apóstrofo interno contam como uma unidade. O resultado de `scripts/count_words.py` é definitivo para esta skill.

## Marcos cumulativos

| Marco | Percentual | Palavra aproximada |
|---|---:|---:|
| Imagem inicial concluída | 1% | 300 |
| Tema declarado | 5% | 1.500 |
| Catalisador | 10% | 3.000 |
| Entrada no ato 2 | 20% | 6.000 |
| História B apresentada | 22–25% | 6.600–7.500 |
| Ponto médio | 50% | 15.000 |
| Tudo está perdido | 75% | 22.500 |
| Entrada no ato 3 | 80% | 24.000 |
| Imagem final começa | 99% | 29.700 |
| Fim | 100% | 30.000 |

Distribuição macro recomendada:

- ato 1: 6.000;
- ato 2A: 9.000;
- ato 2B: 7.500;
- noite escura: 1.500;
- ato 3: 6.000.

## Capítulos e cenas

Padrão: 12 capítulos de 2.500 palavras, com cerca de 36 cenas. Varie naturalmente de 1.800 a 3.200 por capítulo e compense no orçamento. Uma cena comum terá 650–950 palavras, mas interlúdios e clímax podem fugir dessa faixa.

Antes de redigir, crie uma tabela com alvo por capítulo e acumulado. Após cada capítulo, registre real e desvio. Não espere o final para descobrir um excesso de milhares de palavras.

## Ajuste fino sem enchimento

Quando faltar texto, acrescente somente material que cumpra uma função:

- ação que causa a próxima cena;
- reação emocional que muda uma decisão;
- detalhe sensorial que ancora lugar e clima;
- subtexto ou gesto que altera o vínculo;
- preparação/pagamento de elemento já plantado;
- obstáculo que pressiona desejo e necessidade.

Quando sobrar, corte:

- recapitulação do que o leitor acabou de ver;
- saudações e deslocamentos sem conflito;
- emoção nomeada depois de já demonstrada;
- metáforas duplicadas;
- diálogo que repete a mesma posição;
- história de fundo sem efeito presente;
- advérbios e qualificadores redundantes.

Faça ajustes em blocos decrescentes: primeiro centenas, depois dezenas, por fim unidades. Leia o parágrafo inteiro após cada microcorte para preservar concordância e ritmo.

## Comandos

Contagem humana:

`python scripts/count_words.py manuscrito.md --target 30000`

Saída estruturada:

`python scripts/count_words.py manuscrito.md --target 30000 --json`

O processo só passa quando o retorno é zero e a contagem exibida é 30.000.
