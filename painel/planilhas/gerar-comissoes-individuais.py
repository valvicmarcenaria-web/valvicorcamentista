#!/usr/bin/env python3
"""Planilha individual de comissão — uma por colaborador, para compartilhar com ele.

    python3 gerar-comissoes-individuais.py [PASTA_DE_SAIDA]

Cada arquivo puxa sozinho da **Base · Comissões** da Custo por Projeto. O único
preenchimento de configuração é o endereço daquela planilha, em UMA célula:
`Painel!C4`. Enquanto ela estiver vazia, a planilha fica em branco e não dá erro.

Como funciona por dentro:

    Custo por Projeto · Base · Comissões
                 │  IMPORTRANGE, uma vez só, para a aba _base
                 ▼
            aba _base (oculta)
                 │  SUMIFS por pessoa e por projeto
                 ▼
            Comissões · uma linha por cliente/projeto

Por que o IMPORTRANGE aparece uma única vez: ele é lento e tem limite de uso.
Trazer a base inteira uma vez e calcular localmente é mais rápido e não estoura
cota, mesmo com quinze planilhas individuais abertas ao mesmo tempo.

A estrutura muda conforme a classe do profissional:

    vendedor, projetista, coordenação  →  Painel · Comissões
    operação                           →  Painel · Comissões · Avulsos

Operação é quem faz avulso: marceneiro, ajudante e freelancer. Vendedor e
projetista recebem pelo trabalho do projeto, e nada mais.

EDITE ESTE SCRIPT, NUNCA O ARQUIVO GERADO — a próxima geração sobrescreve.
"""
import os
import sys
import unicodedata

from openpyxl import Workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# ── quem recebe planilha, e em que classe ───────────────────────────────
# a classe define o formato: só a operação tem aba de avulsos
PESSOAS = [
    ('Lorrane', 'Projetista', 'projeto'),
    ('Lucas', 'Projetista', 'projeto'),
    ('Bruna', 'Arquiteta · projeto e programação', 'projeto'),
    ('Deivison', 'Coordenador de Produção', 'projeto'),
    ('Ronald', 'Marceneiro', 'operacao'),
    ('Samuel', 'Marceneiro Sênior', 'operacao'),
    ('Cesar', 'Marceneiro', 'operacao'),
    ('Jackson', 'Marceneiro Pleno', 'operacao'),
    ('Jhon', 'Marceneiro', 'operacao'),
    ('Joelson', 'Operador CNC e máquinas', 'operacao'),
    ('Davi', 'Marceneiro Júnior', 'operacao'),
    ('Jomar', 'Marceneiro', 'operacao'),
    ('Bruno', 'Auxiliar de Marceneiro', 'operacao'),
    ('Wallace', 'Trainee', 'operacao'),
    ('Douglas', 'Trainee', 'operacao'),
]
CLASSE_NOME = {'venda': 'Vendas', 'projeto': 'Projeto e coordenação',
               'operacao': 'Operação'}

# Endereço da Custo por Projeto no Drive, escrito DENTRO da fórmula do
# IMPORTRANGE — não numa célula de configuração.
#
# Por que não numa célula: ao colar um link do Drive numa célula, o Google o
# converte sozinho num chip de arquivo. Chip não é texto, o IMPORTRANGE não o
# lê, e a planilha fica zerada sem dar erro — o pior tipo de defeito, o que
# parece estar funcionando. Dentro da fórmula não há o que converter.
#
# Se a Custo por Projeto for recriada noutro arquivo, troque aqui e gere de novo.
FONTE = ('https://docs.google.com/spreadsheets/d/'
         '1tTJXG4w7lDvIcnd0dyr219-leOPwuURqrBk6lJIr18I/edit')

N_PROJ = 40          # slots de projeto, o mesmo teto do Painel Geral
N_AMB = 12           # ambientes por projeto, como na ficha
N_AVULSO = 30        # linhas de avulso
BASE_ABA = 'Base · Comissões'
BASE_FIM = 2 + N_PROJ * N_AMB          # última linha útil da base

