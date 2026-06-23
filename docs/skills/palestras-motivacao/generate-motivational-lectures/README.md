# generate-motivational-lectures

- Categoria: **Palestras e Motivacao** (`palestras-motivacao`)
- Nome declarado: `generate-motivational-lectures`
- Pacote instalavel: `packages/palestras-motivacao/generate-motivational-lectures.zip`
- Pasta copiada: `skills/palestras-motivacao/generate-motivational-lectures`
- Fonte original: `C:\Users\filip\.codex\skills\generate-motivational-lectures`
- Hash do `SKILL.md`: `501975a8eeec75ce48e92568de10502033dfb89dbfd632a0dcbb339cb4d49dfc`

## Resumo

Gera palestras motivacionais completas reproduzindo com fidelidade absoluta o estilo, a metodologia, a estrutura e o vocabulário de um dos cinco maiores palestrantes motivacionais do mundo: Tony Robbins, Simon Sinek, Brené Brown, Les Brown ou Mel Robbins. Use quando o usuário pedir uma palestra motivacional, palestra inspiracional, keynote, treinamento motivacional ou discurso de alto impacto emocional, e quiser o resultado moldado pelo estilo de um desses cinco comunicadores.

## Instalacao individual

```powershell
$zip = "packages/palestras-motivacao/generate-motivational-lectures.zip"
$destino = "C:\Users\filip\.codex\skills"
Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
```

## Rastreabilidade

| Campo | Valor |
|---|---|
| Package ID | `generate-motivational-lectures` |
| Skill name | `generate-motivational-lectures` |
| Categoria | `palestras-motivacao` |
| Namespace | `local` |
| Tipo da fonte | Codex local |
| Fonte original | `C:\Users\filip\.codex\skills\generate-motivational-lectures` |
| Pasta no repositorio | `skills/palestras-motivacao/generate-motivational-lectures` |
| Arquivo principal | `skills/palestras-motivacao/generate-motivational-lectures/SKILL.md` |
| Zip | `packages/palestras-motivacao/generate-motivational-lectures.zip` |
| Tamanho do zip | 21,8 KB |
| Duplicatas consolidadas | 5 |

## Metadados do SKILL.md

| Chave | Valor |
|---|---|
| `name` | generate-motivational-lectures |
| `description` | Gera palestras motivacionais completas reproduzindo com fidelidade absoluta o estilo, a metodologia, a estrutura e o vocabulário de um dos cinco maiores palestrantes motivacionais do mundo: Tony Robbins, Simon Sinek, Brené Brown, Les Brown ou Mel Robbins. Use quando o usuário pedir uma palestra motivacional, palestra inspiracional, keynote, treinamento motivacional ou discurso de alto impacto emocional, e quiser o resultado moldado pelo estilo de um desses cinco comunicadores. |

## Estrutura do pacote

| Metrica | Valor |
|---|---:|
| Arquivos | 7 |
| Diretorios | 2 |
| Tamanho copiado | 53,1 KB |

### Diretorios principais

| Diretorio | Arquivos | Tamanho |
|---|---:|---:|
| `references` | 1 | 26,3 KB |
| `scripts` | 5 | 16,5 KB |

## Secoes internas detectadas

- Generate Motivational Lectures — Os 5 Maiores Comunicadores do Mundo
-   Visão Geral
-   Regras de Fidelidade de Método
-   Palestrantes Disponíveis
-   Antes de Começar — 8 Elementos Obrigatórios
-   Workflow
-   Requisito de Originalidade
-   Requisito de Pesquisa
-   Output Contract
-   Entrega do Documento
-   Ambiente Híbrido
-   Checklist de Qualidade
-     Clareza Estratégica
-     Abertura
-     Diagnóstico
-     Framework
-     Virada Emocional
-     Encerramento
-     Estilo
-     Documento
-   Final Output Override (MD Only)
-   Pergunta Inicial Obrigatoria (Escopo da Producao)

## Arquivos do pacote

| Arquivo | Tamanho |
|---|---:|
| `skills/palestras-motivacao/generate-motivational-lectures/references/palestrantes.md` | 26,3 KB |
| `skills/palestras-motivacao/generate-motivational-lectures/scripts/adapters.py` | 772 B |
| `skills/palestras-motivacao/generate-motivational-lectures/scripts/config.json` | 461 B |
| `skills/palestras-motivacao/generate-motivational-lectures/scripts/core.py` | 6,2 KB |
| `skills/palestras-motivacao/generate-motivational-lectures/scripts/create_lecture_docx.py` | 3,4 KB |
| `skills/palestras-motivacao/generate-motivational-lectures/scripts/create_lecture_epub.py` | 5,8 KB |
| `skills/palestras-motivacao/generate-motivational-lectures/SKILL.md` | 10,2 KB |

## Fontes equivalentes consolidadas

- `C:\Users\filip\.codex\skills\generate-motivational-lectures`
- `C:\Users\filip\.agents\skills\generate-motivational-lectures`
- `C:\Users\filip\.claude\skills\generate-motivational-lectures`
- `C:\Users\filip\.cursor\skills\generate-motivational-lectures`
- `C:\Users\filip\.windsurf\skills\generate-motivational-lectures`

