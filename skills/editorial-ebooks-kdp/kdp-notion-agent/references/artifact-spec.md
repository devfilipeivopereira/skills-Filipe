# Artifact Spec

## 07_landing.html

- HTML simples, responsivo e pronto para publicação.
- Promessa coerente com o tema do livro.
- CTA claro e sem exagero visual.

## 08_bonus.md

- Material complementar coerente com o eixo do ebook.
- Não repetir o livro com outra embalagem.
- Pode ser devocional, guia prático ou roteiro de leitura.

## 09_metadata_kdp.json

Campos mínimos:

- `titulo`
- `subtitulo`
- `autor`
- `descricao_kdp`
- `keywords`
- `categorias`
- `idioma`
- `preco_launch`
- `preco_normal`
- `kindle_unlimited`

Regras obrigatórias para `titulo` e `subtitulo`:

- seguir [title-positioning-playbook.md](./title-positioning-playbook.md)
- `titulo` com até `7 palavras`, sem `:`, sem linguagem de pauta, aula ou texto acadêmico
- `subtitulo` no padrão `Um guia bíblico e prático para...` ou fórmula equivalente aprovada
- `subtitulo` com até `150 caracteres`

## 10_relatorio_cta.json

Campos mínimos:

- `tema`
- `promessa_central`
- `produtos`
- `proxima_acao`

Campos recomendados:

- `produtos[].cta_texto_ebook`
- `produtos[].link`
- `links_inseridos_no_ebook`
- `quantidade_links_inseridos`
- `subagente_origem`

## 11_cta_subagent.json

Artefato opcional produzido por um subagente de curadoria editorial/comercial.

Campos recomendados:

- `tema`
- `promessa_central`
- `audiencia`
- `produtos_sugeridos`
- `ganchos_editoriais_por_capitulo`
- `ctas_recomendados`
- `riscos_de_incoerencia`

Regras:

- este arquivo é apenas de sugestão
- o subagente não deve alterar o ebook diretamente
- o agente principal promove esse conteúdo para `10_relatorio_cta.json`
- apenas produtos coerentes com a promessa do sermão devem ser sugeridos
- se houver risco de o comercial soar forçado, isso deve ser registrado explicitamente

## 12_cta_subagent_brief.md

Briefing gerado pelo agente principal para orientar o subagente.

Deve reunir:

- tema do ebook
- resumo do sermão
- blueprint do ebook
- trecho inicial do manuscrito
- critérios editoriais e limites comerciais

## 13_stage_strategy.md

Estratégia curta de economia de tokens para o caso.

Deve registrar:

- quais etapas merecem maior investimento editorial
- quais etapas devem usar contexto mínimo
- regra de trabalho por capítulo
- limite de reenviar contexto longo apenas quando necessário

## 14_model_routing.json

Plano aplicado de roteamento de modelo por etapa.

Deve registrar:

- etapa
- modelo escolhido
- nível de raciocínio
- arquivos de contexto
- modo de execução
- justificativa

## stage-runs/*.json

Jobs operacionais gerados para executar uma etapa editorial com autonomia.

Cada job deve conter:

- etapa
- profile de execução (`premium|economico`)
- modelo
- nível de raciocínio
- checkpoint (`approve|select|skip`)
- max_feedback_cycles
- previous_attempts
- arquivos de contexto
- instrução operacional
- arquivo de saída esperado
- critérios de sucesso

Regra de reexecução:

- quando houver feedback de checkpoint, reexecutar somente a etapa corrente
- não reiniciar o pipeline completo

## runs/<run_id>/

Artefatos de observabilidade por execução:

- `state.json`:
  - `run_id`, `status`, `stage_current`, `started_at`, `ended_at`, `error`
  - `execution_profile`
  - `ia_agente`
- `events.jsonl`:
  - evento por linha (`stage_started`, `stage_completed`, `checkpoint_waiting`, `checkpoint_feedback`, `run_failed`, `run_completed`)

## Observação

Os artefatos auxiliares devem nascer do mesmo eixo temático do sermão e do ebook. Não criar ofertas ou bônus desconectados da mensagem.

No `push` para o Notion, o pipeline deve preencher a coluna `IA Agente` com o runtime detectado: `codex`, `antigravity`, `claude`, `cursor` ou `windsurf`.

No ebook principal, siga o padrão herdado da skill original:

- inserir de 3 a 5 CTAs discretos ao longo do corpo do livro
- usar hyperlinks para `https://filipeivopereira.com/loja`
- preferir âncoras curtas e naturais, como `workbook extras`, `materiais estudo` e `catálogo bíblico`
- redigir a frase do CTA como continuação pastoral do capítulo, e não como bloco publicitário chamativo
- quando houver `11_cta_subagent.json`, usar suas sugestões como base primária, desde que passem pela validação do agente principal

## Padrão DOCX

O render final para Word e Kindle Create deve manter sempre:

- entrelinha do corpo em `1,25`
- recuo da primeira linha do parágrafo em `8 mm`
- fonte sempre preta em todo o documento
- sumário automático do Word (campo TOC) baseado em Títulos 1, 2 e 3
- `##` como capítulos principais
- capítulos devem seguir o padrão `Capítulo N: Nome do Capítulo`
- `###` como subtítulos com estilo de Word, sem aparecer como markdown bruto
- letra capitular no primeiro parágrafo de cada capítulo principal `##`
- sem letra capitular em prefácio, introdução e `Sobre o Autor`
- subtítulos `###` não reiniciam letra capitular
- subtítulos com espaçamento `2,00` e respiro consistente antes/depois no padrão do Word
- `www.filipeivopereira.com` como hyperlink real no arquivo final
- frases de efeito entre capítulos devem nascer do capítulo anterior, não de tema genérico
- frase de efeito deve sintetizar: dor/luta central, verdade espiritual, virada de perspectiva e chamado final
- frase de efeito deve usar tom de pregação cristã contemporânea, intensa, emocional, direta e memorável
- frase de efeito deve aparecer entre aspas, com negrito e itálico
- frase de efeito deve ter no máximo 200 caracteres
- o ebook não pode conter apêndice, bônus, guias, devocionais ou desafios (ficam no 08_bonus.md)
- as 15k palavras são exclusivas do ebook; não inflar com listas ou materiais paralelos
- `Prefácio`, `Introdução` e `Conclusão` devem ser finalizados por último e com mais de 500 palavras cada
