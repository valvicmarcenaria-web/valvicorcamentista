#!/usr/bin/env python3
"""Testes da planilha de Custo por Projeto.

Calcula as fórmulas de verdade e confere a ficha inteira contra um modelo
independente escrito em Python. Para o Painel Geral, resolve o INDIRECT à mão
— o motor de teste não avalia nome de aba dinâmico, mas o endereço apontado
por cada coluna pode (e deve) ser conferido.

Uso:  python3 testar-custo-projeto.py
"""
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
import openpyxl
import formulas

ARQ = 'Valvic_Custo_por_Projeto.xlsx'
EX = 'Exemplo P-2026-041'
PG = 'Painel Geral'


def xr(x, n=2):
    q = Decimal(1).scaleb(-n)
    return float(Decimal(f'{float(x):.15g}').quantize(q, rounding=ROUND_HALF_UP))


# Tolerância de 1 centavo em valores que nascem de ROUND() sobre um produto em
# ponto flutuante: 0,03 × 73.063,50 vale 2191.9049999999997 em binário, e o
# resultado do arredondamento depende de como cada implementação normaliza os
# 15 dígitos significativos. O motor de teste devolve 2191,90; o Excel devolve
# 2191,91. Um centavo aqui não é defeito de fórmula — um erro de fórmula de
# verdade aparece em ordem de grandeza muito maior.
CENTAVO = 0.011

falhas, testes = [], 0
def ck(nome, obtido, esperado, tol=0.005):
    global testes
    testes += 1
    if isinstance(esperado, (int, float)) and isinstance(obtido, (int, float)):
        ok = abs(obtido - esperado) <= tol
    else:
        ok = str(obtido).strip() == str(esperado).strip()
    if not ok:
        falhas.append(f'{nome}\n     obtido   = {obtido!r}\n     esperado = {esperado!r}')


print('Calculando a planilha com o motor de fórmulas...')
xl = formulas.ExcelModel().loads(ARQ).finish()
sol = xl.calculate()
pat = re.compile(r"^'\[" + re.escape(ARQ) + r"\]([^']+)'!([A-Z]+[0-9]+)$", re.I)
VAL = {}
for k, v in sol.items():
    m = pat.match(str(k))
    if not m:
        continue
    try:
        val = v.value[0, 0]
    except Exception:
        val = getattr(v, 'value', v)
    if hasattr(val, 'item'):
        try: val = val.item()
        except Exception: pass
    VAL[(m.group(1).upper(), m.group(2).upper())] = val

def C(aba, ref):
    return VAL.get((aba.upper(), ref.upper()), '<ausente>')

print(f'{len(VAL)} células resolvidas\n' + '─' * 76)

wbv = openpyxl.load_workbook(ARQ)
ws = wbv[EX]

# ═════════════ modelo independente do exemplo
V = 90000.0
imp = xr(0.075 * V); maq = xr(0.02 * V); cvend = xr(0.03 * V)
trx_o, trx_r = 120.0, 148.0
proj = 1500.0
rt_o = xr(0.05 * (V - imp - maq - trx_o))
rt_r = xr(0.05 * (V - imp - maq - trx_r))
cv_o = xr(imp + maq + trx_o + cvend + proj + rt_o)
cv_r = xr(imp + maq + trx_r + cvend + proj + rt_r)
liq_o, liq_r = xr(V - cv_o), xr(V - cv_r)
AMB = [('Cozinha', 30000, 'Jackson', 0.03, 'Samuel', 0.02),
       ('Suíte', 20000, 'Samuel', 0.03, 'Cezar', 0.02),
       ('Lavanderia', 10000, 'Joelson', 0.03, 'Samuel', 0.02),
       ('Sala', 30000, 'Deivson', 0.03, 'Jackson', 0.02)]
prod, mont, por_pessoa = {}, {}, {}
tot_prod = tot_mont = 0.0
for nome, val, pq, pp, mq, mp in AMB:
    pctamb = val / V
    vp, vm = xr(pctamb * liq_r * pp), xr(pctamb * liq_r * mp)
    prod[nome], mont[nome] = vp, vm
    tot_prod += vp; tot_mont += vm
    por_pessoa[pq] = por_pessoa.get(pq, 0) + vp
    por_pessoa[mq] = por_pessoa.get(mq, 0) + vm
tot_prod, tot_mont = xr(tot_prod), xr(tot_mont)
coord_o, coord_r = xr(0.01 * liq_o), xr(0.01 * liq_r)
com_o = xr(coord_o + xr(0.03 * liq_o) + xr(0.02 * liq_o))
com_r = xr(coord_r + tot_prod + tot_mont)
por_pessoa['Deivson'] = por_pessoa.get('Deivson', 0) + coord_r
MAT = [(14500, 15980), (900, 1120), (6800, 7450), (2200, 2200), (0, 0), (3200, 3200),
       (1100, 1465)]
