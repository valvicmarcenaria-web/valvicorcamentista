# -*- coding: utf-8 -*-
"""UM gerador para a aba de QUALQUER ambiente — layout, texto e formato.

⭐⭐ POR QUE ELE EXISTE  [Jonathan, 28/10/2026]
   > "a formatação do living e da cozinha estao diferentes"

   Estavam, e em quinze pontos: linhas de respiro em uma e não na outra,
   cinzas com dois centésimos de diferença, a mesma tabela mesclada no
   Living e solta na Cozinha, largura de coluna diferente, linha congelada
   em uma só, e a Cozinha ainda carregando uma versão ANTIGA inteira na
   coluna A. Nada disso é descuido de uma vez: é o preço de formatar a aba
   com a mão, duas vezes. ⛔ Duas mãos, dois resultados.

   ⭐ A regra que sai daqui: a aba não se formata, ela se GERA. São 20
     ambientes — o vigésimo tem de sair igual ao primeiro sem eu lembrar
     de nada.

⭐ O RITMO, e ele é o mesmo em toda seção:
       [respiro]  SEÇÃO  [respiro]  conteúdo
   Nenhuma exceção. Era a exceção que fazia o Living parecer apertado onde
   a Cozinha parecia solta.

⛔ locale pt_BR: separador de argumento é ';'. Nome de função vai em
  INGLÊS — a API normaliza o nome e devolve o separador local.
⛔⛔ E A VÍRGULA TAMBÉM É O SEPARADOR DECIMAL. "=ABS(I33)>0.01" foi
  RECUSADO pela API num formato condicional: em pt_BR o literal é 0,01. Fica
  a regra: nunca escrever decimal em fórmula — "=ARRED(I33;2)<>0" diz a
  mesma coisa e não depende de locale nenhum.
⛔⛔ PADRÃO NUMÉRICO SÓ PARA MOEDA E PORCENTAGEM. Em pt_BR o ponto de
  "#,##0.##" é separador de MILHAR, e 110 sai como "110,". Número livre
  (C, L, QTD) vai SEM padrão nenhum.

   uso:  python3 aba.py cozinha 104 47 186 5
         (ambiente · sheetId · linha dos blocos HOJE · linhas HOJE ·
          regras condicionais que a aba já tem — 0 se for aba nova)
"""
import sys, json, importlib.util, pathlib, io, contextlib, subprocess
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P))
import base as B

NOME  = sys.argv[1]
SID   = int(sys.argv[2])
BLK_HOJE = int(sys.argv[3])
FIM_HOJE = int(sys.argv[4])   # quantas linhas a aba tem HOJE
# ⭐⭐ QUANTAS REGRAS CONDICIONAIS A ABA JÁ TEM. Sem isso o gerador não é
#   idempotente: reaplicar DUPLICA as cinco regras e as mesclagens batem de
#   frente com as antigas (a API recusa mesclar por cima de mesclagem). E
#   reaplicar é o caso NORMAL, não a exceção — toda correção de método, como
#   a moldura usinada, reescreve a aba inteira. Aba nova: 0.
N_REGRAS = int(sys.argv[5]) if len(sys.argv) > 5 else 0

sp = importlib.util.spec_from_file_location('AMB', P/f'{NOME}.py')
A = importlib.util.module_from_spec(sp); sys.modules['AMB'] = A
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(A)
PECAS = getattr(A, NOME.upper())
F = A.FOLHA
g = lambda n: getattr(A, n, [])
MOV = list(dict.fromkeys(p['movel'] for p in PECAS))

# ── 1 · quantas linhas tem cada bloco de material ───────────────────────
# ⭐⭐ A LISTA DE CHAPAS SAI DAS PEÇAS, não de uma lista à mão. A frente
#   provençal criou quatro padrões novos de uma vez; se a lista fosse
#   digitada, eles sumiam da compra em silêncio — que é exatamente o erro
#   que a regra de ferro existe para impedir.
CHAPAS = sorted({p['chave'] for p in PECAS if p['chave'].startswith('MDF')},
                key=lambda k: (not k.endswith(' 18'), k))
TXT = F.get('chapa_txt', {})
for k in CHAPAS:
    if k not in TXT: print(f'⚠ chapa sem texto na FOLHA: {k}')
# ⭐ linhas de acabamento: só as que o ambiente tem, e na ORDEM DO PROCESSO
#   — primeiro se fita, depois se fileta. Alfabética punha a filetagem antes
#   da fita, que é ler a fábrica de trás para frente.
ORDEM = ['Fita cor', 'Fita Branco TX', 'Filetagem automática',
         'Filetagem manual']
