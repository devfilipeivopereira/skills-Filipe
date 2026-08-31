# EPUB responsivo para Amazon KDP

## Resultado esperado

Gere EPUB 3 responsivo. Não fixe tamanho de página, fonte, cor do corpo, cabeçalho, rodapé ou números de página. O leitor deve poder alterar fonte, espaçamento, tema e orientação.

## Ordem de leitura

1. página de rosto com título, subtítulo opcional e Kang Arin;
2. copyright;
3. sumário HTML;
4. capítulos;
5. sobre a autora, somente se houver biografia.

A imagem de capa deve estar no manifesto com `properties="cover-image"`, mas não em uma página HTML adicional no `spine`; isso evita a capa duplicada no Kindle. A mesma `capa.jpg` é entregue separadamente para o campo de capa do KDP.

## Conteúdo obrigatório do pacote

- `mimetype` como primeiro item, sem compressão e com `application/epub+zip`;
- `META-INF/container.xml`;
- pacote OPF EPUB 3;
- documento de navegação com `properties="nav"` e sumário lógico;
- sumário HTML visível, incluído no `spine`;
- landmarks para sumário e início do corpo;
- capítulos XHTML válidos e CSS comum;
- imagem JPEG de capa;
- NCX auxiliar para compatibilidade, embora EPUB 3 use o nav.

## Metadados

Inclua:

- identificador único UUID ou ISBN fornecido;
- título e subtítulo, quando houver;
- `dc:creator` Kang Arin com função `aut`;
- `dc:language` `pt-BR`;
- editora/selo;
- data de publicação;
- direitos;
- descrição;
- assuntos;
- `dcterms:modified` em UTC.

Título/subtítulo/autora precisam coincidir exatamente com a capa e os campos enviados ao KDP. Não invente ISBN; o eBook pode ser publicado sem ele.

## Formatação

- Um XHTML por capítulo e quebra antes de cada capítulo.
- Parágrafos do corpo com recuo via CSS; nunca use tabulações ou séries de espaços.
- Primeiro parágrafo após título ou quebra de cena sem recuo.
- Quebras de cena semânticas e visualmente discretas.
- Imagens com dimensões proporcionais, sem depender de posição absoluta.
- Fontes incorporadas somente quando licenciadas e realmente necessárias; o padrão desta skill não incorpora fontes.
- Links internos relativos e funcionais.

## Verificação

`validate_epub.py` confere estrutura ZIP, XML, metadados, manifesto, arquivos, capa, navegação, links do sumário e contagem do manuscrito. Isso não substitui a renderização do Kindle.

Quando disponível, abra no Kindle Previewer e verifique:

- capa aparece uma única vez;
- “Ir para” reconhece sumário e início;
- todos os capítulos abrem pelo sumário;
- mudança de fonte/tamanho não corta nem sobrepõe texto;
- recuos e quebras de cena permanecem claros;
- caracteres portugueses são exibidos corretamente;
- não há páginas em branco inesperadas.

## Fontes oficiais

Requisitos consultados em 31 de agosto de 2026:

- [KDP — eBook Cover Image Guidelines](https://kdp.amazon.com/en_US/help/topic/G200645690)
- [KDP — Internal Cover Image](https://kdp.amazon.com/en_US/help/topic/G6GTK3T3NUHKLEFX)
- [KDP — Create a Table of Contents](https://kdp.amazon.com/en_US/help/topic/G201605710)
- [KDP — Kindle Previewer](https://kdp.amazon.com/en_US/help/topic/G202131170)
- [KDP — Metadata Guidelines](https://kdp.amazon.com/en_US/help/topic/G201097560)
- [KDP — Supported eBook Formats](https://kdp.amazon.com/en_US/help/topic/G79CTKR8BX79E96L)

Verifique novamente as páginas oficiais ao publicar, pois políticas e validadores podem mudar.
