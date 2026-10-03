#!/usr/bin/env python3
"""Migra os preenchimentos de uma versão anterior do Custo por Projeto.

    python3 gerar-custo-projeto.py                      # estrutura nova, vazia
    python3 migrar-custo-projeto.py ANTIGO.xlsx         # traz os dados para ela

Por que existe: a ficha ganhou uma linha (comissão de projetista), três colunas
(projetista, % e comissão) e seis linhas no bloco 5. Tudo que estava abaixo do
bloco 4 desceu. Inserir linha no arquivo pronto não resolve — o openpyxl não
reescreve as referências, e são 16 abas. O caminho seguro é o contrário:
gerar a estrutura nova e trazer para ela SÓ o que foi digitado à mão.

O que este script NÃO traz, e por quê:
  · célula de fórmula que foi sobrescrita à mão — a fórmula volta no lugar;
    quando o número digitado tinha informação, ele é levado para o campo certo
    (o valor de venda vai para o bloco 1; realizado de categoria vai para o
    livro do bloco 8) e o movimento é registrado no relatório final;
  · nomes soltos no bloco 5 — agora estão no cadastro, vindos da aba Listas.

Nada é sobrescrito no arquivo antigo: ele é só lido.
"""
import json
import sys
import unicodedata

import openpyxl

NOVO = 'Valvic_Custo_por_Projeto.xlsx'
FIXAS = ('Instruções', 'Painel Geral', 'Listas', 'Ficha Modelo')

# ── mapa de linhas da versão ANTERIOR (10 colunas, sem projetista) ────────
V0 = dict(
    R_ID2=7, R_ID4=9, R_KPI_V=13, R_RES0=16, R_RESF=21, R_VENDA=28,
    R_IMP=32, R_RTP=37, R_AMB0=43, R_AMBF=54,
    R_COORD=59, R_PRODC=60, R_MONTC=61,
    R_CL0=66, R_CLF=77,
    R_RB0=104, R_RBF=115, R_RB_SUB=116,
    R_LAN0=120, R_LANF=179,
)
CATS_V0 = {  # categoria → linha, na versão anterior
    'MDF e MDP': 82, 'Fita de borda': 83, 'Ferragens': 84, 'Vidros e espelhos': 85,
    'Esquadrias': 86, 'Lâmina natural': 87, 'Consumíveis': 88,
    'Acabamento': 90, 'Serralheria': 91, 'Vidraceiro': 92, 'Outro terceirizado': 93,
    'Uber e aplicativo': 95, 'Carreto e entrega': 96, 'Deslocamento da equipe': 97,
    'Frete de material': 98, 'Estacionamento e pedágio': 99,
}

# ── nomes que mudaram de grafia ao entrar no cadastro ─────────────────────
APELIDOS = {
    'deivson': 'Deivison', 'deivison': 'Deivison',
    'cezar': 'Cesar', 'cesar': 'Cesar', 'césar': 'Cesar',
    'jonh': 'Jhon', 'jhon': 'Jhon', 'jon': 'Jhon',
    'jackson': 'Jackson', 'samuel': 'Samuel', 'joelson': 'Joelson',
    'ronald': 'Ronald', 'jomar': 'Jomar', 'davi': 'Davi', 'bruno': 'Bruno',
    'wallace': 'Wallace', 'douglas': 'Douglas',
    'lorrane': 'Lorrane', 'lucas': 'Lucas', 'bruna': 'Bruna',
}


def chave(txt):
    t = unicodedata.normalize('NFKD', str(txt).strip().lower())
    return ''.join(c for c in t if not unicodedata.combining(c))


def normaliza(valor, cadastro, onde, aviso):
    """Devolve o nome do cadastro que corresponde ao que estava digitado."""
    if valor in (None, ''):
        return None
    k = chave(valor)
    if k in APELIDOS and APELIDOS[k] in cadastro:
        novo = APELIDOS[k]
        if novo != str(valor).strip():
            aviso.append(f'{onde}: "{valor}" → "{novo}"')
        return novo
    for nome in cadastro:
        if chave(nome) == k:
            return nome
    aviso.append(f'{onde}: "{valor}" não está no cadastro — mantido como texto '
                 f'livre, não entra no consolidado do bloco 5')
    return valor


def vazio(x):
    return x is None or (isinstance(x, str) and not x.strip())


def formula(x):
    return isinstance(x, str) and x.startswith('=')


