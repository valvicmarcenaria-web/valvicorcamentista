#!/usr/bin/env python3
"""Acrescenta à Controle de Pagamentos o que o painel precisa — sem regerar nada.

    python3 ajustar-controle-pagamentos.py ENTRADA.xlsx SAIDA.xlsx

Este arquivo tem quatro anos de histórico e abas que ninguém aqui escreveu
(a "Página1", com o levantamento de prejuízos). Por isso ele é **alterado no
lugar**, não regerado: o script abre o arquivo real e acrescenta.

O que entra:

  1 · Previsão · valor e Previsão · data nas abas de ano.
      Vão para o fim das colunas, não no meio. Inserir coluna no meio moveria
      os cinco blocos de pagamento, e as fórmulas que os somam — em três abas
      e quatro anos — apontariam para o lugar errado, em silêncio. Se depois
      você quiser essas colunas ao lado de "Situação", faça a mudança DENTRO do
      Google Sheets: lá, inserir coluna reescreve as referências sozinho.

  2 · Aba "Custo da Empresa": uma linha por mês, com custo fixo e despesa.
      É o que a Gestão Mensal guardava e que não pertence a projeto nenhum.
      Aba de máquina: cabeçalho na linha 1, dados a partir da 2, sem mesclagem.
"""
import sys

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

NAVY, NAVY2, GOLD = '0E2038', '16314F', 'C2A05A'
GOLDS, INPUT, CALC, LINE, MUTED = 'D8BD80', 'FBF7EC', 'EEF1F4', 'D6DBE2', '6C7785'
MOEDA, DATA = 'R$ #,##0.00', 'DD/MM/YYYY'
ANOS = ('2023', '2024', '2025', '2026')
MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# a folha de hoje, para servir de referência na primeira vez que alguém abrir
FOLHA_HOJE = 80560


def cabecalho(cel, texto):
    cel.value = texto
    cel.font = Font(name='Arial', size=8, bold=True, color='FFFFFF')
    cel.fill = PatternFill('solid', fgColor=NAVY2)
    cel.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cel.border = Border(bottom=Side(style='medium', color=GOLD))


def main(entrada, saida):
    wb = openpyxl.load_workbook(entrada)
    tocadas = []

    # ── 1 · previsão de recebimento nas abas de ano ──
    for ano in ANOS:
        if ano not in wb.sheetnames:
            continue
        ws = wb[ano]
        col_v, col_d = ws.max_column + 2, ws.max_column + 3   # deixa uma coluna de respiro
        cabecalho(ws.cell(9, col_v), 'Previsão · valor')
        cabecalho(ws.cell(9, col_d), 'Previsão · data')
        ws.column_dimensions[ws.cell(9, col_v).column_letter].width = 15
        ws.column_dimensions[ws.cell(9, col_d).column_letter].width = 14
        linhas = 0
        for r in range(10, ws.max_row + 1):
            if ws.cell(r, 3).value is None and ws.cell(r, 1).value in MESES:
                continue                                   # linha divisora de mês
            for col, nf in ((col_v, MOEDA), (col_d, DATA)):
                cel = ws.cell(r, col)
                cel.fill = PatternFill('solid', fgColor=INPUT)
                cel.font = Font(name='Arial', size=9, color='1B2733')
                cel.number_format = nf
                cel.border = Border(bottom=Side(style='thin', color=LINE))
            linhas += 1
        tocadas.append(f'{ano}: previsão em {ws.cell(9, col_v).column_letter} e '
                       f'{ws.cell(9, col_d).column_letter}, {linhas} linhas preparadas')

    # ── 2 · aba Custo da Empresa ──
    nome = 'Custo da Empresa'
    if nome in wb.sheetnames:
        del wb[nome]
    ce = wb.create_sheet(nome)
    ce.sheet_properties.tabColor = GOLD
    ce.sheet_view.showGridLines = False
    ce.freeze_panes = 'A2'
    cols = [('Competência', 14, DATA), ('Ano', 8, '0'), ('Mês', 14, None),
            ('Custo fixo', 15, MOEDA), ('Outras despesas', 16, MOEDA),
            ('Total do mês', 15, MOEDA), ('Observação', 46, None)]
    for i, (titulo, larg, _) in enumerate(cols, start=1):
        cabecalho(ce.cell(1, i), titulo)
        ce.column_dimensions[ce.cell(1, i).column_letter].width = larg
    ce.row_dimensions[1].height = 26

    import datetime
    r = 2
    for ano in (2026, 2027):
        for m, mes in enumerate(MESES, start=1):
            ce.cell(r, 1, datetime.date(ano, m, 1)).number_format = DATA
            ce.cell(r, 2, ano).number_format = '0'
            ce.cell(r, 3, mes)
            for c in (4, 5):
                cel = ce.cell(r, c)
                cel.fill = PatternFill('solid', fgColor=INPUT)
                cel.number_format = MOEDA
            t = ce.cell(r, 6, f'=IF(AND($D{r}="",$E{r}=""),"",'
                              f'ROUND(IF($D{r}="",0,$D{r})+IF($E{r}="",0,$E{r}),2))')
            t.number_format = MOEDA
            t.fill = PatternFill('solid', fgColor=CALC)
            t.font = Font(name='Arial', size=9, bold=True, color=NAVY2)
            for c in range(1, 8):
                cel = ce.cell(r, c)
                cel.border = Border(bottom=Side(style='thin', color=LINE))
                if cel.font.name is None or cel.font.size is None:
                    cel.font = Font(name='Arial', size=9, color='1B2733')
                if c in (1, 2):
                    cel.alignment = Alignment(horizontal='center')
            r += 1

    nota = ce.cell(r + 1, 1,
                   '  Custo fixo = folha, pró-labore, aluguel, energia e tudo que a empresa paga '
                   f'mesmo sem vender. Em out/2026 a folha fechada era de R$ {FOLHA_HOJE:,.0f}'
                   .replace(',', '.') + '. Outras despesas = o que varia e não pertence a projeto '
                   'nenhum. O painel lê esta aba para o custo fixo do mês.')
    ce.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1, end_column=7)
    nota.font = Font(name='Arial', size=8.5, color='41505D')
    nota.fill = PatternFill('solid', fgColor='F6EDD6')
    nota.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ce.row_dimensions[r + 1].height = 34
    tocadas.append(f'{nome}: 24 meses (2026 e 2027)')

    wb.save(saida)
    print('═' * 72)
    print('CONTROLE DE PAGAMENTOS · acréscimos')
    print('═' * 72)
    for l in tocadas:
        print('  ·', l)
    print(f'\n  abas preservadas: {len(wb.sheetnames)} — {", ".join(wb.sheetnames)}')
    print(f'\nOK → {saida}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