_tem = B.acabamento(PECAS)
ACAB = [k for k in ORDEM if k in _tem]
assert len(ACAB) == len(_tem), f'⛔ acabamento fora da ORDEM: {set(_tem)-set(ORDEM)}'
nmat = len(CHAPAS) + len(ACAB) + 1 + (1 if g('VIDRO') else 0) + 2
nit, nni, nnt = len(MOV), len(F['nao_marcenaria']), len(F['notas'])
ndv = len(F.get('duvidas', []))

# ── 2 · O LAYOUT CANÔNICO. Toda seção com o mesmo respiro. ──────────────
L = {}
L['tit'], L['sub']   = 1, 2
L['s_amb']           = 4
L['cab_mat']         = 6
L['mat0'] = L['cab_mat'] + 1
L['mat1'] = L['mat0'] + nmat - 1
L['direto']          = L['mat1'] + 1
L['nota']            = L['direto'] + 1
L['s_itens']         = L['nota'] + 2
L['cab_it']          = L['s_itens'] + 2
L['it0'] = L['cab_it'] + 1
L['it1'] = L['it0'] + nit - 1
L['f0']  = L['it1'] + 2
L['f1']  = L['f0'] + 4
L['s_ni']            = L['f1'] + 2
L['ni0'] = L['s_ni'] + 2
L['ni1'] = L['ni0'] + nni - 1
L['s_pec']           = L['ni1'] + 2
L['blk0']            = L['s_pec'] + 2

# ── 3 · os blocos, do mesmo arquivo que faz a conta ─────────────────────
subprocess.run([sys.executable, str(P/'planilha.py'), NOME, str(L['blk0'])],
               check=True, capture_output=True)
R = json.load(open(P/f'_{NOME}-rows.json'))
MAPA   = {int(k): v for k, v in R['mapa'].items()}
FAIXAS = R['faixas']
L['blk1']  = max(MAPA.values())
L['s_nt']  = L['blk1'] + 2
L['nt0']   = L['s_nt'] + 2
L['nt1']   = L['nt0'] + nnt - 1
# ⭐⭐ A CAIXA DE DÚVIDAS  [Jonathan, 28/10/2026]
#   > "Se surgir dúvidas de orçamento. Abra uma caixa de dúvidas na
#   >  planilha mesmo. Para cada ambiente um espaço de dúvidas e liste
#   >  todas as dúvidas lá."
#   ⭐ Instrução de não travar: dúvida não para o orçamento, ela fica
#     escrita onde o preço está, numerada, para o senhor responder em cima.
#   ⭐ Vai no FIM de propósito: seção nova no fim não desloca nenhuma linha
#     acima dela, então acrescentá-la numa aba já montada é barato.
L['s_dv']  = L['nt1'] + 2
L['dv0']   = L['s_dv'] + 2
L['dv1']   = L['dv0'] + max(1, ndv) - 1
L['fim']   = L['dv1']
SHIFT = L['blk0'] - BLK_HOJE
a, b = L['blk0'], L['blk1']          # a faixa de peças, para as fórmulas
K = f'$K${a}:$K${b}'
AREA = 'VLOOKUP("Área da chapa";precos;2;FALSE)'
APR  = 'VLOOKUP("Aproveitamento";precos;2;FALSE)'
M2 = (lambda alvo: f'SUMPRODUCT(({K}={alvo})*IF(ISNUMBER($D${a}:$D${b});'
      f'$D${a}:$D${b}*$E${a}:$E${b}*$F${a}:$F${b};0))/10000')

# ── 4 · O TEXTO DA ABA — uma matriz só, de B1 até K(blk0-1) ─────────────
W = 10                                    # B..K
def linha(**kw):
    r = [''] * W
    for c, v in kw.items(): r['BCDEFGHIJK'.index(c)] = v
    return r
TOP = [linha() for _ in range(L['blk0'] - 1)]
def põe(r, **kw):
    for c, v in kw.items(): TOP[r-1]['BCDEFGHIJK'.index(c)] = v

põe(L['tit'], B=f"  VALVIC MARCENARIA        {F['aba']}")
põe(L['sub'], B='  ' + F['sub'])
põe(L['s_amb'], B='  O AMBIENTE   ·   chapa 275 × 185 com 80% de aproveitamento '
                  '· e ela se conta em número cheio, por cor × espessura')
põe(L['cab_mat'], B='MATERIAL', C='ESPECIFICAÇÃO', D='QUANTIDADE', E='UN',
    F='CUSTO', G='FRETE', H='TOTAL', I='% DO CUSTO')

r = L['mat0']
for chave in CHAPAS:
    prefixo = TXT.get(chave, chave)
    põe(r, B=chave,
        C=f'="{prefixo} · "&ROUND({M2(f"$B{r}")};1)&" m² de peças"',
        D=f'=ROUNDUP({M2(f"$B{r}")}/({AREA}*{APR}))', E='chapas',
        F=f'=D{r}*VLOOKUP($B{r};precos;2;FALSE)',
        G=f'=D{r}*VLOOKUP("Frete MDF";precos;2;FALSE)')
    r += 1
