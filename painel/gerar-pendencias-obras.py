# -*- coding: utf-8 -*-
"""Relatório + checklist das pendências de obra — levantamento do Jonathan.

Editar os dados em dados-pendencias-obras.py; o layout é aqui.

    python3 painel/gerar-pendencias-obras.py > painel/pendencias-obras.html
"""
import importlib.util, os
_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-pendencias-obras.py')
_s = importlib.util.spec_from_file_location('dados_pendencias_obras', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
OBRAS, AGENDA = _m.OBRAS, _m.AGENDA

NITENS = sum(len(o[3]) for o in OBRAS)
NDEV   = sum(1 for o in OBRAS for i in o[3] if i[3] == 'dev')
NDATA  = sum(1 for o in OBRAS for i in o[3] if i[0] != '—')

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea;
  --red:#B0413F; --blue:#2F5D8C; --ok:#2F7D4F; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:12mm 13mm 11mm; display:flex; flex-direction:column;
  page-break-after:always; overflow:hidden }
.sheet:last-child{ page-break-after:auto }
@media print{ body{ background:#fff } .sheet{ margin:0 } }

.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:8px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:25px; font-weight:700;
  color:var(--navy); letter-spacing:.5px; line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7.5px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-top:3px }
.doc{ text-align:right }
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:19px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:8px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.kpis{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin-bottom:9px }
.kpi{ background:var(--navy); color:#fff; border-radius:3px; padding:7px 9px }
.kpi .r{ font-size:7px; letter-spacing:1.3px; text-transform:uppercase; color:var(--goldsoft) }
.kpi .v{ font-size:17px; font-weight:700; font-family:'Cormorant Garamond',serif; margin-top:1px }
.kpi .o{ font-size:7px; color:#b9c3cf; margin-top:1px }

.faixa{ background:var(--navy); color:var(--goldsoft); font-size:8.5px; font-weight:600;
  letter-spacing:2px; text-transform:uppercase; padding:5px 10px; margin:0 0 6px; border-radius:2px }

table.ag{ width:100%; border-collapse:collapse; font-size:8.5px; margin-bottom:10px }
table.ag th{ background:var(--navy2); color:var(--goldsoft); font-size:7px; font-weight:600;
  letter-spacing:.9px; text-transform:uppercase; padding:4px 8px; text-align:left }
table.ag td{ border-bottom:1px solid var(--linha); padding:4px 8px; vertical-align:middle }
table.ag tr:nth-child(odd) td{ background:#f7f9fb }
table.ag .dt{ font-weight:700; color:var(--navy); white-space:nowrap; width:66px }
table.ag .ob{ color:var(--navy2); font-weight:600; width:150px }

.obra{ margin-bottom:5px }
.cab{ background:var(--navy); color:#fff; border-radius:2px 2px 0 0; padding:4px 10px;
  display:flex; justify-content:space-between; align-items:center }
.cab .n{ font-size:9.5px; font-weight:700; letter-spacing:1.6px; text-transform:uppercase; color:var(--goldsoft) }
.cab .st{ font-size:7px; letter-spacing:.8px; text-transform:uppercase; background:rgba(255,255,255,.14);
  padding:1.5px 7px; border-radius:9px; color:#fff }
.nota{ background:var(--goldbg); font-size:8.5px; color:var(--navy2); padding:3px 10px; line-height:1.35 }

table.it{ width:100%; border-collapse:collapse; font-size:9px }
table.it th{ background:var(--navy2); color:var(--goldsoft); font-size:6.5px; font-weight:600;
  letter-spacing:.9px; text-transform:uppercase; padding:3px 8px; text-align:left }
table.it td{ border-bottom:1px solid var(--linha); padding:4px 8px; vertical-align:top }
table.it tr:nth-child(odd) td{ background:#f7f9fb }
.cx{ display:inline-block; width:11px; height:11px; border:1.4px solid var(--navy); border-radius:2px }
.dt{ font-weight:700; color:var(--navy); white-space:nowrap; font-size:8.5px }
.dt.sem{ color:var(--muted); font-weight:400 }
.tx{ font-weight:600; color:var(--navy) }
.de{ font-size:8px; color:var(--muted); display:block; margin-top:1px; line-height:1.35 }
.pt i{ display:block; border-bottom:1px dotted #b6bfc9; height:10px }
.tag{ display:inline-block; font-size:6.5px; font-weight:700; letter-spacing:.6px;
  text-transform:uppercase; padding:1px 5px; border-radius:8px; color:#fff; margin-right:5px;
  vertical-align:1px }
.tag.crit{ background:var(--red) } .tag.dev{ background:var(--blue) }
tr.crit td{ background:#fdf3f3 !important }
tr.dev td{ background:#f2f6fb !important }

.leg{ font-size:7.5px; color:var(--muted); margin-top:2px }
.assina{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; margin-top:auto; padding-top:10px }
.assina > div{ border-top:1px solid var(--ink); padding-top:3px; text-align:center }
.assina .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:7.5px; color:var(--muted) }
.rodape{ margin-top:10px; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

def topo(i, t):
    return f'''  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Pendências de Obra — Relatório e Checklist</h1>
      <div class="m">Levantamento do Jonathan · 27/10/2026 · para Paulo e Deivison · folha {i} de {t}</div></div>
  </div>'''

def bloco(nome, st, nota, itens):
    if not itens:
        return f'''  <div class="obra">
    <div class="cab"><span class="n">{nome}</span><span class="st">{st}</span></div>
    <div class="nota">{nota}</div>
  </div>'''
    ls = []
    for data, txt, det, tipo in itens:
        cls = f' class="{tipo}"' if tipo else ''
        tag = {'crit': '<span class="tag crit">Importante</span>',
               'dev': '<span class="tag dev">Devolutiva</span>'}.get(tipo, '')
        dcl = 'dt sem' if data == '—' else 'dt'
        d = '<span class="de">' + det + '</span>' if det else ''
        ls.append(f'<tr{cls}><td style="width:24px"><span class="cx"></span></td>'
                  f'<td style="width:52px" class="{dcl}">{data}</td>'
                  f'<td>{tag}<span class="tx">{txt}</span>{d}</td>'
                  f'<td style="width:118px" class="pt"><i></i></td></tr>')
    return f'''  <div class="obra">
    <div class="cab"><span class="n">{nome}</span><span class="st">{st}</span></div>
    {'<div class="nota">' + nota + '</div>' if nota else ''}
    <table class="it">
      <tr><th style="width:24px">✓</th><th style="width:52px">Data</th><th>O que fazer</th><th style="width:118px">Feito por / quando</th></tr>
{chr(10).join(ls)}
    </table>
  </div>'''

ag = '\n'.join(
  f'      <tr><td class="dt">{d}</td><td class="ob">{o}</td><td>{t}</td></tr>'
  for d, o, t in AGENDA)

FECHO = """
  <div class="faixa">O que o Jonathan precisa de volta</div>
  <table class="it">
    <tr><th style="width:24px">&#10003;</th><th style="width:112px">Obra</th><th>Pergunta</th><th style="width:140px">Resposta</th></tr>
    <tr class="dev"><td><span class="cx"></span></td><td class="tx">Cristiane</td>
      <td><span class="tx">As pend&#234;ncias s&#227;o mesmo s&#243; rodap&#233;, prateleiras e led?</span>
      <span class="de">Qualquer item fora dessa lista muda o cronograma combinado com a cliente.</span></td>
      <td class="pt"><i></i></td></tr>
    <tr class="dev"><td><span class="cx"></span></td><td class="tx">Cristiane</td>
      <td><span class="tx">Previs&#227;o de entrega das duas c&#244;modas</span>
      <span class="de">Servi&#231;o j&#225; autorizado &#8212; revestimento, rod&#237;zios ocultos e dois com freio.</span></td>
      <td class="pt"><i></i></td></tr>
    <tr class="dev"><td><span class="cx"></span></td><td class="tx">Andrea</td>
      <td><span class="tx">Proje&#231;&#227;o de entrega</span>
      <span class="de">Ideal financeiro at&#233; 13/11. Se n&#227;o couber, qual &#233; a data real?</span></td>
      <td class="pt"><i></i></td></tr>
  </table>
  <div class="leg">Todos os itens deste relat&#243;rio est&#227;o no Todoist, projeto <b>produ&#231;&#227;o / deivison</b>, uma coluna por obra.</div>

  <div class="assina">
    <div><div class="n">Jonathan</div><div class="s">Levantamento &#183; 27/10/2026</div></div>
    <div><div class="n">Paulo</div><div class="s">Recebido em ___/___/______</div></div>
    <div><div class="n">Deivison</div><div class="s">Recebido em ___/___/______</div></div>
  </div>
"""

CORTES = [(0, 3, 'Obras com ação agendada'),
          (3, 8, 'Obras em andamento e agendadas'),
          (8, len(OBRAS), 'Obras sem data firme e em espera')]
NFOLHAS = len(CORTES)

out = ["""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Pendências de obra — relatório e checklist</title>
__FONTES__
<style>%s</style>
</head>
<body>""" % CSS]

for fi, (a, b, titulo) in enumerate(CORTES, 1):
    out.append('<div class="sheet">')
    out.append(topo(fi, NFOLHAS))
    if fi == 1:
        out.append(f"""  <div class="kpis">
    <div class="kpi"><div class="r">Obras</div><div class="v">{len(OBRAS)}</div><div class="o">no levantamento</div></div>
    <div class="kpi"><div class="r">Itens</div><div class="v">{NITENS}</div><div class="o">a acompanhar</div></div>
    <div class="kpi"><div class="r">Com data firme</div><div class="v">{NDATA}</div><div class="o">já agendados</div></div>
    <div class="kpi" style="background:var(--blue)"><div class="r">Devolutivas</div><div class="v">{NDEV}</div>
      <div class="o" style="color:#cfe0f2">respostas que o Jonathan espera</div></div>
  </div>

  <div class="faixa">Agenda consolidada — o que já tem data</div>
  <table class="ag">
    <tr><th style="width:66px">Quando</th><th style="width:150px">Obra</th><th>O que acontece</th></tr>
{ag}
  </table>
""")
    out.append(f'  <div class="faixa">{titulo}</div>')
    for nome, st, nota, itens in OBRAS[a:b]:
        out.append(bloco(nome, st, nota, itens))
    if fi == NFOLHAS:
        out.append(FECHO)
    out.append("""  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Pendências de obra · 27/10/2026</span></div>
</div>""")

out.append('\n</body>\n</html>')
print('\n'.join(out))
