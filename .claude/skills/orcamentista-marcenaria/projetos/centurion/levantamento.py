# -*- coding: utf-8 -*-
"""CENTURION MOTORS — o levantamento, item por item.

⭐ A regra da casa: a CHAPA é a unidade de compra e arredonda-se para cima
  POR PADRÃO × ESPESSURA. Aqui isso importa muito, porque o projeto tem
  dois padrões (amadeirado e branco de estrutura) e um terceiro material
  de chapa inteiramente diferente, o compensado flexível, que vem em
  1600 × 2200 e não em 2750 × 1850.
"""
import importlib.util, math, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
_sp = importlib.util.spec_from_file_location('cent_base', AQUI / 'base.py')
b = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(b)

AMA, EST = 'MDF Amadeirado', 'MDF Branco TX'
FLEX = b.FLEX                 # ⭐ o nome mora na base, com o rendimento dele


class Item:
    """Um móvel. Acumula peças, metros lineares e serviços."""

    def __init__(self, nome, obs=''):
        self.nome, self.obs = nome, obs
        self.pecas, self.lin, self.serv = [], [], []

    def p(self, nome, L, A, qtd=1, mat=AMA, esp=18, obs='', fita=0.0):
        """uma peça de chapa · L × A em cm, fita em metros por peça"""
        self.pecas.append(dict(nome=nome, L=L, A=A, qtd=qtd, mat=mat,
                               esp=esp, obs=obs, fita=fita * qtd))
        return self

    def m(self, nome, metros, preco, un='m', obs='', chave=''):
        """material linear: alma de aço, LED, fita

        ⭐ `chave` é o rótulo na tabela de parâmetros, e é o que faz a
        planilha virar motor: o painel do ambiente soma POR CHAVE, e o
        preço unitário da linha é um VLOOKUP nela. Sem chave, a linha é um
        número solto que ninguém consegue recalcular."""
        self.lin.append(dict(nome=nome, qtd=metros, unit=preco, un=un,
                             obs=obs, chave=chave or nome))
        return self

    def s(self, nome, qtd, preco, un='un', obs='', chave=''):
        """serviço ou avulso: laca, fonte de LED, espelho"""
        self.serv.append(dict(nome=nome, qtd=qtd, unit=preco, un=un, obs=obs,
                              chave=chave or nome))
        return self

    # ── os números ──
    def areas(self):
        """área por (padrão, espessura), em m²"""
        a = {}
        for p in self.pecas:
            k = (p['mat'], p['esp'])
            a[k] = a.get(k, 0) + p['L'] * p['A'] / 10000 * p['qtd']
        return a

    def c_fita(self):
        return sum(p['fita'] for p in self.pecas)

    def n_pecas(self):
        return sum(p['qtd'] for p in self.pecas)

    def c_lin(self):
        return sum(x['qtd'] * x['unit'] for x in self.lin)

    def c_serv(self):
        return sum(x['qtd'] * x['unit'] for x in self.serv)


# ═══════════════════════════════════════════════════════════════════════
#   01 · O FORRO AMADEIRADO
# ═══════════════════════════════════════════════════════════════════════
#   ⭐ "o teto amadeirado precisa ser considerado como um item individual,
#     importante considerar material para montagem de mao amiga"
#     [Jonathan, 23/11/2026]
#   ⛔ MÃO AMIGA É MATERIAL DE MONTAGEM, NÃO ESTRUTURA. São as escoras em
#     T — um sarrafo em pé com travessa no topo — que seguram a placa
#     contra a laje enquanto o marceneiro parafusa. Sem elas não se monta
#     forro de 157 m² a 2,91 m do chão. A Base tem a linha: "Sarrafo de
#     pinus · Estrutura interna · R$ 8,00/m".
#   ⚠ O PERÍMETRO DO FORRO NÃO ESTÁ COTADO. A planta dá a ÁREA (157 m²) e
#     uma cota de 1380 de profundidade; pelo retângulo equivalente o lado
#     menor fica em 157/13,80 = 11,4 m, e o perímetro em 50,4 m. É
#     estimativa, e está nas dúvidas.
FORRO_PROF = 13.80
FORRO_LARG = b.FORRO_M2 / FORRO_PROF
FORRO_PERIM = 2 * (FORRO_PROF + FORRO_LARG)

