# -*- coding: utf-8 -*-
"""Closet Ana · folhas 21 e 22 (PDF p. 23–24). Armário em L, MDF liso Tartufo
por dentro e por fora, do piso ao forro (270). Canto do L = canto morto."""
from motor import *

def closet_L(amb, COR):
    ambiente(amb)
    T = f'{COR} 15'

    # ── Ala D · 159 × 270 × 54 · módulos 55 | 55 | 50 (canto) ────────────────
    m = 'Armário em L · ala D'
    caixa(m, 159, 270, 54, COR, interno=T, fundo=f'{COR} 6', lat_vistas=1)
    divisorias(m, 2, 267, 54, T)
    prateleiras(m, 8, 55, 54, f'{COR} 15')        # 2 × (maleiro + 3)
    cabideiro(m, 55); cabideiro(m, 55)
    #   ⛔ [Jonathan, 06/11/2026] "CLOSET ANA E MATEUS: tire as portas também"
    #     — saem as folhas de correr, o SS150, o trilho, os desempenadores e o
    #     perfil puxador. ⚠ O painel fixo de canto FICA: fecha o canto morto.
    P(m, 'Painel fixo de canto', 268, 52, 1, f'{COR} 18', 2 * (268 + 52) / 100)

    # ── Ala A · 151 × 270 × 50 · módulos 54 (canto) | 48 | 48 ────────────────
    m = 'Armário em L · ala A'
    caixa(m, 151, 270, 50, COR, interno=T, fundo=f'{COR} 6', lat_vistas=1)
    divisorias(m, 2, 267, 50, T)
    prateleiras(m, 6, 48, 50, f'{COR} 15')        # maleiro + 4 · maleiro do cabide
    cabideiro(m, 48)
    gavetas(m, 5, 48, 18, 45, COR)           # gavetas internas
    #   ⛔ [Jonathan, 06/11/2026] sem portas, como na ala D
    P(m, 'Painel fixo de canto', 268, 56, 1, f'{COR} 18', 2 * (268 + 56) / 100)
    O(m, 'Perfil de proteção de piso', 3.10, 'm', 15)

    # ⛔ PERFUMARIA / CRISTALEIRA DE VIDRO (50 × 29 × 267): vidraçaria, sem preço
    #   na Base. Fora do total, como pergunta.


closet_L('Closet Ana', 'Tartufo')
