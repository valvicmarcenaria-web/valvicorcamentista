# -*- coding: utf-8 -*-
"""BRINQUEDOTECA · Eliza e Luiz Gustavo — ORÇAMENTO POR DECOMPOSIÇÃO FÍSICA

Estrutura de separação: por SISTEMA CONSTRUTIVO, não por ambiente — o espaço
é um só, e é o sistema que define quem fabrica, em que ordem e com que risco.

  1 ESTRUTURA E VEDAÇÃO      paredes cenográficas, casinha
  2 CIRCULAÇÃO EM ALTURA     passarela, laje do mezanino, plataformas, escadas
  3 PROTEÇÃO E CONTENÇÃO     gradil com corda, telas, rede de descanso, acrílico
  4 AMORTECIMENTO            piscina de espuma, acolchoamentos, zona de queda
  5 BRINQUEDOS               túnel, parede de escalada, escada horizontal, balanço
  6 MOBILIÁRIO               banco extenso, mesinha, painéis, prateleiras
  7 ACABAMENTOS              pintura automotiva, piso, LED
  8 ENGENHARIA               projeto estrutural e ART
  9 COZINHA DE BRINQUEDO     — precificada em separado, a pedido

★ = adoção sem cotação   ✓ = base da casa
"""
import math
from collections import defaultdict

# ══ INSUMOS ═══════════════════════════════════════════════════════════════
BARRA = 6.0
MET = {'50x30x1,2':(95.,1.44), '40x40x1,5':(122.,1.75),
       '60x40x2,0':(210.,2.93), '30x30x1,2':(62.,1.03)}
mL = lambda p: MET[p][0]/BARRA

MO_SERR, MO_SERR_EST = 24.0, 32.4      # ★ R$/m de perfil · estrutural +35%
CONSUM_S, CHUMB, CHUMB_EST = 0.07, 4.20, 9.24
PARAF_M2, SELAR_M2 = 4.90, 18.0
MDF_U18, MDF_U15 = 320.0, 260.0        # ★ MDF ultra premium cru
COMP_NAV18, COMP_NAV15 = 380.0, 330.0  # ★ compensado naval
CH_UTIL = 2.75*1.85*0.85
PINT_AUTO = 220.0                       # ★ R$/m² de superfície DESENVOLVIDA
VINILICO, LED_M = 120.0, 150.0

# ── ESPUMAS · especificação por aplicação (ver §ESPUMA no relatório) ──────
ESP = {                                  # ★ R$/m³ de placa
 'D20': 760.0,    # piscina de blocos — absorve, não sustenta
 'D23': 980.0,    # acolchoamento de parede, impacto lateral
 'D28': 1180.0,   # assento de uso intenso — banco
 'D33': 1420.0,   # piso de plataforma e degrau — recebe pisada
}
COURVIN, COSTURA = 58.0, 95.0           # ★ R$/m²
BLOCO_PIT = 31.0                         # ★ bloco 20×20×20 D20 revestido, un
EVA_IMPACTO_M2 = 340.0                   # ★ placa certificada p/ zona de queda

# ── CORDAS · por metro linear ────────────────────────────────────────────
CORDA_PA16   = 22.0     # ★ poliamida 16 mm, sem alma
CORDA_COMB16 = 95.0     # ★ COMBINADA: alma de aço galv. + poliamida trançada
REDE_DESC_M2 = 700.0    # ★ rede de descanso, malha 4 cm, poliamida
CABO_PERIM_M = 46.0     # ★ cabo de aço 6 mm + esticador + grampo, por metro
TELA_M2      = 250.0    # ★ tela de proteção
ACRILICO_M2  = 480.0    # ★

ITENS = []
def it(sis, nome, dim, linhas, obs=''):
    t = sum(q*v for _, q, _, v in linhas)
    ITENS.append(dict(sis=sis, nome=nome, dim=dim, linhas=linhas, total=t, obs=obs))
    return t