TER = [(4800, 5400), (1500, 1500), (900, 1250), (0, 0)]
LOG = [(250, 410), (900, 1150), (400, 620), (350, 350), (100, 185)]
mat_o, mat_r = xr(sum(a for a, _ in MAT)), xr(sum(b for _, b in MAT))
ter_o, ter_r = xr(sum(a for a, _ in TER)), xr(sum(b for _, b in TER))
log_o, log_r = xr(sum(a for a, _ in LOG)), xr(sum(b for _, b in LOG))
rb_o, rb_r = 1500.0, xr(850 + 1200 + 320)
custo_o = xr(cv_o + com_o + mat_o + ter_o + log_o + rb_o)
custo_r = xr(cv_r + com_r + mat_r + ter_r + log_r + rb_r)
mc_o, mc_r = xr(V - custo_o), xr(V - custo_r)

# ═════════════ testes
print('TESTE 1 · cascata de custos de venda e receita líquida')
for ref, esp in ((f'C21', imp), ('D21', imp), ('C22', maq), ('D22', maq),
                 ('C23', trx_o), ('D23', trx_r), ('C24', cvend), ('D24', cvend),
                 ('C25', proj), ('D25', proj), ('C26', rt_o), ('D26', rt_r),
                 ('C27', cv_o), ('D27', cv_r), ('C28', liq_o), ('D28', liq_r)):
    ck(f'  {EX}!{ref}', C(EX, ref), esp)
print(f'  {testes} verificações')

n0 = testes
print('\nTESTE 2 · ambientes — comissão de produção e de montagem')
for i, (nome, val, pq, pp, mq, mp) in enumerate(AMB):
    r = 32 + i
    ck(f'  {nome} · % do total', C(EX, f'B{r}'), val / V, tol=1e-9)
    ck(f'  {nome} · produção ({pq})', C(EX, f'F{r}'), prod[nome])
    ck(f'  {nome} · montagem ({mq})', C(EX, f'I{r}'), mont[nome])
    ck(f'  {nome} · total', C(EX, f'J{r}'), xr(prod[nome] + mont[nome]))
ck('  soma dos ambientes', C(EX, 'C42'), V)
ck('  total produção', C(EX, 'F42'), tot_prod)
ck('  total montagem', C(EX, 'I42'), tot_mont)
ck('  conferência dos ambientes', str(C(EX, 'D42'))[:2], 'OK')
print(f'  {testes - n0} verificações')

n0 = testes
print('\nTESTE 3 · comissões por colaborador')
for r in range(53, 65):
    nome = ws.cell(r, 1).value
    if not nome:
        continue
    esp = xr(por_pessoa.get(nome, 0))
    ck(f'  {nome} · total', C(EX, f'H{r}'), esp)
ck('  soma das comissões por pessoa', C(EX, 'H65'), com_r, tol=CENTAVO)
ck('  bate com o subtotal de comissões', C(EX, 'D49'), com_r, tol=CENTAVO)
# nenhum centavo pode se perder entre os ambientes e o consolidado por pessoa
ck('  consolidado por pessoa = subtotal das comissões', C(EX, 'H65'), C(EX, 'D49'), tol=1e-9)
print(f'  {testes - n0} verificações')

n0 = testes
print('\nTESTE 4 · resumo, custo total e margem')
for i, (co, cr_) in enumerate([(cv_o, cv_r), (com_o, com_r), (mat_o, mat_r),
                               (ter_o, ter_r), (log_o, log_r), (rb_o, rb_r)]):
    r = 107 + i
    ck(f'  resumo linha {r} orçado', C(EX, f'C{r}'), co, tol=CENTAVO)
    ck(f'  resumo linha {r} realizado', C(EX, f'D{r}'), cr_, tol=CENTAVO)
    ck(f'  resumo linha {r} desvio', C(EX, f'E{r}'), xr(cr_ - co), tol=CENTAVO)
ck('  custo total orçado', C(EX, 'C113'), custo_o, tol=CENTAVO)
ck('  custo total realizado', C(EX, 'D113'), custo_r, tol=CENTAVO)
ck('  MC orçada', C(EX, 'C114'), mc_o, tol=CENTAVO)
ck('  MC realizada', C(EX, 'D114'), mc_r, tol=CENTAVO)
ck('  MC % orçada', C(EX, 'G114'), mc_o / V, tol=CENTAVO / V)
ck('  MC % realizada', C(EX, 'H114'), mc_r / V, tol=CENTAVO / V)
# o que precisa fechar exatamente: o resumo é a soma dos blocos da própria ficha
ck('  custo total = soma das 6 categorias',
   C(EX, 'D113'), xr(sum(C(EX, f'D{107+i}') for i in range(6))), tol=1e-9)
