# -*- coding: utf-8 -*-
"""BAR CARIOCANDO · Savassi, BH — DET. COZINHA / BANCADA, prancha #104 R02.

⭐ UMA LINHA SÓ: Hettich, MC 38%. [Jonathan, 05/11/2026]

⛔⛔ O QUE ESTA PRANCHA MOSTRA **NÃO É TUDO NOSSO**, e separar é o primeiro
  trabalho. O desenho é de um balcão de bar inteiro: alvenaria, granito,
  revestimento cerâmico, metalon e marcenaria, tudo na mesma folha.
  ⭐ A regra da casa decide: PEDRA NUNCA; obra civil nunca; serralheria só
    quando faz parte do móvel. O que sobra para nós são três peças.

⭐⭐ E A MEDIDA FOI MEDIDA, não estimada. As cotas desta prancha são TEXTO
  de verdade (ao contrário do executivo do Attos, todo vetorizado), então
  elas foram lidas direto do arquivo. O que não tinha cota — a profundidade
  do armário — saiu do vetor, e a escala se provou sozinha: a prancha é 1:25
  e 1 pt = 0,88194 cm; medindo o corte AA os vãos de prateleira deram 29,6 /
  29,7 / 29,8 cm contra a cota de 29,5, e o sóculo deu 10,0 contra 10.
"""
import math, importlib.util, sys, pathlib, contextlib, io

AQUI = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('b', AQUI / 'base.py')
b = importlib.util.module_from_spec(_s); sys.modules['b'] = b
with contextlib.redirect_stdout(io.StringIO()):
    _s.loader.exec_module(b)

COR, BRANCO = 'MDF cor', 'MDF Branco TX'

# ── a ripa ──────────────────────────────────────────────────────────────
#   ⚠⚠ E AQUI A PRANCHA SE CONTRADIZ, na mesma folha: as notas da VISTA A e
#     das plantas dizem "RIPAS DE 4x3CM E ESPAÇAMENTO DE 2CM"; as da VISTA C
#     e do detalhe da porta dizem "RIPAS DE 4x2CM E ESPAÇAMENTO DE 2CM".
#   ⭐ Orço cada face com a ripa que a SUA vista manda, e registro a dúvida.
#     A diferença não é de acabamento: 3 cm de espessura pede DUAS chapas de
#     15 coladas, 2 cm pede uma de 18. É o dobro de material na face errada.
#   ⭐ E A DÚVIDA TEM PREÇO, que é o jeito de levá-la ao arquiteto. Rodar
#     com `RIPA_UNICA=1` unifica as três faces em ripa de 4 × 3 (duas chapas
#     de 15) e põe o substrato da porta também em 15 — o quanto a resposta
#     dele vale sai da diferença entre as duas execuções.
import os as _os
RIPA_UNICA = _os.environ.get('RIPA_UNICA') == '1'
RIPA_L = 4.0              # cm de largura da ripa
RIPA_VAO = 2.0            # cm de vão
PASSO = RIPA_L + RIPA_VAO # 6 cm
#   ⚠ E O DESENHO DESENHA OUTRA COISA: a hachura do ripado na elevação tem
#     passo de ~3,8 cm, não 6. Hachura é grafismo, nota é especificação —
#     sigo a NOTA, e aviso.


