# -*- coding: utf-8 -*-
"""MICHELLE E ARLEI — casa completa  [18/10/2026]

Projeto executivo **INÉDITA ARQUITETURA** (CAU A6346-6), 11/12/2024, R00,
22 pranchas A2. Residencial completo: sala, cozinha, área gourmet,
lavanderia, dois banhos, três quartos e closet da suíte.

⛔⛔ **26 MÓVEIS (M01…M26) EM CINCO CORES DE MDF.** É o maior levantamento
   da casa até aqui. As cinco cores:
     · **Gianduia Natural, Duratex** — M01, M04, M05, M08, M23
     · **Itapuã, Duratex**           — M02, M03, M06, M07, M09, M11(prat. e
       escrivaninha), M19, M20(prat.), M21, M22, M24, M25, M26
     · **Areia, Guararapes**         — M10, M20(ripado), M21(parte)
     · **Brisa, Guararapes**         — M11(painel), M12, M13, M14, M16,
       M17, M18(painel e portas)
     · **Alecrim, Guararapes**       — M15, M18(armário sup. e escrivaninha)
   ⭐ Cada cor × espessura tem o próprio mínimo de uma chapa. Cinco cores
     não dividem chapa entre si — é o que faz este orçamento ser o que é.

AS NOTAS DA PRANCHA (repetidas em todas as folhas de detalhe):
  1. Obrigatoriamente conferir medidas no local
  2. Marcenaria com **furação oculta**, cavilhas só nas áreas internas
  3. Dobradiças de giro com **abertura de 90° e amortecedor**
  4. Gavetas com **corrediça telescópica reforçada e amortecedor**
  5. Puxador **tipo cava** (usinado na própria peça) — ver detalhe
  6. Observar pontos de tomada para recorte no móvel

⭐ [Jonathan 18/10] **"vamos orçar na linha ESSENCIAL com 35% de MC e com
   RT."** ⭐ [Jonathan 19/10] **"vamos subir para 40% a MC."** — o topo da
   faixa ideal da casa (35–40%). A linha Essencial, neste projeto, é:
     · **interior e caixaria em Branco TX**, cor só onde aparece
     · **corrediça telescópica** com amortecedor — é o que a prancha pede
     · **dobradiça com amortecedor a R$ 12**, a nacional da casa
     · **fita e perfil de LED comuns**, não a linha profissional
     · **garantia de 2 anos**
   ⚠ O QUE A LINHA **NÃO** MEXE: as cinco cores de MDF são especificação
     da arquiteta, peça por peça. Trocá-las não é mudar de linha, é mudar
     de projeto — e não foi pedido.
★ INTERIOR: o projeto diz "armário em MDF <cor>" e não fala do miolo. Na
  Essencial o miolo vai em Branco TX; o cenário "tudo na cor" está
  calculado ao lado, no relatório.
"""
import importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('motor_mc', P/'motor_mc.py')
M = importlib.util.module_from_spec(spec); sys.modules['motor_mc'] = M
spec.loader.exec_module(M)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
vg  = lambda v, n=2: f'{v:.{n}f}'.replace('.', ',')

CH_M2, APROV = 2.75*1.85, 0.80
LINHA   = 'essencial'                # ⭐ [Jonathan 18/10]
RT_ON   = True                       # ⭐ [Jonathan 18/10] "e com RT"
BASE    = M.base(parcelas=0, rt=RT_ON, vendedor=False)

# ── preço de chapa, por cor e espessura ─────────────────────────────────
BR   = {6: 190.0, 15: 260.0, 18: 330.0}     # Branco TX — base da casa
COR  = {6: 300.0, 15: 500.0, 18: 600.0}     # MDF de cor — base da casa
CORES = ('Gianduia', 'Itapuã', 'Areia', 'Brisa', 'Alecrim')
FITA_BR, FITA_COR = 2.0 + 2.5, 3.0 + 2.5

