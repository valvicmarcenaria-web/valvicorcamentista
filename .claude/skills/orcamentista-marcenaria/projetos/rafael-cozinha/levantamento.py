# -*- coding: utf-8 -*-
"""RAFAEL · Ap. Social 1º pav. · Cozinha, Jantar e Serviço
Executivo Clara Dobscha Arquitetura, pranchas 09 a 14/14, 15/10/2025.

Levantamento peça a peça (cm). Preços: Valvic · Base de Custos, lida em 04/11/2026.
⛔ Fora do escopo: bancadas em granilite (01, 02, serviço), sóculos de cimento/
   porcelanato, cuba, tanque, canto alemão em alvenaria, mesa e cadeiras, varanda.
⛔ Gaveteiro abaixo da escada (det. p. 8): FORA [Jonathan, 04/11/2026].
⭐ SEM RT e sem vendedor [Jonathan, 04/11/2026] → BASE 84,88% à vista.
"""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import motor_mc as M

CHAPA_M2, APROV = 5.0875, 0.80
CHAPA = {  # R$/chapa · cor = 700/550/350 (Base, Melamínico Fosco)
 'Azul Secreto 18': 700, 'Azul Secreto 15': 550,
 'Tauari 18': 700, 'Tauari 15': 550,
 'Mostrato 15': 550,
 'Branco TX 15': 350, 'Branco TX 6': 250,
}
# fita: (R$ fita/m, R$ filetagem/m)
FITA = {'cor': (3.00, 2.50), 'branco': (2.00, 2.50),
        'cor30': (7.00, 5.00)}   # borda de 50 mm cortada p/ 30 mm, curva → manual
FITA_PERD = 0.10

import os
# ⭐ LINHA DE FERRAGEM — duas versões [Jonathan, 04/11/2026]
#   silver: Bigfer Telescópica 500 mm R$ 15/par + Bigfer Slow Click R$ 4 · 2 anos
#   gold:   Hettich Quadro V6 oculta R$ 150/par + Hettich Sensys R$ 50 · 10 anos
LINHA = os.environ.get('LINHA', 'gold')
DOBR, CORR = {'silver': (4.0, 15.0), 'padrao': (10.0, 80.0),
              'gold': (50.0, 150.0)}[LINHA]
DOBR_NOME = {'silver': 'Bigfer Slow Click', 'padrao': 'Bigfer Inox Click',
             'gold': 'Hettich Sensys'}[LINHA]
CORR_NOME = {'silver': 'Bigfer Telescópica 500 mm', 'padrao': 'Hardt Invisível P-10',
             'gold': 'Hettich Quadro V6 oculta'}[LINHA]

pecas = []   # (movel, nome, c, l, qtd, chapa, fita_m_por_peca, tipo_fita)
def P(movel, nome, c, l, qtd, chapa, fita_m=0.0, tf='cor'):
    pecas.append(dict(movel=movel, nome=nome, c=c, l=l, qtd=qtd,
                      chapa=chapa, fita=fita_m, tf=tf))

def prat30(movel, nome, c, l, cor, borda_m, qtd=1):
    """Prateleira de 30 mm = duas chapas de 15 mm coladas. Fita de 50 mm só
    na borda vista (frente e pontas, inclusive o semicírculo)."""
    P(movel, nome + ' · camada sup.', c, l, qtd, cor + ' 15', borda_m, 'cor30')
    P(movel, nome + ' · camada inf.', c, l, qtd, cor + ' 15', 0)

def gaveta(movel, larg, prof, alt, n=1):
    li = larg - 3.6 - 3.0
    P(movel, 'Gaveta · lateral', prof, alt, 2*n, 'Branco TX 15', (prof+alt*0)/100, 'branco')
    P(movel, 'Gaveta · frente int./traseira', li, alt, 2*n, 'Branco TX 15', li/100, 'branco')
    P(movel, 'Gaveta · fundo', li+1, prof-1, n, 'Branco TX 6', 0)

outras = []  # (movel, item, qtd, un, R$ un, obs)
def O(movel, item, qtd, un, pu, obs=''):
    outras.append(dict(movel=movel, item=item, qtd=qtd, un=un, pu=pu, obs=obs))

