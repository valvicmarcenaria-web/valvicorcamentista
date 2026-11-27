# -*- coding: utf-8 -*-
"""Emite, por aba: (1) o TSV só com DADOS e (2) os blocos de peça,
para replicar H:J com copyPaste. Metade do payload."""
import json, sys, os
_d=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_d); sys.path.insert(0,os.path.join(_d,'..'))
import aba as A

NAO_PECA = {'', 'CHAVE', 'logística', 'embalagem'}

def emitir():
    g = A.gera()
    out = {}
    for nome, rows in g.items():
        linhas, blocos, ini = [], [], None
        for i, r in enumerate(rows, 1):
            r = list(r) + [''] * (11 - len(r))
            k = str(r[10])
            peca = k not in NAO_PECA
            if peca:
                if ini is None: ini = i
                r[7] = r[8] = r[9] = ''      # H, I, J vão por copyPaste
            else:
                if ini is not None:
                    blocos.append((ini, i - 1)); ini = None
            linhas.append('\t'.join('' if c is None else str(c) for c in r))
        if ini is not None: blocos.append((ini, len(rows)))
        out[nome] = {'tsv': '\n'.join(linhas), 'blocos': blocos, 'n': len(rows)}
    return out

if __name__ == '__main__':
    o = emitir()
    json.dump(o, open('emitido.json','w',encoding='utf-8'), ensure_ascii=False)
    for k in sorted(o):
        print('%-26s %3d linhas %3d blocos %6d bytes' % (k, o[k]['n'], len(o[k]['blocos']), len(o[k]['tsv'])))
