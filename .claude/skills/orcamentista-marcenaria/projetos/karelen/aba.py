# -*- coding: utf-8 -*-
"""Gerador das abas de ambiente — Karylen e Henrique.

Padrão da casa: cada ITEM é um bloco autossuficiente; o painel do ambiente
é DERIVADO por chave; só OS PARÂMETROS se digita.

⭐ [Jonathan 27/11/2026] três acréscimos ao padrão:
   1. LOGÍSTICA — espaço para os fretes
   2. DIÁRIAS DE PROFISSIONAL — espaço para dia de terceiro
      ⛔ montagem e fabricação da equipe NÃO entram aqui: são comissão
         (regra do SKILL.md). Estas linhas são para terceiro contratado.
   3. COMPLEXIDADE POR ITEM — cada item tem a sua, e a MC do ambiente é a
      MÉDIA PONDERADA PELO CUSTO dos itens. Antes era uma por ambiente.

⛔ pt-BR: dentro de fórmula o decimal é VÍRGULA; no padrão do TEXT() é PONTO.
⛔ aspa dupla dentro de fórmula tem de ser duplicada.
"""
import sys, os
_d = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _d); sys.path.insert(0, os.path.join(_d, '..'))
from itens import (fechar, ITENS, CHAPA_M2, APROV, MDF, FITA, FILET, CONSUM,
                   CORTE_CH, CORTE_PC)
import motor_mc as M

def N(v):
    """número literal DENTRO de fórmula · decimal com vírgula"""
    return ('%g' % v).replace('.', ',')

def T(t):
    """texto dentro de fórmula · aspa dupla duplicada"""
    return str(t).replace('"', '""')

DIFIC = ['Médio', 'Difícil', 'Complexo']        # +5 / +10 / +20 pontos de MC
PTS   = {'Médio': 0.05, 'Difícil': 0.10, 'Complexo': 0.20}

# complexidade atribuída item a item, pelo que a peça exige
# (ripado vazado, pivô, palhinha, vidro, serralheria, altura regulável…)
def complexidade(nome):
    n = nome.lower()
    if any(k in n for k in ('pivotante', 'adega', 'ripado vazado', 'altura regul')):
        return 'Complexo'
    if any(k in n for k in ('ripad', 'palhinha', 'vidro', 'espelh', 'mão francesa',
                            'correr', 'báscula', 'basculas', 'cabeceira', 'led',
                            'escrivaninha', 'chopeira')):
        return 'Difícil'
    return 'Médio'

class Aba:
    """linhas com resolução em duas passadas: célula pode ser callable(ix)."""
    def __init__(s):
        s.ln = []; s.mk = {}
    def add(s, *cels):
        s.ln.append(list(cels)); return len(s.ln)      # 1-based
    def vazia(s, n=1):
        for _ in range(n): s.ln.append([])
    def marca(s, nome, n=None):
        s.mk[nome] = len(s.ln) + 1 if n is None else n
    def resolve(s):
        ix = s.mk
        out = []
        for r in s.ln:
            out.append([c(ix) if callable(c) else c for c in r])
        return out


# ── colunas ───────────────────────────────────────────────────────────────
# A rótulo · B MATERIAL · C ESPECIFICAÇÃO · D C · E L · F QTD · G UN
# H R$ UN · I CUSTO · J (livre) · K CHAVE NA BASE
# ⭐ intervalos nomeados: a fórmula fica curta e legível, e um só lugar
#   aponta para a Base. Criados na planilha por addNamedRange.
def PRECO(k):   return '=IFERROR(VLOOKUP(%s;Base;2;FALSE);0)' % k
P_AREA  = 'ChapaM2'    # área útil da chapa (m²)
P_APROV = 'Aprov'      # aproveitamento
P_CONS  = 'Consum'     # consumíveis
P_EMB   = 'Embal'      # embalagem

CHAVE_CH = {6: 'MDF cor 6', 15: 'MDF cor 15', 18: 'MDF cor 18'}

