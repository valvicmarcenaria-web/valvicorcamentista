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
                    sist='Rometal'),
    'Blum':    dict(corr=300.0, dobr=50.0, corre=900.0, gar='30 anos',
                    sist='SI Forma'),
}
#   ⛔ a dobradiça de PORTA DE VIDRO não entra na escada: é outro produto
#     (R$ 70 na Base, e ainda A COTAR). Não muda entre as linhas.
MC = 0.42        # ⭐ a mesma que o Jonathan cravou para Hettich e Blum no
#                  Gustavo Raposo. A faixa da casa é 35 a 40; 42 é a dele.


def custo_por_ambiente(linha):
    """Devolve, por ambiente: área de peça, custo próprio e custo rateado."""
    f = LINHAS[linha]
    amb = {}
    for m in lv.M:
        d = amb.setdefault(m.amb, dict(area=0.0, fita=0.0, fita_ripa=0.0,
                                       ferr=0.0, terc=0.0, vidro=0.0, n=0))
        d['n'] += 1
        d['area'] += sum(L * A * q / 10000 for _n, L, A, _e, _m, q in m.pecas)
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

    # ── a chapa, comprada UMA vez para o projeto todo ───────────────────
    total_area = sum(d['area'] for d in amb.values())
    c = lv.custo()
    c_chapa = c['c_chapa']

    out = {}
    for nome, d in amb.items():
        fr = d['area'] / total_area
        chapa = c_chapa * fr                       # ⭐ rateio por área
        fita = d['fita'] * b.FITA_COR * b.FITA_PERDA
        filete = d['fita_ripa'] * b.FILETE_MAO \
            + (d['fita'] - d['fita_ripa']) * b.FILETE_MAQ
        cons = (chapa + fita) * b.CONSUMIVEIS
        direto = chapa + fita + cons + filete + d['terc'] + d['ferr'] + d['vidro']
        direto *= (1 + b.EMBALAGEM)
        out[nome] = dict(n=d['n'], area=d['area'], chapa=chapa, fita=fita,
                         filete=filete, terc=d['terc'], ferr=d['ferr'],
                         vidro=d['vidro'], direto=direto)
    return out


def tabela(mc=MC):
    linhas = {k: custo_por_ambiente(k) for k in LINHAS}
    ambientes = sorted(linhas['Hettich'],
                       key=lambda a: -linhas['Blum'][a]['direto'])
    return ambientes, linhas, mc


if __name__ == '__main__':
    amb, lin, mc = tabela()
    print('═' * 74)
    print(f'ATTOS · COSTA LAGUNA — PREÇO POR AMBIENTE · MC {mc:.0%} · '
          f'BASE {b.BASE:.2%}')
    print('═' * 74)
    print(f'{"ambiente":<14}{"móveis":>7}{"peça m²":>10}'
          f'{"HETTICH":>15}{"BLUM":>15}')
    tot = {k: 0.0 for k in LINHAS}
    for a in amb:
        row = f'{a:<14}{lin["Blum"][a]["n"]:>7}{lin["Blum"][a]["area"]:>10.2f}'
        for k in ('Hettich', 'Blum'):
            pv = b.preco(lin[k][a]['direto'], mc)
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
    print(f'  ⭐ E ela vem de dois lugares só:')
    print(f'      {ncorr:.0f} pares de corrediça  · R$ {d_corr:>8,.2f} de custo')
    print(f'      {nsis:.0f} sistemas de correr  · R$ {d_sis:>8,.2f} de custo')
    print(f'    As {ndobr:.0f} dobradiças comuns NÃO mudam: Hettich e Blum '
          f'custam o mesmo (R$ 50).')
    print(f'    E as {nvid:.0f} de porta de VIDRO são outro produto (R$ 70), '
          f'fora da escada.')

    print(f'\n  outras margens, sobre o total Hettich:')
    for m_ in (0.35, 0.38, 0.40, 0.45):
        t = sum(b.preco(lin['Hettich'][a]['direto'], m_) for a in amb)
        print(f'    MC {m_:.0%}  →  R$ {t:>12,.2f}')