forro = Item('Forro amadeirado',
             '%s m² de forro em MDF amadeirado de %d mm, liso · estruturação '
             'em tira de chapa branca de %d mm, que cobre o barroteamento e '
             'as escoras de mão amiga'
             % (('%0.0f' % b.FORRO_M2), b.FORRO_ESP, b.ESTRUT_ESP))
#   ⛔⛔ A PLACA ENTRA PELA ÁREA REAL, NÃO POR CHAPAS INTEIRAS. Eu lancei
#     39 peças do tamanho da chapa (275 × 185) e o motor, que já divide
#     área por RENDIMENTO, aplicou o aproveitamento de 80% DUAS VEZES:
#     157 m² viraram 198 m² de área e 49 chapas em vez de 39. Dez chapas
#     de R$ 700 saídas do nada, R$ 7.000, sem nada quebrar. Quem lança
#     área lança ÁREA; o rendimento é do motor.
forro.p('Forro amadeirado · a área inteira', FORRO_PROF * 100,
        FORRO_LARG * 100, 1, AMA, b.FORRO_ESP,
        'a área cravada na prancha · ⛔ quem lança área lança ÁREA: o '
        'rendimento da chapa é do motor, e aplicá-lo aqui também cobraria o '
        'desperdício duas vezes · ⭐ %d mm [Jonathan, 23/11/2026: "as chapas '
        'do teto podem ser de 15mm"] — chapa mais barata e quase 200 kg '
        'menos pendurados na laje'
        % b.FORRO_ESP)
#   ⛔⛔ AQUI MORAVAM DUAS LINHAS DE SARRAFO DE PINUS — barroteamento de
#     392,5 m e mão amiga de 35,1 m, R$ 3.420,80 — e as duas SAÍRAM:
#     "nao usamos sarrafo de pinus" [Jonathan, 23/11/2026].
#   ⭐ Entra o que a casa usa de verdade, e a Base já dizia em dois lugares
#     que eu não cruzei: "MDF Branco TX · Estrutura e caixaria · 15 mm ·
#     R$ 350,00" e, na tabela de espessura padrão, "Estrutura e caixaria ·
#     15 mm". Estrutura de forro é CHAPA CORTADA EM TIRA.
#   ⭐ As 5 chapas são número dele: "Considere 5 chapas brancas de 15mm
#     para estruturação" — e lanço a ÁREA LÍQUIDA das 5, 20,35 m², porque
#     quem lança área lança ÁREA; o rendimento é do motor.
ESTRUT_M2_FORRO = b.ESTRUT_CHAPAS_FORRO * b.REND
ESTRUT_TIRA_FORRO = ESTRUT_M2_FORRO / (b.TIRA_L / 100)
forro.p('Estruturação do forro · tira de MDF branco de %d, barrote e mão '
        'amiga' % b.ESTRUT_ESP,
        ESTRUT_TIRA_FORRO * 100, b.TIRA_L, 1, b.ESTRUT, b.ESTRUT_ESP,
        '⭐ 5 chapas cravadas pelo Jonathan = %s m² de chapa = %s m de tira '
        'de %s cm · cobre o barroteamento E as escoras de mão amiga, que são '
        'o que segura a placa contra a laje enquanto se parafusa · ⚠ dá uma '
        'malha de cerca de 75 × 120, mais aberta que os 60 × 120 que eu '
        'havia assumido com sarrafo'
        % (('%0.2f' % ESTRUT_M2_FORRO).replace('.', ','),
           ('%0.1f' % ESTRUT_TIRA_FORRO).replace('.', ','),
           ('%0.0f' % b.TIRA_L)))
forro.m('Fita de borda de cor, 22 mm · perímetro do forro',
        FORRO_PERIM * b.FITA_PERDA, b.FITA_22, 'm',
        '⚠ perímetro ESTIMADO: a prancha dá a área, não o contorno',
        chave='Fita de borda de cor, 22 mm')
forro.m('Filetagem na coladeira automática', FORRO_PERIM * b.FITA_PERDA,
        b.FILETE_MAQ, 'm', '', chave='Filetagem automática')

