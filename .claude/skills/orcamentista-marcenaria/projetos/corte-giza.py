# -*- coding: utf-8 -*-
"""GIZA E RENATO — MARCENARIA DOS BANHEIROS. LEVANTAMENTO E PREÇO.

Rua Gentios 40, Ed. Village Green, Cidade Jardim, BH
PROJETO EXECUTIVO · arq. DANI ROSARIA Arquitetura e Design · 25/08 · rev. 00
5 páginas A3, CASO A (com camada de texto). Detalhamento excelente: cota
peça a peça, nomeia ferragem por modelo e traz vista interna com as
prateleiras cotadas.

ESCOPO — dois armários AÉREOS de espelheira, nada mais:
  · Banheiro suíte  — 190 × 135 × 20 · 3 portas espelhadas + 2 portas falsas
  · Banheiro social — 113 × 136 × 20 · 2 portas espelhadas + 1 porta falsa

⛔ FORA: espelho existente, armário inferior existente, forro de gesso,
   pontos elétricos. A prancha marca os dois armários inferiores como
   EXISTENTES — não entram.

⛔ MONTAGEM NÃO ENTRA NO CUSTO (equipe é salário fixo) — mas entra no escopo.
"""
from collections import defaultdict
import math

W = 100
CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85
A_, LIQF_, B_ = 0.162, 0.88, 0.043
BASE = 1 - A_ - LIQF_*B_
RT_PCT = 0.10
def div(mc, rt=False): return BASE - mc - (LIQF_*RT_PCT if rt else 0.0)
def mc_conferida(p, c): return BASE - c/p

def _pack_faixa(pcs):
    ch = 0; y = x = f = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch += 1; continue
        if x + c > CH_C: y += f; x = 0.0; f = 0.0
        if y + l > CH_L: ch += 1; y = x = f = 0.0
        x += c; f = max(f, l)
    return ch + 1
def _pack_bf(pcs):
    ch = []
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: ch.append([CH_L, []]); continue
        best = None
        for s in ch:
            for fx in s[1]:
                if fx[0] >= l and fx[1] >= c and (best is None or fx[1] < best[1]): best = fx
        if best is not None: best[1] -= c; continue
        for s in ch:
            if s[0] + l <= CH_L:
                s[0] += l; s[1].append([l, CH_C - c]); break
        else: ch.append([l, [[l, CH_C - c]]])
    return len(ch)