NAVY, NAVY2, GOLD = '0E2038', '16314F', 'C2A05A'
GOLDSOFT, GOLDBG, CREME = 'D8BD80', 'F6EDD6', 'FBFAF7'
INK, MUTED, LINHA, ZEBRA = '1B2733', '6C7785', 'E8E3D8', 'F7F5EF'
OK, OKBG, ABERTO, ABERTOBG, CALC = '2F7D4F', 'E6F0E9', 'A8700F', 'FAEFDC', 'EAF1F8'
F = 'Calibri'
_f = Side(style='thin', color='D6DBE2')
BORDA = Border(left=_f, right=_f, top=_f, bottom=_f)
DIN, DATA, PCT = 'R$ #,##0.00', 'DD/MM/YYYY', '0.0%'
MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
STATUS = ['Em aberto', 'Pago']


def literal(itens):
    lit = '"' + ','.join(itens) + '"'
    assert len(lit) <= 255 and all(',' not in i for i in itens)
    return lit


def menu(ws, itens, intervalo):
    dv = DataValidation(type='list', formula1=literal(itens),
                        allow_blank=True, showDropDown=False)   # False = MOSTRA a setinha
    ws.add_data_validation(dv)
    dv.add(intervalo)


def faixa(ws, linha, titulo, sub, ate):
    ws.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=ate)
    c = ws.cell(linha, 1, titulo)
    c.fill = PatternFill('solid', fgColor=NAVY)
    c.font = Font(name=F, size=14, bold=True, color=GOLDSOFT)
    c.alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws.row_dimensions[linha].height = 28
    ws.merge_cells(start_row=linha + 1, start_column=1, end_row=linha + 1, end_column=ate)
    c = ws.cell(linha + 1, 1, sub)
    c.fill = PatternFill('solid', fgColor=GOLDBG)
    c.font = Font(name=F, size=9.5, italic=True, color=NAVY2)
    c.alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws.row_dimensions[linha + 1].height = 19


def cabecalho(ws, linha, cols):
    for i, (titulo, larg) in enumerate(cols, start=1):
        c = ws.cell(linha, i, titulo)
        c.fill = PatternFill('solid', fgColor=NAVY2)
        c.font = Font(name=F, size=9, bold=True, color=GOLDSOFT)
        c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        c.border = BORDA
        ws.column_dimensions[get_column_letter(i)].width = larg
    ws.row_dimensions[linha].height = 28


# ── referências à base importada, já em coluna ──────────────────────────
B = {'projeto': 'A', 'cliente': 'B', 'ambiente': 'C', 'valor': 'E',
     'prod_quem': 'F', 'prod_com': 'H', 'fabricado': 'I',
     'mont_quem': 'J', 'mont_com': 'L', 'montado': 'M',
     'proj_quem': 'N', 'proj_com': 'P', 'entrada': 'R'}


def col(nome):
    return f"_base!${B[nome]}$2:${B[nome]}${BASE_FIM}"


def aba_base(wb):
    """Traz a Base inteira uma vez só. É o único IMPORTRANGE da planilha."""
    ws = wb.create_sheet('_base')
    ws.sheet_state = 'hidden'
    # SEM IFERROR, de propósito. O botão "Permitir acesso" do Google aparece
    # junto com o #REF! que o IMPORTRANGE devolve enquanto a conexão não foi
    # autorizada. Envolver em IFERROR engole esse #REF!, a célula fica vazia e
    # não há como autorizar — foi o que travou as quinze planilhas na primeira
    # tentativa. E depois de autorizada, erro aqui é coisa que se quer ver:
    # significa que a planilha-fonte sumiu ou foi renomeada.
    ws['A1'] = f'=IMPORTRANGE("{FONTE}","{BASE_ABA}!A1:R{BASE_FIM}")'
    return ws


