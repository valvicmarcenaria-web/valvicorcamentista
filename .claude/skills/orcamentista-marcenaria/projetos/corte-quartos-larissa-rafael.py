# -*- coding: utf-8 -*-
"""
QUARTOS MATEUS E MANUELA — Larissa e Rafael  [A Urbanística · Paloma · out-dez/2025]
Alameda do Ipê Amarelo 107, São Luiz, BH · proprietário Rafael Augusto R. de Carvalho

Dois quartos infantis, executivo COMPLETO e cotado (39 pranchas). Tudo lido das
pranchas — nada estimado, salvo o que está marcado [PREMISSA].

CORES
  Mateus  · MDF Duratex Carvalho Hanover (CAR) + Azul Astral (AZU)
  Manuela · MDF Guararapes Rosa Milkshake (ROS) + Bilbao (BIL)
  Ambos entram como melamínico fosco na cor (base: 15mm R$500 · 6mm R$300 · 18mm R$600).

[PREMISSA 1] Nicho Cama do Mateus: as pranchas desenham TODAS as peças com 5 cm de
espessura. Modelado como caixa oca — 2 faces de 15 mm por peça + fita de 50 mm nas
bordas aparentes. É a construção real para essa espessura; confirmar com a arquiteta
se ela aceita 3 cm (2×15 colados), o que baixaria bastante.
[PREMISSA 2] Profundidades onde a prancha não cota: roupeiro 55 (cotado na lateral),
guarda-roupa Manuela 55, rack/escrivaninha 50, cabeceiras 10.
[Jonathan 31/07] Cabeceira estofada e espelhos são NOSSOS, entram no preço:
  · cabeceira estofada do Mateus — 11 módulos de 20×90 = 1,98 m² a R$ 750/m²
  · espelho oval iluminado da Manuela — 140×47 = 0,66 m². O R$ 750/m² foi dado logo
    depois de "cabeceira é nossa", então vale para o ESTOFADO; o espelho fica na base
    (prata R$ 600/m²) + vidraceiro pelo corte oval. Corrigir se for 750 nos dois.

FORA DO ESCOPO (memorial da arquiteta, mas não é marcenaria): tinta, gesso, papel de
parede, spots/plafon/pendente, tapete, cadeira, cortina, mapa-múndi decorativo.
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = CH_C*CH_L/10000
# cores: CAR/AZU no Mateus · ROS/BIL na Manuela. Cores NÃO dividem chapa.
PRECO_ESP = {'15': 500.0, '6': 300.0, '18': 600.0}   # base dados/materiais.json
def P_(m): return PRECO_ESP[m[3:]]
COR_DO_QUARTO = {'MATEUS': ('CAR','AZU'), 'MANUELA': ('ROS','BIL')}
FITA, FILET, FILET_MAN = 3.0, 2.5, 4.0
FITA_50 = 7.0                     # fita de 50 mm p/ peças de 5 cm — [PREMISSA]
DESP_FITA = 1.15
LED_M = 150.0
P_DOBR   = 10.0                   # Hettich Novisys
P_CORR   = 70.0                   # corrediça oculta Hardt (par)
P_CAVA   = 50.0                   # cava usinada, por peça
P_PUX_ML = 0.0                    # puxador em MDF = a própria chapa, já contada
P_PISTAO = 30.0                   # pistão c/ amortecimento (porta basculante)
P_CABID  = 45.0                   # cabideiro por metro
ESTOFADO_M2 = 750.0               # [Jonathan] linho cinza claro, aplicado
ESPELHO_M2  = 600.0               # base: espelho prata
VIDRACEIRO  = 200.0               # corte oval + furação p/ o perfil de LED

# ═══════════════════════════════ nesting (mesmo motor dos outros projetos)
def nest(items):
    if not items: return 0
    pcs = sorted(([max(c,l), min(c,l)] for c,l in items), key=lambda p: -p[1])
    chapas = 0; y = x = faixa = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: chapas += 1; continue
        if x + c > CH_C: y += faixa; x = 0.0; faixa = 0.0
        if y + l > CH_L: chapas += 1; y = x = faixa = 0.0
        x += c; faixa = max(faixa, l)
    chapas += 1
    area = sum(c*l for c,l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

# ═══════════════════════════════ peças: (móvel, desc, material, c, l, qtd)
pecas = []
def a(mv, d, m, c, l, q=1): pecas.append((mv, d, m, c, l, q))

# ─────────────────────────────── MATEUS
M1 = 'M1. Roupeiro 290×266'
# corpo: 2 laterais, 4 divisórias, base, tampo, fundo, sóculo
a(M1,'laterais',            'CAR15', 266, 55, 2)
a(M1,'divisórias verticais','CAR15', 250, 55, 4)
a(M1,'base e tampo',        'CAR15', 286, 55, 2)
a(M1,'fundo',               'CAR6',  286, 250, 1)
a(M1,'sóculo',              'CAR15', 286, 10.5, 1)
# módulo 18: 5 prateleiras · 78,67 (×2): 2 prat + cabideiro · 79,67: 6 nichos · 23: 3 prat
a(M1,'prateleiras mód. 18', 'CAR15', 18, 55, 5)
a(M1,'prateleiras mód. 78', 'CAR18', 78.67, 55, 4)      # >70cm → 18mm anti-empeno
a(M1,'prateleiras mód. 79', 'CAR18', 79.67, 55, 5)
a(M1,'divisória central 79','CAR15', 130, 55, 1)        # separa os nichos de 38,83
a(M1,'prateleiras mód. 23', 'CAR15', 23, 55, 3)
# 4 gavetas (mód. 78 esq.) — caixa de 6 peças + frente
a(M1,'gaveta laterais',     'CAR15', 50, 18, 8)
a(M1,'gaveta frente/costas','CAR15', 74, 18, 8)
a(M1,'gaveta fundo',        'CAR6',  74, 50, 4)
a(M1,'gaveta frentes',      'CAR15', 78.67, 20, 4)
# 4 sapateiras basculantes (mód. 79)
a(M1,'sapateira frentes',   'CAR15', 79.67, 18.5, 4)
a(M1,'sapateira fundos',    'CAR6',  79.67, 30, 4)
# portas ripadas: 6 de 40,83 + 2 de 25/20 · ripas de 2 cm a cada 2 cm
a(M1,'portas — base',       'AZU15', 40.83, 251, 6)
n_rip_M1 = int(290/4)                                    # ripas de 2 + vão de 2
a(M1,'portas — ripas 2 cm', 'CAR15', 251, 2, n_rip_M1)

M2 = 'M2. Móvel TV 275×263'
a(M2,'painel de fundo',     'AZU15', 275, 188, 1)       # base do ripado + azul
n_rip_M2 = int(120/4)
a(M2,'painel — ripas 2 cm', 'CAR15', 188, 2, n_rip_M2)
a(M2,'prateleiras 155',     'CAR18', 155, 20, 2)
a(M2,'prateleira 255',      'CAR18', 255, 20, 1)
a(M2,'base — laterais',     'CAR15', 65, 30, 2)
a(M2,'base — divisórias',   'CAR15', 65, 30, 5)
a(M2,'base — base e tampo', 'CAR15', 271, 30, 2)
a(M2,'base — fundo',        'CAR6',  271, 65, 1)
a(M2,'base — sóculo',       'CAR15', 271, 10, 1)
a(M2,'base — portas 48',    'CAR15', 48, 65, 2)
a(M2,'base — portas 38,75', 'CAR15', 38.75, 65, 4)

M3 = 'M3. Nicho Cama 218×166'
# [PREMISSA 1] peças de 5 cm = caixa oca, 2 faces de 15 mm cada
a(M3,'contorno (2 faces)',  'AZU15', 218, 25, 4)        # topo + base, 2 faces cada
a(M3,'laterais (2 faces)',  'AZU15', 166, 25, 4)
a(M3,'prat. horizontais',   'AZU15', 208, 25, 4)        # 2 níveis × 2 faces
a(M3,'divisórias verticais','AZU15', 47, 25, 12)        # 6 divisórias × 2 faces
a(M3,'fundo',               'AZU6',  218, 166, 1)

M4 = 'M4. Painel + porta mimetizada'
a(M4,'painel',              'CAR15', 264, 122, 1)
n_rip_M4 = int(68/4)                                     # faixa ripada de 68 cm
a(M4,'painel — ripas 2 cm', 'CAR15', 264, 2, n_rip_M4)
a(M4,'porta mimetizada',    'CAR18', 210, 54, 1)

M5 = 'M5. Cabeceira 218×100'
a(M5,'moldura MDF',         'CAR15', 218, 10, 2)
a(M5,'laterais da moldura', 'CAR15', 100, 10, 2)
a(M5,'painel de apoio',     'CAR15', 218, 100, 1)

M6 = 'M6. Mesinha de cabeceira'
a(M6,'laterais',            'CAR15', 45, 40, 2)
a(M6,'base e tampo',        'CAR15', 41, 40, 2)
a(M6,'fundo',               'CAR6',  41, 45, 1)
a(M6,'gaveta laterais',     'CAR15', 35, 15, 4)
a(M6,'gaveta frente/costas','CAR15', 37, 15, 4)
a(M6,'gaveta fundo',        'CAR6',  37, 35, 2)
a(M6,'gaveta frentes',      'CAR15', 41, 18.5, 2)
n_rip_M6 = int(41/4)
a(M6,'ripado — ripas 2 cm', 'AZU15', 37, 2, n_rip_M6)

M7 = 'M7. Rebaixamento MDF 394×100'
a(M7,'pano do forro',       'CAR15', 394, 100, 1)
a(M7,'saia perimetral',     'CAR15', 394, 10, 2)

# ─────────────────────────────── MANUELA
N1 = 'N1. Guarda-roupa 295×267'
a(N1,'laterais',            'ROS15', 267, 55, 2)
a(N1,'divisórias verticais','ROS15', 250, 55, 4)
a(N1,'base e tampo',        'ROS15', 291, 55, 2)
a(N1,'fundo',               'ROS6',  291, 250, 1)
a(N1,'sóculo',              'ROS15', 291, 7, 1)
a(N1,'prateleiras',         'ROS18', 50.5, 55, 10)
a(N1,'prateleiras longas',  'ROS18', 102, 55, 4)
a(N1,'gaveta laterais',     'ROS15', 50, 18, 14)        # 7 gavetas
a(N1,'gaveta frente/costas','ROS15', 46, 18, 14)
a(N1,'gaveta fundo',        'ROS6',  46, 50, 7)
a(N1,'gaveta frentes',      'ROS15', 50.5, 20, 7)
a(N1,'sapateira frentes',   'ROS15', 50.5, 18, 4)
a(N1,'portas de abrir',     'ROS18', 52.5, 210, 4)
a(N1,'porta basculante',    'ROS18', 220, 85, 1)
a(N1,'puxadores Bilbao',    'BIL15', 52.5, 5, 4)

N2 = 'N2. Cabeceira + painel'
a(N2,'painel de fundo',     'BIL15', 300, 100, 1)
a(N2,'painel 1 — moldura',  'BIL15', 135, 100, 1)
a(N2,'painel 2 — moldura',  'BIL15', 110, 100, 1)
a(N2,'painel 3 — moldura',  'BIL15', 75, 100, 1)
a(N2,'molduras salientes',  'BIL15', 100, 10, 12)       # bordas salientes dos 3 painéis

N3 = 'N3. Mesinha de cabeceira'
a(N3,'laterais',            'ROS15', 50, 40, 2)
a(N3,'base e tampo',        'BIL15', 46, 40, 2)
a(N3,'fundo',               'ROS6',  46, 50, 1)
a(N3,'gaveta laterais',     'ROS15', 36, 15, 4)
a(N3,'gaveta frente/costas','ROS15', 42, 15, 4)
a(N3,'gaveta fundo',        'ROS6',  42, 36, 2)
a(N3,'gaveta frentes',      'ROS15', 46, 17, 2)
n_rip_N3 = int(46/4)
a(N3,'ripado — ripas 2 cm', 'ROS15', 38, 2, n_rip_N3)

N4 = 'N4. Escrivaninha + rack 290'
a(N4,'painel de fundo',     'ROS15', 290, 192, 1)
a(N4,'tampo escrivaninha',  'ROS18', 190, 50, 1)
a(N4,'engrossamento tampo', 'ROS15', 190, 8, 1)
a(N4,'laterais de apoio',   'ROS15', 75, 50, 2)
a(N4,'nichos — prateleiras','BIL15', 138, 26, 3)
a(N4,'nichos — divisórias', 'BIL15', 39, 26, 4)
a(N4,'rack — laterais',     'ROS15', 75, 50, 2)
a(N4,'rack — base e tampo', 'ROS15', 186, 50, 2)
a(N4,'rack — divisórias',   'ROS15', 68, 50, 1)
a(N4,'rack — fundo',        'ROS6',  186, 75, 1)
a(N4,'rack — portas',       'BIL15', 47.5, 68, 4)
a(N4,'rack — sapateiras',   'ROS15', 92, 20, 3)

# ═══════════════════════════════ agrupa e nesta (por quarto — cores não se misturam)
QUARTOS = {'MATEUS': [M1,M2,M3,M4,M5,M6,M7], 'MANUELA': [N1,N2,N3,N4]}
QUARTO_DO_MOVEL = {mv: q for q, movs in QUARTOS.items() for mv in movs}
por_q_mat = defaultdict(list)          # (quarto, material) -> peças  → nesting REAL
area_mv   = defaultdict(float)         # (móvel, material)  -> m²     → rateio da chapa
area_q    = defaultdict(float)
for mv, d, m, c, l, q in pecas:
    qt = QUARTO_DO_MOVEL[mv]
    for _ in range(q):
        por_q_mat[(qt, m)].append((c, l))
        area_mv[(mv, m)] += c*l/10000
        area_q[(qt, m)]  += c*l/10000
CHAPAS_Q = {k: nest(v) for k, v in por_q_mat.items()}

# ═══════════════════════════════ fita, por móvel
def perim(mv, frac=0.5):
    return sum(q*2*(c+l)/100 for m,d,mat,c,l,q in pecas if m == mv)*frac

RIPAS = {M1: n_rip_M1, M2: n_rip_M2, M4: n_rip_M4, M6: n_rip_M6, N3: n_rip_N3}
def fita_do_movel(mv):
    """fita normal (22mm) + fita de ripado (manual) + fita de 50mm do nicho cama."""
    normal = perim(mv, 0.5)
    rip = sum(q*(c*2 + l)/100 for m,d,mat,c,l,q in pecas
              if m == mv and 'ripas 2 cm' in d)
    normal -= sum(q*2*(c+l)/100 for m,d,mat,c,l,q in pecas
                  if m == mv and 'ripas 2 cm' in d)*0.5
    larga = 0.0
    if mv == M3:                                  # peças de 5 cm → fita de 50 mm
        larga = perim(mv, 0.5)*0.5; normal -= larga
    return max(normal, 0.0), rip, larga

# ═══════════════════════════════ ferragens e LED, por móvel
FERR = {
    M1: 8*2*P_DOBR + 4*P_CORR + 4*P_PISTAO + 2*0.79*P_CABID,   # 8 portas, 4 gav, 4 sap
    M2: 6*2*P_DOBR + 6*P_CAVA,
    M3: 0.0,
    M4: 3*P_DOBR,                                              # porta mimetizada
    M5: 0.0, M6: 2*P_CORR + 2*P_CAVA, M7: 0.0,
    N1: 4*2*P_DOBR + 2*P_PISTAO + 7*P_CORR + 3*1.02*P_CABID,
    N2: 0.0, N3: 2*P_CORR + 2*P_CAVA,
    N4: 4*2*P_DOBR + 2*P_CORR + 4*P_CAVA,
}
# itens especiais que não são chapa: entram direto no custo do móvel
ESPEC = {
    M5: 11*0.20*0.90*ESTOFADO_M2,                       # cabeceira estofada, 1,98 m²
    N4: (1.40*0.47)*ESPELHO_M2 + VIDRACEIRO,            # espelho oval 140×47 iluminado
}
LED = {M1: 2.50, M2: 5.50, M3: 4.95, M4: 0.0, M5: 0.0, M6: 0.0, M7: 0.0,
       N1: 0.0, N2: 3.15 + 2.75, N3: 0.0, N4: 2.34 + 2.34 + 0.90}

# ═══════════════════════════════ custo por móvel
def custo_movel(mv):
    """chapa rateada: o quarto inteiro é nestado junto, por cor; cada móvel paga
    a fração de chapa correspondente à área que consumiu."""
    qt = QUARTO_DO_MOVEL[mv]
    mats = {m for (v, m) in area_mv if v == mv}
    chapas = {m: CHAPAS_Q[(qt, m)]*area_mv[(mv, m)]/area_q[(qt, m)] for m in mats}
    c_chapa = sum(chapas[m]*P_(m) for m in chapas)
    f_n, f_r, f_l = fita_do_movel(mv)
    c_fita  = (f_n*FITA + f_r*FITA + f_l*FITA_50)*DESP_FITA
    c_filet = f_n*FILET + f_r*FILET_MAN + f_l*FILET_MAN
    c_ferr  = FERR[mv] + LED[mv]*LED_M + ESPEC.get(mv, 0.0)
    return chapas, c_chapa, c_fita, c_filet, c_ferr, (f_n, f_r, f_l)

print('═'*104)
print('QUARTOS MATEUS E MANUELA — LEVANTAMENTO POR MÓVEL')
print('═'*104)
print(f'{"MÓVEL":<32}{"chapas (rateio)":>26}{"chapa R$":>11}{"fita":>10}{"filet":>9}{"ferr+LED":>11}{"CUSTO":>11}')
print('─'*104)
tot = defaultdict(float); tot_chapas = defaultdict(int)
for q, movs in QUARTOS.items():
    print(f'  ▸ {q}')
    sub = 0.0
    for mv in movs:
        ch, cc, cf, cfl, cfe, fs = custo_movel(mv)
        c = cc + cf + cfl + cfe; sub += c
        for m, n in ch.items(): tot_chapas[m] += n
        desc = ' '.join(f'{m}×{n:.1f}' for m, n in sorted(ch.items()))
        print(f'    {mv:<30}{desc:>26}{cc:>11,.0f}{cf:>10,.0f}{cfl:>9,.0f}{cfe:>11,.0f}{c:>11,.0f}')
    tot[q] = sub
    print(f'    {"subtotal " + q:<30}{"":>26}{"":>11}{"":>10}{"":>9}{"":>11}{sub:>11,.0f}')
print('─'*104)
MAT = sum(tot.values())
consum = MAT*0.06
print(f'{"MATERIAL + FERRAGENS + LED":<85}{MAT:>11,.2f}')
print(f'{"Consumíveis (6%)":<85}{consum:>11,.2f}')
LOGISTICA, VISITA, INSTALACAO = 900.0, 400.0, 1200.0
print(f'{"Logística · visita · instalação":<85}{LOGISTICA+VISITA+INSTALACAO:>11,.2f}')
fixedR = MAT + consum + LOGISTICA + VISITA + INSTALACAO
print(f'{"CUSTO DIRETO":<85}{fixedR:>11,.2f}')
print('\n  PLANO DE CORTE — nesting por quarto e por cor (cores não dividem chapa):')
tot_ch = 0
for (qt, m), n in sorted(CHAPAS_Q.items()):
    ap = area_q[(qt, m)]/(n*CH_AREA)*100
    tot_ch += n
    print(f'    {qt:<9}{m:<8}{area_q[(qt,m)]:>7.2f} m²  →  {n:>2} chapa(s)   aproveitamento {ap:>3.0f}%')
print(f'    {"TOTAL":<17}{sum(area_q.values()):>7.2f} m²  →  {tot_ch:>2} chapas'
      f'   aproveitamento médio {sum(area_q.values())/(tot_ch*CH_AREA)*100:.0f}%')

a_, liqF_, b_ = 0.162, 0.88, 0.043
print('\n' + '═'*100)
print('PREÇO')
print('═'*104)
for MC in (0.37, 0.40):
    div = 1 - a_ - liqF_*b_ - MC
    inv = fixedR/div
    r = round(inv/100)*100
    print(f'  MC {MC*100:.0f}%   tabela R$ {r:>10,.0f}   ·   à vista (−10%) R$ {round(r*0.9/100)*100:>10,.0f}')

print('\n  Rateio por quarto (proporcional ao material):')
for q in QUARTOS:
    div = 1 - a_ - liqF_*b_ - 0.40
    parc = fixedR*tot[q]/MAT
    print(f'    {q:<10} custo R$ {parc:>9,.0f}   ·   tabela R$ {round(parc/div/100)*100:>9,.0f}'
          f'   ·   à vista R$ {round(parc/div*0.9/100)*100:>9,.0f}')

print('\n  Itens especiais JÁ DENTRO do número:')
print(f'     · Mateus  — cabeceira estofada linho cinza · 1,98 m² × R$ 750  = R$ {ESPEC[M5]:>8,.2f}')
print(f'     · Manuela — espelho oval 140×47 iluminado + vidraceiro       = R$ {ESPEC[N4]:>8,.2f}')