# ── ferragem, por unidade · DUAS LINHAS ─────────────────────────────────
# ⭐ [Jonathan 19/10] "apresente de forma sucinta a versão na linha premium
#   da Hettich, mostrando a vantagem de tempo de garantia."
# ⛔ A GARANTIA É A DA CORREDIÇA, e é ela que muda:
#     telescópica → 2 anos  ·  oculta Hettich → 10 anos
#   (referencias/proposta-comercial.md, corrigido por Jonathan em 07/08;
#    a oculta HARDT é que dá 5 — a Hettich é a linha Gold da casa.)
# ⭐ [Jonathan 19/10] "a MC da premium vamos subir para 43%." Cada linha
#   passa a ter a PRÓPRIA margem — a Premium não é só ferragem mais cara,
#   é também mais margem. ⚠ 43% está ACIMA da faixa ideal da casa (35–40%).
LINHAS = {
 'essencial': dict(dobr=12.0,  corr=85.0,  basc=60.0,  toque=25.0,
                   correr=420.0, led=65.0, garantia='2 anos',  mc=0.40),
 'premium':   dict(dobr=35.0,  corr=190.0, basc=185.0, toque=45.0,
                   correr=620.0, led=85.0, garantia='10 anos', mc=0.43),
}
CABIDE   = 60.0     # cabideiro, por metro de vão — igual nas duas
MC_ALVO  = LINHAS[LINHA]['mc']       # a MC da linha adotada
# ⭐ PUXADOR CAVA NÃO É FERRAGEM: é usinagem na própria peça. Não entra
#   aqui — entra no tempo de fabricação, que a cascata já carrega.

# ── terceiros e serviços ────────────────────────────────────────────────
# LED: fita + perfil + usinagem da cava + instalação, por metro — por linha
SERRALHA_M = 180.0  # ★ estrutura metálica preta, por metro linear
RODAPE_M   = 95.0   # ★ perfil L de alumínio abas desiguais, por metro
ESTOFADO   = 95.0   # ★ tecido do banco do closet, por m²
TOMADA_CX  = 260.0  # caixa de tomada embutida na marcenaria
SUPORTE_TV = 180.0  # ★ apoio/reforço para suporte de TV

# ════════════════════════════════════════════════════════════════════════
# AS PEÇAS
#   a(amb, móvel, esp, desc, c, l, q, cor, fc)
#     cor = nome da cor  → peça aparente, paga chapa de cor
#     cor = 'int'        → miolo/interior, Branco TX (ou a cor, no cenário B)
#     fc  = 2 fita nos quatro lados · 1 fita só na frente
# ════════════════════════════════════════════════════════════════════════
PCS, FER, TER, LED, AMB_DE = [], {}, {}, {}, {}
FER_KEYS = ('dobr', 'corr', 'basc', 'toque', 'cabide', 'correr')
def fer_un(linha):
    d = dict(LINHAS[linha]); d['cabide'] = CABIDE
    return {k: d[k] for k in FER_KEYS}
FER_UN = fer_un(LINHA)      # a linha adotada, para quem só quer um número

def mov(amb, mv):
    AMB_DE[mv] = amb
    FER.setdefault(mv, dict.fromkeys(FER_UN, 0))
    TER.setdefault(mv, 0.0); LED.setdefault(mv, 0.0)

def a(mv, esp, desc, c, l, q, cor, fc=2):
    PCS.append((mv, esp, desc, c, l, q, cor, fc))
def f(mv, **kw):
    for k, v in kw.items(): FER[mv][k] += v
def ter(mv, v): TER[mv] += v
def led(mv, m): LED[mv] += m

def caixa(mv, larg, alt, prof, cor, prats=0, fundo=True, aberto=False):
    """Caixaria padrão: duas laterais, base e tampo, fundo e prateleiras.
    ⭐ Laterais e horizontais em 15; o que aparece de frente é a fita.
    ⛔⛔ `aberto=True` → NÃO HÁ MIOLO ESCONDIDO. Num móvel sem porta, a
      caixaria É o acabamento: prateleira, lateral e fundo ficam à vista e
      têm de sair na cor do projeto, não em Branco TX. Foi o render do
      closet que mostrou isso — a prancha não diz, e a linha Essencial
      teria entregado um closet aberto branco por dentro."""
    c = cor if aberto else 'int'
    i = larg - 3.0
    a(mv, 15, 'Lateral',         alt, prof, 2, c, 1)
    a(mv, 15, 'Base e tampo',      i, prof, 2, c, 1)
    if prats: a(mv, 15, 'Prateleira', i, prof-2, prats, c, 1)
    if fundo: a(mv, 6, 'Fundo',   larg, alt, 1, c, 0)

def porta(mv, larg, alt, q, cor, dobr=2):
    a(mv, 18, 'Porta de giro · puxador cava', larg, alt, q, cor)
    f(mv, dobr=q*dobr)