def monta(nome_amb, itens_amb, chapas):
    """Devolve (linhas, marcadores) de uma aba de ambiente."""
    A = Aba()
    A.add(nome_amb.upper())
    A.add('Residência Henrique e Karylen · Brisas da Pampulha · detalhamento rev. 00')
    A.vazia()

    # ── ① O AMBIENTE EM NÚMEROS ──────────────────────────────────────────
    A.add('① O AMBIENTE EM NÚMEROS — tudo derivado das peças, nada digitado')
    A.add('', 'MATERIAL', 'ESPECIFICAÇÃO', '', '', 'QTD', 'UN', 'R$ UN', 'CUSTO', '', 'CHAVE')
    amb_ini = len(A.ln) + 1
    for esp in sorted(chapas):
        k = CHAVE_CH[esp]
        A.add('', 'Chapa', 'MDF %d mm · o que o ambiente compra' % esp, '', '',
              (lambda e=esp: (lambda ix: '=ROUNDUP(ROUND(SUMIF($K$%d:$K$%d;"%s";$J$%d:$J$%d)/%s/%s;6);0)'
                 % (ix['pec_ini'], ix['pec_fim'], T(CHAVE_CH[e]),
                    ix['pec_ini'], ix['pec_fim'], P_AREA, P_APROV)))(),
              'chapa', PRECO('$K%d' % (len(A.ln)+1)), None, '', CHAVE_CH[esp])
        A.ln[-1][8] = (lambda r=len(A.ln): (lambda ix: '=ROUND($F%d*$H%d;2)' % (r, r)))()
    amb_chapa_fim = len(A.ln)
    for ch, un in (('Fita de borda cor', 'm'), ('Filetagem máquina', 'm')):
        r = len(A.ln) + 1
        A.add('', 'Insumo', ch, '', '',
              (lambda c=ch: (lambda ix: '=ROUND(SUMIF($K$%d:$K$%d;"%s";$F$%d:$F$%d);2)'
                 % (ix['pec_ini'], ix['pec_fim'], T(c), ix['pec_ini'], ix['pec_fim'])))(),
              un, PRECO('$K%d' % r),
              (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', ch)
    amb_fim = len(A.ln)
    A.marca('amb_ini', amb_ini); A.marca('amb_chapa_fim', amb_chapa_fim)
    A.marca('amb_fim', amb_fim)
    A.vazia()

    # ── ② OS ITENS ───────────────────────────────────────────────────────
    A.add('② OS ITENS — o custo PUXA o total do bloco · a COMPLEXIDADE vira MC')
    A.add('', 'ITEM', 'MEDIDA GERAL', '', '', 'COMPLEXIDADE', '', 'PONTOS', 'CUSTO')
    ite_ini = len(A.ln) + 1
    for i, L in enumerate(itens_amb, 1):
        r = len(A.ln) + 1
        cx = complexidade(L['it'].nome)
        A.add('', 'ITEM %02d · %s' % (i, L['it'].nome), L['it'].medida, '', '',
              cx, '',
              (lambda rr=r: (lambda ix: '=IFERROR(VLOOKUP($F%d;{"Médio"\\%s;"Difícil"\\%s;"Complexo"\\%s};2;FALSE);%s)'
                 % (rr, N(0.05), N(0.10), N(0.20), N(0.05))))(),
              (lambda n=i: (lambda ix: '=$I$%d' % ix['tot_%d' % n]))())
    ite_fim = len(A.ln)
    A.marca('ite_ini', ite_ini); A.marca('ite_fim', ite_fim)
    r = len(A.ln) + 1
    A.add('', 'CUSTO DIRETO DO AMBIENTE', 'peças + insumos + ferragem + terceiros + logística + embalagem',
          '', '', '', '', '',
          (lambda: (lambda ix: '=ROUND(SUM($I$%d:$I$%d)+$I$%d+$I$%d;2)'
             % (ix['ite_ini'], ix['ite_fim'], ix['log_tot'], ix['emb'])))())
    A.marca('cd', r)
    r = len(A.ln) + 1
    A.add('', 'MC DO AMBIENTE', 'alvo do projeto + média dos pontos de complexidade, PONDERADA PELO CUSTO',
          '', '', '', '', '',
          (lambda: (lambda ix: '=ROUND(IFERROR(SUMPRODUCT($H$%d:$H$%d;$I$%d:$I$%d)/SUM($I$%d:$I$%d);%s);4)'
             % (ix['ite_ini'], ix['ite_fim'], ix['ite_ini'], ix['ite_fim'],
                ix['ite_ini'], ix['ite_fim'], N(0.05))))())
    A.marca('mc', r)
    A.vazia()
    return A

def pecas_e_fim(A, itens_amb):
    """③ as peças item por item · ④ logística · ⑤ parâmetros · ⑥ conferência"""
    A.add('③ AS PEÇAS, ITEM POR ITEM — cada bloco é autossuficiente')
    pec_ini = len(A.ln) + 2
    for i, L in enumerate(itens_amb, 1):
        it = L['it']
        A.add('', 'ITEM %02d · %s' % (i, it.nome), it.medida)
        A.add('', 'MATERIAL', 'ESPECIFICAÇÃO', 'C', 'L', 'QTD', 'UN', 'R$ UN', 'CUSTO', 'M²', 'CHAVE')
        a = len(A.ln) + 1
        for desc, C, Lg, q, esp, fita in it.lista:
            r = len(A.ln) + 1
            A.add('', 'Chapa %d mm' % esp, desc, C, Lg, q, 'pç', PRECO('$K%d' % r),
                  (lambda rr=r: (lambda ix: '=ROUND($J%d/%s/%s*$H%d;2)'
                     % (rr, P_AREA, P_APROV, rr)))(),
                  (lambda rr=r: (lambda ix: '=ROUND($D%d*$E%d*$F%d/10000;4)' % (rr, rr, rr)))(),
                  CHAVE_CH[esp])
        ft = round(it.fita*1.15, 2)
        if ft:
            for ch in ('Fita de borda cor', 'Filetagem máquina'):
                r = len(A.ln) + 1
                A.add('', 'Insumo', ch + ' · perímetro aparente ×1,15', '', '', ft, 'm',
                      PRECO('$K%d' % r),
                      (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', ch)
        for nome, q, v in it.fers:
            r = len(A.ln) + 1
            A.add('', 'Ferragem', nome, '', '', q, 'un', v,
                  (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', 'ferragem')
        for nome, v in it.ters:
            r = len(A.ln) + 1
            A.add('', 'Terceiro', nome, '', '', 1, 'vb', round(v, 2),
                  (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', 'terceiro')
        r = len(A.ln) + 1
        A.add('', 'Consumíveis', 'cola, parafuso, limpeza e acabamento · 6% de chapa e fita',
              '', '', 1, 'vb',
              (lambda aa=a, rr=r: (lambda ix: '=ROUND(SUMPRODUCT(($K$%d:$K$%d<>"ferragem")*($K$%d:$K$%d<>"terceiro")*$I$%d:$I$%d)*%s;2)'
                 % (aa, rr-1, aa, rr-1, aa, rr-1, P_CONS)))(),
              (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', 'consumível')
        r = len(A.ln) + 1
        A.add('', 'Corte', 'R$ 2,50 por peça (regra 10)', '', '',
              (lambda aa=a, rr=r: (lambda ix: '=SUMIF($K$%d:$K$%d;"MDF*";$F$%d:$F$%d)' % (aa, rr-1, aa, rr-1)))(),
              'pç', CORTE_PC,
              (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', 'corte')
        r = len(A.ln) + 1
        A.add('', 'TOTAL DO ITEM %02d' % i, '', '', '', '', '', '',
              (lambda aa=a: (lambda ix: '=ROUND(SUM(OFFSET($I$%d;0;0;MAX(1;ROW()-%d);1));2)' % (aa, aa)))())
        A.marca('tot_%d' % i, r)
        A.vazia()
    A.marca('pec_ini', pec_ini); A.marca('pec_fim', len(A.ln))

    # ── ④ LOGÍSTICA E DIÁRIAS ────────────────────────────────────────────
    A.add('④ LOGÍSTICA E DIÁRIAS DE PROFISSIONAL')
    A.add('', '⛔ montagem e fabricação da EQUIPE não entram aqui: são comissão (7,5% no degrau 3). Estas linhas são para TERCEIRO contratado e para os fretes.')
    A.add('', 'MATERIAL', 'ESPECIFICAÇÃO', '', '', 'QTD', 'UN', 'R$ UN', 'CUSTO')
    log_ini = len(A.ln) + 1
    for nome, un, q, v in (('Frete de entrega', 'viagem', 1, 350),
                           ('Frete de retorno / retrabalho', 'viagem', 0, 350),
                           ('Frete de insumo e ferragem', 'viagem', 1, 180),
                           ('Diária de marceneiro terceiro', 'dia', 0, 320),
                           ('Diária de montador terceiro', 'dia', 0, 300),
                           ('Diária de ajudante', 'dia', 0, 180),
                           ('Diária de vidraceiro / serralheiro', 'dia', 0, 450)):
        r = len(A.ln) + 1
        A.add('', 'Logística' if 'Frete' in nome else 'Diária', nome, '', '', q, un, v,
              (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', 'logística')
    log_fim = len(A.ln)
    r = len(A.ln) + 1
    A.add('', 'TOTAL DE LOGÍSTICA E DIÁRIAS', '', '', '', '', '', '',
          (lambda a=log_ini, z=log_fim: (lambda ix: '=ROUND(SUM($I$%d:$I$%d);2)' % (a, z)))())
    A.marca('log_tot', r)
    r = len(A.ln) + 1
    A.add('', 'EMBALAGEM', 'caixa e plástico para transportar · % sobre o custo direto',
          '', '', 1, 'vb',
          (lambda: (lambda ix: '=ROUND((SUM($I$%d:$I$%d)+$I$%d)*%s;2)'
             % (ix['ite_ini'], ix['ite_fim'], ix['log_tot'], P_EMB)))(),
          (lambda rr=r: (lambda ix: '=ROUND($F%d*$H%d;2)' % (rr, rr)))(), '', 'embalagem')
    A.marca('emb', r)
    A.vazia()

    # ── ⑤ CONFERÊNCIA ────────────────────────────────────────────────────
    A.add('⑤ CONFERÊNCIA — as três têm de dar zero')
    for rot, f in (
        # 1 · nenhuma linha de peça fora de um bloco: a soma dos TOTAL DO ITEM
        #     tem de bater com a soma de TODAS as linhas que têm chave em K
        ('nenhuma linha órfã — Σ totais de item × Σ linhas com chave',
         lambda ix: '=ROUND(SUM($I$%d:$I$%d)-SUMIF($K$%d:$K$%d;"<>";$I$%d:$I$%d);2)'
             % (ix['ite_ini'], ix['ite_fim'], ix['pec_ini'], ix['pec_fim'],
                ix['pec_ini'], ix['pec_fim'])),
        # 2 · o painel do ambiente derива das mesmas peças: a área de chapa
        #     lida pelo painel tem de ser a área somada das linhas de chapa
        ('nenhuma peça sem preço — linhas com chave e R$ UN zerado',
         lambda ix: '=SUMPRODUCT(($K$%d:$K$%d<>"")*($K$%d:$K$%d<>"corte")*($H$%d:$H$%d=0))'
             % (ix['pec_ini'], ix['pec_fim'], ix['pec_ini'], ix['pec_fim'],
                ix['pec_ini'], ix['pec_fim'])),
        # 3 · o custo direto é exatamente itens + logística + embalagem
        ('custo direto × itens + logística + embalagem',
         lambda ix: '=ROUND($I$%d-SUM($I$%d:$I$%d)-$I$%d-$I$%d;2)'
             % (ix['cd'], ix['ite_ini'], ix['ite_fim'], ix['log_tot'], ix['emb'])),
    ):
        A.add('', rot, '', '', '', '', '', '', f)
    return A


def gera():
    """Monta todas as abas e devolve {nome: linhas}."""
    r = fechar()
    out = {}
    for amb in sorted(r):
        d = r[amb]
        A = monta(amb, d['itens'], d['chapas'])
        pecas_e_fim(A, d['itens'])
        out[amb] = A.resolve()
    return out

if __name__ == '__main__':
    g = gera()
    for k in sorted(g):
        print('%-26s %3d linhas' % (k, len(g[k])))
    print('TOTAL %d linhas' % sum(len(v) for v in g.values()))
