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
FLEX = 'Compensado flexível'


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

    def m(self, nome, metros, preco, un='m', obs=''):
        """material linear: sarrafo, alma de aço, LED, fita"""
        self.lin.append(dict(nome=nome, qtd=metros, unit=preco, un=un, obs=obs))
        return self

    def s(self, nome, qtd, preco, un='un', obs=''):
        """serviço ou avulso: laca, fonte de LED, suporte"""
        self.serv.append(dict(nome=nome, qtd=qtd, unit=preco, un=un, obs=obs))
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
             '157 m² de forro em MDF amadeirado 18 mm, liso · '
             'barroteamento, fixação e escora de montagem')
#   ⛔⛔ A PLACA ENTRA PELA ÁREA REAL, NÃO POR CHAPAS INTEIRAS. Eu lancei
#     39 peças do tamanho da chapa (275 × 185) e o motor, que já divide
#     área por RENDIMENTO, aplicou o aproveitamento de 80% DUAS VEZES:
#     157 m² viraram 198 m² de área e 49 chapas em vez de 39. Dez chapas
#     de R$ 700 saídas do nada, R$ 7.000, sem nada quebrar. Quem lança
#     área lança ÁREA; o rendimento é do motor.
forro.p('Forro amadeirado · a área inteira', FORRO_PROF * 100,
        FORRO_LARG * 100, 1, AMA, 18,
        'os 157 m² cravados na prancha · o motor divide pelo rendimento '
        'de 4,07 m² por chapa')
#   ⭐ BARROTEAMENTO: malha de 60 × 120, que é o que forro de 18 mm pede
forro.m('Sarrafo de pinus · barroteamento, malha de 60 × 120',
        b.FORRO_M2 / 0.60 + b.FORRO_M2 / 1.20, b.SARRAFO_M, 'm',
        'barrote a cada 60 cm mais travessa a cada 120 · é o que segura o forro')
#   ⭐ MÃO AMIGA: 10 escoras em T, cada uma com um pé de 2,91 m mais a
#     travessa de 60 cm que distribui a pressão na placa
MAO_AMIGA_N = 10
forro.m('Sarrafo de pinus · MÃO AMIGA, escora em T de montagem',
        MAO_AMIGA_N * (b.PE_DIREITO / 100 + 0.60), b.SARRAFO_M, 'm',
        '⭐ %d escoras · o pé vai do piso ao forro (2,91 m) e a travessa de '
        '60 cm espalha a pressão sem marcar a placa' % MAO_AMIGA_N)
forro.m('Fita de borda de cor, 22 mm · perímetro do forro',
        FORRO_PERIM * b.FITA_PERDA, b.FITA_22, 'm',
        '⚠ perímetro ESTIMADO: a prancha dá a área, não o contorno')
forro.m('Filetagem na coladeira automática', FORRO_PERIM * b.FITA_PERDA,
        b.FILETE_MAQ, 'm', '')

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
                '%d nichos de %.0f × %.0f mais o arco de passagem de %.0f · '
                'moldura de %.0f cm, %.0f cm de profundidade'
                % (b.N_NICHOS, b.NICHO_L, b.NICHO_H, b.PASSAGEM_L,
                   b.MOLDURA_L, b.NICHO_PROF))

ARCOS = [('nicho', b.N_NICHOS, b.NICHO), ('passagem', 1, b.PASSAGEM)]
for rot, n, A in ARCOS:
    #   2 costelas por pórtico: uma na boca, outra no fundo da profundidade
    porticos.p('Moldura estrutural do arco de %s · costela' % rot,
               A['envolvente_l'], A['envolvente_a'], 2 * n, AMA, 18,
               '⛔ retângulo do recorte, não o perímetro · o miolo volta ao corte')
    #   compensado flexível: intradorso e extradorso, ao longo da profundidade
    porticos.p('Compensado flexível do arco de %s · intradorso' % rot,
               A['interno'], b.NICHO_PROF, n, FLEX, 4,
               'a superfície curva de dentro, que se vê do vão')
    porticos.p('Compensado flexível do arco de %s · extradorso' % rot,
               A['externo'], b.NICHO_PROF, n, FLEX, 4,
               'a superfície curva de fora, que fecha a estrutura')
    #   alizar de acabamento externo, arrematando contra a parede
    porticos.p('Alizar de acabamento do arco de %s' % rot,
               A['externo'], b.ALIZAR_L, n, AMA, 18,
               '⚠ largura de %.0f cm é premissa: a prancha não cota o alizar'
               % b.ALIZAR_L)

