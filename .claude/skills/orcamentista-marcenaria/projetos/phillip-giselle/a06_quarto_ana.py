# -*- coding: utf-8 -*-
"""Suíte Ana · folhas 17 e 18 (PDF p. 19–20). MDF branco liso (Branco TX)."""
from motor import *

ambiente('Suíte Ana')

# ── 1 · Nichos de prateleiras + banco de janela com gavetões (vista B) ──
#   330 de parede a parede = torre 50 + banco 230 + torre 50; 270 de altura;
#   57 de profundidade. Gavetões 55 de altura, prof. 53.
m = 'Móvel da janela (nichos, banco e gavetões)'
for i in range(2):
    caixa(m, 50, 205, 57)                      # torre acima do banco
    prateleiras(m, 4, 46, 57)
P(m, 'Tampo do banco 5 cm (duas camadas, emenda)', 165, 57, 4, 'Branco TX 18',
  (165 + 57) / 100 / 2, 'cor30')
P(m, 'Travessa sobre a janela', 230, 15, 2, 'Branco TX 18', 2.30)
P(m, 'Banco · lateral', 55, 53, 2, 'Branco TX 15', 1.08)
divisorias(m, 4, 55, 53)
P(m, 'Banco · base (emenda)', 165, 53, 2, 'Branco TX 15', 1.65)
P(m, 'Banco · fundo', 165, 55, 2, 'Branco TX 6')
gavetas(m, 2, 48, 55, 50, 'Branco TX')
gavetas(m, 3, 76.7, 55, 50, 'Branco TX')
O(m, 'Puxador (a definir)', 5, 'un', 50, '⚠ render mostra barra; usei preço de cava')
O(m, 'Perfil de proteção de piso', 3.30, 'm', 15)

# ⛔ MESA DE ESTUDO E MESINHAS FORA [Jonathan, 04/11/2026]: "na suíte da Ana
#   considere apenas o móvel na janela".

# ── 4 · Painel em toda a parede da vista A com 3 portas pivotantes ──────
#   ⭐ [Jonathan, 04/11/2026] "teremos um painel em toda extensão da parede
#   com 3 portas pivotantes mimetizadas · não está no projeto, mas precisa
#   constar assim como o painel do corredor" → material de cor.
#   Parede: 15 + 80 + 86 + 70 + 211 = 462 × 270 (o resto é o nicho).
#   Portas de 80 e 70 cotadas; ⚠ a terceira não existe no desenho: 70.
import math
m = 'Painel com 3 portas mimetizadas'   # ⭐ item próprio [Jonathan 04/11]
PORTAS = [80, 70, 70]
L_liq = 462 - sum(PORTAS)
n = math.ceil(L_liq / 120)
P(m, 'Painel de parede', 270, L_liq / n, n, 'Cor 18', 2 * 2.70)
for L in PORTAS:
    P(m, 'Bandeira sobre a porta', 58, L, 1, 'Cor 18', 2 * (58 + L) / 100)
P(m, 'Travessa de estrutura', 154, 10, 9, 'Branco TX 15', 0)
for L in PORTAS:
    porta_passagem(m, L, 212, 'Cor', sistema='pivo')
O(m, 'Perfil de proteção de piso', L_liq / 100, 'm', 15)
