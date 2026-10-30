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

⛔⛔⛔ CRESÇA A GRADE ANTES DE ESCREVER FÓRMULA. [30/10/2026 · a Rouparia]
  A aba tinha 10 linhas. Gravei o painel de material, que aponta para
  $K$40:$K$57 — linhas que ainda NÃO EXISTIAM. O Sheets não deu erro: ele
  INSERIU as 29 linhas que faltavam e, como toda inserção, DESLOCOU as
  referências. O painel saiu lendo $K$69:$K$86, vinte e nove linhas abaixo
  do bloco de peças, e a aba inteira veio "#VALOR!" e zero.
  ⭐ O engano é fácil porque a gravação volta "success": o que falhou não
    foi o write, foi o endereço. E o bloco de peças, gravado depois com a
    grade já grande, ficou certo — metade da aba boa, metade apontando
    para o vazio.
  ⭐⭐ A ORDEM É: 1) rowCount no tamanho final · 2) conteúdo · 3) formato.
    O `appendDimension` do próprio lote de formato vem TARDE DEMAIS para
    isso: ele roda depois do conteúdo já estar gravado e deslocado.

⛔⛔ RODE O AUDITOR ATÉ ELE FICAR LIMPO ANTES DE GERAR A ABA. [28/10/2026]
  Na Área Gourmet eu gerei a aba, apliquei os 150 requests de formato, e só
  então vi que a CAVA estava declarada no formato errado — `(frentes,
  largura)`, não metros. Corrigir mudou UMA linha de levantamento em cinco,
  a aba cresceu de 139 para 143 linhas, e TODO o formato teve de ser
  reenviado. ⭐ O formato custa o dobro do que parece: ele é digitado à mão
  nos argumentos do MCP. Levantamento primeiro, aba depois.

   uso:  python3 aba.py cozinha 104 47 186 5
         (ambiente · sheetId · linha dos blocos HOJE · linhas HOJE ·
          regras condicionais que a aba já tem — 0 se for aba nova)
