# Master Conformity Checklist

## Objetivo

Checklist mestre de conformidade do `kdp-notion-agent`.

## 1. Fonte e ingestao

- A fonte editorial automatica deve priorizar `Corrigido`.
- `Transcricoes` pode ser usada como fonte automatica para sermoes anteriores a `2024-10-01`.
- O agente cria `Corrigido` como artefato intermediario obrigatorio.
- O minimo de `15.000` palavras se aplica ao ebook final, nunca ao texto-fonte.
- Ao pedir um novo ebook, a skill deve ignorar paginas que ja tenham workspace local preparado no diretorio alvo.

## 2. Correcao da transcricao

- Corrigir ortografia, pontuacao, acentuacao e sintaxe.
- Unir frases quebradas artificialmente.
- Remover ruido de ASR e duplicacoes mecanicas.
- Preservar o conteudo do sermao sem inventar falas, exemplos ou doutrinas.
- Manter o eixo tematico original do sermao.

## 3. Fidelidade editorial

- O ebook deve permanecer fiel a mensagem central do sermao.
- O agente nao pode divagar para temas paralelos.
- Expansao so pode ocorrer por desdobramento legitimo do conteudo original.
- O livro deve soar como livro, nao como transcricao inchada.
- O texto deve manter PT-BR natural, pastoral, elegante e memoravel.

## 4. Estrutura editorial

- `03_resumo_sermao.md` deve identificar tese, texto base, movimentos e limites.
- `04_blueprint_ebook.md` deve definir promessa, leitor ideal, sumario e funcao dos capitulos.
- `04_blueprint_ebook.md` deve declarar aderencia ao padrao da `generate-persuasive-ebooks` ou justificar qualquer desvio.
- O manuscrito final deve manter progressao tematica real.
- O manuscrito final deve seguir a arquitetura editorial da `generate-persuasive-ebooks`: reconhecimento, tensao, revelacao, transformacao.
- Titulos de capitulos devem seguir `Capitulo N: Nome do Capitulo`.
- Para ebooks cristaos longos, o padrao preferencial e introducao + 8 capitulos + fechamento pastoral, salvo limitacao real do sermao.
- `Prefacio`, `Introducao` e `Conclusao` devem ser escritos por ultimo, apos os capitulos principais.
- `Prefacio`, `Introducao` e `Conclusao` devem ter mais de 500 palavras cada.

## 4.1 Estrutura fixa por capitulo

- Capitulo 1 deve abrir loop mental por identificacao profunda e dor latente.
- Capitulo 2 deve revelar causa raiz, quebrar crencas e produzir momento AHA.
- Capitulo 3 deve reposicionar identidade e conduzir a acao.
- Capitulo 4 deve aprofundar biblica e emocionalmente a nova lente.
- Capitulo 5 deve explicitar `o que a Biblia realmente diz`.
- Capitulo 6 deve oferecer framework pratico numerado.
- Capitulo 7 deve separar aplicacao para membros, lideres e pastores.
- Capitulo 8 deve mostrar o custo de continuar igual e fechar com convite implicito.
- Se o sermao nao sustentar essa espinha, o desvio precisa ser justificado no blueprint e no relatorio editorial.

## 4.2 Blueprint obrigatorio

- Cada capitulo deve registrar objetivo neuroemocional.
- Cada capitulo deve registrar crenca quebrada ou leitura defeituosa.
- Cada capitulo deve registrar dor latente a amplificar.
- Cada capitulo deve registrar nova identidade, lente ou modelo mental.
- Cada capitulo deve registrar ancora biblica.
- Cada capitulo deve registrar trecho do sermao que ancora.
- Cada capitulo deve registrar ganho do leitor ao final.
- Cada capitulo deve registrar transicao para o proximo capitulo.

## 4.3 Conformidade com a skill de referencia

