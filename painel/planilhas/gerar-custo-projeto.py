#!/usr/bin/env python3
"""Gera o Controle de Custo Direto por Projeto da Valvic.

Uma lâmina por projeto (duplicável) com todo o custo direto e indireto em
ORÇADO x REALIZADO x DESVIO — é isso que mede a eficiência do orçamento.
Um painel geral consolida os projetos, puxando cada lâmina por INDIRECT.

Uso:  python3 gerar-custo-projeto.py
Saída: Valvic_Custo_por_Projeto.xlsx
"""
import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.properties import PageSetupProperties
from openpyxl.formatting.rule import FormulaRule
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.axis import ChartLines
from openpyxl.chart.text import RichText
from openpyxl.drawing.text import Paragraph, ParagraphProperties, CharacterProperties

NAVY, NAVY2 = '0E2038', '16314F'
GOLD, GOLDS, GOLDBG = 'C2A05A', 'D8BD80', 'F6EDD6'
INK, MUTED = '1B2733', '6C7785'
LINE, LINE2 = 'E8E3D8', 'DFDACD'
OK, BLUE, RED, AMBER = '2F7D4F', '2F5D8C', 'B0413F', 'B57A16'
OKBG, REDBG, AMBBG, BLUEBG = 'E2F0E7', 'FBE7E6', 'FBF1DC', 'E7EEF6'
INPUT, WHITE, CALC = 'FFF9E3', 'FFFFFF', 'F4F6F8'

F = 'Arial'
def font(sz=10, b=False, c=INK, i=False):
    return Font(name=F, size=sz, bold=b, color=c, italic=i)
def fill(c): return PatternFill('solid', fgColor=c)
def side(c=LINE, st='thin'): return Side(style=st, color=c)
GRID = Border(bottom=side(LINE), left=side(LINE), right=side(LINE))
BOTTOM2 = Border(bottom=side(LINE2))
CTR = Alignment(horizontal='center', vertical='center')
CTRW = Alignment(horizontal='center', vertical='center', wrap_text=True)
LEFT = Alignment(horizontal='left', vertical='center')
LEFTI = Alignment(horizontal='left', vertical='center', indent=1)
LEFTIW = Alignment(horizontal='left', vertical='center', wrap_text=True, indent=1)
RIGHT = Alignment(horizontal='right', vertical='center', indent=1)
MOEDA, MOEDA0, PCT0, PCT1, DATA = 'R$ #,##0.00', 'R$ #,##0', '0%', '0.0%', 'DD/MM/YYYY'
DIAS = '0 "dias"'

EQUIPE = ['Deivson', 'Samuel', 'Cezar', 'Jackson', 'Filipe', 'Joelson', 'Jomar',
          'Jonathan Godoy', 'Bruna', 'Hugo', 'Karla', 'Terceiro / avulso']
VENDEDORES = ['Jonathan', 'Vitor', 'Indicação', 'Arquiteto parceiro', 'Outro']
CAUSAS = ['Erro de projeto', 'Erro de medição', 'Erro de produção', 'Erro de montagem',
          'Falha de material', 'Dano no transporte', 'Mudança pedida pelo cliente',
          'Falha de fornecedor', 'Outro']

NCOL = 10
LP = {c: get_column_letter(c) for c in range(1, 61)}
W_FICHA = [30, 10, 14, 18, 8, 13, 18, 8, 13, 14]

wb = openpyxl.Workbook()
wb.remove(wb.active)


def faixa_marca(ws, ncols, titulo, sub, linha=1):
    for i, (txt, fo, bg, alt) in enumerate([
            ('VALVIC MARCENARIA', Font(name=F, size=13, bold=True, color=WHITE), NAVY, 26),
            ('Vargas Decor Ltda   ·   CNPJ 17.269.304/0001-51   ·   Belo Horizonte / MG',
             Font(name=F, size=8, color='9FB0C4'), NAVY, 15),
            (titulo, Font(name=F, size=15, bold=True, color=WHITE), NAVY2, 28),
            (sub, Font(name=F, size=8.5, color='7A5B17', italic=True), GOLDBG, 17)]):
        r = linha + i
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncols)
        c = ws.cell(r, 1, txt); c.font = fo; c.alignment = LEFTI
        ws.row_dimensions[r].height = alt
        for cc in range(1, ncols + 1):
            ws.cell(r, cc).fill = fill(bg)
    return linha + 4


def titulo_secao(ws, row, ncols, texto, nota=''):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    c = ws.cell(row, 1, ('  ' + texto.upper()) + (f'          {nota}' if nota else ''))
    c.font = Font(name=F, size=9, bold=True, color=NAVY); c.alignment = LEFT
    for cc in range(1, ncols + 1):
        cel = ws.cell(row, cc)
        cel.fill = fill(GOLDBG); cel.border = Border(bottom=side(GOLD, 'medium'))
    ws.row_dimensions[row].height = 20
    return row + 1


def cab(ws, row, pares, alt=26):
    for c0, span, txt in pares:
        if span > 1:
            ws.merge_cells(start_row=row, start_column=c0, end_row=row,
                           end_column=c0 + span - 1)
        c = ws.cell(row, c0, txt)
        c.font = Font(name=F, size=8.5, bold=True, color=WHITE); c.alignment = CTRW
        for k in range(span):
            cel = ws.cell(row, c0 + k); cel.fill = fill(NAVY2)
            cel.border = Border(left=side(NAVY2), right=side(NAVY2),
                                bottom=side(GOLD, 'medium'))
    ws.row_dimensions[row].height = alt
    return row + 1


def print_cfg(ws, area, retrato=False, margens=(0.4, 0.3, 0.4, 0.3)):
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.orientation = 'portrait' if retrato else 'landscape'
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = 1, 0
    ws.print_area = area
    l, r, t, b = margens
    ws.page_margins.left, ws.page_margins.right = l, r
    ws.page_margins.top, ws.page_margins.bottom = t, b
    ws.sheet_view.showGridLines = False


def dv(ws, formula, rng):
    d = DataValidation(type='list', formula1=formula, allow_blank=True, showDropDown=False)
    ws.add_data_validation(d); d.add(rng)


def bloco(ws, row, col, span, valor=None, *, f=None, bg=None, al=None, nf=None, bd=True):
    if span > 1:
        ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col + span - 1)
    c = ws.cell(row, col, valor)
    if f: c.font = f
    if al: c.alignment = al
    if nf: c.number_format = nf
    for k in range(span):
        cel = ws.cell(row, col + k)
        if bd: cel.border = GRID
        if bg: cel.fill = fill(bg)
    return c


F_ENT = Font(name=F, size=9.5, color=INK)
F_CALC = Font(name=F, size=9.5, color=NAVY2)
F_PCT = Font(name=F, size=9.5, bold=True, color='7A5B17')
F_SUB = Font(name=F, size=10, bold=True, color=WHITE)

# ══════════════ mapa de linhas da FICHA (o painel depende destes endereços)
R_ID1, R_ID2, R_ID3, R_ID4 = 6, 7, 8, 9
R_KPI_T, R_KPI_L, R_KPI_V = 11, 12, 13
R_VEN_T, R_VEN_H, R_VENDA = 15, 16, 17
R_CV_T, R_CV_H = 19, 20
R_IMP, R_MAQ, R_TRX, R_CVEND, R_PROJ, R_RTP = 21, 22, 23, 24, 25, 26
R_CV_SUB, R_LIQ = 27, 28
R_AMB_T, R_AMB_H, R_AMB0 = 30, 31, 32
N_AMB = 10
R_AMBF = R_AMB0 + N_AMB - 1
R_AMB_TOT = R_AMBF + 1
R_CO_T, R_CO_H = R_AMB_TOT + 2, R_AMB_TOT + 3
R_COORD, R_PRODC, R_MONTC, R_CO_SUB = R_CO_H + 1, R_CO_H + 2, R_CO_H + 3, R_CO_H + 4
R_CL_T, R_CL_H, R_CL0 = R_CO_SUB + 2, R_CO_SUB + 3, R_CO_SUB + 4
N_COL = 12
R_CLF = R_CL0 + N_COL - 1
R_CL_TOT = R_CLF + 1
MATERIAIS = ['MDF / MDP (chapas)', 'Fita de borda', 'Ferragens e acessórios',
             'Vidros e espelhos', 'Esquadrias', 'Lâmina natural',
             'Consumíveis (parafuso, adesivo, tíner, estopa, lixa)']
R_MAT_T, R_MAT_H, R_MAT0 = R_CL_TOT + 2, R_CL_TOT + 3, R_CL_TOT + 4
R_MATF = R_MAT0 + len(MATERIAIS) - 1
R_MAT_SUB = R_MATF + 1
TERCEIROS = ['Acabamento (pintura / laca)', 'Serralheria', 'Vidraceiro',
             'Outro terceirizado']
