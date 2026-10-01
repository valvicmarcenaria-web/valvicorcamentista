# -*- coding: utf-8 -*-
"""SUZI E GUILHERME — sala e escritório  [01/10/2026]

Projeto de interiores Luiza Costa. Caderno da sala (5 folhas, rev. 01 de
30/04) e do escritório (4 folhas, rev. 01 de 11/06).
Levantamento em `levantamento-suzi-guilherme.md`.

DEFINIÇÕES DO JONATHAN [01/10]
  1 Cristaleira/bar em MELAMÍNICO AMADEIRADO  ⭐ e explícito na proposta
  2 Mesa do café em LÂMINA NATURAL  → o xadrez é marchetaria de verdade
  3 Mesa de jantar: TAMPO NOVO
  4 Mármore bege  ⛔ NÃO É NOSSO
  5 Os vidros são nossos — R$ 1.500 por porta
  6 O puxador em perfil metálico bronze já está incluso no custo da porta

FLAGS
  1 ★ RT. Não foi dito. O projeto veio do detalhamento de uma arquiteta, que
    é o caso em que a casa trabalha COM RT — lancei assim. Sem RT o preço cai
    ~13%; está no comparativo no fim.
  2 ★ Linha de ferragem não especificada. Adotei Hettich Sensys e pulsador
    Blum no fecho-toque, coerente com residência de alto padrão.
  3 ★ Dobradiça para porta de vidro não está na base. Lancei R$ 45/un.
    As portas vêm do vidraceiro a R$ 1.500 com o puxador; a dobradiça monta
    na nossa caixa, então é nossa. Confirmar se já vem com a porta.
  4 ★ O VIDRO LEITOSO BRANCO DE ESCREVER (escritório) não é porta — o preço
    de R$ 1.500 não o alcança. Lancei a R$ 550/m². Confirmar.
  5 ★ Marchetaria do tampo da mesa do café: 242 quadrados de 5 × 5 em duas
    lâminas alternadas. Lancei R$ 1.800/m² de tampo. É o item mais caro por
    m² do projeto, e é o que a lâmina natural implica.
  6 ⚠ A geometria do bar foi lida de prancha rasterizada. A própria prancha
    manda conferir medidas no local — vale dobrado aqui.
"""
from collections import defaultdict
from math import ceil
import motor_mc as M

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85

# ── chapa ─────────────────────────────────────────────────────────────────
BR6, BR15, BR18 = 190.0, 260.0, 330.0          # branco TX, interno
COR6, COR15, COR18 = 300.0, 500.0, 600.0       # melamínico de cor/amadeirado
CRU15, CRU18 = 230.0, 300.0                    # MDF cru, para receber lâmina
PRECO = {'BR6':BR6, 'BR15':BR15, 'BR18':BR18, 'CR15':CRU15, 'CR18':CRU18}
# AM melamínico amadeirado (bar) · NE Nero Guararapes · CP Cinza Perfeito
for c in ('AM','NE','CP'):
    PRECO[c+'6'], PRECO[c+'15'], PRECO[c+'18'] = COR6, COR15, COR18
NOME = {'BR6':'branco 6','BR15':'branco 15','BR18':'branco 18',
        'CR15':'MDF cru 15','CR18':'MDF cru 18'}
for c, n in (('AM','Amadeirado'),('NE','Nero'),('CP','Cinza Perf.')):
    for e in ('6','15','18'): NOME[c+e] = f'{n} {e}'
FITA_BR, FITA_COR = 2.0, 3.0

# ── ferragem ★ FLAG 2 e 3 ─────────────────────────────────────────────────
DOBR_UN   = 35.0    # Hettich Sensys
DOBR_VID  = 45.0    # ★ dobradiça para porta de vidro — não está na base
TIPON_UN  = 100.0   # Pulsador Blum (fecho-toque)
SUP_PRAT  = 1.50

# ── terceiros e serviços ──────────────────────────────────────────────────
PORTA_VIDRO = 1500.0   # ⭐ [Jonathan] porta em vidro espelhado bronze,
                       #   COM o puxador em perfil metálico bronze incluso
VIDRO_ESCR  = 550.0    # ★ vidro leitoso branco de escrever, por m² — FLAG 4
LAMINA_M2   = 320.0    # lâmina natural aplicada: lâmina, cola, prensa, verniz
MARCHET_M2  = 1800.0   # ★ marchetaria em xadrez de 5 × 5, por m² — FLAG 5
LED_M       = 150.0    # LED COB fita + perfil
ALUM_M      = 85.0     # perfil de alumínio cinza 2 × 1
ENCORP_M2   = 85.0     # miolo sarrafeado de peça encorpada

