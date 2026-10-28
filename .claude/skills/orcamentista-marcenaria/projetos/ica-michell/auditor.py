# -*- coding: utf-8 -*-
"""Confere o levantamento de um ambiente ANTES de ele virar planilha.

⛔⛔ [Jonathan 28/10] "sempre revise antes de entregar os resultados."

   Oito correções numa rodada só, no Living. Quase todas eram coisas que uma
   conferência MECÂNICA teria pegado: frente sem dobradiça, gaveta sem
   corrediça, peça de largura que não existe, linha que soma e outra que
   subtrai a mesma área. ⭐ A revisão não pode depender de eu lembrar — tem
   de quebrar.

   uso:  python3 auditor.py living
         python3 auditor.py cozinha aba.json
"""
import sys, json, importlib.util, pathlib, io, contextlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P))
import base as B

NOME = sys.argv[1] if len(sys.argv) > 1 else 'living'
sp = importlib.util.spec_from_file_location('AMB', P/f'{NOME}.py')
A = importlib.util.module_from_spec(sp); sys.modules['AMB'] = A
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(A)

PECAS = getattr(A, NOME.upper(), None) or getattr(A, 'PECAS')
g = lambda n: getattr(A, n, [])
GAVETAS, PORTAS, CAVA = g('GAVETAS'), g('PORTAS'), g('CAVA')
LED, ALMAS, SUPORTES = g('LED'), g('ALMAS'), g('SUPORTES')
VIDRO, BASCULAS = g('VIDRO'), g('BASCULAS')
PUXADORES, MOLDURA = g('PUXADORES'), g('MOLDURA')
MOV = list(dict.fromkeys(p['movel'] for p in PECAS))

br = lambda v: f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
FALHAS, AVISOS = [], []
erro, aviso = FALHAS.append, AVISOS.append

# ⭐ a lista de chaves válidas sai da BASE, não de um rol digitado aqui:
#   chave inventada no ambiente tem de quebrar, não passar.
CHAVES = set(B.PRECO) | set(B.PRECO_ACAB) | {'Fita', 'Corrediça', 'Dobradiça',
    'Dobradiça vidro', 'Báscula HK-XS', 'Puxador slim', 'Cava usinada',
    'Puxador Alças Traso 128', 'Moldura provençal', 'LED conjunto',
    'Alma de aço', 'Suporte oculto', 'Vidro reflecta'}

# ── 1 · as peças ────────────────────────────────────────────────────────
for p in PECAS:
    r = f"{p['movel'][:26]} · {p['nome']}"
    if p['c'] <= 0 or p['l'] <= 0: erro(f'{r}: dimensão zero ou negativa')
    if p['qtd'] <= 0: erro(f'{r}: quantidade zero ou NEGATIVA — linha que '
                           'subtrai área não é peça')
    if p['chave'] not in CHAVES: erro(f'{r}: chave fora da Base: "{p["chave"]}"')
    maior, menor = max(p['c'], p['l']), min(p['c'], p['l'])
    if maior > B.CHAPA_C or menor > B.CHAPA_L:
        erro(f'{r}: {p["c"]:g}×{p["l"]:g} NÃO CABE na chapa')

# ── 2 · gaveta ↔ corrediça ──────────────────────────────────────────────
caixas, corr = {}, {}
for p in PECAS:
    if '· fundo' in p['nome'] and ('avet' in p['nome'] or 'aveta' in p['nome']):
        caixas[p['movel']] = caixas.get(p['movel'], 0) + p['qtd']
for mv, rot, q, mm in GAVETAS: corr[mv] = corr.get(mv, 0) + q
for mv in set(caixas) | set(corr):
    if caixas.get(mv, 0) != corr.get(mv, 0):
        erro(f'{mv[:34]}: {caixas.get(mv,0)} caixas de gaveta × '
             f'{corr.get(mv,0)} pares de corrediça — não bate')

# ── 3 · frente com cava ↔ metro de cava ─────────────────────────────────
cava_mov = {mv for mv, *_ in CAVA}
for p in PECAS:
    if 'cava' in p['obs'].lower() and p['movel'] not in cava_mov:
        erro(f'{p["movel"][:30]} · {p["nome"]}: diz "cava" e o móvel não tem '
             'metro de cava declarado')