def parede(nome, L, H, mont=0.60, trav=1.00, dupla=False):
    n_m = math.ceil(L/mont)+1; m_m = n_m*H
    n_t = math.ceil(H/trav)+1; m_t = n_t*L
    m_p = m_m+m_t; m2 = L*H*(2 if dupla else 1)
    n_ch = math.ceil(m2/CH_UTIL*10)/10
    return it('1 · Estrutura e vedação', nome, f'{L:.2f} × {H:.2f} m · {m2:.2f} m² de chapa', [
     (f'Metalon 50×30×1,2 — {n_m} montantes a cada {mont*100:.0f} cm', m_m,'m',mL('50x30x1,2')),
     (f'Metalon 50×30×1,2 — {n_t} travessas',                           m_t,'m',mL('50x30x1,2')),
     ('Mão de obra de serralheria',                                     m_p,'m',MO_SERR),
     ('Consumível de solda e primer',              m_p*mL('50x30x1,2'),'vb',CONSUM_S),
     ('Chumbador',                                             (n_m+n_t)*2,'un',CHUMB),
     (f'MDF ultra premium 18 mm — {n_ch:.1f} chapas',                 n_ch,'ch',MDF_U18),
     ('Parafuso chapa/metalon',                                         m2,'m²',PARAF_M2),
     ('Selagem e lixa — preparo p/ pintura do cliente',                 m2,'m²',SELAR_M2),
    ], obs=f'{m_p:.1f} m de metalon')

# ══ 1 · ESTRUTURA E VEDAÇÃO ══════════════════════════════════════════════
parede('Parede norte (fundo, tijolinho)',      8.165, 2.80)
parede('Parede sul (banco e painéis)',         5.530, 2.55)
parede('Parede leste (escalada e poço)',       4.125, 3.10)
parede('Parede oeste (acesso)',                4.125, 2.55)
parede('Casinha — fachada e laterais',         2.850, 2.85, mont=0.50, dupla=True)

it('1 · Estrutura e vedação', 'Janelas com frisos decorativos', '4 conjuntos', [
 ('MDF ultra 15 mm — folhas, marco e peitoril',              1.6,'ch',MDF_U15),
 ('Metalon 30×30×1,2 — reforço de marco',                   14.0,'m',mL('30x30x1,2')),
 ('Friso decorativo usinado — 4 janelas × 6,2 m',           24.8,'m',18.0),
 ('Veneziana fixa usinada (ripa a ripa)',                    4.4,'m²',260.0),
 ('Mão de obra de marcenaria cenográfica',                  28.0,'h',65.0),
 ('Selagem e lixa',                                          8.8,'m²',SELAR_M2),
], obs='janela cenográfica é usinagem, não módulo — a hora manda no custo')

it('1 · Estrutura e vedação', 'Porta fake, molduras e floreira', 'PR05/07/08', [
 ('MDF ultra 18 mm',                                         1.2,'ch',MDF_U18),
 ('Moldura e almofada usinadas',                            16.0,'m',22.0),
 ('Mão de obra de marcenaria cenográfica',                  14.0,'h',65.0),
 ('Letreiro e toldo da fachada (lona e estrutura)',          1.0,'vb',980.0),
])

it('1 · Estrutura e vedação', 'Nicho profundo e nicho raso', '2 un, portas de giro', [
 ('MDF ultra 15 mm',                                         0.9,'ch',MDF_U15),
 ('Dobradiça Hettich Novisys',                               8.0,'un',10.0),
 ('Mão de obra',                                             9.0,'h',65.0),
])

# ══ 2 · CIRCULAÇÃO EM ALTURA ═════════════════════════════════════════════
Lp, Bp = 5.53, 0.60
n_tr = math.ceil(Lp/0.50)+1
m_pass = 2*Lp + n_tr*Bp + 4*0.85
it('2 · Circulação em altura', 'Passarela estruturada', f'{Lp:.2f} × {Bp:.2f} m, a +2,85 m', [
 ('Metalon 60×40×2,0 — 2 longarinas',                     2*Lp,'m',mL('60x40x2,0')),
 (f'Metalon 40×40×1,5 — {n_tr} travessas',            n_tr*Bp,'m',mL('40x40x1,5')),
 ('Metalon 60×40×2,0 — 4 mãos-francesas',               4*0.85,'m',mL('60x40x2,0')),
 ('Mão de obra de serralheria estrutural',              m_pass,'m',MO_SERR_EST),
 ('Consumível de solda',              m_pass*mL('60x40x2,0'),'vb',CONSUM_S),
 ('Chumbador estrutural 1/2"',                             16.0,'un',CHUMB_EST),
 ('Compensado naval 18 mm — piso',                          1.0,'ch',COMP_NAV18),
], obs=f'{m_pass:.1f} m de metalon · vão livre ~2,7 m — DIMENSIONAR')

