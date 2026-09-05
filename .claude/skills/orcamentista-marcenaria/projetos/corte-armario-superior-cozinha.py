# -*- coding: utf-8 -*-
"""ARMÁRIO SUPERIOR DE COZINHA — levantamento e preço.

Fontes: render do projeto + foto da parede real com medição de 3,02 m.

Premissas do Jonathan [07/08/2026]:
  · interno BRANCO · externo COR
  · linha BÁSICA (Hardt)
  · puxadores PASSANTES (perfil embutido em usinagem passante)
  · custo do LED apresentado SEPARADO

Profundidades dadas: o armário mais alto (plano de cima, que corre inteiro e
passa por cima da geladeira) = 50 cm · o mais estreito (plano de trabalho,
sobre a bancada) = 35 cm.

GEOMETRIA LIDA (⚠ estimada do render sobre a largura medida de 3,02 m)
  Parede 302 · geladeira 72 à direita · trecho sobre a bancada 230
  Pé-direito 260 · bancada 90 · fundo do aéreo inferior 150

  PLANO 50 cm  ─ 210 a 260 (50 alt) sobre a bancada .......... 230 × 50 × 50
                 190 a 260 (70 alt) sobre a geladeira ........  72 × 70 × 50
  PLANO 35 cm  ─ 150 a 210 (60 alt) sobre a bancada .......... 230 × 60 × 35
                   B cristaleira 72 · C coifa 83 · D micro 75
"""
from collections import defaultdict

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75 * 1.85                      # 5,0875 m²

# ── base de custos (referencias/validacao-orcamento.md) ─────────────────────
BRC6, BRC15, BRC18 = 190.0, 250.0, 290.0
COR18              = 580.0
FITA_BRC, FITA_COR = 2.0, 3.0              # R$/m  (+10% desperdício)
FILET_MAQ          = 2.50                  # R$/m aplicado na coladeira

DOBR_HARDT   = 10.0    # un — linha básica
DOBR_VIDRO   = 30.0    # un — dobradiça especial p/ porta de alumínio+vidro
PISTAO_60N   = 35.0    # un — báscula do nicho do micro
SUP_PRAT     = 1.50    # un
PERFIL_PUX   = 48.0    # R$/m — perfil puxador passante (linha SP7000)
USIN_PUX     = 25.0    # R$/m — usinagem passante na CNC
PORTA_VIDRO  = 280.0   # folha 36×60 c/ perfil de alumínio ⚠ CONFIRMAR c/ vidraceiro

LED_ML   = 130.0   # R$/m — fita + perfil com difusor (base real da planilha)
LED_FONTE = 80.0   # un
LED_SENSOR = 50.0  # un

PRECO = {'BRC6': BRC6, 'BRC15': BRC15, 'BRC18': BRC18, 'COR18': COR18}

