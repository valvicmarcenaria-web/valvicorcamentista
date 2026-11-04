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

# ⭐⭐ OS ÍNDICES DA TUPLA DE PEÇA, COM NOME. A tupla já cresceu duas vezes
#   nesta sessão (ganhou a fita e depois o `mao`), e cada vez que ela cresce
#   TODO desempacotamento por posição escorrega uma casa — em silêncio, sem
#   erro, devolvendo outro número. Quem lê a peça lê por estes nomes.
I_NOME, I_L, I_A, I_ESP, I_MAT, I_QTD, I_FITA, I_OBS, I_MAO = range(9)

#   ⛔⛔ A REGRA QUE EU QUEBREI EM VINTE E DUAS LINHAS [Jonathan, 04/11/2026]:
#     "o rack tem 308cm de comprimento / vc deveria ter criado 2 peças para o
#     teto e base ou 3 acompanhando as divisoes das portas para nao ficar com
#     um tampo dividido no meio da porta".
#   ⭐ PEÇA INTEIRA VAI ATÉ 273 — a chapa de 275 menos o acerto de corte. É a
#     regra 9 da casa, está escrita na skill, e eu lancei tampo de 308, de 400
#     e bandeira de 439 como peça única. Peça que não existe.
#   ⭐ E A EMENDA NÃO ESCOLHE ONDE CAI: ela cai na DIVISÓRIA, que é onde as
#     frentes se encontram. O critério é o MENOR número de peças cujas juntas
#     caiam TODAS numa divisória — duas quando dá, três quando duas não dão.
#   ⛔⛔ A TRAVA ESTÁ NO FIM DESTE ARQUIVO, e é ela que faz isso não voltar.
PECA_INTEIRA = 273.0
DOBR_NORMAL = (
    '⭐ [Jonathan, 04/11/2026] "as dobradiças do item 3, sao normais" · folha de vidro COM PERFIL: a dobradiça parafusa no perfil, não no vidro — dobradiça comum de R$ 50, não a de vidro')

#   ⭐ O MARCADOR DE ÁREA. Algumas linhas não são peça de corte: são a ÁREA
#     EQUIVALENTE de um conjunto, lançada numa linha só para o m² fechar. A
#     tira de ripas é a única: cada ripa tem 2 × 272 e cabe folgado na chapa;
#     o que passa de 273 é a SOMA das larguras, que nunca vai para a serra
#     como peça. A trava pula quem está marcado assim.
AREA = '⭐ ÁREA EQUIVALENTE, não peça de corte'

#   ⛔⛔ AS EXCEÇÕES, UMA A UMA, COM O MOTIVO — e nenhuma delas é "esqueci".
#     Peça de 275 é o comprimento CHEIO da chapa: sai sem acerto de corte, ou
#     pede 2 cm de rodapé/sanca por cima. É decisão de obra, e está como
#     dúvida numerada na aba do ambiente.
ACIMA_DE_273 = {
    ('Cozinha', 'Coluna de eletrodoméstico', 'laterais de piso a teto'):
        'lateral de piso a teto de 275 · o comprimento CHEIO da chapa',
    ('Suíte', 'Parede painelada da TV', 'testeira esquerda'):
        'testeira de 275 · o comprimento CHEIO da chapa',
    ('Suíte', 'Parede painelada da TV', 'testeira direita'):
        'testeira de 275 · o comprimento CHEIO da chapa',
}


def faixas(largura, limite=None):
    """⭐ AS FAIXAS DE UM PAINEL CONTÍNUO. Painel de 272 de altura sai na
       dimensão de 275 da chapa, logo a faixa tem no máximo os 185 do outro
       lado. 452 vira 185 + 185 + 82 — e as juntas ficam ESCONDIDAS ATRÁS DAS
       RIPAS, que é o motivo de o painel ripado poder ser emendado onde a
       produção quiser. ⛔ No painel LISO não há ripa para esconder, e aí a
       junta é decisão de projeto: veja a dúvida da aba."""
    #   ⛔⛔ E A DIVISÃO É IGUAL, NÃO GULOSA. Encher de 185 e deixar o resto
    #     daria 185 + 15 num painel de 200 — e tira de 15 cm é desperdício de
    #     chapa e peça frágil de manusear. Divide-se pelo MENOR número de
    #     faixas que cabem, todas do mesmo tamanho: 200 vira 100 + 100, 452
    #     vira três de 150,67, e 300 vira 150 + 150, que põe a junta no meio.
    import math as _m
    lim = limite or b.CHAPA_L
    n = max(1, _m.ceil(round(largura / lim, 6)))
    return [round(largura / n, 2)] * n


