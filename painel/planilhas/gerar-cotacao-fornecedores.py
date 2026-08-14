#!/usr/bin/env python3
"""Gera a planilha de Cotação Comparativa de Fornecedores da Valvic.

Abas: Instruções · Cotação · Pedido de Cotação (A4) · Exemplo · Mapa de Cotações · Listas

Uso:  python3 gerar-cotacao-fornecedores.py
Saída: Valvic_Cotacao_Fornecedores.xlsx
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.properties import PageSetupProperties
from openpyxl.formatting.rule import FormulaRule

# ─────────────────────────────────────────────── paleta Valvic
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
GRID    = Border(bottom=side(LINE), left=side(LINE), right=side(LINE))
BOTTOM2 = Border(bottom=side(LINE2))
CTR   = Alignment(horizontal='center', vertical='center')
CTRW  = Alignment(horizontal='center', vertical='center', wrap_text=True)
LEFT  = Alignment(horizontal='left', vertical='center')
LEFTI = Alignment(horizontal='left', vertical='center', indent=1)
LEFTW = Alignment(horizontal='left', vertical='top', wrap_text=True)
RIGHT = Alignment(horizontal='right', vertical='center', indent=1)
MOEDA, MOEDA0, PCT1, DATA, QTD = 'R$ #,##0.00', 'R$ #,##0', '0.0%', 'DD/MM/YYYY', '#,##0.##'
DIAS = '0 "dias"'

wb = openpyxl.Workbook()

# ══════════════════════════════════════════════ listas
UNIDADES = ['un', 'pç', 'cj', 'jg', 'cx', 'pct', 'm', 'm²', 'm³', 'ml', 'kg', 'L',
            'chapa', 'barra', 'rolo', 'par', 'serviço', 'verba']
CONDICOES = ['À vista', '7 dias', '14 dias', '21 dias', '28 dias', '30 dias', '30/60',
             '30/60/90', '2x sem juros', '3x sem juros', 'Parcelado no cartão',
             'Entrada + saldo', 'A combinar']
FORMAS = ['PIX à vista', 'Boleto à vista', 'Boleto a prazo', 'Cartão de crédito',
          'Transferência', 'Dinheiro', 'A combinar']
SIT_COT = ['Em cotação', 'Aguardando fornecedor', 'Em análise', 'Fechada',
           'Cancelada', 'Suspensa']
PRIORID = ['Normal', 'Urgente', 'Programada']

# ══════════════════════════════════════════════ helpers
def faixa_marca(ws, ncols, titulo, sub, linha=1):
    ws.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=ncols)
    c = ws.cell(linha, 1, 'VALVIC MARCENARIA')
    c.font = Font(name=F, size=13, bold=True, color=WHITE); c.fill = fill(NAVY)
    c.alignment = LEFTI
    ws.row_dimensions[linha].height = 26
    ws.merge_cells(start_row=linha+1, start_column=1, end_row=linha+1, end_column=ncols)
    c = ws.cell(linha+1, 1, 'Vargas Decor Ltda   ·   CNPJ 17.269.304/0001-51   ·   Belo Horizonte / MG')
    c.font = Font(name=F, size=8, color='9FB0C4'); c.fill = fill(NAVY)
    c.alignment = LEFTI
    ws.row_dimensions[linha+1].height = 15
    ws.merge_cells(start_row=linha+2, start_column=1, end_row=linha+2, end_column=ncols)
    c = ws.cell(linha+2, 1, titulo)
    c.font = Font(name=F, size=15, bold=True, color=WHITE); c.fill = fill(NAVY2)
    c.alignment = LEFTI
    ws.row_dimensions[linha+2].height = 28
    ws.merge_cells(start_row=linha+3, start_column=1, end_row=linha+3, end_column=ncols)
    c = ws.cell(linha+3, 1, sub)
    c.font = Font(name=F, size=8.5, color='7A5B17', italic=True); c.fill = fill(GOLDBG)
    c.alignment = LEFTI
    ws.row_dimensions[linha+3].height = 17
    # pintar as colunas restantes da faixa
    for lr in range(linha, linha+4):
        bg = NAVY if lr < linha+2 else (NAVY2 if lr == linha+2 else GOLDBG)
        for cc in range(1, ncols+1):
            ws.cell(lr, cc).fill = fill(bg)
    return linha + 4

def titulo_secao(ws, row, ncols, texto, nota=''):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    c = ws.cell(row, 1, ('  ' + texto.upper()) + (f'          {nota}' if nota else ''))
    c.font = Font(name=F, size=9, bold=True, color=NAVY)
    c.alignment = LEFT
    for cc in range(1, ncols+1):
        cel = ws.cell(row, cc)
        cel.fill = fill(GOLDBG); cel.border = Border(bottom=side(GOLD, 'medium'))
    ws.row_dimensions[row].height = 20
    return row + 1

def cab_tabela(ws, row, headers, widths=None, alt=32):
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row, i, h)
        c.font = Font(name=F, size=8.5, bold=True, color=WHITE); c.fill = fill(NAVY2)
        c.alignment = CTRW
        c.border = Border(left=side(NAVY2), right=side(NAVY2), bottom=side(GOLD, 'medium'))
    ws.row_dimensions[row].height = alt
    if widths:
        for i, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w
    return row + 1

def print_cfg(ws, area, retrato=True, margens=(0.4, 0.3, 0.4, 0.3)):
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

def col_lista(ws, col, titulo, valores, larg=26):
    ws.column_dimensions[col].width = larg
    c = ws[f'{col}1']; c.value = titulo
    c.font = font(9, True, WHITE); c.fill = fill(NAVY2); c.alignment = CTR
    for i, v in enumerate(valores, start=2):
        cc = ws[f'{col}{i}']; cc.value = v; cc.font = font(10); cc.border = BOTTOM2

def bloco(ws, row, col, span, valor=None, *, f=None, bg=None, al=None,
          nf=None, bd=True, h=None):
    """Escreve numa faixa mesclada de `span` colunas a partir de `col`."""
    if span > 1:
        ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col+span-1)
    c = ws.cell(row, col, valor)
    if f:  c.font = f
    if bg: c.fill = fill(bg)
    if al: c.alignment = al
    if nf: c.number_format = nf
    if bd:
        for k in range(span):
            ws.cell(row, col+k).border = GRID
            if bg: ws.cell(row, col+k).fill = fill(bg)
    return c


# ══════════════════════════════════════════════════════════════════════════
#  ABA · Cotação  (modelo — duplicável)
# ══════════════════════════════════════════════════════════════════════════
NCOL = 16
NIT  = 30
R_ID, R_IDV      = 6, 7          # rótulos / valores da identificação
R_FORN, R_VEND   = 10, 11        # nome do fornecedor / vendedor-contato
R_HEAD           = 12
R_IT0            = 13
R_ITF            = R_IT0 + NIT - 1        # 42
R_APT            = R_ITF + 2              # 44  título apuração
R_A0             = R_APT + 1              # 45  primeira linha da apuração
# offsets da apuração
AP = {k: R_A0 + i for i, k in enumerate([
    'itens', 'situacao', 'subtotal', 'pimp', 'vimp', 'frete', 'totbruto',
    'pdesc', 'avista', 'condprazo', 'pacresc', 'aprazo', 'custoprazo',
    'entrega', 'validade', 'subcompleto', 'completo'])}
R_VERT = AP['completo'] + 2               # título veredito
R_V0   = R_VERT + 1
R_NOTA = R_V0 + 5

PARES = [(5, 'E', 'F'), (7, 'G', 'H'), (9, 'I', 'J'), (11, 'K', 'L')]
NOMES_PADRAO = ['Fornecedor 1', 'Fornecedor 2', 'Fornecedor 3', 'Fornecedor 4']

HDR_COT = ['#', 'ITEM / ESPECIFICAÇÃO', 'UN.', 'QTD',
           'UNIT. (R$)', 'TOTAL (R$)', 'UNIT. (R$)', 'TOTAL (R$)',
           'UNIT. (R$)', 'TOTAL (R$)', 'UNIT. (R$)', 'TOTAL (R$)',
           'MENOR UNIT.', 'MELHOR FORNECEDOR', 'TOTAL NO MENOR', 'OBSERVAÇÃO DO ITEM']
W_COT   = [5, 38, 6.5, 8, 11.5, 12.5, 11.5, 12.5, 11.5, 12.5, 11.5, 12.5, 12, 19, 13, 26]

F_LAB   = Font(name=F, size=8, bold=True, color=MUTED)
F_VAL   = Font(name=F, size=10.5, bold=True, color=NAVY2)
F_FORN  = Font(name=F, size=11, bold=True, color=NAVY)
F_ROT   = Font(name=F, size=9, color=INK)
F_ROTB  = Font(name=F, size=9.5, bold=True, color=NAVY)
F_NUM   = Font(name=F, size=9.5, color=NAVY2)
F_NUMI  = Font(name=F, size=9.5, bold=True, color='7A5B17')
F_DEST  = Font(name=F, size=11.5, bold=True, color=WHITE)


def montar_cotacao(ws, dados=None):
    ws.sheet_view.showGridLines = False
    r = faixa_marca(ws, NCOL, 'COTAÇÃO COMPARATIVA DE FORNECEDORES',
                    'Fundo creme = você preenche   ·   fundo cinza = calculado automaticamente   '
                    '·   deixe o preço em branco quando o fornecedor NÃO tiver o item')
    assert r == R_ID - 1, f'faixa terminou em {r}, esperado {R_ID-1}'
    ws.row_dimensions[r].height = 6                      # respiro

    # ── identificação
    ident = [(1, 2, 'COTAÇÃO Nº'), (3, 4, 'DEMANDA / PROJETO'), (7, 4, 'SOLICITANTE'),
             (11, 2, 'DATA DA COTAÇÃO'), (13, 4, 'PRAZO PARA RESPOSTA')]
    for col, span, rot in ident:
        bloco(ws, R_ID, col, span, rot, f=F_LAB, bg=WHITE, al=LEFTI, bd=False)
        bloco(ws, R_IDV, col, span, None, f=F_VAL, bg=INPUT, al=LEFTI)
    ws.row_dimensions[R_ID].height = 14
    ws.row_dimensions[R_IDV].height = 22
    ws[f'K{R_IDV}'].number_format = DATA
    ws[f'M{R_IDV}'].number_format = DATA
    ws.row_dimensions[R_ID + 2].height = 6

    # ── faixa dos fornecedores
    titulo_secao(ws, R_FORN - 1, NCOL, 'Comparativo de propostas',
                 'preencha o nome dos fornecedores nas faixas creme abaixo')
    bloco(ws, R_FORN, 1, 4, 'FORNECEDOR  ▸', f=F_ROTB, bg=CALC, al=RIGHT)
    bloco(ws, R_VEND, 1, 4, 'Vendedor · contato  ▸', f=Font(name=F, size=8.5, color=MUTED),
          bg=CALC, al=RIGHT)
    for i, (c, u, t) in enumerate(PARES):
        bloco(ws, R_FORN, c, 2, NOMES_PADRAO[i], f=F_FORN, bg=INPUT, al=CTRW)
        bloco(ws, R_VEND, c, 2, None, f=Font(name=F, size=8.5, color=INK), bg=INPUT, al=CTRW)
    bloco(ws, R_FORN, 13, 4, 'MELHOR PREÇO POR ITEM', f=Font(name=F, size=9.5, bold=True, color=WHITE),
          bg=NAVY2, al=CTR)
    bloco(ws, R_VEND, 13, 4, 'calculado — mostra quem tem o menor unitário de cada linha',
          f=Font(name=F, size=8, color=MUTED, i=True), bg=CALC, al=CTRW)
    ws.row_dimensions[R_FORN].height = 26
    ws.row_dimensions[R_VEND].height = 20

    # ── tabela de itens
    cab_tabela(ws, R_HEAD, HDR_COT, W_COT)
    for r_ in range(R_IT0, R_ITF + 1):
        i = r_ - R_IT0 + 1
        ws.row_dimensions[r_].height = 18
        c = ws.cell(r_, 1, i); c.font = Font(name=F, size=8.5, color=MUTED)
        c.alignment = CTR; c.border = GRID; c.fill = fill(CALC)
        for col, al, nf, bg, fo in ((2, LEFTI, None, INPUT, font(9.5)),
                                    (3, CTR, None, INPUT, font(9.5)),
                                    (4, CTR, QTD, INPUT, font(9.5, True, NAVY2))):
            c = ws.cell(r_, col); c.alignment = al; c.fill = fill(bg)
            c.border = GRID; c.font = fo
            if nf: c.number_format = nf
        for (cu, u, t) in PARES:
            c = ws.cell(r_, cu); c.number_format = MOEDA; c.fill = fill(INPUT)
            c.border = GRID; c.font = F_NUM; c.alignment = RIGHT
            c = ws.cell(r_, cu + 1)
            c.value = f'=IF(OR($D{r_}="",{u}{r_}=""),"",ROUND($D{r_}*{u}{r_},2))'
            c.number_format = MOEDA; c.fill = fill(CALC); c.border = GRID
            c.font = F_NUM; c.alignment = RIGHT
        # menor unitário
        c = ws.cell(r_, 13)
        c.value = (f'=IF(OR($B{r_}="",COUNT(E{r_},G{r_},I{r_},K{r_})=0),"",'
                   f'MIN(E{r_},G{r_},I{r_},K{r_}))')
        c.number_format = MOEDA; c.fill = fill(CALC); c.border = GRID
        c.font = Font(name=F, size=9.5, bold=True, color=OK); c.alignment = RIGHT
        # fornecedor vencedor da linha
        c = ws.cell(r_, 14)
        c.value = (f'=IF($M{r_}="","",IF(E{r_}=$M{r_},$E${R_FORN},'
                   f'IF(G{r_}=$M{r_},$G${R_FORN},IF(I{r_}=$M{r_},$I${R_FORN},$K${R_FORN}))))')
        c.fill = fill(CALC); c.border = GRID
        c.font = Font(name=F, size=8.5, bold=True, color=NAVY2); c.alignment = CTRW
        # total no menor
        c = ws.cell(r_, 15)
        c.value = f'=IF(OR($D{r_}="",$M{r_}=""),"",ROUND($D{r_}*$M{r_},2))'
        c.number_format = MOEDA; c.fill = fill(CALC); c.border = GRID
        c.font = F_NUM; c.alignment = RIGHT
        # observação
        c = ws.cell(r_, 16); c.fill = fill(INPUT); c.border = GRID
        c.font = font(8.5); c.alignment = LEFTI

    dv(ws, "=Listas!$A$2:$A$19", f'C{R_IT0}:C{R_ITF}')

    # ── apuração por fornecedor
    ws.row_dimensions[R_ITF + 1].height = 8
    titulo_secao(ws, R_APT, NCOL, 'Apuração por fornecedor',
                 'as linhas creme são de preenchimento · as demais se calculam sozinhas')

    LINHAS = [
        ('itens',      'Itens cotados',                       'calc', None,  'Quantos dos itens da lista este fornecedor conseguiu cotar.'),
        ('situacao',   'Situação do pedido',                  'calc', None,  'COMPLETO = tem tudo. PARCIAL = vai faltar item e você precisará de um segundo fornecedor.'),
        ('subtotal',   'Subtotal dos itens',                  'calc', MOEDA, 'Soma dos itens cotados, sem imposto e sem frete.'),
        ('pimp',       '% imposto adicional (ST / IPI / DIFAL)', 'in', PCT1, 'Só o que vem POR FORA do preço. Se o preço já é o final, deixe zerado.'),
        ('vimp',       'Valor do imposto',                    'calc', MOEDA, ''),
        ('frete',      'Frete estimado (R$)',                 'in',   MOEDA, 'Coloque 0 quando o frete estiver embutido ou for por conta do fornecedor.'),
        ('totbruto',   'Total com imposto e frete',           'calc', MOEDA, 'Este é o custo cheio da proposta, antes de desconto ou acréscimo.'),
        ('pdesc',      '% desconto à vista',                  'in',   PCT1,  'Desconto que o fornecedor dá para pagamento à vista.'),
        ('avista',     'TOTAL À VISTA',                       'dest', MOEDA, ''),
        ('condprazo',  'Condição a prazo',                    'in',   None,  'Ex.: 30/60/90, 28 dias, 3x sem juros.'),
        ('pacresc',    '% acréscimo a prazo',                 'in',   PCT1,  'Juros ou acréscimo cobrado no parcelado. Se não há acréscimo, deixe zerado.'),
        ('aprazo',     'TOTAL A PRAZO',                       'dest', MOEDA, ''),
        ('custoprazo', 'Custo do prazo (R$)',                 'calc', MOEDA, 'Quanto o parcelamento custa. Compare com o que o dinheiro rende ou economiza no caixa.'),
        ('entrega',    'Prazo de entrega',                    'in',   DIAS,  'Em dias corridos a partir do pedido.'),
        ('validade',   'Validade da proposta',                'in',   DATA,  'Até quando o fornecedor garante este preço.'),
        ('subcompleto', 'Subtotal se atender 100%',           'calc', MOEDA, 'Auxiliar do veredito — fica em branco quando o fornecedor não tem o pedido inteiro.'),
        ('completo',   'Total à vista se atender 100%',       'calc', MOEDA, 'Auxiliar do veredito — é por aqui que sai o "melhor entre os completos".'),
    ]
    for chave, rotulo, tipo, nf, nota in LINHAS:
        rr = AP[chave]
        dest = tipo == 'dest'
        ws.row_dimensions[rr].height = 22 if dest else 17
        bloco(ws, rr, 1, 4, rotulo,
              f=(Font(name=F, size=9.5, bold=True, color=WHITE) if dest else
                 (Font(name=F, size=9, bold=True, color='7A5B17') if tipo == 'in' else F_ROT)),
              bg=(NAVY2 if dest else (GOLDBG if tipo == 'in' else WHITE)), al=RIGHT)
        for (cu, u, t) in PARES:
            bg = NAVY if dest else (INPUT if tipo == 'in' else CALC)
            fo = F_DEST if dest else (F_NUMI if tipo == 'in' else F_NUM)
            c = bloco(ws, rr, cu, 2, None, f=fo, bg=bg, al=CTR, nf=nf)
        bloco(ws, rr, 13, 4, nota,
              f=Font(name=F, size=8, color=(MUTED if not dest else 'D8BD80'), i=True),
              bg=(NAVY2 if dest else WHITE), al=Alignment(horizontal='left', vertical='center',
                                                          wrap_text=True, indent=1))

    NB = f'COUNTA($B${R_IT0}:$B${R_ITF})'
    for (cu, u, t) in PARES:
        NC = f'COUNT({u}${R_IT0}:{u}${R_ITF})'
        ws.cell(AP['itens'], cu).value = (
            f'=IF({NB}=0,"",{NC}&" de "&{NB})')
        ws.cell(AP['situacao'], cu).value = (
            f'=IF({NB}=0,"",IF({NC}=0,"NÃO COTOU",IF({NC}={NB},"COMPLETO",'
            f'"PARCIAL — faltam "&({NB}-{NC})&" item(ns)")))')
        ws.cell(AP['subtotal'], cu).value = (
            f'=IF({NC}=0,"",ROUND(SUM({t}${R_IT0}:{t}${R_ITF}),2))')
        ws.cell(AP['vimp'], cu).value = (
            f'=IF({u}{AP["subtotal"]}="","",ROUND({u}{AP["subtotal"]}*'
            f'IF({u}{AP["pimp"]}="",0,{u}{AP["pimp"]}),2))')
        ws.cell(AP['totbruto'], cu).value = (
            f'=IF({u}{AP["subtotal"]}="","",ROUND({u}{AP["subtotal"]}+{u}{AP["vimp"]}+'
            f'IF({u}{AP["frete"]}="",0,{u}{AP["frete"]}),2))')
        ws.cell(AP['avista'], cu).value = (
            f'=IF({u}{AP["totbruto"]}="","",ROUND({u}{AP["totbruto"]}*'
            f'(1-IF({u}{AP["pdesc"]}="",0,{u}{AP["pdesc"]})),2))')
        ws.cell(AP['aprazo'], cu).value = (
            f'=IF({u}{AP["totbruto"]}="","",ROUND({u}{AP["totbruto"]}*'
            f'(1+IF({u}{AP["pacresc"]}="",0,{u}{AP["pacresc"]})),2))')
        ws.cell(AP['custoprazo'], cu).value = (
            f'=IF(OR({u}{AP["avista"]}="",{u}{AP["aprazo"]}=""),"",'
            f'ROUND({u}{AP["aprazo"]}-{u}{AP["avista"]},2))')
        ws.cell(AP['subcompleto'], cu).value = (
            f'=IF({u}{AP["situacao"]}="COMPLETO",{u}{AP["subtotal"]},"")')
        ws.cell(AP['completo'], cu).value = (
            f'=IF({u}{AP["situacao"]}="COMPLETO",{u}{AP["avista"]},"")')
        ws.cell(AP['itens'], cu).alignment = CTR
        ws.cell(AP['situacao'], cu).font = Font(name=F, size=9, bold=True, color=NAVY2)
    for _, u, t in PARES:
        dv(ws, "=Listas!$B$2:$B$14", f'{u}{AP["condprazo"]}:{t}{AP["condprazo"]}')

    # ── veredito
    ws.row_dimensions[R_VERT - 1].height = 8
    titulo_secao(ws, R_VERT, NCOL, 'Veredito',
                 'leitura pronta para decidir — confira sempre a coluna de situação')
    AV = [f'${u}${AP["avista"]}' for _, u, _ in PARES]
    AP_ = [f'${u}${AP["aprazo"]}' for _, u, _ in PARES]
    CP = [f'${u}${AP["completo"]}' for _, u, _ in PARES]
    NM = [f'${u}${R_FORN}' for _, u, _ in PARES]
    SI = [f'${u}${AP["situacao"]}' for _, u, _ in PARES]
    CD = [f'${u}${AP["condprazo"]}' for _, u, _ in PARES]

    def escolhe(base, alvo, destino):
        """IF encadeado: qual `destino` corresponde ao menor valor de `base`."""
        return (f'IF({base[0]}={alvo},{destino[0]},IF({base[1]}={alvo},{destino[1]},'
                f'IF({base[2]}={alvo},{destino[2]},{destino[3]})))')

    VER = [
        ('Melhor preço À VISTA', AV, SI, OKBG, OK),
        ('Melhor à vista ENTRE OS COMPLETOS', CP, None, BLUEBG, BLUE),
        ('Melhor preço A PRAZO', AP_, CD, AMBBG, AMBER),
    ]
    rr = R_V0
    for rotulo, base, extra, bg, cor in VER:
        ws.row_dimensions[rr].height = 22
        bloco(ws, rr, 1, 4, rotulo, f=Font(name=F, size=9, bold=True, color=cor),
              bg=bg, al=RIGHT)
        mn = f'MIN({",".join(base)})'
        cond = f'COUNT({",".join(base)})=0'
        c = bloco(ws, rr, 5, 4, None, f=Font(name=F, size=10, bold=True, color=NAVY),
                  bg=bg, al=CTR)
        c.value = f'=IF({cond},"—",{escolhe(base, mn, NM)})'
        c = bloco(ws, rr, 9, 4, None, f=Font(name=F, size=12, bold=True, color=cor),
                  bg=bg, al=CTR, nf=MOEDA)
        c.value = f'=IF({cond},"",{mn})'
        c = bloco(ws, rr, 13, 4, None, f=Font(name=F, size=8.5, color=INK),
                  bg=bg, al=CTRW)
        if extra is not None:
            c.value = f'=IF({cond},"—",{escolhe(base, mn, extra)})'
        else:
            c.value = (f'=IF({cond},"Nenhum fornecedor tem o pedido completo — '
                       f'você vai precisar dividir a compra","Atende 100% dos itens do pedido")')
        rr += 1

    # compra fracionada
    ws.row_dimensions[rr].height = 22
    bloco(ws, rr, 1, 4, 'COMPRA FRACIONADA (item a item)',
          f=Font(name=F, size=9, bold=True, color=NAVY2), bg=CALC, al=RIGHT)
    bloco(ws, rr, 5, 4, 'melhor preço de cada linha',
          f=Font(name=F, size=9, color=MUTED, i=True), bg=CALC, al=CTR)
    SUBC = ','.join(f'${u}${AP["subcompleto"]}' for _, u, _ in PARES)
    c = bloco(ws, rr, 9, 4, None, f=Font(name=F, size=12, bold=True, color=NAVY2),
              bg=CALC, al=CTR, nf=MOEDA)
    c.value = f'=IF(SUM($O${R_IT0}:$O${R_ITF})=0,"",ROUND(SUM($O${R_IT0}:$O${R_ITF}),2))'
    SEMCOT = f'(COUNTA($B${R_IT0}:$B${R_ITF})-COUNT($M${R_IT0}:$M${R_ITF}))'
    c = bloco(ws, rr, 13, 4, None, f=Font(name=F, size=8.5, color=INK), bg=CALC, al=CTRW)
    c.value = (
        f'=IF($I{rr}="","",'
        f'IF({SEMCOT}>0,"Atenção: "&{SEMCOT}&" item(ns) sem nenhuma cotação. ","")&'
        f'IF(COUNT({SUBC})=0,"Nenhum fornecedor tem o pedido completo para servir de comparação.",'
        f'IF(MIN({SUBC})-$I{rr}>0,'
        f'"Economia de "&TEXT(MIN({SUBC})-$I{rr},"R$ #,##0.00")&'
        f'" sobre o subtotal do melhor fornecedor completo — mas some frete e imposto de cada um.",'
        f'"Sem ganho: dividir a compra sai "&TEXT($I{rr}-MIN({SUBC}),"R$ #,##0.00")&'
        f'" mais caro que o melhor fornecedor completo.")))')
    rr += 1

    # ── nota de rodapé
    ws.row_dimensions[rr].height = 8
    rr += 1
    ws.row_dimensions[rr].height = 40
    bloco(ws, rr, 1, NCOL,
          '  Como ler: subtotal e compra fracionada são SEM imposto e frete — a decisão final é sempre pelo TOTAL À VISTA ou TOTAL A PRAZO. '
          'Preço em branco na coluna de um fornecedor significa que ele não tem aquele item (a célula fica avermelhada). '
          'Antes de fechar por preço, confira a situação do pedido, o prazo de entrega e a validade da proposta.',
          f=Font(name=F, size=8.5, color='41505D'), bg=GOLDBG,
          al=Alignment(horizontal='left', vertical='center', wrap_text=True, indent=1))

    # ── formatação condicional
    for (cu, u, t) in PARES:
        rng_u = f'{u}{R_IT0}:{u}{R_ITF}'
        ws.conditional_formatting.add(rng_u, FormulaRule(
            formula=[f'AND($B{R_IT0}<>"",{u}{R_IT0}="")'], fill=fill(REDBG), stopIfTrue=True))
        ws.conditional_formatting.add(rng_u, FormulaRule(
            formula=[f'AND({u}{R_IT0}<>"",$M{R_IT0}<>"",{u}{R_IT0}=$M{R_IT0})'],
            fill=fill(OKBG), font=Font(bold=True, color=OK)))
        # situação do pedido
        rs = f'{u}{AP["situacao"]}:{t}{AP["situacao"]}'
        ws.conditional_formatting.add(rs, FormulaRule(
            formula=[f'${u}${AP["situacao"]}="COMPLETO"'], fill=fill(OKBG),
            font=Font(bold=True, color=OK), stopIfTrue=True))
        ws.conditional_formatting.add(rs, FormulaRule(
            formula=[f'LEFT(${u}${AP["situacao"]},7)="PARCIAL"'], fill=fill(AMBBG),
            font=Font(bold=True, color=AMBER), stopIfTrue=True))
        ws.conditional_formatting.add(rs, FormulaRule(
            formula=[f'${u}${AP["situacao"]}="NÃO COTOU"'], fill=fill(REDBG),
            font=Font(bold=True, color=RED)))
        # menor total à vista / a prazo
        for chave in ('avista', 'aprazo'):
            alvo = [f'${uu}${AP[chave]}' for _, uu, _ in PARES]
            ws.conditional_formatting.add(
                f'{u}{AP[chave]}:{t}{AP[chave]}',
                FormulaRule(formula=[f'AND(${u}${AP[chave]}<>"",${u}${AP[chave]}='
                                     f'MIN({",".join(alvo)}))'],
                            fill=fill(GOLD), font=Font(bold=True, color=NAVY)))

    ws.freeze_panes = f'E{R_IT0}'
    print_cfg(ws, f'A1:P{rr}', retrato=False)

    # ── dados de exemplo
    if dados:
        ws[f'A{R_IDV}'] = dados['num']
        ws[f'C{R_IDV}'] = dados['demanda']
        ws[f'G{R_IDV}'] = dados['solicitante']
        ws[f'K{R_IDV}'] = dados['data']
        ws[f'M{R_IDV}'] = dados['prazo']
        for i, (nome, vend) in enumerate(dados['fornecedores']):
            cu, u, t = PARES[i]
            ws.cell(R_FORN, cu).value = nome
            ws.cell(R_VEND, cu).value = vend
        for j, it in enumerate(dados['itens']):
            r_ = R_IT0 + j
            ws.cell(r_, 2).value = it[0]
            ws.cell(r_, 3).value = it[1]
            ws.cell(r_, 4).value = it[2]
            for i, v in enumerate(it[3]):
                if v is not None:
                    ws.cell(r_, PARES[i][0]).value = v
            if len(it) > 4 and it[4]:
                ws.cell(r_, 16).value = it[4]
        for i, ap in enumerate(dados['apuracao']):
            cu, u, t = PARES[i]
            for chave, val in ap.items():
                ws.cell(AP[chave], cu).value = val


cot = wb.active
cot.title = 'Cotação'
montar_cotacao(cot)

# ══════════════════════════════════════════════════════════════════════════
#  ABA · Pedido de Cotação (A4) — o formulário que vai para o fornecedor
# ══════════════════════════════════════════════════════════════════════════
pc = wb.create_sheet('Pedido de Cotação')
pc.sheet_view.showGridLines = False
NC_PC = 7
W_PC = [5, 46, 7, 9, 15, 16, 24]
r = faixa_marca(pc, NC_PC, 'PEDIDO DE COTAÇÃO',
                'Formulário para enviar ao fornecedor · imprima em A4 ou envie em PDF')
for i, w in enumerate(W_PC, start=1):
    pc.column_dimensions[get_column_letter(i)].width = w

pc.row_dimensions[r].height = 6
r += 1
R_ORIG = r
bloco(pc, r, 1, 3, 'Puxar os itens da aba:', f=Font(name=F, size=8.5, bold=True, color=MUTED),
      bg=WHITE, al=RIGHT, bd=False)
c = bloco(pc, r, 4, 2, 'Cotação', f=Font(name=F, size=10, bold=True, color=NAVY2),
          bg=INPUT, al=CTR)
bloco(pc, r, 6, 2, 'digite aqui o nome exato da aba de cotação',
      f=Font(name=F, size=8, color=MUTED, i=True), bg=WHITE, al=LEFTI, bd=False)
pc.row_dimensions[r].height = 20
r += 2

SRC = f'"\'"&$D${R_ORIG}&"\'!"'
def puxa(ref):
    return f'=IFERROR(INDIRECT({SRC}&"{ref}"),"")'

r = titulo_secao(pc, r, NC_PC, 'Identificação')
linhas_id = [('Cotação nº', f'A{R_IDV}'), ('Demanda / projeto', f'C{R_IDV}'),
             ('Solicitante', f'G{R_IDV}'), ('Data', f'K{R_IDV}'),
             ('Responder até', f'M{R_IDV}')]
for rot, ref in linhas_id:
    bloco(pc, r, 1, 3, rot + '  ▸', f=Font(name=F, size=9, color=MUTED), bg=WHITE, al=RIGHT)
    c = bloco(pc, r, 4, 4, puxa(ref), f=Font(name=F, size=10, bold=True, color=NAVY2),
              bg=CALC, al=LEFTI)
    if rot in ('Data', 'Responder até'):
        c.number_format = DATA
    pc.row_dimensions[r].height = 18
    r += 1

pc.row_dimensions[r].height = 8
r += 1
r = titulo_secao(pc, r, NC_PC, 'Dados do fornecedor', 'preenchimento do fornecedor')
for rot in ('Empresa', 'CNPJ', 'Vendedor', 'Telefone / WhatsApp', 'E-mail'):
    bloco(pc, r, 1, 3, rot + '  ▸', f=Font(name=F, size=9, color=MUTED), bg=WHITE, al=RIGHT)
    bloco(pc, r, 4, 4, None, f=font(10), bg=INPUT, al=LEFTI)
    pc.row_dimensions[r].height = 18
    r += 1

pc.row_dimensions[r].height = 8
r += 1
r = titulo_secao(pc, r, NC_PC, 'Itens solicitados')
r = cab_tabela(pc, r, ['#', 'ITEM / ESPECIFICAÇÃO', 'UN.', 'QTD', 'VALOR UNIT. (R$)',
                       'VALOR TOTAL (R$)', 'MARCA / OBSERVAÇÃO DO FORNECEDOR'], None, 28)
R_PC0 = r
for j in range(NIT):
    rr = R_PC0 + j
    src = R_IT0 + j
    pc.row_dimensions[rr].height = 17
    c = pc.cell(rr, 1, puxa(f'A{src}')); c.font = Font(name=F, size=8.5, color=MUTED)
    c.alignment = CTR; c.fill = fill(CALC); c.border = GRID
    for col, ref, al in ((2, f'B{src}', LEFTI), (3, f'C{src}', CTR), (4, f'D{src}', CTR)):
        c = pc.cell(rr, col, puxa(ref)); c.font = font(9.5); c.alignment = al
        c.fill = fill(CALC); c.border = GRID
        if col == 4: c.number_format = QTD
    c = pc.cell(rr, 5); c.number_format = MOEDA; c.fill = fill(INPUT)
    c.border = GRID; c.font = font(9.5); c.alignment = RIGHT
    c = pc.cell(rr, 6, f'=IF(OR($D{rr}="",$E{rr}=""),"",ROUND($D{rr}*$E{rr},2))')
    c.number_format = MOEDA; c.fill = fill(CALC); c.border = GRID
    c.font = font(9.5, c=NAVY2); c.alignment = RIGHT
    c = pc.cell(rr, 7); c.fill = fill(INPUT); c.border = GRID
    c.font = font(8.5); c.alignment = LEFTI
R_PCF = R_PC0 + NIT - 1
r = R_PCF + 1

pc.row_dimensions[r].height = 22
bloco(pc, r, 1, 5, 'SUBTOTAL DOS ITENS', f=Font(name=F, size=10, bold=True, color=NAVY),
      bg=GOLDBG, al=RIGHT)
c = bloco(pc, r, 6, 1, f'=IF(COUNT($E${R_PC0}:$E${R_PCF})=0,"",ROUND(SUM($F${R_PC0}:$F${R_PCF}),2))',
          f=Font(name=F, size=11, bold=True, color=NAVY), bg=GOLDBG, al=RIGHT, nf=MOEDA)
bloco(pc, r, 7, 1, None, bg=GOLDBG)
R_SUB_PC = r
r += 2

r = titulo_secao(pc, r, NC_PC, 'Condições comerciais', 'preenchimento do fornecedor')
COND_PC = [('% de imposto adicional (ST / IPI / DIFAL)', PCT1),
           ('Frete até a Valvic (R$)', MOEDA),
           ('Preço À VISTA — total (R$)', MOEDA),
           ('Condição a prazo oferecida', None),
           ('Preço A PRAZO — total (R$)', MOEDA),
           ('Prazo de entrega (dias corridos)', DIAS),
           ('Validade desta proposta', DATA)]
R_COND0 = r
for rot, nf in COND_PC:
    bloco(pc, r, 1, 4, rot + '  ▸', f=Font(name=F, size=9.5, color=INK), bg=WHITE, al=RIGHT)
    bloco(pc, r, 5, 3, None, f=Font(name=F, size=10, bold=True, color=NAVY2), bg=INPUT,
          al=LEFTI, nf=nf)
    pc.row_dimensions[r].height = 19
    r += 1

pc.row_dimensions[r].height = 8
r += 1
pc.row_dimensions[r].height = 46
bloco(pc, r, 1, NC_PC,
      '  Observações: (1) informe item por item — quando não trabalhar com algum item, deixe o valor em branco e escreva "não temos" na coluna de observação. '
      '(2) Se o preço já for o final, deixe o imposto adicional zerado. (3) A Valvic compara as propostas pelo valor total entregue, considerando imposto, frete e prazo. '
      '(4) Dúvidas: responda a este mesmo arquivo ou fale com o solicitante indicado acima.',
      f=Font(name=F, size=8.5, color='41505D'), bg=GOLDBG,
      al=Alignment(horizontal='left', vertical='center', wrap_text=True, indent=1))
r += 2
pc.row_dimensions[r].height = 34
bloco(pc, r, 1, 4, 'Assinatura / carimbo do fornecedor', f=Font(name=F, size=8.5, color=MUTED),
      bg=WHITE, al=CTR)
bloco(pc, r, 5, 3, 'Data', f=Font(name=F, size=8.5, color=MUTED), bg=WHITE, al=CTR)
R_PC_FIM = r
dv(pc, "=Listas!$B$2:$B$14", f'E{R_COND0 + 3}:G{R_COND0 + 3}')
print_cfg(pc, f'A1:G{R_PC_FIM}', retrato=True)

# ══════════════════════════════════════════════════════════════════════════
#  ABA · Exemplo
# ══════════════════════════════════════════════════════════════════════════
EX = {
    'num': 'COT-2026-014',
    'demanda': 'Ferragens — obra Cristiane (closet + cozinha)',
    'solicitante': 'Karla · Administrativo',
    'data': '2026-08-14',
    'prazo': '2026-08-18',
    'fornecedores': [
        ('Bigfer', 'Marcos · (31) 9xxxx-xxxx'),
        ('JR Ferragens', 'Andréia · (31) 9xxxx-xxxx'),
        ('MGV Distribuidora', 'Rafael · (31) 9xxxx-xxxx'),
        ('Ferragens Ipê', 'Sandro · (31) 9xxxx-xxxx'),
    ],
    'itens': [
        ('Corrediça telescópica 45 cm — soft close', 'par', 24, [38.90, 36.50, 41.20, 37.80], ''),
        ('Dobradiça caneco 35 mm curva — soft close', 'un', 96, [7.40, 7.90, 6.95, 7.55], ''),
        ('Puxador perfil alumínio preto 3 m', 'barra', 12, [64.00, 61.50, None, 63.20],
         'MGV não trabalha com este perfil'),
        ('Pistão a gás 100 N', 'un', 8, [22.50, 21.80, 24.00, 22.10], ''),
        ('Corrediça oculta 50 cm — push', 'par', 6, [128.00, 132.00, 125.50, None], ''),
        ('Suporte prateleira invisível 12 cm', 'un', 40, [4.20, 4.55, 3.98, 4.30], ''),
        ('Cabideiro extensível 60 cm — alumínio', 'un', 4, [96.00, 89.90, 94.50, 92.00], ''),
        ('Fecho magnético embutir', 'un', 30, [3.10, 3.40, 2.95, 3.25], ''),
    ],
    'apuracao': [
        {'pimp': 0.0,  'frete': 180.00, 'pdesc': 0.05, 'condprazo': '30/60',
         'pacresc': 0.0,  'entrega': 7,  'validade': '2026-08-25'},
        {'pimp': 0.0,  'frete': 0.00,   'pdesc': 0.03, 'condprazo': '28 dias',
         'pacresc': 0.0,  'entrega': 10, 'validade': '2026-08-22'},
        {'pimp': 0.06, 'frete': 240.00, 'pdesc': 0.07, 'condprazo': '30/60/90',
         'pacresc': 0.04, 'entrega': 5,  'validade': '2026-08-20'},
        {'pimp': 0.0,  'frete': 120.00, 'pdesc': 0.04, 'condprazo': '3x sem juros',
         'pacresc': 0.0,  'entrega': 12, 'validade': '2026-08-28'},
    ],
}
ex = wb.create_sheet('Exemplo')
montar_cotacao(ex, EX)
# datas do exemplo como data real
import datetime
ex[f'K{R_IDV}'] = datetime.date(2026, 8, 14)
ex[f'M{R_IDV}'] = datetime.date(2026, 8, 18)
for i in range(4):
    cu = PARES[i][0]
    v = EX['apuracao'][i]['validade']
    y, m, d = (int(x) for x in v.split('-'))
    ex.cell(AP['validade'], cu).value = datetime.date(y, m, d)

# ══════════════════════════════════════════════════════════════════════════
#  ABA · Mapa de Cotações
# ══════════════════════════════════════════════════════════════════════════
mp = wb.create_sheet('Mapa de Cotações')
mp.sheet_view.showGridLines = False
HDR_MP = ['Nº da cotação', 'Data', 'Demanda / projeto', 'Solicitante', 'Prioridade',
          'Fornecedores cotados', 'Fornecedor escolhido', 'Forma de pagamento',
          'Menor proposta (R$)', 'Maior proposta (R$)', 'Valor fechado (R$)',
          'Economia (R$)', 'Economia (%)', 'Situação', 'Observações']
W_MP = [15, 11, 40, 18, 12, 13, 26, 20, 15, 15, 15, 13, 11, 18, 40]
r = faixa_marca(mp, len(HDR_MP), 'MAPA DE COTAÇÕES',
                'Registro de todas as cotações · uma linha por demanda · alimente ao fechar a compra')
r += 1

# KPIs
KPI = [('Cotações registradas', '=COUNTA($A$%d:$A$%d)', '0'),
       ('Em aberto', '=COUNTIF($N$%d:$N$%d,"Em cotação")+COUNTIF($N$%d:$N$%d,"Aguardando fornecedor")+COUNTIF($N$%d:$N$%d,"Em análise")', '0'),
       ('Valor fechado no total', '=IF(COUNT($K$%d:$K$%d)=0,"",SUM($K$%d:$K$%d))', MOEDA0),
       ('Economia acumulada', '=IF(COUNT($L$%d:$L$%d)=0,"",SUM($L$%d:$L$%d))', MOEDA0),
       ('Economia média', '=IF(COUNT($M$%d:$M$%d)=0,"",AVERAGE($M$%d:$M$%d))', PCT1)]
R_KPI = r
MP0, MPF = r + 4, r + 3 + 80
for i, (rot, fx, nf) in enumerate(KPI):
    c0 = 1 + i * 3
    bloco(mp, r, c0, 3, rot, f=Font(name=F, size=8, bold=True, color=MUTED), bg=WHITE, al=CTR, bd=False)
    n = fx.count('%d') // 2
    c = bloco(mp, r + 1, c0, 3, fx % ((MP0, MPF) * n),
              f=Font(name=F, size=15, bold=True, color=NAVY), bg=GOLDBG, al=CTR, nf=nf)
mp.row_dimensions[r].height = 14
mp.row_dimensions[r + 1].height = 30
mp.row_dimensions[r + 2].height = 8
r += 3
r = cab_tabela(mp, r, HDR_MP, W_MP)
assert r == MP0, f'MP0 esperado {MP0}, obtido {r}'

for rr in range(MP0, MPF + 1):
    mp.row_dimensions[rr].height = 17
    for col in range(1, len(HDR_MP) + 1):
        c = mp.cell(rr, col); c.border = GRID; c.font = font(9.5)
        c.alignment = LEFTI; c.fill = fill(INPUT)
    for col, nf, al in ((2, DATA, CTR), (5, None, CTR), (6, '0', CTR), (9, MOEDA, RIGHT),
                        (10, MOEDA, RIGHT), (11, MOEDA, RIGHT), (14, None, CTR)):
        c = mp.cell(rr, col); c.alignment = al
        if nf: c.number_format = nf
    c = mp.cell(rr, 12, f'=IF(OR($J{rr}="",$K{rr}=""),"",ROUND($J{rr}-$K{rr},2))')
    c.number_format = MOEDA; c.fill = fill(CALC); c.alignment = RIGHT
    c.font = Font(name=F, size=9.5, bold=True, color=OK); c.border = GRID
    c = mp.cell(rr, 13, f'=IF(OR($L{rr}="",$J{rr}="",$J{rr}=0),"",$L{rr}/$J{rr})')
    c.number_format = PCT1; c.fill = fill(CALC); c.alignment = CTR
    c.font = Font(name=F, size=9.5, color=NAVY2); c.border = GRID

dv(mp, "=Listas!$D$2:$D$4", f'E{MP0}:E{MPF}')
dv(mp, "=Listas!$C$2:$C$8", f'H{MP0}:H{MPF}')
dv(mp, "=Listas!$E$2:$E$7", f'N{MP0}:N{MPF}')
mp.conditional_formatting.add(f'N{MP0}:N{MPF}', FormulaRule(
    formula=[f'$N{MP0}="Fechada"'], fill=fill(OKBG), font=Font(bold=True, color=OK)))
mp.conditional_formatting.add(f'N{MP0}:N{MPF}', FormulaRule(
    formula=[f'OR($N{MP0}="Cancelada",$N{MP0}="Suspensa")'], fill=fill(REDBG),
    font=Font(color=RED)))
mp.conditional_formatting.add(f'A{MP0}:O{MPF}', FormulaRule(
    formula=[f'AND($E{MP0}="Urgente",$N{MP0}<>"Fechada")'], fill=fill('FDF3F2')))
mp.freeze_panes = f'C{MP0}'
print_cfg(mp, f'A1:O{MPF}', retrato=False)

# ══════════════════════════════════════════════════════════════════════════
#  ABA · Listas
# ══════════════════════════════════════════════════════════════════════════
ls = wb.create_sheet('Listas')
ls.sheet_view.showGridLines = False
col_lista(ls, 'A', 'Unidade', UNIDADES, 14)
col_lista(ls, 'B', 'Condição a prazo', CONDICOES, 22)
col_lista(ls, 'C', 'Forma de pagamento', FORMAS, 22)
col_lista(ls, 'D', 'Prioridade', PRIORID, 16)
col_lista(ls, 'E', 'Situação da cotação', SIT_COT, 24)
ls['G1'] = 'Estas listas alimentam os menus suspensos'
ls['G1'].font = font(9, True, WHITE); ls['G1'].fill = fill(NAVY2); ls['G1'].alignment = CTR
ls.column_dimensions['G'].width = 70
for i, txt in enumerate([
    'Pode acrescentar itens no fim de cada coluna — o menu suspenso já cobre linhas de sobra.',
    'Não apague as colunas nem mude a ordem: as validações apontam para posições fixas.',
], start=2):
    ls.cell(i, 7, txt).font = font(9, c='41505D')

# ══════════════════════════════════════════════════════════════════════════
#  ABA · Instruções
# ══════════════════════════════════════════════════════════════════════════
ins = wb.create_sheet('Instruções', 0)
ins.sheet_view.showGridLines = False
NC_IN = 6
r = faixa_marca(ins, NC_IN, 'COMO USAR ESTA PLANILHA',
                'Cotação comparativa de fornecedores · demandas pontuais')
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

BLOCOS = [
    ('O QUE ESTA PLANILHA RESOLVE', [
        'Você tem uma demanda pontual — ferragens de uma obra, um lote de chapas, um serviço terceirizado — e precisa comparar até quatro fornecedores sem se perder em conversa de WhatsApp.',
        'A planilha faz três coisas que a conta de cabeça não faz: mostra quem tem o pedido COMPLETO, mostra o custo real depois de imposto e frete, e separa o preço À VISTA do preço A PRAZO.',
    ]),
    ('O PASSO A PASSO', [
        '1 · Clique com o botão direito na aba "Cotação" → Mover ou copiar → marque "Criar uma cópia". Renomeie a cópia (ex.: COT-2026-015 Chapas).',
        '2 · Na cópia, preencha a identificação (número, demanda, solicitante, data, prazo de resposta).',
        '3 · Liste os itens: descrição, unidade e quantidade. Uma linha por item, com especificação clara — medida, cor, acabamento, marca de referência.',
        '4 · Escreva o nome dos quatro fornecedores nas faixas creme e o vendedor com o contato logo abaixo.',
        '5 · Se quiser mandar o pedido formatado, vá na aba "Pedido de Cotação", escreva o nome da sua aba no campo do topo e imprima ou salve em PDF. Ela puxa os itens sozinha.',
        '6 · Conforme as respostas chegam, digite só o VALOR UNITÁRIO de cada fornecedor. O total sai sozinho.',
        '7 · Preencha por fornecedor: % de imposto adicional, frete, % de desconto à vista, condição e % de acréscimo a prazo, prazo de entrega e validade.',
        '8 · Leia o VEREDITO no rodapé e registre o resultado na aba "Mapa de Cotações".',
    ]),
    ('A REGRA MAIS IMPORTANTE', [
        'Se o fornecedor NÃO tem um item, deixe o preço em branco. Não escreva zero, não escreva traço.',
        'A célula fica avermelhada e a planilha passa a contar aquele fornecedor como PARCIAL — é assim que ela sabe quem entrega o pedido inteiro e quem vai te obrigar a abrir uma segunda compra.',
    ]),
    ('COMO LER O RESULTADO', [
        'Situação do pedido — COMPLETO (verde) atende tudo; PARCIAL (âmbar) mostra quantos itens faltam; NÃO COTOU (vermelho) não respondeu.',
        'Total à vista e Total a prazo — já contêm imposto, frete, desconto e acréscimo. O menor de cada linha fica com fundo dourado.',
        'Custo do prazo — quanto o parcelamento custa em reais. Compare com o alívio que aquele prazo dá no caixa antes de decidir.',
        'Melhor à vista entre os completos — este é o número que costuma valer a decisão: o mais barato que entrega tudo de uma vez.',
        'Compra fracionada — soma o melhor preço de cada item. É SEM imposto e frete e envolve várias entregas: só vale quando a diferença for grande de verdade.',
    ]),
    ('CUIDADOS', [
        'Preço não é a única variável: prazo de entrega atrasado na obra custa mais caro que qualquer desconto.',
        'Confira a validade da proposta antes de emitir o pedido — preço vencido volta diferente.',
        'Compare sempre a mesma especificação. Corrediça soft close de marcas diferentes não é o mesmo item.',
        'O % de imposto adicional é só o que vem POR FORA do preço. Se o fornecedor já informou o valor final, deixe zerado.',
    ]),
]
for titulo, linhas in BLOCOS:
    r = titulo_secao(ins, r, NC_IN, titulo)
    ins.row_dimensions[r].height = 4
    r += 1
    for t in linhas:
        r = par(r, t, h=30 if len(t) > 115 else (18 if len(t) < 80 else 24))
    ins.row_dimensions[r].height = 8
    r += 1

r = par(r, 'Abas desta planilha:   Instruções  ·  Cotação (modelo, duplique)  ·  Pedido de Cotação (formulário A4)  ·  '
           'Exemplo (preenchido)  ·  Mapa de Cotações (registro)  ·  Listas (menus)',
        f=Font(name=F, size=9, bold=True, color='7A5B17'), h=30, bg=GOLDBG)
print_cfg(ins, f'A1:F{r - 1}', retrato=True)

wb.active = 0
SAIDA = '/home/user/valvicorcamentista/painel/planilhas/Valvic_Cotacao_Fornecedores.xlsx'
wb.save(SAIDA)
print('OK →', SAIDA)
print('Cotação: itens', R_IT0, '-', R_ITF, '| apuração', R_A0, '-', AP['completo'],
      '| veredito', R_V0)
