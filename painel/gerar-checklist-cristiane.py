# -*- coding: utf-8 -*-
"""Checklist da obra Cristiane — uma folha A4 com as pendências listadas no Todoist.

Fonte: projeto "obras em atraso", seção "Cristiane - retorno dia 19/10".
Edite AQUI, nunca no HTML final.

    python3 painel/gerar-checklist-cristiane.py > painel/checklist-obra-cristiane.html
"""

AMBIENTES = [
    ('Geral', '', [
        ('Fazer checklist geral de pendências', ''),
    ]),
    ('Quarto da filha', '', [
        ('Espelho', 'Está pronto na DFA — só buscar'),
        ('Detalhe do perfil de led amassado', ''),
        ('Base da torre', ''),
        ('Perfil de alumínio do rodapé', ''),
    ]),
    ('Quarto do Vitor', '', [
        ('Led', ''),
        ('Acabamento do painel de cabeceira no encontro com o alisar', ''),
    ]),
    ('Quarto do casal', '', [
        ('Acabamento dos frisos na cabeceira', ''),
        ('Perfil de alumínio no piso', ''),
    ]),
    ('Sala', '', [
        ('Rack', ''),
        ('Cristaleira', ''),
        ('Portas', ''),
        ('Painéis', ''),
        ('Finalizar rack', ''),
        ('Instalar rack', ''),
    ]),
]

NITENS = sum(len(a[2]) for a in AMBIENTES)

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

.ident{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin-bottom:10px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold);
  border-radius:2px; padding:6px 8px }
.ident .r{ font-size:7px; letter-spacing:1.3px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:11px; font-weight:700; color:var(--navy); margin-top:2px; min-height:14px }
.ident .v.b{ font-weight:400; color:var(--linha); letter-spacing:1px }

.bloco{ margin-bottom:9px }
.cab{ background:var(--navy); color:#fff; border-radius:2px 2px 0 0;
  padding:5px 10px; display:flex; justify-content:space-between; align-items:center }
.cab .n{ font-size:9.5px; font-weight:700; letter-spacing:1.8px; text-transform:uppercase; color:var(--goldsoft) }
.cab .q{ font-size:8px; color:#b9c3cf }

table.tb{ width:100%; border-collapse:collapse; font-size:9.5px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:7px; font-weight:600;
  letter-spacing:.9px; text-transform:uppercase; padding:4px 8px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:13px 8px; vertical-align:middle }
table.tb tr:nth-child(odd) td{ background:#f7f9fb }
.cx{ display:inline-block; width:12px; height:12px; border:1.4px solid var(--navy);
  border-radius:2px; vertical-align:-2px }
.it{ font-weight:600; color:var(--navy) }
.ob{ font-size:8.5px; color:var(--muted); display:block; margin-top:1px }
.pt i{ display:block; border-bottom:1px dotted #b6bfc9; height:11px }

.fim{ margin-top:auto; border-top:1px solid var(--linha); padding-top:8px;
  display:flex; justify-content:space-between; align-items:flex-end; font-size:8.5px; color:var(--muted) }
"""

def bloco(nome, itens):
    linhas = []
    for titulo, obs in itens:
        o = f'<span class="ob">{obs}</span>' if obs else ''
        linhas.append(
            f'<tr><td style="width:26px"><span class="cx"></span></td>'
            f'<td><span class="it">{titulo}</span>{o}</td>'
            f'<td style="width:165px" class="pt"><i></i></td></tr>')
    return f'''  <div class="bloco">
    <div class="cab"><span class="n">{nome}</span><span class="q">{len(itens)} {"item" if len(itens)==1 else "itens"}</span></div>
    <table class="tb">
      <tr><th style="width:26px">✓</th><th>O que fazer</th><th style="width:165px">Feito por / quando</th></tr>
{chr(10).join(linhas)}
    </table>
  </div>'''

print('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Checklist de finalização — obra Cristiane</title>
__FONTES__
<style>%s</style>
</head>
<body>

<div class="sheet">
  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Finalizações — Obra Cristiane</h1>
      <div class="m">Pendências em aberto · lista de 19/10/2026 · uso interno</div></div>
  </div>

  <div class="ident">
    <div class="c"><div class="r">Obra</div><div class="v">Cristiane</div></div>
    <div class="c"><div class="r">Itens em aberto</div><div class="v">%d</div></div>
    <div class="c"><div class="r">Responsável</div><div class="v b">____________</div></div>
    <div class="c"><div class="r">Início</div><div class="v">19/10/2026</div></div>
  </div>

%s

  <div class="fim">
    <span>Item marcado só depois de conferido no ambiente, com a luz acesa.</span>
    <span>Conferido por ____________________ em ___/___/______</span>
  </div>
</div>

</body>
</html>''' % (CSS, NITENS, '\n'.join(bloco(a[0], a[2]) for a in AMBIENTES)))
