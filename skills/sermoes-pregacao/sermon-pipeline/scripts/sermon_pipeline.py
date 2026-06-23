#!/usr/bin/env python3
"""
Sermon Pipeline — Pr. Filipe Ivo Pereira
YouTube Playlist → Transcrições → Resumos (Claude) → Notion

USO:
    python sermon_pipeline.py \
        --youtube-key "SUA_CHAVE" \
        --anthropic-key "SUA_CHAVE" \
        --notion-token "SEU_TOKEN" \
        --playlist-id "PL8TZC9PmmYq5_4UGM_guQm-SSXHFNwLfj" \
        --modo "completo"

MODOS:
    completo     - Pipeline inteiro (padrão)
    so-resumos   - Usa título+descrição, sem baixar transcrição
    so-excel     - Só lista vídeos, sem Claude nem Notion
    novos-apenas - Só vídeos sem page_id no notion_map.json
    video-unico  - Um único vídeo: --video-id "XXXXX"
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

# ─── Imports opcionais (instalados pelo pipeline) ───────────────────────────
try:
    from googleapiclient.discovery import build as yt_build
except ImportError:
    yt_build = None

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
except ImportError:
    YouTubeTranscriptApi = None

try:
    import anthropic as anthropic_lib
except ImportError:
    anthropic_lib = None

try:
    import pandas as pd
except ImportError:
    pd = None

# ─── Configurações padrão ────────────────────────────────────────────────────
DEFAULT_PLAYLIST   = "PL8TZC9PmmYq5_4UGM_guQm-SSXHFNwLfj"
NOTION_DATABASE_ID = "31146d0421844d08b273b907c49a2195"
RESUMO_COLUNA      = "Resumo da Pregação"
LANGS_TRANSCRIPT   = ["pt", "pt-BR", "en"]
CLAUDE_MODEL       = "claude-opus-4-5"
DELAY_ENTRE_VIDEOS = 1.5  # segundos

# Diretório deste script (para encontrar notion_map.json)
SCRIPT_DIR = Path(__file__).parent

# ─── CLI ─────────────────────────────────────────────────────────────────────
def parse_args():
    p = argparse.ArgumentParser(description="Sermon Pipeline")
    p.add_argument("--youtube-key",   required=True)
    p.add_argument("--anthropic-key", default="")
    p.add_argument("--notion-token",  default="")
    p.add_argument("--playlist-id",   default=DEFAULT_PLAYLIST)
    p.add_argument("--modo",          default="completo",
                   choices=["completo","so-resumos","so-excel","novos-apenas","video-unico"])
    p.add_argument("--video-id",      default="",
                   help="Apenas para modo video-unico")
    p.add_argument("--saida",         default=".",
                   help="Pasta de saída para arquivos gerados")
    return p.parse_args()

# ─── YouTube ─────────────────────────────────────────────────────────────────
def listar_playlist(api_key, playlist_id):
    if not yt_build:
        raise RuntimeError("google-api-python-client não instalado. Execute: pip install google-api-python-client")

    youtube = yt_build("youtube", "v3", developerKey=api_key)
    videos, next_token = [], None

    print(f"  Carregando playlist {playlist_id}...")
    while True:
        res = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_token
        ).execute()

        for item in res["items"]:
            s = item["snippet"]
            vid = s["resourceId"]["videoId"]
            videos.append({
                "video_id":    vid,
                "title":       s.get("title", ""),
                "description": s.get("description", ""),
                "published_at": s.get("publishedAt", ""),
                "position":    s.get("position", 0),
                "link":        f"https://www.youtube.com/watch?v={vid}",
                "thumbnail":   s.get("thumbnails", {}).get("high", {}).get("url", ""),
            })

        next_token = res.get("nextPageToken")
        print(f"    {len(videos)} vídeos carregados...", end="\r")
        if not next_token:
            break

    print(f"  ✅ {len(videos)} vídeos na playlist")

    # Estatísticas em lote
    _enriquecer_stats(youtube, videos)
    return videos


def _enriquecer_stats(youtube, videos):
    ids = [v["video_id"] for v in videos]
    for i in range(0, len(ids), 50):
        batch = ids[i:i+50]
        res = youtube.videos().list(
            part="statistics,contentDetails",
            id=",".join(batch)
        ).execute()
        mapa = {item["id"]: item for item in res.get("items", [])}
        for v in videos[i:i+50]:
            item = mapa.get(v["video_id"], {})
            stats = item.get("statistics", {})
            v["views"]    = stats.get("viewCount", "0")
            v["likes"]    = stats.get("likeCount", "0")
            v["comments"] = stats.get("commentCount", "0")
            v["duration"] = item.get("contentDetails", {}).get("duration", "")


def buscar_video_unico(api_key, video_id):
    youtube = yt_build("youtube", "v3", developerKey=api_key)
    res = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    ).execute()
    if not res.get("items"):
        raise ValueError(f"Vídeo {video_id} não encontrado")
    item = res["items"][0]
    s = item["snippet"]
    stats = item.get("statistics", {})
    return [{
        "video_id":    video_id,
        "title":       s.get("title", ""),
        "description": s.get("description", ""),
        "published_at": s.get("publishedAt", ""),
        "position":    0,
        "link":        f"https://www.youtube.com/watch?v={video_id}",
        "thumbnail":   s.get("thumbnails", {}).get("high", {}).get("url", ""),
        "views":       stats.get("viewCount", "0"),
        "likes":       stats.get("likeCount", "0"),
        "comments":    stats.get("commentCount", "0"),
        "duration":    item.get("contentDetails", {}).get("duration", ""),
    }]

# ─── Transcrições ────────────────────────────────────────────────────────────
def baixar_transcricao(video_id):
    if not YouTubeTranscriptApi:
        raise RuntimeError("youtube-transcript-api não instalado.")

    for lang in LANGS_TRANSCRIPT:
        try:
            t = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            texto = " ".join(seg["text"] for seg in t)
            texto = re.sub(r"\[.*?\]", "", texto)
            texto = re.sub(r"\s+", " ", texto).strip()
            return texto, lang
        except (TranscriptsDisabled, NoTranscriptFound):
            continue
        except Exception:
            continue

    # Fallback: qualquer idioma disponível
    try:
        for t in YouTubeTranscriptApi.list_transcripts(video_id):
            try:
                segs = t.fetch()
                texto = " ".join(s["text"] for s in segs)
                texto = re.sub(r"\s+", " ", texto).strip()
                return texto, t.language_code
            except Exception:
                continue
    except Exception:
        pass

    return None, None

# ─── Resumo com Claude ───────────────────────────────────────────────────────
def gerar_resumo(anthropic_key, titulo, descricao, transcricao, link):
    if not anthropic_lib:
        raise RuntimeError("anthropic não instalado.")

    cliente = anthropic_lib.Anthropic(api_key=anthropic_key)

    if transcricao:
        fonte = f"TRANSCRIÇÃO (trecho inicial):\n{transcricao[:4000]}"
    else:
        fonte = f"DESCRIÇÃO DO VÍDEO:\n{(descricao or '')[:800]}\n(Transcrição não disponível)"

    prompt = f"""Você é especialista em homilética e pregação cristã evangélica brasileira.