def main(antigo):
    with open('mapa-ficha.json', encoding='utf-8') as fp:
        M = json.load(fp)
    EQUIPE, PROJ = M['EQUIPE'], M['PROJETISTAS']
    OC = M['LINHAS_OC']

    velho = openpyxl.load_workbook(antigo)
    novo = openpyxl.load_workbook(NOVO)
    abas = [s for s in velho.sheetnames if s not in FIXAS]

    relatorio, avisos, movidos = [], [], []
    for aba in abas:
        if aba not in novo.sheetnames:
            relatorio.append(f'· {aba!r}: aba não existe na estrutura nova — ignorada')
            continue
        a, b = velho[aba], novo[aba]
        n = 0

        def leva(oc, nc=None, conv=None):
            """Copia uma célula digitada à mão do antigo para o novo."""
            nonlocal n
            v = a[oc].value
            if vazio(v) or formula(v):
                return
            if conv:
                v = conv(v)
            if v is None:
                return
            b[nc or oc] = v
            n += 1

        # ── identificação ──
        for col in 'ADFHJ':
            leva(f'{col}{V0["R_ID2"]}')
        leva(f'A{V0["R_ID4"]}')
        leva(f'D{V0["R_ID4"]}')
        leva(f'F{V0["R_ID4"]}', conv=lambda v: normaliza(
            v, EQUIPE, f'{aba} · coordenador', avisos))

        # ── 1 · valor de venda ──
        leva(f'C{V0["R_VENDA"]}')
        leva(f'D{V0["R_VENDA"]}')
        # o valor de venda digitado em cima do KPI A13 vai para o campo certo
        kpi = a[f'A{V0["R_KPI_V"]}'].value
        if not vazio(kpi) and not formula(kpi) and vazio(b[f'D{V0["R_VENDA"]}'].value):
            b[f'D{V0["R_VENDA"]}'] = kpi
            n += 1
            movidos.append(f'{aba}: valor de venda estava digitado no KPI A13 '
                           f'(célula de fórmula) → levado para D{V0["R_VENDA"]}, '
                           f'o campo "Realizado" do bloco 1')

        # ── 2 · custos de venda: % e valores em reais ──
        for r in range(V0['R_IMP'], V0['R_RTP'] + 1):
            for col in 'BCD':
                leva(f'{col}{r}')

        # ── 3 · ambientes ──
        for r in range(V0['R_AMB0'], V0['R_AMBF'] + 1):
            leva(f'A{r}')
            leva(f'C{r}')
            leva(f'D{r}', conv=lambda v, r=r: normaliza(
                v, EQUIPE, f'{aba} · produção D{r}', avisos))
            leva(f'E{r}')
            leva(f'G{r}', conv=lambda v, r=r: normaliza(
                v, EQUIPE, f'{aba} · montagem G{r}', avisos))
            leva(f'H{r}')

        # ── 4 · percentuais das comissões ──
        for r in (V0['R_COORD'], V0['R_PRODC'], V0['R_MONTC']):
            leva(f'B{r}')

        # ── 6 · orçado por categoria, na linha nova de cada uma ──
        for cat, r_velho in CATS_V0.items():
            rot = a[f'A{r_velho}'].value
            if rot not in (None, cat):
                avisos.append(f'{aba}: a categoria da linha {r_velho} tinha sido '
                              f'renomeada para "{rot}" — o rótulo voltou a "{cat}", '
                              f'senão o SUMIFS não acha os lançamentos')
            leva(f'C{r_velho}', f'C{OC[cat]}')
            # realizado digitado à mão: vira lançamento no livro do bloco 8
            real = a[f'D{r_velho}'].value
            if not vazio(real) and not formula(real) and real:
                movidos.append((aba, cat, real))

        # ── 7 · retrabalho e contingência ──
        for i, r in enumerate(range(V0['R_RB0'], V0['R_RBF'] + 1)):
            for col in 'ABEG':
                leva(f'{col}{r}', f'{col}{M["R_RB0"] + i}')
        leva(f'C{V0["R_RB_SUB"]}', f'C{M["R_RB_SUB"]}')

        # ── 8 · livro de compras ──
        usadas = 0
        for i, r in enumerate(range(V0['R_LAN0'], V0['R_LANF'] + 1)):
            destino = M['R_LAN0'] + i
            algo = False
            for col in 'ABDEGI':
                v = a[f'{col}{r}'].value
                if not vazio(v) and not formula(v):
                    b[f'{col}{destino}'] = v
                    n += 1
                    algo = True
            if algo:
                usadas = i + 1
        relatorio.append(f'· {aba!r}: {n} células · {usadas} lançamentos no livro')
        b._ultima_lanc = usadas

    # ── os realizados digitados à mão entram no livro, como lançamento ──
    extras = []
    for item in [m for m in movidos if isinstance(m, tuple)]:
        aba, cat, valor = item
        b = novo[aba]
        linha = M['R_LAN0'] + getattr(b, '_ultima_lanc', 0)
        if linha > M['R_LANF']:
            extras.append(f'{aba}: não sobrou linha no livro para {cat} '
                          f'R$ {valor:,.2f} — lance à mão')
            continue
        b[f'A{linha}'] = f'{cat.lower()} — lançado à mão na ficha antiga, conferir'
        b[f'B{linha}'] = cat
        b[f'E{linha}'] = valor
        b[f'I{linha}'] = 'Pago'
        b._ultima_lanc = getattr(b, '_ultima_lanc', 0) + 1
        extras.append(f'{aba}: {cat} R$ {valor:,.2f} estava digitado em cima da '
                      f'fórmula do realizado → virou lançamento na linha {linha} '
                      f'do livro, com status Pago')

    novo.save(NOVO)

    print('═' * 76)
    print('MIGRAÇÃO · preenchimentos trazidos para a estrutura nova')
    print('═' * 76)
    for l in relatorio:
        print(l)
    if avisos:
        print('\nNOMES E RÓTULOS AJUSTADOS')
        for l in dict.fromkeys(avisos):
            print(f'  · {l}')
    if extras:
        print('\nVALORES QUE MUDARAM DE LUGAR')
        for l in [m for m in movidos if isinstance(m, str)] + extras:
            print(f'  · {l}')
    print(f'\nOK → {NOVO}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
