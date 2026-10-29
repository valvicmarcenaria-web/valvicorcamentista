# -*- coding: utf-8 -*-
"""O formato da aba 'Preço e Comissões'. Mesma identidade das 19 abas de
   ambiente: Arial, coluna A de margem, ouro nas seções, grade desligada.
   ⭐ o que muda aqui é o AMARELO: ele marca as únicas células que o
     senhor digita, e nada mais na planilha é amarelo."""
import json

SID = 201
FIM = 78

PRETO  = {'red': .1019608, 'green': .1019608, 'blue': .1019608}
CINZA  = {'red': .4196078, 'green': .4196078, 'blue': .4196078}
CLARO  = {'red': .6745098, 'green': .6745098, 'blue': .6745098}
OURO   = {'red': .6862745, 'green': .5137255, 'blue': .2313725}
VERM   = {'red': .7764706, 'green': .1568628, 'blue': .1568628}
BRANCO = {'red': 1, 'green': 1, 'blue': 1}
F7     = {'red': .9686275, 'green': .9686275, 'blue': .9686275}
F5     = {'red': .9607843, 'green': .9607843, 'blue': .9607843}
AMAR   = {'red': 1, 'green': .9490196, 'blue': .8}
ROSA   = {'red': .996, 'green': .922, 'blue': .922}
MOEDA  = {'type': 'CURRENCY', 'pattern': '"R$" #,##0.00'}
PCT1   = {'type': 'PERCENT',  'pattern': '0.0%'}
PCT2   = {'type': 'PERCENT',  'pattern': '0.00%'}
INT    = {'type': 'NUMBER',   'pattern': '0'}

def fm(sz=10, bd=False, it=False, fg=PRETO, bg=None, al='LEFT',
       wr='CLIP', num=None, bor=None):
    t = {'fontFamily': 'Arial', 'fontSize': sz,
         'foregroundColorStyle': {'rgbColor': fg}}
    if bd: t['bold'] = True
    if it: t['italic'] = True
    f = {'textFormat': t, 'horizontalAlignment': al,
         'verticalAlignment': 'MIDDLE', 'wrapStrategy': wr}
    if bg: f['backgroundColorStyle'] = {'rgbColor': bg}
    if num: f['numberFormat'] = num
    if bor: f['borders'] = bor
    return f
COL = 'ABCDEFGHI'
def rng(r0, r1, c0='B', c1='H'):
    return {'sheetId': SID, 'startRowIndex': r0-1, 'endRowIndex': r1,
            'startColumnIndex': COL.index(c0), 'endColumnIndex': COL.index(c1)+1}
def rc(r0, r1, c0, c1, f):
    return {'repeatCell': {'range': rng(r0, r1, c0, c1),
            'cell': {'userEnteredFormat': f}, 'fields': 'userEnteredFormat'}}
def alt(r0, r1, px):
    return {'updateDimensionProperties': {'range': {'sheetId': SID,
            'dimension': 'ROWS', 'startIndex': r0-1, 'endIndex': r1},
            'properties': {'pixelSize': px}, 'fields': 'pixelSize'}}
def mesc(r, c0, c1):
    return {'mergeCells': {'range': rng(r, r, c0, c1), 'mergeType': 'MERGE_ALL'}}
RUA = {'bottom': {'style': 'SOLID', 'width': 1, 'colorStyle': {'rgbColor': PRETO}}}

SECOES  = (4, 12, 29, 38, 64, 72)
ESPACOS = (3, 5, 11, 13, 28, 30, 37, 39, 63, 65, 71, 73)

