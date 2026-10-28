# -*- coding: utf-8 -*-
"""O comum de todo ambiente do ICA: a chapa, a peça, a gaveta e os preços.

⭐ Nasceu do living.py quando a Cozinha chegou. São 20 ambientes — o que é
  regra da casa mora aqui; o que é prancha mora no arquivo do ambiente.

⛔ Toda medida em CENTÍMETROS, como a prancha. Espessura em mm.
"""
CHAPA_C, CHAPA_L = 275.0, 185.0          # cm · confirmado em plano de corte
CHAPA_M2 = CHAPA_C * CHAPA_L / 10000     # 5,0875 m²
APROV    = 0.80
SANGRIA  = 2.0                           # cm de acerto de corte [Jonathan]
ALT_MAX  = CHAPA_C - SANGRIA             # ⭐ 273 — o teto de peça sem emenda

# ── preços, todos da Base de Custos ─────────────────────────────────────
# ⭐ A Base tem uma tabela de ESPESSURA PADRÃO POR APLICAÇÃO, e eu não a
#   estava seguindo:  estrutura e caixaria 15 · fundos 6 · porta 15 ·
#   prateleira 18 acima de 70 cm de vão.  ⛔ Eu vinha lançando caixaria e
#   porta em 18 mm, que é mais caro e não é o padrão da casa.
PRECO = {'MDF cor 18': 700.0, 'MDF cor 15': 550.0, 'MDF cor 6': 350.0,
         'MDF branco 18': 400.0, 'MDF branco 15': 350.0, 'MDF branco 6': 250.0,
         # ⭐ Branco TX é o nome do produto na Base, e é o que vai na aba
         'MDF Branco TX 18': 400.0, 'MDF Branco TX 15': 350.0,
         'MDF Branco TX 6': 250.0,
         # ⭐ cada cor em TRÊS espessuras agora, porque a frente provençal
         #   usa 15 na base e 6 na moldura — e cada uma é um arredondamento
         'MDF Verde Floresta 18': 700.0, 'MDF Verde Floresta 15': 550.0,
         'MDF Verde Floresta 6': 350.0,
         'MDF Jequitibá Rosa 18': 700.0, 'MDF Jequitibá Rosa 15': 550.0,
         'MDF Jequitibá Rosa 6': 350.0,
         'MDF Nogueira Caiena 18': 700.0, 'MDF Nogueira Caiena 6': 350.0,
         # ⭐ padrões que a leitura das pranchas dos outros ambientes trouxe.
         #   Todos são Melamínico Fosco na Base (R$ 700 / 550 / 350), exceto
         #   onde a prancha pede linha mais cara. ⚠ Preto Ultra Premium e
         #   Lacca Fume não estão nomeados na Base: adoto o Fosco e deixo a
         #   dúvida na aba do ambiente.
         'MDF Preto Ultra Premium 18': 700.0, 'MDF Preto Ultra Premium 15': 550.0,
         'MDF Preto Ultra Premium 6': 350.0,
         'MDF Lacca Fume 18': 700.0, 'MDF Lacca Fume 15': 550.0,
         'MDF Carvalho Malva 18': 700.0, 'MDF Carvalho Malva 15': 550.0,
         'MDF Carvalho Malva 6': 350.0,
         'MDF Off White Suave 18': 700.0, 'MDF Off White Suave 15': 550.0,
         'MDF Off White Suave 6': 350.0}
ESTRUTURA, FUNDO_CH, PORTA_CH = 'MDF Branco TX 15', 'MDF Branco TX 6', 15
PRAT_VAO = 70.0   # vão acima disto pede 18 mm, contra empeno [Base]
# ⭐⭐ FITA E FILETAGEM SÃO DUAS COISAS [Jonathan, 28/10/2026]
#   > "nao vi o levamento de filetagem tbm"
#   Estavam, mas escondidas dentro de um preço só: os R$ 5,50 da "fita de
#   cor com filetagem" da Base são R$ 3,00 de fita MAIS R$ 2,50 de
#   filetagem. Juntas num número, nunca se vê que:
#     · a fita BRANCO TX custa R$ 2,00, não R$ 3,00 — e a caixaria toda é
#       branca, então metade dos metros estava precificada a mais
#     · a filetagem de RIPA e de chapa de 6 mm é MANUAL, R$ 5,00 — o dobro
#       da automática, porque não entra na coladeira
#   ⛔ Separar não é cosmética: muda o número nos DOIS sentidos.
FITA_COR, FITA_BRANCO   = 3.00, 2.00   # por metro de aresta
FILETE_AUTO, FILETE_MAO = 2.50, 5.00   # coladeira automática × à mão
FITA_CHEIA = 5.50   # ⚠ só para compatibilidade com o Living
FITA_PERD  = 0.10   # ⭐ 10% de desperdício é da FITA, que é material.
                    #   A filetagem é SERVIÇO, cobrado por metro de aresta
                    #   feita: não tem desperdício.
