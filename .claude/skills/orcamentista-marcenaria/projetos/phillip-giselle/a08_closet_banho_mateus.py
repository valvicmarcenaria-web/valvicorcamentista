# -*- coding: utf-8 -*-
"""Closet e Banho Mateus · folhas 15 e 16 (PDF p. 17–18). MDF Grafite.
⛔ Bancada em mármore branco Paraná e cuba: fora."""
from motor import *

ambiente('Closet e banho Mateus')
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

# ── Cristaleira em Grafite com fechamento em vidro · 29 × 270 × 44 ──────
m = 'Cristaleira'
caixa(m, 29, 270, 44, G, interno=f'{G} 15', fundo=f'{G} 6', lat_vistas=2)
prateleiras(m, 7, 25, 44, f'{G} 15')
O(m, 'Porta de perfil de alumínio com vidro', 0.29 * 2.68, 'm²', 700,
  '⚠ referência da Base: porta de espelho em alumínio · vidro sem preço')

# ── Armário superior com portas de espelho · 164 × 80 × 13 ──────────────
m = 'Armário de espelho'
caixa(m, 164, 80, 11, G, interno=f'{G} 15', lat_vistas=2, base_vista=True)
divisorias(m, 1, 77, 11, f'{G} 15')
prateleiras(m, 4, 80, 11, f'{G} 15')
portas(m, 2, 42, 80, G); portas(m, 2, 40, 80, G)
O(m, 'Espelho prata colado na porta', 1.64 * 0.80, 'm²', 600)
led(m, 1.64 + 2 * 0.80, 'sob o armário + 2 frestas · sem tabela na prancha')

# ── Armário sob bancada · 164 × 58 × 44, suspenso ───────────────────────
m = 'Gabinete suspenso'
caixa(m, 164, 58, 44, G, interno=f'{G} 15', lat_vistas=2, base_vista=True)
divisorias(m, 1, 55, 44, f'{G} 15')
prateleiras(m, 2, 80, 44, f'{G} 18')
portas(m, 2, 42, 58, G); portas(m, 2, 40, 58, G)
O(m, 'Cava 45° usinada', 4, 'frente', 50, '⚠ puxador não especificado')