R_TER_T, R_TER_H, R_TER0 = R_MAT_SUB + 2, R_MAT_SUB + 3, R_MAT_SUB + 4
R_TERF = R_TER0 + len(TERCEIROS) - 1
R_TER_SUB = R_TERF + 1
LOGISTICA = ['Uber / aplicativo', 'Carreto e frete de entrega',
             'Logística da equipe (deslocamento)', 'Frete de material',
             'Estacionamento, pedágio e outros']
R_LOG_T, R_LOG_H, R_LOG0 = R_TER_SUB + 2, R_TER_SUB + 3, R_TER_SUB + 4
R_LOGF = R_LOG0 + len(LOGISTICA) - 1
R_LOG_SUB = R_LOGF + 1
N_RETRAB = 6
R_RB_T, R_RB_H, R_RB0 = R_LOG_SUB + 2, R_LOG_SUB + 3, R_LOG_SUB + 4
R_RBF = R_RB0 + N_RETRAB - 1
R_RB_SUB = R_RBF + 1
CATEGORIAS = ['Custos de venda', 'Comissões operacionais', 'Material',
              'Serviços terceirizados', 'Logística', 'Retrabalho']
R_RES_T, R_RES_H, R_RES0 = R_RB_SUB + 2, R_RB_SUB + 3, R_RB_SUB + 4
R_RESF = R_RES0 + len(CATEGORIAS) - 1
R_CUSTO_TOT = R_RESF + 1
R_MC = R_CUSTO_TOT + 1
R_NOTA = R_MC + 2

VENDA = '$A$13'
SUBLINHAS = {'Custos de venda': R_CV_SUB, 'Comissões operacionais': R_CO_SUB,
             'Material': R_MAT_SUB, 'Serviços terceirizados': R_TER_SUB,
             'Logística': R_LOG_SUB, 'Retrabalho': R_RB_SUB}
print(f'ficha: venda {R_VENDA} · líquido {R_LIQ} · ambientes {R_AMB0}-{R_AMBF} · '
      f'resumo {R_RES0}-{R_MC} · fim {R_NOTA}')


# ══════════════════════════════════════════════════════════════════════
#  A FICHA DE PROJETO
# ══════════════════════════════════════════════════════════════════════
AMB_PROD_Q = f'$D${R_AMB0}:$D${R_AMBF}'
AMB_PROD_V = f'$F${R_AMB0}:$F${R_AMBF}'
AMB_MONT_Q = f'$G${R_AMB0}:$G${R_AMBF}'
AMB_MONT_V = f'$I${R_AMB0}:$I${R_AMBF}'