def nest(items):
    if not items: return 0
    b = [(max(c, l), min(c, l)) for c, l in items]
    ords = [lambda q: -q[1], lambda q: (-q[1], -q[0]), lambda q: -q[0], lambda q: -q[0]*q[1]]
    ch = min(pk(sorted(b, key=k)) for pk in (_pack_faixa, _pack_bf) for k in ords)
    ar = sum(c*l for c, l in items)/10000
    return max(ch, -(-int(ar/(CH_AREA*0.80)*1000)//1000) or 1)

# ── preços · dados/materiais.json (11/06/2026) ────────────────────────────
PRC_BRA = {6: 190.0, 15: 260.0, 18: 330.0, 25: 420.0}   # Branco TX Duratex
NOME_MAT = {'BR': 'MDF Branco TX'}
def prc(m, e): return PRC_BRA[e]

FITA_M, FILET_M, DESPERD = 3.00, 2.50, 1.10
USIN_M   = 25.0        # puxador passante em meia esquadria, por metro
FURO_UN  = 18.0        # ★ furo Ø6 cm fitado na prateleira (usinagem + fita)
# ★ A prancha especifica "suporte de prateleiras NIQUELADO PRATA Delicado".
#   A base tem dois extremos e nenhum meio: "Sup. prateleiras cj4" a R$ 3 (o
#   conjunto — pino plástico comum, R$ 0,75 cada) e "Suporte oculto" a R$ 20.
#   Um pino niquelado à vista não é nenhum dos dois. Adotei R$ 8/un. A R$ 20
#   os 56 suportes custariam R$ 1.120 — mais que toda a chapa do job, o que
#   denuncia que o preço estava errado.
SUP_PRAT = 8.0
ESPELHO_M2 = 600.0     # espelho prata, base
DOBR_HAFELE = 20.0     # Häfele Metalla Chip Soft Close 105°, curva
# ⭐ LED: a prancha ESPECIFICA fita LED COB (Stella All Light EVO 5, 3000 K,
#   IRC>90, 12 V, 15 W) em perfil metálico Usina Design modelo Wood. É
#   exatamente o produto da linha "LED COB (fita + perfil)" da base, a
#   R$ 150/m — e não os R$ 66/m das fitas comuns que os outros motores usam.
#   Aqui o preço da base é o certo.
LED_M = 150.0
DRIVER_UN = 90.0       # ★ driver slim, especificado na prancha

P, FITA, TERC, LED, USIN, DUV = [], [], [], [], [], []
FER = defaultdict(int)
def add(mat, esp, amb, desc, c, l, q=1): P.append((mat, esp, amb, desc, c, l, q))
def fita(a, d, m): FITA.append((a, d, m))
def terc(a, d, v, est=False): TERC.append((a, d, v, est))
def led(a, d, m): LED.append((a, d, m))
def usin(a, m): USIN.append((a, m))
def duv(a, t): DUV.append((a, t))

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — transcrita das cotas da prancha. Tudo em cm.
#
#   Os dois armários têm a MESMA construção; muda a largura e o nº de portas.
#     suíte  190 = 1 + 15 + 53 + 52 + 53 + 15 + 1   (2 portas falsas de 15)
#     social 113 = 2 + 12 + 49 + 49 + 1             (1 porta falsa de 12)
#   Altura: 15 (placa superior de passagem de fiação) + corpo + 2 (perfil LED)
#     suíte  135 = 15 + 118 + 2
#     social 136 = 15 + 119 + 2
#   Profundidade 20 em ambos.
# ═══════════════════════════════════════════════════════════════════════════
PROF = 20.0

def armario(A, larg, alt_corpo, portas, falsas, furos, n_prat, n_div):
    """Espelheira aérea: corpo + placa superior + portas espelhadas + LED."""
    add('BR', 15, A, f'lateral {alt_corpo*10:.0f} × {PROF*10:.0f}', alt_corpo, PROF, 2)
    add('BR', 15, A, f'tampo e base {larg*10:.0f} × {PROF*10:.0f}',
        larg-3, PROF, 2)
    add('BR', 6,  A, f'fundo {larg*10:.0f} × {alt_corpo*10:.0f}', larg-3, alt_corpo-3, 1)
    add('BR', 15, A, 'divisória vertical interna', alt_corpo-3, PROF, n_div)
    add('BR', 15, A, 'prateleira interna', (larg-3)/(n_div+1)-2, PROF-1, n_prat)
    # placa MDF Branco Diamante de 1,5 entre o forro e o armário, para a fiação
    add('BR', 15, A, f'placa superior de passagem de fiação {larg*10:.0f} × 150',
        larg, 15, 1)
    # frentes: portas espelhadas + portas falsas fixas
    for i, p in enumerate(portas, 1):
        add('BR', 18, A, f'porta {i} · {p*10:.0f} × {alt_corpo*10:.0f}', p, alt_corpo, 1)
    for i, f in enumerate(falsas, 1):
        add('BR', 18, A, f'porta falsa {i} · {f*10:.0f} × {alt_corpo*10:.0f}',
            f, alt_corpo, 1)
    FER[A] += 2*len(portas)                      # 2 dobradiças por porta
    # espelho prata colado na face das portas E das portas falsas
    m2 = sum(p*alt_corpo for p in portas + falsas)/10000
    terc(A, f'Espelho prata colado nas frentes ({m2:.2f} m²)', m2*ESPELHO_M2)
    # puxador passante em meia esquadria, no topo de cada folha
    usin(A, sum(portas)/100)
    fita(A, 'frentes e bordas aparentes',
         sum(2*(p+alt_corpo) for p in portas+falsas)/100
         + 2*(larg + alt_corpo)/100 + n_prat*(larg-3)/(n_div+1)/100)
    led(A, 'perfil Usina Design Wood + fita LED COB, superior e inferior',
        2*larg/100)
    terc(A, 'Driver slim da iluminação', DRIVER_UN)
    terc(A, f'{furos} furo(s) Ø6 cm fitado(s) na prateleira', furos*FURO_UN, est=True)
    terc(A, f'Suportes de prateleira niquelados ({n_prat*4} un)',
         n_prat*4*SUP_PRAT)

# ───────────────────────────────────────────────────────────────────────────
# 1 · BANHEIRO SUÍTE — 190 × 135 × 20
#     3 portas espelhadas (53 · 52 · 53) + 2 portas falsas de 15
#     Prateleira com 3 furos Ø6 (secador, babyliss, escovas)
# ───────────────────────────────────────────────────────────────────────────
A = 'Banheiro suíte · armário aéreo'
armario(A, 190, 118, [53, 52, 53], [15, 15], furos=3, n_prat=8, n_div=2)
duv(A, 'a vista interna mostra 8 prateleiras em 3 colunas com alturas '
       'diferentes (19/30/32/16/24/25/20/15). Lancei 8 prateleiras e 2 '
       'divisórias verticais, que é o que o desenho mostra.')

# ───────────────────────────────────────────────────────────────────────────
# 2 · BANHEIRO SOCIAL — 113 × 136 × 20
#     2 portas espelhadas (49 · 49) + 1 porta falsa de 12
#     Prateleira com 1 furo Ø6 (escovas)
# ───────────────────────────────────────────────────────────────────────────
A = 'Banheiro social · armário aéreo'
armario(A, 113, 119, [49, 49], [12], furos=1, n_prat=6, n_div=1)
duv(A, 'a porta falsa de 12 do social esconde a fiação da tomada e o driver '
       'slim. Orcei como frente FIXA espelhada, sem dobradiça — a prancha não '
       'diz se abre. Se for de abrir, entram 2 dobradiças.')

duv('Ambos', 'a prancha manda "PLACA MDF BRANCO DIAMANTE 1,5 cm" no topo e '
    '"MDF BRANCO ÁRTICO" na nota de furo. Branco Diamante e Branco Ártico são '
    'tons diferentes de branco. Orcei tudo em Branco TX Duratex, que é o que a '
    'nota de MARCENARIA especifica. CONFERIR com a arquiteta.')
duv('Ambos', 'as dobradiças são Häfele Metalla Chip Soft Close 105° CURVAS — '
    'curva é para porta sobreposta em lateral. A base tem Häfele a R$ 20; '
    'a Metalla Soft Close costuma custar mais. CONFERIR o preço de compra.')

# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ═══════════════════════════════════════════════════════════════════════════
N_CARRETO, R_CARRETO = 1, 600.0
N_VISITA,  R_VISITA  = 1, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA
ESCADA = [0.35, 0.38, 0.40]

por, area_ch, area_amb = defaultdict(list), defaultdict(float), defaultdict(float)
for m, e, a, d, c, l, q in P:
    for _ in range(q): por[(m, e)].append((c, l))
    ar = c*l*q/10000
    area_ch[(m, e)] += ar; area_amb[a] += ar
CH = {k: nest(v) for k, v in por.items()}
custo_chapa = sum(n*prc(k[0], k[1]) for k, n in CH.items())
area_tot, tot_ch = sum(area_ch.values()), sum(CH.values())
ordem = list(dict.fromkeys(x[2] for x in P))

m_fita_expl = sum(m for _, _, m in FITA)
m_fita = max(m_fita_expl, area_tot*2.6)
custo_fita, custo_filet = m_fita*DESPERD*FITA_M, m_fita*FILET_M
m_usin = sum(m for _, m in USIN); custo_usin = m_usin*USIN_M
m_led = sum(m for _, _, m in LED); custo_led = m_led*LED_M
custo_terc = sum(v for _, _, v, _ in TERC)
TOT_D = sum(FER.values()); custo_ferr = TOT_D*DOBR_HAFELE
consum = (custo_chapa + custo_fita)*0.06
CD = (custo_chapa + custo_fita + custo_filet + custo_usin + custo_led
      + custo_terc + consum + custo_ferr + LOG)

def brl(v, n=2):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')

_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W + '\nPEÇAS QUE NÃO CABEM NA CHAPA')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} · {a} · {d}: {c:.0f} × {l:.0f}')
    print('!'*W + '\n')