def gaveta(mv, larg, alt, prof, q, cor):
    a(mv, 18, 'Frente de gaveta · puxador cava', larg, alt, q, cor)
    a(mv, 15, 'Gaveta · laterais',      prof-6, alt-4, 2*q, 'int', 1)
    a(mv, 15, 'Gaveta · frente e fundo', larg-8, alt-4, 2*q, 'int', 1)
    a(mv,  6, 'Gaveta · fundo',          larg-8, prof-8, q, 'int', 0)
    f(mv, corr=q)

def ripado(mv, larg, alt, cor, ripa=2.0, vao=2.0):
    """Painel ripado: base em 15 na cor e ripas de 18 coladas por cima.
    ⛔ A ripa de 2×2 do projeto sai de chapa de 18 mm — fica 18, não 20.
      É a construção da casa; se a arquiteta quiser 20 cheios, é sarrafo."""
    a(mv, 15, 'Painel ripado · base',  larg, alt, 1, cor, 1)
    a(mv, 18, 'Painel ripado · ripas', larg*ripa/(ripa+vao)*1.10, alt, 1, cor, 0)

# ════════════════════════════════════════════════════════════════════════
# SALA
# ════════════════════════════════════════════════════════════════════════
mov('Sala', 'M01')          # painel de TV liso e ripado + rack suspenso
a('M01', 18, 'Painel liso',               210, 205, 1, 'Gianduia')
ripado('M01', 70, 205, 'Gianduia', ripa=3.0, vao=1.5)   # ⭐ det. da prancha
a('M01', 18, 'Retorno lateral do painel',  22, 205, 1, 'Gianduia')
caixa('M01', 280, 25, 40, 'Gianduia', fundo=True)
gaveta('M01', 70, 25, 40, 4, 'Gianduia')
a('M01', 18, 'Puxador passante · perfil em MDF', 280, 4, 2, 'Gianduia', 1)
ter('M01', SUPORTE_TV)
# ⛔ "ponto de iluminação (arandela) a ser transferido para marcenaria"

# ════════════════════════════════════════════════════════════════════════
# COZINHA
# ════════════════════════════════════════════════════════════════════════
mov('Cozinha', 'M02')       # bancada de lanche, 5 cm de espessura
a('M02', 18, 'Bancada de lanche · duas camadas', 236, 45, 2, 'Itapuã')
a('M02', 15, 'Bancada · sarrafo de alma',        236,  8, 2, 'int', 0)

mov('Cozinha', 'M03')       # prateleira iluminada, 3 cm, 3,23 m
a('M03', 18, 'Prateleira · duas camadas', 323, 45, 2, 'Itapuã')
led('M03', 3.23)

mov('Cozinha', 'M04')       # armário inferior em "U", 6 portas de giro
for _l in (120, 134, 156):
    caixa('M04', _l, 75, 60, 'Gianduia', prats=1)
porta('M04', 60, 75, 6, 'Gianduia')
gaveta('M04', 50, 20, 60, 4, 'Gianduia')      # gavetões e gavetas da v.03
gaveta('M04', 15, 20, 60, 2, 'Gianduia')      # temperos e pano de prato
a('M04', 15, 'Sócalo em alvenaria · fechamento', 410, 10, 1, 'int', 1)

mov('Cozinha', 'M22')       # torre quente: básculas, micro-ondas e forno
# ⛔ Os nichos de forno e de micro-ondas são ABERTOS: o que os forra aparece.
caixa('M22', 155, 250, 70, 'Itapuã', prats=4, aberto=True)
a('M22', 18, 'Báscula · puxador cava',  66, 51, 1, 'Itapuã')
a('M22', 18, 'Báscula · puxador cava',  81, 51, 1, 'Itapuã')
a('M22', 18, 'Báscula · puxador cava',  66, 48, 1, 'Itapuã')
f('M22', basc=3)
gaveta('M22', 151, 26, 70, 1, 'Itapuã')
ter('M22', 0.0)   # nichos de forno e micro-ondas são vão, não peça

mov('Cozinha', 'M23')       # armário superior, 4 portas de giro
caixa('M23', 180, 75, 45, 'Gianduia', prats=2)
porta('M23', 44, 75, 4, 'Gianduia')

