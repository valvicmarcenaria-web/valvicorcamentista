# -*- coding: utf-8 -*-
"""Closet Mateus (o banho saiu [Jonathan, 04/11/2026]) · folhas 15 e 16 (PDF p. 17–18). MDF Grafite.
⛔ Bancada em mármore branco Paraná e cuba: fora."""
from motor import *

ambiente('Closet Mateus')
G = 'Grafite'

# ── Armário do closet · 158 × 270 × 54 · módulos 48 (aberto) | 54 | 54 ──
m = 'Armário do closet'
caixa(m, 158, 270, 54, G, interno=f'{G} 15', fundo=f'{G} 6', lat_vistas=1)
divisorias(m, 2, 267, 54, f'{G} 15')
prateleiras(m, 4, 48, 54, f'{G} 15')           # módulo aberto: maleiro + 3
prateleiras(m, 6, 54, 54, f'{G} 15')           # maleiro + 4 · maleiro
cabideiro(m, 48); cabideiro(m, 54)
gavetas(m, 5, 54, 20, 50, G)
correr(m, [54, 54], 268, G)
O(m, 'Perfil de proteção de piso', 1.58, 'm', 15)

