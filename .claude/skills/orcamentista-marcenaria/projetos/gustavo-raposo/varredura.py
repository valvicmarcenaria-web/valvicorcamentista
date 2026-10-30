# -*- coding: utf-8 -*-
"""Varre TODAS as pranchas e diz, por ambiente, se há marcenaria e qual.

⭐⭐ POR QUE EXISTE [30/10/2026]: o Jonathan perguntou "e os demais
  ambientes?" e eu não tinha resposta — pior, eu tinha uma lista de
  pendências em que a SALA DE ESTAR simplesmente não aparecia. Não porque
  eu a tivesse descartado, mas porque eu nunca a tinha visto.

  ⛔ Lista de pendência feita de memória esquece em silêncio. Esta varre
    a PASTA, que é a única fonte que não esquece.

   uso:  python3 -I varredura.py
"""
import re, pathlib, pymupdf, collections
PR = pathlib.Path(__file__).resolve().parent/'pr'

# ⭐ o que denuncia marcenaria numa chamada de prancha
NOSSO = re.compile(
    r'MDF|marcenaria|laquead|lacad|arm[áa]rio|gavet|prateleira|'
    r'ripad|muxarabi|painel|nicho|band[eê]j|cabideiro|penteadeira|'
    r'cabeceira|r[ée]gua|bancada em MDF|torre|closet', re.I)
# ⛔ o que é de outro fornecedor, por mais que apareça na elevação
ALHEIO = re.compile(
    r'quartzito|granito|m[áa]rmore|porcelanato|pedra|nanoglass|'
    r'louça|cuba|torneira|metais|espelho|vidro|lareira|cortina|'
    r'papel de parede|revestimento|tecido|tapete|sof[áa]|poltrona|'
    r'luminária|pendente|arandela|spot|led', re.I)

def chamadas(pg):
    """As anotações da prancha, sem as cotas e sem o carimbo."""
    txt = pg.get_text('text')
    out = []
    for ln in txt.split('\n'):
        s = ln.strip()
        if len(s) < 6: continue
        if re.fullmatch(r'[\d,.\s×x/–-]+', s): continue
        if re.search(r'Luiza Pacheco|CAU|luizapacheco|direitos autorais|'
                     r'medidas devem ser|Cotas em cent|d[úu]vidas ou necess|'
                     r'CLIENTE|ENDERE|EXECUTIVO|Revis[ãa]o|Formato|Esc\.', s,
                     re.I): continue
        out.append(s)
    return out

AMB = collections.OrderedDict()
for arq in sorted(PR.glob('*.pdf')):
    n = int(arq.name[:2])
    nome = arq.stem[3:].replace('-', ' ')
    pg = pymupdf.open(arq)[0]
    AMB.setdefault(nome, {'pr': [], 'ls': []})
    AMB[nome]['pr'].append(n)
    AMB[nome]['ls'] += chamadas(pg)

for nome, d in AMB.items():
    ls = list(dict.fromkeys(d['ls']))
    nosso  = [s for s in ls if NOSSO.search(s)]
    pr = ', '.join(str(x) for x in d['pr'])
    print(f"\n{'═'*74}\n{nome.upper()}   ·   pranchas {pr}")
    if not nosso:
        print('   ⛔ NENHUMA chamada de marcenaria nesta prancha')
        for s in ls[:6]: print(f'      · {s[:90]}')
    else:
        for s in nosso: print(f'   ⭐ {s[:110]}')
