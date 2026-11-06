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
    'Blum':    dict(corr=300.0, corre=900.0, mc=0.43, marca='Movento',
                    alvo=230_000.0),
}
#   ⭐⭐ A BLUM FECHOU PELO ALVO, NÃO PELA MC [Jonathan, 04/11/2026]: "no
#     preço geral suba a blum para 230k. e diluar coerentemente entre os
#     itens". Então a MC dela deixa de ser escolha e passa a ser RESULTADO:
#     a linha inteira roda na MC que faz o total dar 230k.
#   ⛔⛔ E ISSO SUSPENDE, SÓ NA BLUM, A REGRA DOS 38% FIXOS. Ele a deu com
#     "PODE manter", que é permissão, e depois mandou a Blum a 230k, que é
#     ordem — e as duas não cabem juntas. Escolhi a ordem, e registro a
#     permissão que ela derruba.
#   ⭐ POR QUE ASSIM E NÃO CONCENTRANDO NOS 6 ITENS COM FERRAGEM: aquele
#     caminho pedia MC de 49,7% nesses seis enquanto os outros doze ficavam
#     em 38%. Um painel a 38% e um armário a 49,7% no mesmo projeto não é
#     uma escada de produto — é um preço sem explicação na hora em que o
#     cliente perguntar. A MC única de 46,1% é UM número, e ele se explica:
#     a Blum é outra linha, com outra ferragem e outra garantia.
MC_FIXA = 0.38   # ⭐ a MC dos itens que NÃO mudam de linha
ALVO_BLUM = 230_000.0   # ⭐ [Jonathan, 04/11/2026] "suba a blum para 230k"

# ════════════════════════════════════════════════════════════════════════
# AS DECISÕES COMERCIAIS — ⛔ AQUI, NUNCA NO LEVANTAMENTO
# ════════════════════════════════════════════════════════════════════════
#   ⭐⭐ O LEVANTAMENTO MEDE, A LINHA NEGOCIA. Um "ajuste de R$ 2.500" ou um
#     "preço final de 39.700" não têm peça, não têm chapa e não vão para o
#     plano de corte — se entrassem em `levantamento.py`, o quantitativo
#     passaria a carregar decisão de venda e o plano de corte mentiria.
#     Ficam aqui, nomeados, datados e com o efeito impresso.
#   ⛔ E CADA UM INVERTE O MODELO DA CASA: onde há preço cravado, a MC
#     deixa de ser escolha e passa a ser RESULTADO. O relatório imprime a
#     MC realizada de cada um, porque é ela que diz se o negócio fecha.
DECISOES = '[Jonathan, 04/11/2026]'

GRUPOS = [
    dict(amb='Cozinha', nome='Painel ripado do corredor com as duas portas '
                             'de correr',
         itens=['Painel ripado do corredor',
                'Porta de correr ripada · vestiário',
                'Porta de correr ripada · despensa'],
         cravado=39700.0,
         por=f'{DECISOES} "na cozinha vamos agrupar as duas portas de correr '
             f'com o painel ripado a um preço final de 39.700"'),
    dict(amb='Suíte', nome='Parede painelada da TV, com as duas portas',
         itens=['Parede painelada da TV'],
         cravado=15500.0,
         por=f'{DECISOES} "parede painel da tv com as duas portas a 15.500" · '
             f'⭐ este item NÃO leva corrediça nem sistema de correr, então '
             f'os 15.500 valem nas TRÊS linhas, pela regra do próprio dono'),
    dict(amb='Escritório', nome='Armário superior, bancada e armário inferior',
         itens=['Armário superior', 'Bancada e mesa', 'Armário inferior'],
         por=f'{DECISOES} "No escritorio, separe apenas o custo do painel '
             f'ripado, os demais pode mesclar"'),
    dict(amb='Hall', nome='Painel do hall, com porta de lavanderia e bit de '
                          'canto',
         itens=['Painel do hall com porta de lavanderia',
                'Bit de canto do painel'],
         por=f'{DECISOES} "hall, unifique os itens"'),
]