p, FER, TER = [], defaultdict(lambda: defaultdict(float)), defaultdict(float)
ENCA, LAM = defaultdict(float), defaultdict(float)
def a(mov, mat, desc, c, l, q=1): p.append((mov, mat, desc, c, l, q))
def f(mov, **kw):
    for k, v in kw.items(): FER[mov][k] += v
def t(mov, v): TER[mov] += v
def lam(mov, m2): LAM[mov] += m2          # superfície a receber lâmina natural

# ══════════════════════════════════════════════════════════════════════════
# SALA
# ══════════════════════════════════════════════════════════════════════════

K = 'Sala · cristaleira envidraçada'
# trecho de 199 × 221 × 40, 4 portas de vidro espelhado bronze de 49,5 × 216
# interior: 2 vãos de 95, 5 prateleiras cada
a(K,'AM18','Lateral e montante',          221, 38, 3)
a(K,'AM18','Prateleira interna',           95, 36, 10)
a(K,'AM18','Base e travessa',             199, 38, 2)
a(K,'AM6' ,'Fundo',                       221, 199, 1)
a(K,'AM18','Rodapé',                      199,  5, 1)
f(K, dobrvid=8, sup=10)
t(K, 4*PORTA_VIDRO + 6.0*LED_M)           # ⭐ 4 portas × R$ 1.500 · LED

K = 'Sala · bar com nichos de vinho'
# módulo lateral de 145 × 221 × 60. Nichos de ~8,5 × 8 em ripa de 2 (DET.02)
a(K,'AM18','Lateral',                     221, 58, 2)
a(K,'AM18','Nicho de vinho · ripa vertical', 32, 2, 15)
a(K,'AM18','Nicho de vinho · ripa horizontal', 145, 2, 4)
a(K,'AM18','Nicho de vinho · fundo',      145, 32, 1)
a(K,'AM18','Prateleira com LED',          145, 58, 2)
a(K,'AM18','Porta do armário (fecho-toque)', 87, 55, 1)
a(K,'AM18','Base e travessa do armário',  143, 58, 3)
a(K,'AM6' ,'Fundo',                       221, 143, 1)
a(K,'AM18','Fechamento do vão da cervejeira', 92, 58, 2)
a(K,'AM18','Rodapé',                      145,  5, 1)
f(K, dobr=2, tipon=1, sup=2)
t(K, 3.0*LED_M)
# ⛔ tampo e fundo em mármore bege NÃO são nossos [Jonathan]

K = 'Sala · mesa do café'
# 110 × 55 × 93. MDF cru revestido em LÂMINA NATURAL.
# ⭐ tampo em xadrez de nogueira e carvalho, quadrados de 5 × 5
a(K,'CR18','Tampo (duplado)',             110, 55, 2)
a(K,'CR18','Pé',                           93, 10, 4)
a(K,'CR18','Prateleira',                   84, 45, 1)
a(K,'CR18','Travessa de amarração',        84, 10, 2)
lam(K, 0.93)                              # pés, prateleira, topos e sotopo
t(K, 1.10*0.55*MARCHET_M2)                # ⭐ marchetaria do tampo

K = 'Sala · tampo novo da mesa de jantar'
# 220 × 110, aresta aparente de 5, em lâmina natural.
# ⛔ a estrutura em madeira pintada de preto é existente e fica
a(K,'CR18','Tampo · face',                220, 110, 2)
a(K,'CR18','Aresta · testeira',           660,  5, 1)
ENCA[K] += 2.42
lam(K, 2.42*2 + 0.33)                     # duas faces e a aresta

# ══════════════════════════════════════════════════════════════════════════
# ESCRITÓRIO
# ══════════════════════════════════════════════════════════════════════════

K = 'Escritório · painel e prateleiras'
# painel em MDF Nero de 396 × 217, com perfil de alumínio cinza 2 × 1,
# 1 prateleira em Nero e 2 em Cinza Perfeito de 110 (3 de espessura, 30 prof)
a(K,'NE18','Painel',                      217, 99, 4)
a(K,'BR15','Montante e sarrafo',          217, 10, 8)
a(K,'NE18','Prateleira Nero · face',      131, 30, 2)
a(K,'NE18','Prateleira Nero · testeira',  322,  3, 1)
a(K,'CP18','Prateleira Cinza · face',     110, 30, 4)
a(K,'CP18','Prateleira Cinza · testeira', 280,  3, 2)
ENCA[K] += 1.31*0.30 + 2*1.10*0.30        # prateleiras de 3, encorpadas
f(K, sup=3)
t(K, 8.3*ALUM_M + 1.05*2.20*VIDRO_ESCR)   # ★ perfil + vidro de escrever