class Movel:
    def __init__(self, amb, nome, nota=''):
        self.amb, self.nome, self.nota = amb, nome, nota
        self.pecas, self.fita, self.ferr, self.terc, self.vidro = [], 0.0, [], [], []
        self.fita_ripa = 0.0      # ⭐ a da ripa é MANUAL; o resto é máquina
        self.espec = {}           # ⭐ ESPECIFICAÇÃO por linha de ferragem

    def p(self, nome, L, A, esp, mat=COR, qtd=1, fita_m=0.0, obs='',
          mao=False):
        """Uma peça: L × A em cm, espessura em mm, material e quantas.

        ⭐ A FITA DESCE PARA A PEÇA. Antes ela só existia somada no móvel, e
          por isso o plano de corte não sabia dizer quantos metros de fita
          cada peça leva — que é a pergunta da coladeira. `fita_m` é por
          UNIDADE; quem multiplica pela quantidade é quem lê.
        """
        self.pecas.append((nome, L, A, esp, mat, qtd, fita_m, obs, mao))
        self.fita += fita_m * qtd
        #   ⭐⭐ E A FITA DE MÃO TAMBÉM DESCE PARA A PEÇA. Antes a fita da
        #     ripa era somada no móvel por fora, e por isso o bloco de peças
        #     da planilha não sabia dizer de QUAL peça vinham os 2.595 m de
        #     filetagem manual — 92% de toda a fita do projeto num número
        #     órfão. Agora ela mora na peça que a consome.
        if mao:
            self.fita_ripa += fita_m * qtd
        return self

    def f(self, nome, qtd, unit, obs=''):
        #   ⭐ `obs` vai para a coluna ESPECIFICAÇÃO da linha, que antes saía
        #     sempre '—'. É onde a DECISÃO fica à vista de quem produz: sem
        #     isso, "dobradiça comum numa porta de vidro" parece um erro de
        #     digitação em vez de uma escolha registrada.
        self.ferr.append((nome, qtd, unit))
        if obs: self.espec[nome] = obs
        return self

    def t(self, nome, qtd, unit, obs=''):
        self.terc.append((nome, qtd, unit))
        if obs: self.espec[nome] = obs
        return self

    def v(self, nome, folhas, unit=None):
        self.vidro.append((nome, folhas, unit or b.VIDRO_FOLHA)); return self

    def areas(self):
        """m² por (material, espessura)."""
        d = {}
        for _n, L, A, esp, mat, q, *_ in self.pecas:
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


def base_em_faixas(m, largura, altura):
    """⛔ 452 de base NÃO SAI de chapa de 275: sai em FAIXAS. E aqui a junta é
       livre, porque a ripa passa por cima e esconde — é o que permite emendar
       um painel ripado onde a produção quiser. ⭐ Uma faixa só quando cabe."""
    fx = faixas(largura)
    if len(fx) == 1:
        m.p('base contínua do painel', largura, altura, BASE_ESP)
        return
    for i, w in enumerate(fx, 1):
        m.p(f'base do painel · faixa {i} de {len(fx)}', w, altura, BASE_ESP,
            obs=f'junta escondida atrás da ripa · {len(fx)} faixas somando '
                f'{largura:g} cm')


