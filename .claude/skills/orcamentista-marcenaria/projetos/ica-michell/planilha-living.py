# -*- coding: utf-8 -*-
"""Gera as linhas da aba "01 Living" a partir de living.py.

⭐ A planilha NÃO é digitada: ela sai do mesmo arquivo que faz a conta. Se
  o levantamento mudar, a aba muda junto — e nunca divergem.

⛔ locale pt_BR: separador de argumento é ';'. Pega IF/IFERROR/PROCV/SE.
"""
import json, importlib.util, pathlib, sys
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('L', P/'living.py')
L = importlib.util.module_from_spec(spec); sys.modules['L'] = L
spec.loader.exec_module(L)

CHAVE = {18: 'MDF cor 18', 15: 'MDF cor 15', 6: 'MDF cor 6'}
INICIO = 61                      # primeira linha de bloco

# ── cada item: rótulo curto, medida geral e a cadeia que fecha ──────────
ITENS = [
 (L.D1, 'Sapateira com painel',      '142 × 300 × 42',
  'Altura 178 do painel + 105 da sapateira + 17 da base = 300 · frentes 2 + 34 + 34 + 34 + 2 = 105'),
 (L.D2, 'Aparador com gaveta',       '185 × 55 × 50',
  'Largura 8 + 34 + 8 + 135 = 185 · altura 5 + 45 + 5 = 55 · vista superior 50 + 135 = 185'),
 (L.D3, 'Prateleira iluminada',      '135 × 45 · duplada',
  'Largura 50 + 135 = 185 na elevação · ⭐ 5 cm de espessura = duas peças'),
 (L.D4, 'Divisória em colunas',      f'11 colunas · 70 × 200 mm · {L.ALT_MAX:g} de altura',
  'Cadeia 11 × 7 + 10 × 10 = 177 ⭐ · vertical 300 + 20 = 320 — os 20 cm são a peça de 200 mm · ⛔ sem fita de borda'),
 (L.D5, 'Jardineira com banco',      '520 × 113 × 50',
  'VISTA SUPERIOR 10 + 500 + 10 = 520, profundidade 113 em 44 + 25 + 44 · VISTA FRONTAL altura 30 + 10 + 10 = 50 · ⚠ a lateral traz 10 + 80 + 103 = 193, que não fecha com os 113'),
 (L.D6, 'Divisória com cristaleira', '460 × 300 × 65',
  'Largura 100 + 260 + 100 = 460 · VISTA SUPERIOR fecha a profundidade em 16 + 2 + 15 + 16 + 16 = 65 · ⛔ o 65 é PROFUNDIDADE, não largura: não há peça de 65 de largura'),
 (L.D7, 'Estante',                   '255 × 300 × 40',
  'Largura 5+75+5+60+5+60+5+40 = 255 · altura 5+48+5+48+5+48+5+48+5+43+35+5 = 300'),
 (L.D8, 'Painel com porta mimetizada', '400 × 300',
  'Largura 260 + 80 + 60 = 400 · altura 90 + 210 = 300 · 400 × 273 = 220 de painel cheio + 180 × 63 de travessa + duas portas de 90 × 210'),
]

def linhas_do_item(mov):
    """Materiais, fita e ferragem de um móvel, na ordem da aba."""
    out = []
    for p in L.LIVING:
        if p['movel'] != mov: continue
        out.append([p['nome'], p['obs'] or 'Nogueira Caiena',
                    p['c'], p['l'], p['qtd'], 'm²', CHAVE[p['esp']]])
    # ⭐ A FITA — declarada aresta a aresta nas peças deste móvel
    m = sum((nc*p['c'] + nl*p['l'])*p['qtd']/100
            for p in L.LIVING if p['movel'] == mov
            for nc, nl in [p['fita']])
    if m > 0:
        out.append(['Fita de borda', 'Filetamento declarado aresta a aresta '
                    '· + 10% de desperdício', '', '',
                    round(m*(1+L.FITA_PERD), 1), 'm', 'Fita'])
    for mv, rot, q, mm in L.GAVETAS:
        if mv == mov: out.append(['Corrediça', f'{rot} · {mm} mm', '', '',
                                  q, 'par', 'Corrediça'])
    for mv, rot, nq, nd, pr in L.PORTAS:
        if mv == mov:
            ch = 'Dobradiça' if pr == L.DOBRADICA else 'Dobradiça vidro'
            out.append([ch, f'{rot} · {nd} por folha', '', '',
                        nq*nd, 'un', ch])
    for mv, rot, q, c, l in L.VIDRO:
        if mv == mov: out.append(['Vidro reflecta champagne', rot + ' · ⛔ A COTAR '
                                  'com o vidraceiro, segue sem preço na Base',
                                  c, l, q, 'm²', 'Vidro reflecta'])
    for mv, rot, q, c in L.CAVA:
        if mv == mov: out.append(['Cava usinada', rot, '', '',
                                  round(q*c/100, 2), 'm', 'Cava usinada'])
    for mv, rot, mt in L.LED:
        if mv == mov: out.append(['LED, conjunto completo', rot + ' · fita, perfil, '
                                  'usinagem e instalação', '', '',
                                  mt, 'm', 'LED conjunto'])
    for mv, rot, q in L.ALMAS:
        if mv == mov: out.append(['Alma de aço', rot + ' · contra empeno', '', '',
                                  q, 'barra', 'Alma de aço'])
    for mv, rot, q in L.SUPORTES:
        if mv == mov: out.append(['Suporte oculto', rot + ' · de 40 em 40 cm', '', '',
                                  q, 'un', 'Suporte oculto'])
    return out

def montar():
    """Devolve (valores, formulas, mapa) prontos para a API."""
    val, fml, mapa, r = [], [], {}, INICIO
    AREA = 'PROCV("Área da chapa";precos;2;FALSO)'
    APR  = 'PROCV("Aproveitamento";precos;2;FALSO)'
    for i, (mov, nome, medida, cadeia) in enumerate(ITENS, 1):
        ls = linhas_do_item(mov)
        val.append([f'ITEM {i:02d}', nome, '', '', '', '', '', medida])
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
    val, fml, mapa, fim = montar()
    print(f'✓ {len(val)} linhas · blocos de {INICIO} a {fim-2}')
    print(f'  {len(fml)} células de fórmula')
    for i, (mov, nome, *_ ) in enumerate(ITENS, 1):
        print(f'   ITEM {i:02d} {nome:30} total na linha {mapa[i]}')
    json.dump({'val': val, 'fml': fml, 'mapa': mapa, 'fim': fim},
              open(P/'_living-rows.json', 'w'), ensure_ascii=False)
