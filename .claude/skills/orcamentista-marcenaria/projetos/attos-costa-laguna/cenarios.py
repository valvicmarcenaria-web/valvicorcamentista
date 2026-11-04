# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — o preço por ambiente, nas linhas Hettich e Blum.

⭐ A escada de ferragem é a da Base de Custos, e os preços são os mesmos
  que o Gustavo Raposo usa:

      linha      corrediça/par   dobradiça/un   garantia Valvic
      Hettich        150              50            10 anos
      Blum           300              50            30 anos

  ⛔⛔ E REPARE: HETTICH E BLUM TÊM A MESMA DOBRADIÇA, R$ 50. Entre as duas
    linhas **só a corrediça muda**. Num projeto de armário isso pesa; num
    projeto de PAINEL, como este, quase não aparece — e esse é o achado
    desta folha.

⛔ O RATEIO É POR CONSUMO DE MATERIAL, NÃO POR CHUTE. A chapa se compra
  inteira e arredondada UMA VEZ, para o projeto todo — é assim que o
  dinheiro sai. Mas o preço por ambiente precisa de uma repartição, e ela
  é a proporção da ÁREA DE PEÇA de cada ambiente, que é o que a casa manda:
  "alocar preço por peça na proporção do material".
  ⚠ Logo o valor de um ambiente isolado NÃO é o que ele custaria sozinho:
    sozinho ele pagaria a chapa inteira e o mínimo de cada padrão.
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

# ── as duas linhas ──────────────────────────────────────────────────────
#   ⭐ [Jonathan, 03/11/2026] "versão hettich vamos usar Rometal de 600 e na
#     BLUM Siforma de 900" — o sistema de correr das duas portas ripadas
#     também muda de linha, e é a SEGUNDA (e última) ferragem que muda.
LINHAS = {
    'Hettich': dict(corr=150.0, dobr=50.0, corre=600.0, gar='10 anos',
                    sist='Rometal', mc=0.35),
    'Blum':    dict(corr=300.0, dobr=50.0, corre=900.0, gar='30 anos',
                    sist='SI Forma', mc=0.40),
}
#   ⭐ [Jonathan, 03/11/2026] "Mc de 35% na hettich e 40% na BLUM".
#   ⛔⛔ E ISSO INVERTE O SENTIDO DA ESCADA. Até agora as duas linhas tinham
#     a MESMA MC e a Blum custava mais só pela ferragem — R$ 5.835, 2,8%.
#     Com a Blum cinco pontos acima, a diferença passa a vir da MARGEM, não
#     da peça: a mesma casa, com ferragem de R$ 1.950 a mais, salta de preço
#     porque o divisor muda. A Hettich fica no PISO da casa.
#   ⛔ a dobradiça de PORTA DE VIDRO não entra na escada: é outro produto
#     (R$ 70 na Base, e ainda A COTAR). Não muda entre as linhas.
#   ⛔ Não existe mais uma MC do projeto: cada linha tem a sua.


