# -*- coding: utf-8 -*-
"""HAVERSON SOARES — o preço nas TRÊS LINHAS da casa  [06/11/2026]

⭐⭐ [Jonathan, 06/11/2026] "vamos trabalhar com as nossas três linhas":
   TELESCÓPICA, HETTICH e BLUM, no lugar da Häfele da prancha.
⭐ A cascata é a da aba "Preço e Comissões": nota 5%, margem de erro 2%, serra
   0,5%, manutenção 0,5%, RT de 10% sobre o líquido (⚠ a confirmar com a Luiza
   Pacheco), sem vendedor, sem cartão, produção 7,5% sobre o líquido 2 →
   BASE 76,0875%, a mesma do Attos.
⛔⛔ O QUE NÃO MUDA DE FERRAGEM NÃO MUDA DE PREÇO ENTRE AS LINHAS: item sem
   corrediça nem dobradiça da linha sai a MC 38% nas três. Item com ferragem de
   linha sobe INTEIRO pela escada do Attos, que tem a mesma base: Telescópica
   35% · Hettich 38% · Blum 43%. A trava no fim prova a igualdade.
⭐ O que muda por linha é SÓ o preço da corrediça e da dobradiça:
     Telescópica  Bigfer Telescópica R$ 15 o par · Bigfer Slow Click R$ 4
     Hettich      Quadro V6 R$ 150 o par         · Sensys R$ 50
     Blum         Corrediça Blum R$ 300          · Dobradiça Blum R$ 50
   O articulador das básculas, os pistões e a dobradiça da porta de vidro são
   os mesmos nas três.
⭐ [Jonathan, 09/11/2026] SALA: "rack com a torre de nichos" e "portas com
   sistema mão amiga", separados. E um item de PREÇO FECHADO, sem levantamento:
   "cozinha existente: troca das portas dos armários inferiores, fabricação de
   módulo complementar, tudo em MDF Branco TX, puxador de cava Rometal. Preço de
   venda R$ 2.500" — o mesmo valor nas três linhas, fora da conta de MC.
⭐ O custo de cada item leva a sua parte da sobra de chapa, do corte e dos
   consumíveis pela fração de chapa e fita que ele usa (que não muda de linha),
   e 2% de embalagem sobre o próprio custo. A soma, na Hettich, tem de dar o
   custo direto que a planilha mostra — e dá, na trava.
"""
import io, contextlib, math, sys, pathlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P)); sys.path.insert(0, str(P.parent))
with contextlib.redirect_stdout(io.StringIO()):
    import planilha as PL
    import levantamento as L

NF, ERRO, SERRA, MANUT, RT, VEND = 0.05, 0.02, 0.005, 0.005, 0.10, 0.0
LIQ = 1 - NF
BASE = 1 - (NF + ERRO + SERRA + MANUT + RT * LIQ + VEND * LIQ + 0.075 * (LIQ - RT * LIQ - VEND * LIQ))
assert abs(BASE - 0.760875) < 1e-9, BASE

LINHAS = {'Telescópica': dict(dob=4.0, corr=15.0, mc=0.35),
          'Hettich': dict(dob=50.0, corr=150.0, mc=0.38),
          'Blum': dict(dob=50.0, corr=300.0, mc=0.43)}
MC_FIXA = 0.38
DOB, CORR = 'Dobradiça Hettich', 'Corrediça Hettich'
ORDEM = [a[0] for a in PL.ABAS]
AREA, APROV = PL.AREA, PL.APROV


