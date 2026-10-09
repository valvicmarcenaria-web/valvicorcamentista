# -*- coding: utf-8 -*-
GRUPOS = [
 ("11/10/2026", [
   ("Maria e Valdenir", "Vale dos Cristais", "Fabricação do móvel de carrinhos", 270.00),
   ("Luiz", "", "Comissão do projeto", 90.00),
   ("Walton", "", "Comissão do projeto", 70.00),
   ("Gisele", "Adega · Retiro do Chalé", "Comissão do projeto", 160.00),
   ("Regina", "", "Ida à obra", 90.00),
   ("Dias extras", "", "3 dias extras", 750.00),
 ]),
 ("15/10/2026", [
   ("Maria e Valdenir", "Vale dos Cristais", "Montagem completa na obra", 1800.00),
 ]),
 ("18/10/2026", [
   ("Cristiane", "", "Comissão do projeto", 1500.00),
   ("Samuel", "", "Ajuda na obra", 300.00),
 ]),
]
def brl(v):
    return ('R$ %s' % ('{:,.2f}'.format(v).replace(',','#').replace('.',',').replace('#','.')))
TOTAL = sum(v for _, it in GRUPOS for *_, v in it)
NITENS = sum(len(it) for _, it in GRUPOS)

linhas = []
for data, itens in GRUPOS:
    sub = sum(v for *_, v in itens)
    linhas.append('  <div class="venc"><span class="dt">Vencimento %s</span>'
                  '<span class="sb">%s · %d %s</span></div>' %
                  (data, brl(sub), len(itens), 'item' if len(itens)==1 else 'itens'))
    linhas.append('  <table class="tb">')
    linhas.append('    <tr><th style="width:24px">✓</th><th style="width:150px">Projeto</th>'
                  '<th>Referente a</th><th style="width:96px" class="num">Valor</th></tr>')
    for proj, loc, ref, v in itens:
        p = '<b>%s</b>%s' % (proj, ('<span class="loc">%s</span>' % loc) if loc else '')
        linhas.append('    <tr><td><span class="cx"></span></td><td>%s</td>'
                      '<td>%s</td><td class="num">%s</td></tr>' % (p, ref, brl(v)))
    linhas.append('    <tr class="sub"><td></td><td colspan="2">Subtotal do vencimento</td>'
                  '<td class="num">%s</td></tr>' % brl(sub))
    linhas.append('  </table>')

HTML = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Comissões em aberto — César</title>
__FONTES__
<style>
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:13mm 14mm 12mm; display:flex; flex-direction:column; overflow:hidden }
@media print{ body{ background:#fff } .sheet{ margin:0 } }

.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:6px; margin-bottom:10px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:26px; font-weight:700; color:var(--navy); line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:8px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-top:3px }
.doc{ text-align:right }
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:19px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:8.5px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.ident{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin-bottom:8px }
.ident .c{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:2px; padding:5px 9px }
.ident .r{ font-size:7px; font-weight:700; letter-spacing:.8px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:11px; font-weight:700; color:var(--navy); margin-top:1px }

.destaque{ display:flex; justify-content:space-between; align-items:center; background:var(--navy);
  border-radius:3px; padding:11px 16px; margin-bottom:4px }
.destaque .r{ font-size:9px; font-weight:700; letter-spacing:1.8px; text-transform:uppercase; color:var(--goldsoft) }
.destaque .r small{ display:block; font-weight:400; letter-spacing:.3px; text-transform:none;
  color:rgba(255,255,255,.55); font-size:8.5px; margin-top:2px }
.destaque .v{ font-family:'Cormorant Garamond',serif; font-size:30px; font-weight:700; color:#fff }

.venc{ display:flex; justify-content:space-between; align-items:center; background:var(--goldbg);
  border-left:3px solid var(--gold); border-radius:2px 2px 0 0; padding:5px 10px; margin-top:10px }
.venc .dt{ font-size:9.5px; font-weight:700; letter-spacing:1.6px; text-transform:uppercase; color:var(--navy) }
.venc .sb{ font-size:9.5px; font-weight:700; color:var(--navy2) }

table.tb{ width:100%; border-collapse:collapse; font-size:9.5px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:7.5px; font-weight:600;
  letter-spacing:.8px; text-transform:uppercase; padding:4px 8px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:6px 8px; vertical-align:middle }
table.tb tr:nth-child(even) td{ background:#f8fafb }
table.tb tr.sub td{ background:#fff; border-bottom:none; border-top:1.5px solid var(--navy);
  font-weight:700; color:var(--navy); font-size:9px }
.num{ text-align:right; font-variant-numeric:tabular-nums }
.cx{ display:inline-block; width:11px; height:11px; border:1.4px solid var(--navy); border-radius:2px; vertical-align:-1px }
.loc{ display:block; font-size:8px; color:var(--muted); font-weight:400 }

.nota{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:2px;
  padding:8px 11px; font-size:9px; line-height:1.55; color:#33414F; margin-top:12px }
.nota b{ color:var(--navy) }

.assina{ display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-top:16px }
.assina div{ border-top:1px solid var(--ink); padding-top:4px; text-align:center }
.assina .n{ font-size:9px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:8px; color:var(--muted) }

.rodape{ margin-top:auto; border-top:1px solid var(--linha); padding-top:5px;
  display:flex; justify-content:space-between; font-size:7.5px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
</style>
</head>
<body>

<div class="sheet">
  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc">
      <h1>Comissões em Aberto</h1>
      <div class="m">Prestação de serviços · posição em 09/10/2026</div>
    </div>
  </div>

  <div class="ident">
    <div class="c"><div class="r">Prestador</div><div class="v">César</div></div>
    <div class="c"><div class="r">Modalidade</div><div class="v">PJ</div></div>
    <div class="c"><div class="r">Itens em aberto</div><div class="v">__NITENS__</div></div>
    <div class="c"><div class="r">Vencimentos</div><div class="v">__NVENC__</div></div>
  </div>

  <div class="destaque">
    <div class="r">Total em aberto<small>Contratante: Vargas Decor Ltda — Valvic Marcenaria</small></div>
    <div class="v">__TOTAL__</div>
  </div>

__LINHAS__

  <div class="nota"><b>Como ler esta folha.</b> Os itens estão agrupados pela data em que vencem — é
  nessa data que cada bloco é pago, e não item a item. A coluna de marcar serve para a conferência
  conjunta: cada linha conferida, um visto. Qualquer divergência, aponte antes do primeiro vencimento.</div>

  <div class="assina">
    <div><div class="n">César</div><div class="s">Conferido em ___/___/______</div></div>
    <div><div class="n">Valvic Marcenaria — Vargas Decor Ltda</div><div class="s">Jonathan / Paulo</div></div>
  </div>

  <div class="rodape">
    <span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Comissões em aberto · César · 09/10/2026</span>
  </div>
</div>

</body>
</html>'''
HTML = (HTML.replace('__LINHAS__', '\n'.join(linhas))
            .replace('__TOTAL__', brl(TOTAL))
            .replace('__NITENS__', str(NITENS))
            .replace('__NVENC__', str(len(GRUPOS))))
print(HTML)