print('═'*W)
print('GIZA E RENATO — MARCENARIA DOS BANHEIROS · LEVANTAMENTO E CUSTO')
print('═'*W)
print('Projeto executivo · arq. Dani Rosaria · 25/08 rev.00 · 5 pranchas A3')
print('Dois armários aéreos de espelheira. Armários inferiores são EXISTENTES.')

print('\nESCOPO')
for a in ordem:
    print(f'  {a:<38}{area_amb[a]:>7.2f} m² de chapa   {FER[a]} dobradiças')
print(f'  {"TOTAL":<38}{area_tot:>7.2f} m²')

print('\nPLANO DE CORTE')
for k in sorted(CH, key=lambda k: -k[1]):
    m, e = k; n = CH[k]; pr = prc(m, e)
    print(f'  {NOME_MAT[m]+" "+str(e)+" mm":<26}{area_ch[k]:>7.2f} m²  →  {n:>2} ch. × '
          f'R$ {brl(pr):>8} = R$ {brl(n*pr):>9}   aprov. '
          f'{area_ch[k]/(n*CH_AREA)*100:>3.0f}%')
print(f'  {"TOTAL":<26}{area_tot:>7.2f} m²  →  {tot_ch:>2} chapas{"":>20}'
      f'R$ {brl(custo_chapa):>9}   médio {area_tot/(tot_ch*CH_AREA)*100:.0f}%')

