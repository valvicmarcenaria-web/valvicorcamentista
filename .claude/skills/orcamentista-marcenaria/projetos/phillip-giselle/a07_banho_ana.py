# -*- coding: utf-8 -*-
"""Banho Ana · folhas 19 e 20 (PDF p. 21–22). MDF liso Tartufo."""
from motor import *

ambiente('Banho Ana')

# ── 1 · Gabinete suspenso sob a bancada · 162 × 57 × 50 ─────────────────
#   ⛔ o tampo de marmoraria e a cuba: fora.
m = 'Gabinete suspenso'
caixa(m, 162, 57, 48, 'Tartufo', interno='Tartufo 15', lat_vistas=2, base_vista=True)
divisorias(m, 1, 54, 48, 'Tartufo 15')
prateleiras(m, 2, 78, 48, 'Tartufo 18')
portas(m, 4, 40.5, 57, 'Tartufo')
O(m, 'Cava 45° usinada', 4, 'frente', 50, '⚠ prancha não indica puxador')

# ── 2 · Perfumaria com portas de espelho · 162 × 82 × 30 ────────────────
#   ⚠ profundidade 30 lida da planta (tracejado); caixa sem material escrito.
m = 'Perfumaria de espelho'
caixa(m, 162, 82, 28, 'Tartufo', interno='Tartufo 15', lat_vistas=2, base_vista=True)
divisorias(m, 1, 79, 28, 'Tartufo 15')
prateleiras(m, 4, 78, 28, 'Tartufo 15')
portas(m, 4, 40.5, 82, 'Tartufo')
O(m, 'Espelho prata colado na porta', 4 * 0.405 * 0.82, 'm²', 600)
led(m, 1.62 + 2 * 0.82, 'sob o armário + 2 frestas verticais')

# ⛔ CRISTALEIRA DE VIDRO (torre de perfumes, 50 × 29 × 270): perfil metálico
#   e vidro, SEM PREÇO na Base. Fica fora do total, como pergunta.