def custo_por_ambiente(linha):
    """Devolve, por ambiente: área de peça, custo próprio e custo rateado."""
    f = LINHAS[linha]
    amb = {}
    for m in lv.M:
        d = amb.setdefault(m.amb, dict(area=0.0, fita=0.0, fita_ripa=0.0,
                                       ferr=0.0, terc=0.0, vidro=0.0, n=0,
                                       pecas=0))
        d['n'] += 1
        d['area'] += sum(L * A * q / 10000
                         for _n, L, A, _e, _m, q, *_ in m.pecas)
        #   ⛔⛔ E AQUI NÃO SE DESEMPACOTA POR POSIÇÃO. Esta linha era
        #     `sum(q for *_x, q, _f, _o in m.pecas)`, e no instante em que a
        #     peça ganhou um nono campo o `q` passou a apanhar a FITA: a
        #     contagem de peças virou metragem e o custo saltou R$ 6.712 sem
        #     erro nenhum. Índice nomeado não desliza quando a tupla cresce.
        d['pecas'] = d.get('pecas', 0) + sum(pc[lv.I_QTD] for pc in m.pecas)
        d['fita'] += m.fita
        d['fita_ripa'] += m.fita_ripa
        d['vidro'] += sum(q * u for _n, q, u in m.vidro)
        d['terc'] += sum(q * u for _n, q, u in m.terc if 'Filetagem' not in _n)
        for nome, q, u in m.ferr:
            # ⭐ a troca de linha mexe SÓ na corrediça e na dobradiça comum
            if nome.startswith('Corrediça'):
                u = f['corr']
            elif nome.startswith('Dobradiça') and 'vidro' not in nome:
                u = f['dobr']
            #   ⛔ a de VIDRO fica fora: é outro produto, não é a escada.
            elif nome == 'Sistema de correr':
                u = f['corre']
            d['ferr'] += q * u

    # ── a chapa, contada POR ABA, em número cheio ───────────────────────
    #   ⛔⛔ EU ESTAVA RATEANDO, E O MODELO DA CASA NÃO RATEIA. A planilha
    #     conta a chapa em cada aba de ambiente e o Painel soma — "não existe
    #     2,7 chapas, são 3, e cada padrão puxa no mínimo uma". Rateio dá um
    #     total menor (43 chapas contra 51) porque supõe que a sobra de um
    #     ambiente serve o vizinho, o que o plano de corte raramente permite.
    #   ⭐ E ter dois números para a mesma coisa — um no Python e outro na
    #     planilha — é a divergência que não dá erro. O motor segue a casa.
    area_amb = {}
    for m in lv.M:
        d = area_amb.setdefault(m.amb, {})
        for k, v in m.areas().items():
            d[k] = d.get(k, 0.0) + v

    #   ⚠⚠ E AQUI HÁ UMA ESCOLHA, NÃO UMA CONTA. Contar por aba dá 51 chapas
    #     e R$ 28.450; contar o projeto dá 43 e R$ 24.350 — R$ 4.100, 16,8%.
    #     Fico com a do PROJETO, porque é o que a casa COMPRA, e porque por
    #     aba o Gourmet de 1,77 m² pagaria três chapas inteiras sozinho,
    #     sendo que ele é parede-meia com a cozinha e divide material.
    #   ⭐ O mínimo de uma chapa por padrão continua valendo — no projeto.
    c = lv.custo()
    total_area = sum(d['area'] for d in amb.values())
    CHAPAS_ABA = sum(b.chapas(ar) for d in area_amb.values() for ar in d.values())
    CHAPAS_PROJ = sum(n for _a, n in c['chapas'].values())

    # ⭐⭐ A CHAPA SE CONTA INTEIRA EM CADA ABA — É O MÉTODO DA CASA.
    #   ⛔⛔ E EU TINHA FEITO DIFERENTE. Contei a chapa pelo PROJETO (43) e
    #     ratei por padrão, para não fazer o Gourmet de 1,77 m² pagar três
    #     chapas inteiras sozinho. A conta é defensável — e NÃO é a da casa.
    #     O orçamento do Gustavo Raposo arredonda em CADA aba (a cozinha dele
    #     tem 13 chapas) e explica a sobra na linha "Arredondamento de chapa
    #     para número cheio". Uma planilha que conta diferente das outras é
    #     uma planilha que ninguém consegue comparar com as outras.
    #   ⚠ O preço sobe: 51 chapas no lugar de 43, R$ 4.100 de custo.
    #     Fica registrado, e a decisão de voltar atrás é do Jonathan.
    out = {}
    for nome, d in amb.items():
        fr = d['area'] / total_area
        chapa = sum(b.chapas(ar) * b.PRECO[f'{k[0]} {k[1]}']
                    for k, ar in area_amb[nome].items())
        n_ch = sum(b.chapas(ar) for ar in area_amb[nome].values())
        d['chapas'] = sum(b.chapas(ar) for ar in area_amb[nome].values())
        fita = d['fita'] * b.FITA_COR * b.FITA_PERDA
        filete = d['fita_ripa'] * b.FILETE_MAO \
            + (d['fita'] - d['fita_ripa']) * b.FILETE_MAQ
        cons = (chapa + fita + filete) * b.CONSUMIVEIS
        #   ⭐ O CORTE É DO AMBIENTE, e as duas unidades não se misturam:
        #     a PEÇA entra inteira, porque peça não se parte; a CHAPA entra
        #     rateada pela mesma fração que rateia a chapa em si.
        #   ⛔⛔ E AQUI EU JÁ ERREI UMA VEZ, HÁ TRÊS MINUTOS: ratear o corte
        #     pela fração CRUA de área (168,50 ÷ 4,07 = 41,4 chapas) cobra
        #     41 cortes de uma compra de 43, e a trava pegou R$ 3,26. Quem
        #     manda é a chapa COMPRADA, e ela se rateia, nunca se recalcula.
        corte = n_ch * b.CORTE_CHAPA + d['pecas'] * b.CORTE_PECA
        direto = (chapa + fita + cons + filete + d['terc'] + d['ferr']
                  + d['vidro'] + corte)
        direto *= (1 + b.EMBALAGEM)
        out[nome] = dict(n=d['n'], area=d['area'], chapa=chapa, fita=fita,
                         pecas=d['pecas'], corte=corte, n_ch=n_ch,
                         chapas=d['chapas'], filete=filete, terc=d['terc'],
                         ferr=d['ferr'], vidro=d['vidro'], direto=direto)
    return out


# ⭐⭐ A TRAVA QUE PROVA QUE OS DOIS MOTORES SÃO UM SÓ.
#   O `levantamento.custo()` soma o projeto inteiro de uma vez; o
#   `custo_por_ambiente('Hettich')` soma ambiente por ambiente e rateia a
#   chapa. São dois caminhos para o MESMO número, e durante meia sessão eles
#   deram R$ 67.590 e R$ 69.303 sem nenhum dos dois reclamar — porque o
#   `base.py` guardava a ferragem de um nível que este projeto não vende.
#   ⛔ Enquanto esta linha passar, não existe um segundo custo escondido.
_H = sum(d['direto'] for d in custo_por_ambiente('Hettich').values())
_P = lv.custo()['direto']
assert abs(_H - _P) < 0.01, (
    f'⛔⛔ DOIS CUSTOS PARA A MESMA CASA: por ambiente R$ {_H:,.2f} · '
    f'pelo projeto R$ {_P:,.2f} · diferença R$ {_H - _P:,.2f}')