# ── 4 · porta ↔ dobradiça ───────────────────────────────────────────────
port_mov = {mv for mv, *_ in PORTAS}
for p in PECAS:
    n = p['nome'].lower()
    # ⛔ travessa de moldura carrega o nome da frente mas não é folha
    if ('porta' in n or n.startswith('frente') and 'gavet' not in n) \
       and 'báscula' not in n and 'travessa' not in n \
       and p['movel'] not in port_mov:
        erro(f'{p["movel"][:30]} · {p["nome"]}: porta SEM dobradiça')

# ── 5 · báscula ↔ articulador ───────────────────────────────────────────
#   ⭐ báscula não abre com dobradiça: precisa de articulador a gás
nb = sum(p['qtd'] for p in PECAS if 'báscula' in p['nome'].lower())
na = sum(q for mv, rot, q in BASCULAS)
if nb != na:
    erro(f'{nb} básculas desenhadas × {na} articuladores orçados — não bate')

# ── 6 · vidro ↔ dobradiça de vidro ──────────────────────────────────────
vid_mov = {mv for mv, *_ in VIDRO}
for mv, rot, nq, nd, pr in PORTAS:
    if pr == B.DOBR_VIDRO and mv not in vid_mov:
        erro(f'{mv[:30]}: dobradiça de vidro sem a FOLHA DE VIDRO declarada')

# ── 6b · TODA FRENTE ABRE DE UM MODO SÓ ─────────────────────────────────
#   ⭐⭐ A regra que faltava. A prancha do ICA pedia puxador Alças Traso E
#     cava usinada na mesma frente, e isso ficou dois dias como nota de
#     texto em nunca-orcei.md em vez de quebrar a auditoria. Báscula com
#     pulsador E slim é o mesmo erro, e a Base já avisava dele.
abre = {}
for mv, rot, q in BASCULAS:   abre[mv] = abre.get(mv, set()) | {'báscula slim'}
for mv, rot, q in PUXADORES:  abre[mv] = abre.get(mv, set()) | {'puxador'}
for mv, rot, q, c in CAVA:    abre[mv] = abre.get(mv, set()) | {'cava'}
for mv, modos in abre.items():
    if {'puxador', 'cava'} <= modos:
        erro(f'{mv[:34]}: frente com PUXADOR e CAVA ao mesmo tempo — '
             'um dos dois sai')
for p in PECAS:
    n = p['nome'].lower()
    if n.startswith('frente') and 'travessa' not in n and not abre.get(p['movel']):
        erro(f'{p["movel"][:30]} · {p["nome"]}: frente sem NENHUM modo de '
             'abrir declarado')

# ── 6c · provençal ↔ travessa ↔ mão de obra ─────────────────────────────
#   ⭐ A frente provençal são DUAS chapas e uma mão de obra. Se a base de
#     15 entrar sem as travessas de 6, ou sem a linha de moldura, o
#     orçamento sai barato e calado.
base15 = sum(p['qtd'] for p in PECAS
             if p['chave'].endswith(' 15') and p['nome'].lower().startswith('frente')
             or p['chave'].endswith(' 15') and 'porta de giro' in p['nome'].lower())
trav  = sum(p['qtd'] for p in PECAS if 'travessa deitada' in p['nome'])
mo    = sum(q for mv, rot, q in MOLDURA)
if base15 and trav != 2*base15:
    erro(f'{base15} frentes provençais × {trav} travessas deitadas — '
         f'deviam ser {2*base15}, duas por folha')
if base15 != mo:
    erro(f'{base15} frentes provençais × {mo} na linha de mão de obra de '
         'moldura — não bate')

# ── 7 · peça sem fita, com justificativa? ───────────────────────────────
for p in PECAS:
    if p['fita'] == (0, 0) and not p['chave'].endswith(' 6') \
       and 'sem fita' not in p['obs'].lower():
        aviso(f'{p["movel"][:30]} · {p["nome"]}: sem fita e sem justificativa '
              'no texto — foi decisão ou esquecimento?')

