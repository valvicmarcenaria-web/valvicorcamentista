# -*- coding: utf-8 -*-
"""Escopo de venda — Raquel Franco · quarto e banheiro. Para a gestora.

    python3 painel/gerar-escopo-raquel.py > painel/escopo-venda-raquel.html
"""
import importlib.util, os
_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-escopo-raquel.py')
_s = importlib.util.spec_from_file_location('dados_escopo_raquel', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
OBRA, MARCENARIA, BANHEIRO, ROUPEIRO = _m.OBRA, _m.MARCENARIA, _m.BANHEIRO, _m.ROUPEIRO
MATERIAIS, FERRAGENS, FORA, DEFINIR = _m.MATERIAIS, _m.FERRAGENS, _m.FORA, _m.DEFINIR

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

.duas{ display:grid; grid-template-columns:1fr 1fr; gap:8px }
.cx2{ display:flex; gap:6px; align-items:flex-start; font-size:8.5px; line-height:1.4;
  padding:3px 0; border-bottom:1px solid var(--linha) }
.cx2 span.b{ display:inline-block; width:10px; height:10px; border:1.3px solid var(--navy);
  border-radius:2px; flex:0 0 auto; margin-top:1px }
.foraescopo .cx2{ color:var(--red) }

.assina{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; margin-top:16px; padding-top:10px }
.assina > div{ border-top:1px solid var(--ink); padding-top:3px; text-align:center }
.assina .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:7.5px; color:var(--muted) }
.rodape{ margin-top:auto; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

def topo(i, t):
    return f'''  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Escopo de Venda</h1>
      <div class="m">{OBRA['cliente']} · {OBRA['ambiente']} · folha {i} de {t}</div></div>
  </div>'''

RODAPE = ('  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>'
          '<span>Escopo de venda · __CLI__</span></div>\n</div>').replace('__CLI__', OBRA['cliente'])

def linhas(itens):
    return '\n'.join(
      f'    <tr><td style="width:22px" class="nn">{n}</td>'
      f'<td style="width:150px"><span class="tt">{t}</span><span class="dd">{d}</span></td>'
      f'<td style="width:118px" class="md">{mat}</td>'
      f'<td style="width:96px" class="md">{med}</td>'
      f'<td style="width:34px" class="md">{pr}</td>'
      f'<td style="width:24px"><span class="cx"></span></td></tr>'
      for n, t, mat, med, pr, d in itens)

def lista(itens, ):
    meio = (len(itens) + 1) // 2
    col = lambda ns: '<div>' + ''.join(
      f'<div class="cx2"><span class="b"></span><span>{i}</span></div>' for i in ns) + '</div>'
    return col(itens[:meio]) + col(itens[meio:])

mat_html = '\n'.join(
  f'    <tr><td style="width:170px"><span class="tt">{m}</span></td><td><span class="dd">{o}</span></td></tr>'
  for m, o in MATERIAIS)

def_html = '\n'.join(
  f'    <tr><td style="width:22px"><span class="cx"></span></td>'
  f'<td style="width:160px"><span class="tt">{t}</span></td>'
  f'<td><span class="dd">{d}</span></td>'
  f'<td style="width:95px" class="pt"><i></i></td></tr>'
  for t, d in DEFINIR)

print('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Escopo de venda — Raquel Franco</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
__TOPO1__
  <div class="ident">
    <div class="c"><div class="r">Cliente</div><div class="v">__CLIENTE__</div></div>
    <div class="c"><div class="r">Ambientes</div><div class="v">__AMBIENTE__</div></div>
    <div class="c"><div class="r">Projeto</div><div class="v" style="font-size:8px">__PROJETO__</div></div>
    <div class="c"><div class="r">Designer</div><div class="v" style="font-size:8px">__DESIGNER__</div></div>
  </div>

  <div class="aviso"><b>Como usar.</b> Este é o escopo da venda traduzido em especificação técnica, montado a partir
  do <b>projeto executivo</b> e do registro comercial. Leia-o cruzando com as pranchas: onde esta lista divergir do
  projeto, <b>não libere a produção</b> — registre e devolva ao comercial.<br>
  <b>Origem.</b> A proposta comercial e o contrato assinado <b>não foram localizados no Drive</b>; o escopo abaixo
  reflete o projeto executivo. A conferência contra o contrato continua pendente.<br>
  <b>Nota do projeto, em todas as pranchas:</b> em caso de dúvida não execute, ligue para a designer; todas as medidas
  devem ser rigorosamente conferidas no local.</div>

  <div class="faixa">1 · Marcenaria do quarto</div>
  <table class="tb">
    <tr><th style="width:22px">Nº</th><th style="width:150px">Peça e detalhamento</th>
        <th style="width:118px">Material</th><th style="width:96px">Medidas (cm)</th>
        <th style="width:34px">Prancha</th><th style="width:24px">OK</th></tr>
__MARCENARIA__
  </table>
__RODAPE__

<div class="sheet">
__TOPO2__
  <div class="faixa">2 · Marcenaria do banheiro</div>
  <table class="tb">
    <tr><th style="width:22px">Nº</th><th style="width:150px">Peça e detalhamento</th>
        <th style="width:118px">Material</th><th style="width:96px">Medidas (cm)</th>
        <th style="width:34px">Prancha</th><th style="width:24px">OK</th></tr>
__BANHEIRO__
  </table>

  <div class="faixa">3 · Roupeiro — prancha __RPR__</div>
  <div class="bloco"><h3>Reaproveitamento · __RMED__</h3>__RTXT__</div>

  <div class="faixa">4 · Materiais e acabamentos</div>
  <table class="tb">
    <tr><th style="width:170px">Material</th><th>Onde entra</th></tr>
__MATERIAIS__
  </table>

  <div class="faixa">5 · Ferragens e componentes</div>
  <div class="duas">__FERRAGENS__</div>
__RODAPE__

<div class="sheet">
__TOPO3__
  <div class="faixa">6 · Fora do escopo da marcenaria</div>
  <div class="duas foraescopo">__FORA__</div>

  <div class="faixa">7 · A definir antes de liberar a produção</div>
  <table class="tb">
    <tr><th style="width:22px">&#10003;</th><th style="width:160px">O que</th>
        <th>Condição</th><th style="width:95px">Definido em</th></tr>
__DEFINIR__
  </table>

  <div class="faixa">8 · Registro comercial</div>
  <div class="bloco"><h3>Venda</h3>Valor contratado <b>__VALOR__</b> · situação <b>__SITUACAO__</b>,
  conforme a planilha de gestão. <b>Sem proposta e sem contrato localizados</b> para conferência de condições,
  prazo e memorial descritivo.</div>

  <div class="assina">
    <div><div class="n">Comercial</div><div class="s">Repassado em ___/___/______</div></div>
    <div><div class="n">Gestão</div><div class="s">Recebido e conferido em ___/___/______</div></div>
    <div><div class="n">Produção</div><div class="s">Liberado em ___/___/______</div></div>
  </div>
__RODAPE__

</body>
</html>'''
  .replace('__CSS__', CSS)
  .replace('__TOPO1__', topo(1,3)).replace('__TOPO2__', topo(2,3)).replace('__TOPO3__', topo(3,3))
  .replace('__CLIENTE__', OBRA['cliente']).replace('__AMBIENTE__', OBRA['ambiente'])
  .replace('__PROJETO__', OBRA['projeto']).replace('__DESIGNER__', OBRA['designer'])
  .replace('__MARCENARIA__', linhas(MARCENARIA)).replace('__BANHEIRO__', linhas(BANHEIRO))
  .replace('__RPR__', ROUPEIRO['prancha']).replace('__RMED__', ROUPEIRO['medidas'])
  .replace('__RTXT__', ROUPEIRO['texto'])
  .replace('__MATERIAIS__', mat_html).replace('__FERRAGENS__', lista(FERRAGENS))
  .replace('__FORA__', lista(FORA)).replace('__DEFINIR__', def_html)
  .replace('__VALOR__', OBRA['valor']).replace('__SITUACAO__', OBRA['situacao'])
  .replace('__RODAPE__', RODAPE))
