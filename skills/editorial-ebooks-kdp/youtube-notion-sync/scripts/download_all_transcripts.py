#!/usr/bin/env python3
"""
Baixa legendas automáticas de todos os vídeos da playlist via yt-dlp
e converte para arquivos .txt limpos com título e link.
"""
import json
import os
import re
import subprocess
import sys
import glob
import time

os.makedirs('/home/ubuntu/transcripts', exist_ok=True)
os.makedirs('/home/ubuntu/vtt_temp', exist_ok=True)

# Carregar lista de vídeos
with open('/home/ubuntu/all_studio_links.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

print(f"Total de vídeos: {len(videos)}")

# Carregar resultados anteriores
results_file = '/home/ubuntu/extraction_results_final.json'
if os.path.exists(results_file):
    with open(results_file, 'r', encoding='utf-8') as f:
        results = json.load(f)
    processed_ids = {r['id'] for r in results}
else:
    results = []
    processed_ids = set()

print(f"Já processados: {len(processed_ids)}")

def vtt_to_text(vtt_content):
    """Converte conteúdo VTT para texto limpo sem duplicatas."""
    lines = vtt_content.split('\n')
    text_lines = []
    seen = set()
    
    for line in lines:
        line = line.strip()
        # Pular cabeçalhos, timestamps e linhas vazias
        if not line:
            continue
        if line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
            continue
        if re.match(r'^\d{2}:\d{2}:\d{2}', line):
            continue
        if re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3} -->', line):
            continue
        # Remover tags HTML/VTT
        clean = re.sub(r'<[^>]+>', '', line)
        clean = clean.strip()
        if clean and clean not in seen:
            seen.add(clean)
            text_lines.append(clean)
    
    return '\n'.join(text_lines)

# Processar cada vídeo
deno_path = os.path.expanduser('~/.deno/bin/deno')
base_cmd = [
    'yt-dlp',
    '--write-auto-sub',
    '--sub-lang', 'pt',
    '--skip-download',
    '--cookies-from-browser', 'chromium:/home/ubuntu/.browser_data_dir',
    '--remote-components', 'ejs:github',
    '--js-runtimes', f'deno:{deno_path}',
    '--quiet',
    '--no-warnings',
]

ok_count = sum(1 for r in results if r['status'] == 'ok')
print(f"Transcrições já salvas: {ok_count}")
print(f"\nIniciando processamento...\n")

for i, video in enumerate(videos):
    if video['id'] in processed_ids:
        continue
    
    print(f"[{i+1}/{len(videos)}] {video['title'][:65]}...")
    
    try:
        # Limpar arquivos temporários anteriores
        for f in glob.glob('/home/ubuntu/vtt_temp/*'):
            os.remove(f)
        
        # Baixar legendas
        output_template = f"/home/ubuntu/vtt_temp/{video['id']}"
        cmd = base_cmd + ['-o', output_template, video['public_url']]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        # Procurar arquivo VTT gerado
        vtt_files = glob.glob(f'/home/ubuntu/vtt_temp/{video["id"]}*.vtt')
        
        if not vtt_files:
            # Tentar com pt-BR
            cmd2 = base_cmd.copy()
            cmd2[cmd2.index('pt')] = 'pt-BR'
            cmd2 = cmd2 + ['-o', output_template, video['public_url']]
            result2 = subprocess.run(cmd2, capture_output=True, text=True, timeout=120)
            vtt_files = glob.glob(f'/home/ubuntu/vtt_temp/{video["id"]}*.vtt')
        
        if not vtt_files:
            print(f"  -> Sem legendas disponíveis")
            results.append({'id': video['id'], 'title': video['title'], 'status': 'sem_legendas', 'file': None})
        else:
            # Ler o arquivo VTT
            with open(vtt_files[0], 'r', encoding='utf-8') as f:
                vtt_content = f.read()
            
            # Converter para texto limpo
            transcript = vtt_to_text(vtt_content)
            
            if len(transcript) < 10:
                print(f"  -> Transcrição vazia após conversão")
                results.append({'id': video['id'], 'title': video['title'], 'status': 'vazio', 'file': None})
            else:
                # Salvar em arquivo .txt
                safe_title = "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in video['title']]).strip()[:100]
                filename = f"/home/ubuntu/transcripts/{safe_title}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Título: {video['title']}\n")
                    f.write(f"Link YouTube: {video['public_url']}\n")
                    f.write(f"Link Studio: {video['studio_url']}\n")
                    f.write("=" * 60 + "\n\n")
                    f.write(transcript)
                
                print(f"  -> OK: {len(transcript)} chars")
                results.append({'id': video['id'], 'title': video['title'], 'status': 'ok', 'file': filename})
    
    except subprocess.TimeoutExpired:
        print(f"  -> TIMEOUT")
        results.append({'id': video['id'], 'title': video['title'], 'status': 'timeout', 'file': None})
    except Exception as e:
        print(f"  -> ERRO: {str(e)[:80]}")
        results.append({'id': video['id'], 'title': video['title'], 'status': f'erro: {str(e)[:80]}', 'file': None})
    
    processed_ids.add(video['id'])
    
    # Salvar progresso a cada 5 vídeos
    if len(results) % 5 == 0:
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    
    time.sleep(0.5)

# Salvar resultados finais
with open(results_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Resumo
ok = sum(1 for r in results if r['status'] == 'ok')
sem = sum(1 for r in results if r['status'] == 'sem_legendas')
vazio = sum(1 for r in results if r['status'] == 'vazio')
erros = sum(1 for r in results if r['status'] not in ('ok', 'sem_legendas', 'vazio'))

print(f"\n{'='*60}")
print(f"CONCLUÍDO!")
print(f"  Transcrições salvas com sucesso: {ok}")
print(f"  Sem legendas disponíveis:        {sem}")
print(f"  Transcrição vazia:               {vazio}")
print(f"  Erros/Timeout:                   {erros}")
print(f"  Total processado:                {len(results)}")