Analise os dados da pregação abaixo e gere um RESUMO DESCRITIVO completo e preciso.

TÍTULO: "{titulo}"
LINK: {link}
{fonte}

Escreva um resumo descritivo de 200 a 280 palavras que inclua OBRIGATORIAMENTE:
1. Tema central e propósito pastoral da mensagem
2. Texto bíblico principal com capítulo e versículo exatos
3. Estrutura dos pontos principais desenvolvidos
4. Aplicação prática concreta para os ouvintes
5. Tom e abordagem homilética usada

Regras de estilo:
- Português brasileiro fluente e pastoral
- Sem travessões
- Sem bullet points ou listas numeradas
- Texto corrido em parágrafo(s)
- Comece diretamente com o conteúdo
- Seja específico com textos bíblicos

Retorne APENAS o texto do resumo, sem título nem formatação extra."""

    resp = cliente.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=700,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.content[0].text.strip()

# ─── Notion ──────────────────────────────────────────────────────────────────
def atualizar_notion(notion_token, page_id, resumo):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = json.dumps({
        "properties": {
            RESUMO_COLUNA: {
                "rich_text": [{"type": "text", "text": {"content": resumo[:2000]}}]
            }
        }
    }).encode()

    req = urllib.request.Request(
        url, data=payload, method="PATCH",
        headers={
            "Authorization":  f"Bearer {notion_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type":   "application/json",
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:200]
        print(f"    ⚠️  Notion HTTP {e.code}: {body}")
        return False
    except Exception as e:
        print(f"    ⚠️  Notion erro: {e}")
        return False


def carregar_notion_map():
    mapa_path = SCRIPT_DIR / ".." / "references" / "notion_map.json"
    if mapa_path.exists():
        with open(mapa_path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def salvar_notion_map(mapa):
    mapa_path = SCRIPT_DIR / ".." / "references" / "notion_map.json"
    mapa_path.parent.mkdir(parents=True, exist_ok=True)
    with open(mapa_path, "w", encoding="utf-8") as f:
        json.dump(mapa, f, ensure_ascii=False, indent=2)

# ─── Saída ───────────────────────────────────────────────────────────────────
def salvar_excel(videos, pasta):
    if not pd:
        print("  ⚠️  pandas não instalado, Excel ignorado.")
        return
    df = pd.DataFrame(videos)
    if "published_at" in df.columns:
        df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce").dt.strftime("%d/%m/%Y %H:%M")
    caminho = Path(pasta) / f"pregacoes_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    df.to_excel(caminho, index=False)
    print(f"  📊 Excel salvo: {caminho}")
    return caminho


def salvar_txt(videos, pasta):
    caminho = Path(pasta) / f"transcricoes_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("Transcrições — Pr. Filipe Ivo Pereira\n\n")
        for v in videos:
            f.write(f"{'='*70}\n{v['title']}\n{v['link']}\n{'─'*70}\n")
            f.write(f"{v.get('transcricao') or '(sem transcrição)'}\n\n")
    print(f"  📄 TXT salvo: {caminho}")
    return caminho


def salvar_json_resumos(videos, pasta):
    caminho = Path(pasta) / f"resumos_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    dados = [{
        "video_id": v["video_id"],
        "titulo":   v["title"],
        "link":     v["link"],
        "com_transcricao": bool(v.get("transcricao")),
        "resumo":   v.get("resumo", ""),
    } for v in videos]
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"  📋 JSON salvo: {caminho}")
    return caminho

# ─── Pipeline principal ──────────────────────────────────────────────────────
def main():
    args = parse_args()
    inicio = datetime.now()
    Path(args.saida).mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"SERMON PIPELINE — Pr. Filipe Ivo Pereira")
    print(f"Modo: {args.modo} | Início: {inicio.strftime('%d/%m/%Y %H:%M')}")
    print(f"{'='*60}\n")

    notion_map = carregar_notion_map()

    # ── Etapa 1: Listar vídeos ──────────────────────────────────────────────
    print("ETAPA 1: Carregando vídeos do YouTube...")
    if args.modo == "video-unico":
        if not args.video_id:
            print("  ❌ Use --video-id para o modo video-unico")
            sys.exit(1)
        videos = buscar_video_unico(args.youtube_key, args.video_id)
    else:
        videos = listar_playlist(args.youtube_key, args.playlist_id)

    if args.modo == "novos-apenas":
        antes = len(videos)
        videos = [v for v in videos if v["video_id"] not in notion_map]
        print(f"  Filtrado: {antes} → {len(videos)} vídeos sem mapeamento Notion")

    if args.modo == "so-excel":
        salvar_excel(videos, args.saida)
        print("\nModo so-excel concluído.")
        return

    # ── Etapa 2+3: Transcrições e Resumos ──────────────────────────────────
    print(f"\nETAPA 2+3: Transcrições + Resumos ({len(videos)} vídeos)...")
    usa_transcricao = args.modo not in ("so-resumos",)

    for i, v in enumerate(videos):
        vid   = v["video_id"]
        titulo = v["title"]
        print(f"\n[{i+1}/{len(videos)}] {titulo[:60]}")

        # Transcrição
        if usa_transcricao:
            transcricao, lang = baixar_transcricao(vid)
            if transcricao:
                print(f"  ✅ Transcrição: {lang} ({len(transcricao):,} chars)")
            else:
                print(f"  ❌ Sem transcrição")
                transcricao = None
        else:
            transcricao, lang = None, None

        v["transcricao"] = transcricao
        v["lang"]        = lang or ""

        # Resumo
        if args.anthropic_key:
            try:
                resumo = gerar_resumo(
                    args.anthropic_key,
                    titulo,
                    v.get("description", ""),
                    transcricao,
                    v["link"]
                )
                v["resumo"] = resumo
                print(f"  ✅ Resumo gerado ({len(resumo):,} chars)")
            except Exception as e:
                print(f"  ⚠️  Erro Claude: {e}")
                v["resumo"] = ""
        else:
            v["resumo"] = ""
            print(f"  ⏭️  anthropic_key não fornecida, resumo pulado")

        # Notion
        page_id = notion_map.get(vid, "")
        if page_id and args.notion_token and v.get("resumo"):
            ok = atualizar_notion(args.notion_token, page_id, v["resumo"])
            v["notion_ok"] = "Sim" if ok else "Não"
            print(f"  {'✅' if ok else '⚠️ '} Notion {'atualizado' if ok else 'falhou'}")
        else:
            v["notion_ok"] = "N/A"

        time.sleep(DELAY_ENTRE_VIDEOS)

    # ── Etapa 4: Salvar ─────────────────────────────────────────────────────
    print(f"\nETAPA 4: Salvando arquivos...")
    salvar_excel(videos, args.saida)
    if usa_transcricao:
        salvar_txt(videos, args.saida)
    salvar_json_resumos(videos, args.saida)

    # Atualiza notion_map com vídeos processados (para uso futuro)
    novos = {v["video_id"]: notion_map.get(v["video_id"], "") for v in videos}
    notion_map.update(novos)
    salvar_notion_map(notion_map)

    # ── Relatório ────────────────────────────────────────────────────────────
    total     = len(videos)
    com_trans = sum(1 for v in videos if v.get("transcricao"))
    com_res   = sum(1 for v in videos if v.get("resumo"))
    notion_ok = sum(1 for v in videos if v.get("notion_ok") == "Sim")
    minutos   = int((datetime.now() - inicio).total_seconds() // 60)

    print(f"\n{'='*60}")
    print(f"RELATÓRIO FINAL")
    print(f"{'='*60}")
    print(f"  Total de vídeos     : {total}")
    print(f"  Com transcrição     : {com_trans}/{total}")
    print(f"  Com resumo          : {com_res}/{total}")
    print(f"  Notion atualizado   : {notion_ok}")
    print(f"  Tempo total         : {minutos} min")
    print(f"  Concluído           : {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