# ⭐⭐ FITA E FILETAGEM, UMA LINHA CADA  [Jonathan, 28/10/2026]
#   > "nao vi o levamento de filetagem tbm"
#   Estava dentro da fita, somada num preço cheio. Separadas, aparece que
#   a fita branca custa R$ 2,00 e a de cor R$ 3,00, e que a filetagem de
#   ripa e de 6 mm vai à mão, ao dobro.
EXPLICA = {
 'Fita cor': '22 mm na cor da frente · declarada aresta a aresta, mais 10% '
             'de desperdício',
 'Fita Branco TX': '22 mm na caixaria · ⭐ R$ 2,00 contra R$ 3,00 da fita de '
                   'cor · mais 10% de desperdício',
 'Filetagem automática': 'Coladeira · peça de 15 e 18 mm · ⭐ serviço por '
                         'metro de aresta feita, sem desperdício',
 'Filetagem manual': '⛔ Ripa e chapa de 6 mm não entram na coladeira: vai à '
                     'mão, a R$ 5,00 — o dobro da automática',
}
L['acab0'] = r
for ch in ACAB:
    põe(r, B=ch, C=EXPLICA[ch],
        D=f'=SUMIF({K};"{ch}";$F${a}:$F${b})', E='m',
        F=f'=D{r}*VLOOKUP("{ch}";precos;2;FALSE)',
        G=('=VLOOKUP("Frete fita";precos;2;FALSE)' if ch.startswith('Fita')
           else ''))
    r += 1
L['acab1'] = r - 1

FERR = [('Corrediça', 'corrediça', g('GAVETAS')),
        ('Dobradiça', 'dobradiça', g('PORTAS')),
        ('Dobradiça vidro', None, [x for x in g('PORTAS') if x[4] == B.DOBR_VIDRO]),
        ('Báscula HK-XS', 'articulador HK-XS', g('BASCULAS')),
        # ⭐ slim no lugar do pulsador [Jonathan, 28/10] · são R$ 65 por
        #   báscula de diferença, e a Base já avisava que não se somam
        # ⛔ só as básculas que abrem pelo slim. Na Lavanderia elas abrem
        #   pelo Alças Traso, e o slim não existe lá.
        ('Puxador slim', 'puxador slim',
         [b for b in g('BASCULAS') if (b[3] if len(b) > 3 else 'slim') == 'slim']),
        ('Puxador Alças Traso 128', 'puxador Alças Traso de 128', g('PUXADORES')),
        ('Moldura provençal', 'moldura provençal', g('MOLDURA')),
        ('Cava usinada', 'cava usinada', g('CAVA')),
        ('LED conjunto', 'LED', g('LED')),
        ('Alma de aço', 'alma de aço', g('ALMAS')),
        ('Suporte oculto', 'suporte oculto', g('SUPORTES')),
        ('Cabideiro', 'cabideiro', g('CABIDEIROS')),
        ('Sarrafo de pinus', 'sarrafo de reforço', g('SARRAFOS')),
        ('Serralheria estrutural', 'serralheria estrutural', g('SERRALHERIA'))]
ativos = [(c, rot) for c, rot, lst in FERR if lst]
# ⛔ cava, LED e moldura se medem em metro ou em frente, não em peça:
#   não entram na contagem de "peças de ferragem"
conta  = [c for c, rot in ativos
          if c not in ('Cava usinada', 'LED conjunto', 'Moldura provençal',
                       'Serralheria estrutural', 'Sarrafo de pinus')]
rots   = [rot for c, rot in ativos if rot]
# ⛔ .capitalize() rebaixa o resto da frase, e 'LED' virava 'led'
frase  = ', '.join(rots[:-1])
desc   = frase[:1].upper() + frase[1:] + ' e ' + rots[-1]
L['ferr'] = r
põe(r, B='Ferragem, puxador e iluminação',
    C=f'{desc} · linha {getattr(A, "LINHA", "Blum")} · ⛔ sem fonte: as fitas '
      'da casa são 110 V',
    D='=SUMPRODUCT((' + '+'.join(f'({K}="{c}")' for c in conta) +
      f')*IF(ISNUMBER($F${a}:$F${b});$F${a}:$F${b};0))', E='peças',
    # ⭐ o custo de ferragem é o RESTO: tudo que tem chave, menos chapa,
    #   menos acabamento, menos vidro. Assim nenhuma linha nova de ferragem
    #   pode escapar da conta por eu não a ter listado aqui.
    F=f'=SUMIF({K};"<>";$I${a}:$I${b})' +
      ''.join(f'-SUMIF({K};$B{L["mat0"]+i};$I${a}:$I${b})'
              for i in range(len(CHAPAS))) +
      ''.join(f'-SUMIF({K};$B{L["acab0"]+i};$I${a}:$I${b})'
              for i in range(len(ACAB))) +
      (f'-SUMIF({K};"Vidro reflecta";$I${a}:$I${b})' if g('VIDRO') else ''),
    G='=VLOOKUP("Frete ferragem";precos;2;FALSE)')
