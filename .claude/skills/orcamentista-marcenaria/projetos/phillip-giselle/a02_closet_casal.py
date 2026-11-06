# -*- coding: utf-8 -*-
"""Closet Casal · folhas 09 e 10 (PDF p. 11–12). MDF Areia por dentro e por
fora, do piso ao forro (270), em U. Cantos da sapateira = canto morto."""
from motor import *

ambiente('Closet casal')
A = 'Areia 15'

# ── Armário parede D · 213 × 270 × 54 · 3 módulos de 71 ─────────────────
m = 'Armário parede D'
caixa(m, 213, 270, 54, 'Areia', interno=A, fundo='Areia 6')
divisorias(m, 2, 267, 54, A)
prateleiras(m, 6, 69, 54, A)                   # 3 maleiros + 3 prateleiras
cabideiro(m, 69); cabideiro(m, 69)
gavetas(m, 7, 67, 18, 50, 'Areia')             # gavetas internas, módulo central
#   ⛔ [Jonathan, 06/11/2026] "CLOSET DE CASAL: tire todas as portas" — saem
#     as 3 folhas de correr de 71, o SS150 de 3 portas, o trilho de 3 m, os
#     6 desempenadores e as 3 cavas.

# ── Armário parede B · 144 × 270 × 54 · 2 módulos de 72 ─────────────────
m = 'Armário parede B'
caixa(m, 144, 270, 54, 'Areia', interno=A, fundo='Areia 6')
divisorias(m, 1, 267, 54, A)
prateleiras(m, 4, 70, 54, A)                   # 2 maleiros + 2 prateleiras
cabideiro(m, 70); cabideiro(m, 70)
gavetas(m, 4, 68, 20, 50, 'Areia')
#   ⛔ [Jonathan, 06/11/2026] sem portas: saem as 2 folhas de 72, o SS150,
#     o trilho, os desempenadores e as 2 cavas.

# ── A porta entre o closet e o banho ─────────────────────────────────────
#   ⛔⛔ DUPLICATA REMOVIDA na revisão de 04/11/2026: a "porta de giro em MDF
#   Areia com cava 45°" da parede B do closet (70 × 210) é a MESMA porta da
#   vista D do banho (72 × 212) — o banho do casal só tem essa entrada, pela
#   planta geral. Ela é a "porta do banho" lançada no Quarto casal (ripada,
#   pivô, por decisão do Jonathan). Aqui fica só a bandeira acima dela.

# ── Sapateira parede C · 136 × 270 × 43 · portas de correr com espelho ──
m = 'Sapateira com espelho'
caixa(m, 136, 270, 41, 'Areia', interno=A, fundo='Areia 6')
divisorias(m, 1, 267, 41, A)
prateleiras(m, 12, 66, 41, A)
#   ⛔ [Jonathan, 06/11/2026] as duas portas de espelho SAEM daqui e vão para
#     uma linha própria, no fim deste arquivo.

# ── Parede A · painel em Areia onde corre a porta do quarto ─────────────
#   ⭐ a porta é a MESMA do painel ripado do quarto (já contada lá): aqui
#   entra só o painel do lado do closet e a face Areia da folha.
#   ⭐ [Jonathan, 04/11/2026] "faremos ambas as portas": só as folhas; o
#   painel do lado do closet não entra (a porta já está no Quarto casal).

# ── Fechamento superior em Areia (faixa de 10 no perímetro) ──────────────
m = 'Fechamento superior'
P(m, 'Faixa de fechamento', 157, 10, 4, 'Areia 18', 1.57)
P(m, 'Bandeira acima da porta do banho', 60, 70, 1, 'Areia 18', 2 * (60 + 70) / 100)
O(m, 'Perfil de proteção de piso', 6.30, 'm', 15)

# ── ⭐ LINHA PRÓPRIA: só as portas de espelho [Jonathan, 06/11/2026] ─────
#   "apresente SEPARADO o investimento para colocar só as portas de espelho
#   no closet de casal — linha própria, não embutida no conjunto". São as
#   duas folhas de correr da sapateira (66 e 70 × 268), em Areia 18 com
#   espelho prata colado, no SS150 de 2 portas com trilho e desempenador.
#   ⭐⭐ [Jonathan, 06/11/2026] "as portas de espelho do closet serão de GIRO
#   (com dobradiça)": saem o SS150, o trilho e os desempenadores. As duas
#   folhas dividem o vão de 136 (67,8 cada), em Areia 18 com espelho prata
#   colado, cinco dobradiças por folha (passa de 200 de altura) e cava
#   usinada na borda. ⚠ A cava é minha: a prancha não desenha puxador.
ambiente('Closet casal · portas de espelho')
m = 'Portas de giro com espelho na sapateira'
portas(m, 2, 67.8, 268, 'Areia')
O(m, 'Espelho prata colado na porta', 2 * 0.678 * 2.68, 'm²', 600)
O(m, 'Cava 45° usinada', 2, 'frente', 50)