# ═══ 1 · PRATELEIRAS 01 COZINHA (p.09) — tauari + mostrato, 30 mm, LED ═══
m = '1 Prateleiras 01 cozinha'
prat30(m, 'Prateleira superior 199 (tauari)', 199, 40, 'Tauari', (199+2*40+math.pi*9)/100)
prat30(m, 'Prateleira média 239 (mostrato)', 239, 40, 'Mostrato', (239+2*40+math.pi*9)/100)
prat30(m, 'Prateleira inferior 86 (mostrato)', 86, 40, 'Mostrato', (86+40+math.pi*9)/100)
prat30(m, 'Prateleira inferior 92 (mostrato)', 92, 40, 'Mostrato', (92+40)/100)
O(m, 'LED COB conjunto (fita, perfil, usinagem, instalação)', 6.16, 'm', 150)
O(m, 'Suporte oculto de prateleira (40 em 40 cm)', 16, 'un', 30)
O(m, 'Alma de aço barra chata 5 mm (peça > 1,20 m)', 2, 'barra', 50)
O(m, 'Metalon preto 2×2 — estrutura pronta', 3.4, 'm', 180, '3 montantes × ~1,13 m')

# ═══ 2 · PRATELEIRA JANTAR (p.09) — tauari 30 mm, LED ═══
m = '2 Prateleira jantar'
prat30(m, 'Prateleira 189 × 40', 189, 40, 'Tauari', (189+40+math.pi*9)/100)
prat30(m, 'Prateleira 176 × 25', 176, 25, 'Tauari', (176+25+math.pi*9)/100)
O(m, 'LED COB conjunto', 3.65, 'm', 150)
O(m, 'Suporte oculto de prateleira', 10, 'un', 30)
O(m, 'Alma de aço barra chata 5 mm', 2, 'barra', 50)
O(m, 'Metalon preto 2×2 — estrutura pronta', 1.05, 'm', 180, '3 peças × ~35 cm')

# ═══ 3 · ARMÁRIO INFERIOR 01 COZINHA (p.10) — azul secreto, interno branco ═══
m = '3 Armário inferior 01'
P(m, 'Lateral esquerda (vista)', 70, 63, 1, 'Azul Secreto 15', (70+63)/100)
P(m, 'Lateral direita + face chanfrada', 70, 40, 2, 'Azul Secreto 15', (70+40)/100)
P(m, 'Base', 214, 60, 1, 'Branco TX 15', 2.14, 'branco')
P(m, 'Travessa superior', 214, 10, 2, 'Branco TX 15', 2.14, 'branco')
P(m, 'Divisória', 68, 60, 3, 'Branco TX 15', 0.68, 'branco')
P(m, 'Fundo', 214, 70, 1, 'Branco TX 6')
P(m, 'Prateleira (módulo 55)', 52, 55, 1, 'Branco TX 15', 0.52, 'branco')
P(m, 'Nicho do forno · base e topo', 67, 58, 2, 'Branco TX 15', 0.67, 'branco')
P(m, 'Porta de giro 27,5 × 70', 70, 27.5, 2, 'Azul Secreto 18', 1.95)
P(m, 'Frente de gaveta 58 × 17', 58, 17, 4, 'Azul Secreto 18', 1.50)
P(m, 'Frente de gavetão tempero 25 × 35', 35, 25, 2, 'Azul Secreto 18', 1.20)
gaveta(m, 58, 50, 12, n=4)
gaveta(m, 25, 45, 28, n=2)
prat30(m, 'Prateleira semicírculo r=40 (ponta)', 80, 43, 'Azul Secreto', math.pi*40/100, qtd=2)
O(m, 'Dobradiça c/ amortecimento', 4, 'un', DOBR, DOBR_NOME)
O(m, 'Corrediça', 6, 'par', CORR, CORR_NOME)
O(m, 'Cava 45° usinada', 8, 'frente', 50)
O(m, 'Suporte de prateleira (jogo de 4)', 1, 'prat.', 6.5)

# ═══ 4 · ARMÁRIO INFERIOR 02 COZINHA (p.11) — azul, vão de lava-louças ═══
m = '4 Armário inferior 02'
P(m, 'Lateral direita chanfrada (vista)', 70, 63, 1, 'Azul Secreto 15', (70+63)/100)
P(m, 'Lateral do vão da lava-louças', 70, 63, 1, 'Azul Secreto 15', 0.70)
P(m, 'Divisória lava-louças | armário', 66, 60, 1, 'Branco TX 15', 0.66, 'branco')
P(m, 'Base', 60, 60, 1, 'Branco TX 15', 0.60, 'branco')
P(m, 'Travessa superior', 116, 10, 2, 'Branco TX 15', 1.16, 'branco')
P(m, 'Fundo', 60, 66, 1, 'Branco TX 6')
P(m, 'Prateleira 15 mm', 57, 55, 1, 'Branco TX 15', 0.57, 'branco')
P(m, 'Porta de giro 30 × 66', 66, 30, 2, 'Azul Secreto 18', 1.92)
O(m, 'Dobradiça c/ amortecimento', 4, 'un', DOBR, DOBR_NOME)
O(m, 'Cava 45° usinada', 2, 'frente', 50)
O(m, 'Suporte de prateleira (jogo de 4)', 1, 'prat.', 6.5)

