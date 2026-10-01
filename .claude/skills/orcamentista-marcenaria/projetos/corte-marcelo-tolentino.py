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
  5 ★ Salão principal · SEM MOLA. Tip-on mecânico só funciona com dobradiça
    sem mola — a mola briga com o pulsador e a porta volta a abrir sozinha.
    Novisys e Sensys têm versão sem mola; é ela que tem de ser comprada.
    Confirmar na cotação, senão as 14 portas não fecham no toque.
  6 ★ 2 pulsadores por porta no armário ripado. A Blum especifica 2 unidades
    acima de 1,20 m de altura de porta; estas têm 2,20 m. 14 portas = 28.
  7 Não entram nesta conta, e é de propósito: granito cinza andorinha
    escovado (marmoraria), rodapé Santa Luzia H=15 (perfil comercial, corre
    por toda a sala inclusive nas paredes que não são nossas), molduras das
    fotos 85×150 e as TVs touch (comunicação visual).
  9 ★ Melamínico VERDE, cor próxima da laca, na caixa do armário em laca da
    cozinha. A referência exata se escolhe contra a amostra da laca — não há
    verde na paleta deste projeto para comparar. Lancei no preço de
    melamínico de cor (R$ 500 a chapa de 15, R$ 300 a de 6).
  8 ⚠ O hidrante tem de continuar acessível e sinalizado. A tampa de acesso
    está lançada, mas o revestimento não pode criar trava nem exigir
    ferramenta — conferir com a segurança da obra antes de produzir.
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
#                   PA Preto Absoluto Duratex (pilar do salão principal)
#                   VD melamínico verde, cor próxima da laca ★ ver FLAG 9
for c in ('TA','CM','CP','CE','CB','PA','VD'):
    PRECO[c+'6'], PRECO[c+'15'], PRECO[c+'18'] = COR6, COR15, COR18
NOME = {'BR6':'branco 6','BR15':'branco 15','BR18':'branco 18','FOR':'fórmica'}
for c, n in (('TA','Tauari'),('CM','Carv.Munique'),('CP','Cinza Pixel'),
             ('CE','Cinza Essenc.'),('CB','Cerrado Bold'),('PA','Preto Absol.'),
             ('VD','Verde p/ laca')):
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

DOBR, CORR, TIPON = Q({'dobr':1}), Q({'corr':1}), Q({'tipon':1})
ROUPEIRO_2P       = Q({'roup2p':1})   # sistema de correr completo, 2 portas
SUP_PRAT          = Q({'sup':1})

CEN = ('standard', 'gold')
PRECO_FER = {
    # ★ RO65 Prime provisório nos DOIS cenários — a Hettich não tem sistema de
    #   roupeiro de correr na nossa base. Ver FLAG 5.
    # roup2p = sistema completo de 2 portas de correr, com trilho
    #   standard · RO65 Prime Rometal  ★ 2 × 120 + trilho 160 = 400 (provisório)
    #   gold     · Dominus Rometal       700 + trilho 2 m 300  = 1.000
    'standard': dict(dobr=10.0, corr=40.0,  tipon=100.0, roup2p=400.0,  sup=1.50),
    'gold':     dict(dobr=35.0, corr=120.0, tipon=100.0, roup2p=1000.0, sup=1.50),
}
LINHA    = {'standard': 'Novisys · telescópica · roupeiro RO65 Prime · 15 mm',
            'gold':     'Sensys · oculta Quadro · roupeiro Dominus · porta e prateleira 18 mm'}
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
RIPADO_M2    = 70.0     # ★ montagem do ripado: colagem e alinhamento das ripas
                        #   (a chapa das ripas e a fita entram como peça no corte)
BITE_M       = 20.0     # ★ bite 0,5×0,5 nas juntas do pilar, por metro de aresta

p, FER, TER, ESP = [], defaultdict(Q), defaultdict(float), defaultdict(float)
def a(mov, mat, desc, c, l, q=1): p.append((mov, mat, desc, c, l, q))
def f(mov, q): FER[mov] = FER[mov] + q
def t(mov, v): TER[mov] += v
def e(mov, m2): ESP[mov] += m2*ESPELHO_M2   # espelho, linha separada

# ══════════════════════════════════════════════════════════════════════════
# STAND
# ══════════════════════════════════════════════════════════════════════════

