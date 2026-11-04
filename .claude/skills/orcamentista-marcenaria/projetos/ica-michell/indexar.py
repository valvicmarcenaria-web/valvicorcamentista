# -*- coding: utf-8 -*-
"""Mapa página → ambiente → detalhamento, lido dos PDFs em disco.

⭐⭐ POR QUE ISTO EXISTE, e é o achado que destrava os 16 ambientes que
  faltam. Para orçar eu preciso da prancha, e as 235 páginas moram no
  Drive. Havia dois caminhos e os dois pareciam fechados:

    download_file_content  devolve base64 → 873 KB por página, e 183
                           páginas seriam ~156 MB pelo contexto. ⛔
    read_file_content      devolve TEXTO → ~400 tokens por página, ótimo,
                           mas o texto PERDE A POSIÇÃO da cota. E sem
                           posição eu leio o 65 da cristaleira como
                           largura quando é profundidade. ⛔

  ⭐⭐ O que resolve: resultado grande do MCP é SALVO EM DISCO e NÃO entra
    no contexto — custa só o aviso. Então o download é barato, o PDF fica
    em disco, e aí a geometria sai local, de graça, com pymupdf.

    baixar  ~1,4 k tokens por página de aviso
    ler     0  · roda local
    183 páginas ≈ 256 k tokens  ·  contra 156 MB  ⭐

  ⭐ E a geometria não é luxo: na página 82 o texto solta "594", que é o
    LITRO DO FREEZER, não uma cota. Pela posição ele cai fora sozinho.

   uso:  python3 colher.py      # decodifica o que foi baixado
         python3 indexar.py     # mapa do que há em disco
"""
import json, pathlib, pymupdf, re, sys
SP = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                  '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/ica/pgs')
P = pathlib.Path(__file__).resolve().parent
AMB = ('LIVING|COZINHA|LAVANDERIA|QUARTO|LAVABO|ÁREA GOURMET|BANHO GOURMET|'
       'HOME OFFICE|SUÍTE HÓSPEDES|BANHO HÓSPEDES|SALA DE CINEMA|SUÍTE MASTER|'
       'CLOSET MASTER|BANHO MASTER|SUÍTE MARIANA|CLOSET MARIANA|BANHO MARIANA|'
       'SUÍTE 03|CLOSET 03|BANHO 03')

def ler(f):
    n = int(f.stem[1:]); t = pymupdf.open(f)[0].get_text()
    a = (re.search(rf'\b({AMB})\b', t) or [None, '?'])[1]
    det = re.findall(r'DET\.?\s*0?(\d{1,2})\s*[-–]\s*'
                     r'([A-ZÁÂÃÉÊÍÓÔÕÚÇ][^\n.]{2,36})', t)
    tipo = ('DETALHAMENTO' if det else 'planta' if 'PLANTA' in t
            else 'elevação' if 'ELEVAÇÃO' in t else 'capa')
    return n, a, tipo, ','.join(sorted({d[0] for d in det})), \
           (det[0][1].strip().title() if det else '')

if __name__ == '__main__':
    linhas = sorted(ler(f) for f in SP.glob('p*.pdf'))
    json.dump(linhas, open(P/'_idx.json', 'w'), ensure_ascii=False)
    todas = {int(k) for k in json.load(open(P/'paginas.json'))}
    tem = {l[0] for l in linhas}
    amb = {}
    for n, a, tipo, nd, nome in linhas: amb.setdefault(a, []).append(n)
    W = 74; print('═'*W)
    print(f'PRANCHAS DO ICA · {len(tem)} de {len(todas)} páginas em disco')
    print('═'*W)
    for a, pgs in amb.items():
        d = [l for l in linhas if l[1] == a and l[2] == 'DETALHAMENTO']
        print(f'  {a:16} p{min(pgs):03d}–p{max(pgs):03d}  {len(pgs):2} pág  '
              f'{len(d)} detalhamentos')
    f = sorted(todas - tem)
    print(f'\n⚠ faltam {len(f)} páginas. Para baixar, pegue o ID em '
          f'paginas.json e chame\n  download_file_content — o resultado vai '
          f'para disco e colher.py decodifica.')