Q = []
# ── a folha inteira, limpa ─────────────────────────────────────────────
Q.append(rc(1, FIM, 'A', 'I', fm()))
Q.append(rc(1, FIM, 'I', 'I', fm(sz=9, fg=CLARO)))
# ── faixa preta e subtítulo ────────────────────────────────────────────
Q.append(rc(1, 1, 'B', 'H', fm(16, True, fg=BRANCO, bg=PRETO)))
Q.append(rc(2, 2, 'B', 'H', fm(9, fg=CINZA, wr='WRAP')))
# ── as seis seções, todas iguais ───────────────────────────────────────
for s in SECOES:
    Q.append(rc(s, s, 'B', 'H', fm(11, True, fg=OURO, bor=RUA)))

# ── ① a condição da venda ──────────────────────────────────────────────
Q.append(rc(6, 6, 'B', 'H', fm(8, True, fg=CINZA, bg=F7)))
Q.append(rc(6, 6, 'D', 'D', fm(8, True, fg=CINZA, bg=F7, al='CENTER')))
Q.append(rc(7, 10, 'B', 'B', fm(10, True)))
Q.append(rc(7, 10, 'C', 'C', fm(9, fg=CINZA, wr='WRAP')))
# ⭐ as quatro únicas células de digitação do quadro ①
Q.append(rc(7,  7,  'D', 'D', fm(12, True, bg=AMAR, al='CENTER', num=PCT1)))
Q.append(rc(8,  8,  'D', 'D', fm(12, True, bg=AMAR, al='CENTER', num=INT)))
Q.append(rc(9,  10, 'D', 'D', fm(12, True, bg=AMAR, al='CENTER', num=PCT1)))

