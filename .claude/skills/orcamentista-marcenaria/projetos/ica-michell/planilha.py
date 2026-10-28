# -*- coding: utf-8 -*-
"""Gera a aba de um ambiente a partir do seu levantamento.

⭐ A planilha NÃO é digitada: sai do mesmo arquivo que faz a conta. Quando
  os dois divergem é bug — e já divergiram duas vezes.

⭐⭐ IDENTIDADE N.GESTAO [Jonathan, 28/10]: "copie a identidade visual das
  planilhas de gestao que fizemos". O que a leitura da N.GESTAO 1 mostrou:
    · coluna A vazia e estreita, de margem — o conteúdo começa em B
    · linha 1 "  VALVIC MARCENARIA        <ABA>", numa célula só
    · linha 2 em frase corrida, com " · " separando as ideias
    · seções em caixa alta, recuadas por dois espaços, com "   ·   " e um
      subtítulo que explica a REGRA, não o conteúdo
    · gridlines desligadas · sem campo de imagem
    · tabela com cabeçalho e linha de Total no fim

⛔ locale pt_BR: separador de argumento é ';'.

   uso:  python3 planilha.py cozinha
"""
import sys, json, importlib.util, pathlib, io, contextlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P))
import base as B

NOME = sys.argv[1] if len(sys.argv) > 1 else 'cozinha'
sp = importlib.util.spec_from_file_location('AMB', P/f'{NOME}.py')
A = importlib.util.module_from_spec(sp); sys.modules['AMB'] = A
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(A)
PECAS = getattr(A, NOME.upper())
g = lambda n: getattr(A, n, [])
MOV = list(dict.fromkeys(p['movel'] for p in PECAS))

def linhas_do_item(mov):
    """Materiais, fita e ferragem de um móvel, na ordem da aba."""
    out = []
    for p in PECAS:
        if p['movel'] != mov: continue
        out.append([p['nome'], p['obs'] or '—', p['c'], p['l'], p['qtd'],
                    'm²', p['chave']])
    # ⭐ fita e filetagem, cada uma na sua linha e no seu preço, na ORDEM
    #   DO PROCESSO — primeiro se fita, depois se fileta. Alfabética punha
    #   a filetagem antes, e a aba ficava diferente do arquivo.
    _a = B.acabamento(PECAS, mov)
    for ch in [k for k in ('Fita cor', 'Fita Branco TX',
                           'Filetagem automática', 'Filetagem manual')
               if k in _a]:
        m = _a[ch]
        out.append([ch, {'Fita cor': 'Aresta a aresta, mais 10% de desperdício',
                         'Fita Branco TX': 'Caixaria · R$ 2,00 contra R$ 3,00 '
                                           'da fita de cor · mais 10%',
                         'Filetagem automática': 'Coladeira · 15 e 18 mm · '
                                                 'serviço, sem desperdício',
                         'Filetagem manual': '⛔ Ripa e 6 mm não entram na '
                                             'coladeira · R$ 5,00, o dobro'}[ch],
                    '', '', m, 'm', ch])
    for mv, rot, q, mm in g('GAVETAS'):
        if mv == mov: out.append(['Corrediça', f'{rot} · {mm} mm', '', '', q,
                                  'par', 'Corrediça'])
    for mv, rot, nq, nd, pr in g('PORTAS'):
        if mv == mov:
            ch = 'Dobradiça' if pr == B.DOBRADICA else 'Dobradiça vidro'
            out.append([ch, f'{rot} · {nd} por folha', '', '', nq*nd, 'un', ch])
    for mv, rot, q in g('BASCULAS'):
        if mv == mov:
            out.append(['Báscula HK-XS', rot + ' · articulador a gás Blum',
                        '', '', q, 'un', 'Báscula HK-XS'])
            # ⭐ slim no lugar do pulsador [Jonathan, 28/10/2026]
            out.append(['Puxador slim', 'Rometal · uma por báscula · ⛔ sem '
                        'pulsador Blum: não se somam na mesma frente', '', '',
                        q, 'un', 'Puxador slim'])
    for mv, rot, q in g('PUXADORES'):
        if mv == mov: out.append(['Puxador Alças Traso 128', rot +
                                  ' · Zen Design, 128 mm', '', '', q, 'un',
                                  'Puxador Alças Traso 128'])
    for mv, rot, q in g('MOLDURA'):
        if mv == mov: out.append(['Moldura provençal', rot + ' · mão de obra '
                                  'de travessa e almofada · ⛔ A COTAR, '
                                  'cronometrar uma na fábrica', '', '', q,
                                  'frente', 'Moldura provençal'])
    for mv, rot, q, c, l in g('VIDRO'):
        if mv == mov: out.append(['Vidro reflecta champagne', rot + ' · ⛔ A '
                                  'COTAR, segue sem preço na Base', c, l, q,
                                  'm²', 'Vidro reflecta'])
    for mv, rot, q, c in g('CAVA'):
        if mv == mov: out.append(['Cava usinada', rot, '', '',
                                  round(q*c/100, 2), 'm', 'Cava usinada'])
    for mv, rot, m in g('LED'):
        if mv == mov: out.append(['LED, conjunto completo', rot + ' · fita, '
                                  'perfil, usinagem e instalação', '', '', m,
                                  'm', 'LED conjunto'])
    for mv, rot, q in g('ALMAS'):
        if mv == mov: out.append(['Alma de aço', rot + ' · contra empeno', '',
                                  '', q, 'barra', 'Alma de aço'])
    for mv, rot, q in g('SUPORTES'):
        if mv == mov: out.append(['Suporte oculto', rot + ' · de 40 em 40 cm',
                                  '', '', q, 'un', 'Suporte oculto'])
    # ⭐ serralheria estrutural: valor fechado por móvel, não por metro
    for mv, rot, v_ in g('SERRALHERIA'):
        if mv == mov: out.append(['Serralheria estrutural', rot + ' · ⛔ não é '
                                  'o rodapé de 3 cm, que vai em MDF: aqui o '
                                  'móvel é SUSPENSO e quem o segura é a '
                                  'estrutura', '', '', 1, 'conjunto',
                                  'Serralheria estrutural'])
    return out