mov('Cozinha', 'M26')       # estrutura metálica preta + 2 cachepôs
a('M26', 15, 'Cachepô de temperos · caixa', 44, 25, 2, 'Itapuã')
a('M26', 15, 'Cachepô · laterais e fundo',  25, 20, 6, 'Itapuã', 1)
ter('M26', 1.70*2*SERRALHA_M)      # dois montantes do piso ao teto

# ════════════════════════════════════════════════════════════════════════
# ÁREA GOURMET
# ════════════════════════════════════════════════════════════════════════
mov('Área gourmet', 'M05')  # 2 portas ripadas + gaveta de espetos
caixa('M05', 128, 75, 60, 'Gianduia', prats=1)
ripado('M05', 49, 71, 'Gianduia'); ripado('M05', 49, 71, 'Gianduia')
f('M05', dobr=4)
gaveta('M05', 26, 71, 60, 1, 'Gianduia')      # gaveta vertical de espetos
a('M05', 15, 'Sócalo · fechamento', 128, 10, 1, 'int', 1)

# ════════════════════════════════════════════════════════════════════════
# LAVANDERIA
# ════════════════════════════════════════════════════════════════════════
mov('Lavanderia', 'M06')    # mesa de apoio, estrutura metálica preta
a('M06', 18, 'Tampo',      50, 40, 1, 'Itapuã')
a('M06', 18, 'Prateleira', 50, 40, 1, 'Itapuã')
ter('M06', 0.90*4*SERRALHA_M)

mov('Lavanderia', 'M07')    # armário de básculas iluminado + prateleira
caixa('M07', 165, 48, 40, 'Itapuã', prats=0)
a('M07', 18, 'Báscula · puxador cava', 54, 42, 3, 'Itapuã')
f('M07', basc=3)
a('M07', 18, 'Prateleira iluminada · duas camadas', 146, 20, 2, 'Itapuã')
led('M07', 3.11)            # sob as básculas e sob a prateleira

mov('Lavanderia', 'M08')    # armário inferior, 6 portas de giro
caixa('M08', 220, 75, 57, 'Gianduia', prats=2)
porta('M08', 36, 75, 6, 'Gianduia')
a('M08', 15, 'Sócalo · fechamento', 220, 10, 1, 'int', 1)

# ════════════════════════════════════════════════════════════════════════
# BANHOS
# ════════════════════════════════════════════════════════════════════════
mov('Banho social', 'M09')
caixa('M09', 130, 50, 35, 'Itapuã', prats=1)
porta('M09', 43, 50, 2, 'Itapuã')
gaveta('M09', 43, 23, 35, 2, 'Itapuã')

mov('Banho do casal', 'M10')
caixa('M10', 130, 50, 35, 'Areia', prats=1)
porta('M10', 43, 50, 2, 'Areia')
gaveta('M10', 43, 23, 35, 2, 'Areia')

# ════════════════════════════════════════════════════════════════════════
# QUARTO GABRIEL
# ════════════════════════════════════════════════════════════════════════
mov('Quarto Gabriel', 'M11')   # painel liso e ripado + prateleira + mesa
a('M11', 18, 'Painel liso',   155, 270, 1, 'Brisa')
ripado('M11', 45, 270, 'Brisa')
a('M11', 18, 'Prateleira iluminada · duas camadas', 160, 25, 2, 'Itapuã')
led('M11', 1.60)
a('M11', 18, 'Escrivaninha · tampo',  155, 65, 1, 'Itapuã')
a('M11', 15, 'Escrivaninha · apoio',   65, 20, 2, 'Itapuã', 1)
ter('M11', TOMADA_CX + SUPORTE_TV)

mov('Quarto Gabriel', 'M12')   # armário suspenso, fecho-toque
caixa('M12', 195, 40, 45, 'Brisa', prats=0)
porta('M12', 48, 40, 3, 'Brisa'); f('M12', toque=3)
gaveta('M12', 46, 12, 45, 3, 'Brisa')

mov('Quarto Gabriel', 'M13')   # cabeceira ripada iluminada
ripado('M13', 316, 100, 'Brisa'); ripado('M13', 106, 100, 'Brisa')
led('M13', 4.22)

mov('Quarto Gabriel', 'M24')
a('M24', 18, 'Prateleira · duas camadas',  80, 25, 2, 'Itapuã')
mov('Quarto Gabriel', 'M25')
a('M25', 18, 'Prateleira · duas camadas', 160, 25, 2, 'Itapuã')

