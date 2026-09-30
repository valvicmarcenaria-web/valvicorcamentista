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

# ── ferragens: os itens lançam QUANTIDADE, o cenário dá o preço ──────────
# [Jonathan 30/09] Dois cenários de investimento:
#   standard = a ferragem desta proposta        · garantia 2 anos
#   gold     = Hettich (Sensys + oculta Quadro) · garantia 10 anos
class Q(dict):
    """Unidade de ferragem. `4*DOBR + 8*CORR` vira {'dobr':4,'corr':8}."""
    def __mul__(self, n): return Q({k: v*n for k, v in self.items()})
    __rmul__ = __mul__
    def __add__(self, o):
        r = Q(self)
        for k, v in (o or {}).items(): r[k] = r.get(k, 0) + v
        return r
    __radd__ = __add__

DOBR, CORR, TIPON         = Q({'dobr':1}), Q({'corr':1}), Q({'tipon':1})
RO65P_PORTA, RO65P_TRILHO = Q({'ro_porta':1}), Q({'ro_trilho':1})
SUP_PRAT                  = Q({'sup':1})

CEN = ('standard', 'gold')
PRECO_FER = {
    # ★ RO65 Prime provisório nos DOIS cenários — a Hettich não tem sistema de
    #   roupeiro de correr na nossa base. Ver FLAG 5.
    'standard': dict(dobr=10.0, corr=40.0,  tipon=100.0,
                     ro_porta=120.0, ro_trilho=160.0, sup=1.50),
    'gold':     dict(dobr=35.0, corr=120.0, tipon=100.0,
                     ro_porta=120.0, ro_trilho=160.0, sup=1.50),
}
LINHA    = {'standard': 'Hettich Novisys · corrediça telescópica · RO65 Prime',
            'gold':     'Hettich Sensys · corrediça oculta Quadro Hettich · RO65 Prime'}
GARANTIA = {'standard': '2 anos', 'gold': '10 anos'}

CAVA_M = 50.0     # perfil cava usinado, por metro de frente

# ── terceiros ─────────────────────────────────────────────────────────────
LACA_M2      = 650.0
VIDRO_M2     = 300.0    # incolor temperado
VIDRO_CAN_M2 = 420.0    # ★ canelado — 40% acima do incolor
VIDRO_BRZ_M2 = 420.0    # ★ bronze   — 40% acima do incolor
ESPELHO_M2   = 650.0    # [Jonathan 29/09] linha própria, R$ 650/m²
ALUM_M       = 85.0     # ★ perfil de alumínio (bronze / preto fosco), por metro
ESTOFADO_M2  = 450.0
TUBO_ALU_M   = 60.0     # tubo 2×2 preto
LED_M        = 150.0    # LED COB fita + perfil
USIN_MUX_M2  = 380.0    # ★ usinagem do muxarabi

p, FER, TER, ESP = [], defaultdict(Q), defaultdict(float), defaultdict(float)
def a(mov, mat, desc, c, l, q=1): p.append((mov, mat, desc, c, l, q))
def f(mov, q): FER[mov] = FER[mov] + q
def t(mov, v): TER[mov] += v
def e(mov, m2): ESP[mov] += m2*ESPELHO_M2   # espelho, linha separada

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
# ⚠ corrigido 29/09 na E04: a bancada tem 85 (32,5 + 32,5 + 20) e o espelho
#   acima dela é 85 × 120 — eu tinha lançado 1,2 × 3,70 m, parede inteira.
a(K,'TA18','Frente do gabinete',           37, 32, 2)
a(K,'BR15','Lateral e base',               37, 42, 4)
a(K,'BR6' ,'Fundo',                        37, 85, 1)
a(K,'TA18','Prateleira suspensa',          62, 15, 6)
a(K,'TA18','Lateral da torre',            140, 15, 2)
a(K,'BR18','Chapa de apoio do espelho',   120, 85, 1)
f(K, 4*DOBR + 6*SUP_PRAT)
e(K, 0.85*1.20)
t(K, 1.4*LED_M + 0.6*CAVA_M)

# ── BANHEIRO CASAL ────────────────────────────────────────────────────────
K = 'Banheiro casal · gabinete, espelho e muxarabi'
# ⚠ corrigido 29/09 na E03: o armário tem 140 e QUATRO portas de 35, e a
#   parede leva um ESPELHO COM MOLDURA EM MDF TAUARI de 188 × 116 que não
#   estava na conta.
a(K,'TA18','Frente do gabinete',           40, 35, 4)
a(K,'BR15','Lateral e base',               40, 42, 6)
a(K,'BR6' ,'Fundo',                        40,140, 1)
a(K,'TA18','Moldura do espelho',          192,  4, 2)
a(K,'TA18','Moldura do espelho (lateral)',120,  4, 2)
a(K,'BR18','Chapa de apoio do espelho',   116, 94, 2)
a(K,'TA18','Prateleira',                   35, 22, 4)
a(K,'TA18','Lateral da torre',            120, 22, 2)
a(K,'TA15','Ripa do muxarabi',            120,  2, 46)
a(K,'TA6' ,'Fundo do muxarabi',           120, 35, 1)
f(K, 8*DOBR + 4*SUP_PRAT)
e(K, 1.88*1.16)
t(K, 1.20*0.35*USIN_MUX_M2 + 0.8*LED_M + 1.4*CAVA_M)

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

