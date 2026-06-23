# financeiro-ifc

- Categoria: **Desenvolvimento e DevOps** (`desenvolvimento-devops`)
- Nome declarado: `financeiro-ifc`
- Pacote instalavel: `packages/desenvolvimento-devops/financeiro-ifc.zip`
- Pasta copiada: `skills/desenvolvimento-devops/financeiro-ifc`
- Fonte original: `C:\Users\filip\.codex\skills\financeiro-ifc`
- Hash do `SKILL.md`: `494a70b800ce592e314c1e4a1ebe9557f0cdf7428a8ca98d4e382611b165fe31`

## Resumo

Use sempre que o usuário enviar planilhas mensais de Movimento de Caixa e/ou Movimento de Banco da igreja (arquivos tipo Junho.xlsx, Julho.xlsx, com abas CxXXX/BcXXX) e pedir para tratar, consolidar, padronizar ou preparar os dados para importação num sistema financeiro. Gera duas planilhas consolidadas — Banco e Caixa — com as colunas Data, Tipo, Método, Descrição, Categoria, Sub-Categoria, Código Sub-Categoria e Valor, aplicando a classificação oficial de contas, normalização de sinais, mapeamento de transferências e marcação de pendências em amarelo.

## Instalacao individual

```powershell
$zip = "packages/desenvolvimento-devops/financeiro-ifc.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `financeiro-ifc` |
| Skill name | `financeiro-ifc` |
| Categoria | `desenvolvimento-devops` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\financeiro-ifc` |
| Pasta no repositorio | `skills/desenvolvimento-devops/financeiro-ifc` |
| Arquivo principal | `skills/desenvolvimento-devops/financeiro-ifc/SKILL.md` |
| Zip | `packages/desenvolvimento-devops/financeiro-ifc.zip` |
| Tamanho do zip | 8,1 KB |
| Duplicatas consolidadas | 1 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | financeiro-ifc |
| `description` | Use sempre que o usuário enviar planilhas mensais de Movimento de Caixa e/ou Movimento de Banco da igreja (arquivos tipo Junho.xlsx, Julho.xlsx, com abas CxXXX/BcXXX) e pedir para tratar, consolidar, padronizar ou preparar os dados para importação num sistema financeiro. Gera duas planilhas consolidadas — Banco e Caixa — com as colunas Data, Tipo, Método, Descrição, Categoria, Sub-Categoria, Código Sub-Categoria e Valor, aplicando a classificação oficial de contas, normalização de sinais, mapeamento de transferências e marcação de pendências em amarelo. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 3 |
| Diretorios | 2 |
| Tamanho copiado | 20,7 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `references` | 1 | 4,9 KB |
| `scripts` | 1 | 7,8 KB |

## Secoes internas detectadas

- Financeiro IFC — Tratamento de Planilhas de Caixa e Banco
-   Visão geral
-   Layout de saída (obrigatório)
-   Estrutura dos arquivos de entrada
-   Regras de tratamento
-   Fluxo de execução
-   Formatação visual
-   Regras importantes

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/desenvolvimento-devops/financeiro-ifc/references/classificacao.json` | 4,9 KB |
| `skills/desenvolvimento-devops/financeiro-ifc/scripts/processar.py` | 7,8 KB |
| `skills/desenvolvimento-devops/financeiro-ifc/SKILL.md` | 8,0 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\financeiro-ifc`

## Conteudo integral do SKILL.md

````
markdown
---
name: financeiro-ifc
description: Use sempre que o usuário enviar planilhas mensais de Movimento de Caixa e/ou Movimento de Banco da igreja (arquivos tipo Junho.xlsx, Julho.xlsx, com abas CxXXX/BcXXX) e pedir para tratar, consolidar, padronizar ou preparar os dados para importação num sistema financeiro. Gera duas planilhas consolidadas — Banco e Caixa — com as colunas Data, Tipo, Método, Descrição, Categoria, Sub-Categoria, Código Sub-Categoria e Valor, aplicando a classificação oficial de contas, normalização de sinais, mapeamento de transferências e marcação de pendências em amarelo.
---

# Financeiro IFC — Tratamento de Planilhas de Caixa e Banco

## Visão geral

