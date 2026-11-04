# -*- coding: utf-8 -*-
"""Quarto Mateus · folhas 13 e 14 (PDF p. 15–16). MDF Grafite."""
from motor import *

ambiente('Quarto Mateus')
G = 'Grafite'

# ── Mesa para computador · 205 × 80 × 60, gaveteiro de 3 à esquerda ─────
m = 'Mesa do computador'
P(m, 'Tampo', 205, 60, 1, f'{G} 18', 2 * (205 + 60) / 100)
P(m, 'Lateral do gaveteiro', 78, 58, 2, f'{G} 15', 2 * (78 + 58) / 100)
P(m, 'Gaveteiro · base e fundo', 48, 58, 2, 'Branco TX 15', 0.48)
gavetas(m, 3, 48, 25, 50, G)

# ── Prateleiras sobre a mesa · 2 × 209 × 25 ─────────────────────────────
m = 'Prateleiras suspensas'
P(m, 'Prateleira', 209, 25, 2, f'{G} 18', 2 * (209 + 25) / 100)
O(m, 'Suporte oculto de prateleira', 12, 'un', 30)
O(m, 'Alma de aço barra chata 5 mm', 2, 'barra', 50)

# ── Cabeceira · 415 × 120, LED no topo ──────────────────────────────────
m = 'Cabeceira'
P(m, 'Painel (2, emenda)', 207.5, 120, 2, f'{G} 18', 2 * (207.5 + 120) / 100)
P(m, 'Travessa de fixação', 207.5, 10, 6, 'Branco TX 15', 0)
led(m, 4.15, 'tabela: LED em marcenaria 4,15 m')
O(m, 'Perfil de proteção de piso', 4.15, 'm', 15)

# ── Mesas de cabeceira · 30 × 40 × 30 e 105 × 40 × 32 ───────────────────
#   ⚠ "base em MDF marmorizado à definir": lançada em Grafite até definir.
m = 'Mesas de cabeceira'
caixa(m, 30, 40, 30, G, interno=f'{G} 15', lat_vistas=2, teto_visto=True, fundo=False)
caixa(m, 105, 40, 32, G, interno=f'{G} 15', lat_vistas=2, teto_visto=True, fundo=False)
divisorias(m, 2, 37, 32, f'{G} 15')

# ── Painel de parede em Grafite + porta de giro oculta (vista C) ────────
#   415 × 270, junta horizontal a 215. Porta de 58 no mesmo MDF.
m = 'Painel com porta oculta'
P(m, 'Painel inferior', 215, 89.5, 4, f'{G} 18', 2 * 2.15)
P(m, 'Faixa superior (55)', 207.5, 55, 2, f'{G} 18', 2.075)
P(m, 'Travessa de estrutura', 207.5, 10, 6, 'Branco TX 15', 0)
porta_passagem(m, 58, 212, G, sistema='pivo')
O(m, 'Perfil de proteção de piso', 4.15, 'm', 15)
# ⛔ estante em metal preto (96 × 270, 6 prateleiras): pergunta, fora do total.