print(f'\nFITA E FILETAGEM   {m_fita:.2f} m · R$ {brl(custo_fita)} + R$ {brl(custo_filet)}')
print(f'USINAGEM           puxador passante em meia esquadria · {m_usin:.2f} m · '
      f'R$ {brl(custo_usin)}')
print(f'ILUMINAÇÃO         LED COB + perfil Usina Design · {m_led:.2f} m × '
      f'R$ {brl(LED_M)}/m · R$ {brl(custo_led)}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço fechado na base)')
for a, d, v, est in TERC:
    print(f' {"★" if est else " "}{a:<38}{d[:38]:<39}R$ {brl(v):>9}')
print(f'  {"TOTAL":<78}R$ {brl(custo_terc):>9}')
print(f'\nFERRAGEM — {TOT_D} dobradiças Häfele Metalla Chip Soft Close 105°')

print('\n' + '═'*W)
print('CUSTO DIRETO')
print('═'*W)
for rot, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita),
               ('Filetagem', custo_filet), ('Usinagem do puxador passante', custo_usin),
               ('Iluminação — LED COB especificado', custo_led),
               ('Terceirizados (espelho, drivers, furos, suportes)', custo_terc),
               ('Consumíveis (6% de chapa + fita)', consum),
               ('Ferragem Häfele', custo_ferr),
               (f'Logística — {N_CARRETO} carreto + {N_VISITA} visita', LOG)):
    print(f'    {rot:<74}R$ {brl(v):>9}')
print(f'    {"CUSTO DIRETO":<74}R$ {brl(CD):>9}')

print('\n' + '═'*W)
print('PREÇO — escada de MC, com e sem RT')
print('═'*W)
print(f'  {"MC":<6}{"sem RT":>13}{"MC real":>10}   {"com RT 10%":>13}{"MC real":>10}')
PRECOS = {}
for mc in ESCADA:
    s = round(CD/div(mc, False)/100)*100
    r = round(CD/div(mc, True)/100)*100
    PRECOS[mc] = (s, r)
    print(f'  {mc*100:>4.0f}%{"R$ "+brl(s,0):>13}{mc_conferida(s, CD)*100:>9.1f}%   '
          f'{"R$ "+brl(r,0):>13}{mc_conferida(r, CD)*100:>9.1f}%')
# [Jonathan 25/08] "MC de 40% com rt em ambos" — fechado.
REC, RT_FECHADO = 0.40, True
INV = PRECOS[REC][1 if RT_FECHADO else 0]
INV_SEM = PRECOS[REC][0]
print(f'\n  ► FECHADO · MC {REC*100:.0f}% COM RT ....... R$ {brl(INV,0)}'
      f'     [Jonathan 25/08]')
print(f'    sem RT, referência interna ......... R$ {brl(INV_SEM,0)}')
rm = INV_SEM/area_tot
print(f'  R$/m² de chapa: {rm:.0f} sem RT   (faixa da casa: 626–834)')
if not 626 <= rm <= 834:
    print(f'  ⚠ FORA DA FAIXA. Aqui é ESPERADO: espelho, LED COB e drivers')
    print(f'    respondem por R$ {custo_terc+custo_led:,.0f} — mais que a chapa.'
          .replace(',', '.'))
    print('    Espelheira de banheiro é móvel de pouca chapa e muito acessório.')

print('\n' + '─'*W)
print(f'INVESTIMENTO POR AMBIENTE  (MC {REC*100:.0f}% COM RT)')
tots, linhas = 0, []
for a in ordem:
    v = round(INV*area_amb[a]/area_tot/100)*100
    linhas.append([a, area_amb[a], v]); tots += v
linhas[max(range(len(linhas)), key=lambda i: linhas[i][1])][2] += INV - tots
for a, ar, v in linhas:
    print(f'  {a:<38}{ar:>8.2f} m²{"R$ "+brl(v,0):>14}')
print(f'  {"TOTAL":<38}{area_tot:>8.2f} m²{"R$ "+brl(INV,0):>14}')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(DUV)} itens')
for i, (a, t) in enumerate(DUV, 1):
    print(f'  {i:>2}. [{a}]\n      {t}')
print('\n  ★ Preços adotados, sem linha na base:')
print(f'     · furo Ø6 fitado na prateleira — R$ {brl(FURO_UN,0)}/un')
print(f'     · suporte niquelado "Delicado" — R$ {brl(SUP_PRAT,0)}/un. A base só')
print('       tem o pino comum (R$ 0,75) e o suporte oculto (R$ 20); o')
print('       niquelado à vista não é nenhum dos dois. São 56 no job.')
print('\n⛔ FORA DO ESCOPO: espelho existente, armários inferiores existentes,')
print('   forro de gesso, pontos elétricos e hidráulicos, alvenaria e pintura.')
print('═'*W)
