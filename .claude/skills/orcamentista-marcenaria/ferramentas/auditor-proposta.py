# -*- coding: utf-8 -*-
"""Três passes de auditoria, nesta ordem (referencias/proposta-comercial.md):
   1 conteúdo perdido (HTML → PDF)   2 transbordo   3 metragem e contagem"""
import sys, re, unicodedata, pathlib, json, subprocess, os
from collections import Counter
import pymupdf as fitz

html_p, pdf_p = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
html = html_p.read_text(encoding='utf-8')
doc  = fitz.open(pdf_p)
pdf  = '\n'.join(pg.get_text() for pg in doc)

def norm(t):
    return re.sub(r'[^0-9a-zA-Z%]', '',
                  unicodedata.normalize('NFKD', t)).lower()
npdf = norm(pdf)

# ── 1 · conteúdo perdido ────────────────────────────────────────────────
txt = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.S)
txt = re.sub(r'<[^>]+>', ' ', txt)
txt = (txt.replace('&nbsp;', ' ').replace('&amp;', '&')
          .replace('&mdash;', '—').replace('&lt;', '<').replace('&gt;', '>'))
# ⛔ "está no PDF?" NÃO BASTA. Um trecho que aparece DUAS vezes no HTML e
#   só uma no PDF perdeu uma cópia — e a busca por presença diz que está lá.
#   Foi assim que a folha do pórtico perdeu o rodapé sem ninguém ver: a marca
#   sobreviveu no cabeçalho. Agora compara CONTAGEM.
frags = [f.strip() for f in re.split(r'[.·—\n]', txt) if len(f.strip()) >= 25]
quer  = Counter(norm(f) for f in frags)
vistos, perdidos = set(), []
for f in frags:
    n = norm(f)
    if n in vistos: continue
    vistos.add(n)
    tem = npdf.count(n)
    if tem < quer[n]:
        perdidos.append(f + ('' if quer[n] == 1 else
                             f'   [{quer[n]}× no HTML, {tem}× no PDF]'))
print(f'1 · CONTEÚDO PERDIDO  ......  {"OK" if not perdidos else str(len(perdidos))+" TRECHO(S)"}')
for f in perdidos: print('     ⛔', f[:110])

# ── 2 · transbordo ──────────────────────────────────────────────────────
MM = 72/25.4                 # pt por mm
MARGEM_MIN = 12*MM           # padrão da casa: 12 mm até a borda
print('2 · TRANSBORDO')
ok2 = True
# ⛔ quantos rodapés o HTML MANDA imprimir — a capa não tem, as demais têm.
#   O "i > 1" de antes nunca disparava em documento de UMA página só, que é
#   justamente onde a página 1 tem rodapé. Contar resolve os dois casos.
quer_foot = html.count('class="foot"')
tem_foot  = 0
for i, pg in enumerate(doc, 1):
    bl = [b for b in pg.get_text('blocks') if b[4].strip()]
    # ⛔ o rodapé é a régua. Se ele SUMIU, a página estourou e empurrou o
    #   rodapé para fora — e cair no pg.rect.y1 fazia o auditor dizer "ok".
    # ⛔ a régua é a ocorrência MAIS BAIXA da marca: min() pegava o
    #   cabeçalho em layouts que trazem a marca no topo.
    fb = [b for b in bl if 'valvicmarcenaria' in norm(b[4])
          and b[1] > pg.rect.y1*0.80]
    tem_foot += 1 if fb else 0
    foot_y = max([b[1] for b in fb] or [pg.rect.y1])
    corpo  = [b for b in bl if b[1] < foot_y - 2]
    last   = max([b[3] for b in corpo] or [0])
    folga  = foot_y - last
    flag   = '' if folga > 3 else '  ⛔ ENCOSTA NO RODAPÉ'
    if flag: ok2 = False
    print(f'     pág {i}: último bloco {last:6.1f}  ·  rodapé {foot_y:6.1f}'
          f'  ·  folga {folga:6.1f} pt{flag}')
    if pg.rect.height > 845:
        ok2 = False; print(f'     pág {i}: ⛔ ALTURA {pg.rect.height:.0f} pt — a página esticou')
    # ⛔ O RODAPÉ PODE ESCORREGAR SEM SUMIR. Quando a coluna flex estoura, o
    #   rodapé desce para dentro da margem inferior em vez de desaparecer —
    #   e aí "folga até o rodapé" continua ok, porque a régua desceu junto
    #   com o que ela mede. A margem até a BORDA DA FOLHA é fixa e não mente.
    if fb:
        margem = pg.rect.y1 - max(b[3] for b in fb)
        if margem < MARGEM_MIN:
            ok2 = False
            print(f'     pág {i}: ⛔ RODAPÉ A {margem/MM:.1f} mm DA BORDA '
                  f'(mínimo {MARGEM_MIN/MM:.0f}) — a página comeu a margem')