# ── ② a cascata ────────────────────────────────────────────────────────
Q.append(rc(14, 14, 'B', 'H', fm(8, True, fg=CINZA, bg=F7)))
Q.append(rc(14, 14, 'D', 'E', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
Q.append(rc(15, 25, 'B', 'B', fm(10)))
Q.append(rc(15, 25, 'C', 'C', fm(9, fg=CINZA, wr='WRAP')))
Q.append(rc(15, 25, 'D', 'D', fm(10, al='RIGHT', num=PCT2)))
Q.append(rc(15, 25, 'E', 'E', fm(10, al='RIGHT', num=MOEDA)))
# ⛔ soma e base são o fecho do quadro: elas não são linha, são resultado
Q.append(rc(26, 27, 'B', 'B', fm(10, True, bg=F5)))
Q.append(rc(26, 27, 'C', 'C', fm(9, fg=CINZA, wr='WRAP', bg=F5)))
Q.append(rc(26, 27, 'D', 'D', fm(11, True, al='RIGHT', num=PCT2, bg=F5)))
Q.append(rc(26, 27, 'E', 'E', fm(11, True, al='RIGHT', num=MOEDA, bg=F5)))
Q.append(rc(27, 27, 'B', 'E', fm(11, True, fg=OURO, bg=F5)))
Q.append(rc(27, 27, 'C', 'C', fm(9, fg=CINZA, wr='WRAP', bg=F5)))
Q.append(rc(27, 27, 'D', 'D', fm(11, True, fg=OURO, al='RIGHT', num=PCT2, bg=F5)))
Q.append(rc(27, 27, 'E', 'E', fm(11, True, fg=OURO, al='RIGHT', num=MOEDA, bg=F5)))

# ── ③ o preço do projeto ───────────────────────────────────────────────
Q.append(rc(31, 36, 'B', 'B', fm(10, True)))
Q.append(rc(31, 36, 'C', 'C', fm(9, fg=CINZA, wr='WRAP')))
Q.append(rc(31, 36, 'D', 'D', fm(10, al='RIGHT', num=PCT2)))
Q.append(rc(31, 36, 'E', 'E', fm(10, al='RIGHT', num=MOEDA)))
# ⭐ o preço é a linha que todo mundo procura: ela é a maior da aba
Q.append(rc(34, 34, 'B', 'B', fm(14, True, fg=OURO)))
Q.append(rc(34, 34, 'E', 'E', fm(16, True, fg=OURO, al='RIGHT', num=MOEDA)))
Q.append(rc(35, 35, 'E', 'E', fm(11, True, al='RIGHT', num=MOEDA)))
Q.append(rc(36, 36, 'B', 'B', fm(9, True, fg=CINZA, wr='WRAP')))
Q.append(rc(36, 36, 'C', 'C', fm(9, fg=CLARO, it=True, wr='WRAP')))

# ── ④ por ambiente ─────────────────────────────────────────────────────
Q.append(rc(40, 40, 'B', 'H', fm(8, True, fg=CINZA, bg=F7)))
Q.append(rc(40, 40, 'C', 'H', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
Q.append(rc(40, 40, 'D', 'D', fm(8, True, fg=CINZA, bg=F7, al='CENTER')))
Q.append(rc(41, 60, 'B', 'B', fm(10)))
Q.append(rc(41, 60, 'C', 'C', fm(10, al='RIGHT', num=MOEDA)))
# ⭐ a coluna do AJUSTE é amarela em todas as vinte linhas: é o botão de MC
#   por ambiente que o senhor pediu, espelhado item a item
Q.append(rc(41, 60, 'D', 'D', fm(10, True, bg=AMAR, al='CENTER', num=PCT1)))
Q.append(rc(41, 60, 'E', 'E', fm(10, al='RIGHT', num=PCT2)))
Q.append(rc(41, 60, 'F', 'F', fm(9, fg=CINZA, al='RIGHT', num=PCT1)))
Q.append(rc(41, 60, 'G', 'G', fm(10, True, al='RIGHT', num=MOEDA)))
Q.append(rc(41, 60, 'H', 'H', fm(10, al='RIGHT', num=MOEDA)))
Q.append(rc(61, 61, 'B', 'H', fm(11, True, bg=F5)))
Q.append(rc(61, 61, 'C', 'C', fm(11, True, al='RIGHT', num=MOEDA, bg=F5)))
Q.append(rc(61, 61, 'E', 'E', fm(11, True, al='RIGHT', num=PCT2, bg=F5)))
Q.append(rc(61, 61, 'F', 'F', fm(9, True, fg=CINZA, al='RIGHT', num=PCT1, bg=F5)))
Q.append(rc(61, 61, 'G', 'G', fm(12, True, fg=OURO, al='RIGHT', num=MOEDA, bg=F5)))
Q.append(rc(61, 61, 'H', 'H', fm(11, True, al='RIGHT', num=MOEDA, bg=F5)))
Q.append(rc(62, 62, 'B', 'B', fm(9, True, fg=CINZA, wr='WRAP')))
Q.append(rc(62, 62, 'C', 'C', fm(9, True, al='RIGHT', num=MOEDA)))

# ── ⑤ a escada de pagamento ────────────────────────────────────────────
Q.append(rc(66, 66, 'B', 'H', fm(8, True, fg=CINZA, bg=F7)))
Q.append(rc(66, 66, 'C', 'H', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
Q.append(rc(67, 70, 'B', 'B', fm(10, True)))
Q.append(rc(67, 70, 'C', 'C', fm(10, al='RIGHT', num=INT)))
Q.append(rc(67, 70, 'D', 'D', fm(10, al='RIGHT', num=PCT2)))
Q.append(rc(67, 70, 'E', 'E', fm(10, al='RIGHT', num=PCT2)))
Q.append(rc(67, 70, 'F', 'F', fm(11, True, al='RIGHT', num=MOEDA)))
Q.append(rc(67, 70, 'G', 'G', fm(10, True, al='RIGHT', num=PCT2)))
Q.append(rc(67, 70, 'H', 'H', fm(10, fg=CINZA, al='RIGHT', num=PCT1)))
# ⛔ à vista é o degrau de referência: ele fica em cinza claro para não
#   competir com os outros três, que são os que o cliente escolhe
Q.append(rc(67, 67, 'B', 'H', fm(10, True, bg=F7)))
Q.append(rc(67, 67, 'C', 'C', fm(10, al='RIGHT', num=INT, bg=F7)))
Q.append(rc(67, 67, 'D', 'E', fm(10, al='RIGHT', num=PCT2, bg=F7)))
Q.append(rc(67, 67, 'F', 'F', fm(11, True, al='RIGHT', num=MOEDA, bg=F7)))
Q.append(rc(67, 67, 'G', 'G', fm(10, True, al='RIGHT', num=PCT2, bg=F7)))
Q.append(rc(67, 67, 'H', 'H', fm(10, fg=CLARO, al='RIGHT', num=PCT1, bg=F7)))

# ── ⑥ as notas ─────────────────────────────────────────────────────────
Q.append(rc(74, 78, 'C', 'H', fm(10, wr='WRAP')))

# ── larguras ───────────────────────────────────────────────────────────
#   ⛔ a coluna C serve dois papéis nesta aba: explicação longa nos quadros
#     ① ② ③ ⑥ e dinheiro no ④. 300 px é o acordo: o texto quebra em duas
#     linhas e o número não fica perdido no meio do branco.
for c, px in zip('ABCDEFGHI', (36, 268, 300, 104, 132, 104, 140, 140, 24)):
    Q.append({'updateDimensionProperties': {'range': {'sheetId': SID,
              'dimension': 'COLUMNS', 'startIndex': COL.index(c),
              'endIndex': COL.index(c)+1}, 'properties': {'pixelSize': px},
              'fields': 'pixelSize'}})
Q.append({'updateSheetProperties': {'properties': {'sheetId': SID,
          'gridProperties': {'frozenRowCount': 2, 'hideGridlines': True}},
          'fields': 'gridProperties.frozenRowCount,gridProperties.hideGridlines'}})
# ── alturas ────────────────────────────────────────────────────────────
Q.append(alt(1, 1, 46))
Q.append(alt(2, 2, 34))
for s in SECOES: Q.append(alt(s, s, 30))
for e in ESPACOS: Q.append(alt(e, e, 10))
Q.append(alt(34, 34, 34))
Q.append(alt(61, 61, 30))
# ── mesclagens ─────────────────────────────────────────────────────────
Q.append({'unmergeCells': {'range': rng(1, FIM, 'A', 'I')}})
for r in (1, 2) + SECOES: Q.append(mesc(r, 'B', 'H'))
for r in range(74, 79):   Q.append(mesc(r, 'C', 'H'))
for r in range(31, 37):   Q.append(mesc(r, 'F', 'H'))
Q.append(mesc(62, 'D', 'H'))
# ── as duas conferências gritam quando não fecham ──────────────────────
def grita(r, cel, c0, c1):
    return {'addConditionalFormatRule': {'index': 0, 'rule': {
            'ranges': [rng(r, r, c0, c1)],
            'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA', 'values':
                            [{'userEnteredValue': f'=ROUND({cel};2)<>0'}]},
            'format': {'backgroundColorStyle': {'rgbColor': ROSA},
                       'textFormat': {'bold': True,
                       'foregroundColorStyle': {'rgbColor': VERM}}}}}}}
Q.append(grita(36, '$E$36', 'B', 'H'))
Q.append(grita(62, '$C$62', 'B', 'H'))
# ⛔ e a MC abaixo do piso da casa grita também: 35% não é sugestão
Q.append({'addConditionalFormatRule': {'index': 0, 'rule': {
          'ranges': [rng(41, 61, 'E', 'E')],
          'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA', 'values':
                          [{'userEnteredValue': '=AND($C41>0;$E41<0,35)'}]},
          'format': {'backgroundColorStyle': {'rgbColor': ROSA},
                     'textFormat': {'bold': True,
                     'foregroundColorStyle': {'rgbColor': VERM}}}}}}})

json.dump(Q, open('_fmt-preco.json', 'w'), ensure_ascii=False)
print(len(Q), 'requests')
