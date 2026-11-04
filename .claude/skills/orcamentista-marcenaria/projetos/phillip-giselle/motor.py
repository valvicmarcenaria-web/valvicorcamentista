# -*- coding: utf-8 -*-
"""PHILLIP E GISELLE · motor comum do levantamento (cm, preços da Base de Custos).
Executivo Janaina Pacheco Arquitetura, REV02. Escopo: folhas 07 a 25 (páginas
9 a 27 do PDF). ⛔ Academia, rooftop e fachada FORA [Jonathan, 04/11/2026].

Cada ambiente mora no seu arquivo e chama P() / O() / helpers daqui.
"""
import math, os

CHAPA_M2, APROV = 5.0875, 0.80
COR = {18: 700.0, 15: 550.0, 6: 350.0}           # Melamínico Fosco (cor e amadeirado)
BRANCO = {18: 400.0, 15: 350.0, 6: 250.0}         # Branco TX
FITA = {'cor': (3.00, 2.50), 'branco': (2.00, 2.50),
        'ripa': (3.00, 2.50),                    # ⭐ ripa vai à coladeira [Jonathan 04/11]
        'cor30': (7.00, 5.00),
        'porta60': (8.00, 2.50)}                 # ⭐ fita de 60 da porta, R$ 8 [Jonathan 04/11]
FITA_PERD = 0.10
CORTE_CHAPA, CORTE_PECA = 2.00, 2.50
CONSUM, EMBAL = 0.06, 0.02

LINHA = os.environ.get('LINHA', 'gold')
#   telescópica: Bigfer Telescópica R$ 15/par + Bigfer Slow Click R$ 4
#   hettich:     Quadro V6 oculta R$ 150/par + Sensys R$ 50
#   blum:        Corrediça Blum R$ 300/gaveta + Dobradiça Blum R$ 50
DOBR, CORR = {'telescopica': (4.0, 15.0), 'silver': (4.0, 15.0),
              'padrao': (10.0, 80.0), 'hettich': (50.0, 150.0),
              'gold': (50.0, 150.0), 'blum': (50.0, 300.0)}[LINHA]

pecas, outras = [], []
AMB = [None]          # ambiente corrente

def ambiente(nome):
    AMB[0] = nome

def preco_chapa(chave):
    """'Areia 18' → 700 · 'Branco TX 15' → 350."""
    cor, esp = chave.rsplit(' ', 1)
    return (BRANCO if cor == 'Branco TX' else COR)[int(esp)]

def P(movel, nome, c, l, qtd, chapa, fita_m=0.0, tf=None):
    tf = tf or ('branco' if chapa.startswith('Branco') else 'cor')
    pecas.append(dict(amb=AMB[0], movel=movel, nome=nome, c=c, l=l, qtd=qtd,
                      chapa=chapa, fita=fita_m, tf=tf))

def O(movel, item, qtd, un, pu, obs=''):
    outras.append(dict(amb=AMB[0], movel=movel, item=item, qtd=qtd, un=un,
                       pu=pu, obs=obs))

# ── helpers de construção ──────────────────────────────────────────────
def caixa(movel, L, A, Pf, cor_ext=None, interno='Branco TX 15', fundo=True,
          lat_vistas=0, base_vista=False, teto_visto=False):
    """Caixa de armário: 2 laterais, base, teto, fundo 6 mm.
    lat_vistas = quantas laterais saem na cor externa (15 mm)."""
    ext = f'{cor_ext} 15' if cor_ext else interno
    for i in range(2):
        ch = ext if i < lat_vistas else interno
        P(movel, 'Lateral', A, Pf, 1, ch, (A + Pf) / 100 if ch == ext else A / 100)
    P(movel, 'Base', L - 3, Pf, 1, ext if base_vista else interno, (L - 3) / 100)
    P(movel, 'Teto', L - 3, Pf, 1, ext if teto_visto else interno, (L - 3) / 100)
    if fundo:
        ch = fundo if isinstance(fundo, str) else 'Branco TX 6'
        P(movel, 'Fundo', L - 3, A - 3, 1, ch)