# ── peças  (material, descrição, comprimento, largura, qtd) ─────────────────
pecas = [
    # ── PLANO 50 — aéreo superior sobre a bancada (230 × 50 alt × 50 prof) ──
    ('BRC15', 'Superior — vertical (esq. + 2 divisórias)',   50,  50, 3),
    ('BRC15', 'Superior — tampo',                           230,  50, 1),
    ('BRC15', 'Superior — base',                            230,  50, 1),
    ('BRC18', 'Superior — prateleira (vão 69)',              69,  48, 1),
    ('BRC18', 'Superior — prateleira (vão 80)',              80,  48, 1),
    ('BRC18', 'Superior — prateleira (vão 72)',              72,  48, 1),
    ('BRC6',  'Superior — fundo',                           230,  50, 1),
    ('COR18', 'Superior — porta (sobre a cristaleira)',      36,  50, 2),
    ('COR18', 'Superior — porta (sobre a coifa)',          41.5,  50, 2),
    ('COR18', 'Superior — porta (sobre o micro)',          37.5,  50, 2),
    ('COR18', 'Superior — tamponamento lateral esquerdo',    50,  50, 1),

    # ── PLANO 50 — módulo sobre a geladeira (72 × 70 alt × 50 prof) ─────────
    ('BRC15', 'Geladeira — vertical',                        70,  50, 2),
    ('BRC15', 'Geladeira — tampo',                           72,  50, 1),
    ('BRC15', 'Geladeira — base',                            72,  50, 1),
    ('BRC18', 'Geladeira — prateleira',                      69,  48, 1),
    ('BRC6',  'Geladeira — fundo',                           72,  70, 1),
    ('COR18', 'Geladeira — porta',                           36,  70, 2),

    # ── PLANO 35 — aéreo inferior sobre a bancada (230 × 60 alt × 35 prof) ──
    ('BRC15', 'Inferior — vertical',                         60,  35, 4),
    ('BRC15', 'Inferior — tampo corrido',                   230,  35, 1),
    ('BRC15', 'Inferior — base da cristaleira',              72,  35, 1),
    ('BRC15', 'Inferior — base do vão da coifa (recuo 15)',  83,  35, 1),
    ('BRC15', 'Inferior — base do nicho do micro',           75,  35, 1),
    ('BRC15', 'Inferior — divisória porta/nicho do micro',   75,  35, 1),
    ('BRC18', 'Cristaleira — prateleira',                    69,  33, 2),
    ('BRC18', 'Coifa — prateleira',                          80,  33, 1),
    ('BRC6',  'Inferior — fundo',                           230,  60, 1),
    ('COR18', 'Coifa — porta',                             41.5,  45, 2),
    ('COR18', 'Micro — porta basculante',                    75,  25, 1),
    ('COR18', 'Inferior — tamponamento lateral esquerdo',    60,  35, 1),
]

# ── fita: só as bordas que aparecem ────────────────────────────────────────
fitas = [
    ('COR', 'Portas do plano superior — perímetro',   2*(0.36+0.50)*2 + 2*(0.415+0.50)*2 + 2*(0.375+0.50)*2),
    ('COR', 'Portas da geladeira — perímetro',        2*(0.36+0.70)*2),
    ('COR', 'Portas da coifa — perímetro',            2*(0.415+0.45)*2),
    ('COR', 'Basculante do micro — perímetro',        2*(0.75+0.25)),
    ('COR', 'Tamponamentos — frente e base',          (0.50+0.50) + (0.60+0.35)),
    ('BRC', 'Verticais — canto frontal',              3*0.50 + 2*0.70 + 4*0.60),
    ('BRC', 'Tampo e base do superior — frente',      2*2.30),
    ('BRC', 'Tampo e bases do inferior — frente',     2.30 + 0.72 + 0.83 + 0.75 + 0.75),
    ('BRC', 'Tampo e base da geladeira — frente',     2*0.72),
    ('BRC', 'Prateleiras — frente',                   0.69 + 0.80 + 0.72 + 2*0.69 + 0.80 + 0.69),
    ('BRC', 'Nicho do micro — bordas internas',       2*0.35 + 2*0.75),
]

# ── nesting (função da casa, com varredura de ordens) ──────────────────────
# O empacotador por faixas é guloso: a ordem em que as peças entram decide o
# resultado. Ordenar só por largura decrescente colocou as 3 verticais de 50
# na primeira faixa e empurrou os tampos de 230 para outra chapa — 3 chapas
# para 7,18 m². Varrendo quatro ordens e ficando com a melhor, a mesma lista
# fecha em 2. Verificado à mão antes de aceitar.
def _pack(pcs):
    chapas = 0; y = x = faixa = 0.0
    for c, l in pcs:
        if c > CH_C and l <= CH_C: c, l = l, c
        if c > CH_C or l > CH_L: chapas += 1; continue
        if x + c > CH_C: y += faixa; x = 0.0; faixa = 0.0
        if y + l > CH_L: chapas += 1; y = x = faixa = 0.0
        x += c; faixa = max(faixa, l)
    return chapas + 1

