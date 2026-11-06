# -*- coding: utf-8 -*-
"""Escopo de venda — Attos Henrique Salles · Costa Laguna. Para a gestora.

    python3 painel/gerar-escopo-attos.py > painel/escopo-venda-attos.html
"""
import importlib.util, os
_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-escopo-attos.py')
_s = importlib.util.spec_from_file_location('dados_escopo_attos', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
OBRA, PRAZOS, ESCRITORIO, ITENS = _m.OBRA, _m.PRAZOS, _m.ESCRITORIO, _m.ITENS
FERRAGENS, ESTRUTURA, FORA, DEFINIR = _m.FERRAGENS, _m.ESTRUTURA, _m.FORA, _m.DEFINIR

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea;
  --red:#B0413F; --blue:#2F5D8C; --ok:#2F7D4F; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:11mm 12mm 10mm; display:flex; flex-direction:column;
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

.ident{ display:grid; grid-template-columns:repeat(4,1fr); gap:5px; margin-bottom:7px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold);
  border-radius:2px; padding:5px 8px }
.ident .r{ font-size:6.5px; letter-spacing:1.2px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:9.5px; font-weight:700; color:var(--navy); margin-top:2px }

.aviso{ background:var(--goldbg); border-left:3px solid var(--gold); border-radius:2px;
  padding:6px 9px; font-size:8.5px; line-height:1.48; color:var(--navy2); margin-bottom:8px }
.aviso b{ color:var(--navy) }

.faixa{ background:var(--navy); color:var(--goldsoft); font-size:8.5px; font-weight:600;
  letter-spacing:2px; text-transform:uppercase; padding:5px 10px; margin:8px 0 6px; border-radius:2px }

table.tb{ width:100%; border-collapse:collapse; font-size:8.5px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:6.5px; font-weight:600;
  letter-spacing:.9px; text-transform:uppercase; padding:4px 7px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:5px 7px; vertical-align:top }