Esta skill recebe os arquivos mensais (cada `.xlsx` tem uma aba de Caixa e uma de Banco) e produz **dois arquivos consolidados**:

- `Banco_2025.xlsx` — todos os lançamentos das abas de Banco.
- `Caixa_2025.xlsx` — todos os lançamentos das abas de Caixa.

Ambos no layout exigido pelo sistema de importação, com 8 colunas, códigos de 3 dígitos e classificação oficial aplicada.

A skill é autocontida. A classificação oficial fica em `references/classificacao.json` e a lógica em `scripts/processar.py`. Não dependa de conhecimento externo: leia sempre o JSON de classificação.

## Layout de saída (obrigatório)

Cada planilha tem exatamente estas colunas, nesta ordem:

`Data | Tipo | Método | Descrição | Categoria | Sub-Categoria | Código Sub-Categoria | Valor`

Regras de preenchimento:

- **Data**: data do lançamento, formato `DD/MM/YYYY`.
- **Tipo**: `Receita`, `Despesa` ou `Neutra` (Neutra apenas para Movimentação Bancária 90x).
- **Método**: `Banco` na planilha de Banco, `Caixa` na planilha de Caixa (valor fixo por arquivo).
- **Descrição**: o texto do "Histórico" da origem (renomeado para Descrição), com espaços extras removidos.
- **Categoria**: nome da categoria-mãe (ex.: Entradas, Pessoal, Missões, Ministérios, Despesas Gerais, Capacitação, Manutenção, Patrimônio, Denominação, Movimentação Bancária).
- **Sub-Categoria**: nome da subcategoria correspondente ao código.
- **Código Sub-Categoria**: código de **3 dígitos como texto**, com zeros à esquerda (`001`, `002`, `101`, `306`, `902`).
- **Valor**: número. **Receita = positivo**, **Despesa = negativo**. Para Neutra, segue o crédito (entra +) / débito (sai −).

## Estrutura dos arquivos de entrada

Cada mês é um `.xlsx` com duas abas. Os nomes variam (CxJun25, BcJun25, CxJul2025, BcJul2025, BcAgo25, CxAgo25, etc.), então **identifique a aba pelo prefixo**: começa com `Cx` = Caixa, começa com `Bc` = Banco.

Em todas as abas, a **linha 6 é o cabeçalho** (`Dia/Mes`, `Histórico`, `Tipo`, `Minist`, `Crédito`, `Débito`, `Saldo`). Os dados começam na linha 7+.

Layout de colunas (0-based) por tipo de aba:

- **Caixa (Cx)**: `[Data, Histórico, Código(coluna "Tipo"), Minist, Crédito, Débito, Saldo]`
- **Banco (Bc)**: `[Data, nº sequencial, Histórico, Código(coluna "Tipo"), Minist, Crédito, Débito, Saldo]`

Atenção: a coluna chamada **"Tipo"** na origem contém na verdade o **código numérico** da subcategoria.

## Regras de tratamento

1. **Linhas válidas**: só processe linhas cuja primeira célula seja uma data real. Ignore: linha de cabeçalho, "Saldo do Mês Anterior", "Saldo Final…", e linhas-cabeçalho de agrupamento sem valor (ex.: `Entradas`, `Fatura Cartão de crédito R$ ... Sendo :`). Uma linha sem Crédito e sem Débito é descartada.

2. **Tipo e sinal do Valor**:
   - Se houver valor em **Crédito** → `Receita`, Valor = `+|crédito|`.
   - Se houver valor em **Débito** → `Despesa`, Valor = `−|débito|`.
   - **Normalize o sinal sempre pela coluna** (Crédito/Débito), ignorando o sinal digitado na origem. A origem às vezes lança despesas como positivo; corrija para negativo.

3. **Classificação**: use o código numérico da origem para buscar Tipo/Categoria/Sub-Categoria em `references/classificacao.json`. Grave o código com 3 dígitos (zero-padded, como texto).

4. **Transferências / Movimentação Bancária** (categoria "Movimentação Bancária", Tipo "Neutra"):
   - Histórico `RESGATE` ou começando com `Resgate Aplic` → código **902** (Resgate Aplicação).
   - Histórico `APLICAÇÃO` → código **903** (Aplicação Financeira).
   - `Transferência Entre Contas Cresol` → código **901**.
   - Esses códigos podem aparecer na coluna de código OU apenas no Histórico — detecte por ambos.

