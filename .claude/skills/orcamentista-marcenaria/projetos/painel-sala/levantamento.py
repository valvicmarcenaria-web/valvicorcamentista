# -*- coding: utf-8 -*-
"""PAINEL DA SALA — VISTA 2 · o quantitativo, refeito sobre a Base de Custos.

GEOMETRIA (pranchas SALA - VISTA 2, 1/50, e NICHO RIPADO, 1/30, pág. 18)
  Painel corrido de 682 × 277, sobre sóculo de pedra de 15 (292 no total).

  ┌── 0 ───────── 50 ─────────────────── 352 ──── 366 ── 449 ─── 592 ─ 662 ─ 682
  │   porta ripada │   nicho de pedra 302   │  ←──── PAINEL LISO 330 ────────→
  │   50 × 277     │   75 ripado em cima    │       porta 83    porta 70
  │   ARMÁRIO      │  131 de pedra          │       × 210       × 210
  │                │   71 ripado embaixo    │       PASSAGEM, 42 mm
  └──────── RIPADO 352 ────────────────────┘

⛔ FORA, por regra 19 e por ordem do Jonathan:
   · nicho 131 × 302 em mármore travertino romano estucado
   · sóculo em ALVENARIA revestido de mármore · rodapé de 15 cm em mármore
   · janela 202 × 175 em vidro laminado com estrutura metálica
   · ⭐ A ILUMINAÇÃO DO NICHO — "iluminação nao é nossa" [17/11/2026].
     A prancha escreve "PREVER fita de LED no nicho 3000K" nas duas folhas,
     e PREVER é o elétrico. A marcenaria deixa o rasgo; a fita é de outro.
"""
import math, importlib.util, pathlib

_aqui = pathlib.Path(__file__).resolve().parent
_sp = importlib.util.spec_from_file_location('ps_base', _aqui / 'base.py')
b = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(b)

GIA, EST = 'MDF Gianduia', 'MDF Branco TX'

# ── as cotas, uma vez só ────────────────────────────────────────────────
LARG, ALT = 682.0, 277.0
R_PORTA_L = 50.0
NICHO_L, NICHO_H = 302.0, 131.0
R_SUP, R_INF = 75.0, 71.0
RIPADO_L = R_PORTA_L + NICHO_L           # 352
LISO_L = LARG - RIPADO_L                 # 330
PORTAS = [(83.0, 210.0), (70.0, 210.0)]
assert abs(R_SUP + 4 + 123 + 4 + R_INF - ALT) < 1e-9