if tem_foot < quer_foot:
    ok2 = False
    print(f'     ⛔ RODAPÉ PERDIDO — o HTML manda {quer_foot}, o PDF tem '
          f'{tem_foot}. Alguma página estourou e empurrou o rodapé para fora.')

# ── 3 · metragem e contagem ─────────────────────────────────────────────
PROIB = [
    (r'\b\d{1,3}[,.]\d+\s*(m²|m2|m\b|cm|mm)', 'medida com decimal'),
    (r'\b\d{2,4}\s*(m²|m2|cm|mm)\b',          'medida'),
    # ⚠ [\t ] e não \s: o número tem de estar NA MESMA LINHA do substantivo.
    #   Numeração de item ("03\nPrateleiras suspensas") não é contagem de peça,
    #   e com \s o regex atravessava a quebra e acusava item numerado.
    (r'\b\d{1,2}[\t ]*(portas?|gavetas?|prateleiras?|nichos?|módulos?|'
     r'ripas?|dobradiças?|corrediças?|folhas?|peças?|chapas?|pulsadores?|'
     r'painéis|paineis|painel|fechamentos?|suportes?)\b', 'contagem'),
    (r'\b\d+\s*×\s*\d+',                      'cota cruzada'),
]
EXCECAO = re.compile(r'\b(10|15|18|30|40|50)\s*mm\b|\b2,73\s*m\b'
                     r'|\b30\s*×\s*20\b')
#  15/18 mm liberado por Jonathan em 30/09 (separa as duas linhas)
#  2,73 m  liberado por Jonathan em 01/10 (altura do pano ripado do hall)
#  50 mm   liberado por Jonathan em 07/10 — largura da régua do ripado.
#    ⭐ É ESPECIFICAÇÃO DO DESENHO, não quantitativo: o passo do ripado
#      (régua de 50, vão de 15) É o produto. Sem ele o cliente não sabe o
#      que está comprando, do mesmo jeito que não saberia sem a espessura.
#  40 mm   liberado por Jonathan em 07/10 — faixa de MDF da divisória.
#  10 mm   liberado por Jonathan em 07/10 — vidro temperado da divisória.
#  30 mm   liberado por Jonathan em 07/10 — painel da cama do Jairo.
#  30 × 20 liberado por Jonathan em 07/10 — PERFIL de metalon. Não é
#    cota: é o nome comercial do tubo, como 'MDF 15'. A cota cruzada
#    proibida continua sendo a da PEÇA (uma porta de 45 × 70).
#    ⭐ ESPESSURA DE MATERIAL é especificação. ALTURA é metragem e fica
#      de fora: os 300 mm de cada faixa NÃO entram na proposta, que diz
#      apenas 'as duas em alturas iguais'.
achados = []
for pg in doc:
    for rgx, rot in PROIB:
        for m in re.finditer(rgx, pg.get_text(), re.I):
            if EXCECAO.fullmatch(m.group(0).strip()): continue
            achados.append((rot, m.group(0), pg.number+1))
print(f'3 · METRAGEM E CONTAGEM  ...  {"OK" if not achados else str(len(achados))+" OCORRÊNCIA(S)"}')
for rot, g, n in achados: print(f'     ⛔ pág {n}  {rot}: "{g}"')

print()
print('RESULTADO:', 'TUDO OK' if (not perdidos and ok2 and not achados) else '⛔ CORRIGIR')
