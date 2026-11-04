# -*- coding: utf-8 -*-
"""JÚNIA PORTUGAL · Banho suíte · Ocapi Arquitetura (Dalila Souza)
Detalhamento R00 — VERSÃO PARA ORÇAMENTO (o arquivo diz "banho social", as
folhas dizem "banho suíte"; a apresentação é a do banho suíte).
⛔ Fora: bancada em mármore branco extra, nicho em porcelanato, box, cuba,
   metais, espelho "modelo a definir", porta e alizar pintados.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from motor_lev import *

ambiente('Banho suíte')
#   Armário sob a bancada · 65 × 61 × 38, suspenso a 25 do piso:
#   externamente MDF a definir (cor) e internamente MDF branco · 2 portas de
#   abrir com puxador cava (detalhe) · 1 prateleira · faixa de 10 no topo.
#   ⚠ largura e profundidade medidas na escala 1:25 (65 e 38).
m = 'Gabinete suspenso sob a bancada'
caixa(m, 65, 61, 38, 'Cor', lat_vistas=1, base_vista=True)
prateleiras(m, 1, 62, 38)
portas(m, 2, 32.5, 51, 'Cor')
P(m, 'Faixa superior', 65, 10, 1, 'Cor 15', 2 * (65 + 10) / 100)
O(m, 'Cava usinada (detalhe puxador cava)', 2, 'frente', 50)
