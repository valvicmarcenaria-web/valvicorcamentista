"""Decodifica todo download_file_content salvo em tool-results -> pgs/pNNN.pdf"""
import json, base64, pathlib, re, unicodedata as U, sys
TR = pathlib.Path('/root/.claude/projects/-home-user-valvicorcamentista/'
                  '7882701a-ab48-5bc5-bc38-040da97b2b38/tool-results')
OUT = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                   '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/ica/pgs')
OUT.mkdir(parents=True, exist_ok=True)
novos = 0
for f in sorted(TR.glob('mcp-Google_Drive-download_file_content-*.txt')):
    try: d = json.loads(f.read_text())
    except Exception: continue
    if 'content' not in d: continue
    t = U.normalize('NFC', d.get('title', ''))
    m = re.search(r'p.ginas-(\d+)\.pdf$', t)
    if not m: continue
    alvo = OUT/f'p{int(m.group(1)):03d}.pdf'
    if alvo.exists(): continue
    alvo.write_bytes(base64.b64decode(d['content'])); novos += 1
    f.unlink(missing_ok=True)          # ⭐ libera espaço: o PDF já está salvo
tem = sorted(int(p.stem[1:]) for p in OUT.glob('p*.pdf'))
print(f'novos: {novos} · total local: {len(tem)}')
if tem: print('páginas:', ', '.join(map(str, tem)) if len(tem) < 40 else
              f'{min(tem)}–{max(tem)} ({len(tem)})')
