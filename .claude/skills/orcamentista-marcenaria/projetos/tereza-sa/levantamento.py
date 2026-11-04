# -*- coding: utf-8 -*-
"""TEREZA SÁ · Apartamento Tomé de Souza · Ocapi Arquitetura (Dalila Souza)
Detalhamento R00 de 29/10/2026 — PROJETO PARA ORÇAMENTO.
⛔ Fora: bancada e nicho em super nano glass (pedra), box, louças, metais,
   prateleiras de vidro existentes, persiana, escrivaninha e cadeiras "a
   definir", boiseries pintados, banho social (só tem render, sem detalhamento).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from motor_lev import *
C = 'Cor'          # "acabamento a definir" → padrão de cor 700/550/350

# ═══ ESCRITÓRIO · armário baixo (folhas 01, 03, 04) ═══════════════════════
#   130 × 64 × 40: caixa 52 + tampo 2,5 + base 2,5 + rodapé 7 recuado 5 cm.
#   2 portas de correr 43,33 × 52 · 2 gavetões 43,33 × 28,5 · 2 prateleiras
#   internas (vão 81,67) · externa e internamente no acabamento.
ambiente('Escritório')
m = 'Armário baixo com portas de correr e gavetões'
caixa(m, 130, 57, 40, C, interno=f'{C} 15', fundo=f'{C} 6', lat_vistas=2, teto_visto=True)
divisorias(m, 1, 54, 40, f'{C} 15')
prateleiras(m, 2, 82, 40, f'{C} 18')
for L in (43.33, 43.33):
    P(m, 'Porta de correr', 52, L, 1, f'{C} 15', 2 * (L + 52) / 100)
O(m, 'Kit de correr RO65 Rometal, 1 porta', 2, 'cj', 100)
O(m, 'Trilho RO65 Rometal 2 m', 1, 'un', 100)
gavetas(m, 2, 43.33, 28.5, 37, C)
P(m, 'Rodapé recuado (h 7)', 7, 120, 1, f'{C} 15', 1.20)
P(m, 'Rodapé recuado · lateral', 7, 30, 2, f'{C} 15', 0.30)
O(m, 'Puxador (a definir)', 4, 'un', 50, '⚠ a definir: usei o preço da cava')

# ═══ BANHO SUÍTE (folhas 01 a 05) ═════════════════════════════════════════
ambiente('Banho suíte')
#   Armário superior 165 × 133 × 15 · portas de correr com ESPELHO e trilho
#   oculto · perfil de LED embutido · puxador passante · 3 prateleiras.
m = 'Armário superior com portas de espelho'
caixa(m, 165, 133, 15, C, interno=f'{C} 15', fundo=f'{C} 6', lat_vistas=2, base_vista=True)
prateleiras(m, 3, 160, 13, f'{C} 18')
for L in (82.5, 82.5):
    P(m, 'Porta de correr (base do espelho)', 133, L, 1, f'{C} 15', 2 * (L + 133) / 100)
    O(m, 'Desempenador de porta', 2, 'un', 100)
O(m, 'Espelho prata colado na porta', 2 * 0.825 * 1.33, 'm²', 600)
O(m, 'Sistema de correr Multi Rometal (suspenso, trilho oculto)', 1, 'cj', 500,
  '⚠ a confirmar na Base')
led(m, 1.65, 'perfil de LED embutido sob o armário')
O(m, 'Perfil puxador passante', 2 * 1.33, 'm', 100)

#   Armário inferior suspenso 165 × 63 × 52 (bancada de 54,5) a 20 do piso:
#   3 portas de abrir 35 × 63 · 2 gavetões 60 × 31,5 · prateleiras.
m = 'Gabinete suspenso com portas e gavetões'
caixa(m, 165, 63, 52, C, interno=f'{C} 15', fundo=f'{C} 6', lat_vistas=2, base_vista=True)
divisorias(m, 2, 60, 52, f'{C} 15')
prateleiras(m, 2, 50, 52, f'{C} 15')
portas(m, 3, 35, 63, C)
gavetas(m, 2, 60, 31.5, 48, C)
O(m, 'Puxador (a definir)', 5, 'un', 50, '⚠ a definir: usei o preço da cava')
