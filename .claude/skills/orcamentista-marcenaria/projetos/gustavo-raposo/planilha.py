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
import sys, json, re, importlib.util, pathlib, io, contextlib
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P))
import base as B

# ⛔ o nome do móvel traz a referência da prancha na frente, e nos itens
#    unificados ela é uma FAIXA — "DET 01 a 06", "DET 01 e 02". Um split por
#    espaço cortava no lugar errado e a aba saía com o móvel chamado
#    "a 06 Conjunto da lavanderia".
SO_DET = re.compile(r'^(?:DET|ELEVAÇÃO)\s+\d+(?:\s*(?:a|e|,|\+|/)\s*\d+)*\s+')

NOME = sys.argv[1] if len(sys.argv) > 1 else 'cozinha'
sp = importlib.util.spec_from_file_location('AMB', P/f'{NOME}.py')
A = importlib.util.module_from_spec(sp); sys.modules['AMB'] = A
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(A)
PECAS = getattr(A, NOME.upper().replace('-', '_'))
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
    # ⭐ CORREDIÇA TOUCH [Jonathan, 28/10/2026]: "no caso de corrediças com
    #   abertura por toque, considere a corrediça touch, não precisa de
    #   pulsador". O quinto elemento da tupla diz qual é; sem ele, vale a
    #   corrediça comum, que era o único caso até aqui.
    for gv in g('GAVETAS'):
        mv, rot, q, mm = gv[:4]
        touch = len(gv) > 4 and gv[4] == 'touch'
        if mv == mov:
            out.append(['Corrediça touch' if touch else B.CH_CORREDICA,
                        f'{rot} · {mm} mm' + (' · ⛔ abre por toque: NÃO leva '
                        'pulsador, a própria corrediça abre' if touch else ''),
                        '', '', q, 'par',
                        'Corrediça touch' if touch else B.CH_CORREDICA])
    for mv, rot, nq, nd, pr in g('PORTAS'):
        if mv == mov:
            ch = B.CH_DOBRADICA if pr == B.DOBRADICA else B.CH_DOBR_VIDRO
            out.append([ch, f'{rot} · {nd} por folha', '', '', nq*nd, 'un', ch])
    # ⭐⭐ A BÁSCULA NEM SEMPRE ABRE PELO SLIM. Na Cozinha abre: o Jonathan
    #   fechou HK-XS mais slim Rometal. Na Lavanderia a prancha põe o
    #   Alças Traso em TODA frente, básculas inclusive — e aí o puxador
    #   sai na linha de PUXADORES, não aqui. O quarto elemento da tupla diz
    #   qual é; sem ele, vale o slim, que era o único caso até aqui.
    for b in g('BASCULAS'):
        mv, rot, q = b[:3]
        pux = b[3] if len(b) > 3 else 'slim'
        if mv == mov:
            out.append(['Báscula HK-XS', rot + ' · articulador de molas Blum',
                        '', '', q, 'un', 'Báscula HK-XS'])
            if pux == 'slim':
                out.append(['Puxador slim', 'Rometal · uma por báscula · ⛔ sem '
                            'pulsador Blum: não se somam na mesma frente', '',
                            '', q, 'un', 'Puxador slim'])
    for mv, rot, q in g('PUXADORES'):
        if mv == mov: out.append([B.CH_PUXADOR_128, rot +
                                  ' · Zen Design, 128 mm', '', '', q, 'un',
                                  B.CH_PUXADOR_128])
    for mv, rot, q in g('MOLDURA'):
        if mv == mov: out.append(['Moldura provençal', rot + ' · usinagem do '
                                  'relevo na router, peça inteira de 6 mm · '
                                  '⛔ A COTAR, cronometrar uma na fábrica',
                                  '', '', q, 'frente', 'Moldura provençal'])
    # ⭐ VIDRO E ESPELHO são a mesma vidraçaria e moram na mesma linha
    #   [Jonathan, 28/10/2026 — "considere o espelho" em cinco ambientes].
    #   O sexto elemento da tupla diz a chave; sem ele, vale o reflecta.
    for vd in g('VIDRO'):
        mv, rot, q, c, l = vd[:5]
        ch = vd[5] if len(vd) > 5 else 'Vidro reflecta'
        if mv == mov:
            # ⛔⛔ O AVISO DE "A COTAR" SÓ SAI SE FALTAR PREÇO [30/10/2026].
            #   Ele saía em TODA linha de vidro, inclusive nas que TÊM preço:
            #   o espelho prata colado custa R$ 600/m² e a aba do Lavabo
            #   dizia "segue sem preço na Base" embaixo dele. ⭐ Aviso que
            #   grita onde não há nada errado é aviso que o leitor aprende a
            #   não ler — e este é o único aviso que a planilha tem para
            #   dizer que o total é PISO, não preço fechado.
            cotar = '' if B.PRECO.get(ch) else (' · ⛔ A COTAR, segue sem '
                                                'preço na Base')
            out.append([{'Vidro reflecta': 'Vidro reflecta champagne',
                         'Espelho': 'Espelho'}.get(ch, ch), rot + cotar,
                        c, l, q, 'm²', ch])
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
    # ⭐⭐ ALMA DE PRATELEIRA, CONTADA DAS PEÇAS [Jonathan, 28/10/2026]:
    #   "prateleiras acima de 1.20mt vamos considerar alma de aço". Como o
    #   suporte, é regra da casa — logo é do motor, não da lista.
    _na = B.almas_de_prateleira(PECAS, mov)
    if _na:
        out.append(['Alma de aço', f'{_na} prateleira(s) de vão acima de '
                    f'{B.ALMA_VAO:g} cm · ⛔ contra FLECHA, não contra '
                    'empeno: 18 mm resolve o empeno e não resolve o vão',
                    '', '', _na, 'barra', 'Alma de aço'])
    # ⭐⭐ SUPORTE DE PRATELEIRA, CONTADO DAS PEÇAS [Jonathan, 28/10/2026].
    #   Não há lista de SUPORTES para preencher: toda prateleira interna
    #   de armário leva um jogo de 4 suportes, R$ 6,50, e a conta sai de
    #   `B.prateleiras()`. Quem não leva diz "sem suporte" na obs.
    _np = B.prateleiras(PECAS, mov)
    if _np:
        out.append(['Suporte de prateleira',
                    f'{_np} prateleira(s) interna(s) · composição de 4 '
                    'suportes por prateleira · ⛔ não é suporte oculto',
                    '', '', _np, 'jogo', 'Suporte de prateleira'])
    # ⭐⭐ OUTRAS: a ferragem de uma vez só. Cada ambiente traz um item que
    #   a Base tem e o gerador não — passante no Quarto, corrediça de carga
    #   na bicama, pistão de tampo no baú. Criar uma constante e três
    #   blocos para cada um é como a lista de chapas era antes de sair das
    #   peças: digitada, e por isso esquecível. Aqui a linha vem pronta do
    #   ambiente, com a chave da Base, e o resto do motor não muda.
    for mv, nome, rot, q, un, ch in g('OUTRAS'):
        if mv == mov: out.append([nome, rot, '', '', q, un, ch])
    for mv, rot, q in g('CABIDEIROS'):
        if mv == mov: out.append(['Cabideiro', rot + ' · metal preto ou '
                                  'grafite', '', '', q, 'un', 'Cabideiro'])
    # ⛔⛔ O SARRAFO DE PINUS SAIU: a casa não usa pinus para nada
    #   [Jonathan, 28/10/2026]. Onde ele segurava, entra engradado de MDF
    #   (peça, conta na chapa), estrado em metalon (cama) ou serralheria.
    # ⭐⭐ SERRALHERIA COM VALOR FECHADO, E ELE ENTRA NA CONTA. Até aqui a
    #   linha buscava um preço na Base que nunca existiu, e os R$ 2.500 do
    #   banco do Living saíam ZERO na aba sem ninguém reclamar. Agora o
    #   valor vem do ambiente e vai direto para a coluna de R$ unitário.
    for mv, rot, v_ in g('SERRALHERIA'):
        if mv == mov: out.append(['Serralheria estrutural', rot +
                                  ' · valor fechado do serralheiro', '', '',
                                  1, 'conjunto', 'Serralheria estrutural',
                                  float(v_)])
    return out