# ═══════════════════════════════════════════════════════════════════════
#   02 · OS PÓRTICOS CURVOS
# ═══════════════════════════════════════════════════════════════════════
#   ⭐ A composição é a que o Jonathan descreveu, camada por camada:
#       "a estrutura curva que tem uma largura de 12cm, tera a estrutura
#        em mdf revestido de compensado flexivel nos dois lados (interno e
#        externo) alem da moldura estrutural de mdf teremos o alisar de
#        acabamento externo"
#   ⛔ O RECORTE DO ARCO NÃO SE COMPRA PELO PERÍMETRO, SE COMPRA PELO
#     RETÂNGULO QUE ELE OCUPA NA CHAPA. Um arco de 12 cm de face parece
#     consumir 0,55 m²; na chapa ele ocupa 1,28 × 1,52 = 1,95 m². O miolo
#     de 1,46 m² volta ao plano de corte — e é com ele que saem fundos e
#     prateleiras. Está escrito na folha, porque é dinheiro de verdade.
porticos = Item('Pórticos curvos laqueados café',
                '%d nichos de %.0f × %.0f e %d pórticos de acesso aos '
                'ambientes de %.0f de vão · moldura de %.0f cm de face, '
                '%.0f cm de profundidade · ⭐ os dois pórticos de acesso '
                'entraram no escopo em 23/11/2026 ["os dois porticos de '
                'acesso aos ambientes tbm serao em marcenaria"] · ⚠ assumi '
                'que são iguais ao que eu já tinha lido na VISTA BB: se o '
                'segundo tiver outro vão, o número muda'
                % (b.N_NICHOS, b.NICHO_L, b.NICHO_H, b.N_PASSAGEM,
                   b.PASSAGEM_L, b.MOLDURA_L, b.NICHO_PROF))

#   ⭐⭐ SÃO DOIS PÓRTICOS DE ACESSO, E ELES SÃO NOSSOS [Jonathan,
#     23/11/2026]: "os dois porticos de acesso aos ambientes tbm serao em
#     marcenaria". Eu havia lançado UM, lido na VISTA BB — o outro eu nem
#     tinha visto, e ele não estava no escopo.
ARCOS = [('nicho', b.N_NICHOS, b.NICHO),
         ('passagem', b.N_PASSAGEM, b.PASSAGEM)]
for rot, n, A in ARCOS:
    #   2 costelas por pórtico: uma na boca, outra no fundo da profundidade
    #   ⭐⭐ EM MDF BRANCO, não amadeirado [Jonathan, 23/11/2026]: "Os arcos
    #     podem ser em mdf branco". O pórtico é LACADO CAFÉ e a laca cobre
    #     tudo — pagar R$ 700 de chapa amadeirada para esconder sob laca é
    #     jogar dinheiro fora. Branco 18 custa R$ 400.
    porticos.p('Moldura estrutural do arco de %s · costela' % rot,
               A['envolvente_l'], A['envolvente_a'], 2 * n,
               b.ARCO_MAT, b.ARCO_ESP,
               '⛔ retângulo do recorte, não o perímetro · o miolo volta ao '
               'corte · ⭐ MDF BRANCO: a peça é lacada café, a chapa não '
               'aparece')
    #   compensado flexível: intradorso e extradorso, ao longo da profundidade
    porticos.p('Compensado flexível do arco de %s · intradorso' % rot,
               A['interno'], b.NICHO_PROF, n, FLEX, 4,
               'a superfície curva de dentro, que se vê do vão')
    #   ⭐⭐ A FÓRMICA, SÓ NO INTRADORSO [Jonathan, 23/11/2026]. Ela cobre a
    #     mesma área do compensado de dentro, e é ela que transforma o
    #     compensado — que tem veio e emenda — na PEÇA LISA que a linha de
    #     laca da Base descreve. ⛔ O extradorso não leva: fica cru.
    porticos.p('Fórmica do arco de %s · revestimento do intradorso' % rot,
               A['interno'], b.NICHO_PROF, n, b.FORMICA, b.FORMICA_ESP,
               '⭐ sobre o compensado flexível, para a laca receber superfície '
               'lisa · folha de %.0f × %.0f a R$ %.0f · ⚠ a folha tem %.0f cm '
               'e o intradorso desenvolve %.0f cm: cada arco leva EMENDA, que '
               'desaparece sob a laca mas precisa ser prevista no corte'
               % (b.FORMICA_C, b.FORMICA_L, b.FORMICA_PRECO, b.FORMICA_C,
                  A['interno']))
    porticos.p('Compensado flexível do arco de %s · extradorso' % rot,
               A['externo'], b.NICHO_PROF, n, FLEX, 4,
               'a superfície curva de fora, que fecha a estrutura')
    #   alizar de acabamento externo, arrematando contra a parede
    porticos.p('Alizar de acabamento do arco de %s' % rot,
               A['externo'], b.ALIZAR_L, n, b.ARCO_MAT, b.ARCO_ESP,
               '⭐ %.0f cm de largura [Jonathan, 23/11/2026: "o alizar o '
               'projeto mostra 12cm"] — eu havia lançado 5 cm como premissa '
               'e estava errada · ⭐ MDF BRANCO, porque é peça lacada'
               % b.ALIZAR_L)

