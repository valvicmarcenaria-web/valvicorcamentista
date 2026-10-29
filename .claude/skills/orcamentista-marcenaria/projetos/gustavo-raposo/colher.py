"""Decodifica os download_file_content salvos em tool-results -> pr/<nome>.pdf

⚠ O MCP do Drive devolve base64 e o harness salva em arquivo quando passa do
limite de tokens. Este script pega o que estiver lá e grava o PDF de verdade,
usando o título do próprio arquivo como nome.
"""
import json, base64, pathlib, re, unicodedata as U
TR  = pathlib.Path('/root/.claude/projects/-home-user-valvicorcamentista/'
                   '7882701a-ab48-5bc5-bc38-040da97b2b38/tool-results')
OUT = pathlib.Path(__file__).resolve().parent/'pr'
OUT.mkdir(parents=True, exist_ok=True)
novos = 0
for f in sorted(TR.glob('mcp-Google_Drive-download_file_content-*.txt')):
    try: d = json.loads(f.read_text())
    except Exception: continue
    if 'content' not in d: continue
    t = U.normalize('NFC', d.get('title', ''))
    m = re.match(r'(\d+)\s*-\s*(.+?)_Rev', t)
    if not m: continue
    nome = re.sub(r'[^\w]+', '-', m.group(2)).strip('-').lower()
    alvo = OUT/f'{int(m.group(1)):02d}-{nome}.pdf'
    if alvo.exists(): f.unlink(missing_ok=True); continue
    alvo.write_bytes(base64.b64decode(d['content'])); novos += 1
    f.unlink(missing_ok=True)      # ⭐ libera espaço: o PDF já está no disco
print(f'novos: {novos} · na pasta: ' +
      ', '.join(sorted(p.name for p in OUT.glob('*.pdf'))))
