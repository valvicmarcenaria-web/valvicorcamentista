# -*- coding: utf-8 -*-
"""Circulação · bar · folhas 24 e 25 (PDF p. 26–27). MDF marrom, no nicho
de alvenaria de 116 × 250 × 58. ⛔ Fundo em mármore Michelangelo e o tampo
de 3 cm (pedra no render) ficam FORA."""
from motor import *
import math

ambiente('Circulação')
M_ = 'Marrom'

m = 'Bar embutido'
P(m, 'Forro lateral do nicho', 250, 58, 2, f'{M_} 15', 2.50)
P(m, 'Forro do topo', 116, 58, 1, f'{M_} 15', 1.16)
caixa(m, 116, 82, 45, M_, interno='Branco TX 15', lat_vistas=0)
divisorias(m, 1, 79, 45)
prateleiras(m, 2, 56, 45)
portas(m, 4, 57, 41, M_)
O(m, 'Cava 45° usinada', 4, 'frente', 50, '⚠ 4 portas ou 2 gavetas + 2 portas?')
P(m, 'Prateleira do nicho', 116, 45, 3, f'{M_} 18', 1.16)
O(m, 'Suporte oculto de prateleira', 9, 'un', 30)
led(m, 4.40, 'tabela: LED em marcenaria 4,40 m')


# ── Painel em toda a extensão com 4 portas pivotantes mimetizadas ───────
#   ⭐ [Jonathan, 04/11/2026] "teremos um painel em toda extensão com as 4
#   portas pivotantes mimetizadas" (folha 24, vistas A e B · folha 25, C).
#   Paredes: B 953 + A 247 + C 142 (fora o bar) = 1342 × 250 de altura,
#   menos 4 vãos de 80; bandeira de 38 sobre cada porta.
#   ⚠ cor do painel não especificada: lançado em Branco TX.
m = 'Painel com 4 portas mimetizadas'
PAN = 'Branco TX'
L_liq = 1342 - 4 * 80
n = math.ceil(L_liq / 120)
P(m, 'Painel de parede', 250, L_liq / n, n, f'{PAN} 18', 2 * 2.50)
P(m, 'Bandeira sobre a porta', 38, 80, 4, f'{PAN} 18', 2 * (38 + 80) / 100)
P(m, 'Travessa de estrutura', 1342 / 6, 10, 18, 'Branco TX 15', 0)
for i in range(4):
    porta_passagem(m, 80, 212, PAN, sistema='pivo',
                   extra=[('Fecho rolete para porta pivotante', 1, 'un', 75)])
O(m, 'Perfil de proteção de piso', L_liq / 100, 'm', 15)
