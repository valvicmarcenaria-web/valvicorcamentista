# -*- coding: utf-8 -*-
"""Closet Casal · folhas 09 e 10 (PDF p. 11–12). MDF Areia por dentro e por
fora, do piso ao forro (270), em U. Cantos da sapateira = canto morto."""
from motor import *

ambiente('Closet casal')
A = 'Areia 15'

# ── Armário parede D · 213 × 270 × 54 · 3 módulos de 71 ─────────────────
m = 'Armário parede D'
caixa(m, 213, 270, 54, 'Areia', interno=A, fundo='Areia 6')
divisorias(m, 2, 267, 54, A)
prateleiras(m, 6, 69, 54, A)                   # 3 maleiros + 3 prateleiras
cabideiro(m, 69); cabideiro(m, 69)
gavetas(m, 7, 67, 18, 50, 'Areia')             # gavetas internas, módulo central
for L in (71, 71, 71):
    P(m, 'Porta de correr', 268, L, 1, 'Areia 18', 2 * (L + 268) / 100)
    O(m, 'Desempenador de porta', 2, 'un', 100)
O(m, 'Sistema de correr SS150, 3 portas', 1, 'cj', 700)
O(m, 'Trilho SS150 3 m', 1, 'un', 250)
O(m, 'Cava 45° usinada', 3, 'frente', 50)

# ── Armário parede B · 144 × 270 × 54 · 2 módulos de 72 ─────────────────
m = 'Armário parede B'
caixa(m, 144, 270, 54, 'Areia', interno=A, fundo='Areia 6')
divisorias(m, 1, 267, 54, A)
prateleiras(m, 4, 70, 54, A)                   # 2 maleiros + 2 prateleiras
cabideiro(m, 70); cabideiro(m, 70)
gavetas(m, 4, 68, 20, 50, 'Areia')
correr(m, [72, 72], 268, 'Areia')
O(m, 'Cava 45° usinada', 2, 'frente', 50)

# ── Porta de giro camuflada em Areia, cava 45° · 70 × 210 + bandeira ────
m = 'Porta camuflada de passagem'
porta_passagem(m, 70, 210, 'Areia', sistema='pivo')
P(m, 'Bandeira acima da porta', 60, 70, 1, 'Areia 18', 2 * (60 + 70) / 100)

# ── Sapateira parede C · 136 × 270 × 43 · portas de correr com espelho ──
m = 'Sapateira com espelho'
caixa(m, 136, 270, 41, 'Areia', interno=A, fundo='Areia 6')
divisorias(m, 1, 267, 41, A)
prateleiras(m, 12, 66, 41, A)
correr(m, [66, 70], 268, 'Areia')
O(m, 'Espelho prata colado na porta', (0.66 + 0.70) * 2.68, 'm²', 600)

# ── Parede A · painel em Areia onde corre a porta do quarto ─────────────
#   ⭐ a porta é a MESMA do painel ripado do quarto (já contada lá): aqui
#   entra só o painel do lado do closet e a face Areia da folha.
#   ⭐ [Jonathan, 04/11/2026] "faremos ambas as portas": só as folhas; o
#   painel do lado do closet não entra (a porta já está no Quarto casal).

# ── Fechamento superior em Areia (faixa de 10 no perímetro) ──────────────
m = 'Fechamento superior'
P(m, 'Faixa de fechamento', 157, 10, 4, 'Areia 18', 1.57)
O(m, 'Perfil de proteção de piso', 6.30, 'm', 15)
