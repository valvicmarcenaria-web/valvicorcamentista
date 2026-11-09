# -*- coding: utf-8 -*-
"""ANA CAROLINA E ANDRÉ — o preço que a proposta mostra  [06/11/2026 · revisão 09/11/2026]

⭐ O custo direto sai de `planilha.py` (peça por peça do `levantamento.py`).
⭐ A cascata é a da aba "Preço e Comissões" COMO O JONATHAN A DEIXOU:
   margem de erro 1% (a casa usa 2%), RT de 10% sem vendedor, sem cartão,
   e MC de 40% sem acréscimo de dificuldade [Jonathan, 06/11/2026].
⛔ A conferência no fim trava o build se a conta daqui deixar de bater com
   o que a planilha mostra.
⭐⭐ [09/11/2026] REVISÃO DAS PRANCHAS DE 08/11: interior em Branco TX, exterior
   em Palha, par de portas em palha sintética no closet da suíte, dois
   calceiros Slow Sense, e entram o roupeiro da Suíte master e o armário do
   Quarto Isabella. ANTERIOR guarda os preços da proposta de 06/11.
"""
import io, contextlib, sys, pathlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P)); sys.path.insert(0, str(P.parent))
with contextlib.redirect_stdout(io.StringIO()):
    import planilha as PL

NF, ERRO, SERRA, MANUT, RT = 0.05, 0.01, 0.005, 0.005, 0.10
LIQ = 1 - NF                                   # sem cartão
RT_P = RT * LIQ
COM = 0.075 * (LIQ - RT_P)                      # produção, montagem, projeto, coordenação, gestão
BASE = 1 - (NF + ERRO + SERRA + MANUT + RT_P + COM)
MC = 0.40
ORDEM = [a[0] for a in PL.ABAS]
CD = {a[0]: PL.monta(*a)['cd'] for a in PL.ABAS}
PV = {a: CD[a] / (BASE - MC) for a in ORDEM}
# ⭐ na proposta, cada ambiente em real cheio; o total é a soma do que se lê
PV_R = {a: round(PV[a]) for a in ORDEM}
TOTAL = sum(PV_R.values())
# ⭐ "40% - 30% em 30 dias + 30% em 60 dias" [Jonathan, 06/11/2026]
PAGTO = [('Entrada, na assinatura do contrato', 0.40), ('30 dias após a assinatura', 0.30),
         ('60 dias após a assinatura', 0.30)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

# ⛔ o que a planilha mostra em 09/11/2026, depois da revisão das pranchas de 08/11
PLANILHA = {'Suíte master': 29062.98, 'Closet suíte master': 65767.14, 'Quarto Gabriel': 28131.39,
            'Closet Isabella': 45618.16, 'Quarto Isabella': 30883.75}
# a proposta de 06/11/2026, para a comparação (só três ambientes)
ANTERIOR = {'Closet suíte master': 53022, 'Quarto Gabriel': 29848, 'Closet Isabella': 49332}
assert abs(BASE - 0.770875) < 1e-9, BASE
for a in ORDEM:
    assert abs(PV[a] - PLANILHA[a]) < 0.01, (a, PV[a], PLANILHA[a])

if __name__ == '__main__':
    print(f'base {BASE*100:.4f}% · MC {MC*100:.0f}%')
    for a in ORDEM: print(f'{a:22s} CD {CD[a]:10,.2f} · preço {PV[a]:10,.2f} · na proposta {PV_R[a]:,}')
    print(f'TOTAL {TOTAL:,} · entrada {TOTAL*PAGTO[0][1]:,.2f}')
    print(f'antes (06/11) {sum(ANTERIOR.values()):,} · diferença {TOTAL - sum(ANTERIOR.values()):+,}')
    for a in ORDEM: print(f'   {a:22s} {ANTERIOR.get(a, 0):>8,} → {PV_R[a]:>8,}  ({PV_R[a] - ANTERIOR.get(a, 0):+,})')
