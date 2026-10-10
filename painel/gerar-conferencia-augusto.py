# -*- coding: utf-8 -*-
import importlib.util, os, sys
_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-conferencia-augusto.py')
_sp = importlib.util.spec_from_file_location('dados_conferencia_augusto', _d)
_m = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_m)
GRUPOS = _m.GRUPOS
NITENS = sum(len(g[3]) for g in GRUPOS)

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
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:8px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:23px; font-weight:700; color:var(--navy); line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7px; font-weight:600;
  letter-spacing:2.2px; text-transform:uppercase; color:var(--gold); margin-top:2px }
.doc{ text-align:right }
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:17px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:7.5px; color:var(--muted); letter-spacing:.4px; margin-top:1px }

.ident{ display:grid; grid-template-columns:repeat(4,1fr); gap:5px; margin-bottom:6px }
.ident .c{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:2px; padding:4px 8px }
.ident .r{ font-size:6.6px; font-weight:700; letter-spacing:.7px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:10px; font-weight:700; color:var(--navy); margin-top:1px }

.gr{ display:flex; align-items:center; gap:8px; background:var(--navy); border-radius:2px;
  padding:4px 10px 4px 5px; margin:9px 0 0 }
.gr.crit{ background:var(--red) }
.gr .l{ width:18px; height:18px; flex:0 0 18px; border-radius:50%; background:var(--gold); color:var(--navy);
  font-size:10px; font-weight:800; display:flex; align-items:center; justify-content:center }
