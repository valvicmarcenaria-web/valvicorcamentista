# -*- coding: utf-8 -*-
"""MARCELO TOLENTINO — BRZ Nova Lima  [29/09/2026]

Estande de Vendas (5 ambientes) + Apto Decorado Bosque Residence (6 ambientes).
Projeto Zilda Santiago e Anamaria Diniz. 54 pranchas, todas 1/25, em curvas.

⛔ ESCOPO NOVO. Nada do SPE Nova Lima 1 entra. O motor antigo
   (corte-spe-decorado.py) serve só de referência de custo unitário.

FERRAGEM DESTA VERSÃO [Jonathan 29/09]
  · Dobradiça  Hettich Novisys        R$ 10/un
  · Corrediça  Telescópica            R$ 40/par
  · Roupeiro   RO65 PRIME da Rometal  ★ SEM PREÇO NA BASE — ver FLAG 1

FLAGS
  1 ★ RO65 **Prime** não está em dados/materiais.json. A base só tem o RO65
    comum (R$ 60/porta + trilho 3mt R$ 80). O Prime é linha acima. Lancei
    R$ 120/porta + trilho R$ 160 (2× o comum) como PROVISÓRIO. Cotar.
  2 ★ Fecho toque (tip-on): base só tem Pulsador Blum R$ 100/un. Usado para
    todas as frentes "fecho toque" da cozinha e do aparador da sala de reunião.
  3 ★ Muxarabi do banheiro casal: usinagem fina (ripa 1,5 / vão 5). Sem
    referência na base — lancei como mão de obra de usinagem por m².
  4 Corrediça telescópica derruba a garantia para 2 anos (ferragens.md).
"""
from collections import defaultdict
import motor_mc as M

CH_C, CH_L = 275.0, 185.0
CH_AREA = 2.75*1.85

# ── chapa (dados/materiais.json) ──────────────────────────────────────────
BR6, BR15, BR18 = 190.0, 260.0, 330.0          # MDF Branco TX — interno
COR6, COR15, COR18 = 300.0, 500.0, 600.0       # MDF melamínico fosco — cor
FORM = 400.0                                    # fórmica (copa)
PRECO = {'BR6':BR6, 'BR15':BR15, 'BR18':BR18, 'FOR':FORM}
# cores do projeto: TA Tauari · CM Carvalho Munique · CP Cinza Pixel
#                   CE Cinza Essencial · CB Cerrado Bold
for c in ('TA','CM','CP','CE','CB'):
    PRECO[c+'6'], PRECO[c+'15'], PRECO[c+'18'] = COR6, COR15, COR18
NOME = {'BR6':'branco 6','BR15':'branco 15','BR18':'branco 18','FOR':'fórmica'}
for c, n in (('TA','Tauari'),('CM','Carv.Munique'),('CP','Cinza Pixel'),
             ('CE','Cinza Essenc.'),('CB','Cerrado Bold')):
    for e in ('6','15','18'): NOME[c+e] = f'{n} {e}'

FITA_BR, FITA_COR = 2.0, 3.0

# ── ferragens ─────────────────────────────────────────────────────────────
DOBR   = 10.0     # Hettich Novisys
CORR   = 40.0     # telescópica
TIPON  = 100.0    # ★ pulsador (fecho toque)
RO65P_PORTA, RO65P_TRILHO = 120.0, 160.0   # ★ RO65 Prime — PROVISÓRIO
SUP_PRAT = 1.50
CAVA_M = 50.0     # perfil cava usinado, por metro de frente

# ── terceiros ─────────────────────────────────────────────────────────────
LACA_M2      = 650.0
VIDRO_M2     = 300.0    # incolor temperado
VIDRO_CAN_M2 = 420.0    # ★ canelado — 40% acima do incolor
VIDRO_BRZ_M2 = 420.0    # ★ bronze   — 40% acima do incolor
ESPELHO_M2   = 600.0
ALUM_M       = 85.0     # ★ perfil de alumínio (bronze / preto fosco), por metro
ESTOFADO_M2  = 450.0
TUBO_ALU_M   = 60.0     # tubo 2×2 preto
LED_M        = 150.0    # LED COB fita + perfil
USIN_MUX_M2  = 380.0    # ★ usinagem do muxarabi