# ── custo direto por móvel, POR CENÁRIO ───────────────────────────────────
# ⛔ base do rateio de consumível e logística vem ANTES da ferragem, senão o
#   item sem ferragem muda de custo de um cenário para o outro.
fixo = {mov: chapa_mov[mov] + fita_custo[mov] for mov in MOVS}
base_fixa = sum(fixo.values())
consum = base_fixa*0.06                       # cola, parafuso, limpeza, acabamento
LOG_TOT = sum(LOG.values())
for mov in MOVS:
    fixo[mov] += (consum + LOG_TOT)*fixo[mov]/base_fixa if base_fixa else 0
    fixo[mov] += TER[mov] + ESP[mov]          # terceiros e espelho não mudam

def custo_fer(mov, cen):
    pr = PRECO_FER[cen]
    return sum(pr[k]*q for k, q in FER[mov].items())

CDI = {c: {mov: (fixo[mov] + custo_fer(mov, c))*(1 + M.EMBALAGEM) for mov in MOVS}
       for c in CEN}
CD  = {c: sum(CDI[c].values()) for c in CEN}

# ⛔ guarda: item SEM ferragem tem de custar o MESMO nos dois cenários
for mov in MOVS:
    if not FER[mov]:
        assert abs(CDI['standard'][mov] - CDI['gold'][mov]) < 0.01, mov

# ── MC direcionada por complexidade, fechada POR AMBIENTE ────────────────
# [Jonathan 29/09] sem RT e sem comissão de venda · MC −5 pontos
# [Jonathan 30/09] standard leva mais −3 pontos · gold fica 8 pontos acima
RT_ON, COMISSAO = False, False
BASE = M.base(parcelas=0, rt=RT_ON, vendedor=COMISSAO)
CORTE_STD, DELTA_GOLD = 0.08, 0.08            # 5 + 3 pontos · gold +8 pontos

MC_ITEM = {}
for mov in MOVS:
    b = 0.38
    if any(k in mov for k in ('painel', 'painéis', 'forro', 'Painel')): b = 0.35
    if any(k in mov for k in ('estante', 'muxarabi', 'bancadas de trabalho',
                              'guarda-roupa', 'divisória')):            b = 0.40
    MC_ITEM[mov] = {'standard': b - CORTE_STD, 'gold': b - CORTE_STD + DELTA_GOLD}

AMBS     = list(dict.fromkeys(AMB[m] for m in MOVS))
ITENS_DE = {am: [m for m in MOVS if AMB[m] == am] for am in AMBS}
AR_AMB   = {am: sum(area_mov[m] for m in ITENS_DE[am]) for am in AMBS}
FR_DE    = {am: FRENTE[ITENS_DE[am][0]] for am in AMBS}

CD_AMB  = {c: {am: sum(CDI[c][m] for m in ITENS_DE[am]) for am in AMBS} for c in CEN}
MC_ALVO = {c: {am: sum(CDI[c][m]*MC_ITEM[m][c] for m in ITENS_DE[am])/CD_AMB[c][am]
               for am in AMBS} for c in CEN}
PV      = {c: {am: round(CD_AMB[c][am]/(BASE - MC_ALVO[c][am])/10)*10 for am in AMBS}
           for c in CEN}
TOT     = {c: sum(PV[c].values()) for c in CEN}
MC_REAL = {c: {am: BASE - CD_AMB[c][am]/PV[c][am] for am in AMBS} for c in CEN}

ESP_AMB = {am: sum(ESP[m] for m in ITENS_DE[am]) for am in AMBS}
ESP_TOT = sum(ESP.values())

for c in CEN:
    assert abs(sum(CD_AMB[c].values()) - CD[c]) < 0.01
    assert abs(sum(PV[c].values()) - TOT[c]) < 0.01

