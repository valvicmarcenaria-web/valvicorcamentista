# -*- coding: utf-8 -*-
"""ODINEY — custo direto e preço, Hettich  [16/11/2026]
(motor copiado do Gran Royalle)

Cascata da casa: NF 5% · erro 2% · serra 0,5% · manutenção 0,5% · RT 10% sobre o
líquido (⚠ Jéssica Sollero, a confirmar) · produção 7,5% sobre o líquido 2 →
BASE 76,0875%. ⛔ O que não muda de ferragem não muda de preço: item sem
corrediça/dobradiça de linha a MC 38% nas três; com ferragem de linha,
Telescópica 35% · Hettich 38% · Blum 43%.
Chapa 275 × 185 a 80%, número cheio por cor × espessura POR AMBIENTE · fita +10%
· filetagem 2,50/m · corte 2/chapa + 2,50/peça · consumíveis 6% · embalagem 2%
· frete R$ 200 por ambiente.
"""
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import levantamento as L

PRECO = {
 'MDF Areia Matt 15': 550, 'MDF Areia Matt 18': 700, 'MDF Carvalho Hanover 15': 550, 'MDF Carvalho Hanover 18': 700,
 'MDF Titânio 18': 700, 'MDF Frapê 15': 550, 'MDF Frapê 18': 700, 'MDF Verde Jade 15': 550, 'MDF Branco TX 15': 350, 'MDF Branco TX 18': 400,
 'MDF Branco TX 6': 250, 'Fita cor': 3, 'Fita Branco TX': 2, 'Filetagem automática': 2.5,
 'Dobradiça Hettich': 50, 'Corrediça Hettich': 150, 'Pistão com amortecimento': 30,
 'Cava usinada': 50, 'Suporte de prateleira': 6.5, 'Perfil de proteção de piso': 15,
 'LED conjunto': 150, 'Fonte de LED': 120, 'Porta de vidro reflecta bronze': 660,
 'Porta de espelho em alumínio': 700, 'Cabideiro': 120, 'Canto boleado': 350,
 'Desempenador de porta': 100, 'Sistema de correr Dominus': 800, 'Estofado': 600,
 # ⚠ premissas, A COTAR (vão numeradas nas dúvidas)
 'Kit porta de correr de passagem': 700, 'Kit porta de giro embutida': 450,
 'Suporte de vinhos': 450, 'Puxador Sotille': 90, 'Prateleira de vidro': 300,
 'Fixação invisível': 35, 'Sistema de correr 3 folhas': 1200, 'Sistema de correr leve': 300,
 'Pino de brise': 15, 'Espelho colado': 600, 'Vidro temperado': 400,
 'Divisória de acrílico': 180, 'Kit tulha': 250,
 'Usinagem de ripa': 3, 'Usinagem almofadada': 40, 'Puxador Zen Design': 45, 'Calceiro': 414,
 'Pé metálico': 300, 'Perfil metálico dourado': 45, 'Usinagem CNC muxarabi': 400, 'Porta de vidro incolor': 550,
 'Prateleira de vidro com serralheria': 450, 'Serralheria metalon': 600, 'Palha natural': 650, 'Fecho toque': 25,
}
AREA, APROV, CONS, EMB, FRETE = 5.0875, 0.80, 0.06, 0.02, 200
# ⚠ padrão até o Jonathan confirmar: Hettich, RT 10%, sem comissão
NF, ERRO, SERRA, MANUT, RT, VEND = 0.05, 0.02, 0.005, 0.005, 0.10, 0.0
LIQ = 1 - NF
BASE = 1 - (NF + ERRO + SERRA + MANUT + RT * LIQ + VEND * LIQ + 0.075 * (LIQ - RT * LIQ - VEND * LIQ))
LINHAS = {'Hettich': dict(dob=50.0, corr=150.0, mc=0.38)}
MC_FIXA = 0.38
AJUSTE_MC = 0.0
AJUSTE_AMB = {}

