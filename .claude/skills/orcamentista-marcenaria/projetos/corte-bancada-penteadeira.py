# -*- coding: utf-8 -*-
"""BANCADA / PENTEADEIRA DE QUARTO — LEVANTAMENTO E PREÇO.

[Jonathan 25/08] Render de referência enviado no chat. Pedido:
  · orçar a bancada COM penteadeira basculante no tampo
  · escopo: da TORRE DE PRATELEIRAS (inclusive) para a esquerda
  · FORA: painel de cabeceira (ripado + mármore) e mesa de cabeceira
  · o nicho fechado de cima (aéreo com 2 portas amadeiradas) vira NICHO ABERTO

COTA REAL, medida em obra: PAREDE DE 312 × 257 cm  [Jonathan 25/08].
   A primeira rodada deste orçamento saiu com 210 × 250, adotados por escala
   do render. A parede é 48% mais larga. Refeito inteiro sobre a cota medida —
   e o móvel maior nesta ficou com preço por m² MENOR, porque a chapa passou a
   render. Ver o bloco de aproveitamento no relatório.

   O que continua ESTIMADO (não medido) e precisa de conferência em obra:
     · profundidades — 50 na bancada e 35 no nicho e na torre, os padrões da
       base da casa
     · as alturas intermediárias das prateleiras (155 e 195)
     · a largura da torre (35) e a do gaveteiro (48)
   A largura e a altura totais, essas, são cota de obra.

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

# ── nesting da casa (idêntico a corte-carla.py) ───────────────────────────
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

# ── preços · dados/materiais.json, atualizado em 11/06/2026 ───────────────
PRC_COR = {6: 300.0, 15: 500.0, 18: 600.0, 25: 900.0}   # Melamínico Fosco
PRC_BRA = {6: 190.0, 15: 260.0, 18: 330.0, 25: 420.0}   # Branco TX
# ★ COR 25 mm NÃO EXISTE NA BASE. A base para em 18 mm (600). Os 900 são a
#   extrapolação que os motores da casa já vinham usando (600 × 1,5). Só o
#   tampo e a tampa basculante caem nessa linha — ver DÚVIDAS.
NOME_MAT = {'AM': 'MDF amadeirado', 'FE': 'MDF fendi', 'BT': 'MDF Branco TX'}
def prc(m, e): return PRC_BRA[e] if m == 'BT' else PRC_COR[e]

FITA_M, FILET_M, DESPERD = 3.00, 2.50, 1.10
CAVA_USIN = 25.0                   # usinagem de cava, por metro linear
SUP_PRAT  = 1.50
LED_M     = 28.0 + 38.0            # fita 28 + perfil de alumínio 38
# ⚠ A base traz "LED COB (fita + perfil + usinagem)" a R$ 150/m. Os motores da
#   casa (Eliuton, Vinícius, Carla, SPE) todos usam 66/m. Mantive 66 por
#   coerência com o que já foi vendido; se o projeto pedir COB, a iluminação
#   sobe de ~R$ 450 para ~R$ 1.020. Está nas DÚVIDAS.
ESPELHO_PC = 285.0                 # peça mínima de espelharia (corte + lapidação)

# ── PUXADOR DO GAVETEIRO: perfil AREZZO  [Jonathan 25/08] ─────────────────
# ★ Arezzo NÃO EXISTE na base. É perfil de alumínio da Rometal; adotei a linha
#   do "Perfil cava Rometal RM195" (R$ 250 a barra de 3 m), que é a faixa dele.
#   CONFIRMAR o custo de compra — se vier a R$ 100 como o RM213, cai R$ 150.
PUX_BARRA_M   = 3.0
PUX_BARRA_R   = 250.0
PUX_TAMPINHA  = 4.0                # o par, por frente

# ── DUAS LINHAS DE FERRAGEM  [Jonathan 25/08] ─────────────────────────────
#   O móvel é o MESMO nas duas: mesmo desenho, mesmas cores, mesmo corte
#   racionalizado. O que muda é a ferragem — e com ela a garantia.
#   ★ A dobradiça Blum não está na base. Adotei R$ 60 (Clip Top Blumotion).
#     Pesa pouco: são 2 dobradiças no móvel inteiro.
LINHAS = {
 'HETTICH': dict(nome='Hettich', gar=10,
                 dobr=10.0,  dobr_nome='Hettich Novisys',
                 corr=120.0, corr_nome='Hettich Quadro, oculta',
                 art=30.0,   art_qtd=2, art_est=False,
                 art_nome='dois pistões a gás com amortecimento'),
 'BLUM':    dict(nome='Blum', gar=20,
                 dobr=60.0,  dobr_nome='Blum Clip Top Blumotion', dobr_est=True,
                 corr=300.0, corr_nome='Blum, oculta com Blumotion',
                 art=250.0,  art_qtd=1, art_est=False,
                 art_nome='articulador Blum HK-xs'),
}

P, FITA, TERC, LED, DUV = [], [], [], [], []
FER = defaultdict(lambda: [0, 0, 0])       # dobradiças · corrediças · pistões
CAVA_M = defaultdict(float)
def add(mat, esp, amb, desc, c, l, q=1): P.append((mat, esp, amb, desc, c, l, q))
def fer(a, dobr=0, gav=0, pist=0):
    FER[a][0] += dobr; FER[a][1] += gav; FER[a][2] += pist
def fita(a, d, m): FITA.append((a, d, m))
def terc(a, d, v, est=False): TERC.append((a, d, v, est))
def led(a, d, m): LED.append((a, d, m))
def cava(a, m): CAVA_M[a] += m
def duv(a, t): DUV.append((a, t))
def gaveta(mat, amb, nome, L, Pf, alt, q=1):
    add(mat, 15, amb, f'{nome} · caixa lateral',       Pf-10, alt, 2*q)
    add(mat, 15, amb, f'{nome} · caixa frente/costas', L-6,   alt, 2*q)
    add(mat, 6,  amb, f'{nome} · fundo de gaveta',     L-6,   Pf-10, q)

# ═══════════════════════════════════════════════════════════════════════════
# GEOMETRIA — cota REAL da parede, medida em obra: 312 × 257 cm.
#
#   [Jonathan 25/08] "medida real da Parede 3.12x257" + foto do quarto.
#   A foto trocou a base do orçamento: eu tinha ADOTADO 210 × 250 lendo o
#   render por escala. A parede é 312 × 257 — 48% mais larga. O móvel cresce,
#   e junto com ele o aproveitamento de chapa (é a boa notícia).
#
#   A foto também mostra o que o render não mostrava:
#     · o painel de cabeceira (ripado + mármore) e a mesa de cabeceira JÁ
#       ESTÃO INSTALADOS, na parede ao lado — por isso saem do escopo
#     · há rebaixo de gesso com rasgo de LED linear no teto
#     · piso vinílico escuro já assentado, com rodapé
#
#   Distribuição na parede:
#     ├──────────────── 277 bancada ────────────────┤├── 35 torre ──┤
#
#   Alturas, de cima para baixo:
#     257 ┬ teto
#         │  NICHO SUPERIOR ABERTO (era aéreo com portas)   45 de altura
#     212 ┼
#     195 ── prateleira superior
#     155 ── prateleira inferior (LED por baixo)
#         │  painel de fundo
#      75 ┼ tampo da bancada
#         │  lateral de apoio · vão da cadeira · gaveteiro · penteadeira
#       0 ┴ piso
#
#   ⚠ 277 e 257 NÃO CABEM inteiros na chapa de 275 × 185. Painel de fundo,
#     prateleiras e nicho saem em DUAS peças por nível, emendadas em linha
#     sobre sarrafo contínuo. É construção normal — mas é o tipo de coisa
#     que só aparece quando se faz o plano de corte de verdade.
#
# DOIS CENÁRIOS, MESMA APARÊNCIA:
#   RAC=False · como o render especifica — 3 cores × 4 espessuras
#   RAC=True  · corte racionalizado, sem espessura que exista para uma peça só
# ═══════════════════════════════════════════════════════════════════════════
LARG_PAREDE = 312.0
LARG_TORRE  = 35.0
LARG_BANC   = LARG_PAREDE - LARG_TORRE          # 277
PROF_BANC, PROF_NICHO = 50.0, 35.0
PD = 257.0
H_TAMPO, H_NICHO = 75.0, 45.0
H_PAINEL = (PD - H_NICHO) - H_TAMPO             # 137 de painel de fundo
MEIA = LARG_BANC/2                              # 138,5 — a peça que cabe na chapa

def montar(RAC):
    """Reconstrói o levantamento inteiro. RAC liga o corte racionalizado."""
    P.clear(); FITA.clear(); TERC.clear(); LED.clear(); DUV.clear()
    FER.clear(); CAVA_M.clear()

    ESP_FRENTE    = 15 if RAC else 18        # frente de gaveta
    MAT_FUNDO_INT = 'AM' if RAC else 'BT'    # fundos que ninguém vê
    ESP_PRAT      = 15 if RAC else 25        # prateleiras longas aparentes

    # ───────────────────────────────────────────────────────────────────────
    # 1 · BANCADA E PENTEADEIRA BASCULANTE — fendi
    #     Tampo de 277 partido em trecho fixo (217) + tampa basculante (60).
    # ───────────────────────────────────────────────────────────────────────
    A = 'Bancada e penteadeira'
    add('FE', 25, A, 'tampo fixo 2170 × 500',                     217, PROF_BANC, 1)
    add('FE', 25, A, 'tampa basculante da penteadeira 600 × 460',  60, 46, 1)
    fita(A, 'tampo · bordas aparentes', 2.17 + 2*0.50 + 2*(0.60+0.46))
    terc(A, 'Espelho prata colado na face interna da tampa', ESPELHO_PC, est=True)
    fer(A, dobr=2, pist=2)
    add('FE', 15, A, 'penteadeira · lateral da caixa',         46, 12, 2)
    add('FE', 15, A, 'penteadeira · frente e costas da caixa', 58, 12, 2)
    add('FE', 15, A, 'penteadeira · fundo da caixa',           58, 46, 1)
    add('FE', 15, A, 'penteadeira · divisória organizadora',   44, 10, 2)
    fita(A, 'penteadeira · bordas da caixa e divisórias', 2*(0.46+0.58) + 2*0.44)
    # apoios do tampo: lateral cega à esquerda e montante no meio do vão
    add('FE', 15, A, 'lateral de apoio esquerda 500 × 730', PROF_BANC, 73, 1)
    add('FE', 15, A, 'montante central de apoio do tampo',  PROF_BANC, 73, 1)
    add('FE', 15, A, 'rodapé recuado',                      46, 10, 2)
    fita(A, 'apoios · topo e frente', 2*(0.50 + 0.73))
    duv(A, 'com 277 cm de vão o tampo NÃO se sustenta só nas pontas. Entrou um '
           'montante central de apoio, que no render não aparece. Se a cliente '
           'quiser o vão totalmente livre, o tampo vira estrutura metálica '
           'embutida — e isso é serralheria, não marcenaria.')
    duv(A, 'no render não dá para cravar se o apoio esquerdo é lateral cega ou '
           'módulo com porta. Orcei como LATERAL CEGA — se for módulo fechado, '
           'entram ~0,7 m² de chapa, 2 dobradiças e uma frente.')
    duv(A, 'a tampa basculante foi dimensionada em 600 × 460, o vão útil de uma '
           'penteadeira de uso real. Se a ideia for um trecho maior basculando, '
           'muda a ferragem e o número de pistões.')

    # ───────────────────────────────────────────────────────────────────────
    # 2 · GAVETEIRO DE 3 GAVETAS — fendi
    # ───────────────────────────────────────────────────────────────────────
    A = 'Gaveteiro'
    add('FE', 15, A, 'lateral 500 × 730',   PROF_BANC, 73, 2)
    add('FE', 15, A, 'base 450 × 500',      45, PROF_BANC, 1)
    add('FE', 15, A, 'travessa superior',   45, 10, 2)
    add('FE', 15, A, 'rodapé recuado',      45, 10, 1)
    add(MAT_FUNDO_INT, 6, A, 'fundo 450 × 730', 45, 73, 1)
    add('FE', ESP_FRENTE, A, 'frente de gaveta 480 × 220', 48, 22, 3)
    gaveta(MAT_FUNDO_INT, A, 'gaveta', 45, PROF_BANC, 18, 3)
    fer(A, gav=3)
    # puxador em PERFIL AREZZO nas 3 frentes  [Jonathan 25/08]
    _m_pux = 3*0.48
    _barras = math.ceil(_m_pux/PUX_BARRA_M)
    terc(A, f'Puxador perfil Arezzo — {_barras} barra(s) de {PUX_BARRA_M:.0f} m '
            f'+ tampinhas', _barras*PUX_BARRA_R + 3*PUX_TAMPINHA, est=True)
    fita(A, 'gaveteiro · 3 frentes', 3*2*(0.48+0.22))

    # ───────────────────────────────────────────────────────────────────────
    # 3 · PAINEL DE FUNDO E DUAS PRATELEIRAS — branco
    #     277 não cabe na chapa: duas peças de 138,5 por nível.
    # ───────────────────────────────────────────────────────────────────────
    A = 'Painel de fundo e prateleiras'
    add('BT', 15, A, f'painel de fundo {MEIA*10:.0f} × {H_PAINEL*10:.0f}',
        MEIA, H_PAINEL, 2)
    add('BT', ESP_PRAT, A, f'prateleira {MEIA*10:.0f} × 350', MEIA, PROF_NICHO, 4)
    add('BT', 15, A, 'sarrafo contínuo de fixação da prateleira', MEIA, 8, 4)
    if RAC:
        add('BT', 15, A, 'prateleira · engrossamento da borda frontal', MEIA, 8, 4)
        fita(A, 'prateleiras · borda engrossada', 2*LARG_BANC/100)
    fita(A, 'prateleiras · frente e topos', 2*(LARG_BANC/100 + 2*PROF_NICHO/100))
    led(A, 'LED sob as duas prateleiras', 2*LARG_BANC/100)
    duv(A, 'a prateleira de 277 cm sai em duas peças emendadas em linha, sobre '
           'sarrafo contínuo parafusado no painel. Sem o sarrafo ela barriga no '
           'meio — não existe prateleira de 2,77 m apoiada só nas pontas.')
    duv(A, 'o painel de fundo pode ser parede pintada, e não marcenaria. Está '
           'no orçamento como painel de 15 mm — se for pintura, saem ~3,8 m².')

    # ───────────────────────────────────────────────────────────────────────
    # 4 · NICHO SUPERIOR ABERTO — amadeirado   [Jonathan 25/08]
    #     Era aéreo com portas; vira nicho aberto. Interior = acabamento.
    # ───────────────────────────────────────────────────────────────────────
    A = 'Nicho superior aberto'
    add('AM', 18, A, f'tampo e base {MEIA*10:.0f} × 350', MEIA, PROF_NICHO, 4)
    add('AM', 15, A, 'lateral 350 × 450',                 PROF_NICHO, H_NICHO, 2)
    add('AM', 15, A, 'divisória 350 × 420',               PROF_NICHO, 42, 3)
    add('AM', 6,  A, f'fundo aparente {MEIA*10:.0f} × 420', MEIA, 42, 2)
    fita(A, 'nicho aberto · todas as bordas à vista',
         2*(LARG_BANC/100 + 2*PROF_NICHO/100) + 2*(H_NICHO/100 + PROF_NICHO/100)
         + 3*(0.42 + PROF_NICHO/100))
    led(A, 'LED no nicho superior', LARG_BANC/100)
    duv(A, 'com o nicho ABERTO o interior vira peça de acabamento: o fundo sai '
           'em amadeirado, não em branco, e toda borda leva fita. É o que '
           'encarece a troca pedida — e é o certo.')

    # ───────────────────────────────────────────────────────────────────────
    # 5 · TORRE DE PRATELEIRAS — amadeirado, do piso ao teto
    # ───────────────────────────────────────────────────────────────────────
    A = 'Torre de prateleiras'
    add('AM', 15, A, f'lateral 350 × {(PD-2)*10:.0f}', PROF_NICHO, PD-2, 2)
    add('AM', 18, A, 'tampo e base 320 × 350',         32, PROF_NICHO, 2)
    add('AM', 18, A, 'prateleira de nicho 320 × 350',  32, PROF_NICHO, 6)
    add('AM', 6,  A, f'fundo aparente 320 × {(PD-2)*10:.0f}', 32, PD-2, 1)
    fita(A, 'torre · frentes de lateral, prateleiras e nichos',
         2*(PD-2)/100 + 8*(0.32 + 2*PROF_NICHO/100))
    led(A, 'LED nos 6 nichos da torre', 6*0.32)
    duv(A, 'adotei a torre do PISO AO TETO, com a bancada morrendo nela. Se ela '
           'nascer no tampo, saem ~1,3 m² de chapa.')
    duv(A, 'a foto mostra rebaixo de gesso com rasgo de LED no teto. CONFERIR '
           'se o rebaixo avança sobre esta parede: se avançar, a altura livre '
           'cai e o arremate superior muda.')
    duv(A, 'a foto não mostra tomada nesta parede. CONFERIR os pontos de energia '
           'antes do corte — bancada de trabalho com impressora precisa de '
           'tomada no nível do tampo e passa-fio no painel.')
# ═══════════════════════════════════════════════════════════════════════════
# ═══════════════════════════════════════════════════════════════════════════
# CÁLCULO — corte racionalizado, duas linhas de ferragem
# ═══════════════════════════════════════════════════════════════════════════
N_CARRETO, R_CARRETO = 1, 600.0
N_VISITA,  R_VISITA  = 1, 250.0
LOG = N_CARRETO*R_CARRETO + N_VISITA*R_VISITA
MC = 0.40                  # [Jonathan 25/08] margem fechada
PRAZO = '90 dias corridos'
ENT_PCT = 0.40             # entrada de 40% + 60% na entrega

def rodar(RAC, linha):
    L = LINHAS[linha]
    montar(RAC)
    por, area_ch, area_amb = defaultdict(list), defaultdict(float), defaultdict(float)
    for m, e, a, d, c, l, q in P:
        for _ in range(q): por[(m, e)].append((c, l))
        ar = c*l*q/10000
        area_ch[(m, e)] += ar; area_amb[a] += ar
    CH = {k: nest(v) for k, v in por.items()}
    custo_chapa = sum(n*prc(k[0], k[1]) for k, n in CH.items())
    area_tot = sum(area_ch.values())
    m_fita_expl = sum(m for _, _, m in FITA)
    m_fita = max(m_fita_expl, area_tot*2.6)
    custo_fita, custo_filet = m_fita*DESPERD*FITA_M, m_fita*FILET_M
    n_cava = sum(CAVA_M.values()); custo_cava = n_cava*CAVA_USIN
    m_led = sum(m for _, _, m in LED); custo_led = m_led*LED_M
    n_prat = sum(q for m, e, a, d, c, l, q in P
                 if 'prateleira' in d.lower() and 'engrossamento' not in d.lower())
    custo_sup = n_prat*4*SUP_PRAT
    custo_terc = sum(v for _, _, v, _ in TERC)
    td = sum(x[0] for x in FER.values())
    tg = sum(x[1] for x in FER.values())
    na = L['art_qtd']
    custo_ferr = td*L['dobr'] + tg*L['corr'] + na*L['art']
    consum = (custo_chapa + custo_fita)*0.06
    CD = (custo_chapa + custo_fita + custo_filet + custo_cava + custo_led
          + custo_sup + custo_terc + consum + custo_ferr + LOG)
    return dict(L=L, CH=CH, area_ch=area_ch, area_amb=dict(area_amb), area_tot=area_tot,
                tot_ch=sum(CH.values()), custo_chapa=custo_chapa, m_fita=m_fita,
                m_fita_expl=m_fita_expl, custo_fita=custo_fita, custo_filet=custo_filet,
                custo_cava=custo_cava, m_led=m_led, custo_led=custo_led, n_prat=n_prat,
                custo_sup=custo_sup, custo_terc=custo_terc, consum=consum,
                custo_ferr=custo_ferr, fer=(td, tg, na), CD=CD,
                ordem=list(dict.fromkeys(x[2] for x in P)),
                fer_amb={k: list(v) for k, v in FER.items()},
                terc=list(TERC), duv=list(DUV),
                aprov=area_tot/(sum(CH.values())*CH_AREA)*100)

def brl(v, n=2):
    return f'{v:,.{n}f}'.replace(',', '§').replace('.', ',').replace('§', '.')
def preco(CD, rt=False): return round(CD/div(MC, rt)/100)*100

H = rodar(True,  'HETTICH')     # racionalizado + Hettich  → 10 anos
B = rodar(True,  'BLUM')        # racionalizado + Blum     → 20 anos
R = rodar(False, 'HETTICH')     # como o render especifica → só referência interna
INV_H, INV_B = preco(H['CD']), preco(B['CD'])
INV_R = preco(R['CD'])

montar(True)
_fora = [(m, e, a, d, c, l) for m, e, a, d, c, l, q in P
         if max(c, l) > CH_C or min(c, l) > CH_L]
if _fora:
    print('\n' + '!'*W + '\nPEÇAS QUE NÃO CABEM NA CHAPA DE 275 × 185')
    for m, e, a, d, c, l in _fora:
        print(f'  {NOME_MAT[m]} {e} mm · {a} · {d}: {c:.0f} × {l:.0f} cm')
    print('!'*W + '\n')

print('═'*W)
print('BANCADA COM PENTEADEIRA BASCULANTE — LEVANTAMENTO DE MATERIAL E CUSTO')
print('═'*W)
print('Escopo: da torre de prateleiras para a esquerda. FORA: painel de cabeceira')
print('e mesa de cabeceira. O nicho de cima entra ABERTO.          [Jonathan 25/08]')
print(f'MEDIDO em obra: parede de {LARG_PAREDE:.0f} × {PD:.0f} cm.'
      f'   ADOTADO: bancada a {H_TAMPO:.0f} · prof. {PROF_BANC:.0f} na bancada '
      f'e {PROF_NICHO:.0f} no nicho e na torre.')
print(f'Corte RACIONALIZADO · MC {MC*100:.0f}% · sem RT · duas linhas de ferragem.')

print('\nESCOPO POR MÓVEL')
for a in H['ordem']:
    d, g, p = H['fer_amb'].get(a, [0, 0, 0])
    ex = [f'{d} dobr.' if d else '', f'{g} gav.' if g else '',
          f'{H["L"]["art_qtd"]} articulador(es)' if p else '']
    print(f'  {a:<30}{H["area_amb"][a]:>7.2f} m² de chapa   '
          f'{" · ".join(x for x in ex if x)}')
print(f'  {"TOTAL":<30}{H["area_tot"]:>7.2f} m²')

print('\nPLANO DE CORTE  (nesting por cor × espessura)')
for k in sorted(H['CH'], key=lambda k: (k[0], -k[1])):
    m, e = k; n = H['CH'][k]; pr = prc(m, e)
    ap = H['area_ch'][k]/(n*CH_AREA)*100
    print(f'  {NOME_MAT[m]+" "+str(e)+" mm":<26}{H["area_ch"][k]:>7.2f} m²  →  '
          f'{n:>2} ch. × R$ {brl(pr):>8} = R$ {brl(n*pr):>9}   aprov. {ap:>3.0f}%')
print(f'  {"TOTAL":<26}{H["area_tot"]:>7.2f} m²  →  {H["tot_ch"]:>2} chapas'
      f'{"":>20}R$ {brl(H["custo_chapa"]):>9}   médio {H["aprov"]:.0f}%')

print(f'\nFITA E FILETAGEM   {H["m_fita"]:.2f} m  ·  material R$ '
      f'{brl(H["custo_fita"])}  ·  filetagem R$ {brl(H["custo_filet"])}')
print(f'  (borda lançada peça a peça: {H["m_fita_expl"]:.1f} m = '
      f'{H["m_fita_expl"]/H["area_tot"]:.2f} m/m² · fator da casa 2,6 — o maior manda)')
print(f'ILUMINAÇÃO         {H["m_led"]:.2f} m × R$ {brl(LED_M)}/m  ·  '
      f'R$ {brl(H["custo_led"])}')

print('\nTERCEIRIZADOS E ITENS ESPECIAIS   (★ = sem preço fechado na base)')
for a, d, v, est in H['terc']:
    print(f' {"★" if est else " "}{a:<28}{d[:48]:<49}R$ {brl(v):>9}')

print('\n' + '═'*W)
print('CUSTO DIRETO E PREÇO — as duas linhas de ferragem')
print('═'*W)
print(f'  {"":<44}{"HETTICH · "+str(H["L"]["gar"])+" anos":>18}'
      f'{"BLUM · "+str(B["L"]["gar"])+" anos":>18}')
print(f'  {"":<44}{"─"*18:>18}{"─"*18:>18}')
linhas_custo = [
    ('Chapas',                          H['custo_chapa'], B['custo_chapa']),
    ('Fita e filetagem',                H['custo_fita']+H['custo_filet'],
                                        B['custo_fita']+B['custo_filet']),
    ('Iluminação em LED',               H['custo_led'],   B['custo_led']),
    ('Suportes de prateleira',          H['custo_sup'],   B['custo_sup']),
    ('Terceirizados (espelho + Arezzo)', H['custo_terc'], B['custo_terc']),
    ('Consumíveis (6% de chapa + fita)', H['consum'],     B['consum']),
    ('FERRAGEM',                        H['custo_ferr'],  B['custo_ferr']),
    (f'Logística — {N_CARRETO} carreto + {N_VISITA} visita', LOG, LOG),
]
for rot, vh, vb in linhas_custo:
    dif = '  ←' if abs(vb-vh) > 1 else ''
    print(f'  {rot:<44}{"R$ "+brl(vh):>18}{"R$ "+brl(vb):>18}{dif}')
print(f'  {"CUSTO DIRETO":<44}{"R$ "+brl(H["CD"]):>18}{"R$ "+brl(B["CD"]):>18}')
print(f'\n  {"INVESTIMENTO · MC "+str(int(MC*100))+"% sem RT":<44}'
      f'{"R$ "+brl(INV_H,0):>18}{"R$ "+brl(INV_B,0):>18}')
print(f'  {"MC real":<44}{mc_conferida(INV_H, H["CD"])*100:>17.1f}%'
      f'{mc_conferida(INV_B, B["CD"])*100:>17.1f}%')
print(f'  {"R$/m² de chapa   (faixa da casa 626–834)":<44}'
      f'{INV_H/H["area_tot"]:>18.0f}{INV_B/B["area_tot"]:>18.0f}')
print(f'  {"com RT de 10%":<44}{"R$ "+brl(preco(H["CD"], True),0):>18}'
      f'{"R$ "+brl(preco(B["CD"], True),0):>18}')

print('\n  ESPECIFICAÇÃO DE FERRAGEM')
for R_ in (H, B):
    L = R_['L']
    print(f'    {L["nome"]+" · "+str(L["gar"])+" anos":<22}'
          f'dobradiça {L["dobr_nome"]} · corrediça {L["corr_nome"]}')
    print(f'    {"":<22}tampa basculante em {L["art_nome"]}')

print('\n' + '═'*W)
print('CONDIÇÕES COMERCIAIS   [Jonathan 25/08]')
print('═'*W)
print(f'  Prazo de entrega .......... {PRAZO}')
print(f'  Pagamento ................. entrada de {ENT_PCT*100:.0f}% + '
      f'{(1-ENT_PCT)*100:.0f}% na entrega')
for R_, v in ((H, INV_H), (B, INV_B)):
    ent = round(v*ENT_PCT/100)*100
    print(f'    {R_["L"]["nome"]+" · "+str(R_["L"]["gar"])+" anos":<24}'
          f'R$ {brl(v,0):>9}  =  entrada R$ {brl(ent,0):>8}  +  entrega '
          f'R$ {brl(v-ent,0):>8}   (entrada {ent/v*100:.1f}%)')
_cd = H['CD'] - LOG
_ent = round(INV_H*ENT_PCT/100)*100
print(f'\n  CAIXA: custo direto de compra (sem logística) R$ {brl(_cd)}; a entrada '
      f'da linha')
print(f'  Hettich, R$ {brl(_ent,0)}, cobre {_ent/_cd*100:.0f}% dele. '
      f'{"Material entra pago." if _ent >= _cd else "⚠ FALTA CAPITAL DE GIRO."}')

print('\n' + '─'*W)
print('INVESTIMENTO POR MÓVEL   (linha Hettich · rateio pela área de chapa)')
tots, linhas = 0, []
for a in H['ordem']:
    v = round(INV_H*H['area_amb'][a]/H['area_tot']/100)*100
    linhas.append([a, H['area_amb'][a], v]); tots += v
linhas[max(range(len(linhas)), key=lambda i: linhas[i][1])][2] += INV_H - tots
for a, ar, v in linhas:
    print(f'  {a:<30}{ar:>8.2f} m²{"R$ "+brl(v,0):>16}')
print(f'  {"TOTAL":<30}{H["area_tot"]:>8.2f} m²{"R$ "+brl(INV_H,0):>16}')

print('\n' + '─'*W)
print('REFERÊNCIA INTERNA — o que o corte racionalizado economizou')
print(f'  como o render especifica (3 cores × 4 espessuras): {R["tot_ch"]:>2} chapas · '
      f'aprov. {R["aprov"]:.0f}% · R$ {brl(INV_R,0)}')
print(f'  corte racionalizado (mesma aparência):             {H["tot_ch"]:>2} chapas · '
      f'aprov. {H["aprov"]:.0f}% · R$ {brl(INV_H,0)}')
print(f'  diferença: R$ {brl(INV_H-INV_R,0)}   ⛔ NÃO VAI PARA A PROPOSTA — a regra')
print('  da casa proíbe explicar formação de preço ao cliente.')

print('\n' + '─'*W)
print(f'DÚVIDAS E CONFERÊNCIAS — {len(H["duv"])} itens')
for i, (a, t) in enumerate(H['duv'], 1):
    print(f'  {i:>2}. [{a}] {t}')
print('\n  ★ Preços sem linha fechada na base de materiais:')
print(f'     · PERFIL AREZZO — não existe na base. Adotei R$ {brl(PUX_BARRA_R,0)} a')
print('       barra de 3 m, a faixa do Perfil cava Rometal RM195. Se vier a')
print('       R$ 100 como o RM213, o preço final cai ~R$ 375.')
print('     · DOBRADIÇA BLUM — não existe na base. Adotei R$ 60 (Clip Top')
print('       Blumotion). São só 2 no móvel: impacto de ~R$ 250 no preço.')
print('     · MDF cor 25 mm — a base para em 18 mm (600). Adotei 900, a')
print('       extrapolação que os motores da casa já usavam. Pesa só no tampo.')
print('     · Espelho da penteadeira — peça mínima de espelharia (R$ 285).')
print('     · LED — a base traz LED COB a R$ 150/m; usei os R$ 66/m dos motores')
print(f'       recentes. São {H["m_led"]:.1f} m: se for COB, o preço sobe ~R$ 2.100.')
print('\n⛔ FORA DO ESCOPO: painel de cabeceira (ripado + mármore), mesa de')
print('   cabeceira, roupeiro à esquerda, elétrica, alvenaria e pintura.')
print('═'*W)
