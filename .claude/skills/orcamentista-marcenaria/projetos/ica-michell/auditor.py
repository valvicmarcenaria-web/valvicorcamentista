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

# ⛔⛔ A MESMA REGRA VALE PARA OUTRAS, e faltava. O custo() busca o preço com
#   PRECO.get(chave, 0.0): uma chave digitada errado em OUTRAS não quebra
#   nada — ela sai ZERO e o item fica mais barato EM SILÊNCIO. Foi um teste
#   negativo que mostrou o buraco, tentando quebrar outra regra.
#   ⭐ Chave que existe com preço vazio (corrediça de carga, pistão de baú)
#     continua valendo: o zero ali é da Base, declarado, e aparece na aba.
for o in g('OUTRAS'):
    if o[5] not in B.PRECO:
        erro(f'{o[0][:26]} · {o[1]}: chave de OUTRAS fora da Base: "{o[5]}"')
    maior, menor = max(p['c'], p['l']), min(p['c'], p['l'])
    if maior > B.CHAPA_C or menor > B.CHAPA_L:
        erro(f'{r}: {p["c"]:g}×{p["l"]:g} NÃO CABE na chapa')

# ── 2 · gaveta ↔ corrediça ──────────────────────────────────────────────
caixas, corr = {}, {}
for p in PECAS:
    if '· fundo' in p['nome'] and ('avet' in p['nome'] or 'aveta' in p['nome']):
        caixas[p['movel']] = caixas.get(p['movel'], 0) + p['qtd']
for gv in GAVETAS: corr[gv[0]] = corr.get(gv[0], 0) + gv[2]
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
#   ⛔ NEM TODA FRENTE É PORTA: a do leito inferior da bicama CORRE, em
#     corrediça de carga, e não tem dobradiça nenhuma. A regra só olhava
#     GAVETAS para saber se algo corre, e a corrediça de carga entra por
#     OUTRAS. Agora ela olha os dois.
port_mov = {mv for mv, *_ in PORTAS}
corre_mov = {mv for mv, *_ in GAVETAS} | {o[0] for o in g('OUTRAS')
                                          if 'orrediça' in o[5]}
for p in PECAS:
    n = p['nome'].lower()
    # ⛔ moldura usinada carrega o nome da frente mas não é folha
    # ⛔ PORTA DE CORRER NÃO TEM DOBRADIÇA [Closet Master, 28/10]. A folha
    #   do DET 06 corre em trilho, e a regra a acusou de porta sem
    #   dobradiça. A porta de correr da Sala de Cinema só escapou porque
    #   suas peças se chamam "esquadria": era sorte de nome, não regra.
    if ('porta' in n or n.startswith('frente') and 'gavet' not in n) \
       and 'báscula' not in n and 'moldura' not in n and 'leito' not in n \
       and 'correr' not in n \
       and p['movel'] not in port_mov and p['movel'] not in corre_mov:
        erro(f'{p["movel"][:30]} · {p["nome"]}: porta SEM dobradiça')

# ── 5 · báscula ↔ articulador ───────────────────────────────────────────
#   ⭐ báscula não abre com dobradiça: precisa de articulador a gás
# ⛔⛔ A PALAVRA "BÁSCULA" APARECE EM PEÇA QUE NÃO É BÁSCULA. A frente
#   provençal traz a moldura com o mesmo nome da base, e a caixaria traz a
#   "divisória do módulo basculante" — contadas junto, onze básculas viram
#   vinte e quatro. Articulador é por FRENTE, então a regra tem de saber o
#   que é frente: não é a moldura, e não é peça de estrutura. ⭐ A lista de
#   palavras aqui não é chute de acabamento, é o que a peça É: divisória,
#   prateleira, lateral, base, topo e fundo nunca são frente.
ESTRUTURAL = ('divisória', 'prateleira', 'lateral', 'base', 'topo', 'fundo',
              'moldura usinada')
def frente(p):
    n = p['nome'].lower()
    return not any(w in n for w in ESTRUTURAL)
