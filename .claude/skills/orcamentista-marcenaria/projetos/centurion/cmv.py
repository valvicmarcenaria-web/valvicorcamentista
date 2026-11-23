# -*- coding: utf-8 -*-
"""CENTURION — O CMV, OS ENCARGOS E O PREÇO, ITEM POR ITEM.

⭐ O que é do ITEM e o que é do AMBIENTE:
     do ITEM, direto   peça (fração de chapa), fita, filetagem, laca, LED,
                       ferragem, corte por peça, consumíveis, embalagem
     do AMBIENTE       o arredondamento de chapa para número cheio e o
                       corte por chapa — nascem da CHAPA COMPRADA, e a
                       chapa se compra para o ambiente, não para o item.
                       ⭐ Rateio pela ÁREA que cada item ocupa NAQUELE
                       material: é o único rateio justo, porque é a área
                       que puxa a chapa.
"""
import importlib.util, pathlib

A = pathlib.Path(__file__).resolve().parent


def _m(n, a):
    sp = importlib.util.spec_from_file_location(n, A / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


b = _m('b', 'base.py')
lv = _m('lv', 'levantamento.py')
T = lv.T

#   ⭐ A CASCATA, lida da aba Preço e Comissões (quadro ②)
NOTA = 0.09                 # sobre o bruto
BRUTO_OUTROS = 0.03         # margem de erro 2% + serra 0,5% + manutenção 0,5%
COMISSOES = 0.075           # 2,5 + 2,5 + 1 + 1 + 0,5, sobre o LÍQUIDO
ENCARGOS = NOTA + BRUTO_OUTROS + COMISSOES * (1 - NOTA)
BASE = 1 - ENCARGOS         # 0,81175
MC = 0.50                   # ⭐ o alvo que o Jonathan pediu AGORA

#   ⭐⭐ A MC POR ITEM [Jonathan, 23/11/2026]: "coloque as porcentagens de
#     MC de cada item tbm". ⭐ Ela é ESCOLHIDA, não descoberta — e o quadro
#     ④ da aba Preço e Comissões diz em cima: "a MC é direcionada ao
#     projeto TODO ou a um item específico, conforme a complexidade".
#   ⛔ MC MAIOR QUE A BASE NÃO EXISTE: a 81,175% o preço vai a infinito,
#     porque não sobraria nada para o custo. O assert pega isso antes de a
#     conta sair errada.
#   ⚠ Hoje todas estão no alvo. Mudar uma linha aqui muda SÓ o preço
#     daquele item, e o total se refaz.
MC_ITEM = {}                # nome do item -> MC própria · vazio = todas no alvo


def mc_de(nome):
    m = MC_ITEM.get(nome, MC)
    assert 0 <= m < BASE, 'MC de %.1f%% não cabe na base de %.3f%%: %s' % (
        m * 100, BASE * 100, nome)
    return m


def preco(cmv, mc=MC):
    return cmv / (BASE - mc)


#   ── o que o ambiente compra de chapa a mais do que os itens ocupam ──
ARRED, CORTE_CH = {}, {}
for k, n in T['chapas'].items():
    p = b.PRECO['%s %d' % k]
    ARRED[k] = n * p - T['area'][k] / b.rend(k) * p
    CORTE_CH[k] = n * b.CORTE_CHAPA


def apura():
    out = []
    for i, it in enumerate(lv.ITENS, 1):
        ar = it.areas()
        chapa = sum(v / b.rend(k) * b.PRECO['%s %d' % k] for k, v in ar.items())
        fita = it.c_fita() * b.FITA_PERDA * b.FITA_22
        filete = it.c_fita() * b.FITA_PERDA * b.FILETE_MAQ
        fita_lin = sum(x['qtd'] * x['unit'] for x in it.lin
                       if 'Fita de borda' in x['nome'])
        #   ⭐ a parcela do item em cada material, pela ÁREA
        peso = {k: v / T['area'][k] for k, v in ar.items()}
        arred = sum(ARRED[k] * w for k, w in peso.items())
        corte = sum(CORTE_CH[k] * w for k, w in peso.items())
        corte += it.n_pecas() * b.CORTE_PECA
        cons = (chapa + fita + fita_lin) * b.CONSUMIVEIS
        sub = (chapa + fita + filete + it.c_lin() + it.c_serv()
               + arred + corte + cons)
        emb = sub * b.EMBALAGEM
        out.append(dict(n=i, nome=it.nome, cmv=sub + emb,
                        chapa=chapa + arred, mo=filete,
                        terc=it.c_serv(), outros=corte + cons + emb))
    #   ⛔ A SOMA DOS ITENS TEM DE DAR O CUSTO DIRETO. O resto é
    #     arredondamento de ponto flutuante, e a ÚLTIMA LINHA O ABSORVE —
    #     a mesma regra da coluna de dinheiro na planilha.
    d = T['direto'] - sum(x['cmv'] for x in out)
    out[-1]['cmv'] += d
    return out


ITENS = apura()
for x in ITENS:
    x['mc'] = mc_de(x['nome'])
    x['preco'] = preco(x['cmv'], x['mc'])
    x['encargos'] = x['preco'] * ENCARGOS
    x['margem'] = x['preco'] * x['mc']


def brl(v):
    t = ('%0.2f' % v).replace('.', ',')
    i, _, dd = t.partition(',')
    o = ''
    while len(i) > 3:
        o, i = '.' + i[-3:] + o, i[:-3]
    return i + o + ',' + dd


if __name__ == '__main__':
    print('\n  CASCATA  ' + '─' * 58)
    print('  nota fiscal %.0f%% + margem de erro, serra e manutenção %.0f%% '
          '+ comissões %.1f%% do líquido' % (NOTA * 100, BRUTO_OUTROS * 100,
                                             COMISSOES * 100))
    print('  ENCARGOS %.3f%%   ·   BASE %.3f%%   ·   MC %.0f%%'
          % (ENCARGOS * 100, BASE * 100, MC * 100))
    print('  PREÇO = CMV ÷ (%.5f − %.2f) = CMV ÷ %.5f = CMV × %.4f'
          % (BASE, MC, BASE - MC, 1 / (BASE - MC)))

    print('\n  POR ITEM  ' + '─' * 72)
    print('  %-2s %-34s %12s %6s %12s %12s %12s'
          % ('', 'ITEM', 'CMV', 'MC', 'ENCARGOS', 'MARGEM', 'PREÇO'))
    for x in ITENS:
        print('  %02d %-34s %12s %5.1f%% %12s %12s %12s'
              % (x['n'], x['nome'][:34], brl(x['cmv']), x['mc'] * 100,
                 brl(x['encargos']), brl(x['margem']), brl(x['preco'])))
    s = lambda c: sum(x[c] for x in ITENS)
    #   ⛔ A MC DO TOTAL NÃO É A MÉDIA DAS MC, É A PONDERADA PELO PREÇO —
    #     margem total ÷ preço total. Média simples de percentual mente
    #     sempre que os itens têm tamanhos diferentes, e aqui o maior é 9×
    #     o menor.
    print('  %-37s %12s %5.1f%% %12s %12s %12s'
          % ('TOTAL', brl(s('cmv')), s('margem') / s('preco') * 100,
             brl(s('encargos')), brl(s('margem')), brl(s('preco'))))
    print('  %-37s %12s %6s %12s %12s %12s'
          % ('% do preço', '%.1f%%' % (s('cmv') / s('preco') * 100), '',
             '%.1f%%' % (s('encargos') / s('preco') * 100),
             '%.1f%%' % (s('margem') / s('preco') * 100), '100,0%'))
    print('\n  conferência · CMV somado = custo direto?  %s'
          % brl(s('cmv') - T['direto']))
    print('  conferência · preço − CMV − encargos − margem = %s'
          % brl(s('preco') - s('cmv') - s('encargos') - s('margem')))
    #   ⛔ `%%` SÓ VIRA `%` QUANDO A LINHA TEM O OPERADOR DE FORMATAÇÃO.
    #     Numa string sem `%` depois dela, o `%%` sai literal — e eu já
    #     havia corrigido exatamente isto no levantamento.py nesta sessão.
    print('\n  ⚠ hoje a planilha está com MC de %.0f%% (alvo de %.0f%% mais '
          '%s, %.0f pontos)' % (b.MC * 100, b.MC_ALVO * 100, b.DIFICULDADE,
                                b.PONTOS[b.DIFICULDADE] * 100))
    print('    preço a 55%%  %s   ·   a 50%%  %s   ·   diferença  %s'
          % (brl(b.preco(T['direto'])), brl(s('preco')),
             brl(b.preco(T['direto']) - s('preco'))))