def divisorias(movel, n, A, Pf, ch='Branco TX 15'):
    if n: P(movel, 'Divisória', A, Pf - 2, n, ch, A / 100)

def prateleiras(movel, n, vao, Pf, ch=None, suporte=True):
    if not n: return
    ch = ch or ('Branco TX 18' if vao > 70 else 'Branco TX 15')
    P(movel, 'Prateleira', vao - 0.4, Pf - 3, n, ch, (vao) / 100)
    if suporte: O(movel, 'Suporte de prateleira (jogo de 4)', n, 'prat.', 6.5)
    if vao > 120: O(movel, 'Alma de aço barra chata 5 mm', n, 'barra', 50)

def portas(movel, n, L, A, cor, giro=True):
    P(movel, 'Porta', A, L, n, f'{cor} 18', 2 * (L + A) / 100)
    if giro:
        d = 2 if A <= 90 else 3 if A <= 160 else 4 if A <= 200 else 5
        O(movel, 'Dobradiça c/ amortecimento', n * d, 'un', DOBR)

def gavetas(movel, n, L, A, Pf, cor, frente=True):
    if frente:
        P(movel, 'Frente de gaveta', L, A, n, f'{cor} 18', 2 * (L + A) / 100)
    li, alt = L - 6.6, max(A - 5, 8)
    P(movel, 'Gaveta · lateral', Pf - 5, alt, 2 * n, 'Branco TX 15', (Pf - 5) / 100)
    P(movel, 'Gaveta · frente int./traseira', li, alt, 2 * n, 'Branco TX 15', li / 100)
    P(movel, 'Gaveta · fundo', li + 1, Pf - 6, n, 'Branco TX 6')
    O(movel, 'Corrediça', n, 'par', CORR)

def cabideiro(movel, vao):
    O(movel, 'Cabideiro (tubo oval)', 1, 'un', 120.0, f'vão {vao} cm')

def correr(movel, folhas, A, cor, trilho_m=2):
    """Portas de correr: folha em 18 mm, sistema SS150 (Base), trilho e
    desempenador (1 por folha; 2 se a folha tem 70 cm ou mais)."""
    for L in folhas:
        P(movel, 'Porta de correr', A, L, 1, f'{cor} 18', 2 * (L + A) / 100)
        O(movel, 'Desempenador de porta', 2 if L >= 70 else 1, 'un', 100)
    O(movel, 'Sistema de correr SS150, 2 portas', 1, 'cj', 600)
    O(movel, f'Trilho SS150 {trilho_m} m', 1, 'un', 200 if trilho_m <= 2 else 250)

def led(movel, m, obs=''):
    O(movel, 'LED COB conjunto (fita, perfil, usinagem, instalação)', m, 'm', 150, obs)

RIPADO_M2 = 180.0     # laminação do ripado, R$/m² (Base · Terceirizados)
def ripado(movel, L, A, cor, passo=3.0, larg=2.0, base=True):
    """Cálculo padrão da casa: ripa de 2 com vão de 1 (passo 3), tirada da
    chapa de 18 com perda de serra ×1,10; fita nas DUAS arestas à vista,
    filetagem na coladeira; laminação do ripado por m². Base: painel de 15 mm
    na mesma cor — na PORTA não há base, a base é o sanduíche."""
    n = math.floor((L + 1) / passo)
    if base:
        P(movel, 'Painel base do ripado', A, L, 1, f'{cor} 15', 0)
    P(movel, 'Ripa 2 × 2 (×1,10 perda)', A, larg * 1.10, n, f'{cor} 18',
      2 * A / 100, 'ripa')
    O(movel, 'Laminação do ripado', L * A / 1e4, 'm²', RIPADO_M2)

# ── PORTA DE PASSAGEM: a folha é FEITA [Jonathan, 04/11/2026] ───────────
#   laminacao-e-construcao.md, seção PORTA DE PASSAGEM:
#   ① duas peles de 6 mm na cor · ② miolo G-Door em réguas de 15 no
#   perímetro · ③ ripada: 2 metalons · ④ ripada: ripado padrão SEM base ·
#   ⑤ cava e sistema (pivô ou deslizante).
GDOOR_M2 = 600.0 / (2.75 * 2.055 * 0.80)    # R$ 132,71 o m² de régua
SISTEMA = {'pivo': ('Sistema pivô', 120.0),
           'correr': ('Sistema deslizante RO82 Top c/ amortecimento', 600.0)}
