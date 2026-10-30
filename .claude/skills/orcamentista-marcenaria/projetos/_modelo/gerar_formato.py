# -*- coding: utf-8 -*-
"""Emite o lote de requests de formato das quatro abas fixas."""
import sys, json
sys.path.insert(0, '.')
from formatar import *

def painel(sid=0):
    rng, rc, alt, mesc, larg = mk(sid)
    Q = cabeca(rc, alt, mesc, 60)
    Q += [larg('A', 28), larg('B', 300), larg('C', 120)]
    # os quatro blocos de seção
    for r in (4, 8, 12, 17, 27):
        Q += secao(rc, mesc, r)
    # os dois parágrafos de instrução
    Q += texto(rc, alt, mesc, 6, px=74)
    Q += texto(rc, alt, mesc, 10, px=74)
    # ⭐ O CONJUNTO — cinco indicadores, em pares de colunas
    Q += cabtab(rc, 14)
    Q += [rc(15, 15, 'B', 'K', fm(18, True, al='LEFT')), alt(15, 15, 34)]
    # ONDE ESTÁ O DINHEIRO
    Q += cabtab(rc, 19)
    Q += [rc(20, 24, 'B', 'F', fm(10)),
          rc(20, 25, 'G', 'G', fm(10, al='RIGHT', num=MOEDA)),
          rc(20, 25, 'H', 'H', fm(10, fg=CINZA, al='RIGHT', num=PCT)),
          rc(20, 25, 'I', 'K', fm(9, fg=CINZA, al='RIGHT')),
          rc(25, 25, 'B', 'K', fm(11, True, bor=TETO)),
          rc(25, 25, 'G', 'G', fm(11, True, al='RIGHT', num=MOEDA, bor=TETO))]
    # POR AMBIENTE
    Q += cabtab(rc, 28)
    Q += texto(rc, alt, mesc, 29, px=30, sz=9)
    Q += [rc(30, 30, 'B', 'K', fm(11, True, bor=TETO))]
    Q += [alt(4, 4, 26), alt(8, 8, 26), alt(12, 12, 26), alt(17, 17, 26),
          alt(27, 27, 26)]
    return Q

def preco(sid=201):
    rng, rc, alt, mesc, larg = mk(sid)
    Q = cabeca(rc, alt, mesc, 80, c1='I')
    Q += [larg('A', 28), larg('B', 300), larg('C', 430), larg('D', 110)]
    for r in (4, 12, 29, 38, 64):
        Q += secao(rc, mesc, r, c1='I')
    # ① a condição da venda
    Q += [rc(6, 6, 'B', 'D', fm(8, True, fg=CINZA, bg=F7)),
          rc(7, 10, 'B', 'B', fm(10, True)),
          rc(7, 10, 'C', 'C', fm(9, fg=CINZA, wr='WRAP')),
          rc(7, 7, 'D', 'D', fm(12, True, al='CENTER', bg=AMARELO, num=PCT)),
          rc(8, 8, 'D', 'D', fm(12, True, al='CENTER', bg=AMARELO, num=INT)),
          rc(9, 10, 'D', 'D', fm(12, True, al='CENTER', bg=AMARELO, num=PCT)),
          alt(7, 10, 30)]
    # ② a cascata
    Q += [rc(13, 13, 'B', 'E', fm(8, True, fg=CINZA, bg=F7)),
          rc(14, 25, 'B', 'B', fm(10)),
          rc(14, 25, 'C', 'C', fm(9, fg=CINZA, wr='WRAP')),
          rc(14, 25, 'D', 'D', fm(10, al='RIGHT', num=PCT2)),
          rc(14, 25, 'E', 'E', fm(10, fg=CINZA, al='RIGHT', num=MOEDA)),
          rc(26, 27, 'B', 'E', fm(11, True, bor=TETO)),
          rc(26, 27, 'C', 'C', fm(9, True, fg=CINZA, wr='WRAP', bor=TETO)),
          rc(26, 27, 'D', 'D', fm(11, True, al='RIGHT', num=PCT2, bor=TETO)),
          rc(26, 27, 'E', 'E', fm(11, True, al='RIGHT', num=MOEDA, bor=TETO))]
    # ③ o preço
    Q += [rc(31, 35, 'B', 'B', fm(10, True)),
          rc(31, 35, 'C', 'C', fm(9, fg=CINZA, wr='WRAP')),
          rc(31, 35, 'D', 'D', fm(11, al='RIGHT', num=PCT)),
          rc(31, 35, 'E', 'E', fm(12, True, al='RIGHT', num=MOEDA)),
          rc(33, 33, 'B', 'E', fm(13, True)),
          rc(33, 33, 'E', 'E', fm(14, True, al='RIGHT', num=MOEDA)),
          rc(35, 35, 'B', 'B', fm(9, True, fg=OURO, wr='WRAP')),
          rc(35, 35, 'E', 'E', fm(10, True, fg=OURO, al='RIGHT', num=MOEDA)),
          alt(31, 35, 28)]
    # ④ por ambiente
    Q += [rc(40, 40, 'B', 'H', fm(8, True, fg=CINZA, bg=F7)),
          rc(41, 60, 'B', 'B', fm(10)),
          rc(41, 60, 'C', 'C', fm(10, al='RIGHT', num=MOEDA)),
          rc(41, 60, 'D', 'D', fm(10, al='CENTER', bg=AMARELO)),
          rc(41, 60, 'E', 'E', fm(10, al='RIGHT', num=PCT)),
          rc(41, 60, 'F', 'F', fm(10, fg=CINZA, al='RIGHT', num=PCT)),
          rc(41, 60, 'G', 'G', fm(10, True, al='RIGHT', num=MOEDA)),
          rc(41, 60, 'H', 'H', fm(10, fg=CINZA, al='RIGHT', num=MOEDA)),
          rc(61, 61, 'B', 'H', fm(11, True, bor=TETO)),
          rc(61, 61, 'C', 'C', fm(11, True, al='RIGHT', num=MOEDA, bor=TETO)),
          rc(61, 61, 'E', 'F', fm(11, True, al='RIGHT', num=PCT, bor=TETO)),
          rc(61, 61, 'G', 'H', fm(11, True, al='RIGHT', num=MOEDA, bor=TETO)),
          rc(62, 62, 'B', 'B', fm(9, True, fg=OURO, wr='WRAP')),
          rc(62, 62, 'C', 'C', fm(10, True, fg=OURO, al='RIGHT', num=MOEDA))]
    # ⑤ a dificuldade
    Q += [rc(66, 66, 'B', 'D', fm(8, True, fg=CINZA, bg=F7)),
          rc(67, 69, 'B', 'B', fm(10, True)),
          rc(67, 69, 'C', 'C', fm(9, fg=CINZA, wr='WRAP')),
          rc(67, 69, 'D', 'D', fm(11, True, al='CENTER', num=PCT)),
          alt(67, 69, 32)]
    Q += [alt(4, 4, 26), alt(12, 12, 26), alt(29, 29, 26), alt(38, 38, 26),
          alt(64, 64, 26)]
    return Q