# ════════════════════════════════════════════════════════════════════════
# QUARTO DAS GÊMEAS
# ════════════════════════════════════════════════════════════════════════
mov('Quarto das gêmeas', 'M14')   # baú com tampo
caixa('M14', 90, 45, 52, 'Brisa', prats=0)
a('M14', 18, 'Tampo do baú · puxador cava', 90, 52, 1, 'Brisa')
f('M14', dobr=2, basc=1)

mov('Quarto das gêmeas', 'M15')   # cabeceira iluminada
a('M15', 18, 'Cabeceira · painel', 199, 110, 2, 'Alecrim')
a('M15', 15, 'Cabeceira · alma e fixação', 398, 20, 1, 'int', 0)
led('M15', 3.98); ter('M15', 3.98*RODAPE_M)

mov('Quarto das gêmeas', 'M16')   # duas mesas de cabeceira
caixa('M16', 75, 50, 45, 'Brisa', prats=0)
caixa('M16', 75, 50, 45, 'Brisa', prats=0)
gaveta('M16', 71, 20, 45, 4, 'Brisa')

mov('Quarto das gêmeas', 'M17')
caixa('M17', 136, 50, 45, 'Brisa', prats=1)
porta('M17', 44, 50, 3, 'Brisa')

mov('Quarto das gêmeas', 'M18')   # painel TV + armário superior + mesa
a('M18', 18, 'Painel de TV',  271, 145, 1, 'Brisa')
caixa('M18', 271, 30, 30, 'Alecrim', prats=0)
porta('M18', 54, 30, 5, 'Brisa')
a('M18', 18, 'Prateleira', 165, 3, 2, 'Alecrim')
gaveta('M18', 54, 32, 50, 5, 'Alecrim')
a('M18', 18, 'Escrivaninha · tampo', 270, 50, 1, 'Alecrim')
led('M18', 2.71); ter('M18', TOMADA_CX + SUPORTE_TV)

# ════════════════════════════════════════════════════════════════════════
# SUÍTE MASTER
# ════════════════════════════════════════════════════════════════════════
mov('Suíte master', 'M19')        # cabeceira iluminada
a('M19', 18, 'Cabeceira · painel', 140, 110, 2, 'Itapuã')
a('M19', 15, 'Cabeceira · alma e fixação', 280, 20, 1, 'int', 0)
led('M19', 2.80); ter('M19', 2.80*RODAPE_M)

mov('Suíte master', 'M20')        # painel piso/teto com porta de correr
a('M20', 18, 'Painel liso piso/teto', 309, 270, 1, 'Itapuã')
ripado('M20', 80, 270, 'Areia')
a('M20', 18, 'Porta de correr embutida · puxador cava', 154, 210, 1, 'Itapuã')
f('M20', correr=1)
a('M20', 18, 'Prateleira iluminada · duas camadas', 389, 25, 2, 'Itapuã')
led('M20', 3.89)
ter('M20', 2.70*3*SERRALHA_M + SUPORTE_TV + 3.89*RODAPE_M)

mov('Suíte master', 'M21')        # closet
# ⛔⛔ CLOSET ABERTO, sem porta — confirmado no render do caderno. Toda a
#   caixaria aparece e sai na cor.
caixa('M21', 96, 270, 60, 'Itapuã', prats=3, aberto=True)
caixa('M21', 99, 270, 60, 'Itapuã', prats=3, aberto=True)
caixa('M21', 98, 270, 60, 'Areia',  prats=5, aberto=True)
caixa('M21', 99, 270, 60, 'Itapuã', prats=3, aberto=True)
a('M21', 18, 'Maleiro · frente',  96, 57, 4, 'Itapuã')
f('M21', cabide=3.0)
gaveta('M21', 45, 14, 60, 8, 'Itapuã')
a('M21', 15, 'Sapateira · aba inclinada', 95, 16, 9, 'Itapuã', 1)
f('M21', corr=9)
a('M21', 18, 'Banco · tampo e caixa', 96, 40, 2, 'Areia')
ter('M21', 0.96*0.40*2*ESTOFADO)
led('M21', 3.90)

