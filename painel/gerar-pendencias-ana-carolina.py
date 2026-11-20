# -*- coding: utf-8 -*-
"""Obra Ana Carolina — pendências de entrega, plano de ação e checklist de vistoria.

Duas folhas A4: folha 1 para o Deivison ler e assinar, folha 2 para levar na obra.
Editar os dados em dados-pendencias-ana-carolina.py; o layout é aqui.

    python3 painel/gerar-pendencias-ana-carolina.py > painel/pendencias-ana-carolina.html
"""
import importlib.util, os

_d = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  'dados-pendencias-ana-carolina.py')
_s = importlib.util.spec_from_file_location('dados_pac', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea;
  --red:#B0413F; --redbg:#fdf3f3; --blue:#2F5D8C; --ok:#2F7D4F; }
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
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:18px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:7.5px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.ident{ display:grid; grid-template-columns:1.5fr 1.6fr 1.3fr 1.4fr; gap:5px; margin-bottom:8px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold);
  border-radius:2px; padding:5px 7px }
.ident .c.alerta{ border-top-color:var(--red); background:var(--redbg) }
.ident .r{ font-size:6.5px; letter-spacing:1.2px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:9.5px; font-weight:700; color:var(--navy); margin-top:2px; line-height:1.25 }
.ident .c.alerta .v{ color:var(--red) }
.ident .v.b{ font-weight:400; color:#c3cad3; letter-spacing:1px }

.cab{ background:var(--navy); color:#fff; border-radius:2px 2px 0 0; padding:4px 9px;
  display:flex; justify-content:space-between; align-items:center; margin-top:7px }
.cab .n{ font-size:8.5px; font-weight:700; letter-spacing:1.7px; text-transform:uppercase; color:var(--goldsoft) }
.cab .q{ font-size:7px; color:#b9c3cf; letter-spacing:.5px }

.corpo{ border:1px solid var(--linha); border-top:none; padding:6px 9px 7px; font-size:8.3px; line-height:1.45 }
.corpo p{ margin:0 0 4px }
.corpo ul{ margin:0 0 5px; padding-left:14px }
.corpo li{ margin-bottom:2px }
.fecho{ background:var(--goldbg); border-left:3px solid var(--gold); padding:5px 8px;
  font-size:8.3px; line-height:1.45; color:var(--navy2) }

table.tb{ width:100%; border-collapse:collapse; font-size:8.2px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:6.5px; font-weight:600;
  letter-spacing:.8px; text-transform:uppercase; padding:4px 7px; text-align:left; vertical-align:middle }
table.tb td{ border-bottom:1px solid var(--linha); padding:5px 7px; vertical-align:top; line-height:1.4 }
table.tb tr:nth-child(even) td{ background:#f7f9fb }
.nu{ font-family:'JetBrains Mono',monospace; font-size:8.5px; font-weight:700; color:var(--gold) }
.pend{ font-weight:700; color:var(--red); display:block; line-height:1.25 }
.quando{ font-weight:700; color:var(--navy); white-space:nowrap }
.quando .h{ font-weight:400; font-size:7px; color:var(--muted) }
.quem{ font-weight:600; color:var(--navy2) }
.mono{ font-family:'JetBrains Mono',monospace; font-size:7.5px }
tr.crit td{ background:var(--redbg) !important }
tr.crit .quando{ color:var(--red) }

.causas{ border:1px solid var(--linha); border-top:none; padding:6px 9px }
.causa{ display:flex; gap:7px; font-size:8.3px; line-height:1.42; margin-bottom:4px }
.causa:last-child{ margin-bottom:0 }
.causa .x{ color:var(--red); font-weight:700; font-size:9px; line-height:1.3 }
.causa b{ color:var(--navy) }

.riscos{ border:1px solid var(--linha); border-top:none; padding:6px 9px }
.risco{ font-size:8.2px; line-height:1.42; margin-bottom:4px; padding-left:9px;
  border-left:2px solid var(--goldsoft) }
.risco:last-child{ margin-bottom:0 }
.risco b{ color:var(--navy) }

.cx{ display:inline-block; width:11px; height:11px; border:1.3px solid var(--navy); border-radius:2px }
table.gr{ width:100%; border-collapse:collapse; font-size:8px }
table.gr th{ background:var(--navy2); color:var(--goldsoft); font-size:6px; font-weight:600;
  letter-spacing:.5px; padding:4px 3px; text-align:center; line-height:1.25; vertical-align:bottom }
table.gr th.amb{ text-align:left; padding-left:7px }
table.gr td{ border-bottom:1px solid var(--linha); padding:7px 3px; text-align:center }
table.gr td.amb{ text-align:left; padding-left:7px; font-weight:700; color:var(--navy); font-size:8.5px }
table.gr tr:nth-child(even) td{ background:#f7f9fb }
table.gr td.st{ border-left:1px solid var(--linha) }
.st i{ display:block; border-bottom:1px dotted #b6bfc9; height:10px }
.pt i{ display:block; border-bottom:1px dotted #b6bfc9; height:11px }
.campo{ font-size:7.5px; color:var(--muted) }

.fim{ margin-top:auto; padding-top:9px; display:grid; grid-template-columns:1fr 1fr; gap:22px }
.fim > div{ border-top:1px solid var(--ink); padding-top:4px; text-align:center }
.fim .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.fim .s{ font-size:7px; color:var(--muted) }
.rodape{ margin-top:9px; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:6.5px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

TOPO = ('<div class="topo">'
        '<div class="marca">valvic<small>Marcenaria</small></div>'
        '<div class="doc"><h1>__T__</h1><div class="m">__M__</div></div></div>')

# ── folha 1 ────────────────────────────────────────────────────────────────
ctx = '\n'.join(f'<li>{t}</li>' for t in _m.CONTEXTO)

apont = '\n'.join(
    f'<tr><td style="width:20px" class="nu">{n}</td>'
    f'<td style="width:148px"><span class="pend">{p}</span></td>'
    f'<td>{por}</td>'
    f'<td style="width:132px">{ac}</td></tr>'
    for n, p, por, ac in _m.APONTAMENTOS)

causas = '\n'.join(
    f'<div class="causa"><span class="x">✕</span><div><b>{t}</b> — {d}</div></div>'
    for t, d in _m.CAUSAS)

def _linha_plano(q, o, qm, e):
    cls = ' class="crit"' if q.startswith('Qua') else ''
    return (f'<tr{cls}>'
            f'<td style="width:64px" class="quando">{q}</td>'
            f'<td>{o}</td>'
            f'<td style="width:76px" class="quem">{qm}</td>'
            f'<td style="width:118px">{e}</td></tr>')

plano = '\n'.join(_linha_plano(*l) for l in _m.PLANO)

riscos = '\n'.join(
    f'<div class="risco"><b>{t}</b> {d}</div>' for t, d in _m.RISCOS)

# ── folha 2 ────────────────────────────────────────────────────────────────
confirmadas = '\n'.join(
    f'<tr><td style="width:22px"><span class="cx"></span></td>'
    f'<td style="width:190px"><b style="color:var(--navy)">{t}</b></td>'
    f'<td class="campo">{c}</td></tr>'
    for t, c in _m.PENDENCIAS_CONFIRMADAS)

ths = '\n'.join(f'<th>{c}</th>' for c in _m.CRITERIOS)
grade = '\n'.join(
    '<tr><td class="amb">' + a + '</td>'
    + ''.join('<td><span class="cx"></span></td>' for _ in _m.CRITERIOS)
    + '<td class="st"><i></i></td></tr>'
    for a in _m.AMBIENTES)

novas = '\n'.join(
    f'<tr><td style="width:22px"><span class="cx"></span></td>'
    f'<td class="pt"><i></i></td>'
    f'<td style="width:150px" class="pt"><i></i></td></tr>'
    for _ in range(_m.LINHAS_NOVAS))

HTML = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Obra Ana Carolina — pendências e plano de ação</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
  __TOPO1__

  <div class="ident">
    <div class="c"><div class="r">Cliente</div><div class="v">__CLIENTE__</div></div>
    <div class="c"><div class="r">Obra</div><div class="v">__OBRA__</div></div>
    <div class="c"><div class="r">Vistoria feita em</div><div class="v">__VISTORIA__</div></div>
    <div class="c alerta"><div class="r">Prazo crítico</div><div class="v">__PRAZO__</div></div>
  </div>

  <div class="cab"><span class="n">1 · O contexto — por que estas falhas pesam mais nesta obra</span></div>
  <div class="corpo">
    <p>Esta não é uma obra comum. A cliente:</p>
    <ul>
__CTX__
    </ul>
    <div class="fecho">__FECHO__</div>
  </div>

  <div class="cab"><span class="n">2 · O que a cliente apontou — 19 e 20/11</span>
    <span class="q">__NAP__ pendências até agora</span></div>
  <table class="tb">
    <tr><th>#</th><th>Pendência</th><th>Por que não deveria ter chegado até ela</th><th>Ação</th></tr>
__APONT__
  </table>
  <div class="corpo" style="border-top:1px solid var(--linha); background:var(--redbg)">
    <p style="margin:0"><b>São três até agora — podem aparecer mais.</b> É exatamente por isso que a
    vistoria de terça tem de ser feita com o checklist da folha 2, ambiente por ambiente, e não de olho.</p>
  </div>

  <div class="cab"><span class="n">3 · A causa raiz — não foi azar</span></div>
  <div class="causas">
__CAUSAS__
    <div class="causa" style="margin-top:4px; padding-top:4px; border-top:1px solid var(--linha)">
      <span class="x" style="color:var(--gold)">→</span>
      <div>Enquanto a conferência não virar <b>rotina com papel</b>, a próxima obra repete. O checklist
      da folha 2 passa a ser obrigatório em toda entrega, assinado por você e pelo cliente.</div></div>
  </div>

  <div class="cab"><span class="n">4 · Plano de ação</span><span class="q">entrega livre até 24/11</span></div>
  <table class="tb">
    <tr><th>Quando</th><th>O que fazer</th><th>Quem</th><th>Entregável</th></tr>
__PLANO__
  </table>

  <div class="cab"><span class="n">5 · Condicionantes e riscos</span></div>
  <div class="riscos">
__RISCOS__
  </div>

  <div class="fim">
    <div><div class="n">__GESTOR__</div><div class="s">Gestor de produção · ciente do plano em ___/___/______</div></div>
    <div><div class="n">Jonathan Vargas</div><div class="s">Direção comercial e experiência do cliente</div></div>
  </div>

  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Obra Ana Carolina · pendências e plano de ação · __EMISSAO__</span></div>
</div>

<div class="sheet">
  __TOPO2__

  <div class="ident">
    <div class="c"><div class="r">Responsável pela vistoria</div><div class="v b">__________________</div></div>
    <div class="c"><div class="r">Data</div><div class="v b">___/___/______</div></div>
    <div class="c"><div class="r">Chegada / saída</div><div class="v b">__:__ · __:__</div></div>
    <div class="c"><div class="r">Acompanhado por</div><div class="v b">__________________</div></div>
  </div>

  <div class="cab"><span class="n">A · Pendências já apontadas pela cliente</span>
    <span class="q">medir e anotar na obra</span></div>
  <table class="tb">
    <tr><th style="width:22px">✓</th><th>Item</th><th>Medida / definição levantada na obra</th></tr>
__CONFIRMADAS__
  </table>

  <div class="cab"><span class="n">B · Varredura ambiente por ambiente</span>
    <span class="q">__NAMB__ ambientes · marcar cada critério</span></div>
  <table class="gr">
    <tr><th class="amb">Ambiente</th>__THS__<th style="width:120px">Pendência encontrada</th></tr>
__GRADE__
  </table>
  <div class="corpo" style="border-top:1px solid var(--linha); font-size:7.8px">
    <p style="margin:0"><b>“Itens do projeto conferidos um a um”</b> quer dizer com o projeto executivo na mão,
    lendo a lista de peças do ambiente e apontando cada uma na parede. Foi a ausência desta coluna que
    deixou o espelho do lavabo passar.</p>
  </div>

  <div class="cab"><span class="n">C · Pendências novas encontradas nesta vistoria</span>
    <span class="q">tudo entra no pacote de 24/11</span></div>
  <table class="tb">
    <tr><th style="width:22px">✓</th><th>O que falta ou está errado</th><th style="width:150px">Ambiente / o que fazer</th></tr>
__NOVAS__
  </table>

  <div class="fim">
    <div><div class="n">__GESTOR__</div><div class="s">Vistoria conferida item a item</div></div>
    <div><div class="n">__CLIENTE__</div><div class="s">Cliente · entrega aceita em ___/___/______</div></div>
  </div>

  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Checklist de vistoria final · obra Ana Carolina · __EMISSAO__</span></div>
</div>

</body>
</html>'''

out = (HTML
  .replace('__TOPO1__', TOPO
      .replace('__T__', 'Obra Ana Carolina — Pendências e Plano de Ação')
      .replace('__M__', f'Para {_m.GESTOR} · gestor de produção · emitido em {_m.EMISSAO}'))
  .replace('__TOPO2__', TOPO
      .replace('__T__', 'Checklist de Vistoria Final — Obra Ana Carolina')
      .replace('__M__', 'Para levar na obra · preencher na obra, não depois'))
  .replace('__CSS__', CSS)
  .replace('__CTX__', ctx).replace('__FECHO__', _m.CONTEXTO_FECHO)
  .replace('__APONT__', apont).replace('__NAP__', str(len(_m.APONTAMENTOS)))
  .replace('__CAUSAS__', causas)
  .replace('__PLANO__', plano)
  .replace('__RISCOS__', riscos)
  .replace('__CONFIRMADAS__', confirmadas)
  .replace('__THS__', ths).replace('__GRADE__', grade).replace('__NAMB__', str(len(_m.AMBIENTES)))
  .replace('__NOVAS__', novas)
  .replace('__CLIENTE__', _m.CLIENTE).replace('__OBRA__', _m.OBRA)
  .replace('__VISTORIA__', _m.VISTORIA).replace('__PRAZO__', _m.PRAZO)
  .replace('__GESTOR__', _m.GESTOR).replace('__EMISSAO__', _m.EMISSAO))

print(out)