# ⭐ "GAVETÃO BASCULANTE" É BÁSCULA [Closet Master, 28/10]. A palavra na
#   prancha vem sem acento e com outra terminação, e a regra contava zero
#   básculas enquanto o orçamento trazia um articulador. Conta as duas.
nb = sum(p['qtd'] for p in PECAS
         if ('báscula' in p['nome'].lower()
             or 'basculante' in p['nome'].lower()) and frente(p))
na = sum(b[2] for b in BASCULAS)
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
for b in BASCULAS:
    mv = b[0]
    # ⭐ A BÁSCULA PODE ABRIR POR CAVA [Closet Master, 28/10]. Até aqui o
    #   quarto elemento só distinguia slim de puxador; o gavetão basculante
    #   do Armário 01 abre por CAVA, como a prancha escreve, e a regra o
    #   acusava de ter puxador e cava na mesma frente.
    # ⭐ A BÁSCULA TAMBÉM PODE ABRIR POR PULSADOR [Suíte Mariana, 28/10].
    #   As duas básculas da estante têm frente de Palha Indiana emoldurada
    #   em Sal Rosa e nenhum puxador desenhado — é o mesmo caso das portas
    #   ripadas do Banho Gourmet, e a resposta da casa é o pulsador. Sem
    #   esta linha o modo caía no 'puxador' do default e a regra acusava
    #   pulsador e puxador na mesma frente.
    modo = {'slim': 'báscula slim', 'cava': 'cava',
            'pulsador': 'pulsador'}.get(
        b[3] if len(b) > 3 else 'slim', 'puxador')
    abre[mv] = abre.get(mv, set()) | {modo}
# ⭐ A CORREDIÇA TOUCH É UM MODO DE ABRIR [Jonathan, 28/10/2026]: "não
#   precisa de pulsador, a própria corrediça abre". Declarar os dois na
#   mesma gaveta é pagar duas vezes pela mesma abertura.
for gv in GAVETAS:
    if len(gv) > 4 and gv[4] == 'touch':
        abre[gv[0]] = abre.get(gv[0], set()) | {'touch'}
for mv, rot, q in PUXADORES:  abre[mv] = abre.get(mv, set()) | {'puxador'}
for mv, rot, q, c in CAVA:    abre[mv] = abre.get(mv, set()) | {'cava'}
# ⭐ o puxador passante é o terceiro modo, e é o único do projeto — entra
#   por OUTRAS porque é perfil por metro, não peça por frente
for o in g('OUTRAS'):
    # ⭐ qualquer PUXADOR declarado por OUTRAS conta como modo de abrir: o
    #   passante do Quarto é perfil por metro, o de couro da Suíte Hóspedes
    #   é peça por unidade, e os dois abrem a frente do mesmo jeito.
    if 'uxador' in o[5]: abre[o[0]] = abre.get(o[0], set()) | {'puxador'}
    # ⭐ o pulsador é o quarto modo: a frente abre pelo toque, sem ferragem
    #   à vista. É o que a porta ripada do Banho Gourmet pede, e a Base já
    #   avisa que ele NÃO SE SOMA ao slim nem a puxador na mesma frente.
    if o[5] == 'Pulsador': abre[o[0]] = abre.get(o[0], set()) | {'pulsador'}
# ⭐⭐ ITEM UNIFICADO PODE TER DOIS MODOS [Jonathan, 28/10/2026]. Quando o
#   senhor manda unificar o preço de três detalhamentos num item só, o
#   item passa a conter TRÊS móveis — e a bicama abrir por cava enquanto o
#   baú abre por puxador deixa de ser erro, passa a ser leitura. A regra
#   continua valendo dentro de cada móvel; o que o ambiente declara aqui é
#   que aquele item é um CONJUNTO, e a exceção fica escrita, não implícita.
MISTO = set(g('ABRE_MISTO'))
for mv, modos in abre.items():
    if mv in MISTO: continue
    for a_, b_ in (('puxador', 'cava'), ('pulsador', 'puxador'),
                   ('pulsador', 'cava'), ('pulsador', 'báscula slim'),
                   ('touch', 'pulsador'), ('touch', 'puxador'),
                   ('touch', 'cava')):
        if {a_, b_} <= modos:
            erro(f'{mv[:34]}: frente com {a_.upper()} e {b_.upper()} ao '
                 'mesmo tempo — um dos dois sai')