r += 1
if g('VIDRO'):
    põe(r, B='Vidro',
        C='Reflecta champagne · ⛔ SEM PREÇO na Base: a linha existe vazia de '
          'propósito, para gritar',
        D=f'={M2(chr(34)+"Vidro reflecta"+chr(34))}', E='m²',
        F=f'=SUMIF({K};"Vidro reflecta";$I${a}:$I${b})',
        G='=VLOOKUP("Frete vidro";precos;2;FALSE)')
    r += 1
L['ult_mat'] = r - 1                        # ⭐ onde acaba o material de fato
põe(r, B='Consumíveis',
    C='Cola, lixa, parafuso, cavilha, tapa-furo, fundo e verniz · 6% sobre '
      'chapa, fita e filetagem',
    F=f'=SUM(H{L["mat0"]}:H{L["acab1"]})*VLOOKUP("Consumíveis";precos;2;FALSE)')
L['cons'] = r; r += 1
põe(r, B='Embalagem', C='Papelão, filme e cantoneira · 2% sobre o subtotal',
    F=f'=SUM(H{L["mat0"]}:H{L["cons"]})*VLOOKUP("Embalagem";precos;2;FALSE)')
for i in range(L['mat0'], L['mat1'] + 1):
    põe(i, H=f'=F{i}+G{i}', I=f'=IFERROR(H{i}/$H${L["direto"]};"")')
d = L['direto']
põe(d, B='CUSTO DIRETO DO AMBIENTE', F=f'=SUM(F{L["mat0"]}:F{L["mat1"]})',
    G=f'=SUM(G{L["mat0"]}:G{L["mat1"]})', H=f'=SUM(H{L["mat0"]}:H{L["mat1"]})',
    I=f'=IFERROR(H{d}/$H${d};"")')
põe(L['nota'], C=F['nota'])

põe(L['s_itens'], B='  OS ITENS   ·   cada móvel com o seu custo, porque é '
                    'assim que a fábrica produz e o cliente confere')
põe(L['cab_it'], B='ITEM', C='MÓVEL', D='MEDIDA GERAL', I='CUSTO')
for i, mov in enumerate(MOV, 1):
    põe(L['it0'] + i - 1, B=i, C=mov.split(' ', 2)[-1],
        D=A.CABECA[mov][0], I=f'=I{MAPA[i]}')
f0 = L['f0']
põe(f0,   B='Soma dos itens · chapa rateada em fração',
          I=f'=SUM(I{L["it0"]}:I{L["it1"]})')
põe(f0+1, B='Arredondamento de chapa para número cheio · ⛔ a regra de ferro',
          I='=' + '+'.join(f'F{L["mat0"]+i}' for i in range(len(CHAPAS))) +
            ''.join(f'-SUMIF({K};$B{L["mat0"]+i};$I${a}:$I${b})'
                    for i in range(len(CHAPAS))))
põe(f0+2, B='MATERIAL E FERRAGEM, PELO RATEIO DOS ITENS', I=f'=I{f0}+I{f0+1}')
põe(f0+3, B='Material e ferragem, pelo painel do ambiente',
          I=f'=SUM(F{L["mat0"]}:F{L["ult_mat"]})')
põe(f0+4, B='⭐ CONFERÊNCIA — as duas contas têm de dar a mesma coisa',
          I=f'=I{f0+2}-I{f0+3}')

põe(L['s_ni'], B='  O QUE NÃO É MARCENARIA   ·   está na prancha, não está '
                 'nesta conta')
for i, t in enumerate(F['nao_marcenaria']): põe(L['ni0'] + i, B=t)
põe(L['s_pec'], B='  AS PEÇAS, ITEM POR ITEM   ·   cada linha é uma peça que '
                  'vai para o plano de corte')
NOTAS = [linha(B='  NOTAS E PONTOS EM ABERTO   ·   o que ainda precisa de '
                 'decisão antes de virar preço'), linha()] + \
        [linha(C=t) for t in F['notas']]
DV = F.get('duvidas') or ['— nenhuma dúvida aberta neste ambiente.']
DUVIDAS = [linha(B='  ⚠ DÚVIDAS DE ORÇAMENTO   ·   numeradas, para o senhor '
                   'responder em cima · nenhuma delas trava o preço'),
           linha()] + \
          [linha(B=f'{i:02d}', C=t) for i, t in enumerate(DV, 1)]