def tabela():
    linhas = {k: custo_por_ambiente(k) for k in LINHAS}
    ambientes = sorted(linhas['Hettich'],
                       key=lambda a: -linhas['Blum'][a]['direto'])
    return ambientes, linhas


if __name__ == '__main__':
    amb, lin = tabela()
    print('═' * 74)
    print(f'ATTOS · COSTA LAGUNA — PREÇO POR AMBIENTE · BASE {b.BASE:.2%}'
          f' · Hettich MC {LINHAS["Hettich"]["mc"]:.0%}'
          f' · Blum MC {LINHAS["Blum"]["mc"]:.0%}')
    print('═' * 74)
    print(f'{"ambiente":<14}{"móveis":>7}{"peça m²":>10}'
          f'{"HETTICH":>15}{"BLUM":>15}')
    tot = {k: 0.0 for k in LINHAS}
    for a in amb:
        row = f'{a:<14}{lin["Blum"][a]["n"]:>7}{lin["Blum"][a]["area"]:>10.2f}'
        for k in ('Hettich', 'Blum'):
            pv = b.preco(lin[k][a]['direto'], LINHAS[k]['mc'])
            tot[k] += pv
            row += f'{pv:>15,.0f}'
        print(row)
    print('─' * 74)
    row = f'{"A CASA":<14}{sum(lin["Blum"][a]["n"] for a in amb):>7}' \
          f'{sum(lin["Blum"][a]["area"] for a in amb):>10.2f}'
    for k in ('Hettich', 'Blum'):
        row += f'{tot[k]:>15,.0f}'
    print(row)

    print(f'\n  a diferença entre as duas linhas: '
          f'R$ {tot["Blum"] - tot["Hettich"]:,.2f}  '
          f'({(tot["Blum"]/tot["Hettich"]-1)*100:.1f}%)')
    ncorr = sum(q for m in lv.M for n, q, u in m.ferr if n.startswith('Corrediça'))
    ndobr = sum(q for m in lv.M for n, q, u in m.ferr
                if n.startswith('Dobradiça') and 'vidro' not in n)
    nvid = sum(q for m in lv.M for n, q, u in m.ferr if 'vidro' in n)
    nsis = sum(q for m in lv.M for n, q, u in m.ferr if n == 'Sistema de correr')
    d_corr = ncorr * (LINHAS['Blum']['corr'] - LINHAS['Hettich']['corr'])
    d_sis = nsis * (LINHAS['Blum']['corre'] - LINHAS['Hettich']['corre'])
    # ⛔⛔ ESTA FRASE JÁ MENTIU UMA VEZ. Enquanto as duas linhas tinham a
    #   MESMA MC, a diferença vinha só da ferragem. Com MC diferente, a maior
    #   parte vem da MARGEM — e dizer "vem de dois lugares só" viraria falso
    #   sem ninguém mexer numa linha de código. Agora a conta se separa.
    so_ferr = sum(b.preco(lin['Blum'][a]['direto'], LINHAS['Hettich']['mc'])
                  for a in amb) - tot['Hettich']
    print(f'  ⭐ E ela se parte em duas, que não se confundem:')
    print(f'      a FERRAGEM        R$ {so_ferr:>10,.2f}  '
          f'({so_ferr / (tot["Blum"] - tot["Hettich"]) * 100:.0f}% da diferença)')
    print(f'         {ncorr:.0f} pares de corrediça, R$ {d_corr:,.2f} de custo')
    print(f'         {nsis:.0f} sistemas de correr, R$ {d_sis:,.2f} de custo')
    print(f'      a MARGEM          R$ '
          f'{tot["Blum"] - tot["Hettich"] - so_ferr:>10,.2f}  '
          f'({(tot["Blum"] - tot["Hettich"] - so_ferr) / (tot["Blum"] - tot["Hettich"]) * 100:.0f}%)')
    print(f'         os cinco pontos de MC entre 35% e 40%')
    print(f'    As {ndobr:.0f} dobradiças comuns NÃO mudam: Hettich e Blum '
          f'custam o mesmo (R$ 50).')
    print(f'    E as {nvid:.0f} de porta de VIDRO são outro produto (R$ 70), '
          f'fora da escada.')

    print(f'\n  a MESMA casa, nas duas pontas da faixa:')
    for k in ('Hettich', 'Blum'):
        for m_ in (0.35, 0.40, 0.42):
            t = sum(b.preco(lin[k][a]['direto'], m_) for a in amb)
            marca = '  ← o combinado' if m_ == LINHAS[k]['mc'] else ''
            print(f'    {k:<8} MC {m_:.0%}  →  R$ {t:>12,.2f}{marca}')