for p in PECAS:
    n = p['nome'].lower()
    if n.startswith('frente') and 'travessa' not in n and not abre.get(p['movel']):
        erro(f'{p["movel"][:30]} · {p["nome"]}: frente sem NENHUM modo de '
             'abrir declarado')

# ── 6c · provençal ↔ travessa ↔ mão de obra ─────────────────────────────
#   ⭐ A frente provençal são DUAS PEÇAS INTEIRAS e uma mão de obra. Se a
#     base de 15 entrar sem a moldura de 6, ou sem a linha de usinagem, o
#     orçamento sai barato e calado.
# ⛔ PROVENÇAL É QUEM TEM TRAVESSA, não quem tem nome de frente. A regra
#   olhava o nome e a espessura, e aí a caixaria em Branco TX 15 e as
#   frentes LISAS caíam na conta junto. Na Lavanderia há uma frente lisa de
#   propósito — a gaveta de 10 cm, onde a travessa de 7 não cabe — e ela
#   quebrava a auditoria sem haver erro nenhum. Agora a pergunta é exata:
#   esta peça tem uma moldura usinada com o nome dela?
# ⛔ A CHAVE É (MÓVEL, NOME), não o nome sozinho: "Frente · porta tempero"
#   existe na ilha E na bancada da Cozinha, em medidas diferentes. Com a
#   chave curta, a moldura de um móvel era comparada com a frente do outro
#   e a regra acusava erro onde não havia. ⭐ Peça só é a mesma peça dentro
#   do mesmo móvel.
MOLD = {(p['movel'], p['nome'][:-len(' · moldura usinada')]): p for p in PECAS
        if p['nome'].endswith(' · moldura usinada')}
base15 = sum(p['qtd'] for p in PECAS if (p['movel'], p['nome']) in MOLD)
# ⭐⭐ A MOLDURA TEM DE TER A MEDIDA DA FRENTE. É o que distingue o método
#   da casa — "outra peça de igual tamanho, usinada na router" — de voltar
#   a montar régua. Se alguém reduzir a moldura a uma tira, a chapa de 6 mm
#   despenca e o orçamento sai barato sem ninguém perceber: esta regra é o
#   que não deixa.
for b in PECAS:
    m = MOLD.get((b['movel'], b['nome']))
    if m and (abs(m['c'] - b['c']) > 0.01 or abs(m['l'] - b['l']) > 0.01
              or m['qtd'] != b['qtd']):
        erro(f'{b["movel"][:22]} · {b["nome"]}: moldura {m["c"]:g}×{m["l"]:g}'
             f'×{m["qtd"]} contra frente {b["c"]:g}×{b["l"]:g}×{b["qtd"]} — '
             'a moldura é peça inteira, de mesma medida, não régua')
trav  = sum(p['qtd'] for p in PECAS if 'moldura usinada' in p['nome'])
mo    = sum(q for mv, rot, q in MOLDURA)
# ⛔ UMA moldura por frente, não duas travessas: a moldura é peça inteira
#   de 6 mm usinada na router [Jonathan, 28/10/2026]
if base15 and trav != base15:
    erro(f'{base15} frentes provençais × {trav} molduras usinadas — '
         'deviam ser uma por folha')
if base15 != mo:
    erro(f'{base15} frentes provençais × {mo} na linha de mão de obra de '
         'moldura — não bate')

# ── 6d · ⛔ PINUS ESTÁ PROIBIDO [Jonathan, 28/10/2026] ──────────────────
#   > "Não usamos peças de pinus para nada."
#   A regra existe porque o sarrafo era cômodo: R$ 8 o metro resolvia
#   qualquer engradado sem desenhar nada. Agora o engradado tem de ser
#   peça — travessa de MDF, `B.engradado()` — ou estrutura de verdade:
#   estrado em metalon na cama, serralheria onde o móvel é suspenso.
if g('SARRAFOS'):
    erro(f'{len(g("SARRAFOS"))} linha(s) de SARRAFO de pinus — a casa não usa '
         'pinus para nada: trocar por engradado de MDF, estrado em metalon '
         'ou serralheria estrutural')