def porta_passagem(movel, L, A, cor_a, cor_b=None, ripada=None, sistema='pivo',
                   cava=True, extra=()):
    cor_b = cor_b or cor_a
    P(movel, 'Porta · pele 6 mm face A', A, L, 1, f'{cor_a} 6', 2 * (L + A) / 100, 'porta60')
    P(movel, 'Porta · pele 6 mm face B', A, L, 1, f'{cor_b} 6', 0)
    a_gd = (2 * 15 * A + 2 * 15 * (L - 30)) / 1e4
    O(movel, 'Miolo G-Door em réguas de 15', a_gd, 'm²', GDOOR_M2)
    if ripada:
        ripado(movel, L, A, ripada, base=False)
        O(movel, 'Perfil de metalon contra empeno (barra 3 m)',
          2 * math.ceil(A / 300), 'barra', 100)
    nome, pu = SISTEMA[sistema]
    O(movel, nome, 1, 'cj', pu)
    if cava: O(movel, 'Cava 45° usinada', 1, 'frente', 50)
    for item, q, un, v in extra: O(movel, item, q, un, v)

# ── cálculo ─────────────────────────────────────────────────────────────
def calcula(frete=0.0):
    area, fita, npc = {}, {}, 0
    for p in pecas:
        a = p['c'] * p['l'] / 1e4 * p['qtd']
        area[p['chapa']] = area.get(p['chapa'], 0) + a
        fita[p['tf']] = fita.get(p['tf'], 0) + p['fita'] * p['qtd']
        npc += p['qtd']
    chapas = {k: max(1, math.ceil(v / (CHAPA_M2 * APROV))) for k, v in area.items()}
    c_chapa = sum(chapas[k] * preco_chapa(k) for k in chapas)
    c_fita = sum(m * (1 + FITA_PERD) * FITA[t][0] + m * FITA[t][1] for t, m in fita.items())
    c_out = sum(o['qtd'] * o['pu'] for o in outras)
    c_corte = sum(chapas.values()) * CORTE_CHAPA + npc * CORTE_PECA
    c_cons = CONSUM * (c_chapa + c_fita)
    sem = c_chapa + c_fita + c_out + c_corte + c_cons + frete
    emb = sem * EMBAL / (1 - EMBAL)
    return dict(area=area, chapas=chapas, fita=fita, npecas=npc, chapa=c_chapa,
                fita_r=c_fita, outras=c_out, corte=c_corte, consum=c_cons,
                frete=frete, emb=emb, CD=sem + emb)

def custo_por_ambiente(R):
    """Rateio: chapa pelo custo médio do m² da chave, fita pela peça,
    ferragem pelo item. Corte, consumíveis e frete seguem a CHAPA+FITA do
    ambiente; a embalagem (2%) segue o custo de cada um. Soma = custo direto."""
    m2 = {k: R['chapas'][k] * preco_chapa(k) / R['area'][k] for k in R['area']}
    mdf, fer = {}, {}
    for p in pecas:
        a = p['c'] * p['l'] / 1e4 * p['qtd']; f = p['fita'] * p['qtd']
        v = a * m2[p['chapa']] + f * (1 + FITA_PERD) * FITA[p['tf']][0] + f * FITA[p['tf']][1]
        mdf[p['amb']] = mdf.get(p['amb'], 0) + v
    for o in outras:
        fer[o['amb']] = fer.get(o['amb'], 0) + o['qtd'] * o['pu']
    ambs = list(dict.fromkeys([p['amb'] for p in pecas] + [o['amb'] for o in outras]))
    tm = sum(mdf.values()); rateio = R['corte'] + R['consum'] + R['frete']
    c = {a: mdf.get(a, 0) * (1 + rateio / tm) + fer.get(a, 0) for a in ambs}
    k = R['CD'] / sum(c.values())
    return {a: v * k for a, v in c.items()}

def brl(v): return f'R$ {v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
