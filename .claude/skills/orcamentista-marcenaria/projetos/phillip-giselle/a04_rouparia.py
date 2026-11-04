# -*- coding: utf-8 -*-
"""Rouparia · folha 23 (PDF p. 25). MDF branco liso, do piso ao forro, em L."""
from motor import *

ambiente('Rouparia')

m = 'Armário parede A (174 × 270 × 45)'
caixa(m, 174, 270, 45, 'Branco TX', lat_vistas=1)
prateleiras(m, 5, 171, 45, 'Branco TX 18')     # corridas, com alma de aço
correr(m, [59, 57, 57][:2], 268, 'Branco TX')
P(m, 'Porta de correr', 268, 57, 1, 'Branco TX 18', 2 * (57 + 268) / 100)
O(m, 'Desempenador de porta', 1, 'un', 100)
O(m, 'Acréscimo SS150 de 2 para 3 portas', 1, 'cj', 100)
O(m, 'Cava 45° usinada', 3, 'frente', 50, '⚠ puxador não especificado')

m = 'Armário parede B (121 × 270 × 70)'
caixa(m, 121, 270, 70, 'Branco TX', lat_vistas=1)
divisorias(m, 1, 267, 70)
prateleiras(m, 5, 76, 70, 'Branco TX 18')
correr(m, [38, 38], 268, 'Branco TX')
P(m, 'Painel fixo de canto', 268, 45, 1, 'Branco TX 18', 2 * (268 + 45) / 100)
O(m, 'Cava 45° usinada', 2, 'frente', 50)
O(m, 'Perfil de proteção de piso', 2.95, 'm', 15)