def nest(items):
    if not items: return 0
    base = [(max(c, l), min(c, l)) for c, l in items]
    ordens = [lambda p: -p[1],                    # largura decrescente
              lambda p: (-p[1], -p[0]),           # largura, depois comprimento
              lambda p: -p[0],                    # comprimento decrescente
              lambda p: -p[0]*p[1]]               # área decrescente
    chapas = min(_pack(sorted(base, key=k)) for k in ordens)
    area = sum(c*l for c, l in items)/10000
    return max(chapas, -(-int(area/(CH_AREA*0.80)*1000)//1000) or 1)

por_mat, area_mat = defaultdict(list), defaultdict(float)
for mat, desc, c, l, q in pecas:
    for _ in range(q):
        por_mat[mat].append((c, l))
        area_mat[mat] += c*l/10000

CHAPAS = {m: nest(v) for m, v in por_mat.items()}

print('═'*94)
print('ARMÁRIO SUPERIOR DE COZINHA — 3,02 m · interno branco / externo cor · linha básica')
print('═'*94)
print('\nMÓDULOS')
for d in ('Plano 50 cm — aéreo superior sobre a bancada .......... 230 × 50 alt × 50 prof · 6 portas',
          'Plano 50 cm — módulo sobre a geladeira ................  72 × 70 alt × 50 prof · 2 portas',
          'Plano 35 cm — cristaleira (2 portas de vidro, 2 prat.)   72 × 60 alt × 35 prof',
          'Plano 35 cm — vão da coifa (2 portas, recuo de 15)       83 × 60 alt × 35 prof',
          'Plano 35 cm — nicho do micro (báscula + nicho aberto)    75 × 60 alt × 35 prof'):
    print('  ' + d)

print('\nPLANO DE CORTE  (nesting por cor × espessura — cores nunca dividem chapa)')
custo_chapa = 0.0
for m in sorted(CHAPAS):
    n = CHAPAS[m]; c = n*PRECO[m]; custo_chapa += c
    ap = area_mat[m]/(n*CH_AREA)*100
    print(f'  {m:<7}{area_mat[m]:>6.2f} m²  →  {n} chapa(s) × R$ {PRECO[m]:>6.2f}'
          f'  = R$ {c:>8,.2f}   aproveitamento {ap:>3.0f}%')
tot_ch = sum(CHAPAS.values())
print(f'  {"TOTAL":<7}{sum(area_mat.values()):>6.2f} m²  →  {tot_ch} chapas'
      f'                      R$ {custo_chapa:>8,.2f}   médio '
      f'{sum(area_mat.values())/(tot_ch*CH_AREA)*100:.0f}%')

print('\nFITA DE BORDA  (+10% de desperdício)')
m_cor = sum(m for t, _, m in fitas if t == 'COR')
m_brc = sum(m for t, _, m in fitas if t == 'BRC')
custo_fita = m_cor*1.10*FITA_COR + m_brc*1.10*FITA_BRC
custo_filet = (m_cor + m_brc)*FILET_MAQ
for t, d, m in fitas:
    print(f'  {d:<48}{m:>7.2f} m   fita {t}')
print(f'  {"— cor":<48}{m_cor:>7.2f} m × R$ {FITA_COR:.2f}')
print(f'  {"— branco":<48}{m_brc:>7.2f} m × R$ {FITA_BRC:.2f}')
print(f'  {"material da fita":<48}{m_cor+m_brc:>7.2f} m         R$ {custo_fita:>8,.2f}')
print(f'  {"filetagem na coladeira":<48}{m_cor+m_brc:>7.2f} m × R$ {FILET_MAQ:.2f}'
      f'  = R$ {custo_filet:>8,.2f}')

print('\nFERRAGENS  (linha básica — Hardt)')
# regra da casa: porta até 90 cm de altura = 2 dobradiças
N_DOBR   = 6*2 + 2*2 + 2*2 + 1*2          # superior + geladeira + coifa + basculante
N_DOBR_V = 2*2                            # 2 portas de vidro com perfil de alumínio
N_PRAT   = 3 + 1 + 2 + 1                  # superior + geladeira + cristaleira + coifa
M_PUX    = (0.36*2 + 0.415*2 + 0.375*2) + 0.36*2 + 0.415*2 + 0.75 + 0.72
M_PUX    = round(M_PUX*2)/2 + 0.5         # arredonda p/ cima em meio metro
ferr = [
    (f'Dobradiça Hardt com amortecimento — {N_DOBR} un',        N_DOBR*DOBR_HARDT),
    (f'Dobradiça especial p/ porta de alumínio — {N_DOBR_V} un', N_DOBR_V*DOBR_VIDRO),
    ('Pistão a gás 60N — báscula do micro, 2 un',                2*PISTAO_60N),
    (f'Suporte de prateleira — {N_PRAT*4} un',                   N_PRAT*4*SUP_PRAT),
    (f'Perfil puxador passante — {M_PUX:.1f} m',                 M_PUX*PERFIL_PUX),
    (f'Usinagem passante na CNC — {M_PUX:.1f} m',                M_PUX*USIN_PUX),
    ('Porta de vidro c/ perfil de alumínio 36×60 — 2 folhas ⚠',  2*PORTA_VIDRO),
]
custo_ferr = sum(v for _, v in ferr)
for d, v in ferr: print(f'  {d:<62}R$ {v:>8,.2f}')
print(f'  {"TOTAL":<62}R$ {custo_ferr:>8,.2f}')

# ── LED — apurado à parte, como o Jonathan pediu ───────────────────────────
LED_M = [('Sob o plano de 50 — banho no aéreo inferior', 2.30),
         ('Sob o plano de 35 — banho na bancada',        2.30),
         ('Interno da cristaleira — 2 prateleiras + topo', 3*0.70)]
m_led = sum(m for _, m in LED_M)
m_led_c = -(-m_led // 1)                                  # arredonda p/ metro cheio
custo_led = m_led_c*LED_ML + 2*LED_FONTE + LED_SENSOR
print('\nILUMINAÇÃO LED  (apurada à parte)')
for d, m in LED_M: print(f'  {d:<48}{m:>7.2f} m')
print(f'  {"fita + perfil com difusor":<48}{m_led_c:>7.0f} m × R$ {LED_ML:.2f}'
      f'  = R$ {m_led_c*LED_ML:>8,.2f}')
print(f'  {"fonte / driver — 2 un":<48}                R$ {2*LED_FONTE:>8,.2f}')
print(f'  {"sensor de acionamento — 1 un":<48}                R$ {LED_SENSOR:>8,.2f}')
print(f'  {"CUSTO DO LED":<48}                R$ {custo_led:>8,.2f}')

# ── fechamento de custo ────────────────────────────────────────────────────
consum = (custo_chapa + custo_fita)*0.06
MAT = custo_chapa + custo_fita + custo_filet + custo_ferr + consum
LOG, VIS, INST = 450.0, 250.0, 700.0        # 3 m de aéreo, montagem em altura, 2 pessoas
fixedR_marc = MAT + LOG + VIS + INST
fixedR_led  = custo_led

print('\n' + '─'*94)
print(f'  {"Chapas":<62}R$ {custo_chapa:>8,.2f}')
print(f'  {"Fita (material)":<62}R$ {custo_fita:>8,.2f}')
print(f'  {"Filetagem (aplicação)":<62}R$ {custo_filet:>8,.2f}')
print(f'  {"Ferragens, puxador passante e portas de vidro":<62}R$ {custo_ferr:>8,.2f}')
print(f'  {"Consumíveis (6% de chapa + fita)":<62}R$ {consum:>8,.2f}')
print(f'  {"Logística · visita · instalação":<62}R$ {LOG+VIS+INST:>8,.2f}')
print(f'  {"CUSTO DIRETO — MARCENARIA":<62}R$ {fixedR_marc:>8,.2f}')
print(f'  {"CUSTO DIRETO — LED (separado)":<62}R$ {fixedR_led:>8,.2f}')
print(f'  {"CUSTO DIRETO — TOTAL":<62}R$ {fixedR_marc+fixedR_led:>8,.2f}')

# ── preço ──────────────────────────────────────────────────────────────────
# a=0,162 · liqF=0,88 · b=0,043 — conjunto SEM RT. RT não está embutido.
a_, liqF_, b_, MC = 0.162, 0.88, 0.043, 0.35
div = 1 - a_ - liqF_*b_ - MC

inv_marc = fixedR_marc/div
inv_led  = fixedR_led/div
tab_marc = round(inv_marc/50)*50
tab_led  = round(inv_led/50)*50
tabela   = tab_marc + tab_led

print('\n' + '═'*94)
print(f'PREÇO — MC {MC*100:.0f}% · SEM RT · divisor {div:.5f}')
print('═'*94)
print(f'  Marcenaria      R$ {fixedR_marc:>8,.2f} ÷ {div:.5f} = R$ {inv_marc:>9,.2f}   →  R$ {tab_marc:>7,.0f}')
print(f'  Iluminação LED  R$ {fixedR_led:>8,.2f} ÷ {div:.5f} = R$ {inv_led:>9,.2f}   →  R$ {tab_led:>7,.0f}')
print(f'  {"TOTAL DE TABELA":<48}                     R$ {tabela:>7,.0f}')

print('\n  ESCADA DE PAGAMENTO (padrão da casa)')
escada = [('Entrada 30% + até 10× no cartão', 0.00),
          ('Entrada 50% + até 8× no cartão',  0.03),
          ('Entrada 70% + até 6× no cartão',  0.05),
          ('Entrada 70% + restante em transferência', 0.07)]
for d, desc in escada:
    v = round(tabela*(1-desc)/50)*50
    print(f'    {d:<46}{"—" if not desc else f"−{desc*100:.0f}%":>5}   R$ {v:>8,.0f}')

fixedR = fixedR_marc + fixedR_led
print(f'\n  MC conferida na tabela: {(tabela - tabela*(a_+liqF_*b_) - fixedR)/tabela*100:.1f}%')
print(f'  MC no piso da escada (−7%): '
      f'{(round(tabela*0.93/50)*50 - round(tabela*0.93/50)*50*(a_+liqF_*b_) - fixedR)/(round(tabela*0.93/50)*50)*100:.1f}%')

# ── sensibilidades que o Jonathan precisa ver ──────────────────────────────
print('\n' + '═'*94)
print('DECISÕES QUE MEXEM NO PREÇO')
print('═'*94)

# 1) nicho do micro na cor em vez de branco
area_nicho = (2*35*35 + 2*75*35)/10000        # laterais + base + topo do nicho, em cm²
delta_nicho = area_nicho*(COR18-BRC15)/CH_AREA
print(f'  1. Nicho do micro na COR em vez de branco (é nicho ABERTO, o interior aparece)')
print(f'     {area_nicho:.2f} m² de branco 15 → cor 18 = +R$ {delta_nicho:,.2f} de custo'
      f'  →  +R$ {round(delta_nicho/div/50)*50:,.0f} de venda')
print(f'     O render mostra o nicho na cor. A sua especificação diz interno branco.')

# 2) portas de vidro
print(f'\n  2. As 2 portas de vidro pesam R$ {2*PORTA_VIDRO:,.2f} no custo '
      f'({2*PORTA_VIDRO/fixedR_marc*100:.0f}% do custo da marcenaria)')
fixedR_sem_v = fixedR_marc - 2*PORTA_VIDRO - N_DOBR_V*DOBR_VIDRO + 2*2*DOBR_HARDT \
             + (0.36*0.60*2)*COR18/CH_AREA
print(f'     Trocando por 2 portas cegas na cor: R$ {fixedR_marc:,.2f} → R$ {fixedR_sem_v:,.2f}')
print(f'     Tabela R$ {tab_marc:,.0f} → R$ {round(fixedR_sem_v/div/50)*50:,.0f}'
      f'   (−R$ {tab_marc - round(fixedR_sem_v/div/50)*50:,.0f})')

# 3) LED
print(f'\n  3. LED separado: R$ {tab_led:,.0f} de venda sobre R$ {custo_led:,.2f} de custo.')
print(f'     São {m_led_c:.0f} m de fita + perfil com difusor + 2 fontes + sensor.')
print(f'     Sem o LED interno da cristaleira (−{3*0.70:.1f} m): custo R$ '
      f'{custo_led - 3*0.70*LED_ML:,.2f} → venda R$ '
      f'{round((custo_led - 3*0.70*LED_ML)/div/50)*50:,.0f}')

print('\n' + '─'*94)
print('⚠ A CONFIRMAR ANTES DE FECHAR')
print('  · Pé-direito (usei 2,60) e altura do fundo do aéreo (usei 1,50). Mudam altura de porta.')
print('  · Largura do vão da geladeira (usei 72) — o resto da parede é consequência.')
print('  · Preço da porta de vidro com perfil (usei R$ 280/folha) — cotar com o vidraceiro.')
print('  · Coifa, micro-ondas e pontos elétricos NÃO estão no escopo.')