p, FER, TER = [], defaultdict(float), defaultdict(float)
def a(mov, mat, desc, c, l, q=1): p.append((mov, mat, desc, c, l, q))
def f(mov, v): FER[mov] += v
def t(mov, v): TER[mov] += v

# ══════════════════════════════════════════════════════════════════════════
# STAND
# ══════════════════════════════════════════════════════════════════════════

# ── COPA ──────────────────────────────────────────────────────────────────
K = 'Copa · armário inferior e ilha'
# armário sob a bancada existente: 260 × 60 × 73, gaveteiro 8 gav + portas
a(K,'BR15','Lateral/divisória',            73, 58, 6)
a(K,'BR15','Base e travessas',            258, 58, 2)
a(K,'BR6' ,'Fundo',                       258, 73, 1)
a(K,'FOR' ,'Frentes de gaveta (fórmica)',  60, 19, 8)
a(K,'FOR' ,'Portas (fórmica)',             73, 45, 2)
a(K,'BR15','Caixa de gaveta',              55, 18, 16)
a(K,'BR6' ,'Fundo de gaveta',              55, 45, 8)
f(K, 8*CORR + 4*DOBR)
# ilha: corpo 250 × 43 × 79 (tampo de pedra é da marmoraria)
a(K,'BR15','Ilha · lateral',               79, 43, 4)
a(K,'BR15','Ilha · base e travessa',      248, 43, 2)
a(K,'FOR' ,'Ilha · fechamento em fórmica', 79, 62, 4)
a(K,'BR15','Ilha · nicho do microondas',   55, 42, 3)

K = 'Copa · painel de parede'
# painel piso/teto MDF Tauari 260 × 210, com porta de abrir embutida
a(K,'TA18','Painel',                      210, 68, 4)
a(K,'BR15','Montante de fixação',         210, 10, 5)
a(K,'TA18','Porta embutida',              200, 80, 1)
f(K, 4*DOBR)
t(K, 2.0*CAVA_M)                          # puxador cava na porta

# ── SALA DE REUNIÃO ───────────────────────────────────────────────────────
K = 'Sala de reunião · aparador de cafeteira'
# 245 × 45 × 75 (corpo 63 + tampo 12), 5 portas de 49, fecho toque
a(K,'CB18','Tampo',                       245, 45, 1)
a(K,'CB18','Frente/porta',                 63, 49, 5)
a(K,'BR15','Lateral e divisória',          63, 43, 6)
a(K,'BR15','Base',                        243, 43, 1)
a(K,'BR15','Prateleira interna',          118, 41, 2)
a(K,'BR6' ,'Fundo',                       243, 63, 1)
a(K,'CB18','Lateral aparente / testeira',  75, 45, 2)
f(K, 10*DOBR + 5*TIPON + 2*SUP_PRAT)
t(K, 0.0)   # nicho em porcelanato é da obra