# ── 5 · O FORMATO. Composto em Python, nunca repetido à mão. ────────────
PRETO  = {'red': .1019608, 'green': .1019608, 'blue': .1019608}
CINZA  = {'red': .4196078, 'green': .4196078, 'blue': .4196078}
CLARO  = {'red': .6745098, 'green': .6745098, 'blue': .6745098}
OURO   = {'red': .6862745, 'green': .5137255, 'blue': .2313725}
VERM   = {'red': .7764706, 'green': .1568628, 'blue': .1568628}
BRANCO = {'red': 1, 'green': 1, 'blue': 1}
F7     = {'red': .9686275, 'green': .9686275, 'blue': .9686275}
F5     = {'red': .9607843, 'green': .9607843, 'blue': .9607843}
MOEDA  = {'type': 'CURRENCY', 'pattern': '"R$" #,##0.00'}
PCT    = {'type': 'PERCENT',  'pattern': '0.0%'}
INT    = {'type': 'NUMBER',   'pattern': '0'}

def fm(sz=10, bd=False, it=False, fg=PRETO, bg=None, al='LEFT',
       wr='CLIP', num=None, bor=None):
    """⭐ `fields: "userEnteredFormat"` troca o formato INTEIRO, então o que
      não vem aqui volta ao padrão — e é por isso que omitir é correto, não
      só mais curto. ⛔ E é também o que limpa padrão numérico herdado, que
      era o que fazia 110 aparecer como "110,"."""
    t = {'fontFamily': 'Arial', 'fontSize': sz,
         'foregroundColorStyle': {'rgbColor': fg}}
    if bd: t['bold'] = True
    if it: t['italic'] = True
    f = {'textFormat': t, 'horizontalAlignment': al,
         'verticalAlignment': 'MIDDLE', 'wrapStrategy': wr}
    if bg: f['backgroundColorStyle'] = {'rgbColor': bg}
    if num: f['numberFormat'] = num
    if bor: f['borders'] = bor
    return f
COL = 'ABCDEFGHIJK'
def rng(r0, r1, c0='B', c1='I'):
    return {'sheetId': SID, 'startRowIndex': r0-1, 'endRowIndex': r1,
            'startColumnIndex': COL.index(c0), 'endColumnIndex': COL.index(c1)+1}
def rc(r0, r1, c0, c1, f):
    return {'repeatCell': {'range': rng(r0, r1, c0, c1),
            'cell': {'userEnteredFormat': f}, 'fields': 'userEnteredFormat'}}
def alt(r0, r1, px):
    return {'updateDimensionProperties': {'range': {'sheetId': SID,
            'dimension': 'ROWS', 'startIndex': r0-1, 'endIndex': r1},
            'properties': {'pixelSize': px}, 'fields': 'pixelSize'}}
def mesc(r, c0, c1):
    return {'mergeCells': {'range': rng(r, r, c0, c1), 'mergeType': 'MERGE_ALL'}}
RUA  = {'bottom': {'style': 'SOLID', 'width': 1, 'colorStyle': {'rgbColor': PRETO}}}
TETO = {'top': {'style': 'SOLID_THICK', 'width': 3, 'colorStyle': {'rgbColor': OURO}}}

Q = []
# a base de tudo: a folha inteira, limpa
Q.append(rc(1, L['fim'], 'A', 'K', fm()))
# ⛔ a coluna A é margem e a J é respiro: ficam vazias, e assim se vê
Q.append(rc(1, L['fim'], 'J', 'J', fm(sz=9, fg=CLARO)))
Q.append(rc(1, L['fim'], 'K', 'K', fm(sz=8, fg=CLARO)))
# faixa preta
Q.append(rc(L['tit'], L['tit'], 'B', 'I',
            fm(16, True, fg=BRANCO, bg=PRETO)))
Q.append(rc(L['sub'], L['sub'], 'B', 'I', fm(9, fg=CINZA, wr='WRAP')))
# as seções, todas iguais
for s in ('s_amb', 's_itens', 's_ni', 's_pec'):
    Q.append(rc(L[s], L[s], 'B', 'I', fm(11, True, fg=OURO, bor=RUA)))
Q.append(rc(L['s_nt'], L['s_nt'], 'B', 'I', fm(11, True, fg=OURO, bor=RUA)))
# ⭐ a seção de dúvidas é a única em VERMELHO: ela pede resposta, não leitura
Q.append(rc(L['s_dv'], L['s_dv'], 'B', 'I', fm(11, True, fg=VERM, bor=RUA)))
Q.append(rc(L['dv0'], L['dv1'], 'B', 'B',
            fm(10, True, fg=VERM, al='CENTER', bg=F5)))
