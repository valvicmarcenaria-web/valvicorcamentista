# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — ONDE ESTÃO OS 20%.

⭐⭐ [Jonathan, 04/11/2026] "considere um investimento no orcamento 20% a
  menos". ⛔ E 20% a menos NÃO é uma célula que se digita: é produto que sai
  do projeto, ou margem que sai da casa. Este arquivo mede cada alavanca
  pelo que ela REALMENTE devolve, para a escolha ser de quem pode escolher.

⛔⛔ A ALAVANCA QUE NÃO EXISTE: baixar a MC até o preço cair 20%.
  Preço = custo ÷ (BASE − MC). Para o preço cair 20% com o mesmo custo, o
  denominador tem de SUBIR 25% — e a MC teria de ir de 35% para 24,7%.
  O piso da casa é 35%. Essa porta está fechada, e fica medida aqui para
  ninguém tentar abri-la de novo.

uso:  python3 -I economia.py
"""
import importlib.util, sys, pathlib, contextlib, io, subprocess, re

P = pathlib.Path(__file__).resolve().parent


def _mod(nome, arq, env=None):
    s = importlib.util.spec_from_file_location(nome, P / arq)
    m = importlib.util.module_from_spec(s); sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m


b = _mod('b', 'base.py')
lv = _mod('lv', 'levantamento.py')

CUSTO = lv.custo()['direto']
MC = b.MC_PISO


def preco(custo, base=b.BASE_COM_UM, mc=MC):
    return custo / (base - mc)


ATUAL = preco(CUSTO)
#   ⚠ O QUE A PLANILHA MOSTRA HOJE, que não é o combinado: em 04/11/2026 a
#     célula da MC alvo ('Preço e Comissões'!D7) estava em 50%, posta à mão.
MC_PLANILHA = 0.50


def rodar(**env):
    """O motor inteiro, com outra ripa. ⭐ Subprocesso de propósito: módulo
    já importado não se reconfigura, e fingir que sim é como se inventam
    dois números para a mesma coisa."""
    import os
    e = dict(os.environ); e.update({k: str(v) for k, v in env.items()})
    out = subprocess.run([sys.executable, str(P / 'levantamento.py')],
                         capture_output=True, text=True, env=e, cwd=P).stdout
    m = re.search(r'CUSTO DIRETO\s+R\$\s+([\d,]+\.\d\d)', out)
    return float(m.group(1).replace(',', ''))


def linha(nome, custo, base=b.BASE_COM_UM, mc=MC, nota=''):
    pr = preco(custo, base, mc)
    d = pr / ATUAL - 1
    return (nome, custo, pr, d, nota)


def main():
    print('═' * 78)
    print('ATTOS · COSTA LAGUNA — ONDE ESTÃO OS 20%')
    print('═' * 78)
    print(f'  hoje: custo direto R$ {CUSTO:,.2f} · BASE {b.BASE_COM_UM:.4%} · '
          f'MC {MC:.0%}')
    print(f'        PREÇO  R$ {ATUAL:,.2f}')

    #   ⛔⛔ E A PRIMEIRA PERGUNTA É "20% A MENOS DE QUÊ?". A planilha hoje
    #     NÃO está nos 35% combinados: a célula da MC alvo está em 50%, posta
    #     à mão. São dois números na tela ao mesmo tempo, e −20% de cada um
    #     dá uma conta completamente diferente — uma se resolve mexendo numa
    #     célula, a outra exige tirar produto do projeto.
    print('\n' + '─' * 78)
    print('⛔⛔ 20% A MENOS DE QUÊ? SÃO DUAS CONTAS DIFERENTES')
    print('─' * 78)
    p50 = preco(CUSTO, mc=MC_PLANILHA)
    alvo50 = p50 * 0.8
    mc50 = b.BASE_COM_UM - CUSTO / alvo50
    print(f'  ① do que a PLANILHA mostra hoje, com a MC em '
          f'{MC_PLANILHA:.0%}: R$ {p50:,.2f}')
    print(f'     −20% = R$ {alvo50:,.2f}  →  basta a MC ir de '
          f'{MC_PLANILHA:.0%} para {mc50:.1%}')
    print(f'     ⭐ ZERO mudança de produto, e ainda '
          f'{(mc50 - MC) * 100:.1f} pontos ACIMA do piso de {MC:.0%}')
    print(f'\n  ② do COMBINADO, com a MC em {MC:.0%}: R$ {ATUAL:,.2f}')
    print(f'     −20% = R$ {ATUAL * 0.8:,.2f}  →  são R$ {ATUAL * 0.2:,.2f} '
          f'a tirar, e por margem NÃO DÁ')
    print(f'     ⛔ precisa sair produto · é o que a tabela abaixo mede')

    L = []
    #   ⭐ A ALAVANCA QUE NÃO TOCA NO PROJETO
    L.append(linha('A · SEM VENDEDOR — a casa vende direto', CUSTO,
                   base=b.BASE_SEM_RT,
                   nota='o produto é EXATAMENTE o mesmo · a MC da casa não '
                        'muda um ponto · só não entra a comissão de 10%'))
    #   ⭐ A ALAVANCA DO PRODUTO: a ripa
    for rl, vao in ((3, 1.5), (4, 2), (5, 2.5)):
        c = rodar(RIPA_L=rl, VAO=vao)
        L.append(linha(f'B · RIPA DE {rl:g}, VÃO DE {vao:g} (passo {rl+vao:g})',
                       c, nota='mesmo desenho, ripa mais larga · menos ripas, '
                               'menos fita, menos filetagem, menos chapa de 18'))
    #   ⛔ A ALAVANCA FECHADA
    mc20 = b.BASE_COM_UM - (b.BASE_COM_UM - MC) / 0.8
    L.append(linha(f'C · MC EM {mc20:.1%} — ⛔ ABAIXO DO PISO DE 35%', CUSTO,
                   mc=mc20, nota='⛔ a casa trabalharia de graça 10 pontos '
                                 'abaixo do piso · medido só para fechar a porta'))
    L.append(linha('C′ · MC em 33% — dois pontos abaixo do piso', CUSTO,
                   mc=0.33, nota='⚠ fura o piso e devolve pouco'))

    print('\n' + '─' * 78)
    print(f'{"ALAVANCA":<44}{"CUSTO":>12}{"PREÇO":>13}{"Δ":>9}')
    print('─' * 78)
    for nome, c, pr, d, _ in L:
        print(f'{nome:<44}{c:>12,.0f}{pr:>13,.0f}   {d:>+6.1%}')

    #   ⭐⭐ E A COMBINAÇÃO, que é o que de fato responde ao pedido
    print('\n' + '═' * 78)
    print('AS COMBINAÇÕES QUE CHEGAM AOS 20%')
    print('═' * 78)
    for rl, vao in ((2, 1), (3, 1.5), (4, 2)):
        c = CUSTO if (rl, vao) == (2, 1) else rodar(RIPA_L=rl, VAO=vao)
        pr = preco(c, base=b.BASE_SEM_RT)
        d = pr / ATUAL - 1
        marca = '  ⭐ CHEGA' if d <= -0.20 else ''
        rot = f'sem vendedor + ripa de {rl:g}, vão de {vao:g}'
        print(f'  {rot:<42}R$ {pr:>11,.2f}   {d:>+6.1%}{marca}')

    print('\n' + '─' * 78)
    print('O QUE CADA UMA CUSTA DE VERDADE')
    print('─' * 78)
    _vistos = set()
    for nome, _c, _p, _d, nota in L:
        k = nome.split('·')[0].strip()
        if nota and k not in _vistos:
            _vistos.add(k)
            print(f'  {k} — {nota}')


if __name__ == '__main__':
    main()