def painel_ripado(m, largura, altura, atras=True):
    """A base contínua + as ripas + a mão de obra de ripado."""
    n = ripas_em(largura)
    area_rip = n * (RIPA_L / 100) * (altura / 100)
    if atras:
        base_em_faixas(m, largura, altura)
    #   ⛔ A FITA DA RIPA É O MAIOR METRO DO PROJETO: cada ripa leva fita nas
    #     duas arestas que ficam à vista, e é filetagem MANUAL, porque ripa
    #     de 2 cm não entra na coladeira.
    m.p(f'{n} ripas de {RIPA_L:g} × {altura:g}', RIPA_L * n * b.RIPA_PERDA,
        altura, 18, fita_m=n * altura / 100 * 2, mao=True,
        obs=f'{AREA} · ripa de {RIPA_L:g} cm, vão de {VAO:g}, passo de '
            f'{PASSO:g} · cada ripa tem {RIPA_L:g} × {altura:g} e cabe na '
            f'chapa; o que passa de 273 é a SOMA das {n} larguras · fita nas '
            f'DUAS arestas à vista, {n} × 2 × {altura:g} cm')
    #   ⭐ a perda de serra entra na LARGURA da peça equivalente, que é onde
    #     ela acontece de verdade: cada corte come lâmina.
    m.t('Painel ripado, mão de obra', largura * altura / 10000, b.RIPADO_M2)
    m.t('Filetagem manual de ripa', n * altura / 100 * 2, b.FILETE_MAO)
    #   ⛔ E SEM `round()` AQUI. Arredondar no LANÇAMENTO criava um segundo
    #     número: o `custo()` cobrava a metragem arredondada e o
    #     `custo_por_ambiente()` a cheia, e os dois motores passaram a
    #     divergir em 71 centavos. Quem arredonda é a TELA, nunca a conta.
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
#   ⛔⛔ 308 NÃO SAI DE CHAPA DE 275, E A EMENDA NÃO ESCOLHE ONDE CAI
#     [Jonathan, 04/11/2026]: "o rack tem 308cm de comprimento / vc deveria
#     ter criado 2 peças para o teto e base ou 3 acompanhando as divisoes das
#     portas para nao ficar com um tampo dividido no meio da porta".
#     Eu havia lançado tampo, base e fundo como peça ÚNICA de 308 — peça que
#     NÃO EXISTE. A chapa é 275 × 185 e a peça inteira vai até 273.
#   ⭐ A REGRA QUE EU DEVIA TER APLICADO: o menor número de peças cujas juntas
#     caiam TODAS numa divisória. As frentes são 102 + 102 + 104 = 308, logo as
#     divisórias ficam em 102 e em 204. Duas peças de 204 e 104 põem a única
#     junta em 204, atrás do vão entre a segunda e a terceira basculante —
#     apoiada na divisória e escondida no rasgo. Emenda no meio de uma porta é
#     defeito à vista; emenda no vão não se vê.
m.p('tampo · da lateral à divisória de 204', 204, 45, 15,
    fita_m=(204 + 45) * 2 / 100)
m.p('tampo · da divisória de 204 à lateral', 104, 45, 15,
    fita_m=(104 + 45) * 2 / 100)
m.p('base · da lateral à divisória de 204', 204, 45, 15,
    fita_m=(204 + 45) * 2 / 100)
m.p('base · da divisória de 204 à lateral', 104, 45, 15,
    fita_m=(104 + 45) * 2 / 100)
m.p('laterais', 45, 50, 15, qtd=2, fita_m=(45 + 50) * 2 / 100)
#   ⛔⛔ E AS DIVISÓRIAS NÃO ESTAVAM NA LISTA. Um aparador de 308 com três
#     basculantes não tem onde parafusar articulador nem onde apoiar tampo:
#     são DUAS divisórias, em 102 e em 204, e a de 204 é que recebe a emenda.
m.p('divisórias em 102 e em 204', 45, 50, 15, qtd=2, fita_m=50 / 100)
m.p('divisória sob a gaveta', 60, 41, 15, fita_m=60 / 100)
m.p('fundo · nos dois vãos de 102', 100, 46, 6, qtd=2)
m.p('fundo · no vão de 104', 102, 46, 6)
m.p('frente basculante 102', 102, 50, 15, qtd=2, fita_m=(102 + 50) * 2 / 100)
m.p('frente basculante 104', 104, 50, 15, fita_m=(104 + 50) * 2 / 100)
m.p('gaveta interna · caixa', 60, 10, 15, qtd=2, fita_m=60 / 100)
m.p('gaveta interna · lateral', 31, 10, 15, qtd=2)
m.p('gaveta interna · fundo', 60, 31, 6)
#   ⛔⛔ BÁSCULA NÃO LEVA DOBRADIÇA, LEVA ARTICULADOR. O triângulo com base
#     embaixo e vértice no topo é báscula; o escritório, na MESMA família de
#     pranchas, marca giro com X e com "<". Três articuladores a R$ 250 são
#     R$ 750 onde a dobradiça seriam R$ 90.
m.f('Articulador Blum AVENTOS HK-XS', 3, b.BASCULA_HK)
m.f('Corrediça da gaveta interna', 1, b.CORREDICA_PAR)
m.t('Cava usinada nas 3 frentes', 3.08, b.CAVA_M)

