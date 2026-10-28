# -*- coding: utf-8 -*-
"""Confere o levantamento ANTES de ele virar planilha.

⛔⛔ [Jonathan 28/10] "sempre revise antes de entregar os resultados."

   Oito correções numa rodada só. Quase todas eram coisas que uma conferência
   mecânica teria pegado: frente sem dobradiça, gaveta sem corrediça, peça
   de largura que não existe, linha que soma e outra que subtrai a mesma
   área. ⭐ A revisão não pode depender de eu lembrar — tem de quebrar.

   Uso:  python3 auditor.py            confere o script
         python3 auditor.py planilha.json   confere TAMBÉM contra a aba
"""
import sys, json, importlib.util, pathlib
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('L', P/'living.py')
L = importlib.util.module_from_spec(spec); sys.modules['L'] = L
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(L)

br = lambda v: f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
FALHAS, AVISOS = [], []
def erro(m):  FALHAS.append(m)
def aviso(m): AVISOS.append(m)

CHAVES = {'MDF cor 18', 'MDF cor 15', 'MDF cor 6', 'Fita', 'Corrediça',
          'Dobradiça', 'Dobradiça vidro', 'Cava usinada', 'LED conjunto',
          'Alma de aço', 'Suporte oculto', 'Vidro reflecta'}

# ── 1 · as peças ────────────────────────────────────────────────────────
for p in L.LIVING:
    r = f"{p['movel'][:26]} · {p['nome']}"
    if p['c'] <= 0 or p['l'] <= 0: erro(f'{r}: dimensão zero ou negativa')
    if p['qtd'] == 0:              erro(f'{r}: quantidade zero')
    if p['qtd'] < 0:               erro(f'{r}: QUANTIDADE NEGATIVA — '
                                        'linha que subtrai área não é peça')
    if p['esp'] not in (6, 15, 18): erro(f'{r}: espessura {p["esp"]} fora da base')
    maior, menor = max(p['c'], p['l']), min(p['c'], p['l'])
    if maior > L.CHAPA_C or menor > L.CHAPA_L:
        erro(f'{r}: {p["c"]:g}×{p["l"]:g} NÃO CABE na chapa')

# ── 2 · gaveta ↔ corrediça ──────────────────────────────────────────────
#   ⭐ toda caixa de gaveta precisa de um par de corrediça, e todo par
#     precisa de uma caixa. É o furo que o Jonathan achou em 27/10.
caixas = {}
for p in L.LIVING:
    if '· fundo' in p['nome'] and ('aveta' in p['nome'] or 'Gaveta' in p['nome']):
        caixas[p['movel']] = caixas.get(p['movel'], 0) + p['qtd']
corr = {}
for mv, rot, q, mm in L.GAVETAS: corr[mv] = corr.get(mv, 0) + q
for mv in set(caixas) | set(corr):
    if caixas.get(mv, 0) != corr.get(mv, 0):
        erro(f'{mv[:30]}: {caixas.get(mv,0)} caixas de gaveta × '
             f'{corr.get(mv,0)} pares de corrediça — não bate')

# ── 3 · frente com cava ↔ metro de cava ─────────────────────────────────
cava_mov = {mv for mv, *_ in L.CAVA}
for p in L.LIVING:
    if 'cava' in p['obs'].lower() and p['movel'] not in cava_mov:
        erro(f'{p["movel"][:30]} · {p["nome"]}: diz "cava" e o móvel não '
             'tem metro de cava declarado')

# ── 4 · porta ↔ dobradiça ───────────────────────────────────────────────
#   ⭐ [Jonathan 28/10] item 1: "faltou as dobradiças"
port_mov = {mv for mv, *_ in L.PORTAS}
for p in L.LIVING:
    n = p['nome'].lower()
    if ('porta' in n or n.startswith('frente') and 'gaveta' not in n) \
       and p['movel'] not in port_mov:
        erro(f'{p["movel"][:30]} · {p["nome"]}: frente ou porta SEM dobradiça')

# ── 5 · vidro ↔ porta de vidro ──────────────────────────────────────────
vid_mov = {mv for mv, *_ in L.VIDRO}
for mv, rot, nq, nd, pr in L.PORTAS:
    if pr == L.DOBR_VIDRO and mv not in vid_mov:
        erro(f'{mv[:30]}: dobradiça de vidro sem a FOLHA DE VIDRO declarada')

# ── 6 · alma de aço onde a regra manda ──────────────────────────────────
alma_mov = {mv for mv, *_ in L.ALMAS}
if L.D4 not in alma_mov: erro('As colunas perderam a alma de aço')