# ── 8 · o custo de cada item ────────────────────────────────────────────
def custo(mv):
    # ⭐ toda chave está na Base agora: nada de replace() para achar preço
    # ⛔ .get e não [ ]: chave inválida já foi acusada na regra 1, e o
    #   auditor tem de chegar ao RELATÓRIO para dizer isso. Morrer de
    #   KeyError antes de imprimir esconde a falha em vez de mostrá-la.
    t = sum(p['c']*p['l']*p['qtd']/10000/(B.CHAPA_M2*B.APROV)
            * B.PRECO.get(p['chave'], 0.0)
            for p in PECAS if p['movel'] == mv)
    for ch, m in B.acabamento(PECAS, mv).items():
        t += m * B.PRECO_ACAB[ch]
    for x, rot, q, mm in GAVETAS:
        if x == mv: t += q*B.CORREDICA
    for x, rot, nq, nd, pr in PORTAS:
        if x == mv: t += nq*nd*pr
    for x, rot, q in BASCULAS:
        if x == mv: t += q*(B.BASCULA + B.SLIM)   # ⭐ slim, não pulsador
    for x, rot, q in PUXADORES:
        if x == mv: t += q*B.PUXADOR_128
    for x, rot, q in MOLDURA:
        if x == mv: t += q*B.MOLDURA_MO           # ⛔ zero: a cotar
    for x, rot, q, c in CAVA:
        if x == mv: t += round(q*c/100, 2)*B.CAVA_M
    for x, rot, q, c, l in VIDRO:
        if x == mv: t += round(q*c*l/10000, 2)*B.VIDRO_M2
    for x, rot, m in LED:
        if x == mv: t += m*B.LED_M
    for x, rot, q in ALMAS:
        if x == mv: t += q*B.ALMA
    for x, rot, q in SUPORTES:
        if x == mv: t += q*B.SUPORTE
    return t

TOT = {m: custo(m) for m in MOV}
for m, v in TOT.items():
    if v <= 0: erro(f'{m[:34]}: custo zero ou negativo')

# ── 9 · contra a aba, se vier ───────────────────────────────────────────
if len(sys.argv) > 2:
    aba = json.load(open(sys.argv[2]))
    for i, m in enumerate(MOV, 1):
        k = f'{i:02d}'
        if k not in aba: erro(f'ITEM {k} não veio da aba'); continue
        d = abs(aba[k] - TOT[m])
        if d > 0.05:
            erro(f'ITEM {k} {m[:24]}: aba {br(aba[k])} × script {br(TOT[m])} '
                 f'— difere {br(d)}')

# ── relatório ───────────────────────────────────────────────────────────
W = 76
print('═'*W); print(f'AUDITORIA DO LEVANTAMENTO · {NOME.upper()}'); print('═'*W)
print(f'\n{len(PECAS)} peças · {len(MOV)} itens · '
      f'{len({p["chave"] for p in PECAS if p["chave"].startswith("MDF")})} padrões de chapa\n')
for i, m in enumerate(MOV, 1):
    print(f'  ITEM {i:02d}  {m.split(" ",2)[-1][:40]:42}{br(TOT[m]):>12}')
print(f'  {"":48}{"─"*12}')
print(f'  {"SOMA DOS ITENS":<48}{br(sum(TOT.values())):>12}')
if ALTAS := B.ALTAS:
    print(f'\n⛔ {len(ALTAS)} peça(s) desenhada(s) acima dos {B.ALT_MAX:g} cm da chapa:')
    for mv, n, a, q in ALTAS: print(f'   {mv[:34]:36}{n:24}{a:g} cm × {q}')
if AVISOS:
    print(f'\n⚠ {len(AVISOS)} AVISOS')
    for a in AVISOS: print(f'   · {a}')
print()
if FALHAS:
    print('⛔⛔ ' + f'{len(FALHAS)} FALHAS — NÃO ENTREGAR')
    for f in FALHAS: print(f'   ⛔ {f}')
    sys.exit(1)
print('✓ nenhuma falha. O levantamento pode virar planilha.')