#   ⭐ A LACA, só no que se vê: face frontal de 12 cm, intradorso e alizar.
#     O extradorso fica revestido e cru, escondido nos 6 cm entre pórticos.
_face = sum(n * A['medio'] * b.MOLDURA_L for _r, n, A in ARCOS) / 10000
_intra = sum(n * A['interno'] * b.NICHO_PROF for _r, n, A in ARCOS) / 10000
_aliz = sum(n * A['externo'] * b.ALIZAR_L for _r, n, A in ARCOS) / 10000
LACA_M2 = _face + _intra + _aliz
_extra = sum(n * A['externo'] * b.NICHO_PROF for _r, n, A in ARCOS) / 10000
_br2 = lambda v: ('%0.2f' % v).replace('.', ',')
porticos.s('Laca café · face, lateral do nicho e alizar', LACA_M2, b.LACA_M2,
           'm²',
           '⭐ R$ 650,00 o m², DECISÃO DO JONATHAN [23/11/2026: "laca '
           'considere 650"] · é a linha ALTA da Base, "Laca ou pintura em '
           'peça lisa" do materiais.json, e não a de R$ 300 dos jobs, que eu '
           'havia lançado · ⭐ e é o lugar certo, porque as duas linhas da '
           'Base falam de peça LISA e curva leva mais lixa e mais tempo · '
           '⭐⭐ O QUE A LACA COBRE [Jonathan, 23/11/2026: "os nichos serão '
           'laqueados nas laterais, amadeirado sera apenas o fundo e as '
           'prateleiras"]: a face frontal da moldura de %.0f cm (%s m²), o '
           'INTRADORSO, que é a lateral e a abóbada vistas de dentro do vão '
           '(%s m²), e o alizar de %.0f cm (%s m²) · ⛔ NÃO cobre o '
           'extradorso (%s m²), que fica revestido e cru: ele some nos 6 cm '
           'entre pórticos · ⭐ E A LACA DO INTRADORSO VAI SOBRE FÓRMICA, não '
           'sobre o compensado cru: foi para isso que o Jonathan mandou '
           'revestir em 23/11/2026, e é o que torna a peça LISA de que a '
           'linha de R$ 650 o m² fala · ⚠ se a fórmica for o acabamento '
           'final em vez do substrato, saem %s m² daqui'
           % (b.MOLDURA_L, _br2(_face), _br2(_intra), b.ALIZAR_L,
              _br2(_aliz), _br2(_extra), _br2(_intra)),
           chave='Laca fosca PU')
#   ⭐⭐ A COLA DE CONTATO [Jonathan, 23/11/2026]: "acrescente mais uma lata de
#     cola de contato de 14k no custo dos nichos - custo de 600,00".
#   ⭐ Entra NESTE item, e não no 03, porque é aqui que o nicho é construído:
#     o item 02 se chama pórtico curvo mas descreve "7 nichos de 104 × 193",
#     e é aqui que vivem o compensado e a fórmica que a cola cola. Pôr a
#     cola separada do material que ela adere faria o rateio mentir.
#   ⭐ "MAIS uma lata" porque a cola comum já está nos consumíveis de 6%:
#     esta é uma lata inteira a mais, e laminado em curva come cola.
porticos.s('Cola de contato · lata de %d kg' % b.COLA_KG, 1, b.COLA_LATA,
           'lata',
           '⭐ UMA LATA A MAIS, cravada pelo Jonathan · a cola comum já está '
           'nos consumíveis de 6%% ("cola, lixa, parafuso, cavilha, '
           'tapa-furo"); esta é para colar a fórmica e o compensado flexível '
           'nos %s m² de superfície curva do intradorso e do extradorso, que '
           'bebem cola de contato muito acima do normal'
           % _br2(_intra + _extra),
           chave='Cola de contato · lata de %d kg' % b.COLA_KG)

