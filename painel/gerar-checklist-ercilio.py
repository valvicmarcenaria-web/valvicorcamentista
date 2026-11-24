# -*- coding: utf-8 -*-
"""Checklist de finalização — obra Ercílio. Uma folha A4 para levar na obra.

Editar os dados em dados-checklist-ercilio.py; o layout é aqui.

    python3 painel/gerar-checklist-ercilio.py > painel/checklist-ercilio.html
"""
import importlib.util, os

_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-checklist-ercilio.py')
_s = importlib.util.spec_from_file_location('dados_ercilio', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)

NITENS = sum(len(a[1]) for a in _m.AMBIENTES)

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea; --red:#B0413F; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:11mm 12mm 9mm; display:flex; flex-direction:column;
  page-break-after:always; overflow:hidden }
.sheet:last-child{ page-break-after:auto }
@media print{ body{ background:#fff } .sheet{ margin:0; box-shadow:none } }

.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:8px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:24px; font-weight:700;
  color:var(--navy); letter-spacing:.5px; line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-top:3px }
.doc{ text-align:right }
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:19px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:7.5px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.ident{ display:grid; grid-template-columns:1.6fr 1fr 1fr 1.2fr; gap:5px; margin-bottom:8px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold);
  border-radius:2px; padding:4px 7px }