# ═══ 5 · ARMÁRIO SUPERIOR MAIOR (p.12) — azul, 4 portas ═══
m = '5 Armário superior maior'
P(m, 'Lateral', 41, 40, 2, 'Azul Secreto 15', 0.81)
P(m, 'Base e teto', 196, 40, 2, 'Branco TX 15', 1.96, 'branco')
P(m, 'Divisória', 38, 38, 1, 'Branco TX 15', 0.38, 'branco')
P(m, 'Fundo', 196, 41, 1, 'Branco TX 6')
P(m, 'Porta de giro 48 × 39', 48, 39, 4, 'Azul Secreto 18', 1.74)
O(m, 'Dobradiça c/ amortecimento', 8, 'un', DOBR, DOBR_NOME)
O(m, 'Cava 45° usinada (puxador inferior)', 4, 'frente', 50)

# ═══ 6 · ARMÁRIO SUPERIOR MENOR (p.12) — tauari, 2 basculantes, LED ═══
m = '6 Armário superior menor'
P(m, 'Lateral', 35, 30, 2, 'Tauari 15', 0.65)
P(m, 'Base (vista por baixo)', 116, 30, 1, 'Tauari 15', 1.46)
P(m, 'Teto', 116, 30, 1, 'Branco TX 15', 1.16, 'branco')
P(m, 'Divisória', 32, 28, 1, 'Branco TX 15', 0.32, 'branco')
P(m, 'Prateleira', 56, 28, 2, 'Branco TX 15', 0.56, 'branco')
P(m, 'Fundo', 116, 35, 1, 'Branco TX 6')
P(m, 'Porta basculante 58 × 34', 58, 34, 2, 'Tauari 18', 1.84)
O(m, 'Articulador Blum AVENTOS HK-XS', 2, 'un', 250)
O(m, 'Perfil puxador passante', 1.19, 'm', 100, 'SP7000 · ⚠ confirmar perfil de 1 cm')
O(m, 'LED COB conjunto (inferior frontal)', 1.19, 'm', 150)
O(m, 'Suporte de prateleira (jogo de 4)', 2, 'prat.', 6.5)

# ═══ 7 · PRATELEIRA 02 COZINHA (p.11) — tauari 30 mm sobre os superiores ═══
m = '7 Prateleira 02 cozinha'
prat30(m, 'Prateleira de acabamento 199 × 65', 199, 65, 'Tauari', (199+65+65+12)/100)
O(m, 'LED COB conjunto', 1.92, 'm', 150)
O(m, 'Alma de aço barra chata 5 mm', 1, 'barra', 50)

# ═══ 8 · ARMÁRIO VERTICAL SERVIÇO + PRATELEIRA (p.13) ═══
m = '8 Armário vertical serviço'
P(m, 'Lateral (vista)', 232, 30, 2, 'Azul Secreto 15', 2*2.32/2+0.30)
P(m, 'Base, teto e travessa do gavetão', 62, 30, 3, 'Branco TX 15', 0.62, 'branco')
P(m, 'Divisória vertical', 143, 28, 1, 'Branco TX 15', 1.43, 'branco')
P(m, 'Prateleira coluna estreita', 26, 28, 5, 'Branco TX 15', 0.26, 'branco')
P(m, 'Prateleira superior inteira', 62, 28, 1, 'Branco TX 15', 0.62, 'branco')
P(m, 'Porta de giro 31 × 179', 179, 31, 2, 'Azul Secreto 18', 4.20)
gaveta(m, 63, 26, 40, n=1)
P(m, 'Gavetão · quadro da frente ripada', 63, 6, 2, 'Tauari 18', 0.63)
P(m, 'Gavetão · ripa 3 cm vazada (×1,10 perda)', 47, 3*1.10, 16, 'Tauari 18', 1.00)
prat30(m, 'Prateleira 273 × 32 sobre armário e janela', 273, 32, 'Tauari', (273+32+32)/100)
O(m, 'Dobradiça c/ amortecimento (porta 179 → 4)', 8, 'un', DOBR, DOBR_NOME)
O(m, 'Corrediça', 1, 'par', CORR, CORR_NOME)
O(m, 'Cava redonda ø7 usinada', 2, 'frente', 50, '⚠ preço de cava 45°, confirmar')
O(m, 'Suporte de prateleira (jogo de 4)', 6, 'prat.', 6.5)
O(m, 'Suporte oculto (trecho sobre a janela)', 5, 'un', 30)
O(m, 'Alma de aço barra chata 5 mm', 1, 'barra', 50)
O(m, 'LED COB conjunto', 2.73, 'm', 150)
O(m, 'Perfil de proteção de piso', 0.68, 'm', 15)