def base(sid=200, fim=100):
    rng, rc, alt, mesc, larg = mk(sid)
    Q = cabeca(rc, alt, mesc, fim, c1='F')
    Q += [larg('A', 260), larg('B', 100), larg('C', 90), larg('D', 430),
          larg('E', 230), larg('F', 70)]
    Q += [rc(3, 3, 'A', 'C', fm(11, True, fg=VERM)),
          rc(3, 3, 'D', 'D', fm(11, True, fg=VERM, al='CENTER', bg=AMARELO)),
          alt(3, 3, 30)]
    Q += secao(rc, mesc, 4, c1='F')
    Q += [rc(5, 5, 'A', 'F', fm(8, True, fg=CINZA, bg=F7)),
          rc(6, fim, 'A', 'A', fm(10)),
          rc(6, fim, 'B', 'B', fm(10, True, al='RIGHT', num=MOEDA)),
          rc(6, fim, 'C', 'C', fm(9, fg=CINZA, al='CENTER')),
          rc(6, fim, 'D', 'D', fm(9, fg=CINZA, wr='WRAP')),
          rc(6, fim, 'E', 'E', fm(9, fg=CLARO)),
          rc(6, fim, 'F', 'F', fm(9, fg=CLARO, al='CENTER', num=INT)),
          alt(6, fim, 21)]
    return Q

def modelo(sid=100):
    """⭐ A aba-modelo é SEMENTE, não entrega: toda aba de ambiente de verdade
    sai do aba.py, que já formata as suas 150 células. Aqui basta o esqueleto
    — título, seções, larguras e as faixas de texto corrido."""
    rng, rc, alt, mesc, larg = mk(sid)
    Q = cabeca(rc, alt, mesc, 50)
    Q += [larg('A', 28), larg('B', 300), larg('C', 430)]
    for r in (4, 15, 22, 30):
        Q += secao(rc, mesc, r)
    Q += secao(rc, mesc, 37)
    Q += secao(rc, mesc, 41, verm=True)
    Q += cabtab(rc, 6) + cabtab(rc, 17) + cabtab(rc, 32)
    Q += [rc(7, 11, 'B', 'K', fm(9, fg=CINZA, wr='WRAP')),
          rc(9, 9, 'D', 'D', fm(10, True, al='RIGHT', bg=AMARELO, num=INT)),
          rc(12, 12, 'B', 'K', fm(11, True, bor=TETO)),
          rc(18, 19, 'B', 'K', fm(9, fg=CINZA, wr='WRAP')),
          rc(23, 27, 'B', 'K', fm(9, fg=CINZA, wr='WRAP')),
          rc(33, 34, 'B', 'K', fm(9, fg=CINZA, wr='WRAP')),
          rc(38, 39, 'B', 'K', fm(9, fg=CINZA, wr='WRAP')),
          rc(42, 45, 'B', 'K', fm(9, fg=VERM, wr='WRAP')),
          alt(7, 45, 30)]
    Q += [alt(4, 4, 26), alt(15, 15, 26), alt(22, 22, 26), alt(30, 30, 26),
          alt(37, 37, 26), alt(41, 41, 26)]
    return Q

if __name__ == '__main__':
    qual = sys.argv[1]
    Q = {'painel': painel, 'preco': preco, 'base': base, 'modelo': modelo}[qual]()
    print(len(Q), 'requests', file=sys.stderr)
    print(json.dumps(Q, ensure_ascii=False, separators=(',', ':')))
