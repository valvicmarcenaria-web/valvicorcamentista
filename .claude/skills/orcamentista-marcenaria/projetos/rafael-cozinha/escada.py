# -*- coding: utf-8 -*-
"""RAFAEL · Cozinha — duas versões e a escala de desconto padrão da casa.

  V1 · Telescópica (Silver, 2 anos) ........ MC 33%  ⛔ abaixo do piso de 35%, decisão declarada [Jonathan, 04/11/2026]
  V2 · Oculta Hettich (Gold, 10 anos) ...... MC 38%  [Jonathan, 04/11/2026]
Sem RT, sem vendedor [Jonathan, 04/11/2026].

Escala padrão (proposta-comercial.md):
  30% entrada + 10× cartão ........ valor cheio
  50% entrada +  8× cartão ........ −3%
  70% entrada +  6× cartão ........ −5%
  70% entrada + transferência ..... −7%

⛔ Cada degrau tem a SUA base: o cartão (1,2% por parcela) incide só sobre o
   saldo parcelado. ⭐ A MC-alvo é cravada no PIOR degrau para a casa, de modo
   que nenhuma condição da escala fique abaixo do alvo pedido.
"""
import os, runpy, math, pathlib
import sys; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import motor_mc as M

AQUI = pathlib.Path(__file__).parent
ESCALA = [('Entrada 30% + saldo em até 10× no cartão', 0.30, 10, 0.00),
          ('Entrada 50% + saldo em até 8× no cartão',  0.50,  8, 0.03),
          ('Entrada 70% + saldo em até 6× no cartão',  0.70,  6, 0.05),
          ('Entrada 70% + saldo por transferência',    0.70,  0, 0.07)]

def base(entrada, parc):
    cartao = M.CARTAO_PP * parc * (1 - entrada)          # sobre o bruto
    bruto1 = M.NF + cartao + M.ERRO + M.SERRA + M.MANUT
    liquido = 1 - M.NF - cartao                           # sem RT, sem vendedor
    return 1 - bruto1 - M.PROD * liquido

def cd(linha):
    os.environ['LINHA'] = linha
    return runpy.run_path(str(AQUI / 'levantamento.py'), run_name='lib')['CD']

def brl(v): return f'R$ {v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')

def versao(nome, linha, alvo):
    C = cd(linha)
    # valor cheio que deixa o pior degrau exatamente no alvo, arredondado p/ cima em R$ 100
    cheio = max(C / ((base(e, n) - alvo) * (1 - d)) for _, e, n, d in ESCALA)
    cheio = math.ceil(cheio / 100) * 100
    print(f'\n{nome} · custo direto {brl(C)} · alvo MC {alvo*100:.0f}%')
    linhas = []
    for lab, e, n, d in ESCALA:
        p = cheio * (1 - d)
        mc = base(e, n) - C / p
        linhas.append((lab, d, p, mc))
        print(f'  {lab:44s} {"—" if d == 0 else f"−{d*100:.0f}%":>4s} {brl(p):>14s}  MC {mc*100:5.1f}%')
    return C, cheio, linhas

if __name__ == '__main__':
    v1 = versao('V1 · TELESCÓPICA (Silver · 2 anos)', 'silver', 0.33)
    v2 = versao('V2 · OCULTA HETTICH (Gold · 10 anos)', 'gold', 0.38)