"""
import sys, json, re, importlib.util, pathlib, io, contextlib, subprocess
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
# ⭐⭐ O MÓVEL VEM DAS PEÇAS **E DO CABEÇALHO** [30/10/2026].
#   ⛔ Derivar o móvel só das peças de MDF faz um ambiente SEM MARCENARIA
#     desaparecer da aba inteira: o Lavabo é APENAS espelho, e com MOV vazio
#     não há item, não há cabeçalho, não há conta — o ambiente sai em branco
#     e ninguém nota. ⭐ O CABECA é onde o ambiente DECLARA seus itens: as
#     peças dão a ORDEM, o CABECA garante que nenhum item fique de fora por
#     não ter chapa.
MOV = list(dict.fromkeys([p['movel'] for p in PECAS]
                         + list(getattr(A, 'CABECA', {}))))

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
# ⭐ +2: CORTE POR CHAPA e CORTE POR PEÇA, os dois serviços que o Jonathan
#   cravou em 28/10 e que são por AMBIENTE, não por item
# ⭐⭐ +1 no fim: a linha de FRETE [Jonathan, 29/10/2026]
#   > "eu quero uma linha so para cadastrar o frete do ambiente como se
#   >  fosse mais um item, considere um custo unitario de 200 para que eu
#   >  preencha a quantidade"
#   ⛔ Antes o frete vinha pendurado na coluna FRETE de CADA material —
#     quatro linhas da Base (Frete MDF, fita, ferragem, vidro), todas
#     vazias. Agora é UMA linha do ambiente, com QUANTIDADE que o Jonathan
#     digita. Ela entra DEPOIS da embalagem de propósito: consumível é 6%
#     sobre chapa e embalagem é 2% sobre o subtotal, e não se cobra
#     percentual de fábrica sobre o caminhão.
nmat = len(CHAPAS) + len(ACAB) + 1 + (1 if g('VIDRO') else 0) + 2 + 2 + 1
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
# ⛔⛔ A COLUNA DE FRETE SAIU [Jonathan, 30/10/2026]: "vc manteve a coluna
#   de frete. pode remover." Ela era de quando o frete vinha pendurado em
#   CADA material — quatro linhas da Base, todas vazias. Desde 29/10 o
#   frete é uma LINHA do ambiente, com quantidade que o senhor digita, e a
#   coluna só carregava valor nessa única linha: quinze células vazias para
#   servir uma.
#   ⭐ E o TOTAL saiu junto, porque TOTAL era CUSTO + FRETE: sem a coluna de
#     frete ele repetia o CUSTO, e coluna que repete a vizinha não informa,
#     só ocupa largura que falta na ESPECIFICAÇÃO.
põe(L['cab_mat'], B='MATERIAL', C='ESPECIFICAÇÃO', D='QUANTIDADE', E='UN',
    F='CUSTO', G='% DO CUSTO')

r = L['mat0']
for chave in CHAPAS:
    # ⛔⛔ ASPAS NO TEXTO QUEBRAM A FÓRMULA [30/10/2026 · a Cozinha].
    #   O texto do Branco TX da cozinha cita a prancha — "Interno em MDF
    #   Branco" — e essas aspas FECHAVAM a string do Sheets no meio,
    #   deixando o resto da linha como lixo de sintaxe. ⭐ Dentro de uma
    #   string do Sheets, aspa se escreve DUPLICADA. É o mesmo cuidado que
    #   o separador ';' pede: o gerador escreve numa linguagem que não é
    #   Python, e tem de respeitar a pontuação dela.
    prefixo = TXT.get(chave, chave).replace('"', '""')
    põe(r, B=chave,
        C=f'="{prefixo} · "&ROUND({M2(f"$B{r}")};1)&" m² de peças"',
        D=f'=ROUNDUP({M2(f"$B{r}")}/({AREA}*{APR}))', E='chapas',
        F=f'=D{r}*VLOOKUP($B{r};precos;2;FALSE)')
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
        F=f'=D{r}*VLOOKUP("{ch}";precos;2;FALSE)')
    r += 1
L['acab1'] = r - 1

FERR = [(B.CH_CORREDICA, 'corrediça',
         [x for x in g('GAVETAS') if not (len(x) > 4 and x[4] == 'touch')]),
        (B.CH_DOBRADICA, 'dobradiça', g('PORTAS')),
        (B.CH_DOBR_VIDRO, None, [x for x in g('PORTAS') if x[4] == B.DOBR_VIDRO]),
        ('Báscula HK-XS', 'articulador HK-XS', g('BASCULAS')),
        # ⭐ slim no lugar do pulsador [Jonathan, 28/10] · são R$ 65 por
        #   báscula de diferença, e a Base já avisava que não se somam
        # ⛔ só as básculas que abrem pelo slim. Na Lavanderia elas abrem
        #   pelo Alças Traso, e o slim não existe lá.
        ('Puxador slim', 'puxador slim',
         [b for b in g('BASCULAS') if (b[3] if len(b) > 3 else 'slim') == 'slim']),
        (B.CH_PUXADOR_128, 'puxador Alças Traso de 128', g('PUXADORES')),
        ('Moldura provençal', 'moldura provençal', g('MOLDURA')),
        ('Cava usinada', 'cava usinada', g('CAVA')),
        ('LED conjunto', 'LED', g('LED')),
        ('Alma de aço', 'alma de aço', g('ALMAS')),
        ('Suporte de prateleira', 'suporte de prateleira',
         [1] if B.prateleiras(PECAS) else []),
        ('Corrediça touch', 'corrediça touch',
         [x for x in g('GAVETAS') if len(x) > 4 and x[4] == 'touch']),
        ('Cabideiro', 'cabideiro', g('CABIDEIROS')),
        *[(ch, nome.lower(), [1]) for ch, nome in
          dict((o[5], o[1]) for o in g('OUTRAS')).items()],
        ('Serralheria estrutural', 'serralheria estrutural', g('SERRALHERIA'))]
ativos = [(c, rot) for c, rot, lst in FERR if lst]
# ⛔ cava, LED e moldura se medem em metro ou em frente, não em peça:
#   não entram na contagem de "peças de ferragem"
# ⛔⛔ E USINAGEM NENHUMA ENTRA, por PREFIXO e não por nome [30/10/2026].
#   A lista nominal pegava "Usinagem de encaixe de prateleira" e deixava
#   passar "Usinagem de muxarabi vazado": o Office saiu declarando
#   "531,3 peças" de ferragem, que são os METROS de router do painel. Um
#   serviço medido em metro, somado numa coluna que conta peça, não dá erro
#   na tela — dá um número absurdo que ninguém confere.
POR_METRO = ('Cava usinada', 'LED conjunto', 'Moldura provençal',
             'Serralheria estrutural', 'Perfil de proteção de piso',
             'Palhinha natural', 'Estofamento em linho')
conta  = [c for c, rot in ativos
          if c not in POR_METRO and not c.startswith('Usinagem')]
# ⛔ E O RÓTULO SE REPETE: a Despensa tem 'Suporte de prateleira'
#   contado das peças e 'Suporte oculto' vindo de OUTRAS, e os dois
#   se descrevem como "suporte de prateleira" — a especificação saía
#   "Suporte de prateleira e suporte de prateleira".
rots   = list(dict.fromkeys(rot for c, rot in ativos if rot))
# ⛔ .capitalize() rebaixa o resto da frase, e 'LED' virava 'led'
# ⛔ COM UM RÓTULO SÓ, O "e" SOBRAVA: o Lavabo saiu com a especificação
#   começando em " e perfil de proteção de piso". Vírgula e "e" só existem
#   quando há o que separar.
if len(rots) > 1:
    frase = ', '.join(rots[:-1])
    desc  = frase[:1].upper() + frase[1:] + ' e ' + rots[-1]
elif rots:
    desc  = rots[0][:1].upper() + rots[0][1:]
else:
    desc  = 'Nenhuma — este ambiente não leva ferragem'
L['ferr'] = r
põe(r, B='Ferragem, terceirizados e iluminação',
    # ⭐ a linha de ferragem vem da BASE do projeto, não de um padrão fixo
    # ⛔⛔ E SÓ SE DIZ O QUE EXISTE [30/10/2026 · a Despensa]. A frase vinha
    #   fixa — "linha Hettich · ⛔ sem fonte: as fitas da casa são 110 V" —
    #   em TODO ambiente. Na Despensa, que só tem quadro de metalon, saía
    #   "Estrutura de metalon · linha Hettich", citando uma marca de
    #   ferragem de movimento que não existe lá, e avisando de uma fonte de
    #   LED que ninguém pediu. ⭐ Frase que fala do que não está na aba é
    #   pior que frase nenhuma: ela faz o leitor procurar o que não existe.
    C=desc
      + (f' · linha {getattr(A, "LINHA", getattr(B, "LINHA", "Hettich"))}'
         if any(c in (B.CH_CORREDICA, B.CH_DOBRADICA, 'Corrediça touch')
                for c, _ in ativos) else '')
      + (' · ⛔ sem fonte: as fitas da casa são 110 V'
         if any(c == 'LED conjunto' for c, _ in ativos) else ''),
    # ⛔ E O AMBIENTE PODE NÃO TER NENHUMA PEÇA DE FERRAGEM. O Office é só
    #   um painel: usinagem e perfil, os dois por metro. Com `conta` vazia o
    #   join saía "SUMPRODUCT(()*...)", fórmula inválida — e o Sheets a
    #   aceita como TEXTO, deixando a célula com cara de fórmula e sem
    #   conta nenhuma. Zero é a resposta honesta: não há peça a contar.
    D=('=SUMPRODUCT((' + '+'.join(f'({K}="{c}")' for c in conta) +
       f')*IF(ISNUMBER($F${a}:$F${b});$F${a}:$F${b};0))') if conta else 0, E='peças',
    # ⭐ o custo de ferragem é o RESTO: tudo que tem chave, menos chapa,
    #   menos acabamento, menos vidro. Assim nenhuma linha nova de ferragem
    #   pode escapar da conta por eu não a ter listado aqui.
    F=f'=SUMIF({K};"<>";$I${a}:$I${b})' +
      ''.join(f'-SUMIF({K};$B{L["mat0"]+i};$I${a}:$I${b})'
              for i in range(len(CHAPAS))) +
      ''.join(f'-SUMIF({K};$B{L["acab0"]+i};$I${a}:$I${b})'
              for i in range(len(ACAB))) +
      (f'-SUMIF({K};"Vidro reflecta";$I${a}:$I${b})'
       f'-SUMIF({K};"Espelho";$I${a}:$I${b})' if g('VIDRO') else ''))
r += 1
if g('VIDRO'):
    põe(r, B='Vidro e espelho',
        C='Vidraçaria · ⛔ SEM PREÇO na Base: a linha existe vazia de '
          'propósito, para gritar',
        D=f'={M2(chr(34)+"Vidro reflecta"+chr(34))}+{M2(chr(34)+"Espelho"+chr(34))}',
        E='m²',
        F=f'=SUMIF({K};"Vidro reflecta";$I${a}:$I${b})'
          f'+SUMIF({K};"Espelho";$I${a}:$I${b})')
    r += 1
L['ult_mat'] = r - 1                        # ⭐ onde acaba o material de fato
# ⭐⭐ OS DOIS SERVIÇOS DE CORTE [Jonathan, 28/10/2026]: "Em cada ambiente
#   considere o custo de corte por chapa de 2.00 e corte por peça de 2.50".
#   ⛔ Entram DEPOIS de `ult_mat` de propósito: são serviço do ambiente, não
#     material rateado por item, e por isso ficam fora da CONFERÊNCIA — que
#     compara o rateio dos itens com o painel de material.
põe(r, B='Corte · por chapa',
    C='Serviço de corte, por chapa comprada · R$ 2,00',
    # ⛔⛔ SEM CHAPA, ZERO — e não "=". O Lavabo é apenas espelho: a lista
    #   de chapas sai vazia, o join devolve string vazia e a célula fica com
    #   um "=" solto, que é fórmula inválida. ⭐ O Sheets aceita "=" como
    #   TEXTO e não reclama: a linha fica muda e ninguém vê.
    D=('=' + '+'.join(f'D{L["mat0"]+i}' for i in range(len(CHAPAS))))
      if CHAPAS else 0, E='chapas',
    F=f'=D{r}*VLOOKUP("Corte por chapa";precos;2;FALSE)')
L['corte_ch'] = r; r += 1
põe(r, B='Corte · por peça',
    C='Serviço de corte, por peça cortada · R$ 2,50 · ⛔ conta a PEÇA, não a '
      'linha: uma linha de 4 prateleiras são 4 peças',
    # ⛔⛔ A CONTA ERA POR UNIDADE ("m²") E PEGAVA O QUE NÃO É NOSSO.
    #   Espelho, vidro e LACA também saem em m², e nenhum dos três passa
    #   pela nossa serra: o vidraceiro corta o espelho, a cabine pinta a
    #   laca. Pior na laca, cuja QUANTIDADE é a ÁREA — 12,5 m² de laca
    #   entravam nesta linha como "12,5 peças" a R$ 2,50. ⭐ Quem define a
    #   peça cortada por nós é a CHAVE: só o que começa em "MDF " é chapa
    #   que entra na seccionadora.
    D=f'=SUMPRODUCT((LEFT({K};4)="MDF ")*IF(ISNUMBER($F${a}:$F${b});'
      f'$F${a}:$F${b};0))', E='peças',
    F=f'=D{r}*VLOOKUP("Corte por peça";precos;2;FALSE)')
L['corte_pc'] = r; r += 1
põe(r, B='Consumíveis',
    C='Cola, lixa, parafuso, cavilha, tapa-furo, fundo e verniz · 6% sobre '
      'chapa, fita e filetagem',
    # ⛔ FAIXA INVERTIDA quando não há chapa nem fita: acab1 cai abaixo de
    #   mat0 e saía SUM(F7:F6), que o Sheets lê como erro de referência.
    #   ⭐ Consumível é 6% de chapa, fita e filetagem — sem as três, é zero.
    F=(f'=SUM(F{L["mat0"]}:F{L["acab1"]})*VLOOKUP("Consumíveis";precos;2;FALSE)'
       if L['acab1'] >= L['mat0'] else 0))
L['cons'] = r; r += 1
põe(r, B='Embalagem', C='Papelão, filme e cantoneira · 2% sobre o subtotal',
    F=f'=SUM(F{L["mat0"]}:F{L["cons"]})*VLOOKUP("Embalagem";precos;2;FALSE)')
L['embal'] = r; r += 1
# ⭐⭐ A LINHA DE FRETE DO AMBIENTE [Jonathan, 29/10/2026] · R$ 200 a viagem
#   ⛔ A QUANTIDADE É DELE: a célula D é a única do painel de material que
#     não é fórmula, e por isso vai em AMARELO. Sai 0 e espera.
#   ⭐ O valor vai na coluna de CUSTO como o de todo mundo. O Painel acha o
#     frete do ambiente pelo RÓTULO da linha, não por coluna — e rótulo não
#     se desloca quando uma coluna some.
L['frete'] = r
põe(r, B='Frete', C='⭐ Frete do ambiente · R$ 200 a viagem · ⛔ A QUANTIDADE É '
                    'SUA: digite quantas viagens este ambiente leva, e o '
                    'frete aparece aqui e no Painel · sai ZERO e espera',
    D=0, E='viagem',
    F=f'=D{r}*VLOOKUP("Frete";precos;2;FALSE)')
for i in range(L['mat0'], L['mat1'] + 1):
    põe(i, G=f'=IFERROR(F{i}/$F${L["direto"]};"")')
d = L['direto']
põe(d, B='CUSTO DIRETO DO AMBIENTE', F=f'=SUM(F{L["mat0"]}:F{L["mat1"]})',
    G=f'=IFERROR(F{d}/$F${d};"")')
põe(L['nota'], C=F['nota'])

põe(L['s_itens'], B='  OS ITENS   ·   cada móvel com o seu custo, porque é '
                    'assim que a fábrica produz e o cliente confere')
põe(L['cab_it'], B='ITEM', C='MÓVEL', D='MEDIDA GERAL', I='CUSTO')
# ⛔ o nome do móvel vem com a referência da prancha na frente — "DET 01
#    Lateral" — e ela sai do nome do ITEM, que já tem a sua numeração. Nos
#    itens unificados a referência é uma FAIXA, "DET 01 a 06" ou "DET 01 e
#    02", e um split por espaço cortava no lugar errado: a aba saía com o
#    móvel chamado "a 06 Conjunto da lavanderia".
SO_DET = re.compile(r'^(?:DET|ELEVAÇÃO)\s+\d+(?:\s*(?:a|e|,|\+|/)\s*\d+)*\s+')
for i, mov in enumerate(MOV, 1):
    põe(L['it0'] + i - 1, B=i, C=SO_DET.sub('', mov),
        D=A.CABECA[mov][0], I=f'=I{MAPA[i]}')
f0 = L['f0']
põe(f0,   B='Soma dos itens · chapa rateada em fração',
          I=f'=SUM(I{L["it0"]}:I{L["it1"]})')
# ⛔ outra vez o "=" solto: sem chapa não há arredondamento, e o certo é 0.
põe(f0+1, B='Arredondamento de chapa para número cheio · ⛔ a regra de ferro',
          I=('=' + '+'.join(f'F{L["mat0"]+i}' for i in range(len(CHAPAS))) +
             ''.join(f'-SUMIF({K};$B{L["mat0"]+i};$I${a}:$I${b})'
                     for i in range(len(CHAPAS)))) if CHAPAS else 0)
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
PRETO  = {'red': .102, 'green': .102, 'blue': .102}
CINZA  = {'red': .42, 'green': .42, 'blue': .42}
CLARO  = {'red': .675, 'green': .675, 'blue': .675}
OURO   = {'red': .686, 'green': .514, 'blue': .231}
VERM   = {'red': .776, 'green': .157, 'blue': .157}
BRANCO = {'red': 1, 'green': 1, 'blue': 1}
F7     = {'red': .969, 'green': .969, 'blue': .969}
F5     = {'red': .961, 'green': .961, 'blue': .961}
# ⭐ o MESMO amarelo das quatro células digitáveis da aba Preço e
#   Comissões: na planilha inteira, amarelo significa "escreva aqui"
AMARELO = {'red': 1, 'green': .9490196, 'blue': .8}
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
         'foregroundColor': fg}
    if bd: t['bold'] = True
    if it: t['italic'] = True
    f = {'textFormat': t, 'horizontalAlignment': al,
         'verticalAlignment': 'MIDDLE', 'wrapStrategy': wr}
    if bg: f['backgroundColor'] = bg
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
RUA  = {'bottom': {'style': 'SOLID', 'width': 1, 'color': PRETO}}
TETO = {'top': {'style': 'SOLID_THICK', 'width': 3, 'color': OURO}}

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
Q.append(rc(L['cab_mat'], L['cab_mat'], 'B', 'G', fm(8, True, fg=CINZA, bg=F7)))
Q.append(rc(L['cab_mat'], L['cab_mat'], 'D', 'D', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
Q.append(rc(L['cab_mat'], L['cab_mat'], 'E', 'E', fm(8, True, fg=CINZA, bg=F7, al='CENTER')))
Q.append(rc(L['cab_mat'], L['cab_mat'], 'F', 'G', fm(8, True, fg=CINZA, bg=F7, al='RIGHT')))
m0, m1 = L['mat0'], L['mat1']
Q.append(rc(m0, m1, 'C', 'C', fm(9, fg=CINZA)))
# ⛔ SEM padrão: a coluna mistura chapa (26), metro de fita (482,8) e m²
#   de vidro (5,6). Qualquer padrão estraga um dos três — '0.0' faria
#   26 chapas aparecer como '26,0'.
Q.append(rc(m0, m1, 'D', 'D', fm(10, al='RIGHT')))
Q.append(rc(m0, m1, 'E', 'E', fm(9, fg=CINZA, al='CENTER')))
Q.append(rc(m0, m1, 'F', 'F', fm(10, al='RIGHT', num=MOEDA)))
Q.append(rc(m0, m1, 'G', 'G', fm(10, fg=CINZA, al='RIGHT', num=PCT)))
# ⛔ H e I ficam LIMPAS no painel de material: sem elas a especificação da
#   coluna C respira, e o que sobrava ali eram duas colunas de repetição.
Q.append(rc(m0, m1, 'H', 'I', fm(10)))
# ⭐⭐ A QUANTIDADE DE VIAGENS DE FRETE É A ÚNICA CÉLULA DIGITÁVEL DO PAINEL
#   de material — todas as outras são fórmula. Vai em AMARELO, pela mesma
#   convenção das quatro células da aba Preço e Comissões, para quem abre a
#   planilha saber de longe onde pode escrever.
Q.append(rc(L['frete'], L['frete'], 'D', 'D',
            fm(10, True, al='RIGHT', bg=AMARELO, num=INT)))
Q.append(rc(d, d, 'B', 'G', fm(11, True, bg=F5, bor=TETO)))
Q.append(rc(d, d, 'F', 'F', fm(11, True, bg=F5, bor=TETO, al='RIGHT', num=MOEDA)))
Q.append(rc(d, d, 'G', 'G', fm(11, True, bg=F5, bor=TETO, al='RIGHT', num=PCT)))
Q.append(rc(d, d, 'H', 'I', fm(11, True)))
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
               'foregroundColor': CLARO}}))
Q.append(cond(f'=LEFT($B{a};5)="TOTAL"',
              {'backgroundColor': F5,
               'textFormat': {'bold': True,
               'foregroundColor': PRETO}}))
Q.append(cond(f'=$B{a}="MATERIAL"',
              {'backgroundColor': F7,
               'textFormat': {'bold': True,
               'foregroundColor': CINZA}}))
Q.append(cond(f'=LEFT($B{a};5)="ITEM "',
              {'backgroundColor': PRETO,
               'textFormat': {'bold': True,
               'foregroundColor': BRANCO}}))
# ⭐ a conferência grita quando não fecha
Q.append({'addConditionalFormatRule': {'index': 0, 'rule': {
          'ranges': [rng(f0+4, f0+4, 'B', 'I')],
          'booleanRule': {'condition': {'type': 'CUSTOM_FORMULA', 'values':
                          [{'userEnteredValue': f'=ROUND($I${f0+4};2)<>0'}]},
          'format': {'backgroundColor': {'red': .996,
                     'green': .922, 'blue': .922},
                     'textFormat': {'bold': True,
                     'foregroundColor': VERM}}}}}})

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