#   ⭐ A LACA, só no que se vê: face frontal de 12 cm, intradorso e alizar.
#     O extradorso fica revestido e cru, escondido nos 6 cm entre pórticos.
_face = sum(n * A['medio'] * b.MOLDURA_L for _r, n, A in ARCOS) / 10000
_intra = sum(n * A['interno'] * b.NICHO_PROF for _r, n, A in ARCOS) / 10000
_aliz = sum(n * A['externo'] * b.ALIZAR_L for _r, n, A in ARCOS) / 10000
LACA_M2 = _face + _intra + _aliz
_extra = sum(n * A['externo'] * b.NICHO_PROF for _r, n, A in ARCOS) / 10000
porticos.s('Laca café · face, intradorso e alizar', LACA_M2, b.LACA_M2, 'm²',
           '⭐ R$ 650,00 o m², DECISÃO DO JONATHAN [23/11/2026: "laca '
           'considere 650"] · é a linha ALTA da Base, "Laca ou pintura em '
           'peça lisa" do materiais.json, e não a de R$ 300 dos jobs, que eu '
           'havia lançado · ⭐ e é o lugar certo, porque as duas linhas da '
           'Base falam de peça LISA e curva leva mais lixa e mais tempo · '
           '⛔ o extradorso (%s m²) está revestido e NÃO lacado: ele some '
           'nos 6 cm entre pórticos'
           % ('%0.2f' % _extra).replace('.', ','))

# ═══════════════════════════════════════════════════════════════════════
#   03 · OS NICHOS POR DENTRO · fundo e prateleiras
# ═══════════════════════════════════════════════════════════════════════
#   ⭐ "as prateleiras serao de mdf e precisa de alma de aço e com
#     iluminação de led" [Jonathan, 23/11/2026]
#   ⭐ ALMA DE AÇO: a Base manda "uma por peça, contra empeno". Prateleira
#     de 104 cm de vão sem apoio no meio empena — é o caso exato.
nichos = Item('Nichos por dentro · fundo, prateleira e luz',
              '%d fundos e %d prateleiras de %.0f × %.0f, com alma de aço '
              'e LED em cada uma'
              % (b.N_NICHOS, b.N_NICHOS * b.PRAT_POR_NICHO,
                 b.NICHO_L, b.NICHO_PROF))
#   fundo: o retângulo reto mais a abóbada (meia elipse)
FUNDO_M2 = (b.NICHO_L * b.NICHO_RETO / 10000
            + math.pi * (b.NICHO_L / 2) * b.NICHO_ABOBADA / 2 / 10000)
nichos.p('Fundo do nicho · era ADESIVO na prancha', b.NICHO_L, b.NICHO_H,
         b.N_NICHOS, AMA, 18,
         '⭐ decisão do Jonathan: onde a prancha diz adesivo, vai painel de MDF')
N_PRAT = b.N_NICHOS * b.PRAT_POR_NICHO
nichos.p('Prateleira do nicho', b.NICHO_L, b.NICHO_PROF, N_PRAT, AMA, 18,
         '%d prateleiras · %d por nicho, contadas na VISTA BB ampliada'
         % (N_PRAT, b.PRAT_POR_NICHO),
         fita=(b.NICHO_L + 2 * b.NICHO_PROF) / 100)
nichos.s('Alma de aço · barra chata de 3 m', math.ceil(N_PRAT * b.NICHO_L
         / b.ALMA_M), b.ALMA_BARRA, 'barra',
         '⭐ uma alma por prateleira, como a Base manda · %d prateleiras de '
         '%.0f cm dão %.0f m de barra' % (N_PRAT, b.NICHO_L,
                                          N_PRAT * b.NICHO_L / 100))