# ── 7 · o que NÃO leva fita, leva por decisão? ──────────────────────────
for p in L.LIVING:
    if p['fita'] == (0, 0) and p['esp'] != 6 and 'sem fita' not in p['obs'].lower():
        aviso(f'{p["movel"][:30]} · {p["nome"]}: sem fita e sem justificativa '
              'no texto — foi decisão ou esquecimento?')

# ── 8 · toda chave que a aba vai usar existe na Base ────────────────────
#   ⛔ esta checagem nasceu vazia e não valia nada: conferia um atributo que
#     não existe. Agora ela monta o conjunto de chaves de verdade.
import importlib.util as _iu
_sp = _iu.spec_from_file_location('G', P/'planilha-living.py')
try:
    _g = _iu.module_from_spec(_sp); sys.modules['G'] = _g
    with contextlib.redirect_stdout(io.StringIO()): _sp.loader.exec_module(_g)
    usadas = {ln[-1] for mv in [L.D1, L.D2, L.D3, L.D4, L.D5, L.D6, L.D7, L.D8]
              for ln in _g.linhas_do_item(mv)}
    for ch in sorted(usadas - CHAVES): erro(f'chave fora da Base: "{ch}"')
except Exception as e:
    erro(f'não consegui ler as chaves do gerador: {e}')

# ── 9 · os totais por item, para bater contra a aba ─────────────────────
def custo_item(mv):
    tot = 0.0
    for p in L.LIVING:
        if p['movel'] != mv: continue
        a = p['c']*p['l']*p['qtd']/10000
        tot += a/(L.CHAPA_M2*L.APROV)*(L.CHAPA18 if p['esp'] >= 15 else L.CHAPA6)
    m = sum((nc*p['c']+nl*p['l'])*p['qtd']/100 for p in L.LIVING
            if p['movel'] == mv for nc, nl in [p['fita']])
    tot += round(m*(1+L.FITA_PERD), 1) * L.FITA_CHEIA
    for x, rot, q, mm in L.GAVETAS:
        if x == mv: tot += q*L.CORREDICA
    for x, rot, nq, nd, pr in L.PORTAS:
        if x == mv: tot += nq*nd*pr
    for x, rot, q, c in L.CAVA:
        if x == mv: tot += round(q*c/100, 2)*L.CAVA_M
    for x, rot, q, c, l in L.VIDRO:
        if x == mv: tot += round(q*c*l/10000, 2)*L.VIDRO_M2
    for x, rot, mt in L.LED:
        if x == mv: tot += mt*L.LED_M
    for x, rot, q in L.ALMAS:
        if x == mv: tot += q*L.ALMA
    for x, rot, q in L.SUPORTES:
        if x == mv: tot += q*L.SUPORTE
    return tot

MOV = [L.D1, L.D2, L.D3, L.D4, L.D5, L.D6, L.D7, L.D8]
TOT = {m: custo_item(m) for m in MOV}
for m, v in TOT.items():
    if v <= 0: erro(f'{m[:30]}: custo zero ou negativo')

# ── 10 · contra a aba, se vier ──────────────────────────────────────────
if len(sys.argv) > 1:
    aba = json.load(open(sys.argv[1]))
    for i, m in enumerate(MOV, 1):
        k = f'{i:02d}'
        if k not in aba: erro(f'ITEM {k} não veio da aba'); continue
        d = abs(aba[k] - TOT[m])
        if d > 0.05:
            erro(f'ITEM {k} {m[:24]}: aba {br(aba[k])} × script '
                 f'{br(TOT[m])} — difere {br(d)}')

# ── relatório ───────────────────────────────────────────────────────────
W = 74
print('═'*W); print('AUDITORIA DO LEVANTAMENTO DO LIVING'); print('═'*W)
print(f'\n{len(L.LIVING)} peças · {len(MOV)} itens\n')
for i, m in enumerate(MOV, 1):
    print(f'  ITEM {i:02d}  {m.split(chr(32),2)[-1][:34]:36}{br(TOT[m]):>12}')
print(f'  {"":42}{"─"*12}')
print(f'  {"SOMA DOS ITENS":<42}{br(sum(TOT.values())):>12}')
if AVISOS:
    print(f'\n⚠ {len(AVISOS)} AVISOS')
    for a in AVISOS: print(f'   · {a}')
print()
if FALHAS:
    print('⛔'*2 + f' {len(FALHAS)} FALHAS — NÃO ENTREGAR')
    for f in FALHAS: print(f'   ⛔ {f}')
    sys.exit(1)
print('✓ nenhuma falha. O levantamento pode virar planilha.')
