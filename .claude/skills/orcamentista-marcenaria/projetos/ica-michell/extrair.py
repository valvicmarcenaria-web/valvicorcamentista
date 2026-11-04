# -*- coding: utf-8 -*-
"""Lê os PDFs de página soltos e resume cada um: ambiente, conteúdo,
linhas de especificação e cotas. ⚠ ARQUIVO N = PÁGINA N+1 do documento."""
import re, sys, pathlib, pymupdf
PG = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                  '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/ica/pgs')
RUIDO = re.compile(
 r'^(CONSIDERAÇÕES|IARA|CONTATO|ENDEREÇO|MANHUMIRIM|ESCALA|PROPRIETÁRIO|'
 r'Jessica|Indicada|DATA|ETAPA|Executivo|A3|FORMATO|PÁGINA|\d+ PÁGINA|'
 r'- AS MEDIDAS|- EM CASO|- MEDIDAS|- TODAS|-RESPONSAB|CONTEÚDO|'
 r'@IARACEZAR|skp\d|Century|\*Verificar)', re.I)
AMB = ('LIVING|COZINHA|LAVANDERIA|QUARTO|LAVABO|ÁREA GOURMET|BANHO GOURMET|'
       'HOME OFFICE|SUÍTE HÓSPEDES|BANHO HÓSPEDES|SALA DE CINEMA|SUÍTE MASTER|'
       'CLOSET MASTER|BANHO MASTER|SUÍTE MARIANA|CLOSET MARIANA|BANHO MARIANA|'
       'SUÍTE 03|CLOSET 03|BANHO 03')

def resumo(arq):
    doc = pymupdf.open(arq); pg = doc[0]
    txt = pg.get_text()
    amb = (re.search(rf'\b({AMB})\b', txt) or [None, '?'])[1]
    cont = (re.search(r'CONTEÚDO\s*\n?\s*(.{3,60})', txt) or [None, ''])[1].strip()
    dpg = (re.search(r'(\d{1,3})\s*PÁGINA|PÁGINA\s*(\d{1,3})', txt) or [None])
    linhas, nums = [], []
    for l in txt.split('\n'):
        l = l.strip(' .')
        if not l or RUIDO.match(l): continue
        if re.fullmatch(r'[\d\s,.°º]+', l): nums.append(l); continue
        if len(l) < 4: continue
        linhas.append(re.sub(r'\s+', ' ', l))
    vistos, saida = set(), []
    for l in linhas:
        k = l[:60].lower()
        if k not in vistos: vistos.add(k); saida.append(l)
    return amb, cont, saida, nums

if __name__ == '__main__':
    alvo = sys.argv[1:] or None
    for f in sorted(PG.glob('p*.pdf')):
        n = int(f.stem[1:])
        if alvo and str(n) not in alvo: continue
        amb, cont, linhas, nums = resumo(f)
        print(f'\n{"═"*76}\nARQ {n}  ·  doc pág {n+1}  ·  {amb}  ·  {cont}\n{"═"*76}')
        for l in linhas: print(' ·', l[:150])
        if nums: print('   COTAS:', ' | '.join(nums[:60]))