# ── SALÃO PRINCIPAL ───────────────────────────────────────────────────────
# [Jonathan 30/09] "adicionar esses itens. se atente para os armários com
#   portas ripadas, considere abertura por toque, com feche toque da Blum."
# Sala de 690 × 1040, pé-direito 260. Prancha BRZ_Salão principal, rev. 01.
K = 'Salão principal · armário ripado com abertura por toque'
# E01: 690 de extensão × 220 de altura × 60 de profundidade.
# 14 portas de 49,4 × 220, abrindo aos pares (dobradiça alternada esq./dir.).
# O ripado medido na elevação: passo 9,3 · ripa 6,2 · vão 3,1 → 5 ripas/porta.
# ⛔ SEM PUXADOR: abertura por toque, pulsador Blum. Ver FLAG 6.
a(K,'TA18','Porta ripada (base)',         220, 49.4, 14)
a(K,'TA15','Ripa do ripado',              220,  6.2, 70)
a(K,'BR15','Lateral e divisória',         220, 58,   15)
a(K,'BR15','Base e travessa',             230, 58,    6)
a(K,'BR6' ,'Fundo',                       220, 173,   4)
a(K,'BR15','Prateleira interna',           47, 58,   56)
a(K,'TA18','Rodapé recuado aparente',     230, 10,    3)
f(K, 70*DOBR + 28*TIPON + 56*SUP_PRAT)
t(K, 15.2*RIPADO_M2)                      # 14 portas × 1,087 m² de frente

K = 'Salão principal · armário liso da entrada'
# E05: porta única de 55,5 × 220 embutida na parede pintada, prateleiras H=40.
# Sem puxador também — porta rente à parede, pulsador Blum.
a(K,'TA18','Porta',                       220, 55.5, 1)
a(K,'BR15','Lateral',                     220, 33,   2)
a(K,'BR15','Base e travessa',              52, 33,   2)
a(K,'BR6' ,'Fundo',                       220, 55,   1)
a(K,'BR15','Prateleira interna',           52, 32,   4)
f(K, 5*DOBR + 2*TIPON + 4*SUP_PRAT)

K = 'Salão principal · painel liso piso/teto'
# 172 × 260 na face sul da parede da entrada, com retorno de 17 na testeira.
a(K,'TA18','Painel',                      260, 43, 4)
a(K,'TA18','Retorno de testeira',         260, 17, 1)
a(K,'BR15','Montante de fixação',         260, 10, 4)

K = 'Salão principal · pilar revestido em painel preto'
# E06/E07: pilar do hidrante, 200 × 40 em planta, revestido piso/teto (260)
# nas quatro faces em MDF Preto Absoluto Duratex, bite 0,5×0,5 nas juntas.
a(K,'PA18','Face maior',                  260, 100, 4)
a(K,'PA18','Face estreita',               260,  40, 2)
a(K,'PA18','Tampa de acesso ao hidrante',  90,  35, 1)
a(K,'BR15','Montante e sarrafo',          260,  10, 6)
f(K, 2*DOBR)
t(K, 20.8*BITE_M)                         # 4 arestas + 4 juntas × 2,60

K = 'Salão principal · bancada da secretária'
# E01/E02/Corte AA: 170 × 85 × 100 (corpo 93 + tampo de granito 7).
# Frente inclinada — 40 no topo, 18 na base. Tampo de trabalho a 75.
# ⚠ o granito cinza andorinha escovado é da marmoraria, não entra aqui.
a(K,'TA18','Frente inclinada',            170, 102, 1)
a(K,'TA18','Lateral aparente',            100,  85, 2)
a(K,'TA18','Tampo de trabalho',           115,  45, 1)
a(K,'BR15','Base de apoio do granito',    168,  83, 1)
a(K,'BR15','Montante',                     93,  83, 4)
a(K,'BR15','Travessa',                    165,  40, 3)
a(K,'BR15','Prateleira interna',          165,  40, 1)
a(K,'BR6' ,'Fechamento posterior',        168,  93, 1)
f(K, 1*SUP_PRAT)

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
f(K, 5*DOBR)                              # porta de 230 × 100: 5 dobradiças
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
# ⭐ [Jonathan 01/10] "onde terá o acabamento em laca na cozinha, a estrutura
#   interna será em melamínico em COR PRÓXIMA" — e não em branco. Caixa branca
#   atrás de frente em laca verde aparece na fresta e no vão da porta aberta.
a(K,'BR18','Frente para laca',             91, 43, 5)
a(K,'VD15','Lateral e divisória',          91, 58, 6)
a(K,'VD15','Base e travessa',             215, 58, 3)
a(K,'VD6' ,'Fundo',                       215, 91, 1)
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
t(K, 4.5*LED_M)   # LED sob os nichos em Carvalho Munique (setas na E01/E04)

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
f(K, 6*CORR + ROUPEIRO_2P + 8*SUP_PRAT)
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
f(K, 8*CORR + ROUPEIRO_2P + 7*SUP_PRAT)
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