CORREDICA  = 300.0  # Corrediça Blum, por gaveta
DOBRADICA  =  50.0  # Dobradiça Blum
DOBR_VIDRO =  70.0  # porta de vidro · A COTAR
BASCULA    = 250.0  # Blum AVENTOS HK-XS · ⭐ a báscula da casa
PULSADOR   = 100.0  # ⛔ FORA DA COZINHA [Jonathan, 28/10/2026]
SLIM       =  35.0  # ⭐ Puxador slim Rometal · é o que abre a báscula
#   > "nas básculas da cozinha iremos considerar o articular Hk-xs da blum
#   >  e puxador slim da rometal (R$ 35,00 und). ou seja, nao teremos o
#   >  pulsador blum."
#   ⭐ A própria Base já avisava: "PULSADOR E PUXADOR SLIM NÃO SE SOMAM na
#     mesma frente. São R$ 65 de diferença por porta." Em 17 básculas,
#     R$ 1.105.
CAVA_M     =  50.0  # cava usinada, por metro de frente
PUXADOR    = 172.71 # Alças Traso 416 mm · ⚠ o maior da linha, não é o do ICA
PUXADOR_128 = 110.0 # ⭐ Alças Traso 128 mm [Jonathan, 28/10/2026]
#   ⚠ A Base trazia R$ 56,69 para o 128 mm, de "média de três lojas", no
#     acabamento PRETO. A busca de varejo de hoje achou de R$ 44,92 a
#     R$ 109,22, e o topo da faixa é o níquel velho — que é onde o R$ 110
#     do Jonathan cai. ⭐ Não é divergência: é outro acabamento.
MOLDURA_MO = 0.0    # ⛔ moldura provençal, por frente — SEM PREÇO na Base
LED_M      = 150.0  # LED COB: fita, perfil, usinagem e instalação
ALMA       =  50.0  # barra chata 5 mm, 3 m · toda peça acima de 30 mm
SUPORTE    =  30.0  # suporte oculto de prateleira · de 40 em 40 cm
CABIDEIRO  = 120.0  # cabideiro em metal preto ou grafite · Base, por unidade
# ⭐ reforço estrutural interno. A prancha da Lavanderia manda "prever
#   reforço para suportar lava e seca cheia": o apoio sobe para 18 mm e
#   recebe sarrafo. Sarrafo é material de estrutura, não aparece e não leva
#   fita — por isso entra por metro, como o LED, e não como peça de chapa.
SARRAFO    =   8.0  # sarrafo de pinus · estrutura interna, por metro
VIDRO_M2   =   0.0  # ⛔ reflecta champagne SEM PREÇO — a cotar
# ⭐ SERRALHERIA ESTRUTURAL [Jonathan, 28/10/2026]
#   > "No banco suspenso do living considere uma estrutura de serralheria
#   >  estrutural com um custo de 2.500"
#   ⛔ Não confundir com o rodapé de 3 cm, que a casa faz em MDF melamínico
#     por decisão do Jonathan de 26/10. Aqui é estrutura de verdade: o banco
#     é SUSPENSO e o que o segura não é a marcenaria.
#   ⭐ Entra como VALOR FECHADO por móvel, não por metro: foi assim que o
#     Jonathan deu, e banco suspenso é projeto, não metro linear.
CONSUM, EMBAL = 0.06, 0.02
# ⛔⛔ SEM FONTE DE LED em lugar nenhum: as fitas da casa são 110 V
#   [Jonathan, 28/10/2026]

ALTAS = []   # ⭐ toda peça que o projeto desenhou acima do que a chapa dá