# ── SALA DE ATIVOS ────────────────────────────────────────────────────────
K = 'Sala de ativos · bancadas de trabalho'
# 13,2 m lineares, h=70, tampo 4 cm (duplado 18+18), prof ~60
for nome, ext, pr in (('norte',516,60), ('oeste',375,61), ('sul',432,60)):
    nch = -(-ext//250)                    # tampo emendado a cada ~2,5 m
    a(K,'CM18',f'Tampo {nome} (face)',     ext/nch, pr, nch)
    a(K,'BR18',f'Tampo {nome} (alma)',     ext/nch, pr, nch)
    a(K,'CM18',f'Saia frontal {nome}',     ext/nch, 12, nch)
    a(K,'BR18',f'Painel de apoio {nome}',   62, pr-6, max(2, int(ext//130)))
    a(K,'BR15',f'Canaleta de fiação {nome}',ext/nch, 14, nch*2)
f(K, 24*SUP_PRAT)

K = 'Sala de ativos · divisórias'
# 6 un · 120 alt × 60 prof × 3 esp (duplado 15+15 em Cinza Pixel)
a(K,'CP15','Divisória (face)',            120, 60, 12)
a(K,'CP15','Miolo',                       118, 58, 6)

K = 'Sala de ativos · aparador'
# 170 × 50 × 75 (70 + 5 de base), 4 portas de 42,5, 1 prateleira
a(K,'CM18','Tampo',                       170, 50, 1)
a(K,'CM18','Porta',                        63, 42, 4)
a(K,'BR15','Lateral e divisória',          65, 48, 5)
a(K,'BR15','Base e rodapé',               168, 48, 2)
a(K,'BR18','Prateleira interna',           83, 46, 2)
a(K,'BR6' ,'Fundo',                       168, 65, 1)
a(K,'CM18','Lateral aparente',             75, 50, 2)
f(K, 8*DOBR + 2*SUP_PRAT)

# ── LOUNGE ────────────────────────────────────────────────────────────────
K = 'Lounge · painel Carvalho Munique'
# ~17,4 m²: faixa de 80 sobre o granito (oeste e sul) + parede leste inteira
a(K,'CM18','Faixa oeste',                  80, 65, 6)   # 390 × 80
a(K,'CM18','Retorno oeste',               260, 30, 1)
a(K,'CM18','Retorno oeste estreito',      260,  7, 1)
a(K,'CM18','Faixa sul',                    80, 70, 4)   # 280 × 80
a(K,'CM18','Parede leste',                260, 61, 7)   # 427 × 260
a(K,'BR15','Montante de fixação',         260, 10, 12)

K = 'Lounge · painel Tauari com porta'
# 187,5 × 260, porta de abrir de 100 com puxador cava
a(K,'TA18','Painel',                      260, 44, 2)
a(K,'TA18','Porta',                       230, 100, 1)
a(K,'TA18','Bandeira sobre a porta',       30, 100, 1)
a(K,'BR15','Marco e montante',            260, 12, 4)
f(K, 4*DOBR)
t(K, 2.3*CAVA_M)

# ── BANCADA GOURMET ───────────────────────────────────────────────────────
K = 'Gourmet · painéis e forro Tauari'
# E01 97,5 × 262 · E02 557 × 262 (trecho a 385) · forro
a(K,'TA18','Painel E01',                  262, 49, 2)
a(K,'TA18','Painel E02',                  262, 64, 9)   # 557 × 262
a(K,'TA18','Trecho alto E02 (até 385)',   123, 64, 2)
a(K,'TA18','Forro liso',                  250, 62, 6)   # ~9,3 m² de forro
a(K,'BR15','Montante e sarrafo',          260, 10, 16)

K = 'Gourmet · armários da bancada'
# frente de 340 (2 frigobares + 4 portas) + trecho de 90 · h=73, prof 60
a(K,'TA18','Porta',                        73, 55, 4)
a(K,'TA18','Porta trecho E03',             73, 44, 2)
a(K,'BR15','Lateral e divisória',          73, 58, 8)
a(K,'BR15','Base e travessa',             250, 58, 3)
a(K,'BR6' ,'Fundo',                       250, 73, 2)
a(K,'BR15','Nicho dos frigobares',         73, 58, 3)
a(K,'TA18','Rodapé/zócalo aparente',      340,  5, 1)
f(K, 12*DOBR)

# ══════════════════════════════════════════════════════════════════════════
# APARTAMENTO DECORADO
# ══════════════════════════════════════════════════════════════════════════

# ── COZINHA + ÁREA DE SERVIÇO ─────────────────────────────────────────────
K = 'Cozinha · armários superiores'
# E01 217,5 (5×43,5 h=77) · E03 70 (2×35 h=77) · E03 73 (2×36,5 h=97)
# E02/E04 30 (h=77) · cabideiro 45+30 (h=55)
a(K,'TA18','Porta E01',                    77, 43, 5)
a(K,'TA18','Porta E03 (70)',               77, 35, 2)
a(K,'TA18','Porta E03 (73)',               97, 36, 2)
a(K,'TA18','Porta E02/E04',                77, 30, 1)
a(K,'TA18','Porta do cabideiro',           55, 45, 1)
a(K,'BR15','Lateral e divisória',          77, 33, 12)
a(K,'BR15','Base e tampo',                217, 33, 4)
a(K,'BR15','Lateral/base cabideiro',       55, 33, 4)
a(K,'BR6' ,'Fundo',                       217, 77, 2)
a(K,'BR18','Prateleira interna',          107, 31, 4)
a(K,'TA18','Testeira',                    340, 10, 1)
f(K, 22*DOBR + 11*TIPON + 4*SUP_PRAT)
t(K, 3.4*LED_M)                            # LED sob os suspensos

K = 'Cozinha · torre de eletros e vassoura'
# torre h=240 (micro + forno + lava-roupa) + vassoura 60 (2×30)
a(K,'TA18','Frente da torre',             100, 43, 2)
a(K,'TA18','Porta escamoteável MLR',      100, 43, 1)
a(K,'TA18','Porta de vassoura',           240, 30, 2)
a(K,'BR15','Lateral da torre',            240, 58, 3)
a(K,'BR15','Travessa e base',              85, 58, 6)
a(K,'BR15','Lateral do vassoureiro',      240, 58, 2)
a(K,'BR15','Prateleira do vassoureiro',    58, 56, 4)
a(K,'BR6' ,'Fundo',                       240, 87, 2)
f(K, 10*DOBR + 5*TIPON + 4*SUP_PRAT)

K = 'Cozinha · armário inferior em laca verde'
# E01 217,5 · 5 portas de 43,5 · h=91 · LACA FOSCA VERDE + puxador cava
a(K,'BR18','Frente para laca',             91, 43, 5)
a(K,'BR15','Lateral e divisória',          91, 58, 6)
a(K,'BR15','Base e travessa',             215, 58, 3)
a(K,'BR6' ,'Fundo',                       215, 91, 1)
f(K, 10*DOBR)
t(K, 5*0.91*0.435*2*LACA_M2)               # laca nas duas faces das 5 frentes
t(K, 2.2*CAVA_M)

K = 'Cozinha · armários inferiores Tauari'
# E03/E04 com puxador cava e sóculo em marcenaria h=10
a(K,'TA18','Porta',                        91, 43, 6)
a(K,'BR15','Lateral e divisória',          91, 58, 8)
a(K,'BR15','Base e travessa',             215, 58, 4)
a(K,'BR6' ,'Fundo',                       260, 91, 1)
a(K,'TA18','Sóculo em marcenaria',        280, 10, 1)
a(K,'TA18','Fundo e lateral da geladeira',240, 72, 2)
a(K,'TA18','Painel liso da sala',         250, 62, 2)
f(K, 12*DOBR)
t(K, 2.6*CAVA_M)

K = 'Cozinha · cristaleira'
# 60 de frente, piso/teto (250), porta em perfil de alumínio preto + vidro canelado
a(K,'TA18','Lateral e travessa',          250, 38, 2)
a(K,'BR18','Prateleira',                   58, 36, 5)
a(K,'BR6' ,'Fundo',                       250, 58, 1)
a(K,'TA18','Montante aparente',           250, 10, 2)
f(K, 2*TIPON + 5*SUP_PRAT)
t(K, 2*2.30*0.30*VIDRO_CAN_M2 + 2*5.2*ALUM_M)

K = 'Cozinha · divisória de correr em vidro'
# 2 folhas de correr + 1 fixo, vidro canelado, borda preto fosco alumínio 5cm
# ⚠ NÃO leva RO65: é esquadria de alumínio com trilho embutido, do serralheiro
t(K, 3*2.30*0.80*VIDRO_CAN_M2 + 3*6.2*ALUM_M + 900.0)

# ── SALA E VARANDA ────────────────────────────────────────────────────────
K = 'Sala · estante piso/teto'
# 486 na parede principal + retorno lateral · 250 de altura · prof 20
# malha: montantes de 2 a cada 42 · 7 níveis (base 26 + 6 × 35)
a(K,'TA18','Montante vertical',           250, 20, 13)
a(K,'TA18','Prateleira',                   42, 20, 72)
a(K,'TA18','Travessa de topo e base',     250, 20, 5)
a(K,'TA6' ,'Fundo',                       250, 62, 5)
a(K,'CM18','Nicho em Carvalho Munique',    35, 22, 24)
a(K,'CM18','Fundo do nicho',               35, 42, 8)
f(K, 80*SUP_PRAT)

K = 'Sala · mesa de jantar'
# 158 × 90 · h=75 · tampo com chanfro usinado (DET.01)
a(K,'TA18','Tampo (face)',                158, 90, 1)
a(K,'TA18','Tampo (alma)',                156, 88, 1)
a(K,'TA18','Base / pé central',            73, 45, 4)
a(K,'BR18','Estrutura da base',            73, 40, 4)
t(K, 5.0*CAVA_M)                           # chanfro usinado no perímetro

K = 'Sala · painel de TV'
# 331 (3 folhas de 110 com bite 0,5) × 250
a(K,'TA18','Folha do painel',             250, 55, 6)
a(K,'BR15','Montante de fixação',         250, 10, 6)

# ── QUARTO CASAL ──────────────────────────────────────────────────────────
K = 'Quarto casal · guarda-roupa'
# vão 193 · 2 portas de correr em VIDRO com perfil de alumínio bronze
# folhas 94,6 e 96,5 · h=234 · prof 60
a(K,'TA18','Lateral e divisória',         234, 58, 4)
a(K,'TA18','Base, tampo e maleiro',       191, 58, 3)
a(K,'BR18','Prateleira',                   93, 56, 6)
a(K,'BR15','Caixa de gaveta',              55, 18, 12)
a(K,'BR6' ,'Fundo de gaveta',              55, 52, 6)
a(K,'TA18','Frente de gaveta',             19, 92, 6)
a(K,'BR6' ,'Fundo',                       234, 96, 2)
f(K, 6*CORR + 2*RO65P_PORTA + RO65P_TRILHO + 8*SUP_PRAT)
t(K, 2*0.906*2.34*VIDRO_M2 + 2*6.6*ALUM_M)

K = 'Quarto casal · cabeceira estofada'
a(K,'BR18','Estrutura da cabeceira',      110, 75, 4)
a(K,'BR15','Travessa e fixação',          296, 10, 4)
t(K, 3.00*1.10*ESTOFADO_M2)

K = 'Quarto casal · peseira baú'
a(K,'BR18','Estrutura do baú',             45, 50, 4)
a(K,'BR18','Base e travessa',             156, 48, 3)
a(K,'TA18','Lateral aparente',             45, 50, 2)
t(K, (1.60*0.50 + 2*1.60*0.45)*ESTOFADO_M2)
f(K, 2*DOBR)

K = 'Quarto casal · prateleiras e mesa suspensas'
a(K,'TA18','Prateleira suspensa',          56, 22, 6)
a(K,'TA18','Mesa de cabeceira suspensa',   37, 30, 2)
a(K,'TA18','Fechamento da mesa',           21, 30, 3)
a(K,'BR15','Caixa de gaveta da mesa',      28, 16, 4)
f(K, 1*CORR + 8*SUP_PRAT)
t(K, 4.0*TUBO_ALU_M)

# ── QUARTO SOLTEIRO ───────────────────────────────────────────────────────
K = 'Quarto solteiro · guarda-roupa'
# 160 × 230 × 60 · 2 portas de correr em vidro BRONZE, perfil bronze
a(K,'TA18','Lateral e divisória',         230, 58, 3)
a(K,'TA18','Base, tampo e maleiro',       156, 58, 4)
a(K,'BR18','Prateleira',                   76, 56, 5)
a(K,'BR15','Caixa de gaveta/sapateira',    55, 18, 16)
a(K,'BR6' ,'Fundo de gaveta',              55, 52, 8)
a(K,'TA18','Frente de gaveta',             19, 75, 8)
a(K,'BR6' ,'Fundo',                       230, 78, 2)
f(K, 8*CORR + 2*RO65P_PORTA + RO65P_TRILHO + 7*SUP_PRAT)
t(K, 2*0.74*2.30*VIDRO_BRZ_M2 + 2*6.2*ALUM_M)

K = 'Quarto solteiro · escrivaninha e nicho'
a(K,'TA18','Tampo da escrivaninha',        95, 47, 1)
a(K,'TA18','Lateral e apoio',              72, 45, 2)
a(K,'BR15','Estrutura',                    72, 43, 2)
a(K,'TA18','Nicho na altura da cabeceira', 30, 20, 4)

K = 'Quarto solteiro · prateleiras suspensas'
# 262 de extensão, prateleiras em Tauari com nichos em Cinza Essencial
a(K,'TA18','Prateleira',                   95, 20, 6)
a(K,'CE18','Nicho em Cinza Essencial',     30, 22, 8)
a(K,'CE18','Fundo do nicho',               30, 28, 4)
f(K, 18*SUP_PRAT)

K = 'Quarto solteiro · cabeceira estofada'
a(K,'BR18','Estrutura da cabeceira',       80, 65, 4)
a(K,'BR15','Travessa e fixação',          258, 10, 3)
t(K, 2.62*0.80*ESTOFADO_M2)

# ── BANHEIRO SOCIAL ───────────────────────────────────────────────────────
K = 'Banheiro social · gabinete e prateleiras'
a(K,'TA18','Frente do gabinete',           55, 30, 2)
a(K,'BR15','Lateral e base',               55, 42, 4)
a(K,'BR6' ,'Fundo',                        55, 62, 1)
a(K,'TA18','Prateleira suspensa',          62, 15, 6)
a(K,'TA18','Lateral da torre',            140, 15, 2)
a(K,'BR18','Chapa de apoio do espelho',   120, 62, 3)
f(K, 4*DOBR + 6*SUP_PRAT)
t(K, 1.2*3.70*ESPELHO_M2 + 1.4*LED_M + 0.6*CAVA_M)

# ── BANHEIRO CASAL ────────────────────────────────────────────────────────
K = 'Banheiro casal · gabinete e muxarabi'
a(K,'TA18','Frente do gabinete',           40, 35, 2)
a(K,'BR15','Lateral e base',               40, 42, 4)
a(K,'BR6' ,'Fundo',                        40, 72, 1)
a(K,'TA18','Prateleira',                   35, 22, 4)
a(K,'TA18','Lateral da torre',            120, 22, 2)
a(K,'TA15','Ripa do muxarabi',            120,  2, 46)
a(K,'TA6' ,'Fundo do muxarabi',           120, 35, 1)
f(K, 4*DOBR + 4*SUP_PRAT)
t(K, 1.20*0.35*USIN_MUX_M2 + 0.8*LED_M + 0.7*CAVA_M)

# ══════════════════════════════════════════════════════════════════════════
# CÁLCULO
# ══════════════════════════════════════════════════════════════════════════
def _pack(pcs):
    """Shelf packing (NFDH): abre faixas na largura da chapa e enche cada faixa
    ao longo do comprimento. Peça maior que a chapa é serrada em partes."""
    ch, y, x, hf = 1, 0.0, 0.0, 0.0
    for c, l in pcs:
        if l > CH_L: c, l = l, c          # gira
        if c > CH_C:                      # peça longa: quebra em módulos
            n = -(-int(c*1000)//int(CH_C*1000)); c = c/n
            pcs_extra = [(c, l)]*(n-1)
            pcs = pcs + pcs_extra if isinstance(pcs, list) else pcs
        if x + c <= CH_C and l <= hf:     # cabe na faixa aberta
            x += c; continue
        if y + l <= CH_L:                 # abre faixa nova na mesma chapa
            y += hf if hf else 0
            if y + l > CH_L: ch += 1; y, hf = 0.0, 0.0
            x, hf = c, l; y = y
            continue
        ch += 1; y, x, hf = 0.0, c, l
    return ch

def nest(items):
    if not items: return 0
    base = sorted(((max(c, l), min(c, l)) for c, l in items), key=lambda q: (-q[1], -q[0]))
    ch = _pack(base)
    ar = sum(c*l for c, l in items)/10000
    piso = -(-int(ar/(CH_AREA*0.85)*1000)//1000) or 1   # 85% de aproveitamento teto
    return max(ch, piso)

por, area, area_mov, fita_mov = defaultdict(list), defaultdict(float), defaultdict(float), defaultdict(float)
for mov, mat, d, c, l, q in p:
    for _ in range(q):
        por[mat].append((c, l)); area[mat] += c*l/10000; area_mov[mov] += c*l/10000
        fita_mov[mov] += (c + l)*2/100 * (0.55 if mat.startswith('BR') else 0.75)
CH = {m: nest(v) for m, v in por.items()}

_com_peca = list(dict.fromkeys(x[0] for x in p))
_todos = _com_peca + [k for k in dict.fromkeys(list(FER)+list(TER)) if k not in _com_peca]
_ordem_amb = list(dict.fromkeys(m.split(' · ')[0] for m in _todos))
MOVS = sorted(_todos, key=lambda m: (_ordem_amb.index(m.split(' · ')[0]), _todos.index(m)))
ar_tot = sum(area.values())

# custo de chapa rateado por móvel, proporcional à área de cada material
chapa_mov = defaultdict(float)
for m, n in CH.items():
    custo_m = n*PRECO[m]
    am = defaultdict(float)
    for mov, mat, d, c, l, q in p:
        if mat == m: am[mov] += c*l*q/10000
    tot = sum(am.values())
    for mov, v in am.items(): chapa_mov[mov] += custo_m*v/tot

fita_custo = {mov: fita_mov[mov]*1.10*((FITA_BR+FITA_COR)/2) for mov in MOVS}

# logística — referencias/logistica.md
# ⚠ carreto e diária são por ENDEREÇO, não por ambiente: são dois canteiros
#   (stand e apto decorado), não onze. Só o setup (visita de medição) escala
#   com o número de ambientes.
CARRETO, DIARIA, VISITA = 150.0, 260.0, 275.0
AMB = {mov: mov.split(' · ')[0] for mov in MOVS}
STAND_AMB = ('Copa','Sala de reunião','Sala de ativos','Lounge','Gourmet')
FRENTE = {mov: ('Stand' if AMB[mov] in STAND_AMB else 'Decorado') for mov in MOVS}
fr_area = defaultdict(float)
for mov in MOVS: fr_area[FRENTE[mov]] += area_mov[mov]
log_fr = {}
for fr, ar in fr_area.items():
    n_amb    = len({AMB[m] for m in MOVS if FRENTE[m] == fr})
    carretos = max(2, -(-int(ar)//18))
    dias     = max(3, -(-int(ar)//12))
    log_fr[fr] = dict(compra   = carretos/2*CARRETO,
                      entrega  = carretos/2*CARRETO,
                      equipe   = dias*DIARIA,
                      setup    = (2 + n_amb*0.5)*VISITA)
LOG = {}
for mov in MOVS:
    fr = FRENTE[mov]
    share = area_mov[mov]/fr_area[fr] if fr_area[fr] else 0
    LOG[mov] = sum(log_fr[fr].values())*share

# ── custo direto por móvel ────────────────────────────────────────────────
# ⛔ base do rateio de consumível e logística vem ANTES da ferragem
cdi = {mov: chapa_mov[mov] + fita_custo[mov] for mov in MOVS}
base_fixa = sum(cdi.values())
consum = base_fixa*0.06                       # cola, parafuso, limpeza, acabamento
LOG_TOT = sum(LOG.values())
for mov in MOVS:
    cdi[mov] += (consum + LOG_TOT)*cdi[mov]/base_fixa if base_fixa else 0
for mov in MOVS: cdi[mov] += FER[mov] + TER[mov]
for mov in MOVS: cdi[mov] *= 1 + M.EMBALAGEM  # embalagem 2%, por último

CD = sum(cdi.values())

# ── MC direcionada por complexidade ───────────────────────────────────────
MC_ALVO = defaultdict(lambda: 0.38)
for mov in MOVS:
    if any(k in mov for k in ('painel', 'painéis', 'forro', 'Painel')): MC_ALVO[mov] = 0.35
    if any(k in mov for k in ('estante', 'muxarabi', 'bancadas de trabalho',
                              'guarda-roupa', 'divisória')):            MC_ALVO[mov] = 0.40
BASE = M.base(parcelas=0, rt=True, vendedor=False)

PV = {mov: round(cdi[mov]/(BASE - MC_ALVO[mov])/10)*10 for mov in MOVS}
TOT = sum(PV.values())
MC_REAL = {mov: BASE - cdi[mov]/PV[mov] for mov in MOVS}

# ══════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    br = lambda v: f'{v:,.0f}'.replace(',', '.')
    print('═'*96)
    print('MARCELO TOLENTINO — BRZ NOVA LIMA · stand de vendas + apto decorado')
    print('═'*96)
    print(f'\nBASE = {BASE*100:.2f}%  (à vista · com RT · sem vendedor)\n')

    print('PLANO DE CORTE')
    tc = 0
    for m in sorted(CH, key=lambda k: (k[:2], k)):
        n = CH[m]; c = n*PRECO[m]; tc += c
        print(f'  {NOME[m]:<16}{area[m]:>7.2f} m² → {n:>3} chapa(s) × R$ {PRECO[m]:>6.0f} '
              f'= R$ {br(c):>9}   aprov. {area[m]/(n*CH_AREA)*100:>3.0f}%')
    tch = sum(CH.values())
    print(f'  {"TOTAL":<16}{ar_tot:>7.2f} m² → {tch:>3} chapas'
          f'                 R$ {br(tc):>9}   médio {ar_tot/(tch*CH_AREA)*100:.0f}%')

    print('\nLOGÍSTICA (por endereço)')
    for fr, d in log_fr.items():
        print(f'  {fr:<10}{fr_area[fr]:>7.1f} m²  frete compra {br(d["compra"]):>5} · '
              f'frete entrega {br(d["entrega"]):>5} · equipe {br(d["equipe"]):>5} · '
              f'setup {br(d["setup"]):>5}   = R$ {br(sum(d.values())):>6}')

    print(f'\nCUSTO DIRETO  R$ {br(CD)}   ·   chapa {br(tc)} · fita {br(sum(fita_custo.values()))}'
          f' · consumível {br(consum)} · logística {br(LOG_TOT)}'
          f' · ferragem {br(sum(FER.values()))} · terceiros {br(sum(TER.values()))}')

    print('\n' + '─'*96)
    print(f'{"ITEM":<48}{"m² chapa":>9}{"CUSTO":>11}{"VENDA":>11}{"MC":>7}')
    print('─'*96)
    _amb = None
    for mov in MOVS:
        am = AMB[mov]
        if am != _amb: print(f'\n  {am.upper()}'); _amb = am
        nome = mov.split(' · ')[1] if ' · ' in mov else mov
        print(f'    {nome:<44}{area_mov[mov]:>8.2f}{br(cdi[mov]):>11}{br(PV[mov]):>11}'
              f'{MC_REAL[mov]*100:>6.1f}%')
    print('─'*96)
    print(f'{"TOTAL":<48}{ar_tot:>8.2f}{br(CD):>11}{br(TOT):>11}'
          f'{(BASE - CD/TOT)*100:>6.1f}%')

    print('\nPOR FRENTE')
    for frente, ambs in (('STAND', ('Copa','Sala de reunião','Sala de ativos','Lounge','Gourmet')),
                         ('DECORADO', ('Cozinha','Sala','Quarto casal','Quarto solteiro',
                                       'Banheiro social','Banheiro casal'))):
        c = sum(cdi[m] for m in MOVS if AMB[m] in ambs)
        v = sum(PV[m]  for m in MOVS if AMB[m] in ambs)
        print(f'  {frente:<12}custo R$ {br(c):>9}   venda R$ {br(v):>9}   MC {(BASE-c/v)*100:.1f}%')
