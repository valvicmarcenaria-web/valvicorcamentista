# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — a ponte entre o nome do levantamento e a CHAVE da Base.

⛔⛔ ESTE ARQUIVO EXISTE POR CAUSA DE UM BUG DE R$ 520.
  `startswith('Dobradiça')` pegava 'Dobradiça de porta de vidro' junto, e as
  26 dobradiças de vidro caíram de R$ 70 para R$ 50 sem um aviso. Casamento
  por prefixo pega demais, e pega CALADO.

⭐ A DEFESA NÃO É LER COM MAIS ATENÇÃO: é a trava `confere()`, que exige que
  o preço da chave escolhida seja IGUAL ao preço que o levantamento lançou.
  Se a regra pegar a peça errada, os dois preços divergem e o arquivo não
  carrega. Atenção falha; aritmética não.

⛔ E A OUTRA TRAVA: toda chave aqui tem de EXISTIR na `Base (importada)`.
  Chave que a Base não tem → PROCV não acha → SEERRO devolve "" → a linha
  custa ZERO. É a divergência que não dá erro, e ela mora aqui.
"""
import importlib.util, sys, pathlib, contextlib, io

P = pathlib.Path(__file__).resolve().parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, P / arq)
    m = importlib.util.module_from_spec(s); sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m


b = _mod('b', 'base.py')
lv = _mod('lv', 'levantamento.py')

# ════════════════════════════════════════════════════════════════════════
# 1 · O CATÁLOGO: toda chave que este orçamento usa, com o preço do motor
# ════════════════════════════════════════════════════════════════════════
#   ⭐ A coluna `imp` diz se a `Base (importada)` JÁ tem o preço em B:
#       True  → vem da Base por fórmula, e o motor não precisa dizer nada
#       False → a célula B está vazia porque o IMPORTRANGE está bloqueado,
#               e o valor do motor entra como SOCORRO DECLARADO na coluna G
MOTOR = {
    # chave                            valor        un          imp
    'Área da chapa':                   (b.CHAPA_M2,  'm²',       True),
    'Aproveitamento':                  (b.APROV,     '',         True),
    'Consumíveis':                     (b.CONSUMIVEIS, '',       True),
    'Embalagem':                       (b.EMBALAGEM, '',         True),
    'Desperdício de fita':             (b.FITA_PERDA, '',        None),
    'MDF cor 18':                      (700.0,       'chapa',    False),
    'MDF cor 15':                      (550.0,       'chapa',    False),
    'MDF cor 6':                       (350.0,       'chapa',    False),
    'Fita cor':                        (b.FITA_COR,  'm',        True),
    'Filetagem automática':            (b.FILETE_MAQ, 'm',       True),
    'Filetagem manual':                (b.FILETE_MAO, 'm',       True),
    #   ⭐ [Jonathan, 04/11/2026] a ripa vai à coladeira, e ganha CHAVE
    #     PRÓPRIA em vez de cair dentro da 'Filetagem automática'. Os
    #     2.595,5 m de ripa são 91% da fita do projeto: fundir as duas
    #     esconderia o maior metro do orçamento dentro de outra linha.
    'Filetagem de ripa':               (b.FILETE_RIPA, 'm',      True),
    #   ⭐ [Jonathan, 04/11/2026] a porta de passagem é FEITA na casa
    'Miolo G-Door em régua':           (b.GDOOR_M2,  'm²',      True),
    'Perfil de metalon':               (b.METALON_BARRA, 'barra', True),
    'Dobradiça':                       (b.DOBRADICA, 'un',       False),
    'Dobradiça vidro':                 (b.DOBRADICA_VIDRO, 'un', False),
    'Corrediça Hettich':               (b.CORREDICA_PAR, 'par',  False),
    'Corrediça Blum':                  (300.0,       'par',      None),
    'Báscula HK-XS':                   (b.BASCULA_HK, 'un',      False),
    'Desempenador de porta':           (b.DESEMPENADOR, 'un',    False),
    'Sistema de correr Dominus':       (b.SISTEMA_CORRER, 'conjunto', False),
    'Sistema de correr SI Forma':      (900.0,       'conjunto', True),
    'Sistema pivô':                    (b.SISTEMA_PIVO, 'conjunto', True),
    'Alma de aço':                     (b.ALMA_BARRA, 'barra',   False),
    'Suporte de prateleira':           (b.SUPORTE_JOGO, 'jogo',  True),
    'Cava usinada':                    (b.CAVA_M,    'm',        False),
    'Painel ripado':                   (b.RIPADO_M2, 'm²',       True),
    'Vidro reflecta prata com perfil': (b.VIDRO_M2,   'm²',     True),
    'Corte por chapa':                 (b.CORTE_CHAPA, 'chapa',  True),
    'Corte por peça':                  (b.CORTE_PECA, 'peça',    True),
    'Frete':                           (200.0,       'viagem',   True),
}
#   ⭐ `imp=None` são as chaves que eu ACRESCENTEI à Base com valor digitado
#     (as três do projeto, mais o desperdício de fita e a corrediça Blum).
#     Elas não dependem do IMPORTRANGE.

# ⚠⚠ PENDÊNCIAS DE PREÇO, e cada uma é dinheiro em aberto ─────────────────
A_COTAR = {
    'Cava usinada': 'A Base briga consigo mesma: R$ 50/m em Ferragens e '
                    'R$ 25/m em Terceirizados. Uso 50, o conservador. São '
                    '14,1 m — R$ 353 de diferença.',
    'Painel ripado': 'R$ 180/m² numa faixa de 70 a 420, "depende da largura '
                     'da ripa e do vão". A nossa é passo de 3 cm, que é FINO.',
    'Vidro reflecta prata com perfil': 'O executivo pede REFLECTA CRISTAL e '
                                       'esse padrão não existe na Base.',
    'Sistema de correr Dominus':
        '⛔⛔ DUAS DÚVIDAS NA MESMA LINHA. (1) PREÇO: a Base de Custos importa '
        'R$ 800 para o "Dominus Rometal, 2 portas" e o Jonathan cravou R$ 600 '
        'em 03/11/2026 — travado em 600 na linha 49 da aba Base (importada), '
        'com o motivo impresso na própria linha. São 2 sistemas na cozinha e '
        'R$ 408 no projeto. ⚠ A Base tem OUTRO sistema de 2 portas a R$ 600, '
        'o SS-150: é possível que o 600 dele seja esse. (2) QUANTIDADE: o '
        'conjunto é vendido como "2 PORTAS" e eu lancei UM POR FOLHA; se um '
        'kit servir as duas folhas, cai outros R$ 600.',
}

# ════════════════════════════════════════════════════════════════════════
# 2 · AS REGRAS, e a ORDEM É O QUE IMPORTA
# ════════════════════════════════════════════════════════════════════════
#   ⛔ O exato vem ANTES do prefixo, sempre. A primeira regra que casa ganha.
REGRAS = [
    ('=', 'Dobradiça de porta de vidro',    'Dobradiça vidro'),
    ('^', 'Dobradiça',                      'Dobradiça'),
    ('^', 'Corrediça',                      'Corrediça Hettich'),
    ('=', 'Articulador Blum AVENTOS HK-XS', 'Báscula HK-XS'),
    ('=', 'Desempenador de porta',          'Desempenador de porta'),
    ('=', 'Sistema de correr',              'Sistema de correr Dominus'),
    ('=', 'Sistema pivô',                   'Sistema pivô'),
    ('^', 'Alma de aço',                    'Alma de aço'),
    ('=', 'Suporte de prateleira',          'Suporte de prateleira'),
    ('^', 'Cava usinada',                   'Cava usinada'),
    #   ⭐ [Jonathan, 04/11/2026] a ripa vai à coladeira · a linha mudou
    #     de nome junto com o preço, para o rótulo não mentir
    ('^', 'Filetagem de ripa',              'Filetagem de ripa'),
    ('^', 'Miolo G-Door',                   'Miolo G-Door em régua'),
    ('^', 'Perfil de metalon',              'Perfil de metalon'),
    ('^', 'Filetagem manual',               'Filetagem manual'),
    ('^', 'Painel ripado',                  'Painel ripado'),
    ('^', 'Porta de vidro reflecta',        'Vidro reflecta prata com perfil'),
]


def chave(nome):
    """A chave da Base para um nome de lançamento. ⛔ Uma só, ou explode."""
    achados = [k for op, alvo, k in REGRAS
               if (nome == alvo if op == '=' else nome.startswith(alvo))]
    if not achados:
        raise KeyError(f'⛔⛔ SEM CHAVE DA BASE: "{nome}". Uma linha sem chave '
                       f'custa ZERO e a planilha não reclama.')
    return achados[0]


def confere():
    """⭐⭐ A TRAVA: o preço da chave tem de ser o preço lançado, item a item."""
    erros, vistos = [], {}
    for m in lv.M:
        for attr in ('ferr', 'terc', 'vidro'):
            for nome, q, unit in getattr(m, attr):
                k = chave(nome)
                vistos.setdefault(k, set()).add(round(unit, 4))
                esperado = MOTOR[k][0]
                if abs(unit - esperado) > 1e-6:
                    erros.append(f'  ⛔ {m.amb} · "{nome}" lançado a '
                                 f'R$ {unit:,.2f} e a chave "{k}" vale '
                                 f'R$ {esperado:,.2f}')
    for k, us in vistos.items():
        if len(us) > 1:
            erros.append(f'  ⛔ a chave "{k}" foi lançada com DOIS preços: '
                         + ' e '.join(f'R$ {u:,.2f}' for u in sorted(us)))
    if erros:
        raise AssertionError('⛔⛔ A PONTE ESTÁ TORTA:\n' + '\n'.join(erros))
    return vistos


#   ⛔⛔ ONDE A BASE E O JONATHAN DISCORDAM, item por item.
#     Em 04/11/2026 o IMPORTRANGE foi autorizado e eu pude, pela primeira
#     vez, comparar os ONZE preços que nasceram no socorro do motor com o
#     que a Base importa de verdade. DEZ batem ao centavo. Um não.
#     ⭐ E esta tabela existe para que o próximo que abrir o arquivo não
#     precise descobrir isso de novo: o número da Base fica ESCRITO ao lado
#     do nosso, e quem quiser o da Base troca uma célula.
DIVERGE = {
    'Sistema de correr Dominus': (800.0, 'Jonathan, 03/11/2026 · "versão '
                                 'hettich vamos usar Rometal de 600"'),
}

VISTOS = confere()

if __name__ == '__main__':
    print(f'✓ {len(VISTOS)} chaves em uso, todas com preço igual ao lançado')
    for k in sorted(VISTOS):
        v, un, imp = MOTOR[k]
        if k in DIVERGE:
            base, quem = DIVERGE[k]
            marca = (f'  ⛔ a Base importa R$ {base:,.2f} · TRAVADO em '
                     f'{v:,.0f} [{quem.split(" · ")[0]}]')
        else:
            marca = {True: '',
                     False: '  ⭐ nasceu no socorro do motor · hoje conferida '
                            'contra a Base, bate',
                     None: '  ⭐ chave acrescentada por mim'}[imp]
        print(f'  {k:<34} R$ {v:>9,.2f} / {un:<9}{marca}')
    print(f'\n⚠ {len(A_COTAR)} chaves com preço em aberto:')
    for k in A_COTAR: print(f'  · {k}')