class Item:
    def __init__(self, nome, obs=''):
        self.nome, self.obs = nome, obs
        self.pecas, self.terc, self.fer = [], [], []

    def p(self, nome, L, A, esp, mat=COR, qtd=1, fita=0.0, obs=''):
        self.pecas.append(dict(nome=nome, L=L, A=A, esp=esp, mat=mat,
                               qtd=qtd, fita=fita, obs=obs))
        return self

    def t(self, nome, q, unit, un='m²'):
        self.terc.append((nome, q, unit, un)); return self

    def f(self, nome, q, unit):
        self.fer.append((nome, q, unit)); return self

    def ripado(self, nome, larg, alt, esp_cm, mat=COR):
        """⭐ A ripa não é peça de corte: é ÁREA EQUIVALENTE de chapa.
        Um painel de 182 × 70 com ripa de 4 e vão de 2 leva 30 ripas; o que
        se compra é a faixa de 30 × 4 cm de largura, com a perda de serra."""
        n = int(larg // PASSO)
        if RIPA_UNICA:
            esp_cm = 3.0
        esp_chapa, camadas = (15, 2) if esp_cm >= 2.5 else (18, 1)
        self.p(f'{n} ripas de {RIPA_L:g} × {alt:g} · {esp_cm:g} cm de espessura',
               RIPA_L * n * b.RIPA_PERDA, alt, esp_chapa, mat, qtd=camadas,
               obs=f'área equivalente · {camadas} camada(s) de {esp_chapa} mm')
        self.t('Painel ripado, mão de obra', larg * alt / 10000, b.RIPADO_M2)
        self.t('Filetagem de ripa', n * alt / 100 * 2, b.FILETE_RIPA, 'm')
        return n


M = []

# ═══ 1 · BALCÃO DA COZINHA ══════════════════════════════════════════════
#   VISTA A (fechada e aberta) + planta +0,85 + corte AA.
#   308,5 de frente (94 + 214,5) · 36 de profundidade · duas alturas, 88 e
#   108, porque as bancadas de granito sobre ele têm 90 e 110.
PROF = 36.0
it = Item('Balcão da cozinha · armário com frentes ripadas',
          '308,5 × 36 · módulo de 94 com 88 de altura e módulo de 214,5 com 108')
#   carcaça, em MDF branco — a própria prancha manda: "MARCENARIA INTERNA EM
#   MDF BRANCO"
it.p('laterais e divisórias · módulo A', PROF, 88, 15, BRANCO, 5, fita=.88)
it.p('tampo e base · módulo A', 94, PROF, 15, BRANCO, 2, fita=.94)
it.p('fundo · módulo A', 94, 88, 6, BRANCO, 1)
it.p('prateleiras · módulo A', 21.5, 35, 15, BRANCO, 12, fita=.215)
it.p('laterais e divisórias · módulo B', PROF, 108, 15, BRANCO, 4, fita=1.08)
it.p('tampo e base · módulo B', 214.5, PROF, 15, BRANCO, 2, fita=2.145)
it.p('fundo · módulo B', 214.5, 108, 6, BRANCO, 1)
it.p('prateleiras · módulo B', 69.5, 35, 15, BRANCO, 9, fita=.695)
#   as dez portas ripadas — substrato de cor e ripa de 4 × 3
it.p('substrato de porta · módulo A', 30.3, 78, 15, COR, 3,
     fita=(30.3 + 78) * 2 / 100)
it.p('substrato de porta · módulo B', 31.1, 98, 15, COR, 7,
     fita=(31.1 + 98) * 2 / 100)
it.ripado('frente ripada · módulo A', 91, 78, 3.0)
it.ripado('frente ripada · módulo B', 218, 98, 3.0)
it.f('Dobradiça Hettich Sensys', 3 * b.dobradicas(78) + 7 * b.dobradicas(98),
     b.DOBRADICA)
it.f('Suporte de prateleira, jogo de 4', 21, b.SUPORTE_JOGO)
M.append(it)

# ═══ 2 · FECHAMENTO FRONTAL DO SALÃO ════════════════════════════════════
#   VISTA C · 182 × 70 · ripa de 4 × 2, pela nota da própria vista.
it = Item('Fechamento frontal ripado · face do salão',
          '182 × 70 · ripa de 4 × 2 com vão de 2, pela nota da VISTA C')
it.p('substrato do fechamento', 182, 70, 15, COR, 1, fita=(182 + 70) * 2 / 100)
it.ripado('fechamento do salão', 182, 70, 2.0)
M.append(it)

# ═══ 3 · REVESTIMENTO RIPADO DA PORTA DE ACESSO ═════════════════════════
#   DET. PORTA ACESSO COZINHA · 70 × 115 · "APENAS PARA O LADO DO SALÃO".
#   ⛔ A FOLHA É DE METALON E NÃO É NOSSA: a prancha diz "PORTA ESTRUTURADA
#     EM METALON 3x3CM REVESTIDA EM MDF". Nós revestimos uma face.
it = Item('Revestimento ripado da porta de acesso',
          '70 × 115 · uma face · a estrutura de metalon é da serralheria')
it.p('substrato do revestimento', 70, 115, 15 if RIPA_UNICA else 6, COR, 1,
     fita=(70 + 115) * 2 / 100)
it.ripado('revestimento da porta', 70, 115, 3.0)
M.append(it)


# ════════════════════════════════════════════════════════════════════════
def _levanta(it):
    """área por (material, espessura), fita, peças, terceirizado e ferragem."""
    area, fita_cor, fita_br, pecas = {}, 0.0, 0.0, 0
    c_terc = c_fer = 0.0
    for p in it.pecas:
        k = (p['mat'], p['esp'])
        area[k] = area.get(k, 0.0) + p['L'] * p['A'] / 10000 * p['qtd']
        pecas += p['qtd']
        if p['mat'] == COR:
            fita_cor += p['fita'] * p['qtd']
        else:
            fita_br += p['fita'] * p['qtd']
    for nome, q, unit, un in it.terc:
        c_terc += q * unit
    for nome, q, unit in it.fer:
        c_fer += q * unit
    return dict(area=area, fita_cor=fita_cor, fita_br=fita_br, pecas=pecas,
                c_terc=c_terc, c_fer=c_fer)


def custo(itens):
    """⭐⭐ O ARREDONDAMENTO DE CHAPA É DO PROJETO, NÃO DO ITEM — e foi a
    trava do fim deste arquivo que me obrigou a escrever isto.

    ⛔ Na primeira versão cada item arredondava as suas chapas para cima por
      conta própria. Três itens, cinco materiais: dava NOVE chapas de sobra
      imaginárias e a soma dos três preços (R$ 17.252) estourava o preço do
      projeto (R$ 15.980) em R$ 1.273. Dois números para a mesma coisa, e
      nenhum dos dois reclamava.
    ⭐ Quem compra chapa é o PROJETO. Então a conta de chapa do item é
      fracionária — a área dele dividida pelo rendimento — e o que sobra do
      arredondamento é RATEADO pela área, que é o que o causa. Assim a soma
      dos itens é, por construção, o preço do projeto."""
    L = [(it, _levanta(it)) for it in itens]
    area = {}
    for _it, q in L:
        for k, a in q['area'].items():
            area[k] = area.get(k, 0.0) + a
    chapas = {k: math.ceil(a / (b.CHAPA_M2 * b.APROV)) for k, a in area.items()}
    preco = {k: b.PRECO[f'{k[0]} {k[1]}'] for k in area}
    c_chapa = sum(n * preco[k] for k, n in chapas.items())
    frac = {k: area[k] / (b.CHAPA_M2 * b.APROV) * preco[k] for k in area}
    sobra = {k: chapas[k] * preco[k] - frac[k] for k in area}
    n_chapas = sum(chapas.values())

    def _item(q):
        ch = 0.0
        for k, a in q['area'].items():
            parte = a / area[k]
            ch += a / (b.CHAPA_M2 * b.APROV) * preco[k] + sobra[k] * parte
        corte = (n_chapas * b.CORTE_CHAPA * (q['pecas'] / sum(x['pecas'] for _i, x in L))
                 + q['pecas'] * b.CORTE_PECA)
        fita = (q['fita_cor'] * b.FITA_COR + q['fita_br'] * b.FITA_BRANCA) * b.FITA_PERDA
        cons = (ch + fita) * b.CONSUMIVEIS
        return (ch + fita + corte + cons + q['c_terc'] + q['c_fer']) * (1 + b.EMBALAGEM)

    diretos = [_item(q) for _it, q in L]
    return dict(area=area, chapas=chapas, preco=preco, c_chapa=c_chapa,
                pecas=sum(q['pecas'] for _i, q in L),
                fita_cor=sum(q['fita_cor'] for _i, q in L),
                fita_br=sum(q['fita_br'] for _i, q in L),
                c_fita=sum((q['fita_cor'] * b.FITA_COR + q['fita_br'] * b.FITA_BRANCA)
                           for _i, q in L) * b.FITA_PERDA,
                c_corte=n_chapas * b.CORTE_CHAPA
                        + sum(q['pecas'] for _i, q in L) * b.CORTE_PECA,
                c_cons=(c_chapa + sum((q['fita_cor'] * b.FITA_COR
                                       + q['fita_br'] * b.FITA_BRANCA)
                                      for _i, q in L) * b.FITA_PERDA) * b.CONSUMIVEIS,
                c_terc=sum(q['c_terc'] for _i, q in L),
                c_fer=sum(q['c_fer'] for _i, q in L),
                diretos=diretos, direto=sum(diretos))


def brl(v):
    return 'R$ ' + f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')


if __name__ == '__main__':
    L = 96
    print('═' * L)
    print('BAR CARIOCANDO · COZINHA / BANCADA — prancha #104 R02 · LINHA HETTICH')
    print('═' * L)
    print(f'  BASE {b.BASE:.2%} (sem RT e sem vendedor) · MC {b.MC:.0%}'
          + ('  ·  ⭐ RIPA UNIFICADA em 4 × 3' if RIPA_UNICA else '') + '\n')
    T = custo(M)
    tot_pv = 0.0
    for it, direto in zip(M, T['diretos']):
        pv = direto / (b.BASE - b.MC)
        tot_pv += pv
        print(f'■ {it.nome}')
        print(f'  {it.obs}')
        for p in it.pecas:
            print('    %-52s %6.1f × %5.1f × %2d  ×%2d' %
                  (p['nome'][:52], p['L'], p['A'], p['esp'], p['qtd']))
        for nome, q, unit, un in it.terc:
            print('    %-52s %8.2f %-2s × %s' % (nome, q, un, brl(unit)))
        for nome, q, unit in it.fer:
            print('    %-52s %8.0f un × %s' % (nome, q, brl(unit)))
        print('    %-52s %s' % ('custo direto', brl(direto)))
        print('    %-52s %s\n' % ('PREÇO', brl(pv)))
    print('─' * L)
    print('  CHAPAS')
    for k in sorted(T['chapas']):
        print('    %-22s %5.2f m²  →  %2d chapa(s) × %s = %s'
              % (f'{k[0]} {k[1]} mm', T['area'][k], T['chapas'][k],
                 brl(T['preco'][k]), brl(T['chapas'][k] * T['preco'][k])))
    print('    %-22s %5.1f m de cor · %5.1f m de branca' %
          ('FITA', T['fita_cor'], T['fita_br']))
    print()
    for rot, v in (('chapa', T['c_chapa']), ('fita', T['c_fita']),
                   ('corte', T['c_corte']), ('consumíveis', T['c_cons']),
                   ('terceirizado (ripado + filetagem)', T['c_terc']),
                   ('ferragem', T['c_fer'])):
        print('    %-40s %14s' % (rot, brl(v)))
    print('    %-40s %14s' % ('CUSTO DIRETO (com embalagem)', brl(T['direto'])))
    print('─' * L)
    pv = T['direto'] / (b.BASE - b.MC)
    assert abs(pv - tot_pv) < 0.01, '⛔ a soma dos itens não bate com o motor'
    print('  %-40s %14s' % ('PREÇO · LINHA HETTICH, MC 38%', brl(pv)))
    print('  %-40s %14s' % ('  MC realizada', f'{b.BASE - T["direto"]/pv:.1%}'))
    print('═' * L)
