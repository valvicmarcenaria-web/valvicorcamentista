# -*- coding: utf-8 -*-
import sys, os
_d = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _d); sys.path.insert(0, os.path.join(_d, '..'))
import motor_mc as M
from itens import fechar, MDF

MC = 0.40
KW = dict()                       # à vista, com RT e vendedor
BASE = M.base(**KW)
def pv(cd): return cd/(BASE-MC)
def brl(v, n=0): return f'{v:,.{n}f}'.replace(',','§').replace('.',',').replace('§','.')

r = fechar(); W = 118
print('═'*W)
print('ESTIMATIVA ITEM A ITEM — RESIDÊNCIA HENRIQUE E KARELEN')
print('ferragem Blum · MC %.0f%% · base %.2f%% (à vista, com RT e vendedor)' % (MC*100, BASE*100))
print('⚠ ORDEM DE GRANDEZA — 10 dos 15 ambientes · profundidades assumidas · MDF no piso do Fosco')
print('═'*W)
TOT = 0.0
for amb in sorted(r):
    d = r[amb]
    ch = '  '.join('%d chapas de %d mm' % (n, e) for e, n in sorted(d['chapas'].items()))
    print()
    print('%s' % amb.upper())
    print('   %s' % ch)
    print('   ' + '-'*(W-3))
    print('   %-52s%12s%10s%10s%10s%12s' % ('ITEM  ·  medida','material','ferragem','terceiro','CUSTO','PREÇO'))
    for L in d['itens']:
        it = L['it']
        mat = L['ch']+L['fita']+L['cons']+L['corte']
        nm = it.nome if len(it.nome) <= 34 else it.nome[:33]+'…'
        rot = '%-35s %s' % (nm, it.medida)
        print('   %-52s%12s%10s%10s%10s%12s' % (rot[:52], brl(mat), brl(L['fer']),
              brl(L['ter']), brl(L['cd']), brl(pv(L['cd']))))
    print('   %-52s%12s%10s%10s%10s%12s' % ('TOTAL DO AMBIENTE','','','',
          brl(d['cd']), brl(pv(d['cd']))))
    TOT += d['cd']
print()
print('═'*W)
print('   %-52s%42s%12s' % ('TOTAL — 10 AMBIENTES, 41 ITENS', brl(TOT), brl(pv(TOT))))
print('═'*W)
