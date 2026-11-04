# -*- coding: utf-8 -*-
"""A identidade visual da casa, aplicada às abas que NÃO são de ambiente.

⭐⭐ A regra que o aba.py já tinha aprendido [Jonathan, 28/10/2026]:
  "a formatação do living e da cozinha estao diferentes". Estavam, e em
  quinze pontos — porque foram formatadas à mão, duas vezes. ⛔ Duas mãos,
  dois resultados. A aba não se formata, ela se GERA.

Este arquivo faz pelo Painel, pela Preço e Comissões, pela Base (importada) e
pela aba-modelo o que o aba.py faz pelas abas de ambiente: devolve o lote de
requests, sempre igual.

⭐ A PALETA É A MESMA do aba.py, copiada de lá e não reinventada.
"""
import json

PRETO  = {'red': .102, 'green': .102, 'blue': .102}
CINZA  = {'red': .42,  'green': .42,  'blue': .42}
CLARO  = {'red': .675, 'green': .675, 'blue': .675}
OURO   = {'red': .686, 'green': .514, 'blue': .231}
VERM   = {'red': .776, 'green': .157, 'blue': .157}
BRANCO = {'red': 1, 'green': 1, 'blue': 1}
F7     = {'red': .969, 'green': .969, 'blue': .969}
F5     = {'red': .961, 'green': .961, 'blue': .961}
AMARELO = {'red': 1, 'green': .9490196, 'blue': .8}
MOEDA  = {'type': 'CURRENCY', 'pattern': '"R$" #,##0.00'}
PCT    = {'type': 'PERCENT',  'pattern': '0.0%'}
PCT2   = {'type': 'PERCENT',  'pattern': '0.00%'}
INT    = {'type': 'NUMBER',   'pattern': '0'}

COL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RUA  = {'bottom': {'style': 'SOLID', 'width': 1, 'color': PRETO}}
TETO = {'top': {'style': 'SOLID_THICK', 'width': 3, 'color': OURO}}

def fm(sz=10, bd=False, it=False, fg=PRETO, bg=None, al='LEFT',
       wr='CLIP', num=None, bor=None):
    """⛔ `fields: "userEnteredFormat"` troca o formato INTEIRO, então o que
    não vem aqui volta ao padrão — e é por isso que omitir é correto, não só
    mais curto. ⭐ É também o que limpa padrão numérico herdado."""
    # ⛔ fontSize da API é INTEIRO: 9,5 derruba o lote inteiro com
    #   "Internal error", e o erro não diz qual request falhou.
    t = {'fontFamily': 'Arial', 'fontSize': int(sz), 'foregroundColor': fg}
    if bd: t['bold'] = True
    if it: t['italic'] = True
    f = {'textFormat': t, 'horizontalAlignment': al,
         'verticalAlignment': 'MIDDLE', 'wrapStrategy': wr}
    if bg: f['backgroundColor'] = bg
    if num: f['numberFormat'] = num
    if bor: f['borders'] = bor
    return f

def mk(sid):
    def rng(r0, r1, c0, c1):
        return {'sheetId': sid, 'startRowIndex': r0-1, 'endRowIndex': r1,
                'startColumnIndex': COL.index(c0), 'endColumnIndex': COL.index(c1)+1}
    def rc(r0, r1, c0, c1, f):
        return {'repeatCell': {'range': rng(r0, r1, c0, c1),
                'cell': {'userEnteredFormat': f}, 'fields': 'userEnteredFormat'}}
    def alt(r0, r1, px):
        return {'updateDimensionProperties': {'range': {'sheetId': sid,
                'dimension': 'ROWS', 'startIndex': r0-1, 'endIndex': r1},
                'properties': {'pixelSize': px}, 'fields': 'pixelSize'}}
    def mesc(r, c0, c1):
        return {'mergeCells': {'range': rng(r, r, c0, c1), 'mergeType': 'MERGE_ALL'}}
    def larg(c, px):
        return {'updateDimensionProperties': {'range': {'sheetId': sid,
                'dimension': 'COLUMNS', 'startIndex': COL.index(c),
                'endIndex': COL.index(c)+1}, 'properties': {'pixelSize': px},
                'fields': 'pixelSize'}}
    return rng, rc, alt, mesc, larg

def cabeca(rc, alt, mesc, fim, c1='K'):
    """⭐ O RITMO, e ele é o mesmo em toda aba: título preto de ponta a ponta,
    subtítulo cinza em frase corrida, e a folha inteira limpa por baixo."""
    return [rc(1, fim, 'A', c1, fm()),
            rc(1, 1, 'B', c1, fm(16, True, fg=BRANCO, bg=PRETO)),
            mesc(1, 'B', c1), alt(1, 1, 46),
            rc(2, 2, 'B', c1, fm(9, fg=CINZA, wr='WRAP')),
            mesc(2, 'B', c1), alt(2, 2, 42)]

def secao(rc, mesc, r, c1='K', verm=False):
    """Seção em caixa alta, recuada por dois espaços, com régua por baixo.
    ⭐ A única em VERMELHO é a de dúvidas: ela pede resposta, não leitura."""
    return [rc(r, r, 'B', c1, fm(11, True, fg=VERM if verm else PRETO, bor=RUA)),
            mesc(r, 'B', c1)]

def texto(rc, alt, mesc, r, c1='K', px=None, fg=CINZA, sz=9):
    return [rc(r, r, 'B', c1, fm(sz, fg=fg, wr='WRAP')), mesc(r, 'B', c1)] + \
           ([alt(r, r, px)] if px else [])

def cabtab(rc, r, c0='B', c1='K'):
    return [rc(r, r, c0, c1, fm(8, True, fg=CINZA, bg=F7))]
