# -*- coding: utf-8 -*-
"""Quarto Casal · folhas 07 e 08 (PDF p. 9–10)."""
from motor import *

ambiente('Quarto casal')

# ── 1 · Painel ripado amadeirado, parede do closet (vista C) ────────────
#   271 + 56 (vão do closet) + 112 = 439 × 270 (58 + 212). Ripa 2 × 2,
#   passo de 4 cm lido no desenho (⚠ conferir espaçamento com a arquiteta).
m = 'Painel ripado com porta oculta'
ripado(m, 383, 270, 'Amadeirado')              # parede cheia, fora o vão
ripado(m, 56, 58, 'Amadeirado')                # bandeira acima da porta
P(m, 'Folha da porta (base)', 215, 66, 1, 'Amadeirado 18', 2 * (66 + 215) / 100)
ripado(m, 66, 215, 'Amadeirado', base=False)   # ripas na face do quarto
O(m, 'Sistema de porta de correr c/ amortecimento (RO82 Top)', 1, 'cj', 600,
  '⚠ planta diz GIRO, vista diz CORRER')
O(m, 'Perfil de proteção de piso', 4.39, 'm', 15)

# ── 2 · Mesa rack em MDF areia (vista D) ─────────────────────────────────
#   78 + 78 + 78 + 80 = 314 × 20 de altura × 30 de profundidade, suspensa.
#   ⚠ As divisões de 78 lidas como GAVETAS (4). Tampo emenda: > 273.
m = 'Mesa rack suspensa'
P(m, 'Tampo (2 peças, emenda)', 157, 30, 2, 'Areia 18', 2 * (157 + 30) / 100)
P(m, 'Base', 157, 30, 2, 'Areia 15', 1.57)
P(m, 'Lateral', 20, 30, 2, 'Areia 15', 0.50)
divisorias(m, 3, 17, 30)
gavetas(m, 4, 78, 17, 28, 'Areia')
O(m, 'Suporte oculto (mão-francesa invisível)', 8, 'un', 30)

# ── 3 · Nichos em MDF amadeirado (vista D, canto) ───────────────────────
#   colunas de 17 + 17 + 20 com montantes de 2 → 60 × 260 × 15.
m = 'Torre de nichos'
P(m, 'Montante', 260, 15, 4, 'Amadeirado 18', 2.60 + 0.30)
P(m, 'Prateleira de nicho', 18, 15, 14, 'Amadeirado 18', 0.18)
P(m, 'Fundo', 260, 60, 1, 'Amadeirado 6')

# ── 4 · Espelho prata com LED nas laterais (vista D) ────────────────────
m = 'Espelho com LED'
P(m, 'Base do espelho', 250, 74, 1, 'Branco TX 15', 0)
O(m, 'Espelho prata colado', 0.74 * 2.50, 'm²', 600)
led(m, 5.40, 'tabela luminotécnica: LED em espelho 5,40 m')

# ── 5 · Cabeceira em MDF areia com LED no topo (vista B) ────────────────
m = 'Cabeceira'
P(m, 'Painel', 120, 96, 3, 'Areia 18', 2 * (120 + 96) / 100)
P(m, 'Painel', 120, 93, 1, 'Areia 18', 2 * (120 + 93) / 100)
P(m, 'Travessa de fixação (no lugar do sarrafo)', 381, 10, 3, 'Branco TX 15', 0)
led(m, 3.84, 'tabela luminotécnica: LED em marcenaria 3,84 m')
O(m, 'Perfil de proteção de piso', 3.81, 'm', 15)

# ── 6 · Mesinhas de cabeceira, 2 un (vista B, planta) ───────────────────
#   70 × 50 × 36, MDF areia, base em "madeira marmorizada" (⚠ a definir).
m = 'Mesinhas de cabeceira (2)'
P(m, 'Tampo', 70, 36, 2, 'Areia 18', 2 * (70 + 36) / 100)
P(m, 'Lateral', 42, 36, 4, 'Areia 15', 0.78)
P(m, 'Base', 67, 36, 2, 'Branco TX 15', 0.67)
P(m, 'Fundo', 67, 42, 2, 'Branco TX 6')
gavetas(m, 2, 70, 30, 34, 'Areia')
P(m, 'Base marmorizada (provisório em amadeirado)', 70, 8, 4, 'Amadeirado 18', 1.56)
P(m, 'Base marmorizada · lateral', 36, 8, 4, 'Amadeirado 18', 0.88)
