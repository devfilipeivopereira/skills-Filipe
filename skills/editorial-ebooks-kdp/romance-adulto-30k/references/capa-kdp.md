# Capa de eBook para KDP

## Arquivo entregue

- JPEG em RGB;
- 1600 × 2560 px (proporção 1:1,6);
- vertical, somente frente;
- qualidade alta e preferencialmente até 5 MB;
- sem transparência, lombada, quarta capa ou código de barras.

Esse arquivo serve simultaneamente como capa de marketing enviada separadamente ao KDP e como imagem incorporada no EPUB.

## Briefing visual

Derive do manuscrito final:

- subgênero e tom;
- símbolo ou cenário distintivo;
- paleta de 2–4 cores;
- período/tecnologia corretos;
- composição com um foco principal;
- área de respiro para título na metade superior e autora na inferior;
- contraste que sobreviva em miniatura e em tela monocromática.

Crie a arte de fundo com a ferramenta de geração de imagens, sem texto. Exemplo de estrutura de prompt:

“Capa de eBook, arte de fundo vertical 5:8 para romance [subgênero], [conceito e cena], atmosfera [tom], paleta [cores], composição editorial elegante, foco nítido, amplo espaço negativo limpo na parte superior para título e na parte inferior para nome da autora, sem pessoas reconhecíveis. Sem palavras, letras, tipografia, logotipos, marcas-d'água, preço, selos, código de barras, lombada ou mockup.”

Não imite capa existente nem nomeie artista vivo como estilo. Prefira descrição visual concreta.

## Tipografia

Use `make_kdp_cover.py` para inserir texto exato após a geração. O script aplica proteção de contraste e reduz a fonte para caber, mas a inspeção humana continua obrigatória.

- título: exatamente o valor de `metadata.json`;
- subtítulo: somente se existir nos metadados;
- autora: exatamente `Kang Arin`;
- nada além disso por padrão.

## Inspeção visual

Abra a capa final e verifique em tamanho integral e miniatura:

- título e autora completos, sem erro, corte ou sobreposição;
- hierarquia clara entre título, subtítulo e autora;
- contraste suficiente sobre toda a largura das letras;
- gênero e tom compreensíveis sem depender de texto pequeno;
- anatomia, perspectiva, objetos, reflexos e fundo sem artefatos;
- nenhuma palavra fantasma gerada na arte;
- nenhum conteúdo sexual explícito ou outra imagem inadequada ao anúncio/vitrine;
- correspondência exata com o título e nome da autora nos metadados.

## Fonte oficial

Especificações verificadas em 31 de agosto de 2026: [KDP — Cover Image Guidelines](https://kdp.amazon.com/en_US/help/topic/G200645690). Revise a página oficial novamente se as exigências puderem ter mudado.
