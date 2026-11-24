# -*- coding: utf-8 -*-
"""DAYANE FAUSTINO — três cenários  [24/11/2026]

⭐ [Jonathan, 24/11/2026] "vamos fazer esse orçamento no mesmo formato do anterior" (os três cenários da Jessica Fernandes).

⭐ Devolutiva da Rubia (designer), via Jonathan: "podemos ver como ficaria mudando as ferragens e mantendo a
   palha, e uma opção trocando a palha por um MDF? pode ser estilo o Tela da Guararapes" · Jonathan: "vamos
   adicionar na proposta o cenário de ferragens básicas" · "apresentar esses cenários de forma clara e objetiva".
   1 · Hettich com palha natural       — a proposta fechada (R$ 93.500)
   2 · Ferragem básica com palha       — corrediça telescópica e dobradiça nacional
   3 · Ferragem básica com MDF Tela    — a palha trocada por MDF Tela, Guararapes, nas portas e na cabeceira
⭐ Mesmas regras de margem da proposta (45%; cabeceira 60%; básica 3 pontos abaixo da Hettich, como na casa) e o
   MESMO fator do fechamento em 93.500, para os três cenários serem comparáveis entre si.
⛔ Não se mistura linha de ferragem: cada cenário é uma linha inteira.
"""
import copy, io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import precos as P

P.LINHAS['Básica'] = dict(dob=4.0, corr=15.0, mc=0.35)
P.PRECO['MDF Tela 15'] = 550
ORIG = copy.deepcopy(P.L.ITENS)


def tabela(lin, sem_palha=False):
    P.L.ITENS[:] = copy.deepcopy(ORIG)
    if sem_palha:
        for it in P.L.ITENS:
            for nome, c, l, q, k in list(it['m2']):
                if k == 'Palha natural':
                    it['m2'].remove((nome, c, l, q, k))
                    it['pecas'].append(('Almofada em MDF Tela, Guararapes', c, l, q, 'MDF Tela 15', 0))
    out = {}
    for amb in P.L.AMBIENTES:
        for it in P.custos(amb, lin)[0]:
            f = P.LINHAS[lin]
            mc = (f['mc'] if it['linha'] else P.MC_FIXA) + P.AJUSTE_MC
            mc = P.MC_ITEM.get(it['movel'], mc)
            out[it['movel']] = dict(custo=it['custo'], pv=it['custo'] / (P.BASE - mc))
    P.L.ITENS[:] = copy.deepcopy(ORIG)
    return out


BASE_H = tabela('Hettich')
FATOR = 1.0   # sem fechamento: margem da casa (45% Hettich · 42% básica)
CENARIOS = [
 ('Hettich com palha natural', 'Hettich', 'Palha natural', 10, tabela('Hettich')),
 ('Ferragem básica com palha natural', 'Telescópica', 'Palha natural', 2, tabela('Básica')),
 ('Ferragem básica com MDF Tela', 'Telescópica', 'MDF Tela, Guararapes', 2, tabela('Básica', sem_palha=True)),
]


def valores():
    res = []
    for nome, fer, acab, gar, tab in CENARIOS:
        v = {m: round(t['pv'] * FATOR) for m, t in tab.items()}
        alvo = round(sum(t['pv'] for t in tab.values()) * FATOR / 100) * 100   # total redondo, em centenas
        v[max(v, key=v.get)] += alvo - sum(v.values())
        res.append(dict(nome=nome, ferragem=fer, acab=acab, garantia=gar, itens=v, total=sum(v.values()),
                        custo=sum(t['custo'] for t in tab.values())))
    # os itens sem palha valem o mesmo no cenário 3 e no 2: só muda o que leva palha
    com_palha = {it['movel'] for it in ORIG if any(k == 'Palha natural' for *_, k in it['m2'])}
    r2, r3 = res[1], res[2]
    t2, t3 = CENARIOS[1][4], CENARIOS[2][4]
    for m in r3['itens']:
        r3['itens'][m] = r2['itens'][m] if m not in com_palha else round(r2['itens'][m] * t3[m]['pv'] / t2[m]['pv'])
    alvo = round(sum(r3['itens'].values()) / 100) * 100
    mx = max(com_palha, key=lambda m: r3['itens'][m]); r3['itens'][mx] += alvo - sum(r3['itens'].values())
    r3['total'] = sum(r3['itens'].values())
    return res


if __name__ == '__main__':
    for c in valores():
        print(f"{c['nome']:38s} R$ {c['total']:>9,.0f}  custo {c['custo']:>8,.0f}  MC {(P.BASE - c['custo'] / c['total']) * 100:4.1f}%")
        for m, x in c['itens'].items(): print(f"     {m[:56]:56s} {x:>8,}")