- O `kdp-notion-agent` deve tratar a `generate-persuasive-ebooks` como padrao editorial canonico.
- O agente deve usar `references/persuasive-ebook-style-guide.md` como contrato obrigatorio de tom, voz, estrutura, ritmo e logica argumentativa.
- A forma de escrever deve ficar materialmente proxima dos modelos aprovados pelo usuario, sem copiar trechos literais.
- Capitulos devem abrir com cena, pergunta ou tensao reconhecivel, nunca com abstracao fria.
- O livro deve combinar Biblia, psicologia e aplicacao pratica de forma organica.
- O leitor deve sair reposicionado em identidade, nao apenas informado.
- O livro deve ativar simultaneamente reptiliano, limbico e neocortex sem soar manipulativo.

## 5. Economia de tokens

- O agente deve usar `13_stage_strategy.md`.
- O agente deve preferir contexto curto e reutilizavel.
- O agente deve trabalhar por capitulo quando possivel.
- O agente nao deve reenviar a transcricao inteira sem necessidade.
- O agente deve usar packets por capitulo para escrita e revisao.

## 6. Roteamento de modelo

- O agente deve usar a politica em `references/model-routing-policy.json`.
- O plano aplicado ao caso deve ser salvo em `14_model_routing.json`.
- O plano de execucao do Codex deve ser salvo em `15_codex_orchestration.json`.
- A escolha de `model` e `reasoning_effort` deve ser automatica por etapa.
- A etapa `framing_sections` deve existir e acontecer depois de `chapter_revision` e antes de `final_critique`.
- O profile padrao deve ser `premium`.

## 7. Jobs operacionais

- Cada etapa pode gerar um job em `stage-runs/*.json`.
- O job deve conter etapa, profile, modelo, reasoning effort, checkpoint, max_feedback_cycles, arquivos de contexto, instrucao operacional, arquivo de saida esperado, criterios de sucesso e contrato do subagente.
- Quando houver feedback, deve reexecutar so a etapa corrente.

## 8. Curadoria de CTA

- O subagente nunca escreve direto no ebook.
- O subagente escreve apenas em `11_cta_subagent.json`.
- O agente principal consolida isso em `10_relatorio_cta.json`.
- O ebook deve conter de 3 a 5 CTAs discretos.
- Os links devem apontar para `https://filipeivopereira.com/loja`.
- O CTA nao pode soar como bloco publicitario agressivo.

## 9. Padrao de arquivos finais

- O arquivo principal do ebook deve usar o titulo do ebook no nome.
- O arquivo do bonus deve usar o titulo do ebook no nome.
- A fonte padrao para esse nome deve ser o titulo editorial final do ebook: primeiro `09_metadata_kdp.json.title`, depois o heading `#` de `06_ebook.md`, e so por ultimo o titulo original do caso.
- O padrao esperado e:
- `<Titulo do Ebook>.docx`
- `<Titulo do Ebook> - Bonus.docx`

## 10. Padrao DOCX

- Pagina 1: titulo.
- Pagina 2: copyright fixo.
- Pagina 3: sumario automatico do Word.
- Pagina 4 em diante: prefacio e corpo do livro.
- Frases de efeito entre capitulos principais.
- Ultima pagina: `Sobre o Autor`.

## 11. Upload no Notion

- O `push` deve enviar `Corrigido`, `Ebook_HTML`, `Bonus_PDF`, `Nome_Ebook`, `Data_Criacao`, `Palavras_Ebook`, `Landing_HTML`, `Metadata_KDP`, `Relatorio_CTA`, `Resumo_Sermao`, `Blueprint_Ebook`, `Relatorio_Editorial`, `Score_Qualidade`, `Falhas_QA`, `IA Agente` e `Status`.

## 12. Aprovacao final

Antes de considerar o caso pronto, confirmar:

- validacao local passou
- render local passou
- nomes dos arquivos estao legiveis
- CTAs estao discretos e coerentes
- o sumario esta coeso
- o DOCX segue o padrao fixo
- o Notion recebeu todos os campos e arquivos esperados
- `healthcheck` passou
- testes automatizados passaram
- sync sem drift nos arquivos criticos