# ════════════════════════════════════════════════════════════════════════
# COZINHA
# ════════════════════════════════════════════════════════════════════════
m = mv('Cozinha', 'Armário superior com portas de vidro',
       '283 × 125 × 35, suspenso a 150 · 4 portas de VIDRO')
#   ⛔ MESMO DEFEITO DO APARADOR: 283 não sai de chapa de 275. São 4 portas
#     de 70,8, logo três divisórias internas, em 70,75 · 141,5 · 212,25 —
#     e DUAS peças de 141,5 põem a única junta na divisória do MEIO.
m.p('tampo · metades com junta na divisória de 141,5', 141.5, 35, 15, qtd=2,
    fita_m=141.5 / 100)
m.p('base do corpo · metades com junta em 141,5', 141.5, 35, 15, qtd=2,
    fita_m=141.5 / 100)
m.p('laterais', 35, 100, 15, qtd=2, fita_m=100 / 100)
m.p('divisórias internas', 35, 100, 15, qtd=3, fita_m=100 / 100)
m.p('fundo · metades com junta em 141,5', 141.5, 100, 6, qtd=2)
m.p('faixa inferior de 21 · metades com junta em 141,5', 141.5, 21, 15, qtd=2,
    fita_m=(141.5 + 21) * 2 / 100)
m.p('tampo e fundo da faixa · metades com junta em 141,5', 141.5, 35, 15,
    qtd=4, fita_m=141.5 / 100)
m.v('Porta de vidro reflecta 70,8 × 95', 4)
m.f('Dobradiça das 4 portas de vidro com perfil', 4 * b.dobradicas(95),
    b.DOBRADICA, obs=DOBR_NORMAL)

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
m.f('Dobradiça das 2 portas de vidro com perfil', 2 * b.dobradicas(71),
    b.DOBRADICA, obs=DOBR_NORMAL)
m.f('Suporte de prateleira', 1, b.SUPORTE_JOGO)   # 1 prateleira interna

m = mv('Cozinha', 'Painel ripado do corredor',
       '452 × 272 × 3 — o trecho FIXO. A parede tem 626; os dois vãos de '
       '87 são as portas, lançadas em separado logo abaixo')
N_RIP_COZ = painel_ripado(m, 626 - 2 * 87, 272)      # o painel fixo, sem as portas

for amb, qual in (('Vestiário', 'vestiário'), ('Despensa', 'despensa')):
    m = mv('Cozinha', f'Porta de correr ripada · {qual}',
       '87 × 272 · 29 passos exatos · faz parte dos 626 da parede')
    painel_ripado(m, 87, 272, atras=True)
    #   ⭐ [Jonathan 03/11] o sistema agora é por LINHA: Rometal de 600 na
    #     Hettich e SI Forma de 900 na Blum. O preço entra aqui como o da
    #     Hettich e `cenarios.py` troca por linha — é a ÚNICA ferragem deste
    #     projeto, além da corrediça, que muda entre os dois cenários.
    #   ⚠ UM CONJUNTO POR PORTA: vestiário e despensa são vãos separados, cada
    #     um com o seu trilho. Não é um kit de duas folhas dividindo trilho.
    m.f('Sistema de correr', 1, b.SISTEMA_CORRER)
    m.f('Desempenador de porta', 2, b.DESEMPENADOR)

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
m.f('Dobradiça das 2 portas de vidro com perfil', 2 * b.dobradicas(269),
    b.DOBRADICA, obs=DOBR_NORMAL)
m.f('Suporte de prateleira', 5, b.SUPORTE_JOGO)   # 5 prateleiras internas
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
base_em_faixas(m, 316, 272)
for larg, alt in ((60, 272), (46, 204), (190, 60), (20, 272)):
    n = ripas_em(larg)
    m.p(f'{n} ripas de {RIPA_L:g} × {alt:g}', RIPA_L * n * b.RIPA_PERDA, alt,
        18, fita_m=n * alt / 100 * 2, mao=True,
        obs=f'faixa de {larg:g} cm · passo de {PASSO:g} · fita {n} × 2 × {alt:g} cm')
    m.t('Filetagem manual de ripa', n * alt / 100 * 2, b.FILETE_MAO)
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
base_em_faixas(m, 353.5, 272)
for larg, alt in ((253.5, 272), (50, 202), (50, 62)):
    n = ripas_em(larg)
    m.p(f'{n} ripas de {RIPA_L:g} × {alt:g}', RIPA_L * n * b.RIPA_PERDA, alt,
        18, fita_m=n * alt / 100 * 2, mao=True,
        obs=f'faixa de {larg:g} cm · passo de {PASSO:g} · fita {n} × 2 × {alt:g} cm')
    m.t('Filetagem manual de ripa', n * alt / 100 * 2, b.FILETE_MAO)