def P(nome, movel, c, l, qtd=1, chave='MDF cor 18', fita=(0, 0), obs=''):
    """Uma peça. `fita` = (nº de arestas no COMPRIMENTO, nº na LARGURA).

    ⭐ A CHAVE É POR COR, não só por espessura. Um ambiente com três padrões
      de MDF faz TRÊS arredondamentos de chapa, não um — cada cor é uma
      compra separada e puxa no mínimo uma chapa. Foi o erro que queimou a
      primeira versão desta planilha.

    ⛔ Peça acima de 273 é ANOTADA e rebaixada: é decisão de projeto, não de
      corte, e tem de aparecer na lista.
    """
    def cabe(a, b): return a <= CHAPA_C and b <= CHAPA_L
    if not (cabe(c, l) or cabe(l, c)):
        maior, menor = max(c, l), min(c, l)
        if menor <= CHAPA_L and maior > ALT_MAX:
            ALTAS.append((movel, nome, maior, qtd))
            c, l = (ALT_MAX, l) if c >= l else (c, ALT_MAX)
        else:
            raise AssertionError(f'⛔ {nome} ({c}×{l}) NÃO CABE NA CHAPA')
    return dict(nome=nome, movel=movel, c=c, l=l, qtd=qtd, chave=chave,
                fita=fita, obs=obs)

def gaveta(movel, larg, prof, alt, n=1, rotulo='Caixa de gaveta',
           cor=ESTRUTURA, fundo=FUNDO_CH):
    """A caixa atrás da frente. ⭐ É o que mais se esquece de contar."""
    liq = larg - 3.6
    return [P(f'{rotulo} · lateral', movel, prof, alt, 2*n, cor, (1, 0)),
            P(f'{rotulo} · frente e costas', movel, liq, alt, 2*n, cor, (1, 0)),
            P(f'{rotulo} · fundo', movel, liq, prof, n, fundo, (0, 0),
              'Fundo em 6 mm por encaixe em rasgo — ⛔ sem fita')]

