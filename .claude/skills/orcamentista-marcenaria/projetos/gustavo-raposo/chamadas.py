# -*- coding: utf-8 -*-
"""Despeja as CHAMADAS de uma prancha, limpas do carimbo e das cotas soltas.

⭐ A chamada diz o MATERIAL e a REGRA ("interno em MDF Branco", "gavetas com
  corrediças invisíveis", "puxador tipo cava na marcenaria"). A imagem diz a
  CONTA — quantas folhas, quantas gavetas. São duas leituras diferentes, e
  esta é a barata: faço esta primeiro e só abro a imagem para contar.

   uso:  python3 -I chamadas.py 39 40 41
"""
import re, sys, pathlib, pymupdf
PR = pathlib.Path(__file__).resolve().parent/'pr'
LIXO = re.compile(r'Luiza Pacheco|CAU|luizapacheco|direitos autorais|'
                  r'medidas devem ser|Cotas em cent|d[úu]vidas ou necess|'
                  r'CLIENTE|ENDERE|E;?ECUTIVO|Revis[ãa]o|Formato|'
                  r'escrit[óo]rio de arquitetura|\(31\)|Mar[çc]o, 2026', re.I)
for n in (int(a) for a in sys.argv[1:]):
    arq = next(PR.glob(f'{n:02d}-*.pdf'))
    pg = pymupdf.open(arq)[0]
    print(f"\n{'═'*74}\nPRANCHA {n} · {arq.stem[3:]}")
    # ⭐ junta por BLOCO: a chamada quebra em várias linhas no PDF, e lida
    #   linha a linha ela vira picado sem sentido.
    for b in pg.get_text('blocks'):
        s = ' '.join(x.strip() for x in b[4].split('\n') if x.strip())
        if not s or LIXO.search(s): continue
        if re.fullmatch(r'[\d,.\s×x/Øø–-]+', s): continue
        print(f'   {s}')