m.t('Painel ripado, mão de obra',
    (253.5 * 272 + 50 * 202 + 50 * 62) / 10000, b.RIPADO_M2)

m = mv('Sala de TV', 'Painel liso', '300 × 272 × 2 · com recorte para a pedra')
#   ⛔⛔ E ESTE É O CASO QUE EU NÃO RESOLVO SOZINHA. 300 não sai de chapa de
#     275, então a emenda EXISTE — mas aqui não há ripa para esconder, e uma
#     linha vertical num painel liso de 3 metros é decisão de projeto, não de
#     produção. Lancei 185 + 115, que é o corte mais econômico, e pus a
#     pergunta como dúvida numerada na aba: a junta vai ao meio (150 + 150),
#     alinhada com a borda da pedra, ou atrás da TV?
m.p('painel liso · metades com junta no meio', 150, 272, 15, qtd=2,
    fita_m=(150 + 272) * 2 / 100,
    obs='⚠ emenda À VISTA · junta no MEIO, simétrica · a posição é dúvida '
        'de projeto, e não muda o preço')
#   ⛔ O recorte de 300 × 140 é onde entra o travertino, que NÃO é nosso.
#     A chapa, porém, se compra inteira: o recorte não devolve material.

m = mv('Sala de TV', 'Rack de TV', '400 × 70 × 40 · 4 gavetões de 100 × 30')
#   ⛔ MESMO DEFEITO, e aqui são 400 cm: quatro gavetões de 100, três
#     divisórias em 100 · 200 · 300. DUAS peças de 200 põem a única junta na
#     divisória do meio, no rasgo entre o segundo e o terceiro gavetão.
m.p('tampo · metades com junta na divisória de 200', 200, 40, 15, qtd=2,
    fita_m=200 / 100)
m.p('base · metades com junta em 200', 200, 40, 15, qtd=2, fita_m=200 / 100)
m.p('laterais', 40, 70, 15, qtd=2, fita_m=70 / 100)
m.p('divisórias', 40, 70, 15, qtd=3, fita_m=70 / 100)
m.p('fundo · metades com junta em 200', 200, 70, 6, qtd=2)
m.p('faixa cega superior · metades com junta em 200', 200, 20, 15, qtd=2,
    fita_m=200 / 100)
m.p('faixa cega inferior · metades com junta em 200', 200, 17, 15, qtd=2,
    fita_m=200 / 100)
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
#   ⛔⛔ AQUI DUAS PEÇAS NÃO RESOLVEM, e é o caso que o Jonathan previu com
#     "ou 3 acompanhando as divisões". A bandeira tem 439 e as divisões vêm do
#     que está embaixo dela: porta de giro de 80, módulo central de 256, porta
#     pivotante de 103. Cortar em dois daria 80 + 359 ou 336 + 103 — e 359 e
#     336 passam dos 273. São TRÊS peças, uma por vão, com as juntas em 80 e
#     em 336, cada uma apoiada na sua divisória.
m.p('bandeira · sobre a porta de giro', 80, 65, 15, fita_m=(80 + 65) * 2 / 100)
m.p('bandeira · sobre o módulo central', 256, 65, 15,
    fita_m=(256 + 65) * 2 / 100)
m.p('bandeira · sobre a porta pivotante', 103, 65, 15,
    fita_m=(103 + 65) * 2 / 100)
m.p('módulo central da TV', 256, 207, 15, fita_m=(256 + 207) * 2 / 100)
#   ⭐ 3 cm de prateleira = duas de 15 coladas, exato.
m.p('prateleira de 198 · duas chapas coladas', 198, 28, 15, qtd=2,
    fita_m=(198 + 28) * 2 / 100)
