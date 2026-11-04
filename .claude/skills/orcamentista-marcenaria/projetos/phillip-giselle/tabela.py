# -*- coding: utf-8 -*-
"""Gera TABELA-REVISADA.md a partir de precos.py (nenhum número digitado)."""
import pathlib
from precos import TAB, ORDEM, B, PAGTO, FIXO_ITEM, FIXO_AMB, AVULSO, MESCLA
f = lambda v: f'{v:,.0f}'.replace(',', '.')
L = ['telescopica', 'hettich', 'blum']
o = ['# Phillip e Giselle · tabela revisada (custo × venda)', '',
     'Valores em R$. Sem RT, sem vendedor, sem cartão · pagamento 30/20/20/30 por transferência.',
     'Parte comum a MC 42% (igual nas três linhas) + ferragem de movimento na MC da linha '
     '(Telescópica 35% · Hettich 43% · Blum 55%; itens com ferragem de linha sobem inteiros: Hettich 47%, Blum 52%). Projeto executivo diluído nos closets e no painel da Suíte Ana.',
     'Preços fixos e ajustes pedidos pelo Jonathan em 04/11/2026 estão marcados na linha do item.', '',
     '| Ambiente / item | Telescópica | Hettich | Blum |', '|---|--:|--:|--:|']
for a in ORDEM:
    it = [x for x in TAB['hettich']['pv'] if x[0] == a]
    o.append(f'| **{a}** | | | |')
    for x in it:
        fx = ' · preço fixo' if x in FIXO_ITEM else ''
        if a in MESCLA and MESCLA[a][1] < 1: fx = f' · já com −{(1 - MESCLA[a][1]) * 100:.0f}%'
        o.append(f'| {x[1]}{fx} | ' + ' | '.join(f(TAB[k]['pv'][x]) for k in L) + ' |')
    o.append(f'| *subtotal {a}*{" · preço fixo" if a in FIXO_AMB else ""} | ' + ' | '.join(
        f'*{f(sum(TAB[k]["pv"][y] for y in it))}*' for k in L) + ' |')
    o.append(f'| *custo direto {a}* | ' + ' | '.join(
        f(sum(TAB[k]['cus'][y] for y in it)) for k in L) + ' |')
o += [f'| **TOTAL DE VENDA** | ' + ' | '.join(f"**{f(TAB[k]['venda'])}**" for k in L) + ' |',
      f'| Custo direto | ' + ' | '.join(f(TAB[k]['CD']) for k in L) + ' |',
      f'| MC efetiva | ' + ' | '.join(f"{(B - TAB[k]['CD'] / TAB[k]['venda']) * 100:.1f}%" for k in L) + ' |']
o += ['', '| Parcela | Telescópica | Hettich | Blum |', '|---|--:|--:|--:|']
o += [f'| {lab} ({p*100:.0f}%) | ' + ' | '.join(f(TAB[k]['venda'] * p) for k in L) + ' |' for lab, p in PAGTO]
o += ['', *[f'Serviço avulso (venda, fora da MC): R$ {f(v)} · {d} · {obs}.' for d, v, obs in AVULSO]]
(pathlib.Path(__file__).parent / 'TABELA-REVISADA.md').write_text('\n'.join(o) + '\n', encoding='utf-8')
print('\n'.join(o))