def ripado(movel, larg_total, alt, larg_ripa, vao, chave, obs=''):
    """Ripa solta com vão. ⭐ Conta a ripa, não o painel."""
    n = int(larg_total // (larg_ripa + vao)) + 1
    # ⭐⭐ LAMINAÇÃO NOS DOIS LADOS [Jonathan, 28/10/2026]
    #   > "nas ripas de 3cm, considere a laminação em ambos os lados"
    #   ⛔ Eu tinha (2, 1): filetava as duas pontas de 3 cm e UM lado longo.
    #     Numa ripa solta, com vão, os dois lados longos ficam à vista — são
    #     QUATRO arestas, e as longas são as que valem metro. Numa ripa de
    #     3 × 103 isso é 1,09 m contra 2,12 m: a conta dobra.
    #   ⛔ E ripa não entra na coladeira: a filetagem é MANUAL, R$ 5,00.
    return [P(f'Ripa de {larg_ripa:g}', movel, larg_ripa, alt, n, chave, (2, 2),
              obs or f'Vão de {vao:g} entre as ripas · {n} ripas em '
                     f'{larg_total:g} · laminada nos dois lados')]

# ⛔ MOLDURA_L SAIU. Era a largura da travessa, e era premissa minha: a
#   prancha não a cotava e eu adotei 7 cm. Não existe mais travessa.

def provencal(nome, movel, c, l, qtd, cor15, cor6, obs=''):
    """⭐⭐ FRENTE PROVENÇAL — DUAS PEÇAS INTEIRAS  [Jonathan, 28/10/2026]
       > "para as demais frentes provençais nao considere reguas, considere
       >  outra peça de igual tamanho pois é retirada uma peça inteira e
       >  feito a usinagem na router"

       base ........ 15 mm na cor, medida cheia da frente
       moldura ..... OUTRA peça inteira de 6 mm, MESMA medida, usinada na
                     router — não são quatro réguas montadas

    ⛔⛔ EU ORÇAVA RÉGUA, E RÉGUA NÃO É O QUE SAI DA FÁBRICA. Montava a
      moldura com quatro travessas de 7 cm coladas em volta. A fábrica tira
      uma peça inteira e usina o relevo na router: o que vai para o plano de
      corte é um RETÂNGULO CHEIO de 6 mm, não quatro tiras. Três coisas
      mudam de uma vez:

      1. A CHAPA DE 6 MM SOBE. Quatro réguas de 7 cm numa frente de 60 × 85
         davam 0,20 m²; a peça inteira dá 0,51 m². É duas vezes e meia mais
         de chapa de 6 — e chapa se arredonda inteira.
      2. A FILETAGEM MANUAL SOME. A régua de 6 mm não entrava na coladeira e
         ia à mão, a R$ 5,00. Agora o 6 é COLADO sobre o 15 e o conjunto vai
         à coladeira como uma peça só, de 21 mm, no automático. Por isso a
         peça de 6 entra com fita (0, 0): quem leva o perímetro é a base,
         uma vez só, pelos dois.
      3. A PREMISSA DA TRAVESSA MORRE. Não há largura de régua para adivinhar
         — e com ela morre o limite de tamanho: uma frente de 10 cm, que não
         comportava duas travessas de 7, agora é provençal como qualquer
         outra.

    ⛔ A MÃO DE OBRA continua sem preço na Base, mas agora tem nome certo:
      é USINAGEM NA ROUTER por frente, não montagem de travessa.
    """
    return [P(nome, movel, c, l, qtd, cor15, (2, 2), obs),
            P(f'{nome} · moldura usinada', movel, c, l, qtd, cor6, (0, 0),
              'Peça inteira de 6 mm, mesma medida da base, relevo usinado na '
              'router · colada sobre a base: o perímetro vai na fita da base, '
              '⛔ sem fita própria para não contar o mesmo metro duas vezes')]

def _fita_chave(chave):
    return 'Fita Branco TX' if 'ranco' in chave else 'Fita cor'

def _filete_chave(chave, nome):
    """⛔ Ripa e chapa de 6 mm não entram na coladeira: filetagem à mão.

    ⛔ A REGRA É A ESPESSURA, NÃO A PALAVRA. Eu tinha posto 'ravessa' aqui,
      pensando nas travessas de 6 mm da moldura provençal — e a regra pegou
      a "travessa sobre as portas" do Living, que é painel de 180 × 63 em
      18 mm e entra na coladeira sem dificuldade. Cobrava R$ 5,00 onde são
      R$ 2,50. ⭐ As travessas da moldura já caem aqui pela espessura, que
      é o critério de verdade: quem não entra na máquina é o 6 mm e a ripa.
    """
    return ('Filetagem manual' if chave.endswith(' 6') or 'Ripa' in nome
            else 'Filetagem automática')

def acabamento(pecas, movel=None):
    """⭐ Metros por CHAVE de acabamento, que é o levantamento que faltava.
      A fita leva os 10% de desperdício porque é material; a filetagem não,
      porque é serviço por metro de aresta feita.

    ⛔⛔ O TOTAL DO AMBIENTE É A SOMA DOS MÓVEIS JÁ ARREDONDADOS, não o
      arredondamento da soma. Parece preciosismo e não é: a aba soma com
      SOMASE os valores por móvel, que saem arredondados em 0,1 m, e eu
      arredondava o total do ambiente. Deu R$ 0,54 de diferença entre o
      script e a planilha — pequena, mas é exatamente o tipo de divergência
      que a linha de CONFERÊNCIA existe para não deixar passar. ⭐ E a aba
      está certa: é por móvel que a fábrica executa.
    """
    if movel is None:
        tot = {}
        for mv in dict.fromkeys(p['movel'] for p in pecas):
            for k, v in acabamento(pecas, mv).items():
                tot[k] = round(tot.get(k, 0.0) + v, 1)
        return tot
    out = {}
    for p in pecas:
        if p['movel'] != movel: continue
        nc, nl = p['fita']
        m = (nc*p['c'] + nl*p['l'])*p['qtd']/100
        if m <= 0: continue
        fk = _fita_chave(p['chave'])
        lk = _filete_chave(p['chave'], p['nome'])
        out[fk] = out.get(fk, 0.0) + m*(1 + FITA_PERD)
        out[lk] = out.get(lk, 0.0) + m
    return {k: round(v, 1) for k, v in out.items() if round(v, 1) > 0}

PRECO_ACAB = {'Fita cor': FITA_COR, 'Fita Branco TX': FITA_BRANCO,
              'Filetagem automática': FILETE_AUTO, 'Filetagem manual': FILETE_MAO}

def fita_m(pecas, movel=None):
    """⚠ Só o metro cru, sem desperdício. O Living ainda usa."""
    return sum((nc*p['c'] + nl*p['l'])*p['qtd']/100 for p in pecas
               if movel is None or p['movel'] == movel
               for nc, nl in [p['fita']])