m.f('Alma de aço, barra de 3 m', 1, b.ALMA_BARRA)
#   ⭐ 198 de vão passa de longe dos 120 da regra da casa.
m.p('folha da porta de giro', 80, 207, 15, fita_m=(80 + 207) * 2 / 100)
m.p('folha da porta pivotante', 100, 207, 15, fita_m=(100 + 207) * 2 / 100)
m.f('Dobradiça da porta de giro', b.dobradicas(207), b.DOBRADICA)
m.f('Sistema pivô', 1, b.SISTEMA_PIVO)
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
    #   ⛔⛔ A CHAPA SE CONTA POR AMBIENTE, NÃO PELO PROJETO. Contar o
    #     projeto inteiro de uma vez dá 43 chapas; contar ambiente a ambiente
    #     dá 51, porque a sobra de um raramente serve o vizinho — e é assim
    #     que a casa compra e que as outras planilhas mostram. Dois métodos
    #     para a mesma chapa é a divergência que não dá erro.
    area_amb = {}
    for m in M:
        d = area_amb.setdefault(m.amb, {})
        for k, v in m.areas().items():
            d[k] = d.get(k, 0.0) + v
    chapas, c_chapa = {}, 0.0
    for (mat, esp), a in sorted(area.items()):
        n = sum(b.chapas(d[(mat, esp)]) for d in area_amb.values()
                if (mat, esp) in d)
        chapas[(mat, esp)] = (a, n)
        c_chapa += n * b.PRECO[f'{mat} {esp}']
    c_fita = fita * b.FITA_COR * b.FITA_PERDA
    #   ⭐ a filetagem de máquina cobre tudo o que NÃO é ripa
    fita_maq = fita - fita_ripa
    terc += fita_maq * b.FILETE_MAQ
    #   ⛔ 6% SOBRE CHAPA, FITA E FILETAGEM. A Base escreve "sobre chapa e
    #     fita", e eu segui a letra — mas o orçamento do Gustavo prova a
    #     prática: na cozinha dele, 6% de (4.290 + 284,90) dá R$ 274,49 e a
    #     célula mostra R$ 290,06, que é 6% de (4.290 + 284,90 + 259,50).
    #     A filetagem entra. Quem manda é o que as outras planilhas fazem.
    c_filete = fita_maq * b.FILETE_MAQ + fita_ripa * b.FILETE_MAO
    cons = (c_chapa + c_fita + c_filete) * b.CONSUMIVEIS
    #   ⭐⭐ OS DOIS SERVIÇOS DE CORTE, que o Jonathan cravou por AMBIENTE.
    #     ⛔ `n_pecas` conta a PEÇA, não a linha: uma linha de 4 prateleiras
    #       são 4 peças na serra, e a serra cobra por peça.
    n_chapas = sum(n for _a, n in chapas.values())
    n_pecas = sum(q for m in M for _n, _L, _A, _e, _m2, q, *_ in m.pecas)
    corte = n_chapas * b.CORTE_CHAPA + n_pecas * b.CORTE_PECA
    direto = c_chapa + c_fita + cons + ferr + terc + vidro + corte
    emb = direto * b.EMBALAGEM
    return dict(area=area, chapas=chapas, c_chapa=c_chapa, fita=fita,
                corte=corte, n_chapas=n_chapas, n_pecas=n_pecas,
                fita_ripa=fita_ripa, fita_maq=fita_maq,
                c_fita=c_fita, cons=cons, ferr=ferr, terc=terc, vidro=vidro,
                emb=emb, direto=direto + emb)


# ⭐⭐ A TRAVA DO RIPADO: a soma do que foi lançado tem de bater com a
#   parede desenhada, centímetro a centímetro. Sem ela, "o painel e as
#   portas" vira 800 cm de ripado numa parede de 626 e ninguém vê.
# ════════════════════════════════════════════════════════════════════════
# ⛔⛔ A TRAVA DA PEÇA INTEIRA
# ════════════════════════════════════════════════════════════════════════
#   Esta trava existe porque NADA conferia isso, e por isso vinte e duas
#   linhas passaram: tampo de 308, de 400, bandeira de 439, base de painel de
#   452. Foi o Jonathan que viu, numa delas, olhando a aba. ⭐ Agora o
#   levantamento não importa se alguma peça não sair de uma chapa — e quem
#   quiser abrir exceção escreve o MOTIVO no ACIMA_DE_273, de propósito.
def _trava_peca_inteira():
    fora = []
    for _m in M:
        for _pc in _m.pecas:
            if _pc[I_OBS].startswith(AREA):
                continue
            if max(_pc[I_L], _pc[I_A]) <= PECA_INTEIRA:
                continue
            if (_m.amb, _m.nome, _pc[I_NOME]) in ACIMA_DE_273:
                continue
            fora.append(f'{_m.amb} · {_m.nome} · {_pc[I_NOME]} '
                        f'({_pc[I_L]:g} × {_pc[I_A]:g})')
    assert not fora, ('⛔⛔ PEÇA QUE NÃO SAI DE UMA CHAPA DE 275 × 185:\n  '
                      + '\n  '.join(fora)
                      + '\n⭐ Divida nas DIVISÓRIAS, ou declare a exceção com '
                        'o motivo em ACIMA_DE_273.')