## Conteudo integral do SKILL.md

```
markdown
---
name: generate-motivational-lectures
description: >
  Gera palestras motivacionais completas reproduzindo com fidelidade absoluta o estilo, a metodologia,
  a estrutura e o vocabulário de um dos cinco maiores palestrantes motivacionais do mundo:
  Tony Robbins, Simon Sinek, Brené Brown, Les Brown ou Mel Robbins.
  Use quando o usuário pedir uma palestra motivacional, palestra inspiracional, keynote, treinamento
  motivacional ou discurso de alto impacto emocional, e quiser o resultado moldado pelo estilo de
  um desses cinco comunicadores.
---

# Generate Motivational Lectures — Os 5 Maiores Comunicadores do Mundo

## Visão Geral

Produz uma palestra motivacional completa no estilo fiel de um dos cinco maiores palestrantes do mundo.
Cada palestrante possui anatomia, vocabulário assinatura, sequência emocional e elementos que NÃO podem
ser usados — todos documentados em [references/palestrantes.md](references/palestrantes.md).

Leia [references/palestrantes.md](references/palestrantes.md) antes de escrever qualquer palavra da palestra.
Use [scripts/create_lecture_docx.py](scripts/create_lecture_docx.py) para gerar o `.docx` e
[scripts/create_lecture_epub.py](scripts/create_lecture_epub.py) para o `.epub`.
Use [scripts/core.py](scripts/core.py) como camada de lógica portável e
[scripts/adapters.py](scripts/adapters.py) como camada de adaptação de ambiente.
Mantenha os padrões de runtime em [scripts/config.json](scripts/config.json).

---

## Regras de Fidelidade de Método

- O arquivo de referência é a especificação governante de cada palestrante.
- Siga cada elemento não-negociável do palestrante escolhido, mesmo que este SKILL.md o resuma brevemente.
- Se este SKILL.md e o arquivo de referência divergirem, o arquivo de referência vence.
- Não misture estilos entre palestrantes — a palestra deve ser identificável como de UM único comunicador.
- Se o usuário pedir um palestrante específico, mantenha a metodologia intacta, a menos que ele peça explicitamente um desvio.

---

## Palestrantes Disponíveis

| # | Palestrante     | Método Central                              | Energia de Entrega |
|---|-----------------|---------------------------------------------|--------------------|
| 1 | Tony Robbins    | Tríade + Seis Drivers Humanos               | Alta / Física      |
| 2 | Simon Sinek     | Círculo Dourado / Por Quê                   | Calma / Contemplativa |
| 3 | Brené Brown     | Vulnerabilidade + BRAVING                   | Autêntica / Íntima |
| 4 | Les Brown       | A Fome + Os Três Cs                        | Altíssima / Profética |
| 5 | Mel Robbins     | Regra dos 5 Segundos + Let Them            | Direta / Comportamental |

---

## Antes de Começar — 8 Elementos Obrigatórios

Antes de escrever qualquer parágrafo da palestra, declare explicitamente:

1. **O palestrante escolhido** e por que sua metodologia serve ao objetivo desta palestra.
2. **O problema central** que a audiência enfrenta — descrito com precisão cirúrgica, não com generalidade.
3. **A transformação prometida** — o estado ou resultado concreto que o ouvinte deve alcançar ao final.
4. **A ideia-âncora** — a frase central que sintetiza toda a palestra (não um tema vago, mas uma afirmação poderosa).
5. **O perfil da audiência** — quem são, o que já tentaram, onde estão presos.
6. **O gancho de abertura** — a história ou pergunta que prende nos primeiros 90 segundos.
7. **Os elementos assinatura** do palestrante escolhido que serão usados.
8. **O momento de virada** — o ponto da palestra em que o ouvinte experimenta a mudança cognitiva ou emocional decisiva.

Somente após declarar esses oito elementos, escreva a palestra.

---

## Workflow

1. Receba os parâmetros de entrada do usuário (ou pergunte se faltarem):
   - **Tema**: o assunto central da palestra
   - **Audiência**: perfil de quem vai ouvir
   - **Objetivo de Transformação**: estado que a audiência deve alcançar ao final
   - **Contexto de Entrega**: palestra corporativa / evento de liderança / conferência de vendas / treinamento de equipe / outro
   - **Palestrante a Emular**: Tony Robbins / Simon Sinek / Brené Brown / Les Brown / Mel Robbins
   - **Extensão desejada**: 2.000 / 3.500 / 5.000 palavras (padrão: 5.000)
2. Leia `references/palestrantes.md` para internalizar a metodologia do palestrante escolhido.
3. Declare os 8 elementos obrigatórios.
4. Escreva a palestra seguindo rigorosamente a anatomia, vocabulário e sequência emocional do palestrante.
5. Salve o manuscrito em UTF-8 dentro de `outputs/`.
6. Execute `scripts/create_lecture_docx.py` com `--min-words` igual à extensão escolhida.
7. Execute `scripts/create_lecture_epub.py`.
8. Entregue os caminhos finais ao usuário.

---

## Requisito de Originalidade

- Cada palestra deve ser nova para o pedido atual.
- Não reutilize manuscritos anteriores, cached outputs ou drafts antigos.
- Preserve o estilo e a metodologia do palestrante, mas produza wording e movimento originais.

---

## Requisito de Pesquisa

Antes de redigir, pesquise material atual relevante ao tema e à audiência:
- Estatísticas recentes, ilustrações culturais, exemplos contemporâneos.
- Prefira fontes primárias e recentes.
- Material externo apoia — não substitui — a metodologia do palestrante.
- Inclua link de atribuição quando um dado material moldar substancialmente a palestra.

---

## Output Contract

Antes do corpo da palestra, declare explicitamente os 8 elementos obrigatórios como cabeçalho estruturado.

Sinalize claramente cada fase da anatomia do palestrante escolhido:
- **Robbins**: Ruptura de Estado → Diagnóstico → História → Modelo → Linguagem → Visão → Comprometimento
- **Sinek**: Pergunta Fundadora → Contraste de Casos → Círculo Dourado → Neurociência → História → Convite ao Porquê
- **B. Brown**: Confissão da Pesquisadora → Definição Operacional → Dados que Surpreendem → Roosevelt → Ferramenta → Convite à Coragem
- **L. Brown**: Grito de Abertura → História de Origem → Cemitério dos Sonhos → A Fome → Desafio Pessoal
- **Mel Robbins**: Confissão Crua → Diagnóstico Neurológico → Ferramenta ao Vivo → Histórias de Aplicação → Let Them → Comprometimento

---

## Entrega do Documento

- Escreva o manuscrito da palestra em arquivo UTF-8 (`.md`) dentro de `outputs/` nesta pasta da skill.
- Execute `scripts/create_lecture_docx.py`:
  - `--input`: o arquivo `.md` gerado
  - `--output`: `outputs/<Tema>_<Palestrante>.docx`
  - `--min-words`: a extensão escolhida (padrão 5000)
  - `--docs-dir`: `C:\Users\filip\OneDrive\Área de Trabalho\Palestras Geradas\DOCX`
  - `--reference`: o tema sanitizado
- Não declare o documento completo até que o script confirme o word count.
- Execute `scripts/create_lecture_epub.py`:
  - `--input-docx`: o `.docx` gerado em `outputs/`
  - `--reference`: o tema sanitizado
  - `--speaker`: o nome do palestrante
  - `--output-dir`: `C:\Users\filip\OneDrive\Área de Trabalho\Palestras Geradas\EPUB`
  - `--cleanup-dir`: `outputs/` desta skill
- Nomeie os arquivos usando tema + palestrante. Exemplo: `Lideranca_Tony_Robbins.docx` / `Lideranca_Tony_Robbins.epub`.
- Entregue os caminhos finais de `.docx` e `.epub` ao usuário.
- Após a entrega bem-sucedida dos dois arquivos, esvazie `outputs/` preservando a pasta.

---

## Ambiente Híbrido

- Mantenha leitura/escrita de filesystem em `scripts/adapters.py`.
- Mantenha parsing, word-count e renderização `.docx` em `scripts/core.py`.
- Mantenha padrões (min_words, estilos) em `scripts/config.json`.
- Se o ambiente bloquear escrita no caminho de destino final, use `outputs/` como fallback e informe o caminho.

---

## Checklist de Qualidade

Antes de entregar, verifique:

### Clareza Estratégica
- [ ] Os 8 elementos obrigatórios foram declarados?
- [ ] O palestrante escolhido é o mais adequado para o problema específico da audiência?
- [ ] A ideia-âncora é uma frase memorável e completa — não um tema genérico?

### Abertura
- [ ] A abertura rompe o estado passivo da audiência nos primeiros 90 segundos?
- [ ] A história de abertura ou pergunta inicial cria lacuna cognitiva ou identificação emocional imediata?

### Diagnóstico
- [ ] O problema da audiência foi nomeado com precisão cirúrgica?
- [ ] O diagnóstico nomeia o mecanismo invisível, não apenas o sintoma visível?

### Framework
- [ ] O framework específico do palestrante foi apresentado com clareza e memorabilidade?
- [ ] O framework foi demonstrado em contextos concretos e variados?

### Virada Emocional
- [ ] Há um momento de pico emocional identificável?
- [ ] A virada é orgânica ao método do palestrante?

### Encerramento
- [ ] O encerramento é coerente com a identidade do palestrante escolhido?
- [ ] Há comprometimento específico (convite quieto ou ação imediata)?

### Estilo
- [ ] O vocabulário característico do palestrante está presente nos momentos certos?
- [ ] Os elementos que NÃO devem ser feitos foram evitados?
- [ ] A energia da entrega é coerente com o palestrante?

### Documento
- [ ] O `.docx` gerado atende ao word count mínimo?
- [ ] O `.epub` foi gerado e salvo no destino correto?

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