# ═══════════════════════════════════════════════════════════════════════
#   03 · OS NICHOS POR DENTRO · fundo e prateleiras
# ═══════════════════════════════════════════════════════════════════════
#   ⭐ "as prateleiras serao de mdf e precisa de alma de aço e com
#     iluminação de led" [Jonathan, 23/11/2026]
#   ⭐ ALMA DE AÇO: a Base manda "uma por peça, contra empeno". Prateleira
#     de 104 cm de vão sem apoio no meio empena — é o caso exato.
N_PRAT = b.N_NICHOS * b.PRAT_POR_NICHO
N_PECAS_PRAT = N_PRAT * b.PRAT_CAMADAS
nichos = Item('Nichos por dentro · fundo, prateleira e luz',
              '%d fundos em MDF de %d mm e %d prateleiras de %.0f × %.0f '
              'com %d mm de espessura, em %d peças de %d mm, cada uma com '
              'alma de aço e LED'
              % (b.N_NICHOS, b.FUNDO_ESP, N_PRAT, b.NICHO_L, b.NICHO_PROF,
                 b.PRAT_ESP, N_PECAS_PRAT, b.PRAT_ESP_PECA))
#   ⭐⭐ O FUNDO VAI EM 6 mm [Jonathan, 23/11/2026]: "os fundos serao em mdf
#     de 6mm". A Base concorda em dois lugares — "MDF Branco TX · Fundos ·
#     6 mm" e a tabela de espessura, "Fundos · 6 mm · por encaixe em rasgo,
#     SEM FITA" — e é por isso que esta linha não leva fita.
#   ⚠ Mas AMADEIRADO de 6 mm, não branco: este fundo é a face que se vê
#     dentro do nicho, a que a prancha marcava como ADESIVO.
nichos.p('Fundo do nicho · era ADESIVO na prancha', b.NICHO_L, b.NICHO_H,
         b.N_NICHOS, AMA, b.FUNDO_ESP,
         '⭐ 6 mm, decisão do Jonathan · AMADEIRADO, porque é a face vista '
         'dentro do nicho · ⭐ a Base manda fundo por encaixe em rasgo, SEM '
         'fita — por isso esta linha não tem borda')
#   ⭐⭐ A PRATELEIRA TEM 30 mm EM DUAS PEÇAS DE 15 [Jonathan, 23/11/2026]:
#     "considere 6 em cada, com 30mm de espessura, duas peças de 15mm".
#   ⛔ São duas mudanças que se multiplicam: 6 por nicho em vez de 4 e duas
#     camadas em vez de uma. A área de chapa TRIPLICA.
nichos.p('Prateleira do nicho · camada de %d mm' % b.PRAT_ESP_PECA,
         b.NICHO_L, b.NICHO_PROF, N_PECAS_PRAT, b.PRAT_MAT, b.PRAT_ESP_PECA,
         '⭐ %d prateleiras × %d camadas = %d peças · %d por nicho, cravadas '
         'pelo Jonathan (eu havia contado 4 na VISTA BB) · as duas camadas '
         'colam e viram uma peça de %d mm'
         % (N_PRAT, b.PRAT_CAMADAS, N_PECAS_PRAT, b.PRAT_POR_NICHO,
            b.PRAT_ESP))
#   ⭐ A FITA É DA PRATELEIRA MONTADA, UMA POR PRATELEIRA — não uma por
#     camada. Por isso vem como linha linear, e não no campo `fita` da
#     peça, que multiplicaria pelas 84 peças.
#   ⛔⛔ E SÓ A FRENTE LEVA FITA [Jonathan, 23/11/2026: "os nichos serão
#     laqueados nas laterais, amadeirado sera apenas o fundo e as
#     prateleiras"]. Eu fitava frente MAIS os dois lados de 30 cm — mas a
#     prateleira vai de lateral a lateral do nicho, e essas duas bordas
#     encostam no intradorso LAQUEADO: não se vê, não se fita. Eram 25,2 m
#     de fita e de filetagem a mais, R$ 152,46.
PRAT_PERIM = N_PRAT * b.NICHO_L / 100
nichos.m('Fita de borda de cor · frente das prateleiras montadas',
         PRAT_PERIM * b.FITA_PERDA, b.FITA_22, 'm',
         '⚠ A BORDA TEM %d mm E A FITA DA BASE TEM 22 mm. Prateleira de duas '
         'camadas coladas pede fita de 35 mm, que a Base não lista — lanço a '
         'de 22 mm a R$ 3,00 e marco a diferença nas dúvidas · ⭐ SÓ A FRENTE: '
         'uma fita por prateleira, não por camada, e não nos lados, que '
         'encostam na lateral laqueada do nicho' % b.PRAT_ESP,
         chave='Fita de borda de cor, 22 mm')
