#!/usr/bin/env python3
"""
Baixa as transcrições faltantes usando cookies do navegador (para vídeos autenticados)
e faz upload para o Notion.
"""

import json, requests, os, re, time, subprocess, glob

TOKEN = 'REDACTED_NOTION_API_TOKEN'
headers_json = {'Authorization': f'Bearer {TOKEN}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
TRANSCRIPTS_DIR = '/home/ubuntu/transcripts_missing2'
BROWSER_DATA_DIR = '/home/ubuntu/.browser_data_dir'
os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

def get_video_id_from_url(url):
    """Extrai o ID do vídeo de qualquer URL do YouTube."""
    if not url:
        return None
    patterns = [
        r'(?:v=|youtu\.be/|embed/|/v/|/live/)([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            vid = match.group(1)
            if len(vid) == 11:
                return vid
    return None

def download_transcript_with_cookies(video_url, video_id, title):
    """Baixa a transcrição usando cookies do navegador."""
    safe_title = "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in title]).strip()[:60]
    output_base = os.path.join(TRANSCRIPTS_DIR, f'{safe_title}_{video_id}')
    
    # Tentar com cookies do navegador
    cmd = [
        'yt-dlp',
        '--write-subs',
        '--write-auto-sub',
        '--sub-lang', 'pt,pt-BR,en',
        '--skip-download',
        '--sub-format', 'vtt',
        '--cookies-from-browser', f'chromium:{BROWSER_DATA_DIR}',
        '-o', output_base,
        '--no-playlist',
        video_url
    ]
    
    env = {**os.environ, 'PATH': os.environ.get('PATH', '') + ':/home/ubuntu/.deno/bin'}
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=90, env=env)
        
        # Verificar se o arquivo foi criado
        vtt_files = glob.glob(f'{output_base}*.vtt')
        if vtt_files:
            # Preferir pt sobre en
            pt_files = [f for f in vtt_files if '.pt.' in f or '.pt-BR.' in f]
            return (pt_files[0] if pt_files else vtt_files[0])
    except subprocess.TimeoutExpired:
        print(f'    Timeout ao baixar legendas')
    except Exception as e:
        print(f'    Erro: {e}')
    
    return None

def vtt_to_text(vtt_file, video_url, title):
    """Converte arquivo VTT para texto limpo."""
    try:
        with open(vtt_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        text_lines = []
        seen = set()
        
        for line in lines:
            line = line.strip()
            if (not line or line.startswith('WEBVTT') or line.startswith('Kind:') or
                line.startswith('Language:') or '-->' in line or
                re.match(r'^\d+$', line) or re.match(r'^\d{2}:\d{2}', line)):
                continue
            
            clean = re.sub(r'<[^>]+>', '', line).strip()
            if clean and clean not in seen:
                seen.add(clean)
                text_lines.append(clean)
        
        transcript_text = f"TÍTULO: {title}\nLINK: {video_url}\n\n" + '\n'.join(text_lines)
        return transcript_text
    except Exception as e:
        print(f'    Erro ao converter VTT: {e}')
        return None

def upload_and_update(page_id, txt_content, filename):
    """Faz upload do conteúdo e atualiza a página do Notion."""
    if len(filename) > 99:
        filename = filename[:95] + '.txt'
    
    tmp_path = os.path.join(TRANSCRIPTS_DIR, filename)
    with open(tmp_path, 'w', encoding='utf-8') as f:
        f.write(txt_content)
    
    # Criar upload
    r1 = requests.post('https://api.notion.com/v1/file_uploads', headers=headers_json,
                       json={'name': filename, 'content_type': 'text/plain'})
    upload_id = r1.json().get('id')
    if not upload_id:
        print(f'    Erro ao criar upload: {r1.text[:100]}')
        return False
    
    # Enviar arquivo
    send_url = f'https://api.notion.com/v1/file_uploads/{upload_id}/send'
    with open(tmp_path, 'rb') as fp:
        content = fp.read()
    r2 = requests.post(send_url,
                       headers={'Authorization': f'Bearer {TOKEN}', 'Notion-Version': '2022-06-28'},
                       files={'file': (filename, content, 'text/plain')})
    if r2.status_code not in (200, 201):
        print(f'    Erro ao enviar arquivo: {r2.text[:100]}')
        return False
    
    # Atualizar página
    update_url = f'https://api.notion.com/v1/pages/{page_id}'
    update_payload = {'properties': {'Transcrições': {'files': [
        {'type': 'file_upload', 'file_upload': {'id': upload_id}, 'name': filename}
    ]}}}
    r3 = requests.patch(update_url, headers=headers_json, json=update_payload)
    
    if r3.status_code == 200:
        return True
    else:
        print(f'    Erro ao atualizar página: {r3.text[:200]}')
        return False

def main():
    with open('/home/ubuntu/missing_transcripts.json', 'r', encoding='utf-8') as f:
        missing = json.load(f)
    
    with_video = [m for m in missing if m['video_url']]
    print(f'Processando {len(with_video)} vídeos com link (usando cookies do navegador)...\n')
    
    results = []
    ok = 0
    no_sub = 0
    error = 0
    
    for i, item in enumerate(with_video):
        page_id = item['page_id']
        title = item['title']
        video_url = item['video_url']
        
        print(f'[{i+1}/{len(with_video)}] {title[:60]}...')
        
        video_id = get_video_id_from_url(video_url)
        if not video_id:
            print(f'  -> ID não extraído da URL: {video_url}')
            results.append({**item, 'status': 'sem_video_id'})
            error += 1
            continue
        
        # Baixar transcrição com cookies
        vtt_file = download_transcript_with_cookies(video_url, video_id, title)
        
        if not vtt_file:
            print(f'  -> Sem legendas disponíveis')
            results.append({**item, 'status': 'sem_legenda', 'video_id': video_id})
            no_sub += 1
            continue
        
        print(f'  -> Legenda baixada: {os.path.basename(vtt_file)}')
        
        # Converter para texto
        txt_content = vtt_to_text(vtt_file, video_url, title)
        if not txt_content:
            print(f'  -> Erro ao converter VTT')
            results.append({**item, 'status': 'erro_conversao', 'video_id': video_id})
            error += 1
            continue
        
        # Montar nome do arquivo
        safe_title = "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in title]).strip()[:60]
        filename = f'{safe_title}_{video_id}.txt'
        
        # Upload e atualização
        success = upload_and_update(page_id, txt_content, filename)
        
        if success:
            print(f'  -> OK!')
            results.append({**item, 'status': 'ok', 'video_id': video_id})
            ok += 1
        else:
            results.append({**item, 'status': 'erro_upload', 'video_id': video_id})
            error += 1
        
        # Limpar arquivo VTT temporário
        try:
            os.remove(vtt_file)
        except:
            pass
        
        time.sleep(0.5)
    
    # Salvar resultados
    with open('/home/ubuntu/missing_fix2_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f'\n{"="*60}')
    print(f'CONCLUÍDO!')
    print(f'  Inseridas com sucesso: {ok}')
    print(f'  Sem legendas disponíveis: {no_sub}')
    print(f'  Erros: {error}')
    print(f'  Total processado: {len(with_video)}')
    
    if no_sub > 0:
        print(f'\nVídeos sem legendas:')
        for r in results:
            if r['status'] == 'sem_legenda':
                print(f'  - {r["title"][:60]}')
                print(f'    {r["video_url"]}')

if __name__ == '__main__':
    main()