# ═══ 9 · PRATELEIRAS 02 SERVIÇO (p.13) — trio 30 mm, tauari + mostrato ═══
m = '9 Prateleiras serviço'
prat30(m, 'Prateleira superior (tauari)', 101, 30, 'Tauari', (78+37+math.pi*15)/100)
prat30(m, 'Prateleira (mostrato)', 101, 30, 'Mostrato', (78+37+math.pi*15)/100, qtd=2)
O(m, 'Suporte oculto de prateleira', 9, 'un', 30)
O(m, 'Metalon preto 2×2 — estrutura pronta', 2.56, 'm', 180, '2 montantes × 1,28 m')

# ═══ 10 · ARMÁRIO INFERIOR SERVIÇO (p.14) — tauari suspenso ═══
m = '10 Armário inferior serviço'
P(m, 'Lateral (vista)', 60, 48, 2, 'Tauari 15', 1.08)
P(m, 'Base (suspenso, vista por baixo)', 77, 48, 1, 'Tauari 15', 0.77+0.96)
P(m, 'Travessa superior', 77, 10, 2, 'Branco TX 15', 0.77, 'branco')
P(m, 'Divisória painel fixo | porta', 56, 46, 1, 'Branco TX 15', 0.56, 'branco')
P(m, 'Prateleira 15 mm', 46, 45, 1, 'Branco TX 15', 0.46, 'branco')
P(m, 'Painel frontal fixo', 60, 28, 1, 'Tauari 18', 1.76)
P(m, 'Porta de giro 49 × 56', 56, 49, 1, 'Tauari 18', 2.10)
O(m, 'Dobradiça 165° c/ amortecimento', 2, 'un', 50, '⚠ sem linha na Base — usei R$ 50')
O(m, 'Cava 45° usinada', 1, 'frente', 50)
O(m, 'Suporte de prateleira (jogo de 4)', 1, 'prat.', 6.5)

# ═══════════════════════════ CÁLCULO ═══════════════════════════
area = {}
fita = {}
npecas = 0
for p in pecas:
    a = p['c']*p['l']/1e4*p['qtd']
    area[p['chapa']] = area.get(p['chapa'], 0) + a
    tf = p['tf'] if p['tf'] != 'cor' or 'Branco' not in p['chapa'] else 'branco'
    fita[tf] = fita.get(tf, 0) + p['fita']*p['qtd']
    npecas += p['qtd']

chapas = {k: max(1, math.ceil(v/(CHAPA_M2*APROV))) for k, v in area.items()}
c_chapa = sum(chapas[k]*CHAPA[k] for k in chapas)
c_fita = sum(m_*(1+FITA_PERD)*FITA[t][0] + m_*FITA[t][1] for t, m_ in fita.items())
c_outras = sum(o['qtd']*o['pu'] for o in outras)
c_corte = sum(chapas.values())*2.00 + npecas*2.50
c_consum = 0.06*(c_chapa + c_fita)
FRETE = 400.0   # compra de material + entrega na obra · 2 × R$ 200
sem_emb = c_chapa + c_fita + c_outras + c_corte + c_consum + FRETE
c_emb = sem_emb*0.02/0.98
CD = sem_emb + c_emb

def brl(v): return f'R$ {v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')

if __name__ == '__main__':
    print('CHAPAS')
    for k in sorted(area):
        print(f'  {k:18s} {area[k]:6.2f} m²  → {chapas[k]} chapa(s) × {brl(CHAPA[k])} = {brl(chapas[k]*CHAPA[k])}')
    print('FITA (m de aresta):', {k: round(v, 1) for k, v in fita.items()})
    print('PEÇAS:', npecas)
    print()
    for lab, v in [('Chapas MDF', c_chapa), ('Fita + filetagem', c_fita),
                   ('Ferragem, LED, serralheria', c_outras), ('Corte', c_corte),
                   ('Consumíveis 6%', c_consum), ('Frete', FRETE),
                   ('Embalagem 2%', c_emb), ('CUSTO DIRETO', CD)]:
        print(f'  {lab:28s} {brl(v):>14s}')
    print()
    print('Ferragem/serviços por móvel:')
    mv = {}
    for o in outras: mv[o['movel']] = mv.get(o['movel'], 0) + o['qtd']*o['pu']
    for k, v in mv.items(): print(f'  {k:30s} {brl(v)}')
    print()
    for rt, vend, lab in [(True, False, 'com RT 10%, sem vendedor'),
                          (False, False, 'sem RT e sem vendedor')]:
        print(f'PREÇO à vista · {lab} · BASE {M.base(0, rt, vend)*100:.2f}%')
        for mc in (0.35, 0.38, 0.40):
            print(f'   MC {mc*100:.0f}% → {brl(M.preco(CD, mc, 0, rt, vend))}')