# ── papel da peça e espessura por cenário ────────────────────────────────
# [Jonathan 30/09] "na standard estrutura, porta e prateleiras de 15; na gold
#   as portas e prateleiras passam para 18 mm."
def papel(mat, d):
    dl = d.lower()
    if mat == 'FOR':       return 'FOR'      # fórmica, sem espessura de chapa
    if mat.endswith('6'):  return 'F'        # fundo, 6 mm nos dois
    # ⛔ porta ripada: 18 mm nos DOIS cenários. Ripa colada numa face só faz
    #   par bimetálico; 49,4 × 220 em 15 mm empena, e empenada não fecha no
    #   toque. Aqui a espessura é requisito, não nível de acabamento.
    if 'ripad' in dl:      return 'E18'
    if 'bandeira' in dl or 'tampo e maleiro' in dl: return 'E'
    if any(k in dl for k in ('porta', 'frente', 'prateleira')): return 'PP'
    return 'E'                                # estrutura, 15 mm nos dois

ESP_CEN = {'standard': {'E':'15', 'PP':'15', 'E18':'18'},
           'gold':     {'E':'15', 'PP':'18', 'E18':'18'}}
def mat_cen(mat, pap, cen):
    if pap == 'FOR': return 'FOR'
    cor = mat[:-2] if mat[-2:] in ('15', '18') else mat[:-1]
    return cor + ('6' if pap == 'F' else ESP_CEN[cen][pap])

area_mov, fita_mov = defaultdict(float), defaultdict(float)
por   = {c: defaultdict(list)  for c in CEN}
area  = {c: defaultdict(float) for c in CEN}
amov  = {c: defaultdict(lambda: defaultdict(float)) for c in CEN}   # [cen][mat][mov]
for mov, mat, d, c, l, q in p:
    pap = papel(mat, d)
    area_mov[mov] += c*l*q/10000
    fita_mov[mov] += (c + l)*2/100*q * (0.55 if mat.startswith('BR') else 0.75)
    for cen in CEN:
        mc_ = mat_cen(mat, pap, cen)
        for _ in range(q): por[cen][mc_].append((c, l))
        area[cen][mc_]      += c*l*q/10000
        amov[cen][mc_][mov] += c*l*q/10000

CH      = {c: {m: nest(v) for m, v in por[c].items()} for c in CEN}
ar_tot  = sum(area['standard'].values())
custo_chapa = {c: sum(CH[c][m]*PRECO[m] for m in CH[c]) for c in CEN}

chapa_mov = {c: defaultdict(float) for c in CEN}
for c in CEN:
    for m, n in CH[c].items():
        tot = sum(amov[c][m].values())
        for mov, v in amov[c][m].items():
            chapa_mov[c][mov] += n*PRECO[m]*v/tot

_com_peca = list(dict.fromkeys(x[0] for x in p))
_todos = _com_peca + [k for k in dict.fromkeys(list(FER)+list(TER)+list(ESP)) if k not in _com_peca]
_ordem_amb = list(dict.fromkeys(m.split(' · ')[0] for m in _todos))
MOVS = sorted(_todos, key=lambda m: (_ordem_amb.index(m.split(' · ')[0]), _todos.index(m)))

fita_custo = {mov: fita_mov[mov]*1.10*((FITA_BR+FITA_COR)/2) for mov in MOVS}
# fita e logística não mudam com a espessura: o perímetro é o mesmo

