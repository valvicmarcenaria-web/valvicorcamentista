# -*- coding: utf-8 -*-
"""ANDREA — clínica de dermatologia · ADITIVO: laminação em HPL  [24/10/2026]

⭐ [Jonathan 24/10] Os painéis e as portas **já estão prontos na fábrica**.
   O aditivo é revestir todos eles em **laminado de alta pressão (fórmica)
   Carvalho Mel, acabamento Top Matt**, mediante disponibilidade.
   **Investimento: R$ 16.500.** Prazo: 30 dias de execução APÓS o
   recebimento do material, que o fornecedor pede 45 a 60 dias para
   entregar — **cerca de 90 dias no total.**

⛔⛔ O PREÇO É DELE. Este arquivo NÃO calcula preço: ele **inverte a
   pergunta**. Não temos o quantitativo dos painéis da clínica — nunca
   passou por aqui. Então, em vez de fingir um custo, eu pergunto:

     **até quanto de painel os R$ 16.500 cobrem, sem furar a margem?**

   É o que protege a casa num aditivo fechado por valor cheio: se a área
   real passar do ponto, o aditivo vira prejuízo silencioso.

⛔ SEM RT E SEM COMISSÃO DE VENDEDOR na cascata — é serviço de correção
   dentro de um contrato que já existe. ⚠ Se houver RT para a parceira,
   avisar: muda a base de 85,35% para 76,52% e derruba a área coberta.

★★ TODOS os insumos abaixo são estimativa minha. HPL não está na base da
   casa — a base só tem laminado em chapa melamínica, que é outro produto.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
vg  = lambda v, n=1: f'{v:.{n}f}'.replace('.', ',')

PV      = 16500.0          # ⭐ [Jonathan 24/10] investimento fechado por ele
MC_PISO = M.MC_PISO        # 35%
RT_ON   = False            # ⚠ ver cabeçalho
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ── insumos · TUDO ★ ────────────────────────────────────────────────────
LAM_M2, LAM_PRECO = 3.08*1.25, 650.0   # lâmina de HPL 3080 × 1250 = 3,85 m²
LAM_APROV = 0.82                        # recorte de lâmina rende mais que chapa
COLA_LATA, COLA_REND = 120.0, 10.0      # lata de 2,8 kg · m² de painel por lata
FITA_M, FITA_POR_M2 = 8.0, 3.0          # fita no padrão · m de topo por m² de face
LIXA_M2 = 14.0                          # lixa, estopa e solvente, por m²
# ⭐⭐ A MÃO É O CUSTO, NÃO A FÓRMICA. Laminar painel PRONTO é pior do que
#   laminar peça crua: a superfície tem de ser lixada até pegar poros, a
#   lâmina vai colada à mão sobre peça montada, e o topo é relaminado
#   depois. Nada disso passa pela CNC. Mesma lição da palha e da malha.
MO_M2    = 190.0                        # lixar, cortar, colar, desbastar, fitar
INSTALA  = 900.0                        # desmontagem, transporte e reinstalação

def custo(a_m2):
    """Custo direto para `a_m2` de FACE de painel a revestir."""
    laminas = -(-a_m2/(LAM_M2*LAM_APROV)//1)
    lam     = laminas*LAM_PRECO
    cola    = -(-a_m2/COLA_REND//1)*COLA_LATA
    fita    = a_m2*FITA_POR_M2*FITA_M
    lixa    = a_m2*LIXA_M2
    mat     = lam + cola + fita + lixa
    mo      = a_m2*MO_M2 + INSTALA
    cons    = mat*0.06
    sub     = mat + cons + mo
    return dict(laminas=laminas, lam=lam, cola=cola, fita=fita, lixa=lixa,
                mat=mat, mo=mo, cons=cons, emb=sub*M.EMBALAGEM,
                cd=sub*(1 + M.EMBALAGEM))

def mc(a_m2):  return BASE - custo(a_m2)['cd']/PV

def area_para(mc_alvo, lo=1.0, hi=400.0):
    """Maior área que ainda entrega `mc_alvo` a R$ 16.500 — busca binária."""
    if mc(lo) < mc_alvo: return 0.0
    for _ in range(60):
        meio = (lo + hi)/2
        lo, hi = (meio, hi) if mc(meio) >= mc_alvo else (lo, meio)
    return lo

A_PISO, A_40, A_ZERO = area_para(MC_PISO), area_para(0.40), area_para(0.0)

# ⛔⛔ TRAVAS
assert PV == 16500.0, '⛔ O INVESTIMENTO NÃO É MAIS O DO JONATHAN'
assert A_40 < A_PISO < A_ZERO, '⛔ AS ÁREAS SAÍRAM FORA DE ORDEM'
assert mc(A_PISO) > 0, '⛔ A CONTA NÃO FECHA NEM NO PISO'

if __name__ == '__main__':
    W = 82
    print('═'*W)
    print('ANDREA · CLÍNICA DE DERMATOLOGIA — ADITIVO DE LAMINAÇÃO EM HPL')
    print(f'investimento ⭐ R$ {br(PV)} · sem RT · base {BASE*100:.2f}%')
    print('═'*W)
    print('\n⛔⛔ NÃO TEMOS O QUANTITATIVO DOS PAINÉIS DA CLÍNICA.')
    print('  Eles foram produzidos fora deste repositório. Sem área, não há')
    print('  custo — então a pergunta vira: ATÉ QUANTO DE PAINEL OS')
    print(f'  R$ {br(PV)} COBREM?')

    print(f'\n{"═"*W}')
    print('A RESPOSTA')
    print(f'{"═"*W}')
    print(f'  {"a 40% de MC — topo da faixa ideal":<44}até {vg(A_40):>6} m² de face')
    print(f'  {f"a {MC_PISO:.0%} de MC — piso da casa":<44}até {vg(A_PISO):>6} m² de face')
    print(f'  {"empate · MC zero":<44}até {vg(A_ZERO):>6} m² de face')
    print(f'\n  ⭐ A LEITURA PRÁTICA: uma porta de clínica dá cerca de 1,6 m²')
    print(f'    de face, contando os dois lados. Nos {vg(A_PISO)} m² do piso cabem')
    print(f'    por volta de {A_PISO/1.6:.0f} portas — ou o equivalente em painel.')
    print(f'    ⚠ Se o conjunto da clínica passar disso, os R$ {br(PV)} deixam')
    print(f'      de pagar o piso da casa, e ninguém percebe pela folha.')

    print(f'\n{"═"*W}')
    print(f'ABERTURA DO CUSTO — no ponto de piso ({vg(A_PISO)} m²)')
    print(f'{"═"*W}')
    c = custo(A_PISO)
    for rot, k in [('lâmina de HPL Carvalho Mel Top Matt', 'lam'),
                   ('cola de contato · duas demãos nos dois materiais', 'cola'),
                   ('fita de borda para relaminar os topos', 'fita'),
                   ('lixa, estopa e solvente', 'lixa'),
                   ('consumíveis · 6%', 'cons'),
                   ('mão de obra e reinstalação', 'mo'),
                   ('embalagem · 2%', 'emb')]:
        print(f'  {rot:<50}R$ {br(c[k]):>7}')
    print('  ' + '─'*60)
    print(f'  {"CUSTO DIRETO":<50}R$ {br(c["cd"]):>7}')
    print(f'  {"INVESTIMENTO ⭐ dele":<50}R$ {br(PV):>7}')
    print(f'  {"MC":<50}{mc(A_PISO)*100:>9.1f}%')
    print(f'\n  ⭐⭐ A FÓRMICA É {c["lam"]/c["cd"]*100:.0f}% DO CUSTO. A mão de obra é '
          f'{c["mo"]/c["cd"]*100:.0f}%.')
    print('    Laminar painel PRONTO é mais caro que laminar peça crua: a')
    print('    superfície precisa ser lixada até pegar poros, a lâmina vai')
    print('    colada à mão sobre peça já montada e o topo é relaminado')
    print('    depois. Nada disso passa pela CNC — é a mesma lição da palha')
    print('    natural e da malha de corda.')

    print(f'\n{"═"*W}')
    print('A SENSIBILIDADE')
    print(f'{"═"*W}')
    print(f'  {"área de face":>12}{"custo direto":>16}{"MC":>10}')
    print('  ' + '─'*38)
    for a in (20, 30, 40, 50, 60, 70, 80):
        m = mc(a)
        mk = ''
        if m < 0: mk = '  ⛔ prejuízo'
        elif m < MC_PISO: mk = '  ⚠ abaixo do piso'
        print(f'  {vg(a):>9} m²  R$ {br(custo(a)["cd"]):>11}{m*100:>9.1f}%{mk}')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    print('  · ⛔⛔ A ÁREA REAL DOS PAINÉIS E PORTAS. É o único número que')
    print('    falta, e é o que decide se este aditivo dá lucro ou prejuízo.')
    print('    A fábrica tem a relação de peças — basta somar as faces.')
    print(f'  · ★★ LÂMINA DE HPL CARVALHO MEL TOP MATT a R$ {br(LAM_PRECO)}. HPL não')
    print('    está na base da casa, e Top Matt é acabamento supermatte,')
    print('    acima do laminado comum. ⚠ "Mediante disponibilidade" está no')
    print('    briefing do Jonathan e PRECISA ficar na folha: padrão de')
    print('    importação costuma ter janela de estoque.')
    print(f'  · ★ MÃO DE OBRA a R$ {br(MO_M2)}/m² de face. É a maior linha da conta')
    print('    e a mais incerta — depende de quanto o painel já montado')
    print('    atrapalha o acesso às faces. ⭐ E é a que mais move a resposta:')
    for _mo in (120.0, 150.0, 190.0, 230.0):
        globals()['MO_M2'] = _mo
        print(f'      mão a R$ {br(_mo)}/m²  →  piso da casa até '
              f'{vg(area_para(MC_PISO))} m² de face')
    globals()['MO_M2'] = 190.0
    print('  · ⚠ OS TOPOS. "Relaminação dos topos com fita de borda" entra')
    print('    como fita no padrão. Se a arquiteta pedir topo em HPL dobrado')
    print('    (postforming), é outra conta e outro fornecedor.')
    print(f'  · ⚠ RT. Orçado SEM. Se houver RT para a parceira, a base cai de')
    print(f'    {BASE*100:.2f}% para {M.base(0, True, False)*100:.2f}% e a área coberta no piso '
          f'desce de {vg(A_PISO)}')
    _b = M.base(0, True, False)
    _f = lambda a: _b - custo(a)['cd']/PV
    lo, hi = 1.0, 400.0
    for _ in range(60):
        meio = (lo + hi)/2
        lo, hi = (meio, hi) if _f(meio) >= MC_PISO else (lo, meio)
    print(f'    para {vg(lo)} m².')
    print('  · ⚠ DESMONTAGEM E REINSTALAÇÃO entram na conta como conjunto.')
    print('    Se as peças já estiverem instaladas na clínica, e não na')
    print('    fábrica, é obra em ambiente de atendimento — outro custo e')
    print('    outro prazo.')