table.tb tr:nth-child(odd) td{ background:#f7f9fb }
.nn{ font-family:'JetBrains Mono',monospace; font-size:8.5px; color:var(--gold); font-weight:600 }
.tt{ font-weight:700; color:var(--navy); display:block }
.dd{ font-size:8px; color:#45525f; line-height:1.42 }
.dd b{ color:var(--navy) }
.md{ font-family:'JetBrains Mono',monospace; font-size:7.5px; color:#39465a }
.cx{ display:inline-block; width:11px; height:11px; border:1.4px solid var(--navy); border-radius:2px }
.pt i{ display:block; border-bottom:1px dotted #b6bfc9; height:10px }

.bloco{ border:1px solid var(--linha); border-left:3px solid var(--navy2); border-radius:2px;
  padding:7px 10px; margin-bottom:6px; font-size:8.5px; line-height:1.5; color:#39465a }
.bloco h3{ margin:0 0 3px; font-size:9px; color:var(--navy); font-weight:700;
  letter-spacing:1.1px; text-transform:uppercase }
.bloco b{ color:var(--navy) }
.bloco.alerta{ border-left-color:var(--red); background:#fdf6f5 }
.bloco .ff{ color:var(--red) }
.bloco .ff b{ color:var(--red) }

.destaque{ border:2px solid var(--gold); border-radius:3px; background:#fffdf7;
  padding:8px 11px; margin-bottom:8px }
.destaque h3{ margin:0 0 5px; font-family:'Cormorant Garamond',serif; font-size:15px;
  font-weight:700; color:var(--navy) }
.destaque h3 span{ font-family:'Inter',sans-serif; font-size:7px; font-weight:600;
  letter-spacing:1.6px; text-transform:uppercase; color:var(--gold); display:block; margin-bottom:2px }
.destaque .it{ display:flex; gap:7px; align-items:flex-start; padding:4px 0;
  border-top:1px solid #efe4c8; font-size:8.5px; line-height:1.45; color:#39465a }
.destaque .it b{ color:var(--navy) }
.destaque .it .k{ flex:0 0 118px; font-weight:700; color:var(--navy) }
.destaque .it .q{ flex:0 0 11px; height:11px; border:1.4px solid var(--navy); border-radius:2px; margin-top:1px }
.amb{ font-family:'JetBrains Mono',monospace; font-size:7.5px; letter-spacing:.4px;
  text-transform:uppercase; color:var(--navy2); font-weight:700 }
tr.esc td{ background:#fffdf7 !important; box-shadow:inset 3px 0 0 var(--gold) }
.prz{ display:grid; grid-template-columns:repeat(2,1fr); gap:5px; margin-bottom:8px }
.prz .c{ border:1px solid var(--linha); border-left:3px solid var(--navy2); border-radius:2px; padding:5px 8px }
.prz .r{ font-size:6.5px; letter-spacing:1.2px; text-transform:uppercase; color:var(--muted) }
.prz .v{ font-size:8.5px; color:#39465a; margin-top:2px; line-height:1.4 }
.prz .c.dest{ border-left-color:var(--gold); background:#fffdf7 }
.prz .c.dest .v{ font-weight:700; color:var(--navy) }


.duas{ display:grid; grid-template-columns:1fr 1fr; gap:8px }
.cx2{ display:flex; gap:6px; align-items:flex-start; font-size:8.5px; line-height:1.4;
  padding:3px 0; border-bottom:1px solid var(--linha) }
.cx2 span.b{ display:inline-block; width:10px; height:10px; border:1.3px solid var(--navy);
  border-radius:2px; flex:0 0 auto; margin-top:1px }
.foraescopo .cx2{ color:var(--red) }

.assina{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; margin-top:auto; padding-top:10px }
.assina > div{ border-top:1px solid var(--ink); padding-top:3px; text-align:center }
.assina .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:7.5px; color:var(--muted) }
.rodape{ margin-top:10px; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""


def topo(i, t):
    return f"""  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Escopo de Venda</h1>
      <div class="m">{OBRA['cliente']} · {OBRA['obra']} · folha {i} de 2</div></div>
  </div>"""

RODAPE = ('  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>'
          '<span>Escopo de venda · Costa Laguna · Attos</span></div>\n</div>')

prz_html = ''.join(
  '<div class="c%s"><div class="r">%s</div><div class="v">%s</div></div>'
  % (' dest' if r == 'Escritório' else '', r, v) for r, v in PRAZOS)

esc_html = ''.join(
  f'<div class="it"><span class="q"></span><span class="k">{k}</span><span>{v}</span></div>'
  for k, v in ESCRITORIO)

itens_html = '\n'.join(
  f'    <tr class="{"esc" if a == "Escritório" else ""}">'
  f'<td style="width:62px" class="amb">{a}</td>'
  f'<td style="width:188px"><span class="tt">{t}</span></td>'
  f'<td><span class="dd">{d}</span></td>'
  f'<td style="width:24px"><span class="cx"></span></td></tr>'
  for a, t, d in ITENS)

def_html = '\n'.join(
  f'    <tr><td style="width:22px"><span class="cx"></span></td>'
  f'<td style="width:150px"><span class="tt">{t}</span></td>'
  f'<td><span class="dd">{d}</span></td>'
  f'<td style="width:80px" class="pt"><i></i></td></tr>'
  for t, d in DEFINIR)

print("""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Escopo de venda — Attos · Costa Laguna</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
__TOPO1__
  <div class="ident">
    <div class="c"><div class="r">Cliente</div><div class="v">__CLIENTE__</div></div>
    <div class="c"><div class="r">Obra</div><div class="v" style="font-size:8px">__OBRA__</div></div>
    <div class="c"><div class="r">Projeto</div><div class="v" style="font-size:8px">__PROJETO__</div></div>
    <div class="c"><div class="r">Escopo</div><div class="v" style="font-size:8px">__ESCOPO__</div></div>
  </div>

  <div class="aviso"><b>Como usar.</b> Escopo da venda em especificação técnica, montado a partir do contrato de
  06/11/2026 e da proposta linha Hettich. Leia cruzando com o <b>executivo Costa Laguna ATTOS Rev. 03</b>.
  Onde esta lista divergir do projeto, <b>não libere a produção</b>: registre e devolva ao comercial.<br>
  <b>Alteração de projeto só vale por escrito</b> (cláusula 1.2) e pode gerar aditivo de prazo e de preço.</div>

  <div class="destaque">
    <h3><span>Atenção · prioridade da obra</span>O escritório sai à frente</h3>
__ESCRITORIO__
  </div>

  <div class="prz">__PRAZOS__</div>

  <div class="faixa">1 · Os 14 itens contratados, ambiente por ambiente</div>
  <table class="tb">
    <tr><th style="width:62px">Ambiente</th><th style="width:188px">Item</th>
        <th>Especificação</th><th style="width:24px">OK</th></tr>
__ITENS__
  </table>
__RODAPE__

<div class="sheet">
__TOPO2__
  <div class="faixa">2 · Ferragens, estrutura e o que fica fora</div>
  <div class="bloco"><b>Ferragens.</b> __FERRAGENS__</div>
  <div class="bloco"><b>Estrutura e chapas.</b> __ESTRUTURA__</div>
  <div class="bloco alerta"><span class="ff"><b>Fora do escopo.</b></span> __FORA__</div>

  <div class="faixa">3 · A definir e a alinhar antes de liberar a produção</div>
  <table class="tb">
    <tr><th style="width:22px">&#10003;</th><th style="width:150px">O que</th>
        <th>Condição</th><th style="width:80px">Definido em</th></tr>
__DEFINIR__
  </table>

  <div class="assina">
    <div><div class="n">Comercial</div><div class="s">Repassado em ___/___/______</div></div>
    <div><div class="n">Gestão</div><div class="s">Recebido e conferido em ___/___/______</div></div>
    <div><div class="n">Produção</div><div class="s">Liberado em ___/___/______</div></div>
  </div>
__RODAPE__

</body>
</html>"""
  .replace('__CSS__', CSS)
  .replace('__TOPO1__', topo(1, 2)).replace('__TOPO2__', topo(2, 2))
  .replace('__CLIENTE__', OBRA['cliente']).replace('__OBRA__', OBRA['obra'])
  .replace('__PROJETO__', OBRA['projeto']).replace('__ESCOPO__', OBRA['escopo'])
  .replace('__ESCRITORIO__', esc_html).replace('__PRAZOS__', prz_html)
  .replace('__ITENS__', itens_html).replace('__FERRAGENS__', FERRAGENS)
  .replace('__ESTRUTURA__', ESTRUTURA).replace('__FORA__', FORA)
  .replace('__DEFINIR__', def_html).replace('__RODAPE__', RODAPE))