# logística — referencias/logistica.md
# ⚠ carreto e diária são por ENDEREÇO, não por ambiente: são dois canteiros
#   (stand e apto decorado), não onze. Só o setup (visita de medição) escala
#   com o número de ambientes.
CARRETO, DIARIA, VISITA = 150.0, 260.0, 275.0
AMB = {mov: mov.split(' · ')[0] for mov in MOVS}
STAND_AMB = ('Salão principal','Copa','Sala de reunião','Sala de ativos','Lounge','Gourmet')
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
# ⛔ [30/09] A BASE DO RATEIO NÃO PODE CONTER NADA QUE MUDE ENTRE OS CENÁRIOS.
#   A regra de 29/08 mandava ratear por custo com a base tomada ANTES da
#   ferragem. Isso bastava enquanto só a ferragem diferia. Com a espessura
#   variando por cenário, a própria chapa entrou na base e um item 100%
#   estrutura passou a pegar uma fatia diferente em cada cenário — o assert
#   pegou no "Gourmet · painéis e forro". Duas correções:
#     · consumível  = 6% da chapa e fita DO PRÓPRIO item, sem rateio
#     · logística   = rateada pela ÁREA de chapa, que não muda entre cenários
LOG_TOT = sum(LOG.values())
fixo, consum = {}, {}
for c in CEN:
    fx = {}
    consum[c] = 0.0
    for mov in MOVS:
        proprio = chapa_mov[c][mov] + fita_custo[mov]
        cons    = proprio*0.06                # cola, parafuso, limpeza, acabamento
        consum[c] += cons
        share   = area_mov[mov]/ar_tot if ar_tot else 0
        fx[mov] = proprio + cons + LOG_TOT*share + TER[mov] + ESP[mov]
    fixo[c] = fx

def custo_fer(mov, cen):
    pr = PRECO_FER[cen]
    return sum(pr[k]*q for k, q in FER[mov].items())

CDI = {c: {mov: (fixo[c][mov] + custo_fer(mov, c))*(1 + M.EMBALAGEM) for mov in MOVS}
       for c in CEN}
CD  = {c: sum(CDI[c].values()) for c in CEN}

# ⛔ guarda, agora em duas partes. A partir de 30/09 a ESPESSURA também muda
#   entre cenários, então "sem ferragem" já não basta para o custo ser igual:
#   o item precisa também não ter porta nem prateleira.
SO_ESTRUTURA = {mov for mov in MOVS
                if not FER[mov]
                and all(papel(mat, d) != 'PP' for m2, mat, d, *_ in p if m2 == mov)}
#   Sobra um desvio de até 3% nos itens só-estrutura, e ele é REAL: no gold
#   parte da chapa de 15 migra para 18, o número de chapas de 15 cai e o
#   aproveitamento muda, então o m² de 15 custa um pouco diferente. É efeito
#   de plano de corte compartilhado, não vazamento de rateio — os itens sem
#   chapa própria fecham em 0,00%.
for mov in SO_ESTRUTURA:
    a, b = CDI['standard'][mov], CDI['gold'][mov]
    assert abs(b - a)/a < 0.03, f'{mov}: {a:.0f} vs {b:.0f}'

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
                              'guarda-roupa', 'divisória', 'ripado')):  b = 0.40
    MC_ITEM[mov] = {'standard': b - CORTE_STD, 'gold': b - CORTE_STD + DELTA_GOLD}

AMBS     = list(dict.fromkeys(AMB[m] for m in MOVS))
ITENS_DE = {am: [m for m in MOVS if AMB[m] == am] for am in AMBS}
AR_AMB   = {am: sum(area_mov[m] for m in ITENS_DE[am]) for am in AMBS}
FR_DE    = {am: FRENTE[ITENS_DE[am][0]] for am in AMBS}

CD_AMB  = {c: {am: sum(CDI[c][m] for m in ITENS_DE[am]) for am in AMBS} for c in CEN}
MC_ALVO = {c: {am: sum(CDI[c][m]*MC_ITEM[m][c] for m in ITENS_DE[am])/CD_AMB[c][am]
               for am in AMBS} for c in CEN}
# ⭐ [Jonathan 01/10] "coloque a proposta com um investimento de 189k".
#   O alvo vale para a linha STANDARD, que é a que fecha. A escada de MC por
#   complexidade desce um mesmo delta inteira, por bisseção, para que a
#   distância entre painelaria, armário e item especial continue valendo.
ALVO_STD = 189000.0
def _tot_cen(c, d):
    return sum(round(CD_AMB[c][am]/(BASE - (MC_ALVO[c][am] + d))/10)*10 for am in AMBS)