# ════════════════════════════════════════════════════════════════════════
# O CÁLCULO
# ⛔ NESTING POR COR × ESPESSURA. Cinco cores não dividem chapa entre si:
#   cada par (cor, espessura) tem o próprio mínimo de uma chapa inteira.
# ⛔ RATEIO (lição da Alice): cada peça paga a PRÓPRIA taxa de chapa; a
#   SOBRA — o pedaço comprado e não usado — rateia pela área total.
# ════════════════════════════════════════════════════════════════════════
MOVEIS = list(AMB_DE)
COR_PRINC = {}
for mv in MOVEIS:
    _c = {}
    for m, esp, d, c, l, q, cor, fc in PCS:
        if m == mv and cor != 'int': _c[cor] = _c.get(cor, 0) + c*l*q
    COR_PRINC[mv] = max(_c, key=_c.get) if _c else 'Itapuã'

def calcula(interior_cor=False, linha=None):
    """interior_cor=False → miolo em Branco TX (linha Essencial).
       interior_cor=True  → tudo na cor do móvel (o cenário caro).
       linha → 'essencial' (telescópica) ou 'premium' (oculta Hettich)."""
    linha = linha or LINHA
    FU, LED_M, mc = fer_un(linha), LINHAS[linha]['led'], LINHAS[linha]['mc']
    def cor_de(mv, cor):
        if cor != 'int': return cor
        return COR_PRINC[mv] if interior_cor else 'Branco TX'
    area, area_mv, fita_mv = {}, {}, {}
    for mv, esp, d, c, l, q, cor, fc in PCS:
        k = (cor_de(mv, cor), esp)
        area[k] = area.get(k, 0.0) + c*l*q/1e4
        area_mv[mv] = area_mv.get(mv, 0.0) + c*l*q/1e4
        ft = FITA_BR if k[0] == 'Branco TX' else FITA_COR
        fator = {2: 0.75, 1: 0.4, 0: 0.0}[fc]
        fita_mv[mv] = fita_mv.get(mv, 0.0) + 2*(c+l)*q/100*fator*ft
    preco  = lambda k: BR[k[1]] if k[0] == 'Branco TX' else COR[k[1]]
    chapas = {k: -(-v/(CH_M2*APROV)//1) for k, v in area.items()}
    taxa   = {k: preco(k)/(CH_M2*APROV) for k in area}
    custo_ch = {k: chapas[k]*preco(k) for k in chapas}
    sobra = sum(custo_ch.values()) - sum(area[k]*taxa[k] for k in area)
    at = sum(area_mv.values())
    ch_mv = {}
    for mv, esp, d, c, l, q, cor, fc in PCS:
        ch_mv[mv] = ch_mv.get(mv, 0.0) + c*l*q/1e4*taxa[(cor_de(mv, cor), esp)]
    for mv in MOVEIS: ch_mv[mv] = ch_mv.get(mv, 0.0) + sobra*area_mv[mv]/at
    fer_mv = {mv: sum(FER[mv][x]*FU[x] for x in FU) for mv in MOVEIS}
    led_mv = {mv: LED[mv]*LED_M for mv in MOVEIS}
    CD = {mv: ((ch_mv[mv] + fita_mv.get(mv, 0))*1.06 + fer_mv[mv]
               + TER[mv] + led_mv[mv])*(1 + M.EMBALAGEM) for mv in MOVEIS}
    PV = {mv: round(CD[mv]/(BASE - mc)/10)*10 for mv in MOVEIS}
    return dict(area=area, chapas=chapas, custo_ch=custo_ch, sobra=sobra,
                ch=ch_mv, fita=fita_mv, fer=fer_mv, led=led_mv, ter=dict(TER),
                area_mv=area_mv, CD=CD, PV=PV,
                CD_TOT=sum(CD.values()), TOT=sum(PV.values()))

R   = calcula(False, 'essencial')   # ⭐ o que vai ao cliente
R_C = calcula(True,  'essencial')   # cenário: tudo na cor
PREM = calcula(False, 'premium')    # ⭐ a versão Hettich, 10 anos
TOTAL, TOTAL_PREM = R['TOT'], PREM['TOT']
GARANTIA = {k: LINHAS[k]['garantia'] for k in LINHAS}

# ── desconto à vista ⭐ [Jonathan 19/10] "ênfase para o valor com desconto" ─
# A escada da casa (referencias/proposta-comercial.md) vai até 7% quando o
# saldo não passa pelo cartão. É essa a ponta que o cliente vê em destaque.
DESC_VISTA = 0.07
VISTA      = round(TOTAL*(1 - DESC_VISTA)/10)*10
VISTA_PREM = round(TOTAL_PREM*(1 - DESC_VISTA)/10)*10

# ── por ambiente ────────────────────────────────────────────────────────
AMBS = []
for mv in MOVEIS:
    if AMB_DE[mv] not in AMBS: AMBS.append(AMB_DE[mv])
PV_AMB = {am: sum(R['PV'][mv] for mv in MOVEIS if AMB_DE[mv] == am)
          for am in AMBS}

if __name__ == '__main__':
    W = 88
    print('═'*W)
    print('MICHELLE E ARLEI — CASA COMPLETA  ·  Inédita Arquitetura  ·  R00')
    print(f'LINHA {LINHA.upper()} ⭐ · MC {MC_ALVO:.0%} ⭐ · COM RT ⭐ · '
          f'base {BASE*100:.2f}%')
    print('═'*W)

    print(f'\n{"CHAPA, POR COR E ESPESSURA":<34}{"área m²":>10}{"chapas":>8}'
          f'{"R$/chapa":>10}{"R$":>10}')
    print('─'*W)
    for k in sorted(R['area'], key=lambda k: (k[0], k[1])):
        pr = BR[k[1]] if k[0] == 'Branco TX' else COR[k[1]]
        print(f'{k[0]+" · "+str(k[1])+" mm":<34}{R["area"][k]:>10.2f}'
              f'{R["chapas"][k]:>8.0f}{pr:>10.0f}{R["custo_ch"][k]:>10.0f}')
    print('─'*W)
    _nch = sum(R['chapas'].values())
    print(f'{"TOTAL":<34}{sum(R["area"].values()):>10.2f}{_nch:>8.0f}'
          f'{"":>10}{sum(R["custo_ch"].values()):>10.0f}')
    print(f'\n  ⛔⛔ {len(R["chapas"])} PARES DE COR × ESPESSURA, {_nch:.0f} CHAPAS.')
    print(f'    A sobra comprada e não usada é R$ {br(R["sobra"])} — '
          f'{R["sobra"]/sum(R["custo_ch"].values()):.0%} da chapa.')
    print('    É o preço de cinco cores de MDF num projeto só: cor nenhuma')
    print('    divide chapa com outra, e cada uma paga o próprio mínimo.')

    print(f'\n{"═"*W}')
    print('MÓVEL A MÓVEL')
    print(f'{"═"*W}')
    print(f'{"":<5}{"":<38}{"chapa":>8}{"fita":>7}{"ferr.":>8}'
          f'{"terc.":>8}{"LED":>7}{"CUSTO":>9}{"PREÇO":>9}')
    for am in AMBS:
        print(f'\n{am.upper()}')
        for mv in [m for m in MOVEIS if AMB_DE[m] == am]:
            print(f'{mv:<5}{"":<38}{R["ch"][mv]:>8.0f}{R["fita"][mv]:>7.0f}'
                  f'{R["fer"][mv]:>8.0f}{R["ter"][mv]:>8.0f}{R["led"][mv]:>7.0f}'
                  f'{R["CD"][mv]:>9.0f}{R["PV"][mv]:>9.0f}')
        print(f'{"":<5}{"":<38}{"":>38}{"subtotal":>9}{br(PV_AMB[am]):>9}')

    print(f'\n{"═"*W}')
    print('O INVESTIMENTO, POR AMBIENTE')
    print(f'{"═"*W}')
    for am in AMBS:
        print(f'  {am:<34}R$ {br(PV_AMB[am]):>9}')
    print('  ' + '─'*46)
    print(f'  {"CUSTO DIRETO":<34}R$ {br(R["CD_TOT"]):>9}')
    print(f'  {"INVESTIMENTO TOTAL":<34}R$ {br(TOTAL):>9}')

    print(f'\n{"═"*W}')
    print('★ EM ABERTO')
    print(f'{"═"*W}')
    _d = R_C['TOT'] - TOTAL
    print(f'  · ⭐ INTERIOR EM BRANCO TX — é a linha Essencial. Com o miolo')
    print(f'    NA COR de cada móvel o total iria a R$ {br(R_C["TOT"])}: '
          f'R$ {br(_d)} a mais,')
    print(f'    {_d/TOTAL:.0%}. O projeto não diz o que é o miolo; se a arquiteta')
    print('    quiser cor por dentro, é essa a conta.')
    _srt = M.base(parcelas=0, rt=False, vendedor=False)
    _sem = sum(round(R['CD'][mv]/(_srt-MC_ALVO)/10)*10 for mv in MOVEIS)
    _p35 = sum(round(R['CD'][mv]/(BASE-0.35)/10)*10 for mv in MOVEIS)
    print(f'  · ⭐ MC DE {MC_ALVO:.0%} [Jonathan 19/10], dentro da faixa ideal da casa')
    print(f'    ({M.MC_IDEAL[0]:.0%}–{M.MC_IDEAL[1]:.0%}). A 35% a casa sairia a '
          f'R$ {br(_p35)} — os três pontos')
    print(f'    valem R$ {br(TOTAL-_p35)}.')
    print(f'  · ⭐ RT DE 10% INCLUÍDA [Jonathan 18/10]. Sem ela a casa sairia')
    print(f'    a R$ {br(_sem)} — a RT vale R$ {br(TOTAL-_sem)}.')
    print('  · ⛔⛔ A PRATELEIRA M03 TEM 3,23 m E A CHAPA TEM 2,75.')
    print('    Não existe peça inteira nessa medida: ou vai com emenda, ou')
    print('    vira duas prateleiras com encontro aparente. Decidir com a')
    print('    arquiteta ANTES de produzir — é escolha de projeto, não nossa.')
    print('  · ⛔ RIPA DE 2 × 2 cm. A prancha pede ripa quadrada de 2 cm;')
    print('    cortada de chapa de 18 mm ela fica 18 × 20, não 20 × 20.')
    print('    Para 20 cheios é sarrafo ou chapa de 25 — e muda o preço.')
    print('  · ⛔ PÉ-DIREITO DIVERGENTE NA PRÓPRIA PRANCHA: a planta de')
    print('    layout traz PD = 260 e a de paginação de piso traz 270. Os')
    print('    móveis de piso/teto (M11, M20, M21) dependem disso.')
    print('  · ⚠ BANCADAS (B01…B05) SÃO MARMORARIA, não marcenaria — granito')
    print('    preto São Gabriel. Não estão neste preço.')
    print('  · ⚠ MESA DE CABECEIRA M16: a prancha detalha uma e as vistas')
    print('    mostram duas (são duas camas). Orçei DUAS.')
    print('  · ★ SERRALHERIA (M06, M20, M26 e o rodapé em perfil L) está')
    print(f'    estimada a R$ {br(SERRALHA_M)}/m e R$ {br(RODAPE_M)}/m — cotar.')
    print('  · ⚠ ELETRODOMÉSTICOS são dos clientes. A prancha manda')
    print('    "compatibilizar armário com forno e micro-ondas comprados')
    print('    pelos clientes, NÃO EXECUTAR SEM ESSA COMPATIBILIZAÇÃO".')

    print(f'\n{"═"*W}')
    print('⭐ A VERSÃO PREMIUM — FERRAGEM HETTICH')
    print(f'{"═"*W}')
    print(f'  {"Essencial · telescópica · " + GARANTIA["essencial"]:<40}'
          f'R$ {br(TOTAL):>9}   MC {LINHAS["essencial"]["mc"]:.0%}')
    print(f'  {"Premium · oculta Hettich · " + GARANTIA["premium"]:<40}'
          f'R$ {br(TOTAL_PREM):>9}   MC {LINHAS["premium"]["mc"]:.0%}')
    print(f'  {"diferença":<40}R$ {br(TOTAL_PREM-TOTAL):>9}'
          f'   ({TOTAL_PREM/TOTAL-1:.0%})')
    print(f'\n  ⭐ {TOTAL_PREM/TOTAL-1:.0%} a mais compra CINCO VEZES mais garantia '
          f'({GARANTIA["essencial"]} → {GARANTIA["premium"]}).')
    print('    A corrediça oculta é o que muda: o trilho some por baixo, a')
    print('    gaveta abre inteira e fecha amortecida — e é a peça que decide')
    print('    se o móvel ainda fecha bem no décimo ano.')
    print(f'\n{"═"*W}')
    print(f'  {"À VISTA · −" + f"{DESC_VISTA:.0%}":<40}')
    print(f'  {"Essencial":<40}R$ {br(VISTA):>9}')
    print(f'  {"Premium":<40}R$ {br(VISTA_PREM):>9}')