A_LAJE = 3.97 + 4.5
m_laje = A_LAJE/0.5 + 2*(3.0+1.44)
it('2 · Circulação em altura', 'Laje do mezanino', f'{A_LAJE:.2f} m²', [
 ('Metalon 60×40×2,0 — vigas e barroteamento',           m_laje,'m',mL('60x40x2,0')),
 ('Mão de obra de serralheria estrutural',               m_laje,'m',MO_SERR_EST),
 ('Consumível de solda',              m_laje*mL('60x40x2,0'),'vb',CONSUM_S),
 ('Chumbador estrutural 1/2"',                             22.0,'un',CHUMB_EST),
 ('Compensado naval 18 mm',                                 2.0,'ch',COMP_NAV18),
 ('MDF ultra 15 mm — forro por baixo',                      2.0,'ch',MDF_U15),
])

Lpl, Bpl, Hpl = 0.95, 0.60, 0.57
m_pl = 2*(Lpl+Bpl) + 4*Hpl + 2*Bpl
it('2 · Circulação em altura', 'Plataformas acolchoadas', '5 unidades, de +0,57 a +2,85', [
 ('Metalon 40×40×1,5 — quadro, pés e travamento',      5*m_pl,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                        5*m_pl,'m',MO_SERR),
 ('Consumível de solda',           5*m_pl*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado naval 15 mm — base do tampo',              1.25,'ch',COMP_NAV15),
 ('Espuma D33 de 4 cm — recebe pisada',      5*Lpl*Bpl*0.04,'m³',ESP['D33']),
 ('Courvin náutico',                          5*Lpl*Bpl*2.1,'m²',COURVIN),
 ('Corte, costura e grampeamento',            5*Lpl*Bpl*2.1,'m²',COSTURA),
 ('Chumbador',                                           20.0,'un',CHUMB),
], obs=f'{5*m_pl:.1f} m de metalon no conjunto')

m_esc = 2*(2.6*2 + 4*0.9)
it('2 · Circulação em altura', 'Escadas e rampa com forração', '2 lances', [
 ('Metalon 40×40×1,5 — banzos e degraus',                m_esc,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          m_esc,'m',MO_SERR),
 ('Consumível de solda',              m_esc*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado naval 15 mm — piso dos degraus',            1.4,'ch',COMP_NAV15),
 ('Espuma D33 de 3 cm — degrau (não pode afundar)', 7.3*0.03,'m³',ESP['D33']),
 ('Courvin náutico',                                  7.3*1.6,'m²',COURVIN),
 ('Corte, costura e grampeamento',                    7.3*1.6,'m²',COSTURA),
 ('Chumbador',                                           12.0,'un',CHUMB),
])

# ══ 3 · PROTEÇÃO E CONTENÇÃO ═════════════════════════════════════════════
# ⭐ CORDAS POR METRO LINEAR — o que o Jonathan pediu para abrir
L_GRADIL, H_GRADIL = 9.13, 1.10
PASSO = 0.12                                   # fio horizontal a cada 12 cm
n_fios = math.ceil(H_GRADIL/PASSO)             # 10 fios
M_CORDA_GRADIL = n_fios*L_GRADIL               # 91,3 m
CORDA_ML = CORDA_COMB16                        # ver §CORDA no relatório
m_est_gr = 2*L_GRADIL + math.ceil(L_GRADIL/1.2+1)*H_GRADIL

it('3 · Proteção e contenção', 'Gradil de proteção com corda',
   f'{L_GRADIL:.2f} × {H_GRADIL:.2f} m · {n_fios} fios a cada {PASSO*100:.0f} cm', [
 ('Metalon 50×30×1,2 — quadro e montantes',            m_est_gr,'m',mL('50x30x1,2')),
 ('Mão de obra de serralheria',                        m_est_gr,'m',MO_SERR),
 ('Consumível de solda',             m_est_gr*mL('50x30x1,2'),'vb',CONSUM_S),
 (f'CORDA COMBINADA 16 mm (alma de aço) — {M_CORDA_GRADIL:.1f} m',
                                                 M_CORDA_GRADIL,'m',CORDA_ML),
 ('Terminal, prensa-cabo e olhal — 2 por fio',          n_fios*2,'un',26.0),
 ('Passagem e tensionamento (mão de obra)',       M_CORDA_GRADIL,'m',9.0),
 ('Chumbador',                                             14.0,'un',CHUMB),
], obs=f'⭐ corda: {M_CORDA_GRADIL:.1f} m × R$ {CORDA_ML:.2f}/m = '
       f'R$ {M_CORDA_GRADIL*CORDA_ML:,.2f}'.replace(',','.'))

A_REDE = 3.97
PERIM_REDE = 2*(3.00+1.438) + 1.174           # PR04
it('3 · Proteção e contenção', 'Rede de descanso do mezanino',
   f'{A_REDE:.2f} m² · perímetro {PERIM_REDE:.2f} m', [
 (f'Rede de poliamida malha 4 cm — {A_REDE:.2f} m²',     A_REDE,'m²',REDE_DESC_M2),
 (f'CABO DE AÇO 6 mm no perímetro — {PERIM_REDE:.2f} m', PERIM_REDE,'m',CABO_PERIM_M),
 ('Esticador, sapatilha e grampo',                         16.0,'un',34.0),
 ('Chumbador estrutural na alvenaria e na terça',          18.0,'un',CHUMB_EST),
 ('Instalação e tensionamento',                            10.0,'h',85.0),
], obs=f'⭐ perímetro: {PERIM_REDE:.2f} m × R$ {CABO_PERIM_M:.2f}/m = '
       f'R$ {PERIM_REDE*CABO_PERIM_M:,.2f}'.replace(',','.')
       + ' · ⛔ a fixação depende de avaliação estrutural no local')

it('3 · Proteção e contenção', 'Telas de proteção', '★ ~14 m²', [
 ('Tela de proteção',                                      14.0,'m²',TELA_M2),
 ('Metalon 30×30×1,2 — quadro',                            26.0,'m',mL('30x30x1,2')),
 ('Mão de obra de serralheria e instalação',               26.0,'m',MO_SERR),
])
it('3 · Proteção e contenção', 'Fechamento em acrílico', '★ ~2,2 m²', [
 ('Acrílico cristal 8 mm com usinagem',                     2.2,'m²',ACRILICO_M2),
 ('Perfil de fixação e instalação',                         6.4,'m',48.0),
])

# ══ 4 · AMORTECIMENTO ════════════════════════════════════════════════════
A_POCO, PROF_POCO = 2.535*2.425, 0.55
VOL_POCO = A_POCO*PROF_POCO
N_BLOCOS = math.ceil(VOL_POCO/(0.20**3)*0.62)   # 62% de ocupação (bloco solto)
it('4 · Amortecimento', 'Piscina de espuma',
   f'{A_POCO:.2f} m² × {PROF_POCO:.2f} m = {VOL_POCO:.2f} m³', [
 (f'Bloco 20×20×20 D20 revestido — {N_BLOCOS} un',    N_BLOCOS,'un',BLOCO_PIT),
 ('Fundo acolchoado D23 de 5 cm',               A_POCO*0.05,'m³',ESP['D23']),
 ('Courvin do fundo e das paredes do poço',        A_POCO*2.4,'m²',COURVIN),
 ('Corte e costura',                               A_POCO*2.4,'m²',COSTURA),
 ('Metalon 40×40×1,5 — contenção do poço',               21.0,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          21.0,'m',MO_SERR),
], obs=f'⭐ {N_BLOCOS} blocos a 62% de ocupação — bloco solto não preenche 100%')

it('4 · Amortecimento', 'Zona de queda sob passarela e plataformas',
   '★ 11,0 m² — NÃO está nas pranchas, ver RISCO 2', [
 ('Placa de impacto certificada 10 cm (queda de 2,85 m)',  11.0,'m²',EVA_IMPACTO_M2),
 ('Instalação e arremate',                                 11.0,'m²',45.0),
], obs='⛔ NBR 16071 — dimensionada pela ALTURA DE QUEDA, não por conforto')

it('4 · Amortecimento', 'Acolchoamento de parede em zona de impacto', '★ 12,0 m²', [
 ('Espuma D23 de 4 cm',                              12.0*0.04,'m³',ESP['D23']),
 ('Courvin náutico',                                   12.0*1.3,'m²',COURVIN),
 ('Corte, costura e fixação',                          12.0*1.3,'m²',COSTURA),
 ('Compensado 15 mm — base de fixação',                     2.8,'ch',COMP_NAV15),
])

# ══ 5 · BRINQUEDOS ═══════════════════════════════════════════════════════
L_TUN, B_TUN, H_TUN = 3.60, 0.60, 1.40
n_arco = math.ceil(L_TUN/0.40)+1
it('5 · Brinquedos', 'Túnel escorregador com cobertura em arco',
   f'{L_TUN:.2f} m · vão {B_TUN:.2f} × {H_TUN:.2f} m interno', [
 (f'MDF ultra 15 mm — {n_arco} arcos usinados',              2.6,'ch',MDF_U15),
 ('Compensado flexível 6 mm — casca do arco',                3.4,'ch',290.0),
 ('Compensado naval 15 mm — piso do escorregador',           1.2,'ch',COMP_NAV15),
 ('Metalon 40×40×1,5 — estrutura de apoio',                 16.0,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                             16.0,'m',MO_SERR),
 ('Mão de obra de marcenaria — gabarito e curvatura',       34.0,'h',65.0),
 ('Laminado de alta pressão na pista (deslizamento)',        2.4,'m²',185.0),
 ('Selagem e lixa',                                          9.0,'m²',SELAR_M2),
], obs='curvatura sobre gabarito é hora, não chapa — 34 h mandam no custo')

A_ESC = 2.425*2.45
it('5 · Brinquedos', 'Parede de escalada', f'{A_ESC:.2f} m²', [
 ('Compensado naval 18 mm — painel estrutural',              1.6,'ch',COMP_NAV18),
 ('Metalon 50×30×1,2 — estrutura de trás',                  26.0,'m',mL('50x30x1,2')),
 ('Mão de obra de serralheria',                             26.0,'m',MO_SERR),
 ('Insertos T-nut M10 — 1 a cada 20 cm',                   150.0,'un',1.90),
 ('Agarra de escalada infantil',                            40.0,'un',38.0),
 ('Chumbador',                                              18.0,'un',CHUMB),
 ('Selagem e pintura de base',                              A_ESC,'m²',SELAR_M2),
])

it('5 · Brinquedos', 'Escada horizontal (monkey bars)', '2,9 m de vão', [
 ('Tubo 1.1/2" ch.14 — travessões e banzos',                14.0,'m',22.0),
 ('Mão de obra de serralheria estrutural',                  14.0,'m',MO_SERR_EST),
 ('Chumbador estrutural',                                    8.0,'un',CHUMB_EST),
])
it('5 · Brinquedos', 'Balanço sob viga', 'PR03', [
 ('Assento de balanço infantil com corrente',                1.0,'un',480.0),
 ('Mão-francesa e fixação em metalon 60×40',                 3.2,'m',mL('60x40x2,0')),
 ('Mão de obra e chumbador estrutural',                      6.0,'un',CHUMB_EST),
 ('Mosquetão e manilha galvanizados',                        4.0,'un',38.0),
])

# ══ 6 · MOBILIÁRIO ═══════════════════════════════════════════════════════
L_BANCO, B_BANCO = 5.53, 0.50
m_banco = 2*L_BANCO + math.ceil(L_BANCO/0.8+1)*B_BANCO + 8*0.38
it('6 · Mobiliário', 'Banco extenso', f'{L_BANCO:.2f} × {B_BANCO:.2f} m', [
 ('Metalon 40×40×1,5 — quadro, pés e travamento',        m_banco,'m',mL('40x40x1,5')),
 ('Mão de obra de serralheria',                          m_banco,'m',MO_SERR),
 ('Consumível de solda',            m_banco*mL('40x40x1,5'),'vb',CONSUM_S),
 ('Compensado naval 18 mm — base do assento',                1.0,'ch',COMP_NAV18),
 ('Espuma D28 de 5 cm — assento de uso intenso',
                                        L_BANCO*B_BANCO*0.05,'m³',ESP['D28']),
 ('Courvin náutico',                     L_BANCO*B_BANCO*1.9,'m²',COURVIN),
 ('Corte, costura e grampeamento',       L_BANCO*B_BANCO*1.9,'m²',COSTURA),
 ('Chumbador',                                              14.0,'un',CHUMB),
])
it('6 · Mobiliário', 'Mesinha e 4 banquinhos', 'PR03', [
 ('MDF ultra 18 mm',                                         1.4,'ch',MDF_U18),
 ('Metalon 30×30×1,2 — pés',                                12.0,'m',mL('30x30x1,2')),
 ('Mão de obra de serralheria e marcenaria',                14.0,'h',65.0),
 ('Selagem e lixa',                                          4.2,'m²',SELAR_M2),
])
it('6 · Mobiliário', 'Painel imantado', '1,93 × 1,20 m', [
 ('Chapa galvanizada 0,9 mm (base imantada)',                2.3,'m²',148.0),
 ('MDF ultra 15 mm — moldura e fundo',                       0.8,'ch',MDF_U15),
 ('Mão de obra e fixação',                                   8.0,'h',65.0),
])
it('6 · Mobiliário', 'Painel com bobina de papel e organizadores', '0,60 de prof.', [
 ('MDF ultra 18 mm',                                         1.8,'ch',MDF_U18),
 ('Suporte e eixo da bobina',                                1.0,'vb',320.0),
 ('Organizadores e caixas',                                  6.0,'un',72.0),
 ('Mão de obra de marcenaria',                              12.0,'h',65.0),
 ('Selagem e lixa',                                          6.0,'m²',SELAR_M2),
])
it('6 · Mobiliário', 'Prateleiras, degraus e nichos em MDF', 'PR05 vista A', [
 ('MDF ultra 18 mm',                                         2.2,'ch',MDF_U18),
 ('Metalon 30×30×1,2 — mão-francesa embutida',              18.0,'m',mL('30x30x1,2')),
 ('Mão de obra',                                            16.0,'h',65.0),
 ('Selagem e lixa',                                          7.4,'m²',SELAR_M2),
])

# ══ 7 · ACABAMENTOS ══════════════════════════════════════════════════════
# superfície DESENVOLVIDA da serralheria aparente (≈2,6× a área em planta)
M2_PINT = (Lp*Bp*2.6) + (L_GRADIL*H_GRADIL*1.5) + (5*Lpl*Bpl*1.4) \
        + (2*2.6*1.4) + (A_LAJE*0.8) + 3.2
it('7 · Acabamentos', 'Pintura automotiva da serralheria aparente',
   f'★ {M2_PINT:.1f} m² de superfície DESENVOLVIDA', [
 ('Preparo, primer, base e verniz em cabine',            M2_PINT,'m²',PINT_AUTO),
 ('Transporte fábrica ↔ pintura (2 viagens)',                2.0,'un',420.0),
], obs='⛔ superfície desenvolvida ≈ 2,6× a área em planta — o erro da 1ª versão')

it('7 · Acabamentos', 'Piso vinílico sobre laje e passarela', f'{A_LAJE+Lp*Bp:.2f} m²', [
 ('Piso vinílico em régua',                       A_LAJE+Lp*Bp,'m²',VINILICO),
 ('Manta e cola',                                 A_LAJE+Lp*Bp,'m²',26.0),
])
it('7 · Acabamentos', 'Tapete emborrachado', '★ ~12 m²', [
 ('Placa emborrachada 15 mm',                               12.0,'m²',180.0),
])
it('7 · Acabamentos', 'Iluminação LED', '★ ~14 m', [
 ('Fita LED COB com perfil',                                14.0,'m',LED_M),
 ('Driver e instalação',                                     4.0,'un',180.0),
])

# ══ 8 · ENGENHARIA ═══════════════════════════════════════════════════════
it('8 · Engenharia', 'Projeto estrutural e ART',
   'passarela, laje, plataformas, fixação da rede', [
 ('Cálculo estrutural e detalhamento',                       1.0,'vb',3200.0),
 ('ART do CREA',                                             1.0,'un',600.0),
], obs='⛔ NÃO É OPCIONAL — as pranchas devolvem o dimensionamento (RISCO 1)')

# ══ 9 · COZINHA DE BRINQUEDO — separada ══════════════════════════════════
COZ = []
def cz(d,q,u,v): COZ.append((d,q,u,v))
cz('MDF ultra 18 mm — corpo, bancada e frentes',              3.0,'ch',MDF_U18)
cz('MDF ultra 15 mm — internos e fundo',                      1.0,'ch',MDF_U15)
cz('Dobradiça Hettich Novisys',                              10.0,'un',10.0)
cz('Corrediça telescópica',                                   3.0,'par',40.0)
cz('Cooktop, torneira e pia lúdicos (acessórios)',            1.0,'vb',640.0)
cz('Puxador e botões',                                       14.0,'un',18.0)
cz('Mão de obra de marcenaria',                              18.0,'h',65.0)
cz('Selagem e lixa — preparo p/ pintura',                    11.0,'m²',SELAR_M2)

# ══ CONSOLIDAÇÃO ═════════════════════════════════════════════════════════
import motor_mc as M
CD_SIS = sum(i['total'] for i in ITENS)
CARRETO, DIARIA, VISITA = 150.0, 260.0, 275.0
LOG = 8*CARRETO + 22*DIARIA + 4*VISITA
CONSUM = CD_SIS*0.03
CD = (CD_SIS + LOG + CONSUM)*(1 + M.EMBALAGEM)
CD_COZ = sum(q*v for _,q,_,v in COZ)*(1 + M.EMBALAGEM)
BASE = M.base(parcelas=0, rt=False, vendedor=False)
MC = 0.42

if __name__ == '__main__':
    br  = lambda v: f'{v:,.2f}'.replace(',','§').replace('.',',').replace('§','.')
    br0 = lambda v: f'{v:,.0f}'.replace(',','.')
    W = 96
    print('═'*W); print('BRINQUEDOTECA · Eliza e Luiz Gustavo — ORÇAMENTO POR DECOMPOSIÇÃO')
    print('═'*W)
    por = defaultdict(float)
    for i in ITENS: por[i['sis']] += i['total']
    for sis in dict.fromkeys(i['sis'] for i in ITENS):
        print(f'\n{"═"*W}\n{sis.upper():<70}{br0(por[sis]):>14}{por[sis]/CD_SIS*100:>8.1f}%')
        for i in ITENS:
            if i['sis'] != sis: continue
            print(f'\n  ▸ {i["nome"]}   ·   {i["dim"]}')
            if i['obs']: print(f'    {i["obs"]}')
            for d,q,u,v in i['linhas']:
                print(f'      {d:<54}{q:>8.2f} {u:<4} × {br(v):>8} = {br(q*v):>10}')
            print(f'      {"":<54}{"":>8} {"":<4}   {"":>8}   {br(i["total"]):>10}')
    print(f'\n{"═"*W}')
    print(f'  {"Soma dos sistemas":<70}{br0(CD_SIS):>14}')
    print(f'  {"+ logística, 22 dias de equipe e 4 visitas":<70}{br0(LOG):>14}')
    print(f'  {"+ consumíveis de fábrica (3%)":<70}{br0(CONSUM):>14}')
    print(f'  {"+ embalagem (2%)":<70}{br0(CD-(CD_SIS+LOG+CONSUM)):>14}')
    print(f'  {"CUSTO DIRETO":<70}{br0(CD):>14}')
    p  = round(CD/(BASE-MC)/100)*100
    pc = round(CD_COZ/(BASE-MC)/100)*100
    print(f'\n  BASE {BASE*100:.2f}% · MC {MC:.0%}')
    print(f'  {"BRINQUEDOTECA":<70}{br0(p):>14}')
    print(f'  {"COZINHA DE BRINQUEDO (custo "+br0(CD_COZ)+")":<70}{br0(pc):>14}')
    print(f'  {"TOTAL":<70}{br0(p+pc):>14}')
    print(f'\n  ⭐ CORDAS, por metro linear')
    print(f'     gradil de proteção  {M_CORDA_GRADIL:>6.1f} m × R$ {br(CORDA_ML):>7}'
          f' = {br0(M_CORDA_GRADIL*CORDA_ML):>8}   (corda combinada, alma de aço)')
    print(f'     perímetro da rede   {PERIM_REDE:>6.1f} m × R$ {br(CABO_PERIM_M):>7}'
          f' = {br0(PERIM_REDE*CABO_PERIM_M):>8}   (cabo de aço 6 mm + esticador)')
    print(f'     alternativa poliamida simples: {M_CORDA_GRADIL:.1f} m × R$ {br(CORDA_PA16)}'
          f' = {br0(M_CORDA_GRADIL*CORDA_PA16)}  — economia de '
          f'{br0(M_CORDA_GRADIL*(CORDA_ML-CORDA_PA16))}, ver §CORDA')
