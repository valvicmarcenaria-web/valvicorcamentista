# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — AS TRÊS LINHAS, item a item.

⭐⭐ [Jonathan, 04/11/2026] "35 telescopica (basica) 38 hettich e 43 blum —
  lembrando que so tem alteração de valores os itens que levam as
  respectivas ferragens. os demais pode manter a mc de 38% fixo."

⛔⛔ E A SEGUNDA FRASE É MAIS IMPORTANTE QUE A PRIMEIRA. Ela diz que a MC da
  linha NÃO é a MC do projeto: ela vale só para os itens que carregam a
  ferragem que muda. Um painel ripado, que não leva uma corrediça sequer,
  tem de custar ao cliente EXATAMENTE O MESMO nas três linhas.
⭐ Isso é a regra que o próprio Jonathan cravou em 09/09/2026, no job da
  Luiza: "A cabeceira estofada deve custar o mesmo valor para o cliente em
  ambos os contextos". Aqui ela vira aritmética, e o `_trava()` a prova.

⛔ O QUE MUDA ENTRE AS LINHAS, e é só isto:
     corrediça         R$  80 (Hardt) · R$ 150 (Hettich) · R$ 300 (Blum)
     sistema de correr R$ 600         · R$ 600           · R$ 900
  ⚠ A BÁSICA FICA COM O MESMO SISTEMA DE CORRER DA HETTICH, porque a Base
    não tem um mais barato: SS-150 e Dominus custam os dois R$ 600. Então
    na básica só a CORREDIÇA desce. Isso está medido, não suposto.
  ⛔ A dobradiça NÃO muda: R$ 50 nas três (a Base traz "Dobradiça" e
    "Dobradiça Hettich" pelo mesmo preço).