# ── 6e · SUPORTE DE PRATELEIRA NÃO SE DECLARA ──────────────────────────
#   Ele se conta das peças. Uma lista de SUPORTES sobrando é lista velha,
#   e lista velha soma duas vezes.
if g('SUPORTES'):
    erro('SUPORTES declarado à mão — o suporte de prateleira agora sai de '
         'B.prateleiras(), contado das peças. Apagar a lista.')

# ── 6f · a alma de prateleira é CONTA, não acusação ────────────────────
#   ⭐ [Jonathan, 28/10/2026] "prateleiras acima de 1.20mt vamos considerar
#     alma de aço". Como é toda prateleira larga, sem exceção de projeto,
#     ela entra pelo motor (`B.almas_de_prateleira`) e não por lista — a
#     mesma decisão do suporte. O que sobra para o auditor é conferir que
#     ninguém a declarou DUAS vezes, uma na conta e outra na mão.
for mv, rot, q in ALMAS:
    if 'prateleira' in rot.lower():
        erro(f'{mv[:30]}: ALMAS declara prateleira ("{rot[:40]}") — a alma '
             'de prateleira sai de B.almas_de_prateleira(). ALMAS é só para '
             'coluna, montante e pé.')

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
    for gv in GAVETAS:
        if gv[0] == mv:
            t += gv[2]*(B.CORREDICA_TOUCH
                        if len(gv) > 4 and gv[4] == 'touch' else B.CORREDICA)
    for x, rot, nq, nd, pr in PORTAS:
        if x == mv: t += nq*nd*pr
    for b in BASCULAS:
        # ⭐ o slim só entra onde a báscula abre por ele. Na Lavanderia ela
        #   abre pelo Alças Traso, que já vem na linha de PUXADORES.
        if b[0] == mv:
            t += b[2]*B.BASCULA
            if len(b) <= 3 or b[3] == 'slim': t += b[2]*B.SLIM
    for x, rot, q in PUXADORES:
        if x == mv: t += q*B.PUXADOR_128
    for x, rot, q in MOLDURA:
        if x == mv: t += q*B.MOLDURA_MO           # ⛔ zero: a cotar
    for x, rot, q, c in CAVA:
        if x == mv: t += round(q*c/100, 2)*B.CAVA_M
    # ⭐ vidro e espelho na mesma lista; o 6º elemento diz a chave
    for vd in VIDRO:
        if vd[0] == mv:
            ch = vd[5] if len(vd) > 5 else 'Vidro reflecta'
            t += round(vd[2]*vd[3]*vd[4]/10000, 2)*B.PRECO.get(ch, 0.0)
    for x, rot, m in LED:
        if x == mv: t += m*B.LED_M
    for x, rot, q in ALMAS:
        if x == mv: t += q*B.ALMA
    t += B.almas_de_prateleira(PECAS, mv)*B.ALMA
    # ⭐ o suporte de prateleira não se declara: conta-se das peças
    t += B.prateleiras(PECAS, mv)*B.SUPORTE
    for x, nome, rot, q, un, ch in g('OUTRAS'):
        # ⛔ .get: item da Base sem preço entra como ZERO e denuncia, que é
        #   a regra da casa — não quebra a auditoria
        if x == mv: t += q*B.PRECO.get(ch, 0.0)
    for x, rot, q in g('CABIDEIROS'):
        if x == mv: t += q*B.CABIDEIRO
    # ⭐⭐ A SERRALHERIA ENTRA NA CONTA, e até 28/10 ela NÃO entrava: o
    #   custo() não tinha esta linha e a aba buscava um preço de Base que
    #   nunca existiu. Os R$ 2.500 do banco suspenso do Living saíam zero
    #   nos dois lados — e por saírem zero nos dois, a CONFERÊNCIA fechava
    #   e nada gritava. É o tipo de erro que só aparece quando se soma à
    #   mão o que a planilha já somou.
    for x, rot, v_ in g('SERRALHERIA'):
        if x == mv: t += float(v_)
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