.gr.crit .l{ background:#fff; color:var(--red) }
.gr .t{ font-size:9.5px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:var(--goldsoft) }
.gr.crit .t{ color:#fff }
.gr .n{ margin-left:auto; font-size:8px; font-weight:400; letter-spacing:.3px;
  text-transform:none; color:rgba(255,255,255,.6) }

.nota{ font-size:8.5px; color:var(--navy2); background:var(--goldbg); border-left:3px solid var(--gold);
  padding:4px 10px; line-height:1.4 }

table.tb{ width:100%; border-collapse:collapse; font-size:9px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:7px; font-weight:600;
  letter-spacing:.7px; text-transform:uppercase; padding:3px 7px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:4px 7px; vertical-align:top }
table.tb tr:nth-child(even) td{ background:#f8fafb }
.cx{ display:inline-block; width:10px; height:10px; border:1.3px solid var(--navy);
  border-radius:2px; vertical-align:-1px }
.ti{ font-weight:600; color:var(--navy); line-height:1.3 }
.de{ display:block; font-size:8px; color:#45525f; line-height:1.35; margin-top:1px }
.sel{ display:inline-block; font-size:6.5px; font-weight:800; letter-spacing:.6px; text-transform:uppercase;
  background:var(--red); color:#fff; border-radius:7px; padding:1px 5px; margin-right:5px; vertical-align:1px }

.causa{ border:1.5px solid var(--navy); border-radius:3px; overflow:hidden; margin-top:10px }
.causa .cab{ background:var(--navy); color:var(--goldsoft); padding:6px 12px; font-size:9.5px;
  font-weight:700; letter-spacing:1.8px; text-transform:uppercase }
.causa .in{ padding:10px 12px 12px }
.causa p{ margin:0 0 7px; font-size:9.5px; line-height:1.55; color:#33414F }
.causa p:last-child{ margin-bottom:0 }
.causa b{ color:var(--navy) }

.acao{ display:grid; grid-template-columns:1fr 1fr; gap:7px; margin-top:8px }
.acao .c{ border:1px solid var(--linha); border-left:3px solid var(--red); border-radius:2px; padding:7px 10px }
.acao .t{ font-size:9px; font-weight:700; color:var(--navy); margin-bottom:2px }
.acao .d{ font-size:8.5px; color:#45525f; line-height:1.4 }

.assina{ display:grid; grid-template-columns:1fr 1fr; gap:22px; margin-top:12px; margin-bottom:6px }
.assina > div{ border-top:1px solid var(--ink); padding-top:3px; text-align:center }
.assina .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:7.5px; color:var(--muted) }

.rodape{ margin-top:auto; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.4px; text-transform:uppercase }
"""

def topo(n, tot):
    return '''  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><div class="t" style="font-family:'Cormorant Garamond',serif;font-size:17px;font-weight:600;color:var(--navy)">Conferência Técnica — Obra Augusto</div>
    <div class="m">Visita de 10/10/2026 · checklist de resolutivas · folha %d de %d</div></div>
  </div>''' % (n, tot)

def bloco(letra, titulo, nota, itens):
    crit = any(i[2] for i in itens)
    out = ['  <div class="gr%s"><span class="l">%s</span><span class="t">%s</span>'
           '<span class="n">%d %s</span></div>' %
           (' crit' if crit else '', letra, titulo, len(itens), 'item' if len(itens)==1 else 'itens')]
    if nota:
        out.append('  <div class="nota">%s</div>' % nota)
    out.append('  <table class="tb">')
    out.append('    <tr><th style="width:22px">✓</th><th>O que fazer</th>'
               '<th style="width:118px">Feito por / quando</th></tr>')
    for t, d, c in itens:
        sel = '<span class="sel">Crítico</span>' if c else ''
        out.append('    <tr><td><span class="cx"></span></td>'
                   '<td><span class="ti">%s%s</span><span class="de">%s</span></td><td></td></tr>' % (sel, t, d))
    out.append('  </table>')
    return '\n'.join(out)

# paginacao
def alt(itens, nota):
    h = 30 + (22 if nota else 0) + 20
    for t, d, c in itens:
        h += 20 + 11 * (1 + len(d)//92)
    return h

LIM_P1, LIM = 700, 960
pags, atual, usado = [], [], 0
for g in GRUPOS:
    h = alt(g[3], g[2])
    lim = LIM_P1 if not pags and not atual else LIM
    if atual and usado + h > lim:
        pags.append(atual); atual, usado = [], 0
    atual.append(g); usado += h
if atual: pags.append(atual)
TOT = len(pags)

# bloco de causa raiz — entra no pé da última folha de checklist
CAUSA = '''
  <div class="causa">
    <div class="cab">A leitura da visita — por que estes 21 pontos existem</div>
    <div class="in">
      <p>A maior parte do que foi levantado <b>não é defeito de fabricação</b>. São falhas de montagem
      e de acabamento que teriam sido pegas numa conferência antes da liberação para a obra. Frisos sem
      acabamento, marca de lápis não removida, massa de retoque aparente — nada disso precisa de
      segunda visita do cliente para ser descoberto.</p>

      <p><b>Duas causas, nenhuma delas do cliente.</b></p>

      <p><b>1 · Não estamos conferindo antes de liberar.</b> A conferência de liberação existe no papel,
      mas não está sendo feita com atitude. Enquanto o filtro for o olho do cliente na entrega, todo
      detalhe vira retrabalho — e retrabalho em obra custa muito mais caro que conferência na fábrica.</p>

      <p><b>2 · Faltou critério na alocação de quem montou.</b> O profissional alocado como responsável
      pela montagem não tinha o perfil técnico que a obra exigia. Parte do que apareceu aqui não foi
      descuido: foi <b>limite de capacidade técnica</b>. Alocar sem critério transfere para a obra um
      risco que deveria ter sido resolvido na escala.</p>

      <p>Os dois itens marcados como <b>críticos</b> ilustram o ponto: em vez de soltar e refixar o móvel
      fora de nível, usou-se tampa de parafuso para disfarçar. <b>Gambiarra não é solução econômica —
      é dívida.</b> Ela volta, e volta com a confiança do cliente junto.</p>
    </div>
  </div>

  <div class="acao">
    <div class="c"><div class="t">O que muda a partir desta obra</div>
      <div class="d">Nenhum serviço é liberado para a obra sem conferência registrada — com responsável
      e assinatura. Sem a folha preenchida, o carro não sai.</div></div>
    <div class="c"><div class="t">Critério de alocação</div>
      <div class="d">Definir, antes de escalar, o nível técnico que cada obra exige e quem atende a esse
      nível. Obra de alto padrão não aceita montagem de quem ainda está aprendendo sozinho.</div></div>
  </div>

  <div class="acao" style="grid-template-columns:1fr">
    <div class="c" style="border-left-color:var(--gold)"><div class="t">O lado bom disto</div>
      <div class="d">O nível de detalhe exigido nesta obra — calafetar na cor da lâmina, folga mínima,
      friso acabado — é exatamente o que prepara a equipe para serviços mais exigentes e mais rentáveis.
      Resolver bem aqui é treino pago para o próximo degrau.</div></div>
  </div>

  <div class="assina" style="margin-top:auto">
    <div><div class="n">Deivison</div><div class="s">Coordenação de produção · recebido em ___/___/______</div></div>
    <div><div class="n">Jonathan</div><div class="s">Conferência técnica · 10/10/2026</div></div>
  </div>'''

out = ['''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Conferência técnica — obra Augusto</title>
__FONTES__
<style>%s</style>
</head>
<body>''' % CSS]

for pi, pag in enumerate(pags, 1):
    out.append('<div class="sheet">')
    out.append(topo(pi, TOT))
    if pi == 1:
        out.append('''  <div class="ident">
    <div class="c"><div class="r">Obra</div><div class="v">Augusto</div></div>
    <div class="c"><div class="r">Visita</div><div class="v">10/10/2026</div></div>
    <div class="c"><div class="r">Presentes</div><div class="v" style="font-size:9px">Jonathan, cliente e arquiteta</div></div>
    <div class="c"><div class="r">Pontos levantados</div><div class="v">%d</div></div>
  </div>''' % NITENS)
    for g in pag:
        out.append(bloco(g[0], g[1], g[2], g[3]))
    if pi == TOT:
        out.append(CAUSA)
    out.append('''  <div class="rodape"%s><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Conferência técnica · obra Augusto · 10/10/2026</span></div>
</div>''' % (' style="margin-top:12px"' if pi == TOT else ''))

out.append('''
</body>
</html>''')
print('\n'.join(out))
