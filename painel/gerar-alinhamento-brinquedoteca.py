# -*- coding: utf-8 -*-
"""Alinhamento técnico de venda → produção: brinquedoteca Eliza & Luiz Gustavo.

Documento para a produção ler e cruzar com o projeto executivo. Sem valores,
prazos ou condições comerciais.

    python3 painel/gerar-alinhamento-brinquedoteca.py > painel/alinhamento-brinquedoteca.html
"""
import importlib.util, os
_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-alinhamento-brinquedoteca.py')
_s = importlib.util.spec_from_file_location('dados_alinhamento_brinquedoteca', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
OBRA, SISTEMAS, CONJUNTOS = _m.OBRA, _m.SISTEMAS, _m.CONJUNTOS
ACOMPANHA, NAO_INCLUSO, A_DEFINIR = _m.ACOMPANHA, _m.NAO_INCLUSO, _m.A_DEFINIR

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
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:9px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:25px; font-weight:700;
  color:var(--navy); letter-spacing:.5px; line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7.5px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-top:3px }
.doc{ text-align:right }
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:19px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:8px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.ident{ display:grid; grid-template-columns:repeat(3,1fr); gap:6px; margin-bottom:8px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold);
  border-radius:2px; padding:6px 9px }
.ident .r{ font-size:7px; letter-spacing:1.3px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:10.5px; font-weight:700; color:var(--navy); margin-top:2px }

.aviso{ background:var(--goldbg); border-left:3px solid var(--gold); border-radius:2px;
  padding:7px 10px; font-size:9px; line-height:1.5; color:var(--navy2); margin-bottom:9px }

.faixa{ background:var(--navy); color:var(--goldsoft); font-size:8.5px; font-weight:600;
  letter-spacing:2px; text-transform:uppercase; padding:5px 10px; margin:9px 0 6px; border-radius:2px }

.sis{ border:1px solid var(--linha); border-left:3px solid var(--navy2); border-radius:2px;
  padding:7px 11px; margin-bottom:6px }
.sis h3{ margin:0 0 3px; font-size:9.5px; color:var(--navy); font-weight:700;
  letter-spacing:1.2px; text-transform:uppercase }