nichos.m('Filetagem na coladeira automática · frente das prateleiras',
         PRAT_PERIM * b.FITA_PERDA, b.FILETE_MAQ, 'm', '',
         chave='Filetagem automática')
nichos.s('Alma de aço · barra chata de 3 m', math.ceil(N_PRAT * b.NICHO_L
         / b.ALMA_M), b.ALMA_BARRA, 'barra',
         '⭐ uma alma por PRATELEIRA, como a Base manda, não uma por camada · '
         '%d prateleiras de %.0f cm dão %.0f m de barra'
         % (N_PRAT, b.NICHO_L, N_PRAT * b.NICHO_L / 100),
         chave='Alma de aço · barra de 3 m')
LED_TOTAL = N_PRAT * b.NICHO_L / 100
nichos.m('LED COB · conjunto completo, uma régua por prateleira', LED_TOTAL,
         b.LED_M, 'm',
         '⭐ CONJUNTO: fita, perfil, usinagem e instalação · a Base avisa que '
         'o LED instalado vai de R$ 66 a R$ 150 conforme o que a linha inclui, '
         'e prateleira que acende é o conjunto inteiro',
         chave='LED COB · conjunto completo')
nichos.s('Fonte de LED', math.ceil(LED_TOTAL / 9), b.LED_FONTE, 'un',
         'uma a cada 8 a 10 m de régua', chave='Fonte de LED')

# ═══════════════════════════════════════════════════════════════════════
#   04 · OS PAINÉIS DE PAREDE · o que era adesivo
# ═══════════════════════════════════════════════════════════════════════
paineis = Item('Painéis de parede · o que era adesivo',
               'onde a prancha sinaliza ADESIVO, vai painel de MDF '
               'amadeirado de %d mm, no mesmo padrão do forro'
               % b.PAINEL_ESP)
for rot, L, A in b.PAINEIS:
    #   ⭐⭐ 15 mm [Jonathan, 23/11/2026]: "os paineis nas paredes tbm podem
    #     ser de 15mm". Mesma lógica do forro — o painel é PELE sobre a
    #     alvenaria e quem sustenta é a tira aprumada atrás.
    paineis.p(rot, L, A, 1, AMA, b.PAINEL_ESP, '', fita=2 * (L + A) / 100)
PAINEL_M2 = sum(L * A / 10000 for _r, L, A in b.PAINEIS)
#   ⛔ aqui havia 65,58 m de sarrafo de pinus, R$ 524,66 · saiu
PAINEL_TIRA = PAINEL_M2 / 0.60
paineis.p('Estruturação do painel · tira de MDF branco de %d, montante a '
          'cada 60' % b.ESTRUT_ESP,
          PAINEL_TIRA * 100, b.TIRA_L, 1, b.ESTRUT, b.ESTRUT_ESP,
          'o painel é PELE sobre a alvenaria: a tira aprumada é o que recebe '
          'o parafuso · %s m de tira de %.0f cm, saída de chapa branca de 15 '
          'mm, que é o que a Base manda para estrutura'
          % (('%0.1f' % PAINEL_TIRA).replace('.', ','), b.TIRA_L))

