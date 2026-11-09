# -*- coding: utf-8 -*-
"""Folder — informações obrigatórias no pedido de compra.

    python3 painel/gerar-checklist-pedido-compra.py > painel/checklist-pedido-compra.html
"""
import importlib.util, os
_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-checklist-pedido-compra.py')
_s = importlib.util.spec_from_file_location('dados_checklist_pedido_compra', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
OBRIGATORIAS, EXEMPLOS = _m.OBRIGATORIAS, _m.EXEMPLOS
FAMILIAS, CONFERIR, ERROS = _m.FAMILIAS, _m.CONFERIR, _m.ERROS

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea;
  --red:#B0413F; --ok:#2F7D4F; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:11mm 12mm 10mm; display:flex; flex-direction:column;
  page-break-after:always; overflow:hidden }
.sheet:last-child{ page-break-after:auto }
@media print{ body{ background:#fff } .sheet{ margin:0 } }

.capa{ background:var(--navy); color:#fff; margin:-11mm -12mm 9px; padding:13mm 12mm 10mm }
.marca{ font-family:'Cormorant Garamond',serif; font-size:26px; font-weight:700;
  color:#fff; letter-spacing:.5px; line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7.5px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--goldsoft); margin-top:3px }
.capa h1{ font-family:'Cormorant Garamond',serif; font-size:33px; font-weight:600;
  margin:14px 0 0; line-height:1.08; color:#fff }
.capa h1 b{ color:var(--goldsoft); font-weight:600 }
.capa .sub{ font-size:9.5px; line-height:1.55; color:#c7d2e0; margin-top:8px; max-width:150mm }
.capa .sub b{ color:var(--goldsoft) }

.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:9px }
.topo .marca{ color:var(--navy) }
.topo .marca small{ color:var(--gold) }
.doc{ text-align:right }
.doc h2{ margin:0; font-family:'Cormorant Garamond',serif; font-size:18px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:8px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.faixa{ background:var(--navy); color:var(--goldsoft); font-size:8.5px; font-weight:600;
  letter-spacing:2px; text-transform:uppercase; padding:5px 10px; margin:9px 0 6px; border-radius:2px }
.faixa.g{ background:var(--gold); color:#2a2112 }

.obrig{ display:grid; grid-template-columns:1fr 1fr; gap:6px 9px }
.ob{ border:1px solid var(--linha); border-top:2px solid var(--gold); border-radius:2px;
  padding:6px 9px; display:flex; gap:8px; align-items:flex-start }
.ob .n{ font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:700;
  color:var(--gold); line-height:1; flex:0 0 auto; margin-top:1px }
.ob .t{ font-size:10px; font-weight:700; color:var(--navy); display:block; margin-bottom:2px }
.ob .d{ font-size:8.3px; line-height:1.45; color:#45525f }
.ob .d b{ color:var(--navy) }

.cab{ display:grid; grid-template-columns:1fr 1fr; gap:0 10px }
.cx2{ display:flex; gap:6px; align-items:flex-start; font-size:8.7px; line-height:1.4;
  padding:3.5px 0; border-bottom:1px solid var(--linha); color:#39465a }
.cx2 span.b{ display:inline-block; width:10px; height:10px; border:1.3px solid var(--navy);
  border-radius:2px; flex:0 0 auto; margin-top:1px }

table.tb{ width:100%; border-collapse:collapse; font-size:8.6px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:6.5px; font-weight:600;
  letter-spacing:.9px; text-transform:uppercase; padding:4px 7px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:5.5px 7px; vertical-align:top }
table.tb tr:nth-child(odd) td{ background:#f7f9fb }
.fam{ font-weight:700; color:var(--navy) }
.camp{ font-size:8.4px; line-height:1.5; color:#45525f }
.camp b{ color:var(--navy) }
.cx{ display:inline-block; width:11px; height:11px; border:1.4px solid var(--navy); border-radius:2px }

.bloco{ border:1px solid var(--linha); border-left:3px solid var(--navy2); border-radius:2px;
  padding:7px 10px; font-size:8.6px; line-height:1.5; color:#39465a }
.bloco b{ color:var(--navy) }
.aviso{ background:var(--goldbg); border-left:3px solid var(--gold); border-radius:2px;
  padding:7px 10px; font-size:8.8px; line-height:1.5; color:var(--navy2); margin-bottom:8px }
.aviso b{ color:var(--navy) }

.ex{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:2px;
  padding:6px 10px; margin-bottom:5px; display:flex; gap:10px; align-items:baseline }
.ex .k{ flex:0 0 76px; font-size:8px; font-weight:700; letter-spacing:1.1px;
  text-transform:uppercase; color:var(--gold) }
.ex .v{ font-family:'JetBrains Mono',monospace; font-size:8.3px; line-height:1.55; color:#39465a }
.ex .v b{ color:var(--navy); font-weight:700 }

.erros{ display:grid; grid-template-columns:1fr 1fr; gap:6px }
.er{ border:1px solid #f0dcda; border-left:3px solid var(--red); background:#fdf6f5;
  border-radius:2px; padding:6px 9px }
.er .t{ font-size:9px; font-weight:700; color:var(--red); display:block; margin-bottom:2px }
.er .d{ font-size:8.2px; line-height:1.45; color:#5c4a49 }

.rodape{ margin-top:auto; border-top:1px solid var(--linha); padding-top:5px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

obrig_html = '\n'.join(
  f'    <div class="ob"><span class="n">{n}</span><span>'
  f'<span class="t">{t}</span><span class="d">{d}</span></span></div>'
  for n, t, d in OBRIGATORIAS)

def duas(itens):
    meio = (len(itens) + 1) // 2
    col = lambda ns: '<div>' + ''.join(
      f'<div class="cx2"><span class="b"></span><span>{i}</span></div>' for i in ns) + '</div>'
    return col(itens[:meio]) + col(itens[meio:])

ex_html = '\n'.join(
  f'    <div class="ex"><span class="k">{k}</span><span class="v">{v}</span></div>'
  for k, v in EXEMPLOS)

fam_html = '\n'.join(
  f'    <tr><td style="width:24px"><span class="cx"></span></td>'
  f'<td style="width:148px" class="fam">{f}</td>'
  f'<td class="camp">{c}</td></tr>'
  for f, c in FAMILIAS)

err_html = '\n'.join(
  f'    <div class="er"><span class="t">{t}</span><span class="d">{d}</span></div>'
  for t, d in ERROS)

RODAPE = ('  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>'
          '<span>Pedido de compra · informações obrigatórias</span></div>\n</div>')

print('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pedido de compra — informações obrigatórias</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
  <div class="capa">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <h1>Um item mal escrito<br>vira <b>retrabalho na obra</b>.</h1>
    <div class="sub">Este folder é o padrão da casa para pedido de compra. Todo item pedido a qualquer
    fornecedor precisa das <b>oito informações abaixo</b>, sem exceção.
    <b>Pedido com item incompleto não é enviado</b> — volta para quem pediu.</div>
  </div>

  <div class="faixa g">1 · As oito que todo item precisa ter</div>
  <div class="obrig">
__OBRIGATORIAS__
  </div>

  <div class="faixa">2 · Como fica na prática</div>
__EXEMPLOS__

  <div class="aviso" style="margin-top:9px"><b>A regra que resolve a maioria dos casos.</b>
  Escreva o item de forma que <b>outra pessoa consiga comprar sem te perguntar nada</b>. Se o vendedor
  precisar interpretar, o pedido está incompleto — e quem paga a interpretação errada é a produção,
  três semanas depois, com a chapa já cortada.</div>
__RODAPE__

</body>
</html>'''
  .replace('__CSS__', CSS)
  .replace('__OBRIGATORIAS__', obrig_html)
  .replace('__EXEMPLOS__', ex_html)
  .replace('__RODAPE__', RODAPE))
