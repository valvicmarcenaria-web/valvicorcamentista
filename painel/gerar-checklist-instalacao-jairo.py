# -*- coding: utf-8 -*-
"""Checklist de instalação — obra Jairo. Uma folha A4 para o profissional levar.

Os itens de instalação vêm do Jonathan (27/10/2026). As linhas em branco são
para o levantamento de pendências gerais a ser feito com o Jhon.

    python3 painel/gerar-checklist-instalacao-jairo.py > painel/checklist-instalacao-jairo.html
"""

INSTALAR = [
    ('Cabeceira industrial com estofado', ''),
    ('Estrutura de prateleiras da cozinha', ''),
    ('Mesa de trabalho do quarto', ''),
    ('Mesa de centro', 'PENDENTE DE VALIDAÇÃO DO CLIENTE — não instalar antes de validar'),
]
AGENDADOS = [
    ('Fixação do estofado na estrutura da cabeceira', ''),
    ('Tingimento da peça de madeira', ''),
]
LINHAS_LEVANTAMENTO = 11

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea; --red:#B0413F; }
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
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:20px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:8px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.ident{ display:grid; grid-template-columns:2fr 1fr 1fr 1fr; gap:6px; margin-bottom:10px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold);
  border-radius:2px; padding:6px 8px }
.ident .r{ font-size:7px; letter-spacing:1.3px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:11px; font-weight:700; color:var(--navy); margin-top:3px; min-height:14px }
.ident .v.b{ font-weight:400; color:var(--linha); letter-spacing:1px }

.cab{ background:var(--navy); color:#fff; border-radius:2px 2px 0 0; padding:5px 10px;
  display:flex; justify-content:space-between; align-items:center; margin-top:10px }
.cab .n{ font-size:9.5px; font-weight:700; letter-spacing:1.8px; text-transform:uppercase; color:var(--goldsoft) }
.cab .q{ font-size:8px; color:#b9c3cf }
.nota{ background:var(--goldbg); font-size:8.5px; color:var(--navy2); padding:5px 10px; line-height:1.4 }

table.tb{ width:100%; border-collapse:collapse; font-size:9.5px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:7px; font-weight:600;
  letter-spacing:.9px; text-transform:uppercase; padding:4px 8px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:11px 8px; vertical-align:middle }
table.tb tr:nth-child(odd) td{ background:#f7f9fb }
tr.ret td{ background:#fdf3f3 !important }
.cx{ display:inline-block; width:12px; height:12px; border:1.4px solid var(--navy); border-radius:2px }
.it{ font-weight:600; color:var(--navy) }
.ob{ font-size:8px; color:var(--muted); display:block; margin-top:1px }
.ob.red{ color:var(--red); font-weight:600 }
.pt i{ display:block; border-bottom:1px dotted #b6bfc9; height:11px }
.num{ font-family:'JetBrains Mono',monospace; font-size:8.5px; color:var(--muted) }

.fim{ margin-top:auto; padding-top:10px; display:grid; grid-template-columns:1fr 1fr; gap:24px }
.fim > div{ border-top:1px solid var(--ink); padding-top:4px; text-align:center }
.fim .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.fim .s{ font-size:7.5px; color:var(--muted) }
.rodape{ margin-top:12px; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

def linhas(itens):
    out=[]
    for t,o in itens:
        ret=' class="ret"' if o else ''
        ob=f'<span class="ob red">{o}</span>' if o else ''
        out.append(f'<tr{ret}><td style="width:26px"><span class="cx"></span></td>'
                   f'<td><span class="it">{t}</span>{ob}</td>'
                   f'<td style="width:150px" class="pt"><i></i></td></tr>')
    return '\n'.join(out)

brancas='\n'.join(
  f'<tr><td style="width:26px"><span class="cx"></span></td>'
  f'<td><span class="num">{i:02d}</span> <span class="pt" style="display:inline-block;width:88%"><i></i></span></td>'
  f'<td style="width:150px" class="pt"><i></i></td></tr>'
  for i in range(1, LINHAS_LEVANTAMENTO+1))

print('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Checklist de instalação — obra Jairo</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Checklist de Instalação — Obra Jairo</h1>
      <div class="m">Para o profissional responsável · emitido em 27/10/2026</div></div>
  </div>

  <div class="ident">
    <div class="c"><div class="r">Profissional responsável</div><div class="v b">________________________</div></div>
    <div class="c"><div class="r">Data</div><div class="v b">___/___/______</div></div>
    <div class="c"><div class="r">Chegada</div><div class="v b">___:___</div></div>
    <div class="c"><div class="r">Saída</div><div class="v b">___:___</div></div>
  </div>

  <div class="cab"><span class="n">1 · Itens a instalar</span><span class="q">__NINST__ itens</span></div>
  <table class="tb">
    <tr><th style="width:26px">✓</th><th>Item</th><th style="width:150px">Observação do profissional</th></tr>
__INSTALAR__
  </table>

  <div class="cab"><span class="n">2 · Serviços da peça</span><span class="q">__NAGEN__ itens</span></div>
  <table class="tb">
    <tr><th style="width:26px">✓</th><th>Serviço</th><th style="width:150px">Observação do profissional</th></tr>
__AGENDADOS__
  </table>

  <div class="cab"><span class="n">3 · Pendências gerais — levantamento com o Jhon</span><span class="q">preencher na obra</span></div>
  <div class="nota">Linhas em branco de propósito: são para o levantamento com o <b>Jhon</b>. Anotar item por item, mesmo
  o que parecer pequeno — o que não for escrito aqui não entra na programação e volta como retrabalho.</div>
  <table class="tb">
    <tr><th style="width:26px">✓</th><th>O que falta</th><th style="width:150px">Observação do profissional</th></tr>
__BRANCAS__
  </table>

  <div class="fim">
    <div><div class="n">Profissional responsável</div><div class="s">Levantamento conferido na obra</div></div>
    <div><div class="n">Deivison</div><div class="s">Recebido em ___/___/______</div></div>
  </div>

  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Checklist de instalação · obra Jairo · 27/10/2026</span></div>
</div>

</body>
</html>'''
  .replace('__CSS__', CSS)
  .replace('__INSTALAR__', linhas(INSTALAR)).replace('__NINST__', str(len(INSTALAR)))
  .replace('__AGENDADOS__', linhas(AGENDADOS)).replace('__NAGEN__', str(len(AGENDADOS)))
  .replace('__BRANCAS__', brancas))