#   ⚠⚠ AJUSTE DE CUSTO CRAVADO. Não há peça a remover da cristaleira: o
#     levantamento dela está medido na prancha. Isto é o dono dizendo que o
#     custo dela é outro, e entra como linha DECLARADA, não como peça que
#     some do plano de corte.
AJUSTE_CUSTO = {
    ('Cozinha', 'Cristaleira'):
        (-2500.0, f'{DECISOES} "a cristaleira, subtraia 2.500 de custo em '
                  f'cada linha" · ⛔ o QUANTITATIVO não mudou — nenhuma peça '
                  f'saiu da prancha. Mudou o custo cravado pelo dono'),
}

#   ⭐⭐ MC TRAVADA: item pequeno cuja MC não pode subir com a linha.
MC_TRAVADA = {
    ('Suíte', 'Mesas de cabeceira'):
        (MC_FIXA, f'{DECISOES} "mesas de cabeceira nao pode dobrar o preço '
                  f'so em funçao das corrediças, reveja isso" · ⛔ ELE ESTÁ '
                  f'CERTO E A CAUSA NÃO ERA A CORREDIÇA: 4 pares a mais '
                  f'custam R$ 880, mas a MC de 35% para 43% move o DIVISOR '
                  f'de 0,4548 para 0,3748, e sozinha isso é +21%. Num item '
                  f'de R$ 2 mil a alavanca da margem pesa mais que a peça. '
                  f'⭐ A MC fica em 38% nas três e só o custo da ferragem '
                  f'varia — que é o que o senhor quis dizer'),
}


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
    """Os itens, agrupados e com as decisões comerciais aplicadas."""
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
            cheia, n = b.chapas(a) * preco, b.chapas(a)
            frac = a / (b.CHAPA_M2 * b.APROV) * preco
            for m, d in da:
                parte = m.areas().get(k, 0.0) / a if a else 0.0
                d['arred'] = d.get('arred', 0.0) + (cheia - frac) * parte
                d['corte_chapa'] = (d.get('corte_chapa', 0.0)
                                    + n * b.CORTE_CHAPA * parte)
    for d in I:
        d.setdefault('arred', 0.0); d.setdefault('corte_chapa', 0.0)
        for k in LINHAS:
            d[k] = custo_item(d, k, d['arred'], d['corte_chapa'])
        #   ⚠ o ajuste de custo cravado entra DEPOIS do motor, nas 3 linhas
        aj = AJUSTE_CUSTO.get((d['amb'], d['nome']))
        if aj:
            for k in LINHAS:
                d[k] += aj[0]
            d['ajuste'] = aj

    # ── OS GRUPOS: vários itens viram UM, por decisão comercial ──────────
    G, usados = [], set()
    for g in GRUPOS:
        membros = [d for d in I
                   if d['amb'] == g['amb'] and d['nome'] in g['itens']]
        falta = set(g['itens']) - {d['nome'] for d in membros}
        assert not falta, (f'⛔⛔ grupo "{g["nome"]}" pede itens que não '
                           f'existem no levantamento: {sorted(falta)}')
        for d in membros:
            usados.add((d['amb'], d['nome']))
        novo = dict(amb=g['amb'], nome=g['nome'], grupo=g,
                    membros=[d['nome'] for d in membros],
                    muda=any(d['muda'] for d in membros),
                    corr=sum(d['corr'] for d in membros),
                    corre=sum(d['corre'] for d in membros))
        for k in LINHAS:
            novo[k] = sum(d[k] for d in membros)
        G.append(novo)
    SAIDA = [d for d in I if (d['amb'], d['nome']) not in usados] + G
    #   ⭐ a ordem do levantamento, com cada grupo onde o 1º membro estava
    ordem = {(d['amb'], d['nome']): i for i, d in enumerate(I)}
    SAIDA.sort(key=lambda d: ordem.get(
        (d['amb'], d.get('membros', [d['nome']])[0]), 999))

    # ── O PREÇO: cravado quando há, calculado quando não há ─────────────
    for d in SAIDA:
        g = d.get('grupo') or {}
        cravado = g.get('cravado')
        trava = MC_TRAVADA.get((d['amb'], d['nome']))
        if cravado:
            #   ⭐⭐ O CRAVADO É DA LINHA HETTICH, a de referência, e dele
            #     sai a MC REALIZADA. As outras duas linhas andam os MESMOS
            #     pontos que o senhor pediu (−3 e +5), sobre ela.
            mc_h = b.BASE - d['Hettich'] / cravado
            d['mc_ref'] = mc_h
            for k in LINHAS:
                mc = mc_h + (LINHAS[k]['mc'] - LINHAS['Hettich']['mc']) \
                    if d['muda'] else mc_h
                d[k + '_mc'] = mc
                d[k + '_pv'] = d[k] / (b.BASE - mc)
        else:
            for k in LINHAS:
                mc = (trava[0] if trava else
                      (LINHAS[k]['mc'] if d['muda'] else MC_FIXA))
                d[k + '_mc'] = mc
                d[k + '_pv'] = d[k] / (b.BASE - mc)
        if trava:
            d['trava'] = trava

    #   ── a linha que tem ALVO fecha pelo alvo, e a MC vira resultado ────
    for k, f in LINHAS.items():
        if not f.get('alvo'):
            continue
        #   ⛔⛔ O PREÇO CRAVADO DE UM ITEM QUE NÃO MUDA DE FERRAGEM É
        #     INTOCÁVEL, E A PRIMEIRA VERSÃO DISTO ERRAVA FEIO. Diluindo o
        #     alvo sobre TUDO, a parede da TV — cravada em R$ 15.500, MC
        #     realizada de 57,6% — caía para R$ 10.303 na Blum, porque a MC
        #     única de 46,1% é MENOR que a dela. ⛔ A linha premium ficava
        #     com um item MAIS BARATO que a intermediária, e isso não se
        #     explica para cliente nenhum.
        #   ⭐ Então o cravado sai da diluição e o alvo se faz no resto.
        #   ⛔⛔ E A MC TRAVADA TAMBÉM SOBREVIVE AO ALVO. A primeira versão
        #     disto derrubou a trava das mesas de cabeceira: a Blum passou a
        #     rodar numa MC única e elas voltaram a +70% da básica, que é
        #     EXATAMENTE o que o dono mandou consertar. ⭐ Trava é trava —
        #     ela sai da diluição, como o preço cravado.
        fora = [d for d in SAIDA
                if (d.get('grupo', {}).get('cravado') and not d['muda'])
                or d.get('trava')]
        resto = [d for d in SAIDA if d not in fora]
        pv_fora = 0.0
        for d in fora:
            if d.get('trava'):
                d[k + '_mc'] = d['trava'][0]
                d[k + '_pv'] = d[k] / (b.BASE - d['trava'][0])
            else:
                d[k + '_mc'] = d['mc_ref']
                d[k + '_pv'] = d['grupo']['cravado']
            pv_fora += d[k + '_pv']
        sobra = f['alvo'] - pv_fora
        custo = sum(d[k] for d in resto)
        mc = b.BASE - custo / sobra
        f['mc_realizada'] = mc
        f['fora_da_diluicao'] = [d['nome'] for d in fora]
        for d in resto:
            d[k + '_mc'] = mc
            d[k + '_pv'] = d[k] / (b.BASE - mc)
        #   ⭐ a prova: a soma tem de dar o alvo ao centavo
        soma = sum(d[k + '_pv'] for d in SAIDA)
        assert abs(soma - f['alvo']) < 0.01, (
            f'⛔⛔ a linha {k} deveria fechar em R$ {f["alvo"]:,.2f} e deu '
            f'R$ {soma:,.2f}')
    return SAIDA


