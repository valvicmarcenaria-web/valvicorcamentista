# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — o levantamento peça a peça e o custo.

⛔⛔ TODA MEDIDA AQUI FOI LIDA NA PRANCHA, NO OLHO. O executivo está
  vetorizado e não tem uma cota extraível. O que está escrito em
  `_COZINHA.md`, `_SALA-SUITE.md` e `_HALL-ESCRITORIO.md` é a fonte; aqui
  só se calcula.

⛔ E NADA É ESTIMADO. Cada chapa sai da soma de área das peças, dividida
  pela área útil da chapa e arredondada para cima por padrão × espessura —
  a regra de ferro da Base de Custos.

⚠ AS PREMISSAS, TODAS DECLARADAS. Onde a prancha não diz, eu não chuto: ou
  assumo com o nome "premissa" e o número aparece na lista de pendências, ou
  deixo de fora e nomeio. Elas estão em PREMISSAS, no fim deste arquivo.
"""
import importlib.util, sys, pathlib, math, contextlib, io

P = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('b', P / 'base.py')
b = importlib.util.module_from_spec(_s); sys.modules['b'] = b
with contextlib.redirect_stdout(io.StringIO()): _s.loader.exec_module(b)
b_ = b

COR, BR = 'MDF cor', 'MDF Branco TX'


class Movel:
    def __init__(self, amb, nome, nota=''):
        self.amb, self.nome, self.nota = amb, nome, nota
        self.pecas, self.fita, self.ferr, self.terc, self.vidro = [], 0.0, [], [], []
        self.fita_ripa = 0.0      # ⭐ a da ripa é MANUAL; o resto é máquina

    def p(self, nome, L, A, esp, mat=COR, qtd=1, fita_m=0.0):
        """Uma peça: L × A em cm, espessura em mm, material e quantas."""
        self.pecas.append((nome, L, A, esp, mat, qtd))
        self.fita += fita_m * qtd
        return self

    def f(self, nome, qtd, unit):
        self.ferr.append((nome, qtd, unit)); return self

    def t(self, nome, qtd, unit):
        self.terc.append((nome, qtd, unit)); return self

    def v(self, nome, folhas, unit=None):
        self.vidro.append((nome, folhas, unit or b.VIDRO_FOLHA)); return self

    def areas(self):
        """m² por (material, espessura)."""
        d = {}
        for _n, L, A, esp, mat, q in self.pecas:
            d[(mat, esp)] = d.get((mat, esp), 0.0) + L * A * q / 10000
        return d


M = []                                    # todos os móveis do projeto


def mv(amb, nome, nota=''):
    m = Movel(amb, nome, nota); M.append(m); return m


# ════════════════════════════════════════════════════════════════════════
# O RIPADO — o item do projeto, e o que mais depende de premissa
# ════════════════════════════════════════════════════════════════════════
RIPA_L, VAO, PASSO = 2.0, 1.0, 3.0        # cm · DETALHE 1:5, que é cotado
#   ⚠ A hachura da elevação do escritório desenha passo de 5,0 cm. O detalhe
#     cotado governa sobre a hachura, que é simbólica — mas de 3 para 5 o
#     metro de ripa cai 40%, então fica registrado como pendência.
BASE_ESP = 15                             # a base de 1 cm vira 15 mm, que é
#   a chapa de estrutura da casa. ⚠ A prancha cota 1 cm; 15 mm é o vizinho
#   comercial e o padrão da Base.


def ripas_em(largura_cm):
    """⛔ CONTAGEM, NÃO REGRA DE TRÊS: com ripa nas duas pontas, n ripas e
       n−1 vãos. 626 fecha exato em 209; os demais trechos não fecham e a
       produção decide as pontas."""
    return math.floor((largura_cm + VAO) / PASSO)


RIPAS_POR_CHAPA = math.floor(b.CHAPA_L / (RIPA_L * b.RIPA_PERDA))
#   ⭐ 185 ÷ 2,2 = 84 ripas por chapa. A tira é o corte mais eficiente que
#     existe — mas só porque a ripa de 272 CABE nos 275 da chapa. Fosse 274
#     e cada ripa pediria emenda.


def painel_ripado(m, largura, altura, atras=True):
    """A base contínua + as ripas + a mão de obra de ripado."""
    n = ripas_em(largura)
    area_rip = n * (RIPA_L / 100) * (altura / 100)
    if atras:
        m.p('base contínua do painel', largura, altura, BASE_ESP)
    m.p(f'{n} ripas de {RIPA_L:g} × {altura:g}', RIPA_L * n * b.RIPA_PERDA,
        altura, 18)
    #   ⭐ a perda de serra entra na LARGURA da peça equivalente, que é onde
    #     ela acontece de verdade: cada corte come lâmina.
    m.t('Painel ripado, mão de obra', round(largura * altura / 10000, 2), b.RIPADO_M2)
    #   ⛔ A FITA DA RIPA É O MAIOR METRO DO PROJETO: cada ripa leva fita nas
    #     duas arestas que ficam à vista, e é filetagem MANUAL, porque ripa
    #     de 2 cm não entra na coladeira.
    m.fita += n * altura / 100 * 2
    m.fita_ripa += n * altura / 100 * 2
    m.t('Filetagem manual de ripa', round(n * altura / 100 * 2, 1), b.FILETE_MAO)
    return n


# ════════════════════════════════════════════════════════════════════════
# HALL E JANTAR
# ════════════════════════════════════════════════════════════════════════
m = mv('Hall', 'Painel do hall com porta de lavanderia',
       '206 × 272 × 2, a 3 cm do piso')
m.p('painel fixo esquerdo', 31, 272, 15, fita_m=(31 + 272) * 2 / 100)
m.p('painel fixo direito', 93, 272, 15, fita_m=(93 + 272) * 2 / 100)
m.p('folha da porta mimetizada', 80, 210, 15, fita_m=(80 + 210) * 2 / 100)
m.p('bandeira sobre a porta', 80, 64, 15, fita_m=(80 + 64) * 2 / 100)
m.f('Dobradiça da porta mimetizada', b.dobradicas(210), b.DOBRADICA)
m.t('Cava usinada de 10 cm', 0.10, b.CAVA_M)
#   ⚠ As duas arandelas de Ø26 não são nossas, mas pedem recorte no MDF.
#     Não cobro o recorte: é furo, não peça. Fica nomeado na proposta.

m = mv('Hall', 'Bit de canto do painel', '23 × 272, corte a 45°')
m.p('bit de canto', 23, 272, 15, fita_m=272 * 2 / 100)

m = mv('Jantar', 'Aparador suspenso',
       '308 × 50 × 45, suspenso a 35 do piso · 3 frentes BASCULANTES')
m.p('tampo', 308, 45, 15, fita_m=(308 + 45) * 2 / 100)
m.p('base', 308, 45, 15, fita_m=(308 + 45) * 2 / 100)
m.p('laterais', 45, 50, 15, qtd=2, fita_m=(45 + 50) * 2 / 100)
m.p('divisória sob a gaveta', 60, 41, 15, fita_m=60 / 100)
m.p('fundo', 304, 46, 6)
m.p('frente basculante 102', 102, 50, 15, qtd=2, fita_m=(102 + 50) * 2 / 100)
m.p('frente basculante 104', 104, 50, 15, fita_m=(104 + 50) * 2 / 100)
m.p('gaveta interna · caixa', 60, 10, 15, qtd=2, fita_m=60 / 100)
m.p('gaveta interna · lateral', 31, 10, 15, qtd=2)
m.p('gaveta interna · fundo', 60, 31, 6)
#   ⛔⛔ BÁSCULA NÃO LEVA DOBRADIÇA, LEVA ARTICULADOR. O triângulo com base
#     embaixo e vértice no topo é báscula; o escritório, na MESMA família de
#     pranchas, marca giro com X e com "<". Três articuladores a R$ 250 são
#     R$ 750 onde a dobradiça seriam R$ 90.
m.f('Articulador Blum AVENTOS HK-XS', 3, 250.0)
m.f('Corrediça da gaveta interna', 1, b.CORREDICA_PAR)
m.t('Cava usinada nas 3 frentes', 3.08, b.CAVA_M)

# ════════════════════════════════════════════════════════════════════════
# COZINHA
# ════════════════════════════════════════════════════════════════════════
m = mv('Cozinha', 'Armário superior com portas de vidro',
       '283 × 125 × 35, suspenso a 150 · 4 portas de VIDRO')
m.p('tampo', 283, 35, 15, fita_m=283 / 100)
m.p('base do corpo', 283, 35, 15, fita_m=283 / 100)
m.p('laterais', 35, 100, 15, qtd=2, fita_m=100 / 100)
m.p('divisórias internas', 35, 100, 15, qtd=3, fita_m=100 / 100)
m.p('fundo', 283, 100, 6)
m.p('faixa inferior de 21', 283, 21, 15, fita_m=(283 + 21) * 2 / 100)
m.p('tampo e fundo da faixa', 283, 35, 15, qtd=2, fita_m=283 / 100)
m.v('Porta de vidro reflecta 70,8 × 95', 4)
m.f('Dobradiça de porta de vidro', 4 * b.dobradicas(95), b.DOBRADICA_VIDRO)

m = mv('Cozinha', 'Coluna de eletrodoméstico',
       '104 × 275 × 60 · 2 portas em cima, vão aberto de 98 × 190 embaixo')
m.p('laterais de piso a teto', 60, 275, 15, qtd=2, fita_m=275 / 100)
m.p('tampo', 98, 60, 15, fita_m=98 / 100)
m.p('fundo do armário superior', 98, 60, 15, fita_m=98 / 100)
m.p('fundo do vão', 98, 190, 6)
m.p('fundo do armário de cima', 98, 80, 6)
m.p('porta 49 × 80', 49, 80, 15, qtd=2, fita_m=(49 + 80) * 2 / 100)
m.f('Dobradiça', 2 * b.dobradicas(80), b.DOBRADICA)
m.t('Cava usinada', 0.98, b.CAVA_M)

m = mv('Gourmet', 'Armário complementar com portas de vidro',
       '102 × 86 × 25 (⚠ profundidade NÃO cotada) · 2 portas de VIDRO')
m.p('tampo', 102, 25, 15, fita_m=102 / 100)
m.p('base', 102, 25, 15, fita_m=102 / 100)
m.p('laterais', 25, 71, 15, qtd=2, fita_m=71 / 100)
m.p('fundo', 94, 71, 6)
m.p('prateleira', 94, 25, 18, fita_m=94 / 100)
m.v('Porta de vidro reflecta 47 × 71', 2)
m.f('Dobradiça de porta de vidro', 2 * b.dobradicas(71), b.DOBRADICA_VIDRO)
m.f('Suporte oculto de prateleira', 2, b.SUPORTE_PRAT)

m = mv('Cozinha', 'Painel ripado do corredor',
       '626 × 272 × 3 · o maior item do projeto')
N_RIP_COZ = painel_ripado(m, 626 - 2 * 87, 272)      # o painel fixo, sem as portas

for amb, qual in (('Vestiário', 'vestiário'), ('Despensa', 'despensa')):
    m = mv('Cozinha', f'Porta de correr ripada · {qual}', '87 × 272 · 29 passos exatos')
    painel_ripado(m, 87, 272, atras=True)
    #   ⭐ [Jonathan 03/11] o sistema agora é por LINHA: Rometal de 600 na
    #     Hettich e SI Forma de 900 na Blum. O preço entra aqui como o da
    #     Hettich e `cenarios.py` troca por linha — é a ÚNICA ferragem deste
    #     projeto, além da corrediça, que muda entre os dois cenários.
    #   ⚠ UM CONJUNTO POR PORTA: vestiário e despensa são vãos separados, cada
    #     um com o seu trilho. Não é um kit de duas folhas dividindo trilho.
    m.f('Sistema de correr', 1, 600.0)
    m.f('Desempenador de porta', 2, 100.0)

m = mv('Cozinha', 'Cristaleira', '147 × 275 × 54 · fundo RIPADO · 2 portas de VIDRO')
m.p('laterais', 54, 269, 15, qtd=2, fita_m=269 / 100)
m.p('tampo', 144, 54, 15, fita_m=144 / 100)
m.p('base', 144, 54, 15, fita_m=144 / 100)
m.p('rodapé', 144, 3, 15, fita_m=144 / 100)
m.p('prateleiras de 44', 140, 44, 18, qtd=5, fita_m=140 / 100)
m.p('caixa da base · frente', 100, 30, 15, fita_m=(100 + 30) * 2 / 100)
m.p('caixa da base · laterais', 39, 30, 15, qtd=2)
m.p('caixa da base · fundo e tampo', 100, 39, 15, qtd=2)
painel_ripado(m, 147, 269)                    # ⭐ o fundo inteiro é ripado
m.v('Porta de vidro reflecta 70 × 269', 2)
m.f('Dobradiça de porta de vidro', 2 * b.dobradicas(269), b.DOBRADICA_VIDRO)
m.f('Suporte oculto de prateleira', 5 * 4, b.SUPORTE_PRAT)
#   ⭐ prateleira de 140 de vão pede alma de aço: a regra da casa é acima de
#     120 cm, e a Base manda uma barra por peça.
m.f('Alma de aço, barra de 3 m', 5, b.ALMA_BARRA)
m.f('Corrediça da caixa da base', 1, b.CORREDICA_PAR)

# ════════════════════════════════════════════════════════════════════════
# ESCRITÓRIO
# ════════════════════════════════════════════════════════════════════════
m = mv('Escritório', 'Painel ripado de fundo',
       '316 × 272 · ⚠ orçado pela área APARENTE, 4,25 m²')
#   ⚠⚠ A PRANCHA NÃO DIZ SE O RIPADO PASSA ATRÁS DOS ARMÁRIOS. Parede
#     inteira = 8,60 m²; aparente = 4,25 m². Orço o aparente com a base
#     contínua por trás — a base TEM de ser contínua, é nela que o armário
#     se fixa. São 4,35 m² de diferença no item mais caro.
m.p('base contínua do painel', 316, 272, BASE_ESP)
for larg, alt in ((60, 272), (46, 204), (190, 60), (20, 272)):
    n = ripas_em(larg)
    m.p(f'{n} ripas de {RIPA_L:g} × {alt:g}', RIPA_L * n * b.RIPA_PERDA, alt, 18)
    m.fita += n * alt / 100 * 2
    m.fita_ripa += n * alt / 100 * 2
    m.t('Filetagem manual de ripa', round(n * alt / 100 * 2, 1), b.FILETE_MAO)
m.t('Painel ripado, mão de obra', 4.25, b.RIPADO_M2)

m = mv('Escritório', 'Armário superior', '190 × 80 × 32, suspenso a 135 · 4 portas')
m.p('tampo', 190, 32, 15, fita_m=190 / 100)
m.p('base', 190, 32, 15, fita_m=190 / 100)
m.p('laterais', 32, 80, 15, qtd=2, fita_m=80 / 100)
m.p('divisória central', 32, 80, 15, fita_m=80 / 100)
m.p('fundo', 190, 80, 6)
m.p('porta 47,5 × 80', 47.5, 80, 15, qtd=4, fita_m=(47.5 + 80) * 2 / 100)
m.f('Dobradiça', 4 * b.dobradicas(80), b.DOBRADICA)
m.t('Cava usinada', 1.90, b.CAVA_M)

m = mv('Escritório', 'Bancada e mesa', 'tampo de 216 × 100 a 75 do piso')
#   ⛔ A espessura NÃO É COTADA: os ~4 cm saem da diferença 75 − 71. E a
#     Base não vende chapa de COR em 25 mm — Melamínico Fosco só tem 6, 15 e
#     18. Tampo grosso não se compra, SE DOBRA: duas de 18 coladas dão 36 mm,
#     que é o que a fábrica faz e o que mais se aproxima dos ~4 cm lidos.
m.p('tampo da mesa · duas chapas coladas', 216, 100, 18, qtd=2,
    fita_m=(216 + 100) * 2 / 100)
m.p('tampo sobre o armário', 236, 60, 18, fita_m=236 / 100)

m = mv('Escritório', 'Armário inferior', '236 × 68 × 60 · 2 portas, 2 frentes, gaveteiro')
m.p('laterais', 60, 68, 15, qtd=2, fita_m=68 / 100)
m.p('divisórias', 60, 68, 15, qtd=3, fita_m=68 / 100)
m.p('base', 228, 60, 15, fita_m=228 / 100)
m.p('rodapé recuado', 228, 3, 15, fita_m=228 / 100)
m.p('fundo', 228, 68, 6)
m.p('porta de 50', 50, 68, 15, qtd=2, fita_m=(50 + 68) * 2 / 100)
m.p('frente de 34', 34, 68, 15, qtd=2, fita_m=(34 + 68) * 2 / 100)
for h in (16, 30, 20):
    m.p(f'frente de gaveta {h}', 60, h, 15, fita_m=(60 + h) * 2 / 100)
    m.p(f'caixa da gaveta {h} · lateral', 55, h, 15, qtd=2)
    m.p(f'caixa da gaveta {h} · traseira', 56, h, 15)
    m.p(f'caixa da gaveta {h} · fundo', 56, 55, 6)
m.f('Dobradiça', (2 + 2) * b.dobradicas(68), b.DOBRADICA)
m.f('Corrediça', 3, b.CORREDICA_PAR)
m.t('Cava usinada', 2.28, b.CAVA_M)

# ════════════════════════════════════════════════════════════════════════
# SALA DE TV
# ════════════════════════════════════════════════════════════════════════
m = mv('Sala de TV', 'Painel ripado',
       '353,5 × 272 × 3 · a ripa para onde o rack e a pedra cobrem')
#   ⭐ [Jonathan 03/11] o ripado não corre atrás do que o cobre. Aqui são
#     três faixas, porque o que cobre está em alturas diferentes:
#       0 → 253,5   livre, ripa inteira de 272
#       253,5 → 303,5  o rack toma os 70 de baixo → ripa de 202
#       303,5 → 353,5  rack (70) e travertino (70 a 210) → ripa de 62
m.p('base contínua do painel', 353.5, 272, BASE_ESP)
for larg, alt in ((253.5, 272), (50, 202), (50, 62)):
    n = ripas_em(larg)
    m.p(f'{n} ripas de {RIPA_L:g} × {alt:g}', RIPA_L * n * b.RIPA_PERDA, alt, 18)
    m.fita += n * alt / 100 * 2
    m.fita_ripa += n * alt / 100 * 2
    m.t('Filetagem manual de ripa', round(n * alt / 100 * 2, 1), b.FILETE_MAO)
m.t('Painel ripado, mão de obra',
    round((253.5 * 272 + 50 * 202 + 50 * 62) / 10000, 2), b.RIPADO_M2)

m = mv('Sala de TV', 'Painel liso', '300 × 272 × 2 · com recorte para a pedra')
m.p('painel liso', 300, 272, 15, fita_m=(300 + 272) * 2 / 100)
#   ⛔ O recorte de 300 × 140 é onde entra o travertino, que NÃO é nosso.
#     A chapa, porém, se compra inteira: o recorte não devolve material.

m = mv('Sala de TV', 'Rack de TV', '400 × 70 × 40 · 4 gavetões de 100 × 30')
m.p('tampo', 400, 40, 15, fita_m=400 / 100)
m.p('base', 400, 40, 15, fita_m=400 / 100)
m.p('laterais', 40, 70, 15, qtd=2, fita_m=70 / 100)
m.p('divisórias', 40, 70, 15, qtd=3, fita_m=70 / 100)
m.p('fundo', 400, 70, 6)
m.p('faixa cega superior', 400, 20, 15, fita_m=400 / 100)
m.p('faixa cega inferior', 400, 17, 15, fita_m=400 / 100)
m.p('frente de gavetão', 100, 30, 15, qtd=4, fita_m=(100 + 30) * 2 / 100)
m.p('caixa do gavetão · lateral', 35, 30, 15, qtd=8)
m.p('caixa do gavetão · traseira', 96, 30, 15, qtd=4)
m.p('caixa do gavetão · fundo', 96, 35, 6, qtd=4)
m.f('Corrediça', 4, b.CORREDICA_PAR)
m.t('Cava usinada nos 4 gavetões', 4.00, b.CAVA_M)

# ════════════════════════════════════════════════════════════════════════
# SUÍTE
# ════════════════════════════════════════════════════════════════════════
m = mv('Suíte', 'Painel ripado da cabeceira', '200 × 272 × 3')
painel_ripado(m, 200, 272)

m = mv('Suíte', 'Parede painelada da TV', '467 × 275 × 2 · bandeira contínua de 65')
m.p('testeira esquerda', 9, 275, 15, fita_m=275 / 100)
m.p('testeira direita', 18, 275, 15, fita_m=275 / 100)
m.p('bandeira contínua', 439, 65, 15, fita_m=(439 + 65) * 2 / 100)
m.p('módulo central da TV', 256, 207, 15, fita_m=(256 + 207) * 2 / 100)
#   ⭐ 3 cm de prateleira = duas de 15 coladas, exato.
m.p('prateleira de 198 · duas chapas coladas', 198, 28, 15, qtd=2,
    fita_m=(198 + 28) * 2 / 100)
m.f('Alma de aço, barra de 3 m', 1, b.ALMA_BARRA)
#   ⭐ 198 de vão passa de longe dos 120 da regra da casa.
m.p('folha da porta de giro', 80, 207, 15, fita_m=(80 + 207) * 2 / 100)
m.p('folha da porta pivotante', 100, 207, 15, fita_m=(100 + 207) * 2 / 100)
m.f('Dobradiça da porta de giro', b.dobradicas(207), b.DOBRADICA)
m.f('Sistema pivô', 1, 120.0)
m.t('Cava usinada nas duas folhas', 1.80, b.CAVA_M)

# ⭐ RESOLVIDO em 03/11: as duas portas da suíte SÃO nossas e já estão
#   lançadas acima, como folha de MDF mais ferragem. O bloco abaixo fica só
#   como registro do que era a dúvida.
# ⚠⚠ ERA A PENDÊNCIA:
#   Estão hachuradas como MDF, o que pela legenda as faz nossas, e pelo teste
#   da casa (sai no mesmo caminhão?) também. Mas são porta de PASSAGEM, e a
#   obra pode já tê-las comprado. A Base tem o preço pronto: giro de 80 a
#   R$ 530 e pivô — o maior da tabela é 90 a R$ 840. Em vez de lançar a zero,
#   que é o que a REGRA DOS DOIS ESTADOS proíbe, ficam nomeadas na pendência.
PORTAS_SUITE = [('Porta de giro pronta, 80 cm', 1, 530.0),
                ('Porta pivô pronta, 90 cm (⚠ a folha é 100)', 1, 840.0),
                ('Sistema pivô', 1, 120.0)]


# ════════════════════════════════════════════════════════════════════════
# A CONTA
# ════════════════════════════════════════════════════════════════════════
def custo():
    area, fita, fita_ripa, ferr, terc, vidro = {}, 0.0, 0.0, 0.0, 0.0, 0.0
    for m in M:
        for k, v in m.areas().items():
            area[k] = area.get(k, 0.0) + v
        fita += m.fita
        fita_ripa += m.fita_ripa
        ferr += sum(q * u for _n, q, u in m.ferr)
        terc += sum(q * u for _n, q, u in m.terc)
        vidro += sum(q * u for _n, q, u in m.vidro)
    chapas, c_chapa = {}, 0.0
    for (mat, esp), a in sorted(area.items()):
        n = b.chapas(a)
        chapas[(mat, esp)] = (a, n)
        c_chapa += n * b.PRECO[f'{mat} {esp}']
    c_fita = fita * b.FITA_COR * b.FITA_PERDA
    #   ⭐ a filetagem de máquina cobre tudo o que NÃO é ripa
    fita_maq = fita - fita_ripa
    terc += fita_maq * b.FILETE_MAQ
    cons = (c_chapa + c_fita) * b.CONSUMIVEIS
    direto = c_chapa + c_fita + cons + ferr + terc + vidro
    emb = direto * b.EMBALAGEM
    return dict(area=area, chapas=chapas, c_chapa=c_chapa, fita=fita,
                fita_ripa=fita_ripa, fita_maq=fita_maq,
                c_fita=c_fita, cons=cons, ferr=ferr, terc=terc, vidro=vidro,
                emb=emb, direto=direto + emb)


PREMISSAS = [
 'Passo da ripa 3 cm — o detalhe 1:5 cotado, não a hachura da elevação (5 cm).',
 'Ripado do escritório orçado pela área APARENTE (4,25 m²), com base contínua '
 'atrás. Se correr atrás dos armários, são 8,60 m².',
 'Base do ripado em MDF 15 mm — a prancha cota 1 cm, que não é espessura comercial.',
 'Profundidade do armário gourmet: 25 cm, lida da cadeia do existente. Não é cotada.',
 'Tampo da mesa em duas chapas de 18 coladas (36 mm) — a espessura não é\n cotada e a Base não tem chapa de cor em 25 mm.',
 'Sistema de correr RO65 (R$ 100) nas duas portas ripadas. A prancha não '
 'especifica; na Base vai até R$ 800 o Dominus.',
 'Vidro reflecta PRATA com perfil — o executivo pede "cristal", que não '
 'existe na Base de Custos.',
 'Dobradiça Bigfer Onix a R$ 15 — a Base nunca cravou a do nível Padrão.',
 'Aparador com 3 BÁSCULAS (articulador Blum), não portas de giro: o símbolo '
 'é triângulo, e o escritório usa X e "<" para giro na mesma família.',
 'Sem RT de arquiteta e sem vendedor — BASE de 84,88%.',
 'Sem iluminação: não há uma única indicação de LED em nenhuma das 11 pranchas.',
 'Frete não entra: a Base deixou as quatro linhas de frete vazias de propósito.',
]

if __name__ == '__main__':
    c = custo()
    print('═' * 72)
    print('ATTOS · COSTA LAGUNA — QUANTITATIVO')
    print('═' * 72)
    for (mat, esp), (a, n) in sorted(c['chapas'].items()):
        print(f'  {mat} {esp:>2} mm   {a:7.2f} m²  →  {n:2d} chapa(s)   '
              f'R$ {n * b.PRECO[f"{mat} {esp}"]:>9,.2f}')
    print(f'\n  fita de borda           {c["fita"]:7.1f} m   '
          f'R$ {c["c_fita"]:>9,.2f}   (com os 10% de desperdício)')
    print(f'    da qual, ripa (manual) {c["fita_ripa"]:7.1f} m'
          f'   · caixa (máquina) {c["fita_maq"]:7.1f} m')
    print(f'  chapa                                 R$ {c["c_chapa"]:>9,.2f}')
    print(f'  consumíveis, 6%                       R$ {c["cons"]:>9,.2f}')
    print(f'  ferragem                              R$ {c["ferr"]:>9,.2f}')
    print(f'  terceirizados                         R$ {c["terc"]:>9,.2f}')
    print(f'  vidro                                 R$ {c["vidro"]:>9,.2f}')
    print(f'  embalagem, 2%                         R$ {c["emb"]:>9,.2f}')
    print(f'  {"─"*54}')
    print(f'  CUSTO DIRETO                          R$ {c["direto"]:>9,.2f}')
    _cond = {b.BASE_SEM_RT: 'sem RT e sem vendedor',
             b.BASE_COM_UM: 'com RT OU com vendedor',
             b.BASE_COM_DOIS: 'com RT E com vendedor'}[b.BASE]
    print(f'\n  BASE {b.BASE:.2%} · {_cond}')
    for mc in (0.35, 0.38, 0.40):
        print(f'    MC {mc:.0%}  →  PREÇO  R$ {b.preco(c["direto"], mc):>12,.2f}')
    print(f'\n  ⚠ fora da conta, à espera de decisão:')
    for n, q, u in PORTAS_SUITE:
        print(f'      {n:<42} {q} × R$ {u:,.2f}')
    # ── por ambiente, para saber onde está o dinheiro ────────────────
    print('\n' + '═' * 72)
    print('ONDE ESTÁ O CUSTO')
    print('═' * 72)
    amb = {}
    for m in M:
        ar = sum(L * A * q / 10000 for _n, L, A, _e, _m, q in m.pecas)
        cf = (m.fita * b_.FITA_COR * b_.FITA_PERDA
              + m.fita_ripa * b_.FILETE_MAO
              + (m.fita - m.fita_ripa) * b_.FILETE_MAQ)
        cu = (sum(q * u for _n, q, u in m.ferr)
              + sum(q * u for _n, q, u in m.terc if 'Filetagem' not in _n)
              + sum(q * u for _n, q, u in m.vidro) + cf)
        d = amb.setdefault(m.amb, [0.0, 0.0, 0])
        d[0] += ar; d[1] += cu; d[2] += 1
    for k, (ar, cu, n) in sorted(amb.items(), key=lambda t: -t[1][1]):
        print(f'  {k:<13} {n:2d} móveis · {ar:7.2f} m² de peça · '
              f'R$ {cu:>10,.2f} de fita, ferragem e serviço')

    # ⭐⭐ A PROVA DE SANIDADE DO RIPADO — a conta decomposta contra o preço
    #   de job. Estimar é CONFERÊNCIA do cálculo, nunca o número entregue.
    m2_rip = sum(q for m in M for _n, q, u in m.terc
                 if _n.startswith('Painel ripado'))
    decomp = m2_rip * b_.RIPADO_M2 + c['fita_ripa'] * b_.FILETE_MAO
    print('\n' + '═' * 72)
    print('PROVA DE SANIDADE DO RIPADO')
    print('═' * 72)
    print(f'  {m2_rip:.2f} m² de painel ripado · {c["fita_ripa"]:.0f} m de fita de ripa')
    print(f'  calculado, peça a peça:  R$ {decomp:>10,.2f}  '
          f'= {m2_rip:.1f} m² × 180 + {c["fita_ripa"]:.0f} m × 5')
    print(f'  preço de job no topo da faixa da Base (420/m²): '
          f'R$ {m2_rip * 420:>10,.2f}')
    print(f'  → por m² de painel, o calculado dá R$ {decomp / m2_rip:,.2f}')
    print('  ⭐ A Base avisa que a faixa vai de 70 a 420 e "depende da largura')
    print('    da ripa e do vão". Com ripa de 2 e vão de 1 — passo de 3 — a')
    print('    conta decomposta cai no TOPO da faixa, não no meio. É a prova')
    print('    de que o R$ 180/m² sozinho subestimaria este painel.')

    print(f'\n  {len(M)} móveis · {sum(len(m.pecas) for m in M)} linhas de peça')