_lo, _hi = -0.35, 0.0
for _ in range(80):
    _mid = (_lo + _hi)/2
    if _tot_cen('standard', _mid) < ALVO_STD: _lo = _mid
    else: _hi = _mid
DELTA_FECH = {'standard': (_lo + _hi)/2, 'gold': 0.0}

PV      = {c: {am: round(CD_AMB[c][am]/(BASE - (MC_ALVO[c][am] + DELTA_FECH[c]))/10)*10
               for am in AMBS} for c in CEN}
# o arredondamento de R$ 10 por ambiente deixa resíduo contra o alvo: ele vai
# para o maior ambiente sem espelho, para o total bater no número combinado
_resto = ALVO_STD - sum(PV['standard'].values())
if _resto:
    _maior = max((a for a in AMBS if sum(ESP[m] for m in ITENS_DE[a]) <= 0),
                 key=lambda a: PV['standard'][a])
    PV['standard'][_maior] += _resto
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

    print('\nPLANO DE CORTE')
    for c in CEN:
        print(f'  ── {c} ──')
        for m in sorted(CH[c], key=lambda k: (k[:2], k)):
            n = CH[c][m]; v = n*PRECO[m]
            print(f'    {NOME[m]:<16}{area[c][m]:>7.2f} m² → {n:>3} chapa × R$ {PRECO[m]:>5.0f} '
                  f'= R$ {br(v):>7}   aprov. {area[c][m]/(n*CH_AREA)*100:>3.0f}%')
        tch = sum(CH[c].values())
        print(f'    {"TOTAL":<16}{ar_tot:>7.2f} m² → {tch:>3} chapas'
              f'                R$ {br(custo_chapa[c]):>7}   médio '
              f'{ar_tot/(tch*CH_AREA)*100:.0f}%')

    print('\nABERTURA DO CUSTO DIRETO')
    fer = {c: sum(custo_fer(m, c) for m in MOVS) for c in CEN}
    emb = {c: CD[c] - (custo_chapa[c]+sum(fita_custo.values())+consum[c]+LOG_TOT
                       +fer[c]+sum(TER.values())+ESP_TOT) for c in CEN}
    print(f'  {"":<20}{"standard":>12}{"gold":>12}')
    for rot, v in (('chapa', (custo_chapa['standard'], custo_chapa['gold'])),
                   ('fita de borda', (sum(fita_custo.values()),)*2),
                   ('consumíveis', (consum['standard'], consum['gold'])),
                   ('logística', (LOG_TOT,)*2),
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

    print(f'\n⭐ FECHAMENTO EM R$ {br(ALVO_STD)} — o que o alvo custou')
    _sem = _tot_cen('standard', 0.0)
    print(f'  {"sem alvo, pela escada de MC":<34}R$ {br(_sem):>9}'
          f'   MC {(BASE-CD["standard"]/_sem)*100:>5.1f}%')
    print(f'  {"fechado em 189k ← entregue":<34}R$ {br(TOT["standard"]):>9}'
          f'   MC {(BASE-CD["standard"]/TOT["standard"])*100:>5.1f}%')
    print(f'  {"desconto":<34}R$ {br(_sem-TOT["standard"]):>9}'
          f'   {DELTA_FECH["standard"]*100:>5.1f} pontos de MC')
    print(f'  ⚠ A standard já rodava abaixo do piso de 35% da casa. Em 189k ela')
    print(f'    roda a {(BASE-CD["standard"]/TOT["standard"])*100:.1f}% — '
          f'{35-(BASE-CD["standard"]/TOT["standard"])*100:.1f} pontos abaixo do piso.')

    print(f'\nESPELHOS — mesmo custo nos dois cenários, linha à parte')
    for am in AMBS:
        if ESP_AMB[am] <= 0: continue
        print(f'  {am:<26}{ESP_AMB[am]/ESPELHO_M2:>6.2f} m² × R$ {ESPELHO_M2:.0f} = '
              f'R$ {br(ESP_AMB[am]):>6}')
    print(f'  {"TOTAL":<26}{ESP_TOT/ESPELHO_M2:>6.2f} m²'
          f'{"":>13} R$ {br(ESP_TOT):>6}')