def custos(amb, lin):
    f = LINHAS[lin]
    pr = dict(PRECO, **{'Dobradiça Hettich': f['dob'], 'Corrediça Hettich': f['corr']})
    its = [i for i in L.ITENS if i['amb'] == amb]
    area, npc, mdf, fe = {}, 0, [], []
    for i in its:
        ch = ft = x = 0.0; fc = fb = 0.0
        for nome, c, l, q, k, fm in i['pecas']:
            a = c * l / 1e4 * q; area[k] = area.get(k, 0) + a; npc += q
            ch += a / (AREA * APROV) * pr[k]
            if 'Branco' in k: fb += fm * q
            else: fc += fm * q
        ft = (fc * 3 + fb * 2) * 1.1 + (fc + fb) * 2.5
        for nome, q, k in i['ferr']: x += q * pr[k]
        for nome, c, l, q, k in i['m2']: x += c * l / 1e4 * q * pr[k]
        mdf.append(ch + ft); fe.append(x)
    nch = {k: math.ceil(a / (AREA * APROV) - 1e-9) for k, a in area.items()}
    c_ch = sum(nch[k] * pr[k] for k in nch)
    arred = c_ch - sum(a / (AREA * APROV) * pr[k] for k, a in area.items())
    corte = sum(nch.values()) * 2 + npc * 2.5
    cons = sum(mdf) * CONS + arred * CONS
    tot = sum(mdf)
    out = []
    for i, m, x in zip(its, mdf, fe):
        parte = m / tot
        c = (m + x + parte * (arred + corte + cons)) * (1 + EMB) + parte * FRETE
        linha = any(k in ('Dobradiça Hettich', 'Corrediça Hettich') for _n, _q, k in i['ferr'])
        out.append(dict(movel=i['movel'], medida=i['medida'], custo=c, linha=linha))
    return out, nch


TAB, CHAPAS = {}, {}
for lin, f in LINHAS.items():
    TAB[lin] = {}
    for amb in L.AMBIENTES:
        its, nch = custos(amb, lin); CHAPAS[amb] = nch
        for it in its:
            mc = (f['mc'] if it['linha'] else MC_FIXA) + AJUSTE_MC + AJUSTE_AMB.get(amb, 0)
            TAB[lin][(amb, it['movel'])] = dict(it, mc=mc, pv=it['custo'] / (BASE - mc))

for x, v in TAB['Hettich'].items():
    if not v['linha']:
        assert len({round(TAB[l][x]['pv'], 2) for l in LINHAS}) == 1, x


# ⭐ [Jonathan, 16/11/2026] ajustes de preço: valor FECHADO por ambiente (e um item)
_F = {'Cozinha': 48000, 'Despensa': 7200, 'Lavanderia e lavabo': 35000, 'Banheiro social': 7500,
      'Suíte master': 55000, 'Closet master': 69000, 'Banheiro master': 11500, 'Suíte hóspedes': 52000,
      'Banheiro suíte hóspedes': 6500, 'Closet filha': 75000}
FECHADO = {a: {'Hettich': float(v)} for a, v in _F.items()}
ITEM_FIXO = {('Sala de TV', 'Prateleira iluminada do hall, atravessando o espelho'): 2300.0}
for _x, _v in ITEM_FIXO.items():
    TAB['Hettich'][_x]['pv'] = _v
assert set(_F) <= set(L.AMBIENTES), set(_F) - set(L.AMBIENTES)


def total(lin, amb=None):
    if amb in FECHADO: return FECHADO[amb][lin]
    if amb is None: return sum(total(lin, a) for a in L.AMBIENTES)
    return sum(v['pv'] for (a, _), v in TAB[lin].items() if a == amb)
def custo(lin, amb=None): return sum(v['custo'] for (a, _), v in TAB[lin].items() if amb in (None, a))


if __name__ == '__main__':
    print(f'BASE {BASE*100:.4f}% · sem ferragem de linha MC {MC_FIXA:.0%} · ' +
          ' · '.join(f'{l} {f["mc"]:.0%}' for l, f in LINHAS.items()) + f' · ajuste {AJUSTE_MC:+.0%}')
    print(f"{'':56s}{'Hettich':>12s}")
    for amb in L.AMBIENTES:
        print(f'\n{amb.upper()}  · chapas {sum(CHAPAS[amb].values())} ' +
              ', '.join(f"{k.replace('MDF ','')} {n}" for k, n in sorted(CHAPAS[amb].items())))
        for (a, m), v in TAB['Hettich'].items():
            if a != amb: continue
            print(f"  {'◆' if v['linha'] else ' '} {m[:52]:52s}" + ''.join(f"{TAB[l][(a, m)]['pv']:>12,.0f}" for l in LINHAS))
        print(f"    {'subtotal':52s}" + ''.join(f'{total(l, amb):>12,.0f}' for l in LINHAS)
              + f"   custo {custo('Hettich', amb):,.0f}")
    print(f"\n    {'TOTAL':52s}" + ''.join(f'{total(l):>12,.0f}' for l in LINHAS))
    print(f"    {'custo direto':52s}" + ''.join(f'{custo(l):>12,.0f}' for l in LINHAS))
    print('chapas no total:', sum(sum(c.values()) for c in CHAPAS.values()))