LED_TOTAL = N_PRAT * b.NICHO_L / 100
nichos.m('LED COB · conjunto completo, uma régua por prateleira', LED_TOTAL,
         b.LED_M, 'm',
         '⭐ CONJUNTO: fita, perfil, usinagem e instalação · a Base avisa que '
         'o LED instalado vai de R$ 66 a R$ 150 conforme o que a linha inclui, '
         'e prateleira que acende é o conjunto inteiro')
nichos.s('Fonte de LED', math.ceil(LED_TOTAL / 9), b.LED_FONTE, 'un',
         'uma a cada 8 a 10 m de régua')

# ═══════════════════════════════════════════════════════════════════════
#   04 · OS PAINÉIS DE PAREDE · o que era adesivo
# ═══════════════════════════════════════════════════════════════════════
paineis = Item('Painéis de parede · o que era adesivo',
               'onde a prancha sinaliza ADESIVO, vai painel de MDF '
               'amadeirado, no mesmo padrão do forro')
for rot, L, A in b.PAINEIS:
    paineis.p(rot, L, A, 1, AMA, 18, '', fita=2 * (L + A) / 100)
PAINEL_M2 = sum(L * A / 10000 for _r, L, A in b.PAINEIS)
paineis.m('Sarrafo de pinus · estrutura de fixação, montante a cada 60',
          PAINEL_M2 / 0.60, b.SARRAFO_M, 'm',
          'o painel é PELE sobre a alvenaria: o sarrafo aprumado é o que '
          'recebe o parafuso')

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
                '%s m² de base em MDF 18 mm, aprumada e plana, onde o '
                'espelho vai colado' % ('%0.2f' % sum(
                    L * A / 10000 for _r, L, A in b.ESPELHOS)).replace('.', ','))
for rot, L, A in b.ESPELHOS:
    base_esp.p(rot.replace('espelho', 'base do espelho'), L, A, 1,
               b.ESPELHO_SUBSTRATO, 18,
               '⭐ Branco TX, não amadeirado: a face some inteira sob o '
               'espelho e a chapa custa R$ 400 em vez de R$ 700')
ESP_M2 = sum(L * A / 10000 for _r, L, A in b.ESPELHOS)
base_esp.m('Sarrafo de pinus · estrutura de fixação, montante a cada 60',
           ESP_M2 / 0.60, b.SARRAFO_M, 'm',
           '⛔ espelho colado não perdoa barriga na base: o sarrafo '
           'aprumado é o que garante o plano')

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
               'área da folha e área do painel são a mesma coisa')
espelhos.s('Frete de espelho', 1, b.ESPELHO_FRETE, 'serviço',
           'a Base tem a linha, por serviço · chapa de espelho não vai '
           'junto com a carga de marcenaria')

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
        rend = b.COMP_FLEX_REND if k[0] == FLEX else b.REND
        n = math.ceil(round(v / rend, 6))
        chapas[k] = n
        c_chapa += n * b.PRECO['%s %d' % k]
    c_fita = sum(it.c_fita() for it in ITENS) * b.FITA_PERDA * b.FITA_22
    c_filete = sum(it.c_fita() for it in ITENS) * b.FITA_PERDA * b.FILETE_MAQ
    c_lin = sum(it.c_lin() for it in ITENS)
    c_serv = sum(it.c_serv() for it in ITENS)
    n_ch = sum(chapas.values())
    n_pc = sum(it.n_pecas() for it in ITENS)
    c_corte = n_ch * b.CORTE_CHAPA + n_pc * b.CORTE_PECA
    c_cons = (c_chapa + c_fita) * b.CONSUMIVEIS
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
    for rot, v in [('Chapa · %d chapas' % T['n_ch'], T['c_chapa']),
                   ('Fita de borda, material', T['c_fita']),
                   ('Filetagem, aplicação', T['c_filete']),
                   ('Sarrafo, alma de aço e LED', T['c_lin']),
                   ('Laca, fonte e avulsos', T['c_serv']),
                   ('Corte · %d chapas e %d peças' % (T['n_ch'], T['n_pc']),
                    T['c_corte']),
                   ('Consumíveis · 6%% sobre chapa e fita', T['c_cons']),
                   ('Embalagem · 3%%', T['c_emb'])]:
        print('  %-44s %16s' % (rot, brl(v)))
    print('  %-44s %16s' % ('CUSTO DIRETO', brl(T['direto'])))