def custos(amb, lin):
    """Custo de cada item do ambiente na linha, já com a sua parte do ambiente."""
    f = LINHAS[lin]
    preco = dict(PL.PRECO, **{DOB: f['dob'], CORR: f['corr']})
    itens = [i for i in L.ITENS if i['amb'] == amb]
    area, npc, base_it, ferr_it, mdf_it = {}, 0, [], [], []
    for i in itens:
        ch = ft = fe = 0.0
        fita = {}
        for nome, obs, c, l, q, k, fm, tipo in i['pecas']:
            a = c * l / 1e4 * q
            area[k] = area.get(k, 0.0) + a; npc += q
            ch += a / (AREA * APROV) * preco[k]
            if fm: fita[tipo] = fita.get(tipo, 0) + fm * q
        for tipo, m in fita.items():
            ft += round(m * 1.1, 1) * preco[tipo]
        if fita:
            ft += round(sum(fita.values()), 1) * preco['Filetagem automática']
        for nome, obs, c, l, q, un, k in i['terc']:
            fe += c * l / 1e4 * q * preco[k]
        for nome, obs, q, un, k in i['ferr']:
            fe += q * preco[k]
        mdf_it.append(ch + ft); ferr_it.append(fe); base_it.append(i)
    nch = {k: math.ceil(a / (AREA * APROV)) for k, a in area.items()}
    c_ch = sum(nch[k] * preco[k] for k in nch)
    arred = c_ch - sum(a / (AREA * APROV) * preco[k] for k, a in area.items())
    corte = sum(nch.values()) * preco['Corte por chapa'] + npc * preco['Corte por peça']
    c_ft = sum(mdf_it) - (c_ch - arred)
    cons = (c_ch + c_ft) * PL.CONS
    frete = preco['Frete'] * PL.VIAGENS.get(amb, 1)
    tot = sum(mdf_it)
    out = []
    for i, m, fe in zip(base_it, mdf_it, ferr_it):
        parte = m / tot
        c = (m + fe + parte * (arred + corte + cons)) * (1 + PL.EMB) + parte * frete
        linha = any(k in (DOB, CORR) for *_, k in i['ferr'])
        out.append(dict(movel=i['movel'], custo=c, linha=linha))
    return out


TAB = {}
for lin, f in LINHAS.items():
    TAB[lin] = {}
    for amb in ORDEM:
        for it in custos(amb, lin):
            mc = f['mc'] if it['linha'] else MC_FIXA
            TAB[lin][(amb, it['movel'])] = dict(custo=it['custo'], mc=mc, linha=it['linha'],
                                                pv=it['custo'] / (BASE - mc))

# ⛔ as travas
for amb in ORDEM:
    cd = PL.monta(*[a for a in PL.ABAS if a[0] == amb][0])['cd']
    soma = sum(v['custo'] for (a, _m), v in TAB['Hettich'].items() if a == amb)
    assert abs(cd - soma) < 0.05, (amb, cd, soma)
for x, v in TAB['Hettich'].items():
    if not v['linha']:
        pvs = {round(TAB[l][x]['pv'], 2) for l in LINHAS}
        assert len(pvs) == 1, ('⛔ item sem ferragem de linha com preços diferentes', x, pvs)
for x in TAB['Hettich']:
    assert TAB['Telescópica'][x]['pv'] <= TAB['Hettich'][x]['pv'] + 0.01 <= TAB['Blum'][x]['pv'] + 0.02, x


# ⭐ preço FECHADO pelo Jonathan, sem levantamento: entra igual nas três linhas
FIXOS = {('Cozinha existente', 'Troca das portas dos inferiores e módulo complementar'): 2500.0}


def total(lin, amb=None, fixos=True):
    t = sum(v['pv'] for (a, _m), v in TAB[lin].items() if amb in (None, a))
    if fixos:
        t += sum(v for (a, _m), v in FIXOS.items() if amb in (None, a))
    return t


def custo(lin, amb=None):
    return sum(v['custo'] for (a, _m), v in TAB[lin].items() if amb in (None, a))


if __name__ == '__main__':
    print(f'base {BASE * 100:.4f}% · item sem ferragem de linha a {MC_FIXA:.0%} · '
          + ' · '.join(f'{l} {f["mc"]:.0%}' for l, f in LINHAS.items()))
    for amb in ORDEM:
        print(f'\n{amb.upper()}')
        for (a, m), v in TAB['Hettich'].items():
            if a != amb: continue
            print(f"  {'◆' if v['linha'] else ' '} {m[:52]:52s}" + ''.join(
                f"{TAB[l][(a, m)]['pv']:>12,.0f}" for l in LINHAS))
        print(f"    {'subtotal':52s}" + ''.join(f'{total(l, amb):>12,.0f}' for l in LINHAS))
        print(f"    {'custo direto':52s}" + ''.join(f'{custo(l, amb):>12,.0f}' for l in LINHAS))
    for (a, m), v in FIXOS.items():
        print(f'\n{a.upper()} · preço fechado')
        print(f"    {m[:52]:52s}" + ''.join(f'{v:>12,.0f}' for l in LINHAS))
    print(f"\n    {'TOTAL':52s}" + ''.join(f'{total(l):>12,.0f}' for l in LINHAS))
    print(f"    {'custo direto do levantado':52s}" + ''.join(f'{custo(l):>12,.0f}' for l in LINHAS))
    print(f"    {'MC efetiva do levantado':52s}" + ''.join(
        f'{(BASE - custo(l) / total(l, fixos=False)) * 100:>11.1f}%' for l in LINHAS))
    print('  ◆ = item com corrediça ou dobradiça da linha')