# ══════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    br = lambda v: f'{v:,.0f}'.replace(',', '.')
    W = 98
    print('═'*W)
    print('MARCELO TOLENTINO — BRZ NOVA LIMA · stand de vendas + apto decorado')
    print('═'*W)
    print(f'\nBASE {BASE*100:.2f}%   à vista · sem RT · sem comissão de venda')
    print(f'\n{"":<12}{"ferragem":<52}{"garantia":>10}{"alvos de MC":>22}')
    for c in CEN:
        alvos = sorted({MC_ITEM[m][c] for m in MOVS})
        print(f'  {c:<10}{LINHA[c]:<52}{GARANTIA[c]:>10}'
              f'{"  ·  ".join(f"{a*100:.0f}%" for a in alvos):>22}')

    print('\nPLANO DE CORTE  (idêntico nos dois cenários)')
    tc = 0
    for m in sorted(CH, key=lambda k: (k[:2], k)):
        n = CH[m]; c = n*PRECO[m]; tc += c
        print(f'  {NOME[m]:<16}{area[m]:>7.2f} m² → {n:>3} chapa × R$ {PRECO[m]:>5.0f} '
              f'= R$ {br(c):>7}   aprov. {area[m]/(n*CH_AREA)*100:>3.0f}%')
    tch = sum(CH.values())
    print(f'  {"TOTAL":<16}{ar_tot:>7.2f} m² → {tch:>3} chapas'
          f'                R$ {br(tc):>7}   médio {ar_tot/(tch*CH_AREA)*100:.0f}%')

    print('\nABERTURA DO CUSTO DIRETO')
    fer = {c: sum(custo_fer(m, c) for m in MOVS) for c in CEN}
    emb = {c: CD[c] - (tc+sum(fita_custo.values())+consum+LOG_TOT+fer[c]
                       +sum(TER.values())+ESP_TOT) for c in CEN}
    print(f'  {"":<20}{"standard":>12}{"gold":>12}')
    for rot, v in (('chapa', (tc, tc)), ('fita de borda', (sum(fita_custo.values()),)*2),
                   ('consumíveis', (consum,)*2), ('logística', (LOG_TOT,)*2),
                   ('ferragem', (fer['standard'], fer['gold'])),
                   ('espelhos', (ESP_TOT,)*2),
                   ('terceirizados', (sum(TER.values()),)*2),
                   ('embalagem (2%)', (emb['standard'], emb['gold']))):
        d = '  ←  muda' if abs(v[0]-v[1]) > 1 else ''
        print(f'  {rot:<20}{br(v[0]):>12}{br(v[1]):>12}{d}')
    print(f'  {"CUSTO DIRETO":<20}{br(CD["standard"]):>12}{br(CD["gold"]):>12}')

    print('\n' + '─'*W)
    print(f'{"AMBIENTE":<26}{"m²":>7}' + ''.join(f'{"CUSTO "+c[:3]:>12}{"VENDA "+c[:3]:>12}{"MC":>7}' for c in CEN))
    print('─'*W)
    for fr in ('Stand', 'Decorado'):
        print(f'\n  {fr.upper()}')
        for am in AMBS:
            if FR_DE[am] != fr: continue
            linha = f'    {am:<22}{AR_AMB[am]:>7.1f}'
            for c in CEN:
                linha += f'{br(CD_AMB[c][am]):>12}{br(PV[c][am]):>12}{MC_REAL[c][am]*100:>6.1f}%'
            print(linha)
        linha = f'    {"subtotal "+fr.lower():<22}{fr_area[fr]:>7.1f}'
        for c in CEN:
            cc = sum(CD_AMB[c][a] for a in AMBS if FR_DE[a] == fr)
            vv = sum(PV[c][a]     for a in AMBS if FR_DE[a] == fr)
            linha += f'{br(cc):>12}{br(vv):>12}{(BASE-cc/vv)*100:>6.1f}%'
        print(linha)
    print('─'*W)
    linha = f'  {"TOTAL":<24}{ar_tot:>7.1f}'
    for c in CEN:
        linha += f'{br(CD[c]):>12}{br(TOT[c]):>12}{(BASE-CD[c]/TOT[c])*100:>6.1f}%'
    print(linha)
    print('─'*W)
    d = TOT['gold'] - TOT['standard']
    print(f'\n  gold − standard  =  R$ {br(d)}   (+{d/TOT["standard"]*100:.1f}%)'
          f'   ·   ferragem a mais custa R$ {br(fer["gold"]-fer["standard"])}')

    print(f'\nESPELHOS — mesmo custo nos dois cenários, linha à parte')
    for am in AMBS:
        if ESP_AMB[am] <= 0: continue
        print(f'  {am:<26}{ESP_AMB[am]/ESPELHO_M2:>6.2f} m² × R$ {ESPELHO_M2:.0f} = '
              f'R$ {br(ESP_AMB[am]):>6}')
    print(f'  {"TOTAL":<26}{ESP_TOT/ESPELHO_M2:>6.2f} m²'
          f'{"":>13} R$ {br(ESP_TOT):>6}')