def _trava(I):
    """⭐⭐ AS DUAS PROVAS, e elas são o motivo de este arquivo existir."""
    #   ① a soma dos itens tem de dar o custo do motor MAIS os ajustes
    #     ⭐ e os ajustes entram EXPLÍCITOS na conta da trava: se um dia
    #       alguém acrescentar um ajuste e esquecer daqui, ela acusa.
    ajuste = sum(v[0] for v in AJUSTE_CUSTO.values())
    alvo = lv.custo()['direto'] + ajuste
    soma = sum(d['Hettich'] for d in I)
    assert abs(soma - alvo) < 0.02, (
        f'⛔⛔ a soma dos itens na linha Hettich dá R$ {soma:,.2f} e o motor '
        f'mais os ajustes dá R$ {alvo:,.2f} — diferença de '
        f'R$ {soma - alvo:,.2f}')
    #   ② ITEM SEM A FERRAGEM QUE MUDA TEM DE TER O MESMO PREÇO —
    #     ⛔⛔ MAS SÓ NAS LINHAS QUE NÃO FECHAM POR ALVO. Esta trava disparou
    #       no instante em que a Blum passou a fechar em 230k, e estava
    #       CERTA: fechar uma linha por alvo suspende a regra dos 38% fixos
    #       nela, porque o alvo pega todo o projeto. ⭐ Em vez de afrouxar a
    #       trava, estreitei o que ela cobre — e deixei escrito por quê, para
    #       que ninguém a "conserte" de volta sem saber o que está desfazendo.
    #   ③ ⭐⭐ A ESCADA NÃO PODE DESCER. Nenhum item pode ficar mais
    #     barato numa linha superior — foi exatamente isso que aconteceu
    #     com a parede da TV quando a Blum passou a fechar por alvo, e é o
    #     tipo de coisa que ninguém vê numa tabela de 18 linhas.
    ordem = list(LINHAS)
    for d in I:
        for a, c in zip(ordem, ordem[1:]):
            assert d[c + '_pv'] >= d[a + '_pv'] - 0.01, (
                f'⛔⛔ A ESCADA DESCE em "{d["amb"]} · {d["nome"]}": '
                f'{a} R$ {d[a + "_pv"]:,.2f} → {c} R$ {d[c + "_pv"]:,.2f}. '
                f'Linha superior com item mais barato não se explica.')
    livres = [k for k, f in LINHAS.items() if not f.get('alvo')]
    for d in I:
        if d['muda']:
            continue
        pv = [round(d[k + '_pv'], 2) for k in livres]
        assert len(set(pv)) == 1, (
            f'⛔⛔ "{d["amb"]} · {d["nome"]}" NÃO leva corrediça nem sistema '
            f'de correr e mesmo assim muda de preço entre as linhas '
            + ', '.join(livres) + ': '
            + ' · '.join(f'R$ {p:,.2f}' for p in pv))