ck('  MC = venda - custo total', C(EX, 'D114'),
   xr(C(EX, 'A13') - C(EX, 'D113')), tol=1e-9)
print(f'  {testes - n0} verificações')

n0 = testes
print('\nTESTE 5 · faixa de resultado do topo e entrega')
ck('  KPI venda', C(EX, 'A13'), V)
ck('  KPI custo total', C(EX, 'C13'), custo_r)
ck('  KPI MC R$', C(EX, 'E13'), mc_r)
ck('  KPI MC %', C(EX, 'G13'), mc_r / V, tol=1e-9)
ck('  KPI MC % orçada', C(EX, 'H13'), mc_o / V, tol=CENTAVO / V)
ck('  KPI desvio de custo', C(EX, 'I13'), xr(custo_r - custo_o), tol=CENTAVO)
ck('  KPI espelha o resumo (custo)', C(EX, 'C13'), C(EX, 'D113'), tol=1e-9)
ck('  KPI espelha o resumo (MC)', C(EX, 'E13'), C(EX, 'D114'), tol=1e-9)
ck('  dias de atraso', C(EX, 'H9'), 7)
ck('  situação da entrega', C(EX, 'J9'), 'Atrasado')
print(f'  {testes - n0} verificações')

n0 = testes
print('\nTESTE 6 · a ficha em branco não pode gerar lixo')
for ref in ('A13', 'C13', 'E13', 'G13', 'I13', 'D27', 'D28', 'F32', 'I32', 'J32',
            'H53', 'D107', 'D113', 'D114', 'H9', 'J9'):
    v = C('Ficha Modelo', ref)
    ck(f'  Ficha Modelo!{ref} vazia', '' if v in ('', 0, 0.0) else v, '')
print(f'  {testes - n0} verificações')

n0 = testes
print('\nTESTE 7 · o Painel aponta para os endereços certos da ficha')
pg = wbv[PG]
P0 = next(r for r in range(1, pg.max_row + 1) if pg.cell(r, 2).value == 'Exemplo P-2026-041')
ESPERADO = {3: 'A7', 4: 'A9', 5: 'F7', 6: 'H7', 7: 'J7', 8: 'H9', 9: 'J9',
            10: 'A13', 11: 'C13', 12: 'E13', 13: 'G13', 14: 'H13', 16: 'I13'}
for col, ref in ESPERADO.items():
    f = pg.cell(P0, col).value or ''
    m = re.search(r"&\"'!([A-Z]+[0-9]+)\"\)", f)
    ck(f'  Painel col {openpyxl.utils.get_column_letter(col)} aponta para', 
       m.group(1) if m else f, ref)
    ck(f'  Painel col {openpyxl.utils.get_column_letter(col)} usa IFERROR+INDIRECT',
       f.startswith('=IFERROR(INDIRECT('), True)
# auxiliares das categorias
for k in range(6):
    for j, letra in enumerate(('C', 'D')):
        f = pg.cell(P0, 34 + k * 2 + j).value or ''
        m = re.search(r"&\"'!([A-Z]+[0-9]+)\"\)", f)
        ck(f'  Painel auxiliar categoria {k+1} {letra}',
           m.group(1) if m else f, f'{letra}{107 + k}')
print(f'  {testes - n0} verificações')

n0 = testes
print('\nTESTE 8 · as duas fichas têm exatamente a mesma estrutura')
fm, exx = wbv['Ficha Modelo'], wbv[EX]
dif = 0
for r in range(1, 120):
    for c in range(1, 11):
        a, b = fm.cell(r, c).value, exx.cell(r, c).value
        fa = isinstance(a, str) and a.startswith('=')
        fb = isinstance(b, str) and b.startswith('=')
        if fa or fb:
            if a != b:
                dif += 1
ck('  fórmulas idênticas entre modelo e exemplo', dif, 0)
ck('  mesmo nº de mesclagens', len(fm.merged_cells.ranges), len(exx.merged_cells.ranges))
print(f'  {testes - n0} verificações')

print('\n' + '═' * 76)
print(f'{testes} verificações · {len(falhas)} falha(s)')
if falhas:
    print('═' * 76)
    for f in falhas[:25]:
        print('  ✗ ' + f)
    sys.exit(1)
print('TODOS OS TESTES PASSARAM')