# ═══════════════════════════════════════════════════════════════════════
#   05 · OS PAINÉIS QUE RECEBEM O ESPELHO
# ═══════════════════════════════════════════════════════════════════════
#   ⭐ [Jonathan, 23/11/2026] o espelho virou DOIS itens: o painel que o
#     recebe e o espelho em si. Separar é certo — são dois fornecedores,
#     dois prazos e duas responsabilidades. O painel sai da nossa fábrica
#     com o móvel; o espelho é medido DEPOIS do painel montado, porque a
#     Base avisa: "Vidraceiro. A medida sai depois do móvel montado,
#     nunca antes."
base_esp = Item('Painéis para receber o espelho',
                '%s m² de base em MDF de 18 mm, aprumada e plana, onde o '
                'espelho vai colado · ⛔ aqui NÃO se desce para 15: espelho '
                'colado não perdoa barriga' % ('%0.2f' % sum(
                    L * A / 10000 for _r, L, A in b.ESPELHOS)).replace('.', ','))
for rot, L, A in b.ESPELHOS:
    base_esp.p(rot.replace('espelho', 'base do espelho'), L, A, 1,
               b.ESPELHO_SUBSTRATO, 18,
               '⭐ Branco TX, não amadeirado: a face some inteira sob o '
               'espelho e a chapa custa R$ 400 em vez de R$ 700')
ESP_M2 = sum(L * A / 10000 for _r, L, A in b.ESPELHOS)
#   ⛔ aqui havia 39,39 m de sarrafo de pinus, R$ 315,13 · saiu
ESP_TIRA = ESP_M2 / 0.60
base_esp.p('Estruturação da base · tira de MDF branco de %d, montante a '
           'cada 60' % b.ESTRUT_ESP,
           ESP_TIRA * 100, b.TIRA_L, 1, b.ESTRUT, b.ESTRUT_ESP,
           '⛔ espelho colado não perdoa barriga na base: a tira aprumada é o '
           'que garante o plano · %s m de tira de %.0f cm'
           % (('%0.1f' % ESP_TIRA).replace('.', ','), b.TIRA_L))

# ═══════════════════════════════════════════════════════════════════════
#   06 · OS ESPELHOS
# ═══════════════════════════════════════════════════════════════════════
espelhos = Item('Espelhos prata, colados sobre o painel',
                '%s m² de espelho prata nas vistas AA e CC'
                % ('%0.2f' % ESP_M2).replace('.', ','))
for rot, L, A in b.ESPELHOS:
    espelhos.s(rot, L * A / 10000, b.ESPELHO_M2_PRECO, 'm²',
               '⚠ a Base avisa: "O VIDRO ENTRA PELA ÁREA DA FOLHA, não '
               'pelo vão" · aqui o espelho cobre o painel inteiro, então '
               'área da folha e área do painel são a mesma coisa',
               chave='Espelho prata')
espelhos.s('Frete de espelho', 1, b.ESPELHO_FRETE, 'serviço',
           'a Base tem a linha, por serviço · chapa de espelho não vai '
           'junto com a carga de marcenaria', chave='Frete de espelho')

# ═══════════════════════════════════════════════════════════════════════
#   O FECHAMENTO
# ═══════════════════════════════════════════════════════════════════════
ITENS = [forro, porticos, nichos, paineis, base_esp, espelhos]


def apura():
    chapas, area, c_chapa = {}, {}, 0.0
    for it in ITENS:
        for k, v in it.areas().items():
            area[k] = area.get(k, 0) + v
    for k, v in sorted(area.items()):
        rend = b.rend(k)
        n = math.ceil(round(v / rend, 6))
        chapas[k] = n
        c_chapa += n * b.PRECO['%s %d' % k]
    c_fita = sum(it.c_fita() for it in ITENS) * b.FITA_PERDA * b.FITA_22
    c_filete = sum(it.c_fita() for it in ITENS) * b.FITA_PERDA * b.FILETE_MAQ
    c_lin = sum(it.c_lin() for it in ITENS)
    c_serv = sum(it.c_serv() for it in ITENS)
    #   ⛔⛔ A FITA LANÇADA COMO LINHA LINEAR TAMBÉM É FITA. A regra da casa
    #     é "consumíveis, 6% sobre chapa e fita", e eu lanço fita de dois
    #     jeitos: no campo `fita` da peça (painéis) e como linha `.m()`
    #     quando a borda não é por peça (o perímetro do forro, e a
    #     prateleira montada, cuja fita é uma por prateleira e não uma por
    #     camada). ⭐ A segunda ficava FORA da base dos consumíveis, então
    #     o mesmo material entrava ou não na conta conforme COMO eu o
    #     lancei — e nada quebrava. São R$ 310,45 de fita, 6% dos quais
    #     faltavam na conta.
    c_fita_lin = sum(x['qtd'] * x['unit'] for it in ITENS for x in it.lin
                     if 'Fita de borda' in x['nome'])
    n_ch = sum(chapas.values())
    n_pc = sum(it.n_pecas() for it in ITENS)
    c_corte = n_ch * b.CORTE_CHAPA + n_pc * b.CORTE_PECA
    #   ⚠ A FILETAGEM NÃO ENTRA: a regra diz chapa e FITA, e filetagem é
    #     mão de obra por metro, não material.
    c_cons = (c_chapa + c_fita + c_fita_lin) * b.CONSUMIVEIS
    base = c_chapa + c_fita + c_filete + c_lin + c_serv + c_corte + c_cons
    c_emb = base * b.EMBALAGEM
    return dict(chapas=chapas, area=area, c_chapa=c_chapa, c_fita=c_fita,
                c_filete=c_filete, c_lin=c_lin, c_serv=c_serv, n_ch=n_ch,
                n_pc=n_pc, c_corte=c_corte, c_cons=c_cons, c_emb=c_emb,
                direto=base + c_emb)