def aba_comissoes(wb, nome, classe):
    ws = wb.create_sheet('Comissões')
    ws.sheet_properties.tabColor = GOLD
    cols = [('Projeto', 26), ('Cliente', 24), ('Ambientes', 10),
            ('Valor produzido', 15), ('Comissão a receber', 16),
            ('Pagamento combinado', 15), ('Status', 13), ('Observação', 30)]
    faixa(ws, 1, f'COMISSÕES   ·   {nome.upper()}',
          'Uma linha por projeto. As quatro primeiras colunas vêm sozinhas da Custo por '
          'Projeto — preencha só a data combinada, o status e a observação.', len(cols))
    cabecalho(ws, 3, cols)
    ws.freeze_panes = 'C4'

    p0 = 4
    for i in range(N_PROJ):
        r = p0 + i
        # o nome do projeto é a primeira linha do bloco daquele projeto na base
        lb = 2 + i * N_AMB
        ws.cell(r, 1, f'=IFERROR(IF(_base!$A${lb}="","",_base!$A${lb}),"")')
        ws.cell(r, 2, f'=IFERROR(IF(_base!$B${lb}="","",_base!$B${lb}),"")')
        # quantos ambientes deste projeto passaram pela mão desta pessoa
        ws.cell(r, 3, f'=IF($A{r}="","",'
                      f'COUNTIFS({col("projeto")},$A{r},{col("prod_quem")},"{nome}")'
                      f'+COUNTIFS({col("projeto")},$A{r},{col("mont_quem")},"{nome}")'
                      f'+COUNTIFS({col("projeto")},$A{r},{col("proj_quem")},"{nome}"))')
        # valor de ambiente que ela tocou, em qualquer etapa
        ws.cell(r, 4, f'=IF($A{r}="","",ROUND('
                      f'SUMIFS({col("valor")},{col("projeto")},$A{r},{col("prod_quem")},"{nome}")'
                      f'+SUMIFS({col("valor")},{col("projeto")},$A{r},{col("mont_quem")},"{nome}")'
                      f'+SUMIFS({col("valor")},{col("projeto")},$A{r},{col("proj_quem")},"{nome}"),2))')
        ws.cell(r, 5, f'=IF($A{r}="","",ROUND('
                      f'SUMIFS({col("prod_com")},{col("projeto")},$A{r},{col("prod_quem")},"{nome}")'
                      f'+SUMIFS({col("mont_com")},{col("projeto")},$A{r},{col("mont_quem")},"{nome}")'
                      f'+SUMIFS({col("proj_com")},{col("projeto")},$A{r},{col("proj_quem")},"{nome}"),2))')
        for c, nf, calc in ((1, None, True), (2, None, True), (3, '0', True),
                            (4, DIN, True), (5, DIN, True),
                            (6, DATA, False), (7, None, False), (8, None, False)):
            cel = ws.cell(r, c)
            cel.border = BORDA
            cel.number_format = nf or 'General'
            if calc:
                cel.fill = PatternFill('solid', fgColor=CALC)
                cel.font = Font(name=F, size=10, color=NAVY2,
                                bold=(c == 5), italic=(c != 5))
            else:
                cel.fill = PatternFill('solid', fgColor=ZEBRA if i % 2 else 'FFFFFF')
                cel.font = Font(name=F, size=10, color=INK)
            if c in (3, 6, 7):
                cel.alignment = Alignment(horizontal='center')
    pf = p0 + N_PROJ - 1

    menu(ws, STATUS, f'G{p0}:G{pf}')
    ws.conditional_formatting.add(f'G{p0}:G{pf}', FormulaRule(
        formula=[f'$G{p0}="Pago"'], fill=PatternFill('solid', fgColor=OKBG),
        font=Font(color=OK, bold=True)))
    ws.conditional_formatting.add(f'G{p0}:G{pf}', FormulaRule(
        formula=[f'$G{p0}="Em aberto"'], fill=PatternFill('solid', fgColor=ABERTOBG),
        font=Font(color=ABERTO, bold=True)))
    # projeto que não gerou comissão para esta pessoa fica apagado
    ws.conditional_formatting.add(f'A{p0}:H{pf}', FormulaRule(
        formula=[f'AND($A{p0}<>"",$E{p0}=0)'], font=Font(color='B8BEC6')))

    r = pf + 1
    ws.cell(r, 1, 'TOTAL').font = Font(name=F, size=10, bold=True, color=GOLDSOFT)
    for c in (4, 5):
        cel = ws.cell(r, c, f'=ROUND(SUM({get_column_letter(c)}{p0}:{get_column_letter(c)}{pf}),2)')
        cel.number_format = DIN
        cel.font = Font(name=F, size=10, bold=True, color=GOLDSOFT)
    for c in range(1, len(cols) + 1):
        cel = ws.cell(r, c)
        cel.fill = PatternFill('solid', fgColor=NAVY)
        cel.border = BORDA
    ws.row_dimensions[r].height = 20
    return p0, pf