def montar(inicio):
    val, fml, mapa, r = [], [], {}, inicio
    AREA = 'PROCV("Área da chapa";precos;2;FALSO)'
    APR  = 'PROCV("Aproveitamento";precos;2;FALSO)'
    for i, mov in enumerate(MOV, 1):
        ls = linhas_do_item(mov)
        titulo, cadeia = A.CABECA[mov]
        val.append([f'ITEM {i:02d}', SO_DET.sub('', mov), '', '', '', '', '',
                    titulo])
        val.append(['', cadeia])
        val.append(['MATERIAL', 'ESPECIFICAÇÃO', 'C', 'L', 'QTD', 'UN',
                    'R$ UN', 'CUSTO', '', 'chave na Base'])
        r0 = r + 3
        for j, linha in enumerate(ls):
            nm, esp, c, l, q, un, ch = linha[:7]
            fixo = linha[7] if len(linha) > 7 else None
            lr = r0 + j
            val.append([nm, esp, c, l, q, un, '', '', '', ch])
            # ⭐ R$ unitário: ou vem da Base, pela chave, ou vem fechado do
            #   ambiente (serralheria). O custo é sempre quantidade × R$ un.
            # ⛔⛔ DOIS SENTIDOS DE "m²", E A ABA CONFUNDIA OS DOIS.
            #   Peça de MDF em m² se paga por CHAPA: a área entra dividida
            #   pela área útil da chapa. Palhinha, espelho, vidro e
            #   estofado se pagam POR m²: a área entra inteira. Enquanto o
            #   discriminador era a unidade, os dois caíam na mesma conta e
            #   a palhinha da cabeceira da Suíte Hóspedes somava ZERO —
            #   R$ 2.645,50 de furo numa linha que estava escrita certa.
            #   O discriminador honesto é a CHAVE: só "MDF ..." é chapa.
            fml.append((lr, fixo if fixo is not None else
                        f'=SEERRO(PROCV($K{lr};precos;2;FALSO);"")',
                        f'=SEERRO(SE(ESQUERDA($K{lr};4)="MDF ";'
                        f'$D{lr}*$E{lr}/10000*$F{lr}/({AREA}*{APR})*$H{lr};'
                        f'SE($D{lr}="";$F{lr}*$H{lr};'
                        f'$D{lr}*$E{lr}/10000*$F{lr}*$H{lr}));"")'))
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
    # ⛔⛔ `if h` ERA UMA ARMADILHA: zero é FALSO em Python. A linha de
    #   serralheria sem preço — valor fechado que o senhor ainda não deu —
    #   tem h = 0.0 e caía FORA da faixa de material. Resultado: o
    #   copyPaste não alcançava a linha, a coluna de custo ficava vazia e a
    #   peça desaparecia do total do item sem erro na tela. A pergunta certa
    #   é "esta linha tem R$ unitário?", não "o R$ unitário é diferente de
    #   zero?" — e só as linhas de TOTAL têm h = None.
    mats = sorted(r for r, h, i in fml if h is not None)
    faixas, a, ant = [], mats[0], mats[0]
    for x in mats[1:]:
        if x != ant+1: faixas.append((a, ant)); a = x
        ant = x
    faixas.append((a, ant))
    print(f'✓ {len(val)} linhas · blocos de {INI} a {fim-2}')
    for i, mov in enumerate(MOV, 1):
        print(f'   ITEM {i:02d} {SO_DET.sub("", mov)[:40]:42} total na linha {mapa[i]}')
    print(f'  faixas de material: {faixas}')
    print(f'  totais: {sorted(mapa.values())}')
    print(f'  padrões de chapa: {sorted({p["chave"] for p in PECAS if p["chave"].startswith("MDF")})}')
    json.dump({'val': val, 'fml': fml, 'mapa': mapa, 'fim': fim,
               'faixas': faixas}, open(P/f'_{NOME}-rows.json', 'w'),
              ensure_ascii=False)
