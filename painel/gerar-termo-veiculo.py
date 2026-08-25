#!/usr/bin/env python3
"""Preenche o Termo de Responsabilidade pelo Uso de Veículo para uma pessoa.

Lê `controle-veiculos-termo.html` (a versão em branco, que continua sendo a
fonte única) e devolve um HTML com os campos preenchidos. Assim o texto do
termo nunca é duplicado: mudou a cláusula, muda para todo mundo.

Uso:  python3 gerar-termo-veiculo.py samuel
      python3 gerar-termo-veiculo.py            (lista quem está cadastrado)

Campos que ficam em branco de propósito aparecem como linha pontilhada, para
serem preenchidos à caneta antes da assinatura.
"""
import html
import re
import sys
import unicodedata

BRANCO = 'controle-veiculos-termo.html'

# Placas na ordem em que aparecem no quadro da frota.
FROTA = ['TEN0J18', 'TCR0D79', 'QUY4166']
QUALIFICACOES = ['CLT', 'PRESTADOR', 'PARCEIRO']

# ── quem já está cadastrado ────────────────────────────────────────────────
# Dados conferidos contra a CNH enviada. Deixe '' no que ainda não se sabe;
# o campo sai como linha em branco no documento impresso.
PESSOAS = {
    'samuel': {
        'arquivo': 'Samuel',
        'Nome completo': 'Samuel de Jesus Lourenço',
        'CPF': '146.866.466-26',
        'CNH nº': '07431102717',
        'Categoria': 'AB',
        'Validade': '30/05/2032',
        'Telefone': '(31) 99583-2140',
        'qualificacao': 'PRESTADOR',   # 'CLT' | 'PRESTADOR' | 'PARCEIRO' | None
        'veiculos': FROTA,             # placas autorizadas; [] = marcar à caneta
    },
    'cesar': {
        'arquivo': 'Cesar',
        # o nome sai como está na CNH — no chão de fábrica ele é chamado de Cezar
        'Nome completo': 'Cesar Eduardo Campos Santos',
        'CPF': '043.245.596-51',
        'CNH nº': '01406676021',
        'Categoria': 'AB',
        'Validade': '17/10/2034',
        'Telefone': '(31) 98669-2802',
        'qualificacao': 'CLT',
        'veiculos': FROTA,
    },
    'jackson': {
        'arquivo': 'Jackson',
        'Nome completo': 'Jackson Martins Duarte Neto',
        'CPF': '066.606.486-58',
        'CNH nº': '07562372642',
        'Categoria': 'AB',            # com observação EAR na CNH
        'Validade': '04/08/2032',
        'Telefone': '(31) 99234-4977',
        'qualificacao': 'PRESTADOR',
        'veiculos': FROTA,
    },
    'deivison': {
        'arquivo': 'Deivison',
        # a CNH grafa DEIVISON — no chão de fábrica ele é chamado de Deivson
        'Nome completo': 'Deivison Gonçalves Santos',
        'CPF': '086.137.146-17',
        'CNH nº': '04064719490',
        'Categoria': 'AB',
        'Validade': '17/05/2032',
        'Telefone': '(31) 99424-3857',
        'qualificacao': 'PRESTADOR',
        'veiculos': FROTA,
    },
    'fillipe': {
        'arquivo': 'Fillipe',
        # a CNH grafa FILLIPE, com dois L
        'Nome completo': 'Fillipe Flausino de Moura Freire',
        'CPF': '084.433.616-54',
        'CNH nº': '05274275129',
        'Categoria': 'B',             # só automóvel; cobre os três carros da frota
        'Validade': '13/03/2035',
        # número informado com 8 dígitos; se for celular falta o 9 inicial
        'Telefone': '(31) 9410-0286',
        'qualificacao': 'PRESTADOR',
        'veiculos': FROTA,
    },
}


def sem_acento(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()


def preencher_campo(doc, rotulo, valor):
    """Troca a linha pontilhada do campo `rotulo` pelo valor."""
    alvo = html.escape(rotulo)
    padrao = re.compile(
        r'(<div class="k">' + re.escape(alvo) + r'</div>\s*)<div class="v"></div>')
    if not padrao.search(doc):
        raise SystemExit(f'campo não encontrado no termo: {rotulo!r}')
    if not valor:
        return doc                       # deixa a linha em branco
    return padrao.sub(
        lambda m: m.group(1) + f'<div class="v preenchido">{html.escape(valor)}</div>',
        doc, count=1)


def marcar_caixas(trecho, indices):
    """Devolve o trecho com as N-ésimas caixas marcadas."""
    n = [-1]
    def troca(m):
        n[0] += 1
        return '<span class="cx on">✓</span>' if n[0] in indices else m.group(0)
    return re.sub(r'<span class="cx"></span>', troca, trecho)


def gerar(chave):
    p = PESSOAS[chave]
    doc = open(BRANCO, encoding='utf-8').read()

    # estilos dos campos preenchidos e das caixas marcadas
    doc = doc.replace(
        '.grid .v{height:5.8mm;border-bottom:.25mm dotted #b9c2cc;margin-top:1mm}',
        '.grid .v{height:5.8mm;border-bottom:.25mm dotted #b9c2cc;margin-top:1mm}\n'
        '.grid .v.preenchido{font-size:9.6pt;font-weight:600;color:var(--navy);\n'
        '                    line-height:5.8mm;border-bottom-style:solid;\n'
        '                    border-bottom-color:var(--navy2)}\n'
        '.cx.on{background:var(--navy);color:#fff;font-size:6.4pt;font-weight:700;\n'
        '       text-align:center;line-height:3.4mm}', 1)

    for rotulo in ('Nome completo', 'CPF', 'CNH nº', 'Categoria', 'Validade', 'Telefone'):
        doc = preencher_campo(doc, rotulo, p[rotulo])

    # caixas de qualificação
    ini = doc.index('<div class="qual">')
    fim = doc.index('</div>', doc.index('</span>', doc.index('class="nota"', ini)))
    idx = [QUALIFICACOES.index(p['qualificacao'])] if p['qualificacao'] else []
    doc = doc[:ini] + marcar_caixas(doc[ini:fim], idx) + doc[fim:]

    # caixas da frota
    ini = doc.index('<table class="frota">')
    fim = doc.index('</table>', ini)
    idx = [FROTA.index(v) for v in p['veiculos']]
    doc = doc[:ini] + marcar_caixas(doc[ini:fim], idx) + doc[fim:]

    doc = doc.replace('<title>Valvic · Termo de Responsabilidade pelo Uso de Veículo</title>',
                      f'<title>Valvic · Termo de Veículo — {p["arquivo"]}</title>', 1)

    saida = f'controle-veiculos-termo-{sem_acento(chave)}.html'
    open(saida, 'w', encoding='utf-8').write(doc)

    pendentes = [r for r in ('Telefone',) if not p[r]]
    if not p['qualificacao']:
        pendentes.append('qualificação')
    if not p['veiculos']:
        pendentes.append('veículos autorizados')
    return saida, pendentes


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('pessoas cadastradas:', ', '.join(sorted(PESSOAS)))
        raise SystemExit(0)
    chave = sys.argv[1].lower()
    if chave not in PESSOAS:
        raise SystemExit(f'{chave!r} não está em PESSOAS. Cadastre no topo do script.')
    saida, pendentes = gerar(chave)
    print('OK →', saida)
    print('   a preencher à caneta:', ', '.join(pendentes) if pendentes else 'nada')
