# -*- coding: utf-8 -*-
"""Banho Casal · folhas 11 e 12 (PDF p. 13–14). Tudo em MDF Tartufo."""
from motor import *

ambiente('Banho casal')

# ── 1 · Gabinete suspenso sob a bancada · 184 × 62 × 46 ─────────────────
#   ⛔ a bancada em mármore Michelangelo e as cubas são marmoraria: fora.
m = 'Gabinete suspenso'
caixa(m, 184, 62, 44, 'Tartufo', interno='Tartufo 15', lat_vistas=2, base_vista=True)
divisorias(m, 1, 59, 44, 'Tartufo 15')
prateleiras(m, 2, 89, 44, 'Tartufo 18')
portas(m, 4, 46, 62, 'Tartufo')
O(m, 'Cava 45° usinada', 4, 'frente', 50, '⚠ prancha não indica puxador')

# ── 2 · Armário superior com portas de espelho · 182 × 60 × 13 ─────────
m = 'Armário de espelho'
caixa(m, 182, 60, 11, 'Tartufo', interno='Tartufo 15', lat_vistas=2, base_vista=True)
divisorias(m, 1, 57, 11, 'Tartufo 15')
prateleiras(m, 4, 89, 11, 'Tartufo 15')
portas(m, 4, 45.5, 60, 'Tartufo')
O(m, 'Espelho prata colado na porta', 4 * 0.455 * 0.60, 'm²', 600)
led(m, 1.82 + 3 * 0.60, 'sob o armário 1,82 m + 3 frestas verticais ⚠ tabela só traz 1,82')

# ── 3 · Porta de giro de entrada em MDF Areia, cava 45° · 72 × 212 ──────
#   ⭐ folha feita na casa (método da porta de passagem), sistema pivô.
m = 'Porta do banho em MDF Areia'
porta_passagem(m, 72, 212, 'Areia', sistema='pivo')