def aba_avulsos(wb, nome):
    ws = wb.create_sheet('Avulsos')
    ws.sheet_properties.tabColor = ABERTO
    cols = [('Data', 13), ('Descrição do serviço', 44), ('Valor (R$)', 15),
            ('Pagamento combinado', 16), ('Status', 13), ('Observação', 30)]
    faixa(ws, 1, f'AVULSOS   ·   {nome.upper()}',
          'O que não está preso a um projeto: serviço extra, diária, ajuste. '
          'Tudo digitado aqui.', len(cols))
    cabecalho(ws, 3, cols)
    ws.freeze_panes = 'A4'
    p0 = 4
    for i in range(N_AVULSO):
        r = p0 + i
        for c, nf in ((1, DATA), (2, None), (3, DIN), (4, DATA), (5, None), (6, None)):
            cel = ws.cell(r, c)
            cel.border = BORDA
            cel.number_format = nf or 'General'
            cel.fill = PatternFill('solid', fgColor=ZEBRA if i % 2 else 'FFFFFF')
            cel.font = Font(name=F, size=10, color=INK)
            if c in (1, 4, 5):
                cel.alignment = Alignment(horizontal='center')
    pf = p0 + N_AVULSO - 1
    menu(ws, STATUS, f'E{p0}:E{pf}')
    ws.conditional_formatting.add(f'E{p0}:E{pf}', FormulaRule(
        formula=[f'$E{p0}="Pago"'], fill=PatternFill('solid', fgColor=OKBG),
        font=Font(color=OK, bold=True)))
    r = pf + 1
    ws.cell(r, 1, 'TOTAL').font = Font(name=F, size=10, bold=True, color=GOLDSOFT)
    cel = ws.cell(r, 3, f'=ROUND(SUM($C${p0}:$C${pf}),2)')
    cel.number_format = DIN
    cel.font = Font(name=F, size=10, bold=True, color=GOLDSOFT)
    for c in range(1, len(cols) + 1):
        ws.cell(r, c).fill = PatternFill('solid', fgColor=NAVY)
        ws.cell(r, c).border = BORDA
    ws.row_dimensions[r].height = 20
    return p0, pf


