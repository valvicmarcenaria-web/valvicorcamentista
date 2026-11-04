# -*- coding: utf-8 -*-
"""Monta a planilha de levantamento da Jéssica e Michell (projeto ICA)."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

TINTA, TIT = '1B2527', 'B0833C'
F_TIT   = Font(name='Arial', size=14, bold=True, color=TINTA)
F_SEC   = Font(name='Arial', size=10, bold=True, color='FFFFFF')
F_HD    = Font(name='Arial', size=9,  bold=True, color=TINTA)
F_N     = Font(name='Arial', size=9)
F_IN    = Font(name='Arial', size=9, color='0000FF')      # entrada
F_LINK  = Font(name='Arial', size=9, color='008000')      # vem de outra aba
F_B     = Font(name='Arial', size=9, bold=True)
F_OBS   = Font(name='Arial', size=8, italic=True, color='5B5349')
P_SEC   = PatternFill('solid', fgColor=TINTA)
P_HD    = PatternFill('solid', fgColor='EDE6DA')
P_TOT   = PatternFill('solid', fgColor='F2F5F5')
P_AT    = PatternFill('solid', fgColor='FFF4CC')          # a conferir
RS      = 'R$ #,##0.00;(R$ #,##0.00);"–"'
PCT     = '0.0%;(0.0%);"–"'
M2      = '#,##0.00'
B_FINA  = Border(bottom=Side('thin', color='DCD3C4'))

wb = openpyxl.Workbook()

def secao(ws, lin, texto, ncol=8):
    ws.cell(lin, 1, texto).font = F_SEC
    for c in range(1, ncol+1): ws.cell(lin, c).fill = P_SEC
    return lin+1

def cab(ws, lin, cols):
    for i, t in enumerate(cols, 1):
        c = ws.cell(lin, i, t); c.font = F_HD; c.fill = P_HD
        c.alignment = Alignment(wrap_text=True, vertical='center')
    return lin+1

def larguras(ws, ls):
    for i, w in enumerate(ls, 1): ws.column_dimensions[get_column_letter(i)].width = w

# ════════════════════════════════════════════════════════════════════════
# 3 · BASE DE PREÇOS  (criada primeiro: as outras abas apontam para ela)
# ════════════════════════════════════════════════════════════════════════
bp = wb.active; bp.title = 'Base de Preços'
larguras(bp, [46, 14, 44])
bp['A1'] = 'Base de preços e percentuais'; bp['A1'].font = F_TIT
bp['A2'] = ('Toda célula azul é entrada: mude aqui e o levantamento inteiro '
            'acompanha.'); bp['A2'].font = F_OBS
L = 4
BASE_ROWS = {}
def bloco(titulo, itens, fmt=RS):
    global L
    L = secao(bp, L, titulo, 3)
    L = cab(bp, L, ['Item', 'Valor', 'Origem'])
    for nome, val, fonte in itens:
        bp.cell(L, 1, nome).font = F_N
        c = bp.cell(L, 2, val); c.font = F_IN; c.number_format = fmt
        bp.cell(L, 3, fonte).font = F_OBS
        BASE_ROWS[nome] = L; L += 1
    L += 1

bloco('MDF — todos os padrões Duratex do projeto', [
 ('Chapa 18 mm', 600, 'Jonathan, 26/10/2026'),
 ('Chapa 15 mm', 500, 'base da casa'),
 ('Chapa 6 mm',  300, 'base da casa'),
 ('Fita de borda de cor, com filetagem (R$/m)', 5.50, 'base da casa'),
])
bloco('Ferragem Blum', [
 ('Dobradiça', 50, 'Jonathan, 26/10/2026'),
 ('Corrediça (por gaveta)', 250, 'Jonathan, 26/10/2026'),
 ('Báscula AVENTOS HK-XS', 250, 'Jonathan, 26/10/2026'),
 ('Puxador slim para báscula', 35, 'Jonathan, 26/10/2026'),
 ('Pulsador por porta', 100, 'Jonathan, 26/10/2026 — não usar neste projeto'),
])
bloco('Estrutura e acabamento', [
 ('Alma de aço — barra chata de 5 mm, barra de 3 m', 50,
  'Jonathan, 26/10/2026. Uma por peça acima de 30 mm'),
 ('Perfil de LED com difusor (R$/m)', 65, 'base da casa, linha Essencial'),
 ('Fonte de LED', 120, 'base da casa'),
])
bloco('Rendimento e perdas', [
 ('Aproveitamento de chapa', 0.80, 'base da casa'),
 ('Consumíveis sobre chapa e fita', 0.06, 'base da casa'),
 ('Embalagem sobre o custo direto', 0.02, 'base da casa'),
], PCT)
bloco('Cascata — sobre o preço de venda', [
 ('Nota fiscal', 0.05, 'base da casa'),
 ('Margem de erro', 0.02, 'base da casa'),
 ('Desgaste de serra e fresa', 0.005, 'base da casa'),
 ('Manutenção de máquinas', 0.005, 'base da casa'),
 ('Taxa de cartão, por parcela', 0.012, 'base da casa'),
], PCT)
bloco('Cascata — sobre o líquido (bruto menos nota e cartão)', [
 ('RT da arquiteta', 0.10, 'base da casa'),
 ('Comissão de vendedor', 0.10, 'base da casa'),
], PCT)
bloco('Comissões internas — sobre o líquido 2 (líquido menos RT e vendedor)', [
 ('Produção', 0.025, 'Base · Comissões, N.GESTÃO 2'),
 ('Montagem', 0.025, 'Base · Comissões, N.GESTÃO 2'),
 ('Projeto', 0.010, 'Base · Comissões, N.GESTÃO 2'),
 ('Coordenação', 0.010, 'Base · Comissões, N.GESTÃO 2'),
 ('Gestão de projetos', 0.005, 'Jonathan, 26/10/2026 — comissão nova'),
], PCT)
r0 = BASE_ROWS['Produção']
bp.cell(L, 1, 'Soma das comissões internas').font = F_B
c = bp.cell(L, 2, f'=SUM(B{r0}:B{r0+4})'); c.font = F_B; c.number_format = PCT
bp.cell(L, 3, 'Era 7,0% até 26/10/2026').font = F_OBS
BASE_ROWS['Soma das comissões internas'] = L; L += 2
bloco('Chapa — medidas', [
 ('Comprimento da chapa (cm)', 275, 'padrão confirmado em plano de corte'),
 ('Largura da chapa (cm)', 185, 'padrão confirmado em plano de corte'),
], '#,##0')
rc = BASE_ROWS['Comprimento da chapa (cm)']
bp.cell(L, 1, 'Área da chapa (m²)').font = F_B
c = bp.cell(L, 2, f'=B{rc}*B{rc+1}/10000'); c.font = F_B; c.number_format = M2
BASE_ROWS['Área da chapa (m²)'] = L

def bref(nome): return f"'Base de Preços'!$B${BASE_ROWS[nome]}"

# ════════════════════════════════════════════════════════════════════════
# AMBIENTES
# ════════════════════════════════════════════════════════════════════════
AMBIENTES = [
 ('01 Living',           '012–026', 8,  'Nogueira Caiena'),
 ('02 Cozinha',          '028–043', 5,  'Verde Floresta Velluto e Jequitibá Rosa'),
 ('03 Lavanderia',       '045–060', 6,  'Carvalho Malva Premium e Off White Suave'),
 ('04 Quarto',           '062–071', 6,  'Carvalho Malva Premium e Off White Suave'),
 ('05 Lavabo',           '073–077', 2,  'a definir'),
 ('06 Área Gourmet',     '079–088', 4,  'a definir'),
 ('07 Banho Gourmet',    '090–094', 2,  'a definir'),
 ('08 Home Office',      '096–104', 4,  'a definir'),
 ('09 Suíte Hóspedes',   '106–118', 8,  'a definir'),
 ('10 Banho Hóspedes',   '120–124', 2,  'a definir'),
 ('11 Cinema e Ateliê',  '127–141', 10, 'a definir'),
 ('12 Suíte Master',     '143–153', 3,  'a definir'),
 ('13 Closet Master',    '155–166', 5,  'a definir'),
 ('14 Banho Master',     '168–177', 3,  'a definir'),
 ('15 Suíte Mariana',    '179–192', 11, 'a definir'),
 ('16 Closet Mariana',   '194–201', 2,  'a definir'),
 ('17 Banho Mariana',    '203–208', 3,  'a definir'),
 ('18 Suíte 03',         '210–222', 6,  'a definir'),
 ('19 Closet 03',        '224–230', 2,  'a definir'),
 ('20 Banho 03',         '232–235', 2,  'a definir'),
]

LIVING_MOVEIS = [
 ('01', 'Sapateira com painel',
  'Painel de 300 de altura. Sapateira com puxador cava usinado na própria '
  'madeira e LED na base.', 'Larguras das frentes a confirmar no desenho'),
 ('02', 'Aparador com gaveta',
  '185 × 50, altura 45. Gaveta com puxador cava. Vão deixado para planta.', ''),
 ('03', 'Prateleira',
  '135 × 45, com iluminação.', ''),
 ('04', 'Divisória em ripas',
  'Onze ripas de 7 com vão de 10, profundidade 20, altura 300. Largura total '
  '177.', 'Cadeia de cota fecha: 11×7 + 10×10 = 177'),
 ('05', 'Jardineira com banco',
  'Conjunto de 520. Floreira de 500 × 50. Banco de 80 × 50, altura 44, com '
  'LED inferior.', 'O projeto pede reforço estrutural na parede'),
 ('06', 'Divisória com cristaleira',
  'Divisória de 360 × 300. Cristaleira de 100 × 260 com portas de giro em '
  'vidro reflecta champagne e prateleiras internas iluminadas. Rack com '
  'gavetas e base recuada com LED.', 'Contagem de gavetas e portas a fechar'),
 ('07', 'Estante',
  '300 × 215, profundidade 40. Quatro nichos de 48 com fundo ripado. Gavetas '
  'com puxador cava.', 'Contagem de gavetas a fechar'),
 ('08', 'Painel com porta mimetizada',
  'Painel de 400 × 300. Porta mimetizada de giro de 90 × 210, com puxador '
  'cava.', ''),
]
LIVING_NAO = [
 ('Parede com pedra Atacama Branca', 'Revestimento de parede — não é marcenaria'),
 ('Porta ripada', 'Consta na elevação 02; confirmar se entra no nosso escopo'),
 ('Tinta Decora Efeitos Especiais Velvet', 'Pintura — não é marcenaria'),
 ('Mobiliário solto', 'Sofá Tiffany, Poltrona Serfa, Mesa Cambuí, Cadeira '
  'Ditta, luminárias, tapete, cortinas e espelhos decorativos'),
]

def aba_ambiente(nome, paginas, ndet, padrao, moveis=None, nao=None):
    # ⛔ As linhas de detalhe só recebem fórmula nas abas já levantadas. Nas
    #   outras elas ficam vazias: as somas continuam certas (vazio soma zero),
    #   a numeração das linhas não muda, e o arquivo cai pela metade.
    FORM = moveis is not None
    ws = wb.create_sheet(nome)
    larguras(ws, [30, 30, 13, 13, 8, 9, 12, 46])
    ws['A1'] = nome[3:]; ws['A1'].font = F_TIT
    ws['A2'] = (f'Projeto ICA · páginas {paginas} · {ndet} detalhamentos · '
                f'MDF {padrao}')
    ws['A2'].font = F_OBS
    l = 4
    l = secao(ws, l, 'MÓVEIS DO AMBIENTE')
    l = cab(ws, l, ['DET', 'Móvel', 'O que o projeto especifica', '', '', '',
                    '', 'Conferência'])
    lin_mov = l
    N_MOVEIS = 12          # ⛔ fixo em todas as abas: o Resumo soma por linha
    if moveis:
        for det, mv, esp, conf in moveis:
            ws.cell(l, 1, det).font = F_N
            ws.cell(l, 2, mv).font = F_B
            ws.cell(l, 3, esp).font = F_N
            ws.cell(l, 3).alignment = Alignment(wrap_text=True, vertical='top')
            ws.merge_cells(start_row=l, start_column=3, end_row=l, end_column=7)
            c = ws.cell(l, 8, conf); c.font = F_OBS
            c.alignment = Alignment(wrap_text=True, vertical='top')
            if conf: c.fill = P_AT
            ws.row_dimensions[l].height = 30
            l += 1
    else:
        c = ws.cell(l, 1, 'A levantar — páginas ainda não lidas')
        c.font = F_OBS; c.fill = P_AT; l += 1
    l = lin_mov + N_MOVEIS          # ⛔ sempre o mesmo ponto de saída
    l += 1

    ini = {}
    def tabela(titulo, colunas, nlinhas=12):
        nonlocal l
        l = secao(ws, l, titulo)
        l = cab(ws, l, colunas)
        ini[titulo] = l
        l += nlinhas
        return l

    tabela('CHAPA', ['Peça', 'Móvel', 'Comprimento (cm)', 'Largura (cm)',
                     'Qtd', 'Esp (mm)', 'Área (m²)', 'Observação'], 14)
    r = ini['CHAPA']
    for i in range(r, r+14):
        c = ws.cell(i, 7, f'=IF(C{i}="","",C{i}*D{i}*E{i}/10000)' if FORM else None)
        c.number_format = M2; c.font = F_N
        pass  # sem bordas por linha: cada uma vira um registro de estilo
    ws.cell(l, 1, 'Área total (m²)').font = F_B
    c = ws.cell(l, 7, f'=SUM(G{r}:G{r+13})'); c.font = F_B; c.number_format = M2
    AREA = f'$G${l}'; l += 1
    ws.cell(l, 1, 'Chapas, com aproveitamento').font = F_B
    c = ws.cell(l, 7, f'=IF({AREA}=0,0,ROUNDUP({AREA}/({bref("Área da chapa (m²)")}'
                      f'*{bref("Aproveitamento de chapa")}),0))')
    c.font = F_B; c.number_format = '#,##0'
    CHAPAS = f'$G${l}'; l += 1
    ws.cell(l, 1, 'Custo de chapa').font = F_B
    c = ws.cell(l, 7, f'={CHAPAS}*{bref("Chapa 18 mm")}')
    c.font = F_B; c.number_format = RS; c.fill = P_TOT
    CUSTO_CHAPA = f'$G${l}'; l += 2

    tabela('FITA DE BORDA', ['Onde', 'Móvel', 'Metros', '', '', '', 'Custo',
                             'Observação'], 6)
    r = ini['FITA DE BORDA']
    for i in range(r, r+6):
        c = ws.cell(i, 7, f'=IF(C{i}="","",C{i}*{bref("Fita de borda de cor, com filetagem (R$/m)")})' if FORM else None)
        c.number_format = RS; c.font = F_N
        pass  # sem bordas por linha: cada uma vira um registro de estilo
    ws.cell(l, 1, 'Custo de fita').font = F_B
    c = ws.cell(l, 7, f'=SUM(G{r}:G{r+5})'); c.font = F_B
    c.number_format = RS; c.fill = P_TOT
    CUSTO_FITA = f'$G${l}'; l += 2

    tabela('FERRAGEM BLUM', ['Item', 'Móvel', 'Qtd', 'R$ unitário', '', '',
                             'Custo', 'Observação'], 10)
    r = ini['FERRAGEM BLUM']
    for i in range(r, r+10):
        c = ws.cell(i, 7, f'=IF(C{i}="","",C{i}*D{i})' if FORM else None)
        c.number_format = RS; c.font = F_N
        ws.cell(i, 4).number_format = RS
        pass  # sem bordas por linha: cada uma vira um registro de estilo
    ws.cell(l, 1, 'Custo de ferragem').font = F_B
    c = ws.cell(l, 7, f'=SUM(G{r}:G{r+9})'); c.font = F_B
    c.number_format = RS; c.fill = P_TOT
    CUSTO_FER = f'$G${l}'; l += 2

    tabela('ALMA DE AÇO — peças acima de 30 mm', ['Peça', 'Móvel',
            'Qtd de peças', 'Altura (cm)', 'Barras', '', 'Custo',
            'Observação'], 5)
    r = ini['ALMA DE AÇO — peças acima de 30 mm']
    for i in range(r, r+5):
        c = ws.cell(i, 5, f'=IF(C{i}="","",ROUNDUP(C{i}*D{i}/300,0))' if FORM else None)
        c.number_format = '#,##0'; c.font = F_N
        c = ws.cell(i, 7, f'=IF(E{i}="","",E{i}*{bref("Alma de aço — barra chata de 5 mm, barra de 3 m")})' if FORM else None)
        c.number_format = RS; c.font = F_N
        pass  # sem bordas por linha: cada uma vira um registro de estilo
    ws.cell(l, 1, 'Custo de alma de aço').font = F_B
    c = ws.cell(l, 7, f'=SUM(G{r}:G{r+4})'); c.font = F_B
    c.number_format = RS; c.fill = P_TOT
    CUSTO_ALMA = f'$G${l}'; l += 2

    tabela('ILUMINAÇÃO E TERCEIRIZADOS', ['Item', 'Móvel', 'Qtd', 'R$ unitário',
            '', '', 'Custo', 'Observação'], 6)
    r = ini['ILUMINAÇÃO E TERCEIRIZADOS']
    for i in range(r, r+6):
        c = ws.cell(i, 7, f'=IF(C{i}="","",C{i}*D{i})' if FORM else None)
        c.number_format = RS; c.font = F_N
        ws.cell(i, 4).number_format = RS
        pass  # sem bordas por linha: cada uma vira um registro de estilo
    ws.cell(l, 1, 'Custo de iluminação e terceirizados').font = F_B
    c = ws.cell(l, 7, f'=SUM(G{r}:G{r+5})'); c.font = F_B
    c.number_format = RS; c.fill = P_TOT
    CUSTO_TER = f'$G${l}'; l += 2

    l = secao(ws, l, 'NÃO É MARCENARIA — consta na prancha, fora do nosso escopo')
    l = cab(ws, l, ['Item', 'Por quê', '', '', '', '', '', ''])
    lin_nao = l
    for it, pq in (nao or []):
        ws.cell(l, 1, it).font = F_N
        c = ws.cell(l, 2, pq); c.font = F_OBS
        ws.merge_cells(start_row=l, start_column=2, end_row=l, end_column=8)
        l += 1
    l = lin_nao + 6          # ⛔ fixo: mantém o custo direto na mesma linha
    l += 1

    l = secao(ws, l, 'CUSTO DIRETO DO AMBIENTE')
    for rot, ref in [('Chapa', CUSTO_CHAPA), ('Fita', CUSTO_FITA),
                     ('Ferragem Blum', CUSTO_FER), ('Alma de aço', CUSTO_ALMA),
                     ('Iluminação e terceirizados', CUSTO_TER)]:
        ws.cell(l, 1, rot).font = F_N
        c = ws.cell(l, 7, f'={ref}'); c.number_format = RS; c.font = F_N
        l += 1
    ws.cell(l, 1, 'Consumíveis sobre chapa e fita').font = F_N
    c = ws.cell(l, 7, f'=({CUSTO_CHAPA}+{CUSTO_FITA})*{bref("Consumíveis sobre chapa e fita")}')
    c.number_format = RS; c.font = F_N; CONS = f'$G${l}'; l += 1
    ws.cell(l, 1, 'Subtotal').font = F_B
    c = ws.cell(l, 7, f'={CUSTO_CHAPA}+{CUSTO_FITA}+{CUSTO_FER}+{CUSTO_ALMA}'
                      f'+{CUSTO_TER}+{CONS}')
    c.font = F_B; c.number_format = RS; SUB = f'$G${l}'; l += 1
    ws.cell(l, 1, 'Embalagem').font = F_N
    c = ws.cell(l, 7, f'={SUB}*{bref("Embalagem sobre o custo direto")}')
    c.number_format = RS; c.font = F_N; EMB = f'$G${l}'; l += 1
    ws.cell(l, 1, 'CUSTO DIRETO').font = Font(name='Arial', size=11, bold=True,
                                              color=TINTA)
    c = ws.cell(l, 7, f'={SUB}+{EMB}')
    c.font = Font(name='Arial', size=11, bold=True, color=TINTA)
    c.number_format = RS; c.fill = P_TOT
    return ws, dict(cd=l, chapa=int(CUSTO_CHAPA.split('$')[2]),
                    fita=int(CUSTO_FITA.split('$')[2]),
                    fer=int(CUSTO_FER.split('$')[2]),
                    alma=int(CUSTO_ALMA.split('$')[2]),
                    ter=int(CUSTO_TER.split('$')[2]),
                    area=int(AREA.split('$')[2]),
                    chapas=int(CHAPAS.split('$')[2]))

# ⛔ Só o ambiente já levantado ganha aba. Os outros entram no Resumo como
#   linha de escopo e ganham a sua aba quando o levantamento chegar neles —
#   aba vazia não é levantamento, é peso de arquivo.
COM_ABA = {'01 Living'}
CD_REF = {}
for nome, pags, nd, pad in AMBIENTES:
    if nome not in COM_ABA: continue
    mv = LIVING_MOVEIS if nome == '01 Living' else None
    na = LIVING_NAO    if nome == '01 Living' else None
    _, LIN = aba_ambiente(nome, pags, nd, pad, mv, na)
    CD_REF[nome] = LIN

# ⭐ o Living, preenchido com o que o desenho já deu
lv = wb['01 Living']
r = CD_REF['01 Living']['area'] - 14   # primeira linha da tabela CHAPA
DADOS = [
 ('Ripa do brise', 'DET 04 Divisória', 7, 300, 11, 18, 'Vão de 10 entre ripas'),
 ('Travessa da divisória', 'DET 04 Divisória', 177, 20, 2, 18, ''),
 ('Tampo do aparador', 'DET 02 Aparador', 185, 50, 1, 18, ''),
 ('Prateleira', 'DET 03 Prateleira', 135, 45, 1, 18, 'Com iluminação'),
 ('Lateral da estante', 'DET 07 Estante', 40, 215, 2, 18, ''),
 ('Prateleira da estante', 'DET 07 Estante', 300, 40, 4, 18, 'Quatro nichos de 48'),
 ('Painel da porta mimetizada', 'DET 08 Painel', 400, 300, 1, 18, ''),
 ('Folha da porta mimetizada', 'DET 08 Painel', 90, 210, 1, 18, ''),
 ('Floreira', 'DET 05 Jardineira', 500, 50, 1, 18, ''),
 ('Assento do banco', 'DET 05 Jardineira', 80, 50, 1, 18, 'Com LED inferior'),
]
for i, (p, m, c_, l_, q, e, o) in enumerate(DADOS):
    lv.cell(r+i, 1, p).font = F_N
    lv.cell(r+i, 2, m).font = F_N
    for col, val in ((3, c_), (4, l_), (5, q), (6, e)):
        cl = lv.cell(r+i, col, val); cl.font = F_IN; cl.number_format = '#,##0'
    lv.cell(r+i, 8, o).font = F_OBS
lv.cell(r-2, 8, 'Medidas lidas dos detalhamentos. Levantamento parcial — '
                'faltam as peças de caixaria.').font = F_OBS

# alma de aço do Living
ra = None
for row in lv.iter_rows(min_col=1, max_col=1):
    if row[0].value == 'Peça' and lv.cell(row[0].row-1, 1).value and \
       'ALMA' in str(lv.cell(row[0].row-1, 1).value): ra = row[0].row+1
if ra:
    lv.cell(ra, 1, 'Ripa do brise').font = F_N
    lv.cell(ra, 2, 'DET 04 Divisória').font = F_N
    for col, val in ((3, 11), (4, 300)):
        cl = lv.cell(ra, col, val); cl.font = F_IN; cl.number_format = '#,##0'
    lv.cell(ra, 8, 'Ripa de 7 cm: passa de 30 mm, logo leva alma').font = F_OBS

wb.save('/tmp/claude-0/-home-user-valvicorcamentista/7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/planilha.xlsx')
import json, pathlib
pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/cdref.json').write_text(json.dumps(CD_REF))
print('abas:', len(wb.sheetnames)); print(wb.sheetnames)

# ════════════════════════════════════════════════════════════════════════
# 1 · RESUMO GERAL   |   2 · CUSTOS FINANCEIROS E OPERACIONAIS
# ════════════════════════════════════════════════════════════════════════
LIN = CD_REF['01 Living']          # as linhas são iguais em todas as abas
def ref(aba, campo): return f"'{aba}'!$G${LIN[campo]}"

rg = wb.create_sheet('Resumo Geral')
larguras(rg, [24, 11, 7, 12, 9, 14, 12, 14, 12, 14, 16, 9, 24])
rg['A1'] = 'Jéssica e Michell — levantamento de quantitativo'
rg['A1'].font = Font(name='Arial', size=16, bold=True, color=TINTA)
rg['A2'] = ('Projeto ICA · Iara Cezar Arquitetura e Interiores · executivo '
            '10/2026 · 235 páginas · 20 ambientes · 94 detalhamentos')
rg['A2'].font = F_OBS
rg['A3'] = ('Cada ambiente tem a sua aba. Os números aqui são somas das abas, '
            'não valores digitados.')
rg['A3'].font = F_OBS
l = 5
l = secao(rg, l, 'LEVANTAMENTO POR AMBIENTE', 13)
l = cab(rg, l, ['Ambiente', 'Páginas', 'DET', 'Área de chapa (m²)', 'Chapas',
                'Chapa', 'Fita', 'Ferragem Blum', 'Alma de aço',
                'Terceirizados', 'Custo direto', '% do total', 'Situação'])
r0 = l
for nome, pags, nd, _pad in AMBIENTES:
    rg.cell(l, 1, nome[3:]).font = F_N
    rg.cell(l, 2, pags).font = F_OBS
    rg.cell(l, 3, nd).font = F_N
    for col, campo, fmt in ((4, 'area', M2), (5, 'chapas', '#,##0'),
                            (6, 'chapa', RS), (7, 'fita', RS),
                            (8, 'fer', RS), (9, 'alma', RS),
                            (10, 'ter', RS), (11, 'cd', RS)):
        tem = nome in COM_ABA
        c = rg.cell(l, col, f"={ref(nome, campo)}" if tem else None)
        c.number_format = fmt; c.font = F_LINK if tem else F_N
    c = rg.cell(l, 12, f'=IF($K${r0+len(AMBIENTES)}=0,0,K{l}/$K${r0+len(AMBIENTES)})')
    c.number_format = PCT; c.font = F_N
    c = rg.cell(l, 13, 'Levantado' if nome in COM_ABA else 'A levantar')
    c.font = F_OBS
    if nome != '01 Living': c.fill = P_AT
    pass
    l += 1
rg.cell(l, 1, 'TOTAL').font = F_B
for col in range(4, 12):
    c = rg.cell(l, col, f'=SUM({get_column_letter(col)}{r0}:'
                        f'{get_column_letter(col)}{l-1})')
    c.font = F_B; c.fill = P_TOT
    c.number_format = M2 if col == 4 else ('#,##0' if col == 5 else RS)
TOT = {k: f'$={get_column_letter(c)}${l}' for k, c in
       (('area',4),('chapas',5),('chapa',6),('fita',7),('fer',8),('alma',9),
        ('ter',10),('cd',11))}
TOTL = l
l += 2

l = secao(rg, l, 'MATERIAIS, TERCEIRIZADOS E COMISSÕES', 13)
l = cab(rg, l, ['Linha', 'Valor', '% do custo direto', '', '', '', '', '', '',
                '', '', '', 'Observação'])
def linha_res(rot, formula, obs=''):
    global l
    rg.cell(l, 1, rot).font = F_N
    c = rg.cell(l, 2, formula); c.number_format = RS; c.font = F_LINK
    c = rg.cell(l, 3, f'=IF($K${TOTL}=0,0,B{l}/$K${TOTL})')
    c.number_format = PCT; c.font = F_N
    rg.cell(l, 13, obs).font = F_OBS
    l += 1
linha_res('MDF — chapa', f'=K{TOTL-len(AMBIENTES)-1+len(AMBIENTES)+0}'
          if False else f'=F{TOTL}', 'Todos os padrões Duratex a R$ 600')
linha_res('Fita de borda', f'=G{TOTL}')
linha_res('Ferragem Blum', f'=H{TOTL}',
          'Dobradiça 50, corrediça 250, HK-XS 250, puxador slim 35')
linha_res('Alma de aço', f'=I{TOTL}',
          'Barra chata de 5 mm, uma por peça acima de 30 mm')
linha_res('Iluminação e terceirizados', f'=J{TOTL}')
rg.cell(l, 1, 'CUSTO DIRETO DO PROJETO').font = Font(name='Arial', size=11,
                                                     bold=True, color=TINTA)
c = rg.cell(l, 2, f'=K{TOTL}'); c.font = Font(name='Arial', size=11, bold=True,
                                              color=TINTA)
c.number_format = RS; c.fill = P_TOT
CD_TOT = f'$B${l}'; l += 2

rg.cell(l, 1, 'O que a prancha traz e NÃO é marcenaria').font = F_B; l += 1
for it in ('Parede com pedra Atacama Branca, revestimentos e pinturas',
           'Pedras de bancada: quartzito, granito e travertino',
           'Mobiliário solto, luminárias, tapetes, cortinas e espelhos',
           'Eletrodomésticos, cubas, torneiras e metais'):
    rg.cell(l, 1, it).font = F_OBS
    rg.merge_cells(start_row=l, start_column=1, end_row=l, end_column=13); l += 1

# ── aba 2 ───────────────────────────────────────────────────────────────
cu = wb.create_sheet('Custos')
larguras(cu, [40, 16, 14, 44])
cu['A1'] = 'Custos financeiros e operacionais'
cu['A1'].font = Font(name='Arial', size=16, bold=True, color=TINTA)
cu['A2'] = ('Operacional é o que sai da fábrica. Financeiro é o que sai do '
            'preço antes de a fábrica ver.')
cu['A2'].font = F_OBS
l = 4
l = secao(cu, l, 'ENTRADAS', 4)
l = cab(cu, l, ['Entrada', 'Valor', '', 'Observação'])
ENT = {}
for rot, val, fmt, obs in [
  ('Preço de venda', 0, RS, 'A definir — alinhar as questões técnicas antes'),
  ('Margem de contribuição alvo', 0.40, PCT, 'Faixa ideal da casa: 35 a 40%'),
  ('Número de parcelas no cartão', 0, '#,##0', 'Zero quando não há cartão'),
  ('Tem RT?  1 para sim, 0 para não', 1, '#,##0', 'Projeto de arquiteta'),
  ('Tem comissão de vendedor?  1 ou 0', 0, '#,##0', '')]:
    cu.cell(l, 1, rot).font = F_N
    c = cu.cell(l, 2, val); c.font = F_IN; c.number_format = fmt
    c.fill = PatternFill('solid', fgColor='FFFF00')
    cu.cell(l, 4, obs).font = F_OBS
    ENT[rot] = l; l += 1
PV   = f"$B${ENT['Preço de venda']}"
MC   = f"$B${ENT['Margem de contribuição alvo']}"
NPAR = f"$B${ENT['Número de parcelas no cartão']}"
TRT  = f"$B${ENT['Tem RT?  1 para sim, 0 para não']}"
TVEN = f"$B${ENT['Tem comissão de vendedor?  1 ou 0']}"
l += 1

# ⛔ A ORDEM IMPORTA: o financeiro vem primeiro porque é ele que produz o
#   líquido 2, que é a base das comissões do bloco operacional.
l = secao(cu, l, 'CUSTOS FINANCEIROS — o que sai do preço antes da fábrica', 4)
l = cab(cu, l, ['Linha', 'Valor', '% do preço', 'Observação'])
def linha(rot, formula, obs='', neg=False, forte=False, fmt=RS):
    global l
    cu.cell(l, 1, rot).font = F_B if forte else F_N
    c = cu.cell(l, 2, formula); c.number_format = fmt
    c.font = F_B if forte else F_LINK
    if forte: c.fill = P_TOT
    c = cu.cell(l, 3, f'=IF({PV}=0,0,B{l}/{PV})'); c.number_format = PCT
    c.font = F_N
    cu.cell(l, 4, obs).font = F_OBS
    l += 1
    return l-1
R_NF   = linha('Nota fiscal', f'={PV}*{bref("Nota fiscal")}')
R_CAR  = linha('Taxa de máquina de cartão',
               f'={PV}*{bref("Taxa de cartão, por parcela")}*{NPAR}')
R_LIQ  = linha('Líquido  =  preço − nota − cartão', f'={PV}-B{R_NF}-B{R_CAR}',
               'Base da RT e da comissão de vendedor', forte=True)
LIQ    = f'$B${R_LIQ}'
R_RT   = linha('RT da arquiteta', f'={LIQ}*{bref("RT da arquiteta")}*{TRT}')
R_VEN  = linha('Comissão de vendedor',
               f'={LIQ}*{bref("Comissão de vendedor")}*{TVEN}')
R_LQ2  = linha('Líquido 2  =  líquido − RT − vendedor',
               f'={LIQ}-B{R_RT}-B{R_VEN}',
               'Base de todas as comissões internas', forte=True)
LIQ2   = f'$B${R_LQ2}'
R_FIN  = linha('TOTAL FINANCEIRO', f'=B{R_NF}+B{R_CAR}+B{R_RT}+B{R_VEN}',
               forte=True)
FIN_TOT = f'$B${R_FIN}'
l += 1

l = secao(cu, l, 'CUSTOS OPERACIONAIS — o que sai da fábrica', 4)
l = cab(cu, l, ['Linha', 'Valor', '% do preço', 'Observação'])
R_MAT = linha('Materiais, ferragem e terceirizados',
              f"='Resumo Geral'!{CD_TOT}",
              'Custo direto somado das vinte abas de ambiente')
R_COM = []
for rot, nome in [('Comissão de produção', 'Produção'),
                  ('Comissão de montagem', 'Montagem'),
                  ('Comissão de projeto', 'Projeto'),
                  ('Comissão de coordenação', 'Coordenação'),
                  ('Comissão de gestão de projetos', 'Gestão de projetos')]:
    R_COM.append(linha(rot, f'={LIQ2}*{bref(nome)}'))
R_ERR = linha('Margem de erro', f'={PV}*{bref("Margem de erro")}')
R_SER = linha('Desgaste de serra e fresa',
              f'={PV}*{bref("Desgaste de serra e fresa")}')
R_MAN = linha('Manutenção de máquinas',
              f'={PV}*{bref("Manutenção de máquinas")}')
R_OP  = linha('TOTAL OPERACIONAL', f'=SUM(B{R_MAT}:B{R_MAN})', forte=True)
OP_TOT = f'$B${R_OP}'
l += 1

l = secao(cu, l, 'A BASE DA CASA, NESTA CONDIÇÃO', 4)
l = cab(cu, l, ['Linha', 'Valor', '', 'Observação'])
cu.cell(l, 1, 'Encargos sobre o preço, somados').font = F_N
c = cu.cell(l, 2, f'={bref("Nota fiscal")}+{bref("Taxa de cartão, por parcela")}'
                  f'*{NPAR}+{bref("Margem de erro")}'
                  f'+{bref("Desgaste de serra e fresa")}'
                  f'+{bref("Manutenção de máquinas")}')
c.number_format = PCT; c.font = F_N; R_E1 = l; l += 1
# ⛔ FRAÇÃO PURA, não dividida pelo preço: a base da casa existe antes de
#   haver preço, e com o preço em zero a divisão zerava a conta.
cu.cell(l, 1, 'Líquido, como fração do preço').font = F_N
c = cu.cell(l, 2, f'=1-{bref("Nota fiscal")}'
                  f'-{bref("Taxa de cartão, por parcela")}*{NPAR}')
c.number_format = PCT; c.font = F_N; R_LF = l; l += 1
cu.cell(l, 1, 'RT e vendedor, como fração do preço').font = F_N
c = cu.cell(l, 2, f'=B{R_LF}*({bref("RT da arquiteta")}*{TRT}'
                  f'+{bref("Comissão de vendedor")}*{TVEN})')
c.number_format = PCT; c.font = F_N; R_E2 = l; l += 1
cu.cell(l, 1, 'Comissões internas, como fração do preço').font = F_N
c = cu.cell(l, 2, f'=(B{R_LF}-B{R_E2})*{bref("Soma das comissões internas")}')
c.number_format = PCT; c.font = F_N; R_E3 = l; l += 1
cu.cell(l, 1, 'BASE  =  o que sobra para custo e margem').font = F_B
c = cu.cell(l, 2, f'=1-B{R_E1}-B{R_E2}-B{R_E3}')
c.number_format = PCT; c.font = F_B; c.fill = P_TOT
cu.cell(l, 4, 'Com RT e sem vendedor dá 76,09%; sem os dois, 84,88%').font = F_OBS
BASE_C = f'$B${l}'; l += 2

l = secao(cu, l, 'RESULTADO', 4)
l = cab(cu, l, ['Linha', 'Valor', '', 'Observação'])
for rot, f_, fmt, obs, forte in [
  ('Preço de venda', f'={PV}', RS, '', False),
  ('Menos custos financeiros', f'=-{FIN_TOT}', RS, '', False),
  ('Menos custos operacionais', f'=-{OP_TOT}', RS, '', False),
  ('MARGEM DE CONTRIBUIÇÃO', f'={PV}-{FIN_TOT}-{OP_TOT}', RS, '', True),
  ('MC em percentual', f'=IF({PV}=0,0,({PV}-{FIN_TOT}-{OP_TOT})/{PV})', PCT,
   'Piso da casa 35%, faixa ideal de 35 a 40%', True),
  ('Preço para a MC alvo',
   f'=IF({BASE_C}-{MC}<=0,0,ROUND(B{R_MAT}/({BASE_C}-{MC})/10,0)*10)', RS,
   'Custo direto dividido por base menos MC, arredondado a R$ 10', True)]:
    cu.cell(l, 1, rot).font = F_B if forte else F_N
    c = cu.cell(l, 2, f_); c.font = F_B if forte else F_N
    c.number_format = fmt
    if forte: c.fill = P_TOT
    cu.cell(l, 4, obs).font = F_OBS
    l += 1

ORDEM = ['Resumo Geral', 'Custos', 'Base de Preços'] + \
        [a for a, *_ in AMBIENTES if a in COM_ABA]
assert sorted(ORDEM) == sorted(wb.sheetnames), '⛔ A ORDEM NÃO COBRE AS ABAS'
wb._sheets = [wb[n] for n in ORDEM]
wb.save('/tmp/claude-0/-home-user-valvicorcamentista/7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/planilha.xlsx')
print('ordem final:', wb.sheetnames[:5], '...', wb.sheetnames[-2:])

# ── Living · ferragem, alma e iluminação ────────────────────────────────
L0 = CD_REF['01 Living']
def preencher(lv, linha0, dados):
    for i, cols in enumerate(dados):
        for col, val in cols.items():
            c = lv.cell(linha0+i, col, val)
            c.font = F_IN if isinstance(val, (int, float)) else (
                F_OBS if col == 8 else F_N)
            if col in (3, 5): c.number_format = '#,##0'
            if col == 4: c.number_format = RS
            if col == 8 and isinstance(val, str) and 'contar' in val:
                c.fill = P_AT
FER0 = L0['fer'] - 10
preencher(lv, FER0, [
 {1:'Dobradiça Blum', 2:'DET 08 Porta mimetizada', 3:4,
  4:f'={bref("Dobradiça")}', 8:'Folha de 90 × 210; confirmar se leva quatro ou cinco'},
 {1:'Corrediça Blum', 2:'DET 02 Aparador', 3:1, 4:f'={bref("Corrediça (por gaveta)")}',
  8:'Uma gaveta'},
 {1:'Dobradiça Blum', 2:'DET 01 Sapateira',
  4:f'={bref("Dobradiça")}', 8:'A contar: tipo e número de frentes a confirmar'},
 {1:'Dobradiça Blum', 2:'DET 06 Portas de vidro da cristaleira',
  4:f'={bref("Dobradiça")}', 8:'A contar no desenho'},
 {1:'Corrediça Blum', 2:'DET 06 Gavetas do rack',
  4:f'={bref("Corrediça (por gaveta)")}', 8:'A contar no desenho'},
 {1:'Corrediça Blum', 2:'DET 07 Gavetas da estante',
  4:f'={bref("Corrediça (por gaveta)")}', 8:'A contar no desenho'},
])
TER0 = L0['ter'] - 6
preencher(lv, TER0, [
 {1:'Perfil de LED com difusor (m)', 2:'DET 03 Prateleira', 3:1.35,
  4:f'={bref("Perfil de LED com difusor (R$/m)")}', 8:'Prateleira de 135'},
 {1:'Perfil de LED com difusor (m)', 2:'DET 01 Sapateira',
  4:f'={bref("Perfil de LED com difusor (R$/m)")}', 8:'A contar: LED na base'},
 {1:'Perfil de LED com difusor (m)', 2:'DET 05 Banco e floreira',
  4:f'={bref("Perfil de LED com difusor (R$/m)")}', 8:'A contar'},
 {1:'Perfil de LED com difusor (m)', 2:'DET 06 Cristaleira e base recuada',
  4:f'={bref("Perfil de LED com difusor (R$/m)")}', 8:'A contar: prateleiras e base'},
 {1:'Fonte de LED', 2:'Living', 3:1, 4:f'={bref("Fonte de LED")}', 8:''},
 {1:'Vidro reflecta champagne', 2:'DET 06 Portas da cristaleira',
  8:'A cotar com o vidraceiro; não está na base da casa'},
])
lv.cell(L0['fer']-11, 8, 'Blum: dobradiça 50, corrediça 250').font = F_OBS
wb.save('/tmp/claude-0/-home-user-valvicorcamentista/7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/planilha.xlsx')
print('Living completado')