5. **Códigos antigos / desconhecidos**: se o código da origem não existir na classificação atual (ex.: 202, 208, 209 do esquema antigo de Missões), deixe **Categoria, Sub-Categoria e Código em branco** e **pinte as células de Sub-Categoria e Código de amarelo** (`FFFF00`) para revisão manual. Defina o Tipo pelo crédito/débito mesmo assim. Reporte ao usuário quantas linhas amarelas ficaram.

6. **Regras por Descrição (prioridade máxima)**: certas descrições têm classificação fixa, independentemente do código numérico lançado na origem. Estas regras **sobrescrevem** o código da origem e são aplicadas por correspondência de texto (sem acento, minúsculas). Ordem de avaliação (primeira que casar vence):

   | Texto na Descrição contém | Código | Categoria / Sub-Categoria |
   |---|---|---|
   | `ramon e ana` | 205 | Missões / Missão Projeto Espanha - Ramon e Ana |
   | `pense laranja` | 303 | Ministérios / Ministério Infantil |
   | `missionarios cobim` | 204 | Missões / Missionários COBIM SC |
   | `agencia missionaria` | 207 | Missões / Agência Missionária |
   | `projeto missionario natal` | 204 | Missões / Missionários COBIM SC |
   | `projeto missionario picarras` | 204 | Missões / Missionários COBIM SC |
   | `projeto missionario itapema` | 204 | Missões / Missionários COBIM SC |
   | `projeto missionario itajai` | 204 | Missões / Missionários COBIM SC |

   Essas regras ficam em `DESC_RULES` no `scripts/processar.py`. Para adicionar novas, basta inserir uma linha lá. Com elas, os antigos códigos 202/208/209 de Missões deixam de cair em amarelo.

## Fluxo de execução

1. Liste os arquivos enviados em `/mnt/user-data/uploads/`. Cada `.xlsx` mensal deve ter uma aba Cx e uma Bc.
2. Leia `references/classificacao.json`.
3. Rode o script de processamento:

```bash
cd /caminho/da/skill
python scripts/processar.py --uploads /mnt/user-data/uploads --out /mnt/user-data/outputs --ano 2025
```

O script:
- Detecta automaticamente as abas Cx/Bc de cada arquivo.
- Aplica todas as regras acima.
- Gera `Banco_<ano>.xlsx` e `Caixa_<ano>.xlsx` em `--out`.
- Imprime um JSON com: nº de linhas por planilha, nº de linhas amarelas (pendentes), lista de códigos desconhecidos encontrados e a soma de valores (para conferência).

4. **Conferência**: a soma da coluna Valor de cada planilha deve bater com a soma de (Crédito + Débito) normalizada da origem. Note que a coluna "Saldo" dos arquivos originais costuma ter inconsistências manuais — **não use o Saldo como validação**; use a soma Crédito/Débito.
5. Apresente os dois arquivos com `present_files` e reporte: total de lançamentos, linhas pendentes (amarelas) e qualquer código desconhecido.

## Formatação visual

- Fonte Arial. Cabeçalho com fundo azul-escuro (`1F3864`), texto branco, negrito, centralizado.
- Congelar a primeira linha (`freeze_panes='A2'`) e habilitar AutoFiltro.
- Larguras sugeridas: Data 12, Tipo 10, Método 10, Descrição 52, Categoria 16, Sub-Categoria 40, Código 18, Valor 14.
- Valor com formato `#,##0.00;[Red](#,##0.00)`.
- Não use a função "Design" / layout de página do Claude para entregar nada — apenas os arquivos `.xlsx`.

## Regras importantes

- Sempre confirme com o usuário qualquer decisão nova de mapeamento de código desconhecido antes de gravar (a menos que ele já tenha instruído a deixar em amarelo).
- Não invente subcategorias: se não estiver no JSON, vai para amarelo.
- Entregue apenas os dois `.xlsx` (ou um único arquivo com duas abas, se o usuário pedir).
- A tarefa só termina quando os dois arquivos existem em `/mnt/user-data/outputs` e a conferência de somas foi reportada.
````