def aba_painel(wb, nome, funcao, classe, com, avu):
    ws = wb.create_sheet('Painel', 0)
    ws.sheet_properties.tabColor = NAVY2
    for c, w in zip('ABCDEFG', (4, 24, 17, 17, 17, 17, 17)):
        ws.column_dimensions[c].width = w
    faixa(ws, 1, f'{nome.upper()}   ·   {funcao}',
          f'{CLASSE_NOME[classe]}  ·  tudo se calcula sozinho a partir da aba Comissões.', 7)

    ws.merge_cells(start_row=3, start_column=2, end_row=3, end_column=7)
    c = ws.cell(3, 2, '  Os números vêm sozinhos da Custo por Projeto. Na primeira abertura o '
                      'Google pede para autorizar a conexão — clique em Permitir acesso. É uma vez só.')
    c.fill = PatternFill('solid', fgColor=GOLDBG)
    c.font = Font(name=F, size=9, color=NAVY2)
    c.alignment = Alignment(horizontal='left', vertical='center')
    ws.row_dimensions[3].height = 22

    cp0, cpf = com
    kpis = [('Comissão no ano', f"=ROUND(SUM('Comissões'!$E${cp0}:$E${cpf}),2)", NAVY),
            ('Já paga', f'=ROUND(SUMIF(\'Comissões\'!$G${cp0}:$G${cpf},"Pago",'
                        f"'Comissões'!$E${cp0}:$E${cpf}),2)", OK),
            ('A receber', f"=ROUND($C$7-$E$7,2)", ABERTO)]
    if avu:
        ap0, apf = avu
        kpis.append(('Avulsos no ano', f"=ROUND(SUM('Avulsos'!$C${ap0}:$C${apf}),2)", NAVY2))
    for i, (rot, formula, cor) in enumerate(kpis):
        c0 = 3 + i * 2 if i < 3 else 3
        linha = 6 if i < 3 else 9
        if i == 3:
            c0 = 3
        r = ws.cell(linha, c0, rot)
        r.font = Font(name=F, size=9, bold=True, color=MUTED)
        ws.merge_cells(start_row=linha, start_column=c0, end_row=linha, end_column=c0 + 1)
        v = ws.cell(linha + 1, c0, formula)
        v.number_format = DIN
        v.font = Font(name=F, size=16, bold=True, color=cor)
        ws.merge_cells(start_row=linha + 1, start_column=c0, end_row=linha + 1, end_column=c0 + 1)
        ws.row_dimensions[linha + 1].height = 26

    lm = 12 if avu else 10
    ws.merge_cells(start_row=lm, start_column=2, end_row=lm, end_column=7)
    c = ws.cell(lm, 2, 'MÊS A MÊS   ·   pela data combinada de pagamento')
    c.fill = PatternFill('solid', fgColor=GOLDBG)
    c.font = Font(name=F, size=10, bold=True, color=NAVY2)
    c.alignment = Alignment(horizontal='left', vertical='center', indent=1)
    ws.row_dimensions[lm].height = 20

    cab = ['Mês', 'Comissão', 'Paga', 'A receber']
    for i, t in enumerate(cab):
        cc = ws.cell(lm + 1, 2 + i, t)
        cc.fill = PatternFill('solid', fgColor=NAVY)
        cc.font = Font(name=F, size=9, bold=True, color=GOLDSOFT)
        cc.alignment = Alignment(horizontal='center', vertical='center')
        cc.border = BORDA
    for i, mes in enumerate(MESES):
        r = lm + 2 + i
        ws.cell(r, 2, mes).font = Font(name=F, size=10, bold=True, color=NAVY2)
        ini, fim = f'DATE(YEAR(TODAY()),{i+1},1)', f'EOMONTH(DATE(YEAR(TODAY()),{i+1},1),0)'
        ws.cell(r, 3, f"=ROUND(SUMIFS('Comissões'!$E${cp0}:$E${cpf},"
                      f"'Comissões'!$F${cp0}:$F${cpf},\">=\"&{ini},"
                      f"'Comissões'!$F${cp0}:$F${cpf},\"<=\"&{fim}),2)")
        ws.cell(r, 4, f"=ROUND(SUMIFS('Comissões'!$E${cp0}:$E${cpf},"
                      f"'Comissões'!$F${cp0}:$F${cpf},\">=\"&{ini},"
                      f"'Comissões'!$F${cp0}:$F${cpf},\"<=\"&{fim},"
                      f"'Comissões'!$G${cp0}:$G${cpf},\"Pago\"),2)")
        ws.cell(r, 5, f'=ROUND($C{r}-$D{r},2)')
        for c in range(2, 6):
            cel = ws.cell(r, c)
            cel.border = BORDA
            cel.fill = PatternFill('solid', fgColor=ZEBRA if i % 2 else 'FFFFFF')
            if c >= 3:
                cel.number_format = DIN
                cel.font = Font(name=F, size=10, color=NAVY2)
    rt = lm + 14
    ws.cell(rt, 2, 'Total do ano').font = Font(name=F, size=10, bold=True, color=GOLDSOFT)
    for c in range(3, 6):
        L = get_column_letter(c)
        cel = ws.cell(rt, c, f'=ROUND(SUM({L}{lm+2}:{L}{lm+13}),2)')
        cel.number_format = DIN
        cel.font = Font(name=F, size=10, bold=True, color=GOLDSOFT)
    for c in range(2, 6):
        ws.cell(rt, c).fill = PatternFill('solid', fgColor=NAVY)
        ws.cell(rt, c).border = BORDA

    nota = ws.cell(rt + 2, 2,
                   'A comissão aparece aqui assim que o projeto é preenchido na Custo por '
                   'Projeto. A data combinada e o status são lançados pela Valvic. '
                   'Divergência se fala antes do pagamento.')
    ws.merge_cells(start_row=rt + 2, start_column=2, end_row=rt + 2, end_column=7)
    nota.font = Font(name=F, size=9, color=MUTED)
    nota.alignment = Alignment(vertical='center', wrap_text=True)
    ws.row_dimensions[rt + 2].height = 30


def sem_acento(t):
    t = unicodedata.normalize('NFKD', t)
    return ''.join(c for c in t if not unicodedata.combining(c))


def gerar(nome, funcao, classe, pasta):
    wb = Workbook()
    wb.remove(wb.active)
    com = aba_comissoes(wb, nome, classe)
    avu = aba_avulsos(wb, nome) if classe == 'operacao' else None
    aba_base(wb)
    aba_painel(wb, nome, funcao, classe, com, avu)
    wb.active = 0
    arq = os.path.join(pasta, f'Valvic_Comissao_{sem_acento(nome).replace(" ", "_")}.xlsx')
    wb.save(arq)
    return arq


if __name__ == '__main__':
    pasta = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(pasta, exist_ok=True)
    for nome, funcao, classe in PESSOAS:
        a = gerar(nome, funcao, classe, pasta)
        print(f'  {CLASSE_NOME[classe]:<24} {os.path.basename(a)}')
    print(f'\n{len(PESSOAS)} planilhas em {pasta}')
