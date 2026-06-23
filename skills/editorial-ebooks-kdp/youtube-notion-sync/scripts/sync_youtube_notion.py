#!/usr/bin/env python3
import json, requests, os, re, time, subprocess, glob, argparse

def get_video_id(url):
    if not url: return None
    match = re.search(r'(?:v=|youtu\.be/|embed/|/v/|/live/)([a-zA-Z0-9_-]{11})', url)
    return match.group(1) if match else None

def download_transcript(video_url, video_id, title, output_dir, browser_data_dir):
    safe_title = "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in title]).strip()[:60]
    output_base = os.path.join(output_dir, f'{safe_title}_{video_id}')
    cmd = [
        'yt-dlp', '--write-subs', '--write-auto-sub', '--sub-lang', 'pt,pt-BR,en',
        '--skip-download', '--sub-format', 'vtt',
        '--cookies-from-browser', f'chromium:{browser_data_dir}',
        '-o', output_base, '--no-playlist', video_url
    ]
    env = {**os.environ, 'PATH': os.environ.get('PATH', '') + ':/home/ubuntu/.deno/bin'}
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=90, env=env)
        vtt_files = glob.glob(f'{output_base}*.vtt')
        if vtt_files:
            pt_files = [f for f in vtt_files if '.pt.' in f or '.pt-BR.' in f]
            return pt_files[0] if pt_files else vtt_files[0]
    except: pass
    return None

def vtt_to_text(vtt_file, video_url, title):
    try:
        with open(vtt_file, 'r', encoding='utf-8') as f: content = f.read()
        lines = content.split('\n')
        text_lines = []
        seen = set()
        for line in lines:
            line = line.strip()
            if not line or line.startswith('WEBVTT') or '-->' in line or re.match(r'^\d+$', line): continue
            clean = re.sub(r'<[^>]+>', '', line).strip()
            if clean and clean not in seen:
                seen.add(clean)
                text_lines.append(clean)
        return f"TÍTULO: {title}\nLINK: {video_url}\n\n" + '\n'.join(text_lines)
    except: return None

def upload_to_notion(token, page_id, txt_content, filename, output_dir):
    if len(filename) > 99: filename = filename[:95] + '.txt'
    tmp_path = os.path.join(output_dir, filename)
    with open(tmp_path, 'w', encoding='utf-8') as f: f.write(txt_content)
    headers = {'Authorization': f'Bearer {token}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
    
    r1 = requests.post('https://api.notion.com/v1/file_uploads', headers=headers, json={'name': filename, 'content_type': 'text/plain'})
    upload_id = r1.json().get('id')
    if not upload_id: return False
    
    with open(tmp_path, 'rb') as fp:
        requests.post(f'https://api.notion.com/v1/file_uploads/{upload_id}/send',
                      headers={'Authorization': f'Bearer {token}', 'Notion-Version': '2022-06-28'},
                      files={'file': (filename, fp.read(), 'text/plain')})
    
    update_payload = {'properties': {'Transcrições': {'files': [{'type': 'file_upload', 'file_upload': {'id': upload_id}, 'name': filename}]}}}
    r3 = requests.patch(f'https://api.notion.com/v1/pages/{page_id}', headers=headers, json=update_payload)
    return r3.status_code == 200

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', required=True)
    parser.add_argument('--db_id', required=True)
    parser.add_argument('--mode', choices=['missing', 'playlist'], default='missing')
    parser.add_argument('--playlist_url')
    args = parser.parse_args()

    headers = {'Authorization': f'Bearer {args.token}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
    output_dir = '/home/ubuntu/sync_output'
    os.makedirs(output_dir, exist_ok=True)
    browser_data = '/home/ubuntu/.browser_data_dir'

    if args.mode == 'missing':
        pages = []
        url = f'https://api.notion.com/v1/databases/{args.db_id}/query'
        while True:
            r = requests.post(url, headers=headers, json={'page_size': 100})
            data = r.json()
            pages.extend(data.get('results', []))
            if not data.get('has_more'): break
            url = f'https://api.notion.com/v1/databases/{args.db_id}/query'
            time.sleep(0.3)
        
        for page in pages:
            props = page['properties']
            if not props.get('Transcrições', {}).get('files'):
                title = "".join([t['plain_text'] for t in props.get('TÍTULO DO SERMÃO', {}).get('title', [])])
                video_url = props.get('Vídeo', {}).get('url')
                if not video_url: continue
                
                vid = get_video_id(video_url)
                vtt = download_transcript(video_url, vid, title, output_dir, browser_data)
                if vtt:
                    txt = vtt_to_text(vtt, video_url, title)
                    if upload_to_notion(args.token, page['id'], txt, f"{vid}.txt", output_dir):
                        print(f"Atualizado: {title}")
                    os.remove(vtt)

if __name__ == '__main__': main()