T = apura()


def brl(v):
    #   ⛔ folha brasileira: separador de milhar, senão 52700,00 não se lê
    t = ('%0.2f' % v).replace('.', ',')
    i, _, d = t.partition(',')
    out = ''
    while len(i) > 3:
        out, i = '.' + i[-3:] + out, i[:-3]
    return i + out + ',' + d


if __name__ == '__main__':
    S = '─'
    print('\n  CENTURION MOTORS · LEVANTAMENTO  ' + S * 42)
    print('  Projeto CLS · prancha 554, rev. 00 de 17/11/2025 · '
          'Vila da Serra\n')

    print('  ① A CHAPA, POR PADRÃO E ESPESSURA  ' + S * 40)
    print('  %-28s %9s %7s %12s' % ('PADRÃO', 'ÁREA m²', 'CHAPAS', 'R$'))
    for k, n in sorted(T['chapas'].items()):
        print('  %-28s %9.2f %7d %12s'
              % ('%s %d' % k, T['area'][k], n, brl(n * b.PRECO['%s %d' % k])))
    print('  %-28s %9s %7d %12s' % ('', '', T['n_ch'], brl(T['c_chapa'])))

    print('\n  ② OS %d ITENS  ' % len(ITENS) + S * 55)
    for it in ITENS:
        print('\n  ■ %s' % it.nome)
        print('    %s' % it.obs)
        for p in it.pecas:
            print('      %-52s %6.0f × %-6.0f %3d pç  %s %d'
                  % (p['nome'][:52], p['L'], p['A'], p['qtd'], p['mat'], p['esp']))
        for x in it.lin + it.serv:
            print('      %-52s %8.1f %-6s %12s'
                  % (x['nome'][:52], x['qtd'], x['un'],
                     brl(x['qtd'] * x['unit'])))

    print('\n  ③ O CUSTO DIRETO  ' + S * 56)
    #   ⛔ RÓTULO E CONTEÚDO NA MESMA PASSADA: "Sarrafo, alma de aço e LED"
    #     mentia duas vezes — o sarrafo saiu do projeto e a alma de aço
    #     nunca esteve nesta linha, ela é serviço.
    for rot, v in [('Chapa · %d chapas' % T['n_ch'], T['c_chapa']),
                   ('Fita de borda nas peças', T['c_fita']),
                   ('Filetagem nas peças', T['c_filete']),
                   ('Fita, filetagem e LED lançados por metro', T['c_lin']),
                   ('Laca, alma de aço, espelho e avulsos', T['c_serv']),
                   ('Corte · %d chapas e %d peças' % (T['n_ch'], T['n_pc']),
                    T['c_corte']),
                   ('Consumíveis · %s%% sobre chapa e fita'
                    % ('%0.0f' % (b.CONSUMIVEIS * 100)), T['c_cons']),
                   ('Embalagem · %s%% sobre o custo'
                    % ('%0.0f' % (b.EMBALAGEM * 100)), T['c_emb'])]:
        print('  %-44s %16s' % (rot, brl(v)))
    print('  %-44s %16s' % ('CUSTO DIRETO', brl(T['direto'])))
