# -*- coding: utf-8 -*-
"""Phillip e Giselle · CUSTO × VENDA por ambiente, nas três linhas.

⛔⛔ O QUE NÃO MUDA DE FERRAGEM NÃO MUDA DE PREÇO [Jonathan, 04/11/2026]
  "os itens que não mudam as ferragens, em cada versão o preço de venda tem
  de ser o mesmo · o painel da circulação com as 4 portas tem que ser os
  30.420 em todas as versões · revise esse conceito em todo o orçamento".
  ⭐ O preço de cada ambiente = PARTE COMUM a MC 42% (igual nas três) +
    FERRAGEM DE MOVIMENTO (corrediça e dobradiça) na MC da linha:
    Telescópica 35 · Hettich 38 · Blum 45.

Decisões [Jonathan, 04/11/2026]:
  · SEM RT e SEM VENDEDOR [Jonathan, 04/11/2026: "tire o percentual de vendedor"]
  · MC Telescópica 35% · Hettich 38% · Blum 45%
  · ⛔ SEM CARTÃO e SEM ESCALA DE DESCONTO: "não considere o cartão de crédito
    nesse cliente · parcelamentos igual à proposta do Michel e do Gustavo" →
    30% na assinatura, 20% em 30 dias, 20% em 60, 30% em 90, transferência.
    Um valor só por linha.
  · Closet Mateus com o MESMO custo do Closet Ana ("considere custo igual")
  · Projeto executivo: custo de R$ 2.000, precificado como os ambientes
  · Serviço avulso do rodapé: R$ 1.900 de VENDA, fora da MC
"""
import sys, os, json, subprocess, math, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import motor_mc as MC
from resumo import AVULSO
import motor as M

LIN = {'telescopica': ('Telescópica', 0.35), 'hettich': ('Hettich', 0.38),
       'blum': ('Blum', 0.45)}   # ⭐ 45% [Jonathan, 04/11/2026]
PROJETO = 2000.0
PAGTO = [('Entrada, na assinatura do contrato', 0.30),
         ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20),
         ('90 dias após a assinatura', 0.30)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9
ESCALA = [('Transferência, 30/20/20/30', 0.0, 0, 0.00)]   # sem cartão

def base(entrada, parc):
    """Cascata da casa com cartão só sobre o saldo, sem RT e sem vendedor."""
    cartao = MC.CARTAO_PP * parc * (1 - entrada)
    bruto = MC.NF + cartao + MC.ERRO + MC.SERRA + MC.MANUT
    liq = 1 - MC.NF - cartao
    vend = 0.0                                       # ⛔ sem vendedor
    liq2 = liq - vend
    return 1 - bruto - vend - MC.PROD * liq2

def custos(linha):
    r = subprocess.run([sys.executable, 'resumo.py'], env=dict(os.environ, LINHA=linha),
                       capture_output=True, text=True, check=True,
                       cwd=pathlib.Path(__file__).parent)
    amb = json.loads(r.stdout)['amb']
    amb['Closet Mateus'] = amb['Closet Ana']          # ⭐ custo igual
    ferr = json.loads(r.stdout)['ferr']
    ferr['Closet Mateus'] = ferr.get('Closet Ana', 0)
    return amb, ferr

MC_COMUM = 0.42

# ⭐⭐ O PROJETO NÃO É LINHA DA PROPOSTA [Jonathan, 04/11/2026]: "projeto
#   executivo não deve constar na descrição dos itens, dilua o custo dele
#   entre os itens (closets e painel do quarto da Ana)". Os R$ 2.000 entram
#   na PARTE COMUM desses quatro, na proporção do custo de cada um — que não
#   depende da linha, então o rateio é o mesmo nas três.
def _painel_ana():
    import importlib, os
    os.environ['LINHA'] = 'hettich'
    import motor as MM
    from resumo import AMBS
    for a_ in AMBS: importlib.import_module(a_)
    R_ = MM.calcula(600.0)
    m2 = {k_: R_['chapas'][k_] * MM.preco_chapa(k_) / R_['area'][k_] for k_ in R_['area']}
    v = sum(p_['c'] * p_['l'] / 1e4 * p_['qtd'] * m2[p_['chapa']] for p_ in MM.pecas
            if p_['movel'] == 'Painel com 3 portas mimetizadas')
    v += sum(o_['qtd'] * o_['pu'] for o_ in MM.outras
             if o_['movel'] == 'Painel com 3 portas mimetizadas')
    return v
PESO_PAINEL_ANA = _painel_ana()
DILUI = ['Closet casal', 'Closet Ana', 'Closet Mateus', 'Suíte Ana']

TAB = {}
B = base(0, 0)
for k, (nome, mc) in LIN.items():
    amb, ferr = custos(k); CD = sum(amb.values())
    pv, com = {}, {}
    pesos = {a: (amb[a] - ferr.get(a, 0)) for a in DILUI[:3]}
    pesos['Suíte Ana'] = PESO_PAINEL_ANA
    soma = sum(pesos.values())
    for a, c in amb.items():
        f = ferr.get(a, 0.0); com[a] = c - f + PROJETO * pesos.get(a, 0) / soma
        amb[a] = c + PROJETO * pesos.get(a, 0) / soma
        pv[a] = round(com[a] / (B - MC_COMUM), -1) + round(f / (B - mc), -1)
    CD = sum(amb.values())                      # ⭐ já com o projeto diluído
    cheio = sum(pv.values())
    esc = [('Transferência, 30/20/20/30', 0.0, cheio, B - CD / cheio)]
    TAB[k] = dict(nome=nome, mc=mc, amb=amb, CD=CD, cheio=cheio, pv=pv, esc=esc,
                  com=com, ferr=ferr)
# ⛔ a trava: parte comum IGUAL nas três linhas, ambiente por ambiente
for a in TAB['hettich']['com']:
    v = [round(TAB[k]['com'][a], 2) for k in TAB]
    assert max(v) - min(v) < 0.05, (a, v)

if __name__ == '__main__':
    t0 = TAB['hettich']
    print(f"{'Ambiente':33s}" + ''.join(f"{'custo ' + t['nome'][:5]:>13s}{'venda':>13s}" for t in TAB.values()))
    for a in t0['amb']:
        print(f"{a:33s}" + ''.join(f"{M.brl(t['amb'][a]):>13s}{M.brl(t['pv'][a]):>13s}" for t in TAB.values()))
    print(f"{'TOTAL':33s}" + ''.join(f"{M.brl(t['CD']):>13s}{M.brl(t['cheio']):>13s}" for t in TAB.values()))
    for t in TAB.values():
        print(f"\n{t['nome']} · MC {t['mc']*100:.0f}%")
        for lab, d, p, mc in t['esc']:
            print(f"   {lab}: {M.brl(p)} · MC efetiva {mc*100:.1f}% · base {B*100:.2f}%")
        for lab, f in PAGTO:
            print(f"      {lab:36s} {f*100:3.0f}%  {M.brl(t['cheio']*f)}")
    for dsc, v, obs in AVULSO: print(f'\nAVULSO {M.brl(v)} (venda) · {obs}')