Q.append(rc(L['dv0'], L['dv1'], 'C', 'I', fm(10, wr='WRAP')))
# ── o painel do ambiente ───────────────────────────────────────────────
Q.append(rc(L['cab_mat'], L['cab_mat'], 'B', 'I', fm(8, True, fg=CINZA, bg=F7)))
Q.append(rc(L['cab_mat'], L['cab_mat'], 'D', 'D', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
Q.append(rc(L['cab_mat'], L['cab_mat'], 'E', 'E', fm(8, True, fg=CINZA, bg=F7, al='CENTER')))
Q.append(rc(L['cab_mat'], L['cab_mat'], 'F', 'I', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
m0, m1 = L['mat0'], L['mat1']
Q.append(rc(m0, m1, 'C', 'C', fm(9, fg=CINZA)))
# ⛔ SEM padrão: a coluna mistura chapa (26), metro de fita (482,8) e m²
#   de vidro (5,6). Qualquer padrão estraga um dos três — '0.0' faria
#   26 chapas aparecer como '26,0'.
Q.append(rc(m0, m1, 'D', 'D', fm(10, al='RIGHT')))
Q.append(rc(m0, m1, 'E', 'E', fm(9, fg=CINZA, al='CENTER')))
Q.append(rc(m0, m1, 'F', 'H', fm(10, al='RIGHT', num=MOEDA)))
Q.append(rc(m0, m1, 'I', 'I', fm(10, fg=CINZA, al='RIGHT', num=PCT)))
Q.append(rc(d, d, 'B', 'I', fm(11, True, bg=F5, bor=TETO)))
Q.append(rc(d, d, 'F', 'H', fm(11, True, bg=F5, bor=TETO, al='RIGHT', num=MOEDA)))
Q.append(rc(d, d, 'I', 'I', fm(11, True, bg=F5, bor=TETO, al='RIGHT', num=PCT)))
Q.append(rc(L['nota'], L['nota'], 'C', 'I', fm(9, it=True, fg=CINZA, wr='WRAP')))
# ── a tabela dos itens ─────────────────────────────────────────────────
ci = L['cab_it']
Q.append(rc(ci, ci, 'B', 'I', fm(8, True, fg=CINZA, bg=F7)))
Q.append(rc(ci, ci, 'B', 'B', fm(8, True, fg=CINZA, bg=F7, al='CENTER')))
Q.append(rc(ci, ci, 'I', 'I', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
Q.append(rc(L['it0'], L['it1'], 'B', 'B', fm(10, True, al='CENTER', num=INT)))
Q.append(rc(L['it0'], L['it1'], 'C', 'C', fm(10)))
Q.append(rc(L['it0'], L['it1'], 'D', 'H', fm(9, fg=CINZA)))
Q.append(rc(L['it0'], L['it1'], 'I', 'I', fm(10, True, al='RIGHT', num=MOEDA)))
Q.append(rc(f0, f0+1, 'B', 'H', fm(10, fg=CINZA)))
Q.append(rc(f0, f0+1, 'I', 'I', fm(10, fg=CINZA, al='RIGHT', num=MOEDA)))
Q.append(rc(f0+2, f0+2, 'B', 'H', fm(11, True, bg=F5, bor=TETO)))
Q.append(rc(f0+2, f0+2, 'I', 'I', fm(11, True, bg=F5, bor=TETO, al='RIGHT', num=MOEDA)))
Q.append(rc(f0+3, f0+3, 'B', 'H', fm(10, fg=CINZA)))
Q.append(rc(f0+3, f0+3, 'I', 'I', fm(10, fg=CINZA, al='RIGHT', num=MOEDA)))
Q.append(rc(f0+4, f0+4, 'B', 'H', fm(11, True, bg=F5)))
Q.append(rc(f0+4, f0+4, 'I', 'I', fm(11, True, bg=F5, al='RIGHT', num=MOEDA)))
# ── o que não é marcenaria, e as notas ─────────────────────────────────
Q.append(rc(L['ni0'], L['ni1'], 'B', 'H', fm(10, fg=CINZA)))
Q.append(rc(L['nt0'], L['nt1'], 'C', 'I', fm(9, fg=CINZA, wr='WRAP')))
# ── as peças, coluna por coluna — é aqui que o alinhamento se perdia ───
Q.append(rc(a, b, 'B', 'B', fm(10)))
Q.append(rc(a, b, 'C', 'C', fm(9, fg=CINZA)))
Q.append(rc(a, b, 'D', 'F', fm(10, al='RIGHT')))        # ⛔ SEM padrão numérico
Q.append(rc(a, b, 'G', 'G', fm(9, fg=CINZA, al='CENTER')))
Q.append(rc(a, b, 'H', 'I', fm(10, al='RIGHT', num=MOEDA)))
Q.append(rc(a, b, 'K', 'K', fm(8, fg=CLARO)))
# ── alturas: o respiro é fino, a seção é larga ─────────────────────────
Q.append(alt(1, L['fim'], 21))
Q.append(alt(L['tit'], L['tit'], 34))
for s in ('s_amb', 's_itens', 's_ni', 's_pec', 's_nt', 's_dv'):
    Q.append(alt(L[s], L[s], 26))
for z in (3, L['s_amb']+1, L['nota']+1, L['s_itens']+1, L['it1']+1,
          L['s_ni']+1, L['s_pec']+1, L['f1']+1, L['blk1']+1, L['s_nt']+1,
          L['nt1']+1, L['s_dv']+1):
    Q.append(alt(z, z, 8))
# ⛔⛔ autoResizeDimensions NÃO enxerga célula mesclada: a linha fica em 21 px
#   e o texto embrulhado desaparece. Então a altura se CALCULA — e assim ela
#   sai igual nas duas abas, que é o ponto de tudo isto.
PX = dict(zip('ABCDEFGHIJK', (36, 258, 500, 62, 62, 62, 54, 104, 128, 24, 150)))
def altura(txt, c0, c1, pt=9):
    larg = sum(PX[c] for c in 'ABCDEFGHIJK'[COL.index(c0):COL.index(c1)+1])
    # ⭐ errar para CIMA: linha sobrando é respiro, linha faltando é texto
    #   cortado. Daí o 0.62 (Arial é mais larga do que a média) e os 8% de
    #   folga — texto que enche 90% da última linha quase sempre vira duas.
    por_linha = max(20, int(larg / (pt * 0.62)))
    n = max(1, -(-int(len(txt) * 1.08) // por_linha))
    return max(21, n * (pt + 4) + 8)
Q.append(alt(L['sub'], L['sub'], altura(TOP[L['sub']-1][0], 'B', 'I')))
Q.append(alt(L['nota'], L['nota'], altura(TOP[L['nota']-1][1], 'C', 'I')))
for i in range(L['nt0'], L['nt1']+1):
    Q.append(alt(i, i, altura(NOTAS[i - L['s_nt']][1], 'C', 'I')))
for i in range(L['dv0'], L['dv1']+1):
    Q.append(alt(i, i, altura(DUVIDAS[i - L['s_dv']][1], 'C', 'I')))
# ⭐ a aba acaba onde o conteúdo acaba — sobra de linha guarda formato velho
# ⛔⛔ E ELA TAMBÉM PODE CRESCER. O gerador nasceu encolhendo abas (Living e
#   Cozinha, que já existiam grandes) e emitia deleteDimension sempre. Na
#   Lavanderia, que entra numa cópia de 173 linhas e precisa de 236, isso
#   virou um intervalo INVERTIDO — startIndex 237, endIndex 173 — que a API
#   recusa e derruba o lote inteiro. Agora são três casos, e o terceiro é
#   não fazer nada.
if L['fim'] + 1 < FIM_HOJE:
    Q.append({'deleteDimension': {'range': {'sheetId': SID, 'dimension': 'ROWS',
              'startIndex': L['fim']+1, 'endIndex': FIM_HOJE}}})
CRESCER = max(0, L['fim'] - FIM_HOJE)   # ⭐ aplicado LÁ NA FRENTE, ver 5b
# ── larguras, iguais nas duas abas ─────────────────────────────────────
for c, px in zip('ABCDEFGHIJK', (36, 258, 500, 62, 62, 62, 54, 104, 128, 24, 150)):
    Q.append({'updateDimensionProperties': {'range': {'sheetId': SID,
              'dimension': 'COLUMNS', 'startIndex': COL.index(c),
              'endIndex': COL.index(c)+1}, 'properties': {'pixelSize': px},
              'fields': 'pixelSize'}})
Q.append({'updateSheetProperties': {'properties': {'sheetId': SID,
          'gridProperties': {'frozenRowCount': 2, 'hideGridlines': True}},
          'fields': 'gridProperties.frozenRowCount,gridProperties.hideGridlines'}})
# ── mesclagens ─────────────────────────────────────────────────────────
for s in ('tit', 'sub', 's_amb', 's_itens', 's_ni', 's_pec', 's_nt', 's_dv'):
    Q.append(mesc(L[s], 'B', 'I'))
Q.append(mesc(L['nota'], 'C', 'I'))
for i in range(L['it0'], L['it1']+1): Q.append(mesc(i, 'D', 'H'))
for i in range(f0, L['f1']+1):        Q.append(mesc(i, 'B', 'H'))
for i in range(L['ni0'], L['ni1']+1): Q.append(mesc(i, 'B', 'H'))
for i in range(L['nt0'], L['nt1']+1): Q.append(mesc(i, 'C', 'I'))
for i in range(L['dv0'], L['dv1']+1): Q.append(mesc(i, 'C', 'I'))
# ── o condicional: o bloco se pinta sozinho ────────────────────────────
def cond(f, fmt_):
    return {'addConditionalFormatRule': {'index': 0, 'rule': {
            'ranges': [rng(a, b, 'B', 'I')],
            'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA',
                            'values': [{'userEnteredValue': f}]}, 'format': fmt_}}}}
Q.append(cond(f'=AND($B{a}="";$C{a}<>"")',
              {'textFormat': {'italic': True,
               'foregroundColorStyle': {'rgbColor': CLARO}}}))
Q.append(cond(f'=LEFT($B{a};5)="TOTAL"',
              {'backgroundColorStyle': {'rgbColor': F5},
               'textFormat': {'bold': True,
               'foregroundColorStyle': {'rgbColor': PRETO}}}))
Q.append(cond(f'=$B{a}="MATERIAL"',
              {'backgroundColorStyle': {'rgbColor': F7},
               'textFormat': {'bold': True,
               'foregroundColorStyle': {'rgbColor': CINZA}}}))
Q.append(cond(f'=LEFT($B{a};5)="ITEM "',
              {'backgroundColorStyle': {'rgbColor': PRETO},
               'textFormat': {'bold': True,
               'foregroundColorStyle': {'rgbColor': BRANCO}}}))
# ⭐ a conferência grita quando não fecha
Q.append({'addConditionalFormatRule': {'index': 0, 'rule': {
          'ranges': [rng(f0+4, f0+4, 'B', 'I')],
          'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA', 'values':
                          [{'userEnteredValue': f'=ROUND($I${f0+4};2)<>0'}]},
          'format': {'backgroundColorStyle': {'rgbColor': {'red': .996,
                     'green': .922, 'blue': .922}},
                     'textFormat': {'bold': True,
                     'foregroundColorStyle': {'rgbColor': VERM}}}}}}})

# ── 5b · a limpeza, que vem ANTES de tudo ───────────────────────────────
#   ⛔ a ordem importa: apagar regra por índice 0 N vezes só funciona se
#     ninguém acrescentou nenhuma no meio, e desmesclar tem de vir antes de
#     mesclar de novo, senão a API recusa.
# ⛔⛔ CRESCER VEM PRIMEIRO, antes de tudo. Formatar, mesclar ou medir uma
#   linha que ainda não existe é erro de intervalo, e um erro só derruba o
#   lote inteiro — a aba fica metade nova, metade velha.
LIMPA = ([{'appendDimension': {'sheetId': SID, 'dimension': 'ROWS',
           'length': CRESCER}}] if CRESCER else [])
LIMPA += [{'deleteConditionalFormatRule': {'sheetId': SID, 'index': 0}}
          for _ in range(N_REGRAS)]
LIMPA.append({'unmergeCells': {'range': {'sheetId': SID, 'startRowIndex': 0,
              'endRowIndex': max(FIM_HOJE, L['fim']), 'startColumnIndex': 0,
              'endColumnIndex': 11}}})
Q[:0] = LIMPA

# ── 6 · saída ──────────────────────────────────────────────────────────
OUT = dict(sheetId=SID, mapa=MAPA, layout=L, shift=SHIFT, faixas=FAIXAS,
           top_range=f"B1:K{L['blk0']-1}", top=TOP,
           notas_range=f"B{L['s_nt']}:K{L['nt1']}", notas=NOTAS,
           duvidas_range=f"B{L['s_dv']}:K{L['dv1']}", duvidas=DUVIDAS,
           requests=Q)
json.dump(OUT, open(P/f'_aba-{NOME}.json', 'w'), ensure_ascii=False)
json.dump(Q, open(P/f'_req-{NOME}.json', 'w'), ensure_ascii=False,
          separators=(',', ':'))
print(f'═══ {NOME.upper()} · sheetId {SID} ═══')
for k in ('tit','sub','s_amb','cab_mat','mat0','mat1','direto','nota',
          's_itens','cab_it','it0','it1','f0','f1','s_ni','ni0','ni1',
          's_pec','blk0','blk1','s_nt','nt0','nt1','s_dv','dv0','dv1','fim'):
    print(f'   {k:9} {L[k]}')
print(f'   SHIFT     {SHIFT:+d}  (blocos hoje em {BLK_HOJE} → {L["blk0"]})')
print(f'   {len(Q)} requests · {len(TOP)} linhas de topo · {len(NOTAS)} de nota')
print(f'   totais dos itens: {[MAPA[i] for i in sorted(MAPA)]}')
