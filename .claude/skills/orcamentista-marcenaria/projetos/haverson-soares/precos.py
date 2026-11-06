# -*- coding: utf-8 -*-
"""HAVERSON SOARES — o preço, ambiente por ambiente  [06/11/2026]

⭐ O custo direto sai de `planilha.py` (peça por peça do `levantamento.py`), com
   os preços da Base de 06/11/2026 — é o que a planilha tem de mostrar depois
   que o IMPORTRANGE for autorizado.
⭐ A cascata é a da aba "Preço e Comissões" com os padrões da casa:
   nota 5%, margem de erro 2%, serra 0,5%, manutenção 0,5%, RT de 10% sobre o
   líquido (⚠ a confirmar com a Luiza Pacheco), sem vendedor, sem cartão, e
   produção 7,5% sobre o líquido 2.
⚠ A MC ainda não foi escolhida: a planilha está em 38%, e aqui saem 35, 38 e 40.
"""
import io, contextlib, sys, pathlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P)); sys.path.insert(0, str(P.parent))
with contextlib.redirect_stdout(io.StringIO()):
    import planilha as PL

NF, ERRO, SERRA, MANUT, RT, VEND = 0.05, 0.02, 0.005, 0.005, 0.10, 0.0
LIQ = 1 - NF
COM = 0.075 * (LIQ - RT * LIQ - VEND * LIQ)
BASE = 1 - (NF + ERRO + SERRA + MANUT + RT * LIQ + VEND * LIQ + COM)
assert abs(BASE - 0.760875) < 1e-9, BASE
ORDEM = [a[0] for a in PL.ABAS]
CD = {a[0]: PL.monta(*a)['cd'] for a in PL.ABAS}
MCS = (0.35, 0.38, 0.40)
PV = {mc: {a: CD[a] / (BASE - mc) for a in ORDEM} for mc in MCS}

if __name__ == '__main__':
    print(f'base {BASE * 100:.4f}% · RT 10% · sem vendedor · margem de erro 2%')
    for a in ORDEM:
        print(f'{a:10s} CD {CD[a]:10,.2f} · ' + ' · '.join(f'MC {mc:.0%} {PV[mc][a]:10,.2f}' for mc in MCS))
    print(f'{"TOTAL":10s} CD {sum(CD.values()):10,.2f} · '
          + ' · '.join(f'MC {mc:.0%} {sum(PV[mc].values()):10,.2f}' for mc in MCS))