class Item:
    def __init__(self, nome, obs=''):
        self.nome, self.obs = nome, obs
        self.pecas, self.terc, self.fer = [], [], []
        self.fita22 = self.fita50 = self.fita_ripa = 0.0

    def p(self, nome, L, A, esp, mat=GIA, qtd=1, f22=0.0, f50=0.0, obs=''):
        self.pecas.append(dict(nome=nome, L=L, A=A, esp=esp, mat=mat,
                               qtd=qtd, f22=f22, f50=f50, obs=obs))
        self.fita22 += f22 * qtd
        self.fita50 += f50 * qtd
        return self

    def t(self, nome, q, unit, un='m'):
        if q: self.terc.append((nome, q, unit, un))
        return self

    def f(self, nome, q, unit):
        if q: self.fer.append((nome, q, unit))
        return self

    def ripado(self, larg, alt, nome):
        """⭐⭐ O RIPADO, AGORA COM AS TRÊS LINHAS QUE ELE TEM — e não com
        duas, como eu tinha feito:
          1. ÁREA EQUIVALENTE de chapa das ripas, com a perda de serra 1,10
             da linha "Perda de serra ao tirar ripa" dos Terceirizados;
          2. FITA MAIS FILETAGEM das duas faces de cada ripa. ⛔ Eu cobrava
             só a filetagem. A fita de 285 metros não existia no orçamento.
             E a filetagem é MANUAL: coladeira automática não pega peça de
             20 mm de largura, e a Base nomeia o caso.
          3. a mão de obra de painel ripado, por m² de FACE.
        ⛔ A ripa NÃO entra na contagem de peças do corte — quem paga o
          corte das tiras é a linha de mão de obra."""
        n = int(larg // b.PASSO)
        self.p(f'{nome} · {n} ripas de {b.RIPA_L:g} × {alt:.0f}',
               b.RIPA_L * n * b.RIPA_PERDA, alt, b.RIPA_ESP_MM, GIA, 1,
               obs=f'área equivalente · passo {b.PASSO:g} · perda de serra 1,10')
        #   as duas faces de cada ripa, mais os dois topos
        self.fita_ripa += n * alt / 100 * 2 + n * b.RIPA_L / 100 * 2
        self.t('Painel ripado, mão de obra', larg * alt / 10000, b.RIPADO_M2, 'm²')
        return self

    def caixa(self, L, A, P, vaos, nome):
        """⭐⭐ A CAIXA QUE AS BANDAS NÃO TINHAM [Jonathan, 18/11/2026].
        Até ontem a banda do nicho era uma PELE: uma chapa com ripas
        coladas. Agora ela é armário, e armário tem lateral, divisória,
        tampo, base, fundo e prateleira — mais a ferragem de cada folha.
        ⛔ Peça com mais de 273 cm não existe: a chapa é 275 e a sangria é
          2. Tampo, base e fundo de 302 saem EMENDADOS, e é por isso que a
          conta é de área e não de peça inteira."""
        n_lat = vaos + 1
        self.p(f'{nome} · laterais e divisórias', P, A, b.ESP_ESTRUTURA,
               GIA, n_lat, f22=A / 100)
        emenda = 2 if L > b.ALT_MAX else 1
        self.p(f'{nome} · tampo e base', L / emenda, P, b.ESP_ESTRUTURA,
               GIA, 2 * emenda, f22=L / emenda / 100,
               obs='emendado' if emenda > 1 else '')
        self.p(f'{nome} · fundo', L / emenda, A, b.ESP_FUNDO, GIA, emenda,
               obs='⛔ fundo em Gianduia: a caixa é vista com a porta aberta')
        larg = (L - n_lat * 1.5) / vaos
        self.p(f'{nome} · prateleiras', larg, P - 2, 18, GIA, vaos,
               f22=larg / 100)
        self.f('Suporte de prateleira, jogo de 4', vaos, b.SUPORTE_JOGO)
        return self

    def folhas_ripadas(self, L, A, vaos, nome):
        """⭐ A base do ripado deixa de ser UM painel e vira N FOLHAS DE
        PORTA. A área é a mesma e as ripas são as mesmas — o que muda é a
        fita, que passa a ter o perímetro de cada folha, e a ferragem.
        ⛔ A junta das folhas cai dentro do vão de 2 cm da trama: fechadas,
          elas somem, e é por isso que a prancha não desenha divisão."""
        larg = L / vaos
        self.p(f'{nome} · {vaos} folhas de {larg:.1f} × {A:.0f}'.replace('.', ','),
               larg, A, b.ESP_PORTA, GIA, vaos, f22=(larg + A) * 2 / 100,
               obs='BASE onde as ripas são coladas')
        return self

    def porta_passagem(self, L, A, i):
        """⛔⛔ 42 MM, e não 18. A aba MDF crava "Portas de passagem · 42 mm"
        em "ESPESSURA PADRÃO POR APLICAÇÃO". Folha de 42 é tamponamento:
        18 + 18 + 6, a MESMA ÁREA TRÊS VEZES. As duas faces em Gianduia —
        ⚠ a de dentro é vista do outro ambiente e o acabamento de lá não
        está nas pranchas — e o miolo em Branco TX, que ninguém vê.
        ⛔ E a borda de 42 mm NÃO leva fita de 22: leva a de 50, que a Base
          lista a R$ 7,00 "para peça de 5 cm"."""
        for j, (esp, mat) in enumerate(b.PASSAGEM_CAMADAS):
            cam = ('face vista', 'face oposta', 'miolo')[j]
            self.p(f'Porta {i} · {cam} {esp} mm', L, A, esp, mat, 1,
                   f50=(L + A) * 2 / 100 if j == 0 else 0.0,
                   obs='tamponamento de 42 mm' if j == 0 else '')
        self.f('Sistema pivô de porta mimetizada', 1, b.SISTEMA_PIVO)
        self.f('Fecho rolete para porta pivotante', 1, b.FECHO_ROLETE)
        return self


M = []
def novo(nome, obs=''):
    it = Item(nome, obs); M.append(it); return it


# ════════════════════════════════════════════════════════════════════════
# 01 · PAINEL RIPADO — as duas bandas em volta do nicho
# ════════════════════════════════════════════════════════════════════════
#   ⭐⭐ "vc quantificou onde esta as chapas da base onde as ripas serão
#     coladas?" — estas duas linhas são essa base, e agora elas aparecem na
#     tabela com nome, medida, espessura e m², em vez de sumirem dentro de
#     um total de chapa.
it = novo('Armário superior do nicho',
          f'{NICHO_L:.0f} × {R_SUP:.0f} × 50 · {b.VAOS_BANDA} folhas de giro')
it.caixa(NICHO_L, R_SUP, b.PROF_UTIL, b.VAOS_BANDA, 'Armário superior')
it.folhas_ripadas(NICHO_L, R_SUP, b.VAOS_BANDA, 'Armário superior')
it.ripado(NICHO_L, R_SUP, 'Ripas da banda superior')
#   ⛔ Porta de GIRO também em cima [Jonathan, 18/11/2026]. 75 de altura →
#     2 dobradiças por folha, pela tabela da Base.
it.f(b.DOBRADICA_NOME, b.VAOS_BANDA * b.dobradicas(R_SUP), b.DOBRADICA)
it.f(b.PULSADOR_NOME, b.VAOS_BANDA, b.PULSADOR)

it = novo('Armário inferior do nicho',
          f'{NICHO_L:.0f} × {R_INF:.0f} × 50 · {b.VAOS_BANDA} folhas de abrir')
it.caixa(NICHO_L, R_INF, b.PROF_UTIL, b.VAOS_BANDA, 'Armário inferior')
it.folhas_ripadas(NICHO_L, R_INF, b.VAOS_BANDA, 'Armário inferior')
it.ripado(NICHO_L, R_INF, 'Ripas da banda inferior')
#   15 a 86 cm do piso: porta de abrir, 71 de altura → 2 dobradiças cada.
it.f(b.DOBRADICA_NOME, b.VAOS_BANDA * b.dobradicas(R_INF), b.DOBRADICA)
it.f(b.PULSADOR_NOME, b.VAOS_BANDA, b.PULSADOR)

# ════════════════════════════════════════════════════════════════════════
# 02 · PORTA RIPADA DO ARMÁRIO — 50 × 277
# ════════════════════════════════════════════════════════════════════════
it = novo('Armário lateral, porta ripada inteira',
          f'{R_PORTA_L:.0f} × {ALT:.0f} × 50 · folha inteira, abertura por toque')
#   ⭐ A folha É a base das ripas. 15 mm, que é a espessura de porta da aba
#     MDF — e as 12 ripas coladas na frente enrijecem o conjunto.
it.p('BASE do ripado · folha da porta', R_PORTA_L, ALT, b.ESP_PORTA, GIA, 1,
     f22=(R_PORTA_L + ALT) * 2 / 100, obs='onde as ripas são coladas')
it.ripado(R_PORTA_L, ALT, 'Ripas da porta')
#   ⭐⭐ "e as dobradiças da porta a esquerda?" — não havia NENHUMA. Esta
#     porta é de ARMÁRIO, não de passagem: dobradiça, não pivô. E a tabela
#     da Base manda CINCO, porque 277 passa de 200 cm.
it.f(b.DOBRADICA_NOME, b.dobradicas(ALT), b.DOBRADICA)
#   ⚠ 2,77 m de altura em 15 mm: a Base tem a barra chata contra empeno.
it.f('Alma de aço, barra chata de 3 m', 1, b.ALMA_BARRA)
#   ⛔ E ELA TAMBÉM NÃO TEM PUXADOR. Eu tinha escrito "sem puxador" sem
#     dizer como ela abre. Abre por toque, como as outras oito.
it.f(b.PULSADOR_NOME, 1, b.PULSADOR)
#   ⭐⭐ A CAIXA DESTE, QUE A PRANCHA CHAMA DE "ARMÁRIO 50X274CM" E QUE EU
#     TINHA DEIXADO DE FORA por não ter interior desenhado. Com as duas
#     bandas virando armário, deixar OCO justamente o que o executivo
#     nomeia armário deixou de fazer sentido. ⚠ Vai em linha própria: é a
#     única das três que o Jonathan não pediu, e some com uma palavra.
it.caixa(R_PORTA_L, ALT, b.PROF_UTIL, 1, 'Armário lateral')
it.p('Armário lateral · prateleiras extras', R_PORTA_L - 3, b.PROF_UTIL - 2,
     18, GIA, 4, f22=(R_PORTA_L - 3) / 100, obs='2,77 m de altura · 5 no total')
it.f('Suporte de prateleira, jogo de 4', 4, b.SUPORTE_JOGO)

# ════════════════════════════════════════════════════════════════════════
# 03 · PAINEL LISO — 330 × 277, do fim da pedra para a direita
# ════════════════════════════════════════════════════════════════════════
#   ⭐ [Jonathan, 17/11/2026] "Do nicho de pedra para a direita, o painel
#     vai ser liso com as duas portas mimetizadas, mas não vai ser ripado."
it = novo('Painel liso com os vãos das duas portas',
          f'{LISO_L:.0f} × {ALT:.0f} · face melamínica, sem ripa')
_h_sup = ALT - PORTAS[0][1]              # 67
#   ⛔ 330 cm não sai de uma chapa de 275: a faixa superior é emendada.
it.p('Faixa superior sobre as portas', LISO_L / 2, _h_sup, 18, GIA, 2,
     f22=(LISO_L / 2 + _h_sup) * 2 / 100, obs='emendada · 330 > 273')
for i, (a, z) in enumerate([(RIPADO_L, 366.0), (449.0, 592.0),
                            (662.0, LARG)], 1):
    it.p(f'Faixa vertical {i} entre vãos', z - a, PORTAS[0][1], 18, GIA, 1,
         f22=((z - a) + PORTAS[0][1]) * 2 / 100)

# ════════════════════════════════════════════════════════════════════════
# 04 · AS DUAS PORTAS DE PASSAGEM MIMETIZADAS — 42 mm
# ════════════════════════════════════════════════════════════════════════
it = novo('Duas portas mimetizadas de passagem',
          '83 × 210 e 70 × 210 · tamponamento de 42 mm, 18 + 18 + 6')
for i, (L, A) in enumerate(PORTAS, 1):
    it.porta_passagem(L, A, i)
    #   o marco, que também é nosso: 15 cm para abraçar os 42 da folha
    it.p(f'Marco mimetizado da porta {i}', 2 * A + L, 15, 18, GIA, 1,
         f22=(2 * A + L) / 100)

# ════════════════════════════════════════════════════════════════════════
# 05 · ESTRUTURA DE FIXAÇÃO
# ════════════════════════════════════════════════════════════════════════
#   ⛔ REGRA 1 DA CASA: pinus está proibido. Travessa de MDF, da chapa.
it = novo('Estrutura de fixação do painel',
          'montantes a cada 60 cm e três fiadas de travessa')
it.p('Montantes verticais a cada 60 cm', 8, ALT, 18, EST, 12,
     obs='não aparece · MDF branco')
it.p('Travessas horizontais', LARG / 2, 8, 18, EST, 6,
     obs='três fiadas, emendadas')


# ════════════════════════════════════════════════════════════════════════
# O CUSTO
# ════════════════════════════════════════════════════════════════════════
def _levanta(it):
    area, pecas = {}, 0
    for p in it.pecas:
        k = (p['mat'], p['esp'])
        area[k] = area.get(k, 0.0) + p['L'] * p['A'] / 10000 * p['qtd']
        pecas += p['qtd']
    #   ⭐⭐ FITA = MATERIAL (com os 10% de desperdício que a própria Base
    #     manda somar) MAIS A APLICAÇÃO. A Base publica o par pronto para a
    #     de 22: "Fita de cor com filetagem, preço cheio da casa · R$ 5,50
    #     · já inclui a aplicação" = 3,00 + 2,50. Aqui sai 5,80, que é o
    #     mesmo par com os 10% em cima do material — e para a de 50 não há
    #     linha cheia na Base, então ela se monta igual: 7,00 + 2,50.
    mat22 = it.fita22 * b.FITA_22 * b.FITA_PERDA
    mat50 = it.fita50 * b.FITA_50 * b.FITA_PERDA
    matrp = it.fita_ripa * b.FITA_22 * b.FITA_PERDA
    apl = (it.fita22 + it.fita50) * b.FILETE_MAQ + it.fita_ripa * b.FILETE_RIPA
    return dict(area=area, pecas=pecas,
                fita_m=it.fita22 + it.fita50 + it.fita_ripa,
                c_fita_mat=mat22 + mat50 + matrp, c_filete=apl,
                c_terc=sum(q * u for _n, q, u, _un in it.terc),
                c_fer=sum(q * u for _n, q, u in it.fer))


def custo(itens, arredonda=True):
    """⭐ "⛔ NÃO EXISTE 2,7 CHAPAS, SÃO 3. A chapa é a unidade de compra:
    arredonda-se para cima POR PADRÃO × ESPESSURA, e cada padrão puxa no
    mínimo uma chapa." — aba MDF da Base, em caixa alta.
    A sobra do arredondamento é RATEADA pela área, para que a soma dos
    itens continue sendo o custo do projeto."""
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
        #   "Consumíveis · sobre chapa e fita · 6%" — sobre MATERIAL, não
        #   sobre a mão de obra de aplicar.
        cons = (ch + q['c_fita_mat']) * b.CONSUMIVEIS
        return ((ch + q['c_fita_mat'] + q['c_filete'] + corte + cons
                 + q['c_terc'] + q['c_fer']) * (1 + b.EMBALAGEM))

    diretos = [_item(q) for _it, q in L]
    #   ⛔⛔ A LOGÍSTICA DE GOVERNADOR VALADARES, no lugar do frete de BH.
    #     Ela é do PROJETO, não de um item, e por isso é rateada pelo custo
    #     direto — senão a soma dos itens deixa de ser o custo do projeto.
    c_frete = b.CUSTO_GV
    soma = sum(diretos)
    diretos = [d + c_frete * (d / soma) for d in diretos]
    T = dict(area=area, chapas=chapas, preco=preco, c_chapa=c_chapa,
             pecas=n_pecas, n_chapas=n_chapas,
             fita_m=sum(q['fita_m'] for _i, q in L),
             c_fita_mat=sum(q['c_fita_mat'] for _i, q in L),
             c_filete=sum(q['c_filete'] for _i, q in L),
             c_corte=n_chapas * b.CORTE_CHAPA + n_pecas * b.CORTE_PECA,
             c_terc=sum(q['c_terc'] for _i, q in L),
             c_fer=sum(q['c_fer'] for _i, q in L),
             c_frete=c_frete, diretos=diretos, direto=sum(diretos), L=L)
    T['c_cons'] = (T['c_chapa'] + T['c_fita_mat']) * b.CONSUMIVEIS
    T['c_emb'] = (T['direto'] - c_frete
                  - (T['c_chapa'] + T['c_fita_mat'] + T['c_filete']
                     + T['c_corte'] + T['c_cons'] + T['c_terc'] + T['c_fer']))
    return T


def brl(v):
    return f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')


T = custo(M)
DIRETO = T['direto']

#   ⭐⭐ A MC É LIDA DO PREÇO: MC = BASE − custo ÷ preço.
MC = b.BASE - DIRETO / b.PRECO_FECHADO
MC_SEM_RT = b.BASE_SEM_RT - DIRETO / b.PRECO_FECHADO
MARGEM = b.PRECO_FECHADO * b.BASE - DIRETO
FIXO_DIA = 4000.0
assert abs(DIRETO / (b.BASE - MC) - b.PRECO_FECHADO) < 0.01

#   ⭐ O rateio do preço fechado entre os itens, pelo custo direto. O último
#     absorve o centavo, para que a tabela some o preço exato.
_br = [d / DIRETO * b.PRECO_FECHADO for d in T['diretos']]
RATEIO = [round(v, 2) for v in _br[:-1]]
RATEIO.append(round(b.PRECO_FECHADO - sum(RATEIO), 2))
assert abs(sum(RATEIO) - b.PRECO_FECHADO) < 1e-9


# ════════════════════════════════════════════════════════════════════════
# A TABELA
# ════════════════════════════════════════════════════════════════════════
BANDAS = [(R_PORTA_L, ALT, 'Porta ripada do armário'),
          (NICHO_L, R_SUP, 'Banda superior do nicho'),
          (NICHO_L, R_INF, 'Banda inferior do nicho')]


def _ripas():
    for larg, alt, rot in BANDAS:
        n = int(larg // b.PASSO)
        yield (rot, larg, alt, n,
               n * alt / 100 * 2 + n * b.RIPA_L / 100 * 2,
               larg * alt / 10000)


if __name__ == '__main__':
    S = '─'
    print(f'\n  PAINEL DA SALA · VISTA 2 — LEVANTAMENTO REFEITO SOBRE A BASE')
    print(f'  {b.EXECUTIVO}')
    print(f'  filetagem da ripa: '
          f'{"COLADEIRA · R$ 2,50" if b.RIPA_NA_MAQUINA else "MANUAL · R$ 5,00"}'
          f'  ·  chapa de cor: R$ {brl(b.PRECO["MDF Gianduia 18"])}')

    print(f'\n  ① A RIPA E A SUA BASE  ' + S * 52)
    print(f'  {"BANDA":<26}{"FACE":>12}{"RIPAS":>7}{"FITA+FILETE m":>15}'
          f'{"m² FACE":>9}')
    tn = tf = tm = 0.0
    for rot, larg, alt, n, mf, m2 in _ripas():
        print(f'  {rot:<26}{f"{larg:.0f} × {alt:.0f}":>12}{n:>7}{mf:>15.1f}'
              f'{m2:>9.2f}')
        tn += n; tf += mf; tm += m2
    print(f'  {"TOTAL":<26}{"":>12}{int(tn):>7}{tf:>15.1f}{tm:>9.2f}')
    print(f'  {"":<26}passo {b.PASSO:g} cm · ripa {b.RIPA_L:g} · vão '
          f'{b.RIPA_VAO:g} · 25 ripas por metro')
    print(f'\n  A BASE onde as ripas são coladas, peça a peça:')
    for it, _q in T['L']:
        for p in it.pecas:
            if p['nome'].startswith('BASE'):
                med = '%.0f × %.0f × %d' % (p['L'], p['A'], p['esp'])
                print(f'    {p["nome"]:<40}{med:>18}'
                      f'{p["L"]*p["A"]/10000:>8.2f} m²')
    print(f'    {"soma da base ripada":<40}{"":>18}{tm:>8.2f} m²')

    print(f'\n  ② O QUANTITATIVO DE CHAPAS  ' + S * 47)
    print(f'  {"PADRÃO E ESPESSURA":<28}{"ÁREA":>9}{"FRAÇÃO":>9}'
          f'{"CHAPAS":>8}{"R$/CHAPA":>12}{"CUSTO":>14}')
    rend = b.CHAPA_M2 * b.APROV
    for k, n in sorted(T['chapas'].items()):
        a = T['area'][k]
        rot = '%s %d mm' % (k[0], k[1])
        print(f'  {rot:<28}{a:>7.2f} m²{a/rend:>9.2f}'
              f'{n:>8}{brl(T["preco"][k]):>12}{brl(n*T["preco"][k]):>14}')
    print(f'  {"TOTAL":<28}{sum(T["area"].values()):>7.2f} m²{"":>9}'
          f'{T["n_chapas"]:>8}{"":>12}{brl(T["c_chapa"]):>14}')
    print('  ⛔ "NÃO EXISTE 2,7 CHAPAS, SÃO 3" — aba MDF. Arredonda-se por\n'
          '     PADRÃO × ESPESSURA, e cada padrão puxa no mínimo uma chapa.')

    print(f'\n  ③ FITA DE BORDA E FILETAGEM  ' + S * 46)
    print(f'  {"ONDE":<34}{"METROS":>9}{"R$/m":>9}{"MATERIAL":>12}'
          f'{"APLICAÇÃO":>12}')
    f22 = sum(i.fita22 for i in M); f50 = sum(i.fita50 for i in M)
    frp = sum(i.fita_ripa for i in M)
    for rot, m, pm, pa in [
            ('Fita 22 mm · peças e portas', f22, b.FITA_22, b.FILETE_MAQ),
            ('Fita 50 mm · borda de 42 das portas', f50, b.FITA_50, b.FILETE_MAQ),
            ('Fita 22 mm · as duas faces da ripa', frp, b.FITA_22, b.FILETE_RIPA)]:
        print(f'  {rot:<34}{m:>9.1f}'
              f'{brl(pm*b.FITA_PERDA+pa):>9}{brl(m*pm*b.FITA_PERDA):>12}'
              f'{brl(m*pa):>12}')
    print(f'  {"TOTAL":<34}{T["fita_m"]:>9.1f}{"":>9}'
          f'{brl(T["c_fita_mat"]):>12}{brl(T["c_filete"]):>12}')
    print(f'  {"fita mais filetagem":<34}{"":>9}{"":>9}'
          f'{brl(T["c_fita_mat"]+T["c_filete"]):>24}')
    print('  ⛔ A ripa de 2 cm NÃO entra na coladeira automática: a Base\n'
          '     nomeia o caso em "Filetagem manual · o que não entra na\n'
          '     máquina · R$ 5,00". Rode RIPA_NA_MAQUINA=1 para comparar.')

    print(f'\n  ④ FERRAGEM  ' + S * 62)
    _ag = {}
    for it, _q in T['L']:
        for n, qt, u in it.fer:
            a = _ag.setdefault(n, [0, u]); a[0] += qt
    for n, (qt, u) in _ag.items():
        print(f'  {n:<44}{qt:>5} ×{brl(u):>10}{brl(qt*u):>15}')
    print(f'  {"TOTAL":<44}{"":>5}{"":>11}{brl(T["c_fer"]):>15}')
    print('  ⭐ A escada de dobradiça da Base, para a porta da esquerda:')
    for nome, v in b.ESCADA_DOBRADICA:
        d = b.dobradicas(ALT)
        print(f'     {nome:<28}{d} × {brl(v):>8} = {brl(d*v):>9}'
              f'{"   ← orçado" if v == b.DOBRADICA else ""}')

    print(f'\n  ⑤ O CUSTO POR ITEM  ' + S * 55)
    for (it, q), d in zip(T['L'], T['diretos']):
        print(f'  {it.nome:<54}{brl(d):>20}')
        print(f'    {it.obs}')
    print(f'  {"CUSTO DIRETO":<54}{brl(DIRETO):>20}')

    print(f'\n  ⑥ O CUSTO POR NATUREZA  ' + S * 51)
    for rot, v in [(f'Chapa · {T["n_chapas"]} chapas', T['c_chapa']),
                   (f'Fita de borda · {T["fita_m"]:.0f} m, material', T['c_fita_mat']),
                   ('Filetagem · aplicação', T['c_filete']),
                   (f'Corte · {T["n_chapas"]} chapas, {T["pecas"]} peças', T['c_corte']),
                   ('Consumíveis · 6% sobre chapa e fita', T['c_cons']),
                   ('Terceirizado · painel ripado', T['c_terc']),
                   ('Ferragem', T['c_fer']),
                   (f'Logística · {b.OBRA}', T['c_frete']),
                   ('Embalagem · 2%', T['c_emb'])]:
        print(f'  {rot:<54}{brl(v):>20}')
    print(f'  {"CUSTO DIRETO":<54}{brl(DIRETO):>20}')

    print(f'\n  ⑦ A LOGÍSTICA DE {b.OBRA.upper()}  ' + S * 36)
    print(f'  {"":<34}{"VEÍCULO":>11}{"EQUIPE":>11}{"CAMA":>9}'
          f'{"COMIDA":>9}{"TOTAL":>11}')
    for v in b.LOGISTICA:
        c = b.viagem(v)
        print(f'  {v["rotulo"]:<34}{brl(c["veiculo"]):>11}'
              f'{brl(c["equipe"]):>11}{brl(c["hospedagem"]):>9}'
              f'{brl(c["alimentacao"]):>9}{brl(sum(c.values())):>11}')
        print(f'    {v["pessoas"]} pessoa(s) · {v["dias"]:g} dias · '
              f'{v["noites"]} noite(s) · {b.KM_IDA*2:.0f} km de ida e volta')
    print(f'  {"TOTAL":<34}{"":>40}{brl(b.CUSTO_GV):>11}')
    print('  ⚠ Só a hora de marceneiro vem da Base (R$ 36 com encargos). O\n'
          '     resto é estimativa minha, linha a linha, porque as QUATRO\n'
          '     linhas de frete da Base estão vazias — "A COTAR".')

    print(f'\n  ⑧ O FECHAMENTO  ' + S * 59)
    print(f'  {"PREÇO FECHADO":<40}{brl(b.PRECO_FECHADO):>18}')
    print(f'  {"custo direto":<40}{brl(DIRETO):>18}')
    print(f'  {"  dos quais, logística de GV":<40}{brl(b.CUSTO_GV):>18}')
    print(f'  {"MC LIDA · com RT de 10%":<40}{MC*100:>17.2f}%')
    print(f'  {"MC LIDA · se não houver RT":<40}{MC_SEM_RT*100:>17.2f}%')
    print(f'  {"margem de contribuição":<40}{brl(MARGEM):>18}')
    print(f'  {"empate em dias de fábrica":<40}{MARGEM/FIXO_DIA:>16.1f} d')
    print(f'\n  ⚠ SE A LOGÍSTICA DE GV NÃO EXISTISSE (frete de BH, R$ 400):')
    _sem = DIRETO - b.CUSTO_GV + 400.0
    print(f'  {"  custo direto":<40}{brl(_sem):>18}')
    print(f'  {"  MC que eu estaria reportando":<40}'
          f'{(b.BASE - _sem/b.PRECO_FECHADO)*100:>17.2f}%')
    print(f'  {"  o que GV custa, em pontos de MC":<40}'
          f'{((b.BASE - _sem/b.PRECO_FECHADO) - MC)*100:>17.2f} pt')

    print(f'\n  ⑨ O RATEIO DO PREÇO  ' + S * 54)
    for (it, _q), v in zip(T['L'], RATEIO):
        print(f'  {it.nome:<54}{brl(v):>20}')
    print(f'  {"PREÇO FECHADO":<54}{brl(b.PRECO_FECHADO):>20}')
