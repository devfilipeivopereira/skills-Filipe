# Setup rapido

Instalar dependencias Python:

```bash
python -m pip install -U yt-dlp imageio-ffmpeg
```

Observacoes:
- `yt-dlp` baixa o video no melhor formato disponivel.
- O script usa `ffmpeg` do PATH quando existir.
- Se `ffmpeg` nao estiver no PATH, o script tenta usar o binario de `imageio-ffmpeg`.
