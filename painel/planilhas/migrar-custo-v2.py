#!/usr/bin/env python3
"""Migra a Custo por Projeto para a estrutura com notas fiscais e datas de etapa.

    python3 gerar-custo-projeto.py                  # estrutura nova, vazia
    python3 migrar-custo-v2.py ANTIGO.xlsx [SAIDA]  # traz os preenchimentos

O que mudou de uma versão para a outra:

  · o bloco 1 ganhou quatro linhas de nota fiscal e o total faturado, então
    TUDO o que fica abaixo dele desceu seis linhas;
  · o bloco 3 ganhou `fabricado em` e `montado em`, então as colunas de
    montagem e de projetista andaram para a direita.

      ambiente antigo:  A  B  C  D  E  F  G  H  I  J  K  L  M
      ambiente novo:    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
                                          ↑ nova       ↑ nova

Nada é escrito no arquivo antigo: ele é só lido. O relatório no fim diz
quantas células vieram de cada aba — confira contra o inventário antes de
aposentar o original.
"""
import json
import sys

import openpyxl

NOVO_PADRAO = 'Valvic_Custo_por_Projeto.xlsx'
FIXAS = ('Instruções', 'Painel Geral', 'Listas', 'Ficha Modelo', 'Base · Comissões')
DESLOCA = 6          # quanto o bloco 1 empurrou tudo que vem depois

# ── estrutura da versão anterior ────────────────────────────────────────
V0 = dict(R_ID2=7, R_ID4=9, R_KPI_V=13, R_VENDA=28,
          R_IMP=32, R_RTP=37, R_AMB0=43, R_AMBF=54,
          R_COORD=59, R_PROJC=62, R_RB0=111, R_RBF=122, R_RB_SUB=123,
          R_LAN0=127, R_LANF=186)

# coluna do ambiente na versão anterior → coluna na nova
COL_AMB = {'A': 'A',    # nome do ambiente
           'C': 'C',    # valor
           'D': 'D', 'E': 'E',          # produção: quem e %
           'G': 'H', 'H': 'I',          # montagem: quem e %
           'J': 'L', 'K': 'M'}          # projetista: quem e %


def vazio(x):
    return x is None or (isinstance(x, str) and not x.strip())


def formula(x):
    return isinstance(x, str) and x.startswith('=')


def main(antigo, saida):
    with open('mapa-ficha.json', encoding='utf-8') as fp:
        M = json.load(fp)

    velho = openpyxl.load_workbook(antigo)
    novo = openpyxl.load_workbook(saida)

    relatorio, avisos = [], []
    total = 0

    for aba in [s for s in velho.sheetnames if s not in FIXAS]:
        if aba not in novo.sheetnames:
            avisos.append(f'{aba!r}: não existe na estrutura nova — NADA foi trazido. '
                          f'Acrescente em PROJETOS_ABAS e gere de novo.')
            continue
        a, b = velho[aba], novo[aba]
        n = 0

        def leva(origem, destino=None):
            """Copia uma célula digitada à mão. Fórmula e vazio não passam."""
            nonlocal n
            v = a[origem].value
            if vazio(v) or formula(v):
                return
            b[destino or origem] = v
            n += 1

        # identificação — não mudou de lugar
        for ref in ('A7', 'D7', 'F7', 'H7', 'J7', 'A9', 'D9', 'F9'):
            leva(ref)

        # bloco 1 · valor de venda — mesma linha
        leva(f'C{V0["R_VENDA"]}')
        leva(f'D{V0["R_VENDA"]}')

        # bloco 2 · custos de venda
        for r in range(V0['R_IMP'], V0['R_RTP'] + 1):
            for col in 'BCD':
                leva(f'{col}{r}', f'{col}{r + DESLOCA}')

        # bloco 3 · ambientes — linha desloca e coluna remapeia
        for r in range(V0['R_AMB0'], V0['R_AMBF'] + 1):
            for antes, depois in COL_AMB.items():
                leva(f'{antes}{r}', f'{depois}{r + DESLOCA}')

        # bloco 4 · percentuais das comissões
        for r in range(V0['R_COORD'], V0['R_PROJC'] + 1):
            leva(f'B{r}', f'B{r + DESLOCA}')

        # bloco 6 · orçado por categoria
        for cat in M['CATEGORIAS_COMPRA']:
            novo_r = M['LINHAS_OC'][cat]
            leva(f'C{novo_r - DESLOCA}', f'C{novo_r}')

        # bloco 7 · retrabalho e contingência
        for r in range(V0['R_RB0'], V0['R_RBF'] + 1):
            for col in 'ABEG':
                leva(f'{col}{r}', f'{col}{r + DESLOCA}')
        leva(f'C{V0["R_RB_SUB"]}', f'C{V0["R_RB_SUB"] + DESLOCA}')

        # bloco 8 · livro de compras
        for r in range(V0['R_LAN0'], V0['R_LANF'] + 1):
            for col in 'ABDEGI':
                leva(f'{col}{r}', f'{col}{r + DESLOCA}')

        relatorio.append((aba, n))
        total += n

    novo.save(saida)

    print('═' * 72)
    print('MIGRAÇÃO · notas fiscais e datas de etapa')
    print('═' * 72)
    for aba, n in relatorio:
        print(f'  {aba:<28} {n:>5} células')
    print(f'  {"TOTAL":<28} {total:>5} células')
    if avisos:
        print('\nATENÇÃO')
        for l in avisos:
            print(f'  · {l}')
    print(f'\nOK → {saida}')
    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else NOVO_PADRAO)