def main():
    I = monta(); _trava(I)
    print('═' * 96)
    print('ATTOS · COSTA LAGUNA — AS TRÊS LINHAS, ITEM A ITEM')
    print('═' * 96)
    mcb = LINHAS['Blum'].get('mc_realizada')
    print(f'  BASE {b.BASE:.2%} (vendedor {b.VENDEDOR:.0%}, sem cartão) · '
          f'MC {MC_FIXA:.0%} fixa nos itens sem ferragem, nas linhas '
          f'básica e Hettich')
    print(f'  ⭐ A BLUM FECHA PELO ALVO DE R$ {LINHAS["Blum"]["alvo"]:,.0f}: '
          f'MC única de {mcb:.1%} em TODOS os itens dela')
    print(f'  {"":<44}{"BÁSICA":>15}{"HETTICH":>15}{"BLUM":>15}')
    print(f'  {"":<44}{"telescópica":>15}{"Quadro V6":>15}{"Movento":>15}')
    print(f'  {"":<44}{"MC 35%":>15}{"MC 38%":>15}{"MC " + format(LINHAS["Blum"]["mc_realizada"], ".1%"):>15}')
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
          f'têm PREÇO IDÊNTICO na básica e na Hettich, e o motor trava se '
          f'não tiverem')
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
    print(f'     a MARGEM   · básica {LINHAS["Básica"]["mc"]:.0%} · Hettich '
          f'{LINHAS["Hettich"]["mc"]:.0%} · Blum '
          f'{LINHAS["Blum"]["mc_realizada"]:.1%} (pelo alvo)')
    print(f'        ⭐ fora da diluição da Blum, por decisão: '
          + ' · '.join(LINHAS['Blum']['fora_da_diluicao']))

    # ════════════════════════════════════════════════════════════════════
    #   ⛔⛔ OS 230k DA BLUM — E A CONTRADIÇÃO QUE ELES ABREM
    # ════════════════════════════════════════════════════════════════════
    #   ⭐⭐ [Jonathan, 04/11/2026] "no preço geral suba a blum para 230k. e
    #     diluar coerentemente entre os itens."
    #   ⛔ ISSO BRIGA COM A REGRA DELE PRÓPRIO, dada minutos antes: "os
    #     demais pode manter a mc de 38% fixo" — que faz 12 itens terem
    #     PREÇO IDÊNTICO nas três linhas. Se os 230k forem diluídos sobre
    #     TODOS, esses 12 deixam de ser iguais. Se forem diluídos só sobre
    #     os que levam ferragem, eles levam o aumento inteiro.
    #   ⭐ Não escolho por ele. Meço as três saídas e mostro o que cada uma
    #     quebra, com nome e número.
    # ── onde a MC deixou de ser escolha e virou resultado ───────────────
    crav = [d for d in I if d.get('grupo', {}).get('cravado')]
    if crav:
        print('\n  ⭐⭐ ONDE O PREÇO FOI CRAVADO, A MC É RESULTADO — e é ela '
              'que diz se fecha:')
        for d in crav:
            g = d['grupo']
            print(f'     {d["nome"][:50]:<50} R$ {g["cravado"]:>9,.0f}  '
                  f'→ MC REALIZADA {d["mc_ref"]:>5.1%}')
            print(f'        custo R$ {d["Hettich"]:,.2f} · '
                  f'{"ACIMA" if d["mc_ref"] >= b.MC_PISO else "⛔ ABAIXO"} '
                  f'do piso da casa ({b.MC_PISO:.0%})'
                  + (f' · os itens somavam R$ '
                     f'{sum(x for x in [0]):,.0f}' if False else ''))
    trav = [d for d in I if d.get('trava')]
    if trav:
        print('\n  ⭐ ONDE A MC FOI TRAVADA:')
        for d in trav:
            dif = d['Blum_pv'] / d['Básica_pv'] - 1
            print(f'     {d["nome"][:50]:<50} MC {d["trava"][0]:.0%} nas três '
                  f'· básica → blum {dif:+.0%}')
        print('     ⭐ ERA +70% e caiu para +41%: o que sobrou é SÓ a '
              'corrediça, R$ 880 de custo\n        em 4 pares.')
        print('     ⚠⚠ E AÍ MORA OUTRA COISA QUE VALE OLHAR: a Base cobra '
              'R$ 300 o par de Blum\n        para QUALQUER gaveta. A gaveta '
              'da mesa de cabeceira tem 45 cm de profundidade\n        e '
              '14 cm de altura — leva uma corrediça MENOR, e mais barata, que '
              'a de\n        cozinha. Se a Base separasse por tamanho, estes '
              '+41% cairiam sozinhos.')

    print('\n' + '═' * 96)
    print('COMO A BLUM CHEGOU AOS 230k — e os dois caminhos que eu descartei')
    print('═' * 96)
    print('  ⛔⛔ OS 230k BRIGAVAM COM A REGRA DO PRÓPRIO DONO, dada minutos')
    print('     antes: "os demais pode manter a mc de 38% fixo", que faz os')
    print('     itens sem ferragem terem preço IGUAL nas três linhas. Um alvo')
    print('     de projeto pega TODO o projeto. As duas não cabem juntas.')
    print('  ⭐ "Pode manter" é permissão; "suba a blum para 230k" é ordem.')
    print('     A ordem ganhou, e a permissão fica registrada como derrubada.')
    print('\n  ① diluir sobre TUDO, proporcional ao preço')
    print('     ⛔ descartado: a parede da TV, cravada em R$ 15.500 com MC de')
    print('       57,6%, CAÍA para R$ 10.303 na Blum — linha premium com item')
    print('       mais barato que a intermediária não se explica.')
    print('  ② concentrar nos itens com ferragem')
    print('     ⛔ descartado: pedia MC de 49,7% nesses seis enquanto os outros')
    print('       doze ficavam em 38%. Um painel a 38% e um armário a 49,7% no')
    print('       mesmo projeto não é escada de produto, é preço sem resposta.')
    print(f'  ⭐ ③ ESCOLHIDO: MC única de '
          f'{LINHAS["Blum"]["mc_realizada"]:.1%} na Blum, com o preço cravado')
    print('       e a MC travada FORA da diluição. É UM número, e ele se')
    print('       explica: a Blum é outra linha, com outra ferragem e outra')
    print('       garantia.')
    print(f'\n  ⚠ E ELA RODA ACIMA DA FAIXA IDEAL DA CASA ({b.MC_FAIXA[0]:.0%} '
          f'a {b.MC_FAIXA[1]:.0%}). É escolha do dono, não descoberta minha.')


if __name__ == '__main__':
    main()
