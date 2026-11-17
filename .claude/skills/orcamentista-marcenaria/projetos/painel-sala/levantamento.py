# -*- coding: utf-8 -*-
"""PAINEL DA SALA — VISTA 2 · o quantitativo, peça a peça.

GEOMETRIA LIDA DAS PRANCHAS
  Painel corrido de 682 de largura × 277 de altura, sobre sóculo de 15.
  Volume de 50 de profundidade (vista lateral e perspectiva, 1/30).

  ┌── 0 ───────── 50 ─────────────────── 352 ──── 366 ── 449 ─── 592 ─ 662 ─ 682
  │   porta ripada │   nicho de pedra 302   │  ←──── PAINEL LISO 330 ────────→
  │   50 × 277     │   (75 ripado em cima,  │       porta 83    porta 70
  │                │    131 de pedra,       │       × 210       × 210
  │                │    71 ripado embaixo)  │
  └──────── RIPADO 352 ────────────────────┘

  Alturas, da vista lateral 1/30:  75 | 4 | 123 | 4 | 71 | 15  =  292
  O 4 + 123 + 4 = 131 é o "NICHO 131X302CM EM MÁRMORE TRAVERTINO ROMANO".

⛔⛔ A FRONTEIRA DO ESCOPO — regra 19 [Jonathan, 29/10/2026]: "pedra nao é
  escopo da marcenaria". Ficam FORA, e não se lançam nem a zero:
    · o NICHO 131 × 302 em mármore travertino romano estucado
    · o SÓCULO em ALVENARIA revestido de mármore (a prancha diz alvenaria)
    · o RODAPÉ de 15 cm em mármore travertino
    · a JANELA 202 × 175 em vidro laminado com estrutura metálica preta
  ⭐ A fita de LED do nicho é NOSSA: ela é usinada e embutida na marcenaria.

⚠ O QUE EU ASSUMI, e está na lista de dúvidas: o painel é PELE sobre
  estrutura/alvenaria existente — a prancha diz "sóculo em alvenaria", e o
  nicho é revestido pelo marmorista. Orço a pele, as três folhas de porta e
  a estrutura de fixação. ⛔ O INTERIOR do "ARMÁRIO 50X274" atrás da porta
  ripada NÃO está desenhado em lugar nenhum — não tem prateleira, divisória
  nem profundidade útil cotada — e por isso NÃO está orçado.
"""
import math, importlib.util, pathlib

_aqui = pathlib.Path(__file__).resolve().parent
_sp = importlib.util.spec_from_file_location('ps_base', _aqui / 'base.py')
b = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(b)

GIA = 'MDF Gianduia'
EST = 'MDF Branco TX'

# ── as cotas, uma vez só ────────────────────────────────────────────────
LARG, ALT = 682.0, 277.0
R_PORTA_L = 50.0                      # porta ripada do armário
NICHO_L, NICHO_H = 302.0, 131.0       # o vazio de pedra
R_SUP, R_INF = 75.0, 71.0             # bandas ripadas acima e abaixo
RIPADO_L = R_PORTA_L + NICHO_L        # 352 · até onde termina a pedra
LISO_L = LARG - RIPADO_L              # 330
PORTAS = [(83.0, 210.0), (70.0, 210.0)]   # mimetizadas, do chão
assert abs(R_SUP + 4 + 123 + 4 + R_INF - ALT) < 1e-9