def montar(inicio):
    val, fml, mapa, r = [], [], {}, inicio
    AREA = 'PROCV("Área da chapa";precos;2;FALSO)'
    APR  = 'PROCV("Aproveitamento";precos;2;FALSO)'
    for i, mov in enumerate(MOV, 1):
        ls = linhas_do_item(mov)
        titulo, cadeia = A.CABECA[mov]
        val.append([f'ITEM {i:02d}', mov.split(' ', 2)[-1], '', '', '', '', '',
                    titulo])
        val.append(['', cadeia])
        val.append(['MATERIAL', 'ESPECIFICAÇÃO', 'C', 'L', 'QTD', 'UN',
                    'R$ UN', 'CUSTO', '', 'chave na Base'])
        r0 = r + 3
        for j, (nm, esp, c, l, q, un, ch) in enumerate(ls):
            lr = r0 + j
            val.append([nm, esp, c, l, q, un, '', '', '', ch])
            fml.append((lr, f'=SEERRO(PROCV($K{lr};precos;2;FALSO);"")',
                        f'=SEERRO(SE($G{lr}="m²";$D{lr}*$E{lr}/10000*$F{lr}'
                        f'/({AREA}*{APR})*$H{lr};$F{lr}*$H{lr});"")'))
        rt = r0 + len(ls)
        val.append([f'TOTAL DO ITEM {i:02d}', '', '', '', '', '', '', ''])
        fml.append((rt, None, f'=SOMA(I{r0}:I{rt-1})'))
        mapa[i] = rt
        val.append([''])
        r = rt + 2
    return val, fml, mapa, r

if __name__ == '__main__':
    INI = int(sys.argv[2]) if len(sys.argv) > 2 else 37
    val, fml, mapa, fim = montar(INI)
    mats = sorted(r for r, h, i in fml if h)
    faixas, a, ant = [], mats[0], mats[0]
    for x in mats[1:]:
        if x != ant+1: faixas.append((a, ant)); a = x
        ant = x
    faixas.append((a, ant))
    print(f'✓ {len(val)} linhas · blocos de {INI} a {fim-2}')
    for i, mov in enumerate(MOV, 1):
        print(f'   ITEM {i:02d} {mov.split(" ",2)[-1][:40]:42} total na linha {mapa[i]}')
    print(f'  faixas de material: {faixas}')
    print(f'  totais: {sorted(mapa.values())}')
    print(f'  padrões de chapa: {sorted({p["chave"] for p in PECAS if p["chave"].startswith("MDF")})}')
    json.dump({'val': val, 'fml': fml, 'mapa': mapa, 'fim': fim,
               'faixas': faixas}, open(P/f'_{NOME}-rows.json', 'w'),
              ensure_ascii=False)
