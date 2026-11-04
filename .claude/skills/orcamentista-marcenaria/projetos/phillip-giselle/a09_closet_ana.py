# -*- coding: utf-8 -*-
"""Closet Ana · folhas 21 e 22 (PDF p. 23–24). Armário em L, MDF liso Tartufo
por dentro e por fora, do piso ao forro (270). Canto do L = canto morto."""
from motor import *

ambiente('Closet Ana')
T = 'Tartufo 15'

# ── Ala D · 159 × 270 × 54 · módulos 55 | 55 | 50 (canto) ────────────────
m = 'Armário em L · ala D'
caixa(m, 159, 270, 54, 'Tartufo', interno=T, fundo='Tartufo 6', lat_vistas=1)
divisorias(m, 2, 267, 54, T)
prateleiras(m, 8, 55, 54, 'Tartufo 15')        # 2 × (maleiro + 3)
cabideiro(m, 55); cabideiro(m, 55)
correr(m, [55, 53], 268, 'Tartufo')
P(m, 'Painel fixo de canto', 268, 52, 1, 'Tartufo 18', 2 * (268 + 52) / 100)
O(m, 'Perfil puxador vertical', 2 * 1.50, 'm', 100, 'SP7000 · ⚠ sem especificação')

# ── Ala A · 151 × 270 × 50 · módulos 54 (canto) | 48 | 48 ────────────────
m = 'Armário em L · ala A'
caixa(m, 151, 270, 50, 'Tartufo', interno=T, fundo='Tartufo 6', lat_vistas=1)
divisorias(m, 2, 267, 50, T)
prateleiras(m, 6, 48, 50, 'Tartufo 15')        # maleiro + 4 · maleiro do cabide
cabideiro(m, 48)
gavetas(m, 5, 48, 18, 45, 'Tartufo')           # gavetas internas
correr(m, [46, 48], 268, 'Tartufo')
P(m, 'Painel fixo de canto', 268, 56, 1, 'Tartufo 18', 2 * (268 + 56) / 100)
O(m, 'Perfil puxador vertical', 2 * 1.50, 'm', 100, 'SP7000 · ⚠ sem especificação')
O(m, 'Perfil de proteção de piso', 3.10, 'm', 15)

# ⛔ PERFUMARIA / CRISTALEIRA DE VIDRO (50 × 29 × 267): vidraçaria, sem preço
#   na Base. Fora do total, como pergunta.