def linha_custo(ws, r, rotulo, tipo, *, base_o=None, base_r=None, dica=''):
    """tipo: 'pct' (B=% e C/D calculados) · 'rs' (C/D digitados) · 'calc'."""
    ws.row_dimensions[r].height = 17
    bloco(ws, r, 1, 1, rotulo, f=Font(name=F, size=9.5, color=INK), bg=WHITE, al=LEFTI)
    if tipo == 'pct':
        c = bloco(ws, r, 2, 1, None, f=F_PCT, bg=INPUT, al=CTR, nf=PCT1)
        bloco(ws, r, 3, 1, f'=IF($B{r}="","",ROUND($B{r}*{base_o},2))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 4, 1, f'=IF($B{r}="","",ROUND($B{r}*{base_r},2))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
    elif tipo == 'rs':
        bloco(ws, r, 2, 1, None, bg=WHITE)
        bloco(ws, r, 3, 1, None, f=F_ENT, bg=INPUT, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 4, 1, None, f=F_ENT, bg=INPUT, al=RIGHT, nf=MOEDA)
    else:                                    # calc: C e D vêm de fora
        bloco(ws, r, 2, 1, None, bg=WHITE)
        bloco(ws, r, 3, 1, None, f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 4, 1, None, f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
    bloco(ws, r, 5, 2, f'=IF(OR($C{r}="",$D{r}=""),"",ROUND($D{r}-$C{r},2))',
          f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
    bloco(ws, r, 7, 1, f'=IF(OR($D{r}="",{VENDA}="",{VENDA}=0),"",$D{r}/{VENDA})',
          f=Font(name=F, size=9, color=MUTED), bg=CALC, al=CTR, nf=PCT1)
    bloco(ws, r, 8, 3, dica or None, f=Font(name=F, size=8.5, color=INK), bg=INPUT, al=LEFTI)


CAB_CUSTO = [(1, 1, 'Item'), (2, 1, '%'), (3, 1, 'Orçado (R$)'), (4, 1, 'Realizado (R$)'),
             (5, 2, 'Desvio (R$)'), (7, 1, '% da venda'), (8, 3, 'Observação')]


def subtotal(ws, r, rotulo, ini, fim, dest=False):
    ws.row_dimensions[r].height = 20 if not dest else 24
    bg = NAVY if dest else NAVY2
    bloco(ws, r, 1, 2, rotulo, f=F_SUB if not dest else Font(name=F, size=11, bold=True,
                                                             color=WHITE), bg=bg, al=RIGHT)
    for col in (3, 4):
        bloco(ws, r, col, 1, f'=ROUND(SUM({LP[col]}{ini}:{LP[col]}{fim}),2)',
              f=Font(name=F, size=10 if not dest else 11.5, bold=True, color=GOLDS),
              bg=bg, al=RIGHT, nf=MOEDA)
    bloco(ws, r, 5, 2, f'=ROUND($D{r}-$C{r},2)',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=bg, al=RIGHT, nf=MOEDA)
    bloco(ws, r, 7, 1, f'=IF(OR({VENDA}="",{VENDA}=0),"",$D{r}/{VENDA})',
          f=Font(name=F, size=9.5, bold=True, color=GOLDS), bg=bg, al=CTR, nf=PCT1)
    bloco(ws, r, 8, 3, None, bg=bg)
    return r


def montar_ficha(ws, dados=None):
    ws.sheet_view.showGridLines = False
    for i, w in enumerate(W_FICHA, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    r = faixa_marca(ws, NCOL, 'FICHA DE CUSTO DO PROJETO',
                    'Fundo creme = você preenche · fundo cinza = calculado · '
                    'duplique esta aba a cada projeto novo e registre o nome dela no Painel Geral')
    assert r == R_ID1 - 1, f'faixa terminou em {r}'
    ws.row_dimensions[r].height = 6

    # ── identificação
    IDENT = [((1, 3, 'CLIENTE'), (4, 2, 'Nº DO PROJETO'), (6, 2, 'DATA DE ENTRADA'),
              (8, 2, 'ENTREGA PREVISTA'), (10, 1, 'ENTREGA REAL')),
             ((1, 3, 'PROJETO'), (4, 2, 'VENDEDOR'), (6, 2, 'COORDENADOR'),
              (8, 2, 'DIAS DE ATRASO'), (10, 1, 'SITUAÇÃO DA ENTREGA'))]
    for k, linha in enumerate(IDENT):
        rl, rv = R_ID1 + k * 2, R_ID2 + k * 2
        for c0, span, rot in linha:
            bloco(ws, rl, c0, span, rot, f=Font(name=F, size=7.5, bold=True, color=MUTED),
                  bg=WHITE, al=CTR, bd=False)
            calc = (k == 1 and c0 in (8, 10))
            bloco(ws, rv, c0, span, None,
                  f=Font(name=F, size=10, bold=True, color=NAVY2),
                  bg=CALC if calc else INPUT, al=LEFTI if c0 in (1, 4) else CTR)
        ws.row_dimensions[rl].height = 13
        ws.row_dimensions[rv].height = 21
    for ref, nf in ((f'F{R_ID2}', DATA), (f'H{R_ID2}', DATA), (f'J{R_ID2}', DATA),
                    (f'H{R_ID4}', DIAS)):
        ws[ref].number_format = nf
    ws[f'H{R_ID4}'] = (f'=IF(OR($H${R_ID2}="",$J${R_ID2}=""),"",$J${R_ID2}-$H${R_ID2})')
    ws[f'J{R_ID4}'] = (
        f'=IF($H${R_ID2}="","",IF($J${R_ID2}="",'
        f'IF(TODAY()>$H${R_ID2},"Atrasado","Em produção"),'
        f'IF($H${R_ID4}<=0,"No prazo","Atrasado")))')
    ws.row_dimensions[R_ID4 + 1].height = 8

    # ── faixa de resultado do projeto
    titulo_secao(ws, R_KPI_T, NCOL, 'Resultado do projeto',
                 'atualiza sozinho conforme você lança os custos abaixo')
    KPIS = [(1, 2, 'VALOR DE VENDA', MOEDA0), (3, 2, 'CUSTO TOTAL', MOEDA0),
            (5, 2, 'MARGEM DE CONTRIBUIÇÃO', MOEDA0), (7, 1, 'MC %', PCT1),
            (8, 1, 'MC % ORÇADA', PCT1), (9, 2, 'DESVIO DE CUSTO', MOEDA0)]
    for c0, span, rot, nf in KPIS:
        bloco(ws, R_KPI_L, c0, span, rot, f=Font(name=F, size=7.5, bold=True, color=MUTED),
              bg=WHITE, al=CTR, bd=False)
        bloco(ws, R_KPI_V, c0, span, None,
              f=Font(name=F, size=13, bold=True, color=NAVY), bg=GOLDBG, al=CTR, nf=nf)
    ws.row_dimensions[R_KPI_L].height = 13
    ws.row_dimensions[R_KPI_V].height = 30
    ws.row_dimensions[R_KPI_V + 1].height = 8

    # ── 1 · valor de venda
    titulo_secao(ws, R_VEN_T, NCOL, '1 · Valor de venda')
    cab(ws, R_VEN_H, CAB_CUSTO)
    linha_custo(ws, R_VENDA, 'Valor de venda do projeto', 'rs',
                dica='Orçado = valor da proposta · Realizado = valor fechado')
    ws[f'G{R_VENDA}'] = None
    ws.row_dimensions[R_VENDA + 1].height = 8

    # ── 2 · custos de venda
    titulo_secao(ws, R_CV_T, NCOL, '2 · Custos de venda',
                 'tudo que sai por causa da venda · define a RECEITA LÍQUIDA')
    cab(ws, R_CV_H, CAB_CUSTO)
    BASE_RT_O = f'($C${R_VENDA}-SUM($C${R_IMP}:$C${R_TRX}))'
    BASE_RT_R = f'({VENDA}-SUM($D${R_IMP}:$D${R_TRX}))'
    linha_custo(ws, R_IMP, 'Impostos sobre a nota (Simples)', 'pct',
                base_o=f'$C${R_VENDA}', base_r=VENDA, dica='% sobre o valor de venda')
    linha_custo(ws, R_MAQ, 'Taxa de máquina de cartão', 'pct',
                base_o=f'$C${R_VENDA}', base_r=VENDA, dica='% sobre o valor de venda')
    linha_custo(ws, R_TRX, 'Taxas de transação (PIX, boleto, TED)', 'rs',
                dica='valor em reais')
    linha_custo(ws, R_CVEND, 'Comissão de venda (vendedor)', 'pct',
                base_o=f'$C${R_VENDA}', base_r=VENDA, dica='% sobre o valor de venda')
    linha_custo(ws, R_PROJ, 'Projeto / anteprojeto (externo)', 'rs',
                dica='projetista ou arquiteto contratado para o projeto')
    linha_custo(ws, R_RTP, 'RT do parceiro', 'pct', base_o=BASE_RT_O, base_r=BASE_RT_R,
                dica='% sobre o líquido: venda menos impostos, máquina e taxas')
    subtotal(ws, R_CV_SUB, '(=) SUBTOTAL DOS CUSTOS DE VENDA', R_IMP, R_RTP)
    ws.row_dimensions[R_LIQ].height = 24
    bloco(ws, R_LIQ, 1, 2, '(=) RECEITA LÍQUIDA',
          f=Font(name=F, size=11, bold=True, color=WHITE), bg=NAVY, al=RIGHT)
    bloco(ws, R_LIQ, 3, 1, f'=ROUND($C${R_VENDA}-$C${R_CV_SUB},2)',
          f=Font(name=F, size=11.5, bold=True, color=GOLDS), bg=NAVY, al=RIGHT, nf=MOEDA)
    bloco(ws, R_LIQ, 4, 1, f'=ROUND({VENDA}-$D${R_CV_SUB},2)',
          f=Font(name=F, size=11.5, bold=True, color=GOLDS), bg=NAVY, al=RIGHT, nf=MOEDA)
    bloco(ws, R_LIQ, 5, 2, f'=ROUND($D${R_LIQ}-$C${R_LIQ},2)',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY, al=RIGHT, nf=MOEDA)
    bloco(ws, R_LIQ, 7, 1, f'=IF(OR({VENDA}="",{VENDA}=0),"",$D${R_LIQ}/{VENDA})',
          f=Font(name=F, size=9.5, bold=True, color=GOLDS), bg=NAVY, al=CTR, nf=PCT1)
    bloco(ws, R_LIQ, 8, 3, 'É esta a base das comissões de coordenação, produção e montagem',
          f=Font(name=F, size=8.5, color=GOLDS, i=True), bg=NAVY, al=LEFTI)
    ws.row_dimensions[R_LIQ + 1].height = 8

    # ── 3 · ambientes, produção e montagem
    titulo_secao(ws, R_AMB_T, NCOL, '3 · Ambientes, produção e montagem',
                 'um projeto tem vários ambientes · cada um com seu produtor e seu montador')
    cab(ws, R_AMB_H, [(1, 1, 'Ambiente'), (2, 1, '% do total'), (3, 1, 'Valor do ambiente (R$)'),
                      (4, 1, 'Produção — quem'), (5, 1, '%'), (6, 1, 'Comissão produção (R$)'),
                      (7, 1, 'Montagem — quem'), (8, 1, '%'), (9, 1, 'Comissão montagem (R$)'),
                      (10, 1, 'Total do ambiente')], alt=32)
    for r in range(R_AMB0, R_AMBF + 1):
        ws.row_dimensions[r].height = 18
        bloco(ws, r, 1, 1, None, f=F_ENT, bg=INPUT, al=LEFTI)
        bloco(ws, r, 2, 1, f'=IF(OR($C{r}="",{VENDA}="",{VENDA}=0),"",$C{r}/{VENDA})',
              f=Font(name=F, size=9, color=MUTED), bg=CALC, al=CTR, nf=PCT1)
        bloco(ws, r, 3, 1, None, f=Font(name=F, size=9.5, bold=True, color=NAVY),
              bg=INPUT, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 4, 1, None, f=F_ENT, bg=INPUT, al=LEFTI)
        bloco(ws, r, 5, 1, None, f=F_PCT, bg=INPUT, al=CTR, nf=PCT1)
        bloco(ws, r, 6, 1, f'=IF(OR($B{r}="",$E{r}="",$D${R_LIQ}=""),"",'
                           f'ROUND($B{r}*$D${R_LIQ}*$E{r},2))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 7, 1, None, f=F_ENT, bg=INPUT, al=LEFTI)
        bloco(ws, r, 8, 1, None, f=F_PCT, bg=INPUT, al=CTR, nf=PCT1)
        bloco(ws, r, 9, 1, f'=IF(OR($B{r}="",$H{r}="",$D${R_LIQ}=""),"",'
                           f'ROUND($B{r}*$D${R_LIQ}*$H{r},2))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 10, 1, f'=IF(AND($F{r}="",$I{r}=""),"",'
                            f'ROUND(IF($F{r}="",0,$F{r})+IF($I{r}="",0,$I{r}),2))',
              f=Font(name=F, size=9.5, bold=True, color=NAVY2), bg=CALC, al=RIGHT, nf=MOEDA)
    dv(ws, '=Listas!$A$2:$A$13', f'D{R_AMB0}:D{R_AMBF}')
    dv(ws, '=Listas!$A$2:$A$13', f'G{R_AMB0}:G{R_AMBF}')
    ws.row_dimensions[R_AMB_TOT].height = 20
    bloco(ws, R_AMB_TOT, 1, 1, 'SOMA DOS AMBIENTES', f=F_SUB, bg=NAVY2, al=RIGHT)
    bloco(ws, R_AMB_TOT, 2, 1, f'=IF({VENDA}=0,"",$C${R_AMB_TOT}/{VENDA})',
          f=Font(name=F, size=9.5, bold=True, color=GOLDS), bg=NAVY2, al=CTR, nf=PCT1)
    for col in (3, 6, 9, 10):
        bloco(ws, R_AMB_TOT, col, 1,
              f'=ROUND(SUM({LP[col]}{R_AMB0}:{LP[col]}{R_AMBF}),2)',
              f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=MOEDA)
    bloco(ws, R_AMB_TOT, 4, 2,
          f'=IF($C${R_AMB_TOT}=0,"—",IF(ROUND($C${R_AMB_TOT}-{VENDA},2)=0,'
          f'"OK · os ambientes somam o valor de venda",'
          f'"ATENÇÃO: diferença de "&TEXT($C${R_AMB_TOT}-{VENDA},"R$ #,##0.00")))',
          f=Font(name=F, size=8.5, bold=True, color=GOLDS), bg=NAVY2, al=CTR)
    bloco(ws, R_AMB_TOT, 7, 2, None, bg=NAVY2)
    ws.row_dimensions[R_AMB_TOT + 1].height = 8

    # ── 4 · comissões operacionais
    titulo_secao(ws, R_CO_T, NCOL, '4 · Comissões operacionais',
                 'calculadas sobre a RECEITA LÍQUIDA · o realizado vem dos ambientes acima')
    cab(ws, R_CO_H, CAB_CUSTO)
    linha_custo(ws, R_COORD, 'Coordenação de produção', 'pct',
                base_o=f'$C${R_LIQ}', base_r=f'$D${R_LIQ}',
                dica='quem coordena está na identificação, no topo da ficha')
    for r, rot, orig, dica in (
            (R_PRODC, 'Comissão de produção', f'$F${R_AMB_TOT}',
             'orçado = % único estimado · realizado = soma dos ambientes'),
            (R_MONTC, 'Comissão de montagem', f'$I${R_AMB_TOT}',
             'orçado = % único estimado · realizado = soma dos ambientes')):
        linha_custo(ws, r, rot, 'pct', base_o=f'$C${R_LIQ}', base_r=f'$D${R_LIQ}', dica=dica)
        bloco(ws, r, 4, 1, f'=IF({orig}=0,"",{orig})', f=F_CALC, bg=CALC,
              al=RIGHT, nf=MOEDA)
    subtotal(ws, R_CO_SUB, '(=) SUBTOTAL DAS COMISSÕES', R_COORD, R_MONTC)
    ws.row_dimensions[R_CO_SUB + 1].height = 8

    # ── 5 · comissões por colaborador
    titulo_secao(ws, R_CL_T, NCOL, '5 · Comissões por colaborador',
                 'consolidado automático — quem recebe o quê neste projeto')
    cab(ws, R_CL_H, [(1, 1, 'Colaborador'), (2, 2, 'Produção (R$)'), (4, 2, 'Montagem (R$)'),
                     (6, 2, 'Coordenação (R$)'), (8, 3, 'Total no projeto (R$)')])
    for i, r in enumerate(range(R_CL0, R_CLF + 1)):
        ws.row_dimensions[r].height = 17
        bloco(ws, r, 1, 1, EQUIPE[i] if i < len(EQUIPE) else None,
              f=Font(name=F, size=9.5, bold=True, color=NAVY2), bg=INPUT, al=LEFTI)
        bloco(ws, r, 2, 2, f'=IF($A{r}="","",ROUND(SUMIF({AMB_PROD_Q},$A{r},{AMB_PROD_V}),2))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 4, 2, f'=IF($A{r}="","",ROUND(SUMIF({AMB_MONT_Q},$A{r},{AMB_MONT_V}),2))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 6, 2, f'=IF($A{r}="","",IF($A{r}=$F${R_ID4},'
                           f'IF($D${R_COORD}="",0,$D${R_COORD}),0))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 8, 3, f'=IF($A{r}="","",ROUND($B{r}+$D{r}+$F{r},2))',
              f=Font(name=F, size=10, bold=True, color=NAVY), bg=CALC, al=RIGHT, nf=MOEDA)
    dv(ws, '=Listas!$A$2:$A$13', f'A{R_CL0}:A{R_CLF}')
    ws.row_dimensions[R_CL_TOT].height = 20
    bloco(ws, R_CL_TOT, 1, 1, 'TOTAL', f=F_SUB, bg=NAVY2, al=RIGHT)
    for c0, span in ((2, 2), (4, 2), (6, 2), (8, 3)):
        bloco(ws, R_CL_TOT, c0, span,
              f'=ROUND(SUM({LP[c0]}{R_CL0}:{LP[c0]}{R_CLF}),2)',
              f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=MOEDA)
    ws.row_dimensions[R_CL_TOT + 1].height = 8

    # ── 6, 7, 8 · material, terceirizados e logística
    for tit, nota, rt, rh, r0, itens, rsub, rot_sub in (
            ('6 · Material', 'custo direto de insumo comprado para este projeto',
             R_MAT_T, R_MAT_H, R_MAT0, MATERIAIS, R_MAT_SUB, '(=) SUBTOTAL DE MATERIAL'),
            ('7 · Serviços terceirizados', 'o que foi feito fora da fábrica',
             R_TER_T, R_TER_H, R_TER0, TERCEIROS, R_TER_SUB, '(=) SUBTOTAL DE TERCEIRIZADOS'),
            ('8 · Custos logísticos', 'deslocamento de gente, de material e de móvel pronto',
             R_LOG_T, R_LOG_H, R_LOG0, LOGISTICA, R_LOG_SUB, '(=) SUBTOTAL DE LOGÍSTICA')):
        titulo_secao(ws, rt, NCOL, tit, nota)
        cab(ws, rh, CAB_CUSTO)
        for i, item in enumerate(itens):
            linha_custo(ws, r0 + i, item, 'rs')
        subtotal(ws, rsub, rot_sub, r0, r0 + len(itens) - 1)
        ws.row_dimensions[rsub + 1].height = 8

    # ── 9 · retrabalho
    titulo_secao(ws, R_RB_T, NCOL, '9 · Retrabalho',
                 'o que aconteceu, por que aconteceu e quanto custou — é aqui que o '
                 'orçamento aprende')
    cab(ws, R_RB_H, [(1, 1, 'O que aconteceu'), (2, 3, 'Causa'),
                     (5, 2, 'Custo estimado (R$)'), (7, 4, 'Providência / responsável')])
    for r in range(R_RB0, R_RBF + 1):
        ws.row_dimensions[r].height = 18
        bloco(ws, r, 1, 1, None, f=F_ENT, bg=INPUT, al=LEFTI)
        bloco(ws, r, 2, 3, None, f=F_ENT, bg=INPUT, al=LEFTI)
        bloco(ws, r, 5, 2, None, f=Font(name=F, size=9.5, bold=True, color=RED),
              bg=INPUT, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 7, 4, None, f=Font(name=F, size=8.5, color=INK), bg=INPUT, al=LEFTI)
    dv(ws, '=Listas!$C$2:$C$10', f'B{R_RB0}:B{R_RBF}')
    ws.row_dimensions[R_RB_SUB].height = 20
    bloco(ws, R_RB_SUB, 1, 2, 'CONTINGÊNCIA PREVISTA NO ORÇAMENTO  →', f=F_SUB,
          bg=NAVY2, al=RIGHT)
    bloco(ws, R_RB_SUB, 3, 1, None, f=Font(name=F, size=10, bold=True, color=GOLDS),
          bg=INPUT, al=RIGHT, nf=MOEDA)
    bloco(ws, R_RB_SUB, 4, 1, f'=ROUND(SUM($E${R_RB0}:$E${R_RBF}),2)',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=MOEDA)
    bloco(ws, R_RB_SUB, 5, 2, f'=ROUND($D${R_RB_SUB}-IF($C${R_RB_SUB}="",0,$C${R_RB_SUB}),2)',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=MOEDA)
    bloco(ws, R_RB_SUB, 7, 1,
          f'=IF(OR({VENDA}="",{VENDA}=0),"",$D${R_RB_SUB}/{VENDA})',
          f=Font(name=F, size=9.5, bold=True, color=GOLDS), bg=NAVY2, al=CTR, nf=PCT1)
    bloco(ws, R_RB_SUB, 8, 3, 'orçado = a contingência que você previu · realizado = a soma acima',
          f=Font(name=F, size=8.5, color=GOLDS, i=True), bg=NAVY2, al=LEFTI)
    ws.row_dimensions[R_RB_SUB + 1].height = 8

    # ── 10 · resumo e margem
    titulo_secao(ws, R_RES_T, NCOL, '10 · Resumo e margem de contribuição')
    cab(ws, R_RES_H, [(1, 1, 'Categoria'), (2, 1, ''), (3, 1, 'Orçado (R$)'),
                      (4, 1, 'Realizado (R$)'), (5, 2, 'Desvio (R$)'), (7, 1, 'Desvio (%)'),
                      (8, 3, '% da venda realizada')])
    for i, categoria in enumerate(CATEGORIAS):
        r = R_RES0 + i
        orig = SUBLINHAS[categoria]
        ws.row_dimensions[r].height = 18
        bloco(ws, r, 1, 2, categoria, f=Font(name=F, size=9.5, color=INK), bg=WHITE, al=LEFTI)
        for col in (3, 4):
            bloco(ws, r, col, 1, f'=IF({LP[col]}{orig}="","",{LP[col]}{orig})',
                  f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 5, 2, f'=IF(OR($C{r}="",$D{r}=""),"",ROUND($D{r}-$C{r},2))',
              f=F_CALC, bg=CALC, al=RIGHT, nf=MOEDA)
        bloco(ws, r, 7, 1, f'=IF(OR($C{r}="",$C{r}=0,$D{r}=""),"",$D{r}/$C{r}-1)',
              f=Font(name=F, size=9.5, bold=True, color=NAVY2), bg=CALC, al=CTR,
              nf='+0%;-0%;0%')
        bloco(ws, r, 8, 3, f'=IF(OR($D{r}="",{VENDA}="",{VENDA}=0),"",$D{r}/{VENDA})',
              f=Font(name=F, size=9.5, color=MUTED), bg=CALC, al=CTR, nf=PCT1)
    ws.row_dimensions[R_CUSTO_TOT].height = 22
    bloco(ws, R_CUSTO_TOT, 1, 2, '(=) CUSTO TOTAL DO PROJETO', f=F_SUB, bg=NAVY2, al=RIGHT)
    for col in (3, 4):
        bloco(ws, R_CUSTO_TOT, col, 1,
              f'=ROUND(SUM({LP[col]}{R_RES0}:{LP[col]}{R_RESF}),2)',
              f=Font(name=F, size=11, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=MOEDA)
    bloco(ws, R_CUSTO_TOT, 5, 2, f'=ROUND($D${R_CUSTO_TOT}-$C${R_CUSTO_TOT},2)',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=MOEDA)
    bloco(ws, R_CUSTO_TOT, 7, 1,
          f'=IF(OR($C${R_CUSTO_TOT}="",$C${R_CUSTO_TOT}=0),"",'
          f'$D${R_CUSTO_TOT}/$C${R_CUSTO_TOT}-1)',
          f=Font(name=F, size=9.5, bold=True, color=GOLDS), bg=NAVY2, al=CTR,
          nf='+0%;-0%;0%')
    bloco(ws, R_CUSTO_TOT, 8, 3,
          f'=IF(OR({VENDA}="",{VENDA}=0),"",$D${R_CUSTO_TOT}/{VENDA})',
          f=Font(name=F, size=9.5, bold=True, color=GOLDS), bg=NAVY2, al=CTR, nf=PCT1)
    ws.row_dimensions[R_MC].height = 28
    bloco(ws, R_MC, 1, 2, '(=) MARGEM DE CONTRIBUIÇÃO',
          f=Font(name=F, size=11.5, bold=True, color=WHITE), bg=NAVY, al=RIGHT)
    bloco(ws, R_MC, 3, 1, f'=ROUND($C${R_VENDA}-$C${R_CUSTO_TOT},2)',
          f=Font(name=F, size=12, bold=True, color=GOLDS), bg=NAVY, al=RIGHT, nf=MOEDA)
    bloco(ws, R_MC, 4, 1, f'=ROUND({VENDA}-$D${R_CUSTO_TOT},2)',
          f=Font(name=F, size=12, bold=True, color=GOLDS), bg=NAVY, al=RIGHT, nf=MOEDA)
    bloco(ws, R_MC, 5, 2, f'=ROUND($D${R_MC}-$C${R_MC},2)',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY, al=RIGHT, nf=MOEDA)
    bloco(ws, R_MC, 7, 1,
          f'=IF(OR($C${R_VENDA}="",$C${R_VENDA}=0),"",$C${R_MC}/$C${R_VENDA})',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY, al=CTR, nf=PCT1)
    bloco(ws, R_MC, 8, 3, f'=IF(OR({VENDA}="",{VENDA}=0),"",$D${R_MC}/{VENDA})',
          f=Font(name=F, size=12, bold=True, color=GOLDS), bg=NAVY, al=CTR, nf=PCT1)

    # ── KPIs do topo
    ws[f'A{R_KPI_V}'] = f'=IF($D${R_VENDA}="",$C${R_VENDA},$D${R_VENDA})'
    ws[f'C{R_KPI_V}'] = f'=IF($D${R_CUSTO_TOT}=0,"",$D${R_CUSTO_TOT})'
    ws[f'E{R_KPI_V}'] = f'=IF({VENDA}="","",$D${R_MC})'
    ws[f'G{R_KPI_V}'] = f'=IF(OR({VENDA}="",{VENDA}=0),"",$D${R_MC}/{VENDA})'
    ws[f'H{R_KPI_V}'] = (f'=IF(OR($C${R_VENDA}="",$C${R_VENDA}=0),"",'
                         f'$C${R_MC}/$C${R_VENDA})')
    ws[f'I{R_KPI_V}'] = (f'=IF(OR($C${R_CUSTO_TOT}=0,$D${R_CUSTO_TOT}=0),"",'
                         f'ROUND($D${R_CUSTO_TOT}-$C${R_CUSTO_TOT},2))')

    # ── nota de rodapé
    ws.row_dimensions[R_NOTA].height = 46
    bloco(ws, R_NOTA, 1, NCOL,
          '  Como usar: preencha primeiro a coluna ORÇADO com o que o orçamento previu, e vá preenchendo a coluna '
          'REALIZADO conforme o projeto anda. O desvio de cada linha é o que mostra onde o orçamento erra. '
          'As comissões de coordenação, produção e montagem incidem sobre a RECEITA LÍQUIDA (linha destacada), '
          'não sobre o valor de venda. A soma dos ambientes precisa fechar com o valor de venda — a própria '
          'tabela avisa quando não fecha.',
          f=Font(name=F, size=8.5, color='41505D'), bg=GOLDBG, al=LEFTIW)

    # ── formatação condicional
    for rng, ref in ((f'E{R_RES0}:F{R_CUSTO_TOT}', f'$E{R_RES0}'),
                     (f'E{R_CV_SUB}:F{R_CV_SUB}', f'$E{R_CV_SUB}')):
        ws.conditional_formatting.add(rng, FormulaRule(
            formula=[f'AND({ref}<>"",{ref}>0)'], font=Font(bold=True, color=RED)))
        ws.conditional_formatting.add(rng, FormulaRule(
            formula=[f'AND({ref}<>"",{ref}<0)'], font=Font(bold=True, color=OK)))
    ws.conditional_formatting.add(f'J{R_ID4}', FormulaRule(
        formula=[f'$J${R_ID4}="No prazo"'], fill=fill(OKBG),
        font=Font(bold=True, color=OK), stopIfTrue=True))
    ws.conditional_formatting.add(f'J{R_ID4}', FormulaRule(
        formula=[f'$J${R_ID4}="Atrasado"'], fill=fill(REDBG), font=Font(bold=True, color=RED)))
    ws.conditional_formatting.add(f'A{R_KPI_V}:J{R_KPI_V}', FormulaRule(
        formula=[f'AND($G${R_KPI_V}<>"",$G${R_KPI_V}<0.25)'], fill=fill(REDBG)))
    dv(ws, '=Listas!$B$2:$B$6', f'D{R_ID2}:E{R_ID2}')
    dv(ws, '=Listas!$A$2:$A$13', f'F{R_ID4}:G{R_ID4}')
    ws.freeze_panes = f'A{R_VEN_T}'
    print_cfg(ws, f'A1:J{R_NOTA}')
    return ws


# ══════════════════════════════════════════════════════════════════════
#  ABAS
# ══════════════════════════════════════════════════════════════════════
EXEMPLO = {
    'cliente': 'Jonathan Vargas', 'num': 'P-2026-041',
    'projeto': 'Apartamento completo — 4 ambientes',
    'entrada': datetime.date(2026, 5, 12), 'prevista': datetime.date(2026, 7, 30),
    'real': datetime.date(2026, 8, 6), 'vendedor': 'Jonathan', 'coordenador': 'Deivson',
    'venda_o': 90000, 'venda_r': 90000,
    'cv': {R_IMP: 0.075, R_MAQ: 0.02, R_CVEND: 0.03, R_RTP: 0.05},
    'cv_rs': {R_TRX: (120, 148), R_PROJ: (1500, 1500)},
    'ambientes': [('Cozinha', 30000, 'Jackson', 0.03, 'Samuel', 0.02),
                  ('Suíte', 20000, 'Samuel', 0.03, 'Cezar', 0.02),
                  ('Lavanderia', 10000, 'Joelson', 0.03, 'Samuel', 0.02),
                  ('Sala', 30000, 'Deivson', 0.03, 'Jackson', 0.02)],
    'coord': 0.01, 'prod_o': 0.03, 'mont_o': 0.02,
    'material': [(14500, 15980), (900, 1120), (6800, 7450), (2200, 2200),
                 (0, 0), (3200, 3200), (1100, 1465)],
    'terceiros': [(4800, 5400), (1500, 1500), (900, 1250), (0, 0)],
    'logistica': [(250, 410), (900, 1150), (400, 620), (350, 350), (100, 185)],
    'contingencia': 1500,
    'retrabalho': [
        ('Porta da cozinha empenou depois de instalada', 'Falha de material',
         850, 'Refeita em MDF de outro lote · fornecedor notificado'),
        ('Nicho da suíte 4 cm fora da medida', 'Erro de medição',
         1200, 'Refeito · medição passa a ser conferida por 2 pessoas'),
        ('Risco no tampo da lavanderia no transporte', 'Dano no transporte',
         320, 'Polido no local · exigir manta no carreto'),
    ],
}


def preencher(ws, d):
    ws[f'A{R_ID2}'] = d['cliente']; ws[f'D{R_ID2}'] = d['num']
    ws[f'F{R_ID2}'] = d['entrada']; ws[f'H{R_ID2}'] = d['prevista']
    ws[f'J{R_ID2}'] = d['real']
    ws[f'A{R_ID4}'] = d['projeto']; ws[f'D{R_ID4}'] = d['vendedor']
    ws[f'F{R_ID4}'] = d['coordenador']
    ws[f'C{R_VENDA}'] = d['venda_o']; ws[f'D{R_VENDA}'] = d['venda_r']
    for r, pct in d['cv'].items():
        ws[f'B{r}'] = pct
    for r, (o, rr) in d['cv_rs'].items():
        ws[f'C{r}'] = o; ws[f'D{r}'] = rr
    for i, (nome, val, pq, pp, mq, mp) in enumerate(d['ambientes']):
        r = R_AMB0 + i
        ws[f'A{r}'] = nome; ws[f'C{r}'] = val
        ws[f'D{r}'] = pq; ws[f'E{r}'] = pp
        ws[f'G{r}'] = mq; ws[f'H{r}'] = mp
    ws[f'B{R_COORD}'] = d['coord']
    ws[f'B{R_PRODC}'] = d['prod_o']; ws[f'B{R_MONTC}'] = d['mont_o']
    for r0, vals in ((R_MAT0, d['material']), (R_TER0, d['terceiros']),
                     (R_LOG0, d['logistica'])):
        for i, (o, rr) in enumerate(vals):
            ws[f'C{r0 + i}'] = o or None
            ws[f'D{r0 + i}'] = rr or None
    ws[f'C{R_RB_SUB}'] = d['contingencia']
    for i, (oc, causa, custo, prov) in enumerate(d['retrabalho']):
        r = R_RB0 + i
        ws[f'A{r}'] = oc; ws[f'B{r}'] = causa; ws[f'E{r}'] = custo; ws[f'G{r}'] = prov


ficha = wb.create_sheet('Ficha Modelo')
montar_ficha(ficha)
ex = wb.create_sheet('Exemplo P-2026-041')
montar_ficha(ex)
preencher(ex, EXEMPLO)


# ══════════════════════════════════════════════════════════════════════
#  ABA · Painel Geral
# ══════════════════════════════════════════════════════════════════════
pg = wb.create_sheet('Painel Geral', 0)
pg.sheet_view.showGridLines = False
NC_PG = 17
N_SLOT = 40
C_AUX0 = 34                                   # AH — auxiliares ocultas
W_PG = [5, 22, 20, 28, 11, 11, 11, 9, 14, 14, 14, 14, 9, 9, 9, 14, 26]
r = faixa_marca(pg, NC_PG, 'PAINEL GERAL DE CUSTO POR PROJETO',
                'Cada linha puxa uma ficha · digite o nome exato da aba na coluna ABA e o '
                'resto aparece sozinho')
for i, w in enumerate(W_PG, start=1):
    pg.column_dimensions[get_column_letter(i)].width = w
pg.row_dimensions[r].height = 6
r += 1

P0, PF = r + 5, r + 4 + N_SLOT
KPI_PG = [(1, 3, 'PROJETOS', '0'), (4, 3, 'VENDIDO', MOEDA0), (7, 3, 'CUSTO TOTAL', MOEDA0),
          (10, 3, 'MARGEM DE CONTRIB.', MOEDA0), (13, 2, 'MC MÉDIA', PCT1),
          (15, 3, 'ENTREGA NO PRAZO', PCT0)]
FX_KPI = [f'=COUNTA($B${P0}:$B${PF})',
          f'=ROUND(SUM($J${P0}:$J${PF}),2)',
          f'=ROUND(SUM($K${P0}:$K${PF}),2)',
          f'=ROUND(SUM($L${P0}:$L${PF}),2)',
          f'=IF(SUM($J${P0}:$J${PF})=0,"",SUM($L${P0}:$L${PF})/SUM($J${P0}:$J${PF}))',
          f'=IF(COUNTIF($I${P0}:$I${PF},"No prazo")+COUNTIF($I${P0}:$I${PF},"Atrasado")=0,"",'
          f'COUNTIF($I${P0}:$I${PF},"No prazo")/'
          f'(COUNTIF($I${P0}:$I${PF},"No prazo")+COUNTIF($I${P0}:$I${PF},"Atrasado")))']
for (c0, span, rot, nf), fx in zip(KPI_PG, FX_KPI):
    bloco(pg, r, c0, span, rot, f=Font(name=F, size=8, bold=True, color=MUTED), bg=WHITE,
          al=CTR, bd=False)
    bloco(pg, r + 1, c0, span, fx, f=Font(name=F, size=15, bold=True, color=NAVY),
          bg=GOLDBG, al=CTR, nf=nf)
pg.row_dimensions[r].height = 14
pg.row_dimensions[r + 1].height = 32
pg.row_dimensions[r + 2].height = 8
r = titulo_secao(pg, r + 3, NC_PG, 'Projetos',
                 'digite na coluna ABA o nome exato da lâmina de cada projeto')
HDR_PG = ['#', 'Aba do projeto', 'Cliente', 'Projeto', 'Entrada', 'Prevista', 'Entregue',
          'Dias', 'Entrega', 'Venda', 'Custo total', 'MC (R$)', 'MC %', 'MC % orç.',
          'Δ p.p.', 'Desvio de custo', 'Diagnóstico']
r = cab(pg, r, [(i + 1, 1, h) for i, h in enumerate(HDR_PG)], alt=30)
assert r == P0, f'P0 esperado {P0}, obtido {r}'

def puxa(r, ref):
    return f'=IFERROR(INDIRECT("\'"&$B{r}&"\'!{ref}"),"")'


REFS = [(3, f'A{R_ID2}', None, LEFTI), (4, f'A{R_ID4}', None, LEFTI),
        (5, f'F{R_ID2}', DATA, CTR), (6, f'H{R_ID2}', DATA, CTR),
        (7, f'J{R_ID2}', DATA, CTR), (8, f'H{R_ID4}', '0', CTR),
        (9, f'J{R_ID4}', None, CTR), (10, f'A{R_KPI_V}', MOEDA0, RIGHT),
        (11, f'C{R_KPI_V}', MOEDA0, RIGHT), (12, f'E{R_KPI_V}', MOEDA0, RIGHT),
        (13, f'G{R_KPI_V}', PCT1, CTR), (14, f'H{R_KPI_V}', PCT1, CTR),
        (16, f'I{R_KPI_V}', MOEDA0, RIGHT)]

for i, r in enumerate(range(P0, PF + 1), start=1):
    pg.row_dimensions[r].height = 17
    bloco(pg, r, 1, 1, i, f=Font(name=F, size=8.5, color=MUTED), bg=CALC, al=CTR)
    bloco(pg, r, 2, 1, None, f=Font(name=F, size=9.5, bold=True, color=NAVY),
          bg=INPUT, al=LEFTI)
    for col, ref, nf, al in REFS:
        bloco(pg, r, col, 1, puxa(r, ref), f=Font(name=F, size=9.5, color=NAVY2),
              bg=CALC, al=al, nf=nf)
    bloco(pg, r, 15, 1, f'=IF(OR($M{r}="",$N{r}=""),"",ROUND(($M{r}-$N{r})*100,1))',
          f=Font(name=F, size=9.5, bold=True, color=NAVY2), bg=CALC, al=CTR,
          nf='+0.0;-0.0;0.0')
    bloco(pg, r, 17, 1,
          f'=IF($M{r}="","",IF($M{r}>=0.35,"Margem boa",'
          f'IF($M{r}>=0.25,"Margem apertada","Margem crítica")))',
          f=Font(name=F, size=8.5, bold=True, color=NAVY2), bg=CALC, al=CTR)
    for k in range(len(CATEGORIAS)):
        for j, col_f in enumerate(('C', 'D')):
            c = pg.cell(r, C_AUX0 + k * 2 + j, puxa(r, f'{col_f}{R_RES0 + k}'))
            c.number_format = MOEDA; c.font = font(8, c=MUTED)

pg.row_dimensions[PF + 1].height = 20
bloco(pg, PF + 1, 1, 9, 'TOTAL', f=F_SUB, bg=NAVY2, al=RIGHT)
for col, nf in ((10, MOEDA0), (11, MOEDA0), (12, MOEDA0)):
    bloco(pg, PF + 1, col, 1, f'=ROUND(SUM({LP[col]}{P0}:{LP[col]}{PF}),2)',
          f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=nf)
bloco(pg, PF + 1, 13, 1, f'=IF($J${PF+1}=0,"",$L${PF+1}/$J${PF+1})',
      f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=CTR, nf=PCT1)
bloco(pg, PF + 1, 14, 2, None, bg=NAVY2)
bloco(pg, PF + 1, 16, 1, f'=ROUND(SUM($P${P0}:$P${PF}),2)',
      f=Font(name=F, size=10, bold=True, color=GOLDS), bg=NAVY2, al=RIGHT, nf=MOEDA0)
bloco(pg, PF + 1, 17, 1, None, bg=NAVY2)
for txt, bg, cor in (('Margem boa', OKBG, OK), ('Margem apertada', AMBBG, AMBER),
                     ('Margem crítica', REDBG, RED)):
    pg.conditional_formatting.add(f'Q{P0}:Q{PF}', FormulaRule(
        formula=[f'$Q{P0}="{txt}"'], fill=fill(bg), font=Font(bold=True, color=cor),
        stopIfTrue=True))
for txt, bg, cor in (('No prazo', OKBG, OK), ('Atrasado', REDBG, RED),
                     ('Em produção', BLUEBG, BLUE)):
    pg.conditional_formatting.add(f'I{P0}:I{PF}', FormulaRule(
        formula=[f'$I{P0}="{txt}"'], fill=fill(bg), font=Font(bold=True, color=cor),
        stopIfTrue=True))
pg.conditional_formatting.add(f'P{P0}:P{PF}', FormulaRule(
    formula=[f'AND($P{P0}<>"",$P{P0}>0)'], font=Font(bold=True, color=RED)))
pg.conditional_formatting.add(f'P{P0}:P{PF}', FormulaRule(
    formula=[f'AND($P{P0}<>"",$P{P0}<0)'], font=Font(bold=True, color=OK)))
for c in range(C_AUX0, C_AUX0 + len(CATEGORIAS) * 2):
    pg.column_dimensions[get_column_letter(c)].hidden = True

pg[f'B{P0}'] = 'Exemplo P-2026-041'
r = PF + 3

# ── onde o orçamento erra
R_ERR_T = r
r = titulo_secao(pg, r, NC_PG, 'Onde o orçamento erra',
                 'somando todos os projetos lançados · desvio positivo = gastou mais do que previu')
R_ERR_H = r
r = cab(pg, r, [(1, 3, 'Categoria'), (4, 2, 'Orçado (R$)'), (6, 2, 'Realizado (R$)'),
                (8, 2, 'Desvio (R$)'), (10, 2, 'Desvio (%)'), (12, 2, '% da venda'),
                (14, 4, 'Leitura')], alt=26)
R_ERR0 = r
for k, categoria in enumerate(CATEGORIAS):
    co, cr = get_column_letter(C_AUX0 + k * 2), get_column_letter(C_AUX0 + k * 2 + 1)
    pg.row_dimensions[r].height = 19
    bloco(pg, r, 1, 3, categoria, f=Font(name=F, size=9.5, color=INK), bg=WHITE, al=LEFTI)
    bloco(pg, r, 4, 2, f'=ROUND(SUM({co}${P0}:{co}${PF}),2)', f=F_CALC, bg=CALC,
          al=RIGHT, nf=MOEDA0)
    bloco(pg, r, 6, 2, f'=ROUND(SUM({cr}${P0}:{cr}${PF}),2)', f=F_CALC, bg=CALC,
          al=RIGHT, nf=MOEDA0)
    bloco(pg, r, 8, 2, f'=ROUND($F{r}-$D{r},2)',
          f=Font(name=F, size=9.5, bold=True, color=NAVY2), bg=CALC, al=RIGHT, nf=MOEDA0)
    bloco(pg, r, 10, 2, f'=IF($D{r}=0,"",$F{r}/$D{r}-1)',
          f=Font(name=F, size=10, bold=True, color=NAVY2), bg=CALC, al=CTR,
          nf='+0.0%;-0.0%;0.0%')
    bloco(pg, r, 12, 2, f'=IF($J${PF+1}=0,"",$F{r}/$J${PF+1})', f=F_CALC, bg=CALC,
          al=CTR, nf=PCT1)
    bloco(pg, r, 14, 4,
          f'=IF($D{r}=0,"—",IF($J{r}>0.1,"Estourou mais de 10% — revisar a premissa",'
          f'IF($J{r}<-0.1,"Sobrou mais de 10% — orçamento pode estar gordo",'
          f'"Dentro do previsto")))',
          f=Font(name=F, size=8.5, color=INK), bg=CALC, al=LEFTI)
    r += 1
R_ERRF = r - 1
for txt, bg, cor in (('Estourou', REDBG, RED), ('Sobrou', AMBBG, AMBER),
                     ('Dentro', OKBG, OK)):
    pg.conditional_formatting.add(f'N{R_ERR0}:Q{R_ERRF}', FormulaRule(
        formula=[f'LEFT($N{R_ERR0},{len(txt)})="{txt}"'], fill=fill(bg),
        font=Font(bold=True, color=cor), stopIfTrue=True))
r += 1

# ── leituras automáticas
R_LEI_T = r
r = titulo_secao(pg, r, NC_PG, 'Leituras', 'frases montadas a partir dos números acima')
LEITURAS = [
    (f'="Carteira lançada: "&COUNTA($B${P0}:$B${PF})&" projeto(s), "&'
     f'TEXT($J${PF+1},"R$ #,##0")&" de venda e "&TEXT($L${PF+1},"R$ #,##0")&'
     f'" de margem de contribuição — "&TEXT($M${PF+1},"0.0%")&" sobre a venda."'),
    (f'="Categoria que mais estoura: "&INDEX($A${R_ERR0}:$A${R_ERRF},'
     f'MATCH(MAX($H${R_ERR0}:$H${R_ERRF}),$H${R_ERR0}:$H${R_ERRF},0))&'
     f'", com "&TEXT(MAX($H${R_ERR0}:$H${R_ERRF}),"R$ #,##0")&" acima do orçado. "&'
     f'"Categoria que mais sobra: "&INDEX($A${R_ERR0}:$A${R_ERRF},'
     f'MATCH(MIN($H${R_ERR0}:$H${R_ERRF}),$H${R_ERR0}:$H${R_ERRF},0))&"."'),
    (f'="Margem: "&COUNTIF($Q${P0}:$Q${PF},"Margem crítica")&" projeto(s) abaixo de 25%, "&'
     f'COUNTIF($Q${P0}:$Q${PF},"Margem apertada")&" entre 25% e 35% e "&'
     f'COUNTIF($Q${P0}:$Q${PF},"Margem boa")&" acima de 35%."'),
    (f'="Entrega: "&COUNTIF($I${P0}:$I${PF},"No prazo")&" no prazo, "&'
     f'COUNTIF($I${P0}:$I${PF},"Atrasado")&" atrasado(s) e "&'
     f'COUNTIF($I${P0}:$I${PF},"Em produção")&" ainda em produção. Atraso médio dos '
     f'entregues: "&IF(COUNT($H${P0}:$H${PF})=0,"—",'
     f'TEXT(AVERAGE($H${P0}:$H${PF}),"0")&" dia(s)")&"."'),
]
for txt in LEITURAS:
    pg.row_dimensions[r].height = 22
    bloco(pg, r, 1, NC_PG, txt, f=Font(name=F, size=9.5, color='2A3744'), bg=WHITE,
          al=LEFTIW, bd=False)
    r += 1
pg.row_dimensions[r].height = 8
r += 1
pg.row_dimensions[r].height = 46
bloco(pg, r, 1, NC_PG,
      '  Como alimentar: a cada projeto novo, clique com o botão direito na aba "Ficha Modelo" → Mover ou copiar → '
      'Criar uma cópia, renomeie a cópia (ex.: P-2026-042 Maria) e escreva esse mesmo nome numa linha livre da '
      'coluna ABA aqui. Todo o resto desta tela se preenche sozinho. Se o nome estiver errado ou a aba não existir, '
      'a linha simplesmente fica em branco — não quebra nada.',
      f=Font(name=F, size=8.5, color='41505D'), bg=GOLDBG, al=LEFTIW)
R_FIM_PG = r

# ── gráficos
def estilo(ch, titulo):
    ch.style = None
    ch.y_axis.majorGridlines = ChartLines()
    ch.y_axis.txPr = RichText(p=[Paragraph(pPr=ParagraphProperties(
        defRPr=CharacterProperties(sz=800, solidFill=MUTED)),
        endParaRPr=CharacterProperties(sz=800))])
    ch.x_axis.txPr = ch.y_axis.txPr
    ch.legend.position = 'b'; ch.legend.overlay = False
    ch.title = titulo

g1 = BarChart(); g1.type = 'col'
g1.add_data(Reference(pg, min_col=13, min_row=P0 - 1, max_row=PF), titles_from_data=True)
g1.set_categories(Reference(pg, min_col=3, min_row=P0, max_row=PF))
estilo(g1, 'Margem de contribuição por projeto')
g1.y_axis.numFmt = '0%'
g1.series[0].graphicalProperties.solidFill = GOLD
g1.width, g1.height = 17, 8
pg.add_chart(g1, f'S{R_ERR_T - 20}')

g2 = BarChart(); g2.type = 'bar'
g2.add_data(Reference(pg, min_col=8, min_row=R_ERR_H, max_row=R_ERRF), titles_from_data=True)
g2.set_categories(Reference(pg, min_col=1, min_row=R_ERR0, max_row=R_ERRF))
estilo(g2, 'Desvio do orçamento por categoria (R$)')
g2.y_axis.numFmt = 'R$ #,##0'
g2.series[0].graphicalProperties.solidFill = NAVY2
g2.width, g2.height = 17, 8
pg.add_chart(g2, f'S{R_ERR_T}')
pg.freeze_panes = f'C{P0}'
print_cfg(pg, f'A1:Q{R_FIM_PG}')


# ══════════════════════════════════════════════════════════════════════
#  ABA · Listas
# ══════════════════════════════════════════════════════════════════════
ls = wb.create_sheet('Listas')
ls.sheet_view.showGridLines = False
for col, titulo, vals, larg in (('A', 'Equipe', EQUIPE, 24), ('B', 'Vendedor', VENDEDORES, 22),
                                ('C', 'Causa do retrabalho', CAUSAS, 30)):
    ls.column_dimensions[col].width = larg
    c = ls[f'{col}1']; c.value = titulo
    c.font = font(9, True, WHITE); c.fill = fill(NAVY2); c.alignment = CTR
    for i, v in enumerate(vals, start=2):
        cc = ls[f'{col}{i}']; cc.value = v; cc.font = font(10); cc.border = BOTTOM2
ls['E1'] = 'Para que servem'
ls['E1'].font = font(9, True, WHITE); ls['E1'].fill = fill(NAVY2); ls['E1'].alignment = CTR
ls.column_dimensions['E'].width = 84
for i, t in enumerate([
    'Coluna A — alimenta os menus de produção, montagem, coordenação e a tabela de comissões por colaborador.',
    'Se você acrescentar alguém, inclua também na tabela "Comissões por colaborador" da ficha, senão a pessoa não aparece no consolidado.',
    'Coluna C — causas do retrabalho. É a lista mais estratégica da planilha: ela é que vai dizer se o problema está no projeto, na medição, na produção ou no fornecedor.',
], start=2):
    c = ls.cell(i, 5, t); c.font = font(9, c='41505D')
    c.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ls.row_dimensions[i].height = 30


# ══════════════════════════════════════════════════════════════════════
#  ABA · Instruções
# ══════════════════════════════════════════════════════════════════════
ins = wb.create_sheet('Instruções', 0)
ins.sheet_view.showGridLines = False
NC_IN = 6
r = faixa_marca(ins, NC_IN, 'COMO USAR ESTA PLANILHA',
                'Custo direto por projeto · orçado × realizado · eficiência do orçamento')
for i, w in enumerate([4, 34, 30, 30, 30, 12], start=1):
    ins.column_dimensions[get_column_letter(i)].width = w
r += 1


def par(row, texto, f=None, h=None, bg=None):
    ins.merge_cells(start_row=row, start_column=1, end_row=row, end_column=NC_IN)
    c = ins.cell(row, 1, '   ' + texto)
    c.font = f or font(10, c='2A3744')
    c.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    if bg:
        for k in range(1, NC_IN + 1):
            ins.cell(row, k).fill = fill(bg)
    ins.row_dimensions[row].height = h or 18
    return row + 1


BLOCOS_IN = [
    ('PARA QUE SERVE', [
        'Medir se o seu orçamento acerta. Cada linha de custo tem ORÇADO e REALIZADO lado a lado, e o desvio entre os dois é a resposta.',
        'Sem a coluna ORÇADO isto seria só um controle de gasto. Com ela, vira uma régua: você descobre que sempre erra ferragem para menos, ou que a logística custa o dobro do que você imagina.',
    ]),
    ('O PASSO A PASSO', [
        '1 · Botão direito na aba "Ficha Modelo" → Mover ou copiar → marcar "Criar uma cópia". Renomeie (ex.: P-2026-042 Maria).',
        '2 · Preencha a identificação: cliente, nº, projeto, data de entrada, entrega prevista, vendedor e coordenador.',
        '3 · Ainda na venda, lance o ORÇADO (valor da proposta) e o REALIZADO (valor fechado). A diferença entre os dois já é informação: é o quanto você deu de desconto.',
        '4 · Preencha as premissas de custo de venda (% de imposto, máquina, comissão e RT). Elas se aplicam sozinhas aos dois cenários.',
        '5 · Liste os ambientes com o valor de cada um, e para cada ambiente quem produziu e quem montou, com o % de comissão.',
        '6 · Conforme o projeto anda, lance material, terceirizados, logística e retrabalho na coluna REALIZADO.',
        '7 · Vá ao Painel Geral e escreva o nome da aba nova numa linha livre da coluna ABA.',
    ]),
    ('A CASCATA DE CÁLCULO — a ordem importa', [
        'Valor de venda  −  custos de venda (impostos, máquina, taxas, comissão de venda, projeto, RT)  =  RECEITA LÍQUIDA',
        'A receita líquida é a base das comissões de coordenação, produção e montagem. Não é o valor de venda. Isso reduz a comissão e é proposital: o marceneiro não deve ser comissionado sobre o imposto e sobre o RT do arquiteto.',
        'O RT tem uma base própria: incide sobre a venda menos impostos, máquina e taxas de transação — como você pediu.',
        'Depois da receita líquida saem, na ordem: comissões, material, terceirizados, logística e retrabalho. O que sobra é a MARGEM DE CONTRIBUIÇÃO do projeto.',
    ]),
    ('COMO FUNCIONAM AS COMISSÕES POR AMBIENTE', [
        'Cada ambiente tem um valor em reais. A planilha calcula o % que ele representa do projeto e aplica esse % sobre a receita líquida — essa é a base do ambiente.',
        'Sobre a base do ambiente incidem dois percentuais: o de quem produziu e o de quem montou. Pessoas diferentes em ambientes diferentes, cada uma com seu percentual.',
        'Exemplo: projeto de R$ 90.000 com cozinha R$ 30.000 (33,3%). Se a receita líquida for R$ 76.000, a base da cozinha é R$ 25.333. A 3% de produção, o Jackson recebe R$ 760 por aquele ambiente.',
        'A tabela "Comissões por colaborador" soma tudo automaticamente: quanto cada pessoa leva de produção, de montagem e de coordenação naquele projeto.',
        'A soma dos ambientes precisa fechar com o valor de venda. A própria linha de total avisa quando não fecha.',
    ]),
    ('RETRABALHO — a parte que mais ensina', [
        'Registre o que aconteceu, a causa (menu suspenso) e o custo estimado. Não precisa ser exato: o valor aproximado já serve.',
        'No orçamento você lança a CONTINGÊNCIA prevista. O desvio entre a contingência e o retrabalho real é o que diz se a sua provisão está no tamanho certo.',
        'Com o tempo, a coluna Causa vira o dado mais valioso da planilha: se metade dos retrabalhos é "erro de medição", o problema não é preço, é processo.',
    ]),
    ('O PAINEL GERAL', [
        'Seis indicadores no topo: nº de projetos, vendido, custo total, margem em reais, margem média e percentual de entrega no prazo.',
        'A tabela de projetos puxa cada ficha pelo nome da aba. Se o nome estiver errado, a linha fica em branco — não quebra.',
        'O bloco "Onde o orçamento erra" soma todos os projetos por categoria e mostra em qual delas você mais estoura. É o retorno direto para a Lavinia ajustar a base de orçamento.',
        'Dois gráficos: margem por projeto e desvio do orçamento por categoria.',
    ]),
    ('CUIDADOS', [
        'Não insira nem apague linhas dentro da ficha. O Painel Geral procura os números em endereços fixos — se a ficha mudar de forma, ele lê a célula errada.',
        'Para acrescentar ambientes, colaboradores ou linhas de retrabalho, use as linhas de sobra que já existem em cada bloco.',
        'A margem calculada aqui é de CONTRIBUIÇÃO: ela ainda não paga o custo fixo da empresa. Um projeto com 30% de MC não deu 30% de lucro.',
        'O custo de retrabalho é estimado por você. Ele não sai de nota fiscal — é a sua leitura do prejuízo, e vale mais registrada por alto do que não registrada.',
    ]),
]
for titulo, linhas in BLOCOS_IN:
    r = titulo_secao(ins, r, NC_IN, titulo)
    ins.row_dimensions[r].height = 4
    r += 1
    for t in linhas:
        r = par(r, t, h=30 if len(t) > 115 else (18 if len(t) < 80 else 24))
    ins.row_dimensions[r].height = 8
    r += 1
r = par(r, 'Abas:   Instruções  ·  Painel Geral  ·  Ficha Modelo (duplique esta)  ·  '
           'Exemplo P-2026-041 (preenchido)  ·  Listas',
        f=Font(name=F, size=9, bold=True, color='7A5B17'), h=26, bg=GOLDBG)
print_cfg(ins, f'A1:F{r - 1}', retrato=True)

wb.active = 0
SAIDA = '/home/user/valvicorcamentista/painel/planilhas/Valvic_Custo_por_Projeto.xlsx'
wb.save(SAIDA)
print('OK →', SAIDA)
print(f'   painel: projetos {P0}-{PF} · erros {R_ERR0}-{R_ERRF} · fim {R_FIM_PG}')
