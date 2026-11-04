# -*- coding: utf-8 -*-
"""Circulação · bar · folhas 24 e 25 (PDF p. 26–27). MDF marrom, no nicho
de alvenaria de 116 × 250 × 58. ⛔ Fundo em mármore Michelangelo e o tampo
de 3 cm (pedra no render) ficam FORA."""
from motor import *

ambiente('Circulação · bar')
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
