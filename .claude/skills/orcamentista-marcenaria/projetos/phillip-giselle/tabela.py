# -*- coding: utf-8 -*-
"""Gera TABELA-REVISADA.md a partir de precos.py (nenhum número digitado).
⭐ [06/11/2026] duas linhas (Hettich e Blum), o opcional das portas de espelho
   em linha própria, fora do total, e o "antes" de 04/11 ao lado do que mudou."""
import pathlib
from precos import TAB, ORDEM, B, PAGTO, FIXO_ITEM, FIXO_AMB, AVULSO, MESCLA, VISTO, ANTES, TOTAL_ANTES, OPCIONAL
f = lambda v: f'{v:,.0f}'.replace(',', '.')
L = list(TAB)
o = ['# Phillip e Giselle · tabela revisada (custo × venda) · revisão de escopo de 06/11/2026', '',
     'Valores em R$. Sem RT, sem vendedor, sem cartão · pagamento 30/20/20/30 por transferência.',
     'Duas linhas: **Hettich** e **Blum**. Parte comum a MC 42% + ferragem de movimento na MC da linha '
     '(Hettich 43% · Blum 55%; itens com ferragem de linha sobem inteiros: Hettich 47%, Blum 52%).',
     '⛔ O que a revisão NÃO tocou fica no preço que o cliente viu em 04/11 (marcado "como em 04/11").', '',
     '| Ambiente / item | Hettich | Blum | em 04/11 (H · B) |', '|---|--:|--:|--:|']
for a in ORDEM:
    if a in OPCIONAL: continue
    it = [x for x in TAB['hettich']['pv'] if x[0] == a]
    o.append(f'| **{a}** | | | |')
    for x in it:
        nota = ''
        if x in FIXO_ITEM: nota = ' · preço fixo'
        if x in VISTO: nota = ' · como em 04/11'
        if a in MESCLA and MESCLA[a][1] < 1: nota = f' · já com −{(1 - MESCLA[a][1]) * 100:.0f}%'
        antes = next((v for y, v in ANTES.items() if y[0] == a), None)
        ant = f'{f(antes[0])} · {f(antes[1])}' if antes else '='
        o.append(f'| {x[1]}{nota} | ' + ' | '.join(f(TAB[k]['pv'][x]) for k in L) + f' | {ant} |')
    o.append(f'| *custo direto {a}* | ' + ' | '.join(f(sum(TAB[k]['cus'][y] for y in it)) for k in L) + ' | |')
o.append('| **Quarto Mateus** · ⛔ saiu inteiro | — | — | ' + f"{f(ANTES[('Quarto Mateus', '(cinco itens)')][0])} · {f(ANTES[('Quarto Mateus', '(cinco itens)')][1])} |")
o += [f'| **TOTAL DO CONJUNTO** | ' + ' | '.join(f"**{f(TAB[k]['venda'])}**" for k in L) + f" | {f(TOTAL_ANTES['hettich'])} · {f(TOTAL_ANTES['blum'])} |",
      f'| Custo direto | ' + ' | '.join(f(TAB[k]['CD']) for k in L) + ' | |',
      f'| MC efetiva | ' + ' | '.join(f"{(B - TAB[k]['CD'] / TAB[k]['venda']) * 100:.1f}%" for k in L) + ' | |']
o += ['', '**Opcional, em linha própria, fora do total:**', '', '| Opcional | Hettich | Blum |', '|---|--:|--:|']
for k0 in TAB['hettich']['opc']:
    o.append(f'| {k0[1]} (closet de casal) | ' + ' | '.join(f(TAB[k]['opc'][k0]) for k in L) + ' |')
o.append('| *MC do opcional* | ' + ' | '.join(
    f"{(B - sum(TAB[k]['opc_cus'].values()) / sum(TAB[k]['opc'].values())) * 100:.1f}%" for k in L) + ' |')
o.append('| *custo direto do opcional* | ' + ' | '.join(f(sum(TAB[k]['opc_cus'].values())) for k in L) + ' |')
o.append('| *conjunto + opcional* | ' + ' | '.join(f(TAB[k]['venda'] + sum(TAB[k]['opc'].values())) for k in L) + ' |')
o += ['', '| Parcela (do conjunto) | Hettich | Blum |', '|---|--:|--:|']
o += [f'| {lab} ({p*100:.0f}%) | ' + ' | '.join(f(TAB[k]['venda'] * p) for k in L) + ' |' for lab, p in PAGTO]
o += ['', *[f'Serviço avulso (venda, fora da MC): R$ {f(v)} · {d} · {obs}.' for d, v, obs in AVULSO]]
(pathlib.Path(__file__).parent / 'TABELA-REVISADA.md').write_text('\n'.join(o) + '\n', encoding='utf-8')
print('\n'.join(o))