K = 'Escritório · mesa de trabalho'
# 220 × 70 × 75, tampo de 5 com acabamento em 1/2 esquadria (DET.02)
# ⭐ prever borracha nos pés para nivelamento
a(K,'CP18','Tampo · face',                220, 70, 2)
a(K,'CP18','Tampo · testeira',            580,  5, 1)
a(K,'CP18','Pé / lateral · face',          70, 70, 4)
a(K,'CP18','Pé / lateral · testeira',     280,  5, 2)
a(K,'BR15','Travessa de estrutura',       210, 20, 2)
a(K,'CP18','Saia frontal',                210, 15, 1)
ENCA[K] += 2.20*0.70 + 2*0.70*0.70

# ══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ══════════════════════════════════════════════════════════════════════════
def _pack(pcs):
    ch, y, x, hf = 1, 0.0, 0.0, 0.0
    for c, l in pcs:
        if l > CH_L: c, l = l, c
        if c > CH_C:
            n = -(-int(c*1000)//int(CH_C*1000)); c = c/n
        if x + c <= CH_C and l <= hf: x += c; continue
        if y + l <= CH_L:
            y += hf if hf else 0
            if y + l > CH_L: ch += 1; y, hf = 0.0, 0.0
            x, hf = c, l
            continue
        ch += 1; y, x, hf = 0.0, c, l
    return ch

def nest(items):
    if not items: return 0
    base = sorted(((max(c, l), min(c, l)) for c, l in items), key=lambda q: (-q[1], -q[0]))
    ch = _pack(base)
    ar = sum(c*l for c, l in items)/10000
    piso = -(-int(ar/(CH_AREA*0.85)*1000)//1000) or 1
    return max(ch, piso)

area_mov, fita_mov = defaultdict(float), defaultdict(float)
por, area = defaultdict(list), defaultdict(float)
amov = defaultdict(lambda: defaultdict(float))
for mov, mat, d, c, l, q in p:
    n = max(1, ceil(max(c, l)/CH_C))
    cc, ll = (c/n, l) if c >= l else (c, l/n)
    area_mov[mov] += c*l*q/10000
    fita_mov[mov] += (c + l)*2/100*q * (0.55 if mat.startswith(('BR','CR')) else 0.75)
    for _ in range(q*n): por[mat].append((cc, ll))
    area[mat]      += c*l*q/10000
    amov[mat][mov] += c*l*q/10000

CH = {m: nest(v) for m, v in por.items()}
ar_tot = sum(area.values())
custo_chapa = sum(CH[m]*PRECO[m] for m in CH)
chapa_mov = defaultdict(float)
for m, n in CH.items():
    tot = sum(amov[m].values())
    for mov, v in amov[m].items(): chapa_mov[mov] += n*PRECO[m]*v/tot

_com = list(dict.fromkeys(x[0] for x in p))
MOVS = _com + [k for k in dict.fromkeys(list(FER)+list(TER)) if k not in _com]
fita_custo = {mov: fita_mov[mov]*1.10*((FITA_BR+FITA_COR)/2) for mov in MOVS}
enc_custo  = {mov: ENCA[mov]*ENCORP_M2 for mov in MOVS}
lam_custo  = {mov: LAM[mov]*LAMINA_M2  for mov in MOVS}

# logística — referencias/logistica.md, praça regional
CARRETO, DIARIA, VISITA = 150.0, 260.0, 275.0
AMB  = {mov: mov.split(' · ')[0] for mov in MOVS}
AMBS = list(dict.fromkeys(AMB[m] for m in MOVS))
carretos = max(2, ceil(ar_tot/18)); dias = max(3, ceil(ar_tot/12))
LOG_TOT = carretos*CARRETO + dias*DIARIA + (2 + len(AMBS)*0.5)*VISITA

PRECO_FER = dict(dobr=DOBR_UN, dobrvid=DOBR_VID, tipon=TIPON_UN, sup=SUP_PRAT)
def custo_fer(mov): return sum(PRECO_FER[k]*q for k, q in FER[mov].items())

CDI = {}
for mov in MOVS:
    proprio = chapa_mov[mov] + fita_custo[mov] + enc_custo[mov] + lam_custo[mov]
    cons    = proprio*0.06
    share   = area_mov[mov]/ar_tot if ar_tot else 0
    CDI[mov] = (proprio + cons + LOG_TOT*share + TER[mov]
                + custo_fer(mov))*(1 + M.EMBALAGEM)
CD = sum(CDI.values())
consum = sum((chapa_mov[m]+fita_custo[m]+enc_custo[m]+lam_custo[m])*0.06 for m in MOVS)

# ── margem ────────────────────────────────────────────────────────────────
RT_ON, COMISSAO = True, False          # ★ FLAG 1
BASE = M.base(parcelas=0, rt=RT_ON, vendedor=COMISSAO)
MC_ITEM = {}
for mov in MOVS:
    b = 0.38
    if 'painel' in mov:                                      b = 0.35
    if any(k in mov for k in ('cristaleira','nichos','café')): b = 0.40
    MC_ITEM[mov] = b

ITENS   = {am: [m for m in MOVS if AMB[m] == am] for am in AMBS}
AR_AMB  = {am: sum(area_mov[m] for m in ITENS[am]) for am in AMBS}
CD_AMB  = {am: sum(CDI[m] for m in ITENS[am]) for am in AMBS}
PV_IT   = {m: round(CDI[m]/(BASE - MC_ITEM[m])/10)*10 for m in MOVS}
PV      = {am: sum(PV_IT[m] for m in ITENS[am]) for am in AMBS}
TOT     = sum(PV.values())
MC_REAL = {m: BASE - CDI[m]/PV_IT[m] for m in MOVS}

# ══════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    br = lambda v: f'{v:,.0f}'.replace(',', '.')
    W = 96
    print('═'*W)
    print('SUZI E GUILHERME — sala e escritório · projeto Luiza Costa')
    print('═'*W)
    print(f'\nBASE {BASE*100:.2f}%   à vista · COM RT · sem comissão   ★ FLAG 1')

    print('\nPLANO DE CORTE')
    for m in sorted(CH, key=lambda k: (k[:2], k)):
        n = CH[m]
        print(f'  {NOME[m]:<16}{area[m]:>7.2f} m² → {n:>3} chapa × R$ {PRECO[m]:>5.0f} '
              f'= R$ {br(n*PRECO[m]):>6}   aprov. {area[m]/(n*CH_AREA)*100:>3.0f}%')
    tch = sum(CH.values())
    print(f'  {"TOTAL":<16}{ar_tot:>7.2f} m² → {tch:>3} chapas'
          f'               R$ {br(custo_chapa):>6}   médio '
          f'{ar_tot/(tch*CH_AREA)*100:.0f}%')

    print('\nABERTURA DO CUSTO DIRETO')
    fer = sum(custo_fer(m) for m in MOVS)
    emb = CD - (custo_chapa + sum(fita_custo.values()) + sum(enc_custo.values())
                + sum(lam_custo.values()) + consum + LOG_TOT + fer + sum(TER.values()))
    for rot, v in (('chapa', custo_chapa), ('fita de borda', sum(fita_custo.values())),
                   ('lâmina natural aplicada', sum(lam_custo.values())),
                   ('miolo encorpado', sum(enc_custo.values())),
                   ('consumíveis', consum), ('logística', LOG_TOT),
                   ('ferragem', fer), ('terceiros e serviços', sum(TER.values())),
                   ('embalagem (2%)', emb)):
        print(f'  {rot:<26}{br(v):>10}')
    print(f'  {"CUSTO DIRETO":<26}{br(CD):>10}')
    print(f'\n  dentro de terceiros: 4 portas de vidro R$ {br(4*PORTA_VIDRO)} · '
          f'vidro de escrever R$ {br(1.05*2.20*VIDRO_ESCR)}')
    print(f'                       marchetaria do tampo R$ {br(1.10*0.55*MARCHET_M2)} · '
          f'LED R$ {br(9.0*LED_M)} · perfil R$ {br(8.3*ALUM_M)}')

    print('\n' + '─'*W)
    print(f'{"ITEM":<44}{"m²":>7}{"CUSTO":>11}{"VENDA":>11}{"MC":>8}')
    print('─'*W)
    for am in AMBS:
        print(f'\n  {am.upper()}')
        for m in ITENS[am]:
            print(f'    {m.split(" · ")[1]:<40}{area_mov[m]:>7.1f}{br(CDI[m]):>11}'
                  f'{br(PV_IT[m]):>11}{MC_REAL[m]*100:>7.1f}%')
        print(f'    {"subtotal":<40}{AR_AMB[am]:>7.1f}{br(CD_AMB[am]):>11}'
              f'{br(PV[am]):>11}{(BASE-CD_AMB[am]/PV[am])*100:>7.1f}%')
    print('─'*W)
    print(f'  {"TOTAL":<42}{ar_tot:>7.1f}{br(CD):>11}{br(TOT):>11}'
          f'{(BASE-CD/TOT)*100:>7.1f}%')
    print('─'*W)

    print('\n★ FLAG 1 — e se não houvesse RT?')
    b2 = M.base(parcelas=0, rt=False, vendedor=False)
    t2 = sum(round(CDI[m]/(b2 - MC_ITEM[m])/10)*10 for m in MOVS)
    print(f'  BASE {b2*100:.2f}%  →  R$ {br(t2)}   ({(t2/TOT-1)*100:+.1f}%, '
          f'R$ {br(TOT-t2)} a menos para o cliente)')