.ident .r{ font-size:6.5px; letter-spacing:1.2px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:10px; font-weight:700; color:var(--navy); margin-top:2px }
.ident .v.b{ font-weight:400; color:#c3cad3; letter-spacing:1px }

.nota{ background:var(--goldbg); border-left:3px solid var(--gold); padding:4px 9px;
  font-size:8.3px; line-height:1.45; color:var(--navy2); margin-bottom:8px }

.cab{ background:var(--navy); color:#fff; border-radius:2px 2px 0 0; padding:4px 9px;
  display:flex; justify-content:space-between; align-items:center; margin-top:7px }
.cab .n{ font-size:8.5px; font-weight:700; letter-spacing:1.7px; text-transform:uppercase; color:var(--goldsoft) }
.cab .q{ font-size:7px; color:#b9c3cf; letter-spacing:.5px }

table.tb{ width:100%; border-collapse:collapse; font-size:9px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:6.5px; font-weight:600;
  letter-spacing:.8px; text-transform:uppercase; padding:4px 7px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:4px 7px; vertical-align:middle }
tr.amb td{ background:#eef2f6 !important; padding:3px 7px }
tr.amb .a{ font-size:7.5px; font-weight:700; letter-spacing:1.6px; text-transform:uppercase; color:var(--navy) }
tr.amb .c{ font-size:7px; color:var(--muted) }
table.tb tr.it:nth-child(even) td{ background:#fafbfc }
.cx{ display:inline-block; width:12px; height:12px; border:1.4px solid var(--navy); border-radius:2px }
.it b{ font-weight:600; color:var(--navy) }
.esp{ font-size:7.5px; color:var(--muted); display:block; margin-top:1px }
.pt i{ display:block; border-bottom:1px dotted #b6bfc9; height:11px }
.nu{ font-family:'JetBrains Mono',monospace; font-size:8px; color:var(--muted) }

table.mt{ width:100%; border-collapse:collapse; font-size:8.5px }
table.mt th{ background:var(--navy2); color:var(--goldsoft); font-size:6.5px; font-weight:600;
  letter-spacing:.8px; text-transform:uppercase; padding:4px 7px; text-align:left }
table.mt td{ border-bottom:1px solid var(--linha); padding:3.5px 7px; vertical-align:middle }
table.mt tr:nth-child(even) td{ background:#fafbfc }
.mt .m{ font-weight:600; color:var(--navy) }
.mt .p{ color:var(--muted); font-size:7.5px }

.fim{ margin-top:auto; padding-top:9px; display:grid; grid-template-columns:1fr 1fr; gap:22px }
.fim > div{ border-top:1px solid var(--ink); padding-top:4px; text-align:center }
.fim .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.fim .s{ font-size:7px; color:var(--muted) }
.rodape{ margin-top:9px; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:6.5px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

linhas, n = [], 0
for amb, itens in _m.AMBIENTES:
    linhas.append(f'<tr class="amb"><td colspan="4"><span class="a">{amb}</span> '
                  f'<span class="c">&nbsp;·&nbsp; {len(itens)} '
                  f'{"item" if len(itens)==1 else "itens"}</span></td></tr>')
    for it, esp in itens:
        n += 1
        e = f'<span class="esp">{esp}</span>' if esp else ''
        linhas.append(f'<tr class="it"><td style="width:24px"><span class="cx"></span></td>'
                      f'<td style="width:20px" class="nu">{n:02d}</td>'
                      f'<td><b>{it}</b>{e}</td>'
                      f'<td style="width:128px" class="pt"><i></i></td></tr>')
ITENS = '\n'.join(linhas)

MAT = '\n'.join(
    f'<tr><td style="width:24px"><span class="cx"></span></td>'
    f'<td class="m">{m}</td><td class="p">{p}</td></tr>' for m, p in _m.MATERIAL)

NOVAS = '\n'.join(
    '<tr class="it"><td style="width:24px"><span class="cx"></span></td>'
    '<td class="pt" colspan="2"><i></i></td>'
    '<td style="width:128px" class="pt"><i></i></td></tr>'
    for _ in range(_m.LINHAS_NOVAS))

HTML = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Checklist de finalização — obra Ercílio</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Checklist de Finalização — Obra __CLIENTE__</h1>
      <div class="m">Para levar na obra · preencher na obra, não depois · emitido em __EMISSAO__</div></div>
  </div>

  <div class="ident">
    <div class="c"><div class="r">Responsável na obra</div><div class="v b">__________________</div></div>
    <div class="c"><div class="r">Data</div><div class="v b">___/___/______</div></div>
    <div class="c"><div class="r">Chegada / saída</div><div class="v b">__:__ · __:__</div></div>
    <div class="c"><div class="r">Itens previstos</div><div class="v">__NITENS__ em 5 ambientes</div></div>
  </div>

  <div class="nota">__NOTA__</div>

  <div class="cab"><span class="n">1 · Demandas por ambiente</span>
    <span class="q">marcar ao concluir · anotar o que travou</span></div>
  <table class="tb">
    <tr><th style="width:24px">✓</th><th style="width:20px">#</th><th>O que fazer</th>
      <th style="width:128px">Observação na obra</th></tr>
__ITENS__
  </table>

  <div class="cab"><span class="n">2 · Material a levar</span>
    <span class="q">conferir antes de sair da fábrica</span></div>
  <table class="mt">
    <tr><th style="width:24px">✓</th><th style="width:210px">Material</th><th>Para quê</th></tr>
__MAT__
  </table>

  <div class="cab"><span class="n">3 · Pendências novas encontradas na obra</span>
    <span class="q">tudo o que aparecer entra aqui</span></div>
  <table class="tb">
    <tr><th style="width:24px">✓</th><th colspan="2">O que falta ou está errado</th>
      <th style="width:128px">Ambiente</th></tr>
__NOVAS__
  </table>

  <div class="fim">
    <div><div class="n">Responsável na obra</div><div class="s">Checklist conferido item a item</div></div>
    <div><div class="n">Deivison Gonçalves</div><div class="s">Gestor de produção · recebido em ___/___/______</div></div>
  </div>

  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Checklist de finalização · obra __CLIENTE__ · __EMISSAO__</span></div>
</div>

</body>
</html>'''

print(HTML
  .replace('__CSS__', CSS)
  .replace('__ITENS__', ITENS).replace('__NITENS__', str(NITENS))
  .replace('__MAT__', MAT).replace('__NOVAS__', NOVAS)
  .replace('__NOTA__', _m.NOTA_ORDEM)
  .replace('__CLIENTE__', _m.CLIENTE).replace('__EMISSAO__', _m.EMISSAO))
