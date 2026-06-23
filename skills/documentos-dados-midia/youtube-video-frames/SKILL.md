---
name: youtube-video-frames
description: Baixa videos de links do YouTube e extrai centenas de frames em alta qualidade para pastas locais do projeto. Use quando o usuario pedir para converter video do YouTube em imagens, capturar frames, montar dataset de frames ou salvar screenshots em lote a partir de um link.
---

# YouTube Video Frames

Extrair frames de videos do YouTube com foco em qualidade alta e volume (centenas de imagens) usando um script Python local.
Salvar tudo dentro da pasta de projeto atual por padrao.

## Fluxo Rapido

1. Validar dependencias (`yt-dlp`, `ffmpeg` e opcionalmente `imageio-ffmpeg`).
2. Rodar `scripts/extract_youtube_frames.py` com o link do YouTube.
3. Confirmar a pasta de saida `./<nome-do-video-id>/frames` no projeto atual.

## Comando Padrao

```bash
python C:/Users/filip/.codex/skills/youtube-video-frames/scripts/extract_youtube_frames.py "<YOUTUBE_URL>"
```

Esse comando gera aproximadamente `500` frames em `jpg` de alta qualidade (padrao `--jpeg-quality 2`) dentro da pasta atual do projeto.

## Modos de Extracao

- Quantidade alvo (padrao): usar `--target-frames 500` para distribuir frames ao longo do video.
- FPS fixo: usar `--fps 2` (ou outro valor) para controlar densidade por segundo.
- Limite absoluto: usar `--max-frames 800` para truncar o total final.

## Opcoes Mais Uteis

- `--output-root "C:/caminho/do/projeto"`: definir pasta base de saida.
- `--folder-name "nome-customizado"`: escolher nome da pasta final.
- `--image-format png`: gerar `.png` em vez de `.jpg`.
- `--max-height 1080`: limitar resolucao maxima baixada para reduzir tamanho do video.
- `--start 00:01:00 --end 00:04:00`: extrair apenas um trecho.
- `--overwrite`: sobrescrever pasta de saida existente.
- `--keep-video`: manter o video baixado em `_video/`.

## Exemplo Operacional (centenas de imagens)

```bash
python C:/Users/filip/.codex/skills/youtube-video-frames/scripts/extract_youtube_frames.py "https://www.youtube.com/watch?v=SEU_ID" --target-frames 900 --image-format jpg --jpeg-quality 2 --max-height 1080 --output-root "C:/Users/filip/DEV/Frames_Video_To_Image"
```

## Resultado Esperado

- Pasta criada no projeto:
  - `<output-root>/<titulo-video-id>/frames/frame_000001.jpg`
  - `<output-root>/<titulo-video-id>/frames/frame_000002.jpg`
  - ...
- Log final com total de frames criados e caminho da pasta.

## Falhas Comuns e Correcao

- `yt-dlp is not installed`: instalar com `python -m pip install yt-dlp`.
- `ffmpeg not found`: instalar ffmpeg no PATH ou `python -m pip install imageio-ffmpeg`.
- Pasta de saida ja existe: usar `--overwrite` ou `--folder-name`.