class Item:
    def __init__(self, nome, obs=''):
        self.nome, self.obs = nome, obs
        self.pecas, self.terc, self.fer = [], [], []

    def p(self, nome, L, A, esp, mat=GIA, qtd=1, fita=0.0, obs=''):
        self.pecas.append(dict(nome=nome, L=L, A=A, esp=esp, mat=mat,
                               qtd=qtd, fita=fita, obs=obs))
        return self

    def t(self, nome, q, unit, un='m'):
        if q: self.terc.append((nome, q, unit, un))
        return self

    def f(self, nome, q, unit):
        if q: self.fer.append((nome, q, unit))
        return self

    def ripado(self, larg, alt, nome):
        """⭐⭐ O PADRÃO DE COTAÇÃO DA CASA PARA RIPADO, com o passo DESTE
        projeto (4 cm, não 6). Três linhas, sempre as mesmas:
          1. a ÁREA EQUIVALENTE de chapa das ripas — ripa não é peça;
          2. a mão de obra de painel ripado, por m² de FACE;
          3. a filetagem das DUAS faces de cada ripa, por metro.
        ⛔ A ripa NÃO entra na contagem de peças do corte: quem paga o corte
          de 164 tiras é a linha de mão de obra, e cobrar os dois é cobrar
          duas vezes o mesmo serviço."""
        n = int(larg // b.PASSO)
        self.p(f'{nome} · {n} ripas de {b.RIPA_L:g} × {alt:.0f}',
               b.RIPA_L * n * b.RIPA_PERDA, alt, b.RIPA_ESP_MM, GIA, 1,
               obs=f'área equivalente · passo {b.PASSO:g} cm')
        self.t('Painel ripado, mão de obra', larg * alt / 10000, b.RIPADO_M2, 'm²')
        self.t('Filetagem de ripa, duas faces', n * alt / 100 * 2, b.FILETE_RIPA)
        return self


M = []
def novo(nome, obs=''):
    it = Item(nome, obs); M.append(it); return it


# ════════════════════════════════════════════════════════════════════════
# 01 · PAINEL RIPADO — 352 × 277, até onde a pedra termina
# ════════════════════════════════════════════════════════════════════════
it = novo('Painel ripado com o vão do nicho',
          f'{RIPADO_L:.0f} × {ALT:.0f} · trama 20/20, passo 4 cm')
#   ⛔ O SUBSTRATO SAI NO MESMO GIANDUIA. O vão de 2 cm tem 2 cm de fundo:
#     vê-se o que está atrás da ripa. Branco ou cru apareceria na obra.
it.p('Substrato do ripado · banda superior', NICHO_L, R_SUP,
     b.SUBSTRATO_ESP_MM, GIA, 1, NICHO_L / 100, 'topo do vão do nicho')
it.p('Substrato do ripado · banda inferior', NICHO_L, R_INF,
     b.SUBSTRATO_ESP_MM, GIA, 1, NICHO_L / 100, 'base do vão do nicho')
it.ripado(NICHO_L, R_SUP, 'Ripado da banda superior')
it.ripado(NICHO_L, R_INF, 'Ripado da banda inferior')

# ════════════════════════════════════════════════════════════════════════
# 02 · PORTA RIPADA DO ARMÁRIO — 50 × 277, mimetizada
# ════════════════════════════════════════════════════════════════════════
#   ⚠ A prancha chama de "ARMÁRIO 50X274CM RIPADO EM MDF GIANDUIA TRAMA".
#     Oriento-me pelo DETALHE 1/30, que dá 277 de folha sobre o sóculo.
it = novo('Porta ripada do armário, mimetizada',
          f'{R_PORTA_L:.0f} × {ALT:.0f} · folha inteira, sem puxador')
#   ⭐ Folha de 18 mm, não 15: 2,77 m de altura numa folha de 50 de largura
#     empena se for fina, e ela ainda recebe 12 ripas coladas na frente.
it.p('Folha da porta', R_PORTA_L, ALT, 18, GIA, 1, (R_PORTA_L + ALT) * 2 / 100)
it.ripado(R_PORTA_L, ALT, 'Ripado da porta')
it.f('Sistema pivô de porta mimetizada', 1, b.SISTEMA_PIVO)
it.f('Fecho rolete', 1, b.FECHO_ROLETE)

# ════════════════════════════════════════════════════════════════════════
# 03 · PAINEL LISO — 330 × 277, do fim da pedra para a direita
# ════════════════════════════════════════════════════════════════════════
#   ⭐⭐ [Jonathan, 17/11/2026] "Do nicho de pedra para a direita, o painel
#     vai ser liso com as duas portas mimetizadas, mas não vai ser ripado."
#     São 9,14 m² de face que deixam de levar ripa, filetagem e mão de obra
#     de painel ripado — e passam a levar chapa de 18 inteira, porque aqui
#     a face vista É a melamina.
it = novo('Painel liso com os vãos das duas portas',
          f'{LISO_L:.0f} × {ALT:.0f} · face melamínica, sem ripa')
_h_sup = ALT - PORTAS[0][1]            # 67 · faixa acima das portas
#   ⛔ 330 cm NÃO SAI DE UMA CHAPA DE 275: a faixa superior é emendada.
it.p('Faixa superior sobre as portas', LISO_L / 2, _h_sup, 18, GIA, 2,
     (LISO_L / 2 + _h_sup) * 2 / 100, 'emendada · 330 > 273 de peça')
#   as três faixas verticais que sobram ao lado e entre as portas
_x = [(RIPADO_L, 366.0), (449.0, 592.0), (662.0, LARG)]
for i, (a, z) in enumerate(_x, 1):
    it.p(f'Faixa vertical {i} entre vãos', z - a, PORTAS[0][1], 18, GIA, 1,
         ((z - a) + PORTAS[0][1]) * 2 / 100)

# ════════════════════════════════════════════════════════════════════════
# 04 · AS DUAS PORTAS MIMETIZADAS DE PASSAGEM
# ════════════════════════════════════════════════════════════════════════
#   ⚠ São portas DE PASSAGEM, não de armário: 210 de altura, arco de
#     abertura para dentro da sala e arranque NO PISO — elas cruzam a linha
#     do sóculo de pedra. Por isso levam marco, e não dobradiça de caixa.
it = novo('Duas portas mimetizadas de passagem',
          '83 × 210 e 70 × 210 · face lisa, alinhadas ao painel')
for i, (L, A) in enumerate(PORTAS, 1):
    it.p(f'Folha da porta {i} · {L:.0f} × {A:.0f}', L, A, 18, GIA, 1,
         (L + A) * 2 / 100)
    it.p(f'Marco mimetizado da porta {i}', 2 * A + L, 12, 18, GIA, 1,
         (2 * A + L) / 100)
    it.f('Sistema pivô de porta mimetizada', 1, b.SISTEMA_PIVO)
    it.f('Fecho rolete', 1, b.FECHO_ROLETE)

# ════════════════════════════════════════════════════════════════════════
# 05 · ESTRUTURA DE FIXAÇÃO E ILUMINAÇÃO DO NICHO
# ════════════════════════════════════════════════════════════════════════
#   ⛔ REGRA 1 DA CASA: pinus está proibido. O que segurava o painel em
#     sarrafo passa a ser TRAVESSA DE MDF, tirada da própria chapa.
it = novo('Estrutura de fixação do painel',
          'montantes a cada 60 cm e três fiadas de travessa')
it.p('Montantes verticais a cada 60 cm', 8, ALT, 18, EST, 12,
     obs='não aparece · MDF branco')
it.p('Travessas horizontais', LARG / 2, 8, 18, EST, 6,
     obs='três fiadas, emendadas')

#   ⭐ "PREVER FITA DE LED NO NICHO 3000K" — a prancha escreve em duas
#     folhas. É usinagem na marcenaria, então é nossa.
it = novo('Iluminação do nicho',
          'fita 3000K no topo do vão, perfil de embutir e difusor')
it.t('Fita LED 3000K, perfil de embutir e difusor', NICHO_L / 100, b.LED_M)
it.f('Fonte de LED', 1, b.LED_FONTE)


# ════════════════════════════════════════════════════════════════════════
# O CUSTO
# ════════════════════════════════════════════════════════════════════════
def _levanta(it):
    area, fita, pecas = {}, 0.0, 0
    for p in it.pecas:
        k = (p['mat'], p['esp'])
        area[k] = area.get(k, 0.0) + p['L'] * p['A'] / 10000 * p['qtd']
        pecas += p['qtd']
        fita += p['fita'] * p['qtd']
    return dict(area=area, fita=fita, pecas=pecas,
                c_terc=sum(q * u for _n, q, u, _un in it.terc),
                c_fer=sum(q * u for _n, q, u in it.fer))


def custo(itens, arredonda=True):
    """⭐⭐ O ARREDONDAMENTO DE CHAPA É DO PROJETO, NÃO DO ITEM, e a sobra é
    RATEADA pela área. Assim a soma dos itens É o custo do projeto."""
    L = [(it, _levanta(it)) for it in itens]
    area = {}
    for _it, q in L:
        for k, a in q['area'].items():
            area[k] = area.get(k, 0.0) + a
    rend = b.CHAPA_M2 * b.APROV
    chapas = {k: (math.ceil(a / rend) if arredonda else a / rend)
              for k, a in area.items()}
    preco = {k: b.PRECO[f'{k[0]} {k[1]}'] for k in area}
    c_chapa = sum(n * preco[k] for k, n in chapas.items())
    sobra = {k: chapas[k] * preco[k] - area[k] / rend * preco[k] for k in area}
    n_chapas, n_pecas = sum(chapas.values()), sum(q['pecas'] for _i, q in L)

    def _item(q):
        ch = sum(a / rend * preco[k] + sobra[k] * (a / area[k])
                 for k, a in q['area'].items())
        corte = (n_chapas * b.CORTE_CHAPA * (q['pecas'] / n_pecas)
                 + q['pecas'] * b.CORTE_PECA)
        fita = q['fita'] * b.FITA_COR * b.FITA_PERDA
        cons = (ch + fita) * b.CONSUMIVEIS
        return (ch + fita + corte + cons + q['c_terc'] + q['c_fer']) * (1 + b.EMBALAGEM)

    c_fita = sum(q['fita'] for _i, q in L) * b.FITA_COR * b.FITA_PERDA
    diretos = [_item(q) for _it, q in L]
    c_frete = b.VIAGENS * b.FRETE_VIAGEM
    soma = sum(diretos)
    diretos = [d + c_frete * (d / soma) for d in diretos]
    return dict(area=area, chapas=chapas, preco=preco, c_chapa=c_chapa,
                pecas=n_pecas, n_chapas=n_chapas,
                fita=sum(q['fita'] for _i, q in L), c_fita=c_fita,
                c_corte=n_chapas * b.CORTE_CHAPA + n_pecas * b.CORTE_PECA,
                c_cons=(c_chapa + c_fita) * b.CONSUMIVEIS,
                c_terc=sum(q['c_terc'] for _i, q in L),
                c_fer=sum(q['c_fer'] for _i, q in L),
                c_frete=c_frete, diretos=diretos, direto=sum(diretos), L=L)


def brl(v):
    return f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')


T = custo(M)
DIRETO = T['direto']


# ════════════════════════════════════════════════════════════════════════
# A TABELA — é o que o Jonathan pediu antes da proposta
# ════════════════════════════════════════════════════════════════════════
def _ripas():
    """⭐ O número que ele pediu em primeiro lugar: quantas ripas e quantos
    metros de filete. Separado por banda, porque a fábrica corta assim."""
    R = []
    for larg, alt, rot in [(R_PORTA_L, ALT, 'Porta ripada'),
                           (NICHO_L, R_SUP, 'Banda superior do nicho'),
                           (NICHO_L, R_INF, 'Banda inferior do nicho')]:
        n = int(larg // b.PASSO)
        R.append((rot, larg, alt, n, n * alt / 100, n * alt / 100 * 2,
                  larg * alt / 10000))
    return R


if __name__ == '__main__':
    L, S = 74, '─'
    print(f'\n  PAINEL DA SALA · VISTA 2 — LEVANTAMENTO DE CUSTOS')
    print(f'  {b.EXECUTIVO}')
    if b.ESPECIAL:
        print('  ⚠ rodando na linha ESPECIAL de R$ 1.000 a chapa')

    print(f'\n  ① A RIPA  ' + S * (L - 10))
    print(f'  {"BANDA":<26}{"FACE":>12}{"RIPAS":>8}{"RIPA m":>10}'
          f'{"FILETE m":>10}{"m² FACE":>8}')
    tn = tf = tm = 0.0
    for rot, larg, alt, n, mr, mf, m2 in _ripas():
        print(f'  {rot:<26}{f"{larg:.0f} × {alt:.0f}":>12}{n:>8}'
              f'{mr:>10.1f}{mf:>10.1f}{m2:>8.2f}')
        tn += n; tf += mf; tm += m2
    print(f'  {"TOTAL":<26}{"":>12}{int(tn):>8}{"":>10}{tf:>10.1f}{tm:>8.2f}')
    print(f'  {"":<26}passo {b.PASSO:g} cm · ripa {b.RIPA_L:g} · vão '
          f'{b.RIPA_VAO:g} · {25:.0f} ripas por metro')

    print(f'\n  ⚠ CONTRA O PASSO PADRÃO DA CASA (ripa 4, vão 2 · passo 6)')
    _n6 = sum(int(l // 6.0) for l, _a, _r in
              [(R_PORTA_L, ALT, 0), (NICHO_L, R_SUP, 0), (NICHO_L, R_INF, 0)])
    _f6 = sum(int(l // 6.0) * a / 100 * 2 for l, a in
              [(R_PORTA_L, ALT), (NICHO_L, R_SUP), (NICHO_L, R_INF)])
    print(f'  {"":<26}{"ESTE (20/20)":>14}{"CASA (40/20)":>14}{"A MAIS":>12}')
    print(f'  {"ripas":<26}{int(tn):>14}{_n6:>14}{int(tn)-_n6:>12}')
    print(f'  {"metros de filete":<26}{tf:>14.1f}{_f6:>14.1f}{tf-_f6:>12.1f}')
    print(f'  {"custo da filetagem":<26}'
          f'{brl(tf*b.FILETE_RIPA):>14}{brl(_f6*b.FILETE_RIPA):>14}'
          f'{brl((tf-_f6)*b.FILETE_RIPA):>12}')

    print(f'\n  ② AS FACES  ' + S * (L - 12))
    _liso = LISO_L * ALT / 10000
    _port = sum(x * y for x, y in PORTAS) / 10000
    for rot, v in [('Ripado · com ripa, filete e mão de obra', tm),
                   ('Liso · só chapa melamínica', _liso - _port),
                   ('Portas mimetizadas de passagem', _port),
                   ('Porta ripada do armário (já no ripado)', 0.0)]:
        if v: print(f'  {rot:<50}{v:>10.2f} m²')
    print(f'  {"TOTAL DE FACE":<50}{tm + _liso:>10.2f} m²')

    print(f'\n  ③ O CUSTO POR ITEM  ' + S * (L - 20))
    for (it, q), d in zip(T['L'], T['diretos']):
        print(f'  {it.nome:<52}{brl(d):>20}')
        print(f'    {it.obs}')
    print(f'  {"CUSTO DIRETO":<52}{brl(DIRETO):>20}')

    print(f'\n  ④ O CUSTO POR NATUREZA  ' + S * (L - 24))
    for k, n in sorted(T['chapas'].items()):
        rot = '%s %d mm · %.2f m²' % (k[0], k[1], T['area'][k])
        print(f'  {rot:<36}{n:>3} chapas ×{brl(T["preco"][k]):>10}'
              f'{brl(n * T["preco"][k]):>21}')
    _emb = DIRETO - T['c_frete'] - (T['c_chapa'] + T['c_fita'] + T['c_corte']
                                    + T['c_cons'] + T['c_fer'] + T['c_terc'])
    for rot, v in [(f'Fita de borda · {T["fita"]:.1f} m', T['c_fita']),
                   (f'Corte · {T["n_chapas"]} chapas, {T["pecas"]} peças', T['c_corte']),
                   ('Consumíveis · 6%', T['c_cons']),
                   ('Terceirizados · ripado, filete e LED', T['c_terc']),
                   ('Ferragem · 3 pivôs e 3 fechos, fonte', T['c_fer']),
                   (f'Frete · {b.VIAGENS} viagens', T['c_frete']),
                   ('Embalagem · 2%', _emb)]:
        print(f'  {rot:<52}{brl(v):>20}')
    print(f'  {"CUSTO DIRETO":<52}{brl(DIRETO):>20}')

    print(f'\n  ⑤ O QUE O TERCEIRIZADO PESA  ' + S * (L - 29))
    _ag = {}
    for it, _q in T['L']:
        for n, qt, u, un in it.terc:
            a = _ag.setdefault(n, [0.0, u, un]); a[0] += qt
    for n, (qt, u, un) in _ag.items():
        print(f'  {n:<40}{qt:>9.2f} {un:<4}×{brl(u):>9}{brl(qt * u):>16}')

    print(f'\n  ⑥ A RÉGUA DE PREÇO  ' + S * (L - 20))
    print('  ⚠ Nenhum preço foi fechado: o Jonathan pediu o CUSTO, não a MC.')
    print(f'  {"":<30}{"MC 35%":>20}{"MC 40%":>20}')
    for rot, base in [('sem RT', b.BASE_SEM_RT), ('com RT de 10%', b.BASE_COM_RT)]:
        print(f'  {rot:<30}'
              f'{brl(DIRETO / (base - b.FAIXA[0])):>20}'
              f'{brl(DIRETO / (base - b.FAIXA[1])):>20}')