.sis ul{ margin:0; padding-left:14px }
.sis li{ font-size:9px; line-height:1.5; color:#39465a; margin-bottom:1px }
.sis b{ color:var(--navy) }

table.tb{ width:100%; border-collapse:collapse; font-size:9px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:7px; font-weight:600;
  letter-spacing:.9px; text-transform:uppercase; padding:4px 8px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:6px 8px; vertical-align:top }
table.tb tr:nth-child(odd) td{ background:#f7f9fb }
.nn{ font-family:'JetBrains Mono',monospace; font-size:9px; color:var(--gold); font-weight:600 }
.tt{ font-weight:700; color:var(--navy); display:block; margin-bottom:1px }
.dd{ font-size:8.5px; color:#45525f; line-height:1.45 }
.dd b{ color:var(--navy) }
.cx{ display:inline-block; width:12px; height:12px; border:1.4px solid var(--navy); border-radius:2px }
.pt i{ display:block; border-bottom:1px dotted #b6bfc9; height:10px }

.duas{ display:grid; grid-template-columns:1fr 1fr; gap:8px }
.cx2{ display:flex; gap:6px; align-items:flex-start; font-size:9px; line-height:1.4;
  padding:3px 0; border-bottom:1px solid var(--linha) }
.cx2 span.b{ display:inline-block; width:10px; height:10px; border:1.3px solid var(--navy);
  border-radius:2px; flex:0 0 auto; margin-top:1px }
.foraescopo .cx2{ color:var(--red) }

.assina{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; margin-top:auto; padding-top:10px }
.assina > div{ border-top:1px solid var(--ink); padding-top:3px; text-align:center }
.assina .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:7.5px; color:var(--muted) }
.rodape{ margin-top:11px; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

def topo(i, t):
    return f'''  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Alinhamento Técnico — Brinquedoteca</h1>
      <div class="m">{OBRA['cliente']} · venda → produção · folha {i} de {t}</div></div>
  </div>'''

RODAPE = '''  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Alinhamento técnico · brinquedoteca · __CLI__</span></div>
</div>'''.replace('__CLI__', OBRA['cliente'])

sis_html = '\n'.join(
  '  <div class="sis"><h3>%s</h3><ul>%s</ul></div>' % (t, ''.join(f'<li>{i}</li>' for i in its))
  for t, its in SISTEMAS)

conj_html = '\n'.join(
  f'    <tr><td style="width:26px" class="nn">{n}</td>'
  f'<td><span class="tt">{t}</span><span class="dd">{d}</span></td>'
  f'<td style="width:26px"><span class="cx"></span></td>'
  f'<td style="width:132px" class="pt"><i></i></td></tr>'
  for n, t, d in CONJUNTOS)

def lista(itens, cls=''):
    meio = (len(itens) + 1) // 2
    col = lambda ns: '<div>' + ''.join(
      f'<div class="cx2"><span class="b"></span><span>{i}</span></div>' for i in ns) + '</div>'
    return col(itens[:meio]) + col(itens[meio:])

defin_html = '\n'.join(
  f'    <tr><td style="width:26px"><span class="cx"></span></td>'
  f'<td style="width:190px"><span class="tt">{t}</span></td>'
  f'<td><span class="dd">{d}</span></td>'
  f'<td style="width:120px" class="pt"><i></i></td></tr>'
  for t, d in A_DEFINIR)

print('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Alinhamento técnico — brinquedoteca</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
__TOPO1__
  <div class="ident">
    <div class="c"><div class="r">Cliente</div><div class="v">__CLIENTE__</div></div>
    <div class="c"><div class="r">Objeto</div><div class="v">__OBJETO__</div></div>
    <div class="c"><div class="r">Projeto</div><div class="v" style="font-size:9px">__PROJETO__</div></div>
  </div>

  <div class="aviso"><b>Como usar este documento.</b> Ele traz o que foi vendido, em especificação técnica.
  Leia cruzando com o <b>projeto executivo</b>: onde a especificação daqui divergir do projeto, <b>não produza</b> —
  registre a divergência e devolva ao comercial antes de cortar, soldar ou comprar.<br>
  <b>Ofícios no contrato:</b> __OFICIOS__.</div>

  <div class="faixa">1 · Especificação por sistema</div>
__SISTEMAS__
__RODAPE__

<div class="sheet">
__TOPO2__
  <div class="faixa">2 · Os conjuntos — confira cada um contra o projeto</div>
  <table class="tb">
    <tr><th style="width:26px">Nº</th><th>Conjunto e especificação</th>
        <th style="width:26px">Confere</th><th style="width:132px">Divergência encontrada</th></tr>
__CONJUNTOS__
  </table>
__RODAPE__

<div class="sheet">
__TOPO3__
  <div class="faixa">3 · O que acompanha o fornecimento</div>
  <div class="duas">__ACOMPANHA__</div>

  <div class="faixa">4 · Fora do escopo — não fabricar, não comprar, não instalar</div>
  <div class="duas foraescopo">__NAOINCLUSO__</div>

  <div class="faixa">5 · A definir antes da fabricação</div>
  <table class="tb">
    <tr><th style="width:26px">&#10003;</th><th style="width:190px">O que</th><th>Condição</th><th style="width:120px">Definido em</th></tr>
__DEFINIR__
  </table>

  <div class="assina">
    <div><div class="n">Comercial</div><div class="s">Repassado em ___/___/______</div></div>
    <div><div class="n">Produção</div><div class="s">Recebido e conferido em ___/___/______</div></div>
    <div><div class="n">Projeto</div><div class="s">Conferido em ___/___/______</div></div>
  </div>
__RODAPE__

</body>
</html>'''
  .replace('__CSS__', CSS)
  .replace('__TOPO1__', topo(1,3)).replace('__TOPO2__', topo(2,3)).replace('__TOPO3__', topo(3,3))
  .replace('__CLIENTE__', OBRA['cliente']).replace('__OBJETO__', OBRA['objeto'])
  .replace('__PROJETO__', OBRA['projeto']).replace('__OFICIOS__', OBRA['oficios'])
  .replace('__SISTEMAS__', sis_html).replace('__CONJUNTOS__', conj_html)
  .replace('__ACOMPANHA__', lista(ACOMPANHA)).replace('__NAOINCLUSO__', lista(NAO_INCLUSO))
  .replace('__DEFINIR__', defin_html)
  .replace('__RODAPE__', RODAPE))