_trava_peca_inteira()

_RIP_LANCADO = sum(q for _m in M for _n, q, _u in _m.terc
                   if _n.startswith('Painel ripado'))
_RIP_DESENHO = ((626 * 272)                 # corredor da cozinha, com as portas
                + (147 * 269)               # fundo da cristaleira
                + (253.5 * 272 + 50 * 202 + 50 * 62)   # sala, em três faixas
                + (200 * 272)) / 10000 + 4.25          # suíte · escritório aparente
assert abs(_RIP_LANCADO - _RIP_DESENHO) < 0.02, \
    f'⛔⛔ RIPADO LANÇADO {_RIP_LANCADO:.2f} m² ≠ DESENHADO {_RIP_DESENHO:.2f} m²'

# ⭐⭐ E A TRAVA QUE FECHA A PORTA PARA SEMPRE: o atributo `fita_ripa` de
#   cada móvel tem de ser EXATAMENTE a metragem que ele lançou como
#   filetagem manual. São dois registros do mesmo metro — um que o
#   `custo_por_ambiente` lê e um que o `custo()` lê — e eles divergiram em
#   10 cm porque TRÊS lugares diferentes lançam ripa e só um tinha sido
#   corrigido. ⛔ Código duplicado não se confere no olho: varre-se.
for _m in M:
    _lc = sum(q for _n, q, _u in _m.terc if 'Filetagem' in _n)
    assert abs(_m.fita_ripa - _lc) < 1e-9, (
        f'⛔⛔ {_m.amb} · {_m.nome}: fita_ripa {_m.fita_ripa:.4f} m ≠ '
        f'filetagem lançada {_lc:.4f} m')

_RIPAS_COZ = sum(int(_n.split()[0]) for _m in M if _m.amb == 'Cozinha'
                 for _n, *_ in _m.pecas if 'ripas de' in _n
                 and 'cristaleira' not in _m.nome.lower())
assert _RIPAS_COZ == ripas_em(626), \
    f'⛔⛔ {_RIPAS_COZ} ripas no corredor, e 626 cm pedem {ripas_em(626)}'

PREMISSAS = [
 'Passo da ripa 3 cm — o detalhe 1:5 cotado, não a hachura da elevação (5 cm).',
 'Ripado do escritório orçado pela área APARENTE (4,25 m²), com base contínua '
 'atrás. Se correr atrás dos armários, são 8,60 m².',
 'Base do ripado em MDF 15 mm — a prancha cota 1 cm, que não é espessura comercial.',
 'Profundidade do armário gourmet: 25 cm, lida da cadeia do existente. Não é cotada.',
 'Tampo da mesa em duas chapas de 18 coladas (36 mm) — a espessura não é\n cotada e a Base não tem chapa de cor em 25 mm.',
 'Sistema de correr das duas portas ripadas: a prancha não especifica, e o '
 'Jonathan cravou por LINHA — Rometal R$ 600 na Hettich e SI Forma R$ 900 na '
 'Blum. ⚠ A Base diz "SS-150, 2 portas" por R$ 600: se UM kit servir as duas '
 'folhas, esta linha cai pela metade.',
 'Vidro reflecta PRATA com perfil — o executivo pede "cristal", que não '
 'existe na Base de Custos.',
 'Dobradiça Bigfer Onix a R$ 15 — a Base nunca cravou a do nível Padrão.',
 'Aparador com 3 BÁSCULAS (articulador Blum), não portas de giro: o símbolo '
 'é triângulo, e o escritório usa X e "<" para giro na mesma família.',
 '⛔ NÃO É MAIS PREMISSA: há comissão de VENDEDOR de 10% [Jonathan, '
 '03/11/2026], então a BASE é a linha "com RT OU com vendedor" da aba '
 'Comissões — 76,09%, e não os 84,88% que eu tinha assumido.',
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
        ar = sum(L * A * q / 10000 for _n, L, A, _e, _m, q, *_ in m.pecas)
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