uso:  python3 -I linhas.py
"""
import importlib.util, sys, pathlib, contextlib, io

P = pathlib.Path(__file__).resolve().parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, P / arq)
    m = importlib.util.module_from_spec(s); sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m


b = _mod('b', 'base.py')
lv = _mod('lv', 'levantamento.py')

CORR_HETTICH, CORRE_HETTICH = b.CORREDICA_PAR, b.SISTEMA_CORRER
LINHAS = {
    'Básica':  dict(corr=80.0,  corre=600.0, mc=0.35, marca='Hardt'),
    'Hettich': dict(corr=150.0, corre=600.0, mc=0.38, marca='Quadro V6'),
    'Blum':    dict(corr=300.0, corre=900.0, mc=0.43, marca='Movento'),
}
MC_FIXA = 0.38   # ⭐ a MC dos itens que NÃO mudam de linha


def item(m):
    """O custo de UM móvel, repartido pelo que muda e pelo que não muda.

    ⛔⛔ TUDO É CALCULADO NO ITEM, nunca rateado de um total do projeto. Se
      o consumível ou a embalagem viessem de um bolo rateado, encarecer a
      ferragem de um móvel baratearia o vizinho — é o vazamento que o
      `estrutura-orcamento.md` documenta, e ele faria um item SEM ferragem
      mudar de preço entre as linhas sem ninguém ver.
    """
    d = dict(amb=m.amb, nome=m.nome, nota=m.nota)
    #   chapa: o rateio em fração, e o arredondamento fica no ambiente
    d['mat'] = sum(a / (b.CHAPA_M2 * b.APROV) * b.PRECO[f'{k[0]} {k[1]}']
                   for k, a in m.areas().items())
    d['fita'] = m.fita * b.FITA_COR * b.FITA_PERDA
    fita_maq = m.fita - m.fita_ripa
    d['filete'] = fita_maq * b.FILETE_MAQ + m.fita_ripa * b.FILETE_RIPA
    #   ⭐ o terceirizado lançado JÁ TEM a filetagem de ripa como linha; a
    #     de máquina não é lançada, entra aqui, igual ao `custo()`.
    d['terc'] = sum(q * u for _n, q, u in m.terc) + fita_maq * b.FILETE_MAQ
    d['vidro'] = sum(q * u for _n, q, u in m.vidro)
    d['pecas'] = sum(q for _n, _L, _A, _e, _m, q, *_ in m.pecas)
    #   ── a ferragem, separada em: a que muda e a que não muda ───────────
    d['corr'] = sum(q for _n, q, u in m.ferr if u == CORR_HETTICH)
    d['corre'] = sum(q for _n, q, u in m.ferr if u == CORRE_HETTICH)
    d['fer_fixa'] = sum(q * u for _n, q, u in m.ferr
                        if u not in (CORR_HETTICH, CORRE_HETTICH))
    #   ⭐⭐ É ISTO QUE DECIDE SE O ITEM MUDA DE PREÇO ENTRE AS LINHAS.
    d['muda'] = bool(d['corr'] or d['corre'])
    return d


def custo_item(d, linha, arred=0.0, corte_chapa=0.0):
    """Custo direto do item na linha, já com consumível, corte e embalagem."""
    f = LINHAS[linha]
    fer = d['fer_fixa'] + d['corr'] * f['corr'] + d['corre'] * f['corre']
    chapa = d['mat'] + arred
    cons = (chapa + d['fita'] + d['filete']) * b.CONSUMIVEIS
    corte = corte_chapa + d['pecas'] * b.CORTE_PECA
    sub = chapa + d['fita'] + cons + fer + d['terc'] + d['vidro'] + corte
    return sub * (1 + b.EMBALAGEM)


def monta():
    """Todos os itens, com o arredondamento de chapa rateado no ambiente."""
    I = [item(m) for m in lv.M]
    #   ── o arredondamento e o corte por chapa são do AMBIENTE ───────────
    #     ⭐ rateados pela ÁREA de cada material, que é o que os causa —
    #       nunca pelo custo total, que já tem ferragem dentro.
    for amb in {d['amb'] for d in I}:
        da = [(m, d) for m, d in zip(lv.M, I) if d['amb'] == amb]
        area = {}
        for m, _d in da:
            for k, a in m.areas().items():
                area[k] = area.get(k, 0.0) + a
        for k, a in area.items():
            preco = b.PRECO[f'{k[0]} {k[1]}']
            cheia = b.chapas(a) * preco
            frac = a / (b.CHAPA_M2 * b.APROV) * preco
            n = b.chapas(a)
            for m, d in da:
                parte = m.areas().get(k, 0.0) / a if a else 0.0
                d['arred'] = d.get('arred', 0.0) + (cheia - frac) * parte
                d['corte_chapa'] = (d.get('corte_chapa', 0.0)
                                    + n * b.CORTE_CHAPA * parte)
    for d in I:
        d.setdefault('arred', 0.0); d.setdefault('corte_chapa', 0.0)
        for k in LINHAS:
            d[k] = custo_item(d, k, d['arred'], d['corte_chapa'])
            mc = LINHAS[k]['mc'] if d['muda'] else MC_FIXA
            d[k + '_mc'] = mc
            d[k + '_pv'] = d[k] / (b.BASE - mc)
    return I


def _trava(I):
    """⭐⭐ AS DUAS PROVAS, e elas são o motivo de este arquivo existir."""
    #   ① a soma dos itens tem de dar o custo direto do projeto
    alvo = lv.custo()['direto']
    for k in LINHAS:
        if k != 'Hettich':
            continue
        soma = sum(d[k] for d in I)
        assert abs(soma - alvo) < 0.02, (
            f'⛔⛔ a soma dos itens na linha {k} dá R$ {soma:,.2f} e o motor '
            f'diz R$ {alvo:,.2f} — diferença de R$ {soma - alvo:,.2f}')
    #   ② ITEM SEM A FERRAGEM QUE MUDA TEM DE TER O MESMO PREÇO NAS TRÊS
    for d in I:
        if d['muda']:
            continue
        pv = [round(d[k + '_pv'], 2) for k in LINHAS]
        assert len(set(pv)) == 1, (
            f'⛔⛔ "{d["amb"]} · {d["nome"]}" NÃO leva corrediça nem sistema '
            f'de correr e mesmo assim muda de preço entre as linhas: '
            + ' · '.join(f'R$ {p:,.2f}' for p in pv))


def main():
    I = monta(); _trava(I)
    print('═' * 96)
    print('ATTOS · COSTA LAGUNA — AS TRÊS LINHAS, ITEM A ITEM')
    print('═' * 96)
    print(f'  BASE {b.BASE:.2%} (vendedor {b.VENDEDOR:.0%}, sem cartão) · '
          f'MC {MC_FIXA:.0%} fixa nos itens que não mudam de ferragem')
    print(f'  {"":<44}{"BÁSICA":>15}{"HETTICH":>15}{"BLUM":>15}')
    print(f'  {"":<44}{"telescópica":>15}{"Quadro V6":>15}{"Movento":>15}')
    print(f'  {"":<44}{"MC 35%":>15}{"MC 38%":>15}{"MC 43%":>15}')
    print('─' * 96)
    tot = {k: 0.0 for k in LINHAS}
    for amb in sorted({d['amb'] for d in I},
                      key=lambda a: -sum(d['Blum_pv'] for d in I
                                         if d['amb'] == a)):
        print(f'  {amb.upper()}')
        for d in [x for x in I if x['amb'] == amb]:
            marca = ' ◆' if d['muda'] else '  '
            print(f'   {marca} {d["nome"][:39]:<39}'
                  + ''.join(f'{d[k + "_pv"]:>15,.0f}' for k in LINHAS))
            for k in LINHAS:
                tot[k] += d[k + '_pv']
    print('─' * 96)
    print(f'  {"A CASA":<43}' + ''.join(f'{tot[k]:>15,.0f}' for k in LINHAS))
    print(f'\n  ◆ = item que leva corrediça ou sistema de correr · '
          f'só estes mudam de preço entre as linhas')
    muda = [d for d in I if d['muda']]
    print(f'  {len(muda)} itens de {len(I)} mudam · os outros {len(I) - len(muda)} '
          f'têm PREÇO IDÊNTICO nas três colunas, e o motor trava se não tiverem')
    print(f'\n  da BÁSICA para a HETTICH: R$ {tot["Hettich"] - tot["Básica"]:>10,.2f}'
          f'   ({tot["Hettich"] / tot["Básica"] - 1:+.1%})')
    print(f'  da HETTICH para a BLUM:   R$ {tot["Blum"] - tot["Hettich"]:>10,.2f}'
          f'   ({tot["Blum"] / tot["Hettich"] - 1:+.1%})')
    print(f'  da BÁSICA para a BLUM:    R$ {tot["Blum"] - tot["Básica"]:>10,.2f}'
          f'   ({tot["Blum"] / tot["Básica"] - 1:+.1%})')
    ncorr = sum(d['corr'] for d in I); nsis = sum(d['corre'] for d in I)
    print(f'\n  ⭐ E A ESCADA TEM DOIS DEGRAUS QUE NÃO SE CONFUNDEM:')
    print(f'     a FERRAGEM · {ncorr:.0f} pares de corrediça e {nsis:.0f} '
          f'sistemas de correr')
    for k in LINHAS:
        c = ncorr * LINHAS[k]['corr'] + nsis * LINHAS[k]['corre']
        print(f'        {k:<10} R$ {c:>9,.2f} de custo')
    print(f'     a MARGEM   · 35% · 38% · 43% — e ela só pega nos '
          f'{len(muda)} itens com ferragem')
    #   ⚠⚠ E AQUI MORA UM CASO QUE VALE O SENHOR OLHAR: itens cujo CUSTO é
    #     idêntico entre duas linhas e cujo PREÇO não é, porque só a MC
    #     mudou. Acontece com o sistema de correr, que custa R$ 600 na
    #     básica e na Hettich — a Base não tem um mais barato.
    so_mc = [d for d in I if d['muda']
             and abs(d['Básica'] - d['Hettich']) < 0.01]
    if so_mc:
        print(f'\n  ⚠⚠ {len(so_mc)} ITEM(NS) COM O MESMO CUSTO NA BÁSICA E NA '
              f'HETTICH, E PREÇO DIFERENTE:')
        for d in so_mc:
            dif = d['Hettich_pv'] - d['Básica_pv']
            print(f'       {d["amb"]} · {d["nome"][:38]:<38} '
                  f'R$ {d["Básica_pv"]:>9,.0f} → R$ {d["Hettich_pv"]:>9,.0f}'
                  f'   (+R$ {dif:,.0f}, só MC)')
        print('     ⛔ Eles levam SISTEMA DE CORRER e não levam corrediça — e o '
              'sistema custa\n       R$ 600 nas duas linhas, porque a Base não '
              'tem um mais barato. O cliente\n       paga 3 pontos de MC a mais '
              'sem levar ferragem diferente nenhuma.\n     ⚠ Ou a básica leva um '
              'sistema mais simples (e aí falta o preço dele na\n       Base), ou '
              'estes itens ficam na MC de 35% também. É decisão sua.')


if __name__ == '__main__':
    main()
