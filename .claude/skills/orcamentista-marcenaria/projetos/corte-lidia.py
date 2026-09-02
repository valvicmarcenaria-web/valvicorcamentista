# -*- coding: utf-8 -*-
"""LÍDIA DE SOUZA — MARCENARIA DA SALA DE ESTAR E JANTAR. LEVANTAMENTO E PREÇO.

CADERNO DE MARCENARIA · decoradora JÉSSICA SOLLERO · 01.SETEMBRO.2026
8 páginas A4, CASO B (texto em curvas — lido por rasterização, não por camada
de texto). Ambiente único: SALA ESTAR E JANTAR. A prancha carimba
"CONFERIR MEDIDAS NO LOCAL" em todas as folhas.

ESCOPO — quatro conjuntos em duas paredes:
  PAREDE DO JANTAR (579 × 270)
    1 · Painel em MDF Cumaru ......... 579 × 230, com o vão da cristaleira
                                        recortado · perfil de alumínio na base
    2 · Cristaleira em MDF Frapê ..... 192 × 200 × 16, embutida no painel
                                        2 colunas de 93 · portas em vidro
                                        reflecta bronze na coluna direita
  PAREDE DA TV (238,5 × 260)
    3 · Painel em MDF Atenna ......... 238,5 × 250, acima do rodapé
    4 · Rack em MDF Cumaru ........... 214 × 30 × 40, suspenso
                                        báscula ripada vazada + 2 gavetões
                                        ripados + 2 nichos laterais

[Jonathan 02/09] COM RT · MC 35% · prazo 60 dias corridos ·
                 ferragens: corrediça TELESCÓPICA e dobradiça HETTICH.
  A telescópica é o que ele pediu neste job. A regra de 29/08 em
  `ferragens.md` diz que ela não é default de motor — e diz também que,
  quando aparece, é decisão de conversa. Foi o caso. Garantia da corrediça: 2 anos.

⛔ FORA — o caderno mostra, mas não é marcenaria: sofá, mesa, cadeiras,
   poltrona, tapete, pendente, cortina, TV, ar-condicionado, gesso e sanca,
   rodapé de obra, revestimento e pintura das paredes.
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
# Frapê, Cumaru e Atenna são linhas ARAUCO de melamínico — tier "cor" da base.
PRC_COR = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}
PRC_BRA = {6: 190.0, 15: 260.0, 18: 330.0, 25: 420.0}   # Branco TX, interno
NOME_MAT = {'FR': 'MDF Frapê (ARAUCO)', 'CU': 'MDF Cumaru (ARAUCO)',
            'AT': 'MDF Atenna (ARAUCO)', 'BR': 'MDF Branco TX'}
def prc(m, e): return PRC_BRA[e] if m == 'BR' else PRC_COR[e]

FITA_M, FILET_M, DESPERD = 3.00, 2.50, 1.10
USIN_M   = 25.0        # cava de puxador usinada, por metro
ESQ_M    = 15.0        # ★ meia esquadria (chanfro de 45° na borda da chapa).
                       #   Não é cava: é passada de fresa, mais rápida. A base
                       #   não separa as duas; adotei 15 contra os 25 da cava.
RAIO_UN  = 35.0        # ★ borda arredondada R20 no rack — usinagem + fita
                       #   curva. Sem linha na base; adotado por peça.
DOBR     = 35.0        # Hettich Sensys com amortecimento [Jonathan 02/09]
                       #   ★ se for a Novisys (R$ 10 na base), o job cai ~R$ 400
CORR_TEL = 40.0        # corrediça telescópica com amortecimento, o par
PISTAO   = 30.0        # pistão a gás com amortecimento — báscula do rack
# ★ LED: a prancha pede "LED 3000K", sem dizer COB. A base tem COB a R$ 150/m;
#   os componentes soltos dão fita 28 + perfil 38 = R$ 66/m, que é o que os
#   motores recentes usam para LED comum. Adotei 66. Se a decoradora quiser
#   COB (o render mostra brilho contínuo nas prateleiras), sobe ~R$ 800.
LED_M    = 66.0
# ★ Porta de vidro reflecta bronze COMPLETA (perfil bronze + puxador sotille +
#   furos de dobradiça). A base tem a linha por unidade numa folha de
#   ~2,00 × 0,36 m a R$ 475 — R$ 660/m², referência confirmada no job
#   Kenia & Fábio (12/06/2026). As folhas daqui são maiores; vai pelo m².
VIDRO_M2 = 660.0
PUX_SOTILLE = 50.0     # ★ puxador sotille bronze, sem linha na base
PERFIL_ALU_M = 40.0    # ★ perfil de alumínio na base do painel
ADEGA_UN = 35.0        # ★ suporte de garrafa em tubinho preto, por garrafa

P, FITA, TERC, LED, USIN, ESQ, DUV = [], [], [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])       # dobradiças · telescópicas · pistões
def add(mat, esp, amb, desc, c, l, q=1): P.append((mat, esp, amb, desc, c, l, q))
def fer(a, dobr=0, tel=0, pis=0):
    FER[a][0] += dobr; FER[a][1] += tel; FER[a][2] += pis
def fita(a, d, m): FITA.append((a, d, m))
def terc(a, d, v, est=False): TERC.append((a, d, v, est))
def led(a, d, m): LED.append((a, d, m))
def usin(a, m): USIN.append((a, m))
def esq(a, m): ESQ.append((a, m))
def duv(a, t): DUV.append((a, t))

LIM_C, LIM_L = 270.0, 180.0
def _partir(c, l):
    """Peça maior que a chapa vira n peças emendadas — o painel de 5,79 m não
    sai inteiro de uma chapa de 2,75."""
    if c < l: c, l = l, c
    nc = max(1, math.ceil(c/LIM_C)); nl = max(1, math.ceil(l/LIM_L))
    return [(c/nc, l/nl)]*(nc*nl)
def painel(mat, esp, amb, desc, c, l, q=1):
    for cc, ll in _partir(c, l): add(mat, esp, amb, desc, cc, ll, q)
def gaveta(mat, amb, nome, L, Pf, alt, q=1):
    add(mat, 15, amb, f'{nome} · caixa lateral',       Pf-10, alt, 2*q)
    add(mat, 15, amb, f'{nome} · caixa frente/costas', L-6,   alt, 2*q)
    add(mat, 6,  amb, f'{nome} · fundo de gaveta',     L-6,   Pf-10, q)

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — cotas das pranchas 2 a 6. Tudo em cm.
#
#   PAREDE DO JANTAR (pranchas 2, 3 e 4)
#     largura 579 = 73 + 192 (cristaleira) + 314
#     altura  270 = 40 (sanca de gesso, fora) + 200 (cristaleira) + 30 (base)
#     profundidade 22 = 6 (painel) + 16 (cristaleira)
#
#   PAREDE DA TV (pranchas 5 e 6)
#     largura 238,5 · altura 260 · rodapé 10 · rack 214 × 30 × 40, suspenso
# ═══════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────
# 1 · PAINEL DA SALA DE JANTAR — MDF Cumaru, 579 × 230, com o vão recortado
#     A cristaleira é "embutida no painel": o painel não é um retângulo cheio,
#     são três faixas em volta do vão de 192 × 200.
# ───────────────────────────────────────────────────────────────────────────
A = 'Painel do jantar'
L_PAR, H_PAN, ESP_PAN = 579.0, 230.0, 6.0
L_CRIS, H_CRIS, P_CRIS = 192.0, 200.0, 16.0
painel('CU', 6, A, 'faixa à esquerda da cristaleira 730 × 2300',  73, H_PAN)
painel('CU', 6, A, 'faixa à direita da cristaleira 3140 × 2300', 314, H_PAN)
painel('CU', 6, A, 'faixa sob a cristaleira 1920 × 300',      L_CRIS, 30)
# ½ esquadria em todo o perímetro aparente + as quatro bordas do vão
esq(A, 2*(L_PAR + H_PAN)/100 + 2*(L_CRIS + H_CRIS)/100)
fita(A, 'perímetro do painel e bordas do vão da cristaleira',
     2*(L_PAR + H_PAN)/100 + 2*(L_CRIS + H_CRIS)/100)
terc(A, f'Perfil de alumínio na base ({L_PAR/100:.2f} m)',
     L_PAR/100*PERFIL_ALU_M, est=True)
duv(A, 'a prancha 4 cota o painel com 6 mm de espessura (22 = 6 + 16). Um '
       'tamponamento de 5,79 × 2,30 m em 6 mm NÃO fica plano numa parede fora '
       'de prumo: ou vai colado em parede preparada, ou pede sarrafeamento. '
       'Orcei os 6 mm como desenhado; o SARRAFEAMENTO NÃO ESTÁ NO PREÇO. '
       'Se o painel subir para 15 mm, a profundidade total vira 31 e não 22.')
duv(A, 'a faixa de 40 no topo da parede foi lida como SANCA DE GESSO e ficou '
       'fora da marcenaria — o painel vai do piso (230) até a sanca. Se os 40 '
       'forem marcenaria, entram mais 2,3 m² de Cumaru.')

# ───────────────────────────────────────────────────────────────────────────
# 2 · CRISTALEIRA — MDF Frapê, 192 × 200 × 16, embutida no painel
#     Duas colunas de 93 (2 + 93 + 2 + 93 + 2 = 192).
#     ESQUERDA, aberta: prateleira a 36 · nicho de 78 com divisória e 2
#       prateleiras · faixa de 38 · gavetão de 38
#     DIREITA, atrás de 2 portas de vidro de 48,5: 4 prateleiras (36/38/38/38)
#       e a adega de 38 no rodapé
# ───────────────────────────────────────────────────────────────────────────
A = 'Cristaleira'
COL = 93.0
add('FR', 15, A, f'lateral {H_CRIS*10:.0f} × {P_CRIS*10:.0f}', H_CRIS, P_CRIS, 2)
add('FR', 15, A, f'tampo e base {L_CRIS*10:.0f} × {P_CRIS*10:.0f}',
    L_CRIS-3, P_CRIS, 2)
add('FR', 15, A, 'divisória vertical central', H_CRIS, P_CRIS, 1)
painel('FR', 6, A, 'fundo', L_CRIS-3, H_CRIS-3, 1)
add('FR', 15, A, 'prateleira', COL, P_CRIS-1, 8)      # 4 por coluna
add('FR', 15, A, 'divisória interna do nicho', 78, P_CRIS, 1)
add('FR', 15, A, 'prateleira do nicho', COL/2-1, P_CRIS-1, 2)
add('FR', 15, A, 'frente do gavetão 930 × 380', COL, 38, 1)
gaveta('BR', A, 'gavetão', COL, P_CRIS, 34, 1)
fer(A, tel=1)                                        # gavetão em telescópica
terc(A, '2 portas em vidro reflecta bronze, perfil bronze e puxador sotille '
        f'({2*0.485*2.00:.2f} m²)', 2*0.485*2.00*VIDRO_M2)
fer(A, dobr=4)                                       # 2 dobradiças por folha
terc(A, 'Puxador sotille bronze no gavetão', PUX_SOTILLE, est=True)
terc(A, 'Adega em tubinho preto, 8 garrafas', 8*ADEGA_UN, est=True)
led(A, 'LED 3000 K sob as 10 prateleiras e sob o móvel',
    10*COL/100 + L_CRIS/100)
usin(A, COL/100)                                     # cava do gavetão
fita(A, 'frentes, prateleiras e bordas aparentes',
     2*(COL+0.38*100)/100 + 10*COL/100 + 2*(L_CRIS+H_CRIS)/100 + H_CRIS/100)
duv(A, 'a elevação EXTERNA (prancha 2) cota o gavetão em 40 e a INTERNA '
       '(prancha 3) em 38. Adotei 38, que é o que fecha a soma da coluna '
       '(36 + 78 + 38 + 38 + 4 divisórias de 2 = 200).')
duv(A, 'a coluna ESQUERDA foi lida como ABERTA e a DIREITA atrás das duas '
       'folhas de vidro — é o que a elevação externa desenha (o X do vidro '
       'só aparece nos 48,5 + 48,5 da direita). O render mostra vidro na '
       'frente inteira. CONFERIR: se as duas colunas levarem vidro, entram '
       'mais 2 folhas, ~R$ 1.280 de custo.')
duv(A, 'a profundidade útil de 16 é rasa para taça e garrafa em pé. É o que a '
       'prancha 4 cota (22 = 6 + 16). CONFERIR com a decoradora.')

# ───────────────────────────────────────────────────────────────────────────
# 3 · PAINEL DA TV — MDF Atenna, 238,5 × 250, acima do rodapé
# ───────────────────────────────────────────────────────────────────────────
A = 'Painel da TV'
L_TV, H_TV = 238.5, 250.0
painel('AT', 6, A, f'painel {L_TV*10:.0f} × {H_TV*10:.0f}', L_TV, H_TV)
esq(A, 2*(L_TV + H_TV)/100)
fita(A, 'perímetro do painel', 2*(L_TV + H_TV)/100)
duv(A, 'a cadeia de cotas da prancha 6 não fecha: 200 (painel) + 30 (rack) + '
       '30 (vão sob o rack) + 10 (rodapé) = 270, mas a cota geral da parede é '
       '260. Adotei painel de 250 acima do rodapé de 10. CONFERIR no local — '
       'a própria prancha carimba "conferir medidas".')
duv(A, 'o painel da TV tem recorte e passa-cabo para a TV e para a tomada. '
       'Prevemos o recorte e o reforço; a TV e os pontos são da obra.')

# ───────────────────────────────────────────────────────────────────────────
# 4 · RACK DA TV — MDF Cumaru, 214 × 30 × 40, suspenso
#     20 (nicho) + 58 (báscula) + 58 (gavetão) + 58 (gavetão) + 20 (nicho)
#     Frentes ripadas: ripas de 3 × 2 cm com espaçamento de 3 cm.
#     A báscula é VAZADA — só as ripas, sem frente atrás delas.
# ───────────────────────────────────────────────────────────────────────────
A = 'Rack da TV'
L_RACK, H_RACK, P_RACK = 214.0, 30.0, 40.0
add('CU', 15, A, f'lateral {H_RACK*10:.0f} × {P_RACK*10:.0f}', H_RACK, P_RACK, 2)
add('CU', 15, A, f'tampo e base {L_RACK*10:.0f} × {P_RACK*10:.0f}',
    L_RACK-3, P_RACK, 2)
add('CU', 15, A, 'divisória vertical', H_RACK, P_RACK, 4)
add('BR', 6,  A, 'fundo', L_RACK-3, H_RACK-3, 1)
add('CU', 15, A, 'nicho lateral · prateleira e fundo', 20, P_RACK, 2)
# frentes: 2 gavetões com base em chapa + ripado colado; a báscula é vazada
add('CU', 15, A, 'frente do gavetão 580 × 300', 58, H_RACK, 2)
gaveta('BR', A, 'gavetão', 58, P_RACK, 26, 2)
# ripado · ripa de 3 cm de largura em chapa de 18, espaçamento de 3 cm.
# 174 cm de frente ripada (báscula + 2 gavetões) a passo de 6 cm = 29 ripas.
N_RIPAS = 29
add('CU', 15, A, 'ripa 30 × 300 do ripado das frentes', 3, H_RACK, N_RIPAS)
add('CU', 15, A, 'moldura da báscula vazada 580 × 300', 58, H_RACK, 1)
fer(A, dobr=2, tel=2, pis=2)     # báscula com pistão a gás · 2 gavetões
terc(A, f'Usinagem das bordas arredondadas R20 ({4} cantos)', 4*RAIO_UN, est=True)
esq(A, 2*(L_RACK + H_RACK)/100 + 2*(0.20+P_RACK/100))    # ½ esquadria e nichos
fita(A, 'frentes, ripado, nichos e bordas aparentes',
     N_RIPAS*2*(0.03 + H_RACK/100) + 2*2*(0.58 + H_RACK/100)
     + 2*(L_RACK + H_RACK)/100 + 4*(0.20 + P_RACK/100))
duv(A, 'as ripas são cotadas em 3 × 2 cm e NENHUMA chapa dá 2 cm exatos. '
       'Orcei em 15 mm: a de 18 sozinha puxava uma chapa inteira a 5% de '
       'aproveitamento (R$ 600 para 0,26 m²), enquanto a de 15 entra na chapa '
       'de Cumaru que já está aberta. Ripa de 2 cm exata pede chapa de 25 e '
       'volta a puxar chapa só para ela.')
duv(A, 'a báscula VAZADA foi orçada com moldura e ripas: sem uma moldura a '
       'ripa não tem onde se prender e a frente empena. Se a decoradora '
       'quiser a ripa presa direto na estrutura, é serralheria, não '
       'marcenaria.')
duv(A, 'o rack tem 30 de altura e 40 de profundidade para báscula com pistão '
       'a gás e dois gavetões. Cabe, mas é justo: gavetão de 58 × 26 útil. '
       'CONFERIR se a decoradora espera guardar controle e cabo ou mais que '
       'isso.')

# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ═══════════════════════════════════════════════════════════════════════════
N_CARRETO, R_CARRETO = 1, 600.0
N_VISITA,  R_VISITA  = 1, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA
ESCADA = [0.32, 0.35, 0.38]

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
m_esq  = sum(m for _, m in ESQ);  custo_esq  = m_esq*ESQ_M
m_led = sum(m for _, _, m in LED); custo_led = m_led*LED_M
custo_terc = sum(v for _, _, v, _ in TERC)
TD = sum(f[0] for f in FER.values())
TT = sum(f[1] for f in FER.values())
TP = sum(f[2] for f in FER.values())
custo_ferr = TD*DOBR + TT*CORR_TEL + TP*PISTAO
consum = (custo_chapa + custo_fita)*0.06
CD = (custo_chapa + custo_fita + custo_filet + custo_usin + custo_esq
      + custo_led + custo_terc + consum + custo_ferr + LOG)

# ── CUSTO DIRETO POR ITEM · rateio por CUSTO, nunca por área [29/08] ──────
cd_amb = defaultdict(float)
_ar_gr = defaultdict(float)
for m, e, a, d, c, l, q in P: _ar_gr[(m, e, a)] += c*l*q/10000
for (m, e, a), ar in _ar_gr.items():
    cd_amb[a] += CH[(m, e)]*prc(m, e) * ar/area_ch[(m, e)]
_f_amb = defaultdict(float)
if m_fita > m_fita_expl:
    for a in ordem: _f_amb[a] = m_fita*area_amb[a]/area_tot
else:
    for a, d, mm in FITA: _f_amb[a] += mm
for a, mm in _f_amb.items(): cd_amb[a] += mm*(DESPERD*FITA_M + FILET_M)
for a, mm in USIN:       cd_amb[a] += mm*USIN_M
for a, mm in ESQ:        cd_amb[a] += mm*ESQ_M
for a, d, mm in LED:     cd_amb[a] += mm*LED_M
for a, d, v, _e in TERC: cd_amb[a] += v
for a, (dd, tt, pp) in FER.items():
    cd_amb[a] += dd*DOBR + tt*CORR_TEL + pp*PISTAO
_bruto = sum(cd_amb.values())
for a in list(cd_amb): cd_amb[a] += (consum + LOG)*cd_amb[a]/_bruto
assert abs(sum(cd_amb.values()) - CD) < 0.01, (sum(cd_amb.values()), CD)

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
print('LÍDIA DE SOUZA — SALA DE ESTAR E JANTAR · LEVANTAMENTO E CUSTO')
print('═'*W)
print('Caderno de marcenaria · decoradora Jéssica Sollero · 01.SET.2026 · 8 pág. A4')
print('Quatro conjuntos em duas paredes. Texto em curvas: lido por rasterização.')

print('\nESCOPO')
for a in ordem:
    d, t, p = FER[a]
    ex = [f'{d} dobr.' if d else '', f'{t} telescópica' if t else '',
          f'{p} pistão' if p else '']
    print(f'  {a:<28}{area_amb[a]:>7.2f} m²   {" · ".join(x for x in ex if x)}')
print(f'  {"TOTAL":<28}{area_tot:>7.2f} m²')

print('\nPLANO DE CORTE')
for k, n in sorted(CH.items(), key=lambda x: (-x[1], x[0])):
    print(f'  {NOME_MAT[k[0]]+" "+str(k[1])+" mm":<30}{area_ch[k]:>6.2f} m²  →  '
          f'{n:>2} ch. × R$ {prc(*k):>7.2f} = R$ {brl(n*prc(*k)):>9}   aprov. '
          f'{area_ch[k]/(n*CH_AREA)*100:>3.0f}%')
print(f'  {"TOTAL":<30}{area_tot:>6.2f} m²  →  {tot_ch:>2} chapas{"":>19}'
      f'R$ {brl(custo_chapa):>9}   médio {area_tot/(tot_ch*CH_AREA)*100:.0f}%')

print(f'\nFITA E FILETAGEM   {m_fita:.2f} m · R$ {brl(custo_fita)} + R$ {brl(custo_filet)}')
print(f'USINAGEM           cava de puxador · {m_usin:.2f} m · R$ {brl(custo_usin)}')
print(f'MEIA ESQUADRIA     {m_esq:.2f} m × R$ {brl(ESQ_M)}/m · R$ {brl(custo_esq)}')
print(f'ILUMINAÇÃO         LED 3000 K · {m_led:.2f} m × R$ {brl(LED_M)}/m · R$ {brl(custo_led)}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço fechado na base)')
for a, d, v, est in TERC:
    print(f' {"★" if est else " "}{a:<28} {d[:46]:<46} R$ {brl(v):>9}')
print(f'  {"TOTAL":<76}R$ {brl(custo_terc):>9}')
print(f'\nFERRAGEM — {TD} dobradiças Hettich Sensys · {TT} corrediças '
      f'telescópicas · {TP} pistões a gás')

print('\n' + '═'*W)
print('CUSTO DIRETO')
print('═'*W)
for rot, v in (('Chapas', custo_chapa), ('Fita (material)', custo_fita),
               ('Filetagem', custo_filet), ('Usinagem da cava', custo_usin),
               ('Meia esquadria', custo_esq),
               ('Iluminação', custo_led),
               ('Terceirizados (vidro, adega, perfil, raios, puxador)', custo_terc),
               ('Consumíveis (6% de chapa + fita)', consum),
               ('Ferragem', custo_ferr),
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
# ── MC POR ITEM, NÃO DO JOB [Jonathan 02/09] ─────────────────────────────
#   "o rack e o painel da sala pode considerar uma MC de 40% e unifique o item
#    para que ambos sejam um único valor / diminua a MC da cristaleira para 30%
#    e o painel suba para 40%"
#
#   O preço deixa de sair de uma MC única do job: cada item é precificado pela
#   SUA margem sobre o SEU custo direto, e o total é a soma. O rack e o painel
#   da TV são a mesma parede e saem como UM item na proposta.
RT_FECHADO = True
UNIR = {'Rack da TV': 'Painel e rack da TV',
        'Painel da TV': 'Painel e rack da TV'}
MC_ITEM = {'Cristaleira': 0.30,
           'Painel do jantar': 0.40,
           'Painel e rack da TV': 0.40}
# [Jonathan 02/09] "vamos colocar o painel e rack a 11.500" — preço de VENDA
# fechado, por cima da MC do item. A MC que ele implica é calculada e impressa,
# não escondida.
PRECO_FIXO = {'Painel e rack da TV': 11500}

cd_item, area_item, ordem_item = defaultdict(float), defaultdict(float), []
for a in ordem:
    k = UNIR.get(a, a)
    if k not in ordem_item: ordem_item.append(k)
    cd_item[k] += cd_amb[a]; area_item[k] += area_amb[a]
assert abs(sum(cd_item.values()) - CD) < 0.01
assert set(cd_item) == set(MC_ITEM), (set(cd_item), set(MC_ITEM))

print('\n' + '─'*W)
print('INVESTIMENTO POR ITEM — MC fechada item a item, com RT')
print(f'  {"":26}{"m² chapa":>10}{"custo direto":>14}{"MC":>7}{"investimento":>15}')
PRECO_ITEM, INV = {}, 0
for a in ordem_item:
    if a in PRECO_FIXO:                  # preço fechado manda na MC do item
        v = PRECO_FIXO[a]
        mc = mc_conferida(v, cd_item[a]) - (LIQF_*RT_PCT if RT_FECHADO else 0)
        marca = '  ◄ preço fechado'
    else:
        mc = MC_ITEM[a]
        v = round(cd_item[a]/div(mc, RT_FECHADO)/100)*100
        marca = ''
    PRECO_ITEM[a] = v; INV += v
    print(f'  {a:<26}{area_item[a]:>7.2f} m²{"R$ "+brl(cd_item[a],0):>14}'
          f'{mc*100:>6.0f}%{"R$ "+brl(v,0):>15}{marca}')
print(f'  {"TOTAL":<26}{area_tot:>7.2f} m²{"R$ "+brl(CD,0):>14}{"":>7}'
      f'{"R$ "+brl(INV,0):>15}')
_mcjob = mc_conferida(INV, CD) - LIQF_*RT_PCT
INV_SEM = round(CD/(BASE - _mcjob)/100)*100     # o mesmo job, sem a RT
print(f'\n  ► INVESTIMENTO FECHADO ....... R$ {brl(INV,0)}     [Jonathan 02/09]')
print(f'    MC do JOB, misturada: {_mcjob*100:.1f}% com RT'
      f'   (era 35% cravada em tudo, R$ {brl(PRECOS[0.35][1],0)})')
for a in PRECO_FIXO:
    _m = mc_conferida(PRECO_FIXO[a], cd_item[a]) - LIQF_*RT_PCT
    print(f'    ◄ "{a}" com preço fechado em R$ {brl(PRECO_FIXO[a],0)} '
          f'implica MC de {_m*100:.1f}%')
if _mcjob < 0.35:
    print('  ⚠ ABAIXO DO PISO DE 35% DA CASA — a mistura das margens derrubou')
    print('    a MC do job. Registrado para não ser lido como erro de motor.')
rm = INV_SEM/area_tot
print(f'  R$/m² de chapa: {rm:.0f} sem RT   (faixa da casa: 626–834)')
if not 626 <= rm <= 834:
    print(f'  ⚠ FORA DA FAIXA — conferir. Vidro, LED, adega e perfil somam '
          f'R$ {brl(custo_terc+custo_led,0)}.')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(DUV)} itens')
for i, (a, t) in enumerate(DUV, 1):
    print(f'  {i:>2}. [{a}]\n      {t}')
print('\n  ★ Preços adotados, sem linha fechada na base:')
print(f'     · porta de vidro reflecta bronze completa — R$ {brl(VIDRO_M2,0)}/m²')
print(f'       (a base tem a folha de ~2,00 × 0,36 a R$ 475 = R$ 660/m²,')
print(f'        referência confirmada no job Kenia & Fábio 12/06/2026)')
print(f'     · LED 3000 K comum — R$ {brl(LED_M,0)}/m (fita 28 + perfil 38). Se')
print(f'       for COB, a base manda R$ 150/m e o job sobe ~R$ 800')
print(f'     · perfil de alumínio na base — R$ {brl(PERFIL_ALU_M,0)}/m')
print(f'     · puxador sotille bronze — R$ {brl(PUX_SOTILLE,0)}/un')
print(f'     · adega em tubinho preto — R$ {brl(ADEGA_UN,0)} por garrafa')
print(f'     · borda arredondada R20 — R$ {brl(RAIO_UN,0)} por canto')
print(f'     · meia esquadria — R$ {brl(ESQ_M,0)}/m (a base não separa chanfro')
print( '       de cava; a cava fica nos R$ 25/m de sempre)')
print('\n⛔ FORA DO ESCOPO: sofá, mesa, cadeiras, poltrona, tapete, pendente,')
print('   cortina, TV, ar-condicionado, gesso e sanca, rodapé de obra,')
print('   sarrafeamento das paredes, revestimento, pintura e pontos elétricos.')
print('═'*W)
