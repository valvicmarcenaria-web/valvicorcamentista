# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-valvicorcamentista/3bc82c4c-c807-53cb-9dd2-0a0b402dbf83/scratchpad')
from dados_checklist import SECOES, FECHAMENTO

CSS = """
:root{
  --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea; --cream:#FBFAF7;
}
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:13mm 14mm 12mm; display:flex; flex-direction:column;
  page-break-after:always; overflow:hidden }
.sheet:last-child{ page-break-after:auto }
@media print{ body{ background:#fff } .sheet{ margin:0 } }

/* ---------- capa ---------- */
.capa{ background:radial-gradient(120% 70% at 50% -10%, #1c3a5c 0%, var(--navy) 46%, #0a1526 100%);
  color:var(--cream); padding:0; justify-content:center; align-items:center; text-align:center }
.capa .moldura{ position:absolute; inset:14mm; border:1px solid rgba(194,160,90,.38); border-radius:3px }
.capa .moldura::before,.capa .moldura::after{ content:""; position:absolute; width:26px; height:26px; border:2px solid var(--gold) }
.capa .moldura::before{ top:-1px; left:-1px; border-right:none; border-bottom:none }
.capa .moldura::after{ bottom:-1px; right:-1px; border-left:none; border-top:none }
.capa .in{ position:relative; z-index:2; padding:0 26mm }
.capa .mono{ width:62px; height:62px; margin:0 auto 14px; border:1.6px solid var(--gold); border-radius:6px;
  display:flex; align-items:center; justify-content:center; font-family:'Cormorant Garamond',serif;
  font-weight:700; font-size:32px; color:var(--gold) }
.capa .marca{ font-size:13px; font-weight:700; letter-spacing:5px; text-transform:uppercase; color:#fff }
.capa .marca small{ display:block; font-size:9px; letter-spacing:1.6px; color:rgba(255,255,255,.45); margin-top:5px; font-weight:400; text-transform:none }
.capa h1{ font-family:'Cormorant Garamond',serif; font-weight:700; font-size:52px; line-height:1.04;
  margin:34px 0 0; color:#fff }
.capa h1 span{ color:var(--goldsoft) }
.capa .sub{ font-size:13px; color:rgba(255,255,255,.7); margin-top:14px; line-height:1.6; max-width:118mm; margin-left:auto; margin-right:auto }
.capa .fio{ display:flex; align-items:center; justify-content:center; margin:26px 0 }
.capa .fio .ln{ width:54px; height:1px; background:rgba(194,160,90,.45) }
.capa .fio .d{ width:7px; height:7px; background:var(--gold); transform:rotate(45deg); margin:0 11px }
.capa .porque{ border:1px solid rgba(194,160,90,.3); border-left:3px solid var(--gold); border-radius:3px;
  padding:14px 18px; text-align:left; font-size:11px; line-height:1.62; color:rgba(255,255,255,.8); background:rgba(255,255,255,.03) }
.capa .porque b{ color:var(--goldsoft) }
.capa .passos{ display:grid; grid-template-columns:repeat(3,1fr); gap:9px; margin-top:16px }
.capa .passo{ border:1px solid rgba(255,255,255,.14); border-radius:3px; padding:11px 10px; text-align:left }
.capa .passo .n{ font-family:'Cormorant Garamond',serif; font-size:20px; font-weight:700; color:var(--gold); line-height:1 }
.capa .passo .t{ font-size:9.5px; line-height:1.45; color:rgba(255,255,255,.72); margin-top:5px }
.capa .assina{ margin-top:30px; font-size:10px; color:rgba(255,255,255,.45); letter-spacing:.4px }
.capa .assina b{ color:var(--goldsoft); font-weight:600 }

/* ---------- miolo ---------- */
.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:8px }
.marca2{ font-family:'Cormorant Garamond',serif; font-size:21px; font-weight:700; color:var(--navy); line-height:1 }
.marca2 small{ display:block; font-family:'Inter',sans-serif; font-size:7px; font-weight:600;
  letter-spacing:2.2px; text-transform:uppercase; color:var(--gold); margin-top:2px }
.doc{ text-align:right }
.doc .t{ font-family:'Cormorant Garamond',serif; font-size:15px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:7.5px; color:var(--muted); letter-spacing:.4px; margin-top:1px }

.sec{ display:flex; align-items:center; gap:9px; background:var(--navy); border-radius:2px;
  padding:4px 10px 4px 5px; margin:9px 0 0 }
.sec .n{ width:19px; height:19px; flex:0 0 19px; border-radius:50%; background:var(--gold); color:var(--navy);
  font-size:10px; font-weight:800; display:flex; align-items:center; justify-content:center;
  font-family:'Inter',sans-serif }
.sec .t{ font-size:9.5px; font-weight:700; letter-spacing:1.9px; text-transform:uppercase; color:var(--goldsoft) }

.it{ display:flex; align-items:baseline; gap:8px; padding:4.1px 2px 0; border-bottom:1px solid #eef1f4 }
.it .cx{ width:10px; height:10px; flex:0 0 10px; border:1.3px solid var(--navy); border-radius:2px; position:relative; top:1px }
.it .q{ font-size:9.3px; color:var(--ink); line-height:1.3; white-space:nowrap }
.it .ln{ flex:1; border-bottom:1px dotted #b9c2cc; margin-bottom:2px; min-width:26px }
.it.wrap .q{ white-space:normal }

.nota{ display:flex; align-items:flex-start; gap:8px; background:var(--goldbg); border-left:3px solid var(--gold);
  border-radius:2px; padding:5px 10px; margin:3px 0 1px }
.nota .et{ font-size:7px; font-weight:800; letter-spacing:.9px; text-transform:uppercase; color:var(--navy);
  background:var(--gold); border-radius:8px; padding:1.5px 6px; flex:0 0 auto; position:relative; top:1px }
.nota .tx{ font-size:9px; color:var(--navy2); line-height:1.4 }

.encerra{ flex:1; display:flex; flex-direction:column; justify-content:center; gap:12px }
.fecha{ border:1.5px solid var(--navy); border-radius:3px; overflow:hidden }
.fecha .cab{ background:var(--navy); color:var(--goldsoft); padding:10px 16px; font-size:11px; font-weight:700;
  letter-spacing:1.9px; text-transform:uppercase }
.fecha .in{ padding:14px 16px 16px }
.fecha .intro{ font-size:10.5px; color:var(--muted); line-height:1.55; margin:0 0 12px }
.fecha .grade{ display:grid; grid-template-columns:1fr 1fr; gap:4px 22px }
.fecha .li{ display:flex; align-items:baseline; gap:9px; font-size:11px; color:var(--ink); padding:6.5px 0;
  border-bottom:1px solid #eef1f4 }
.fecha .li .d{ width:5px; height:5px; flex:0 0 5px; background:var(--gold); transform:rotate(45deg) }

.enc{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:3px; padding:14px 16px }
.enc .t{ font-size:11.5px; font-weight:700; color:var(--navy); margin-bottom:5px }
.enc .tx{ font-size:10.5px; color:#33414F; line-height:1.6 }
.enc .tx b{ color:var(--navy) }

.ident{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:7px; margin-bottom:3px }
.ident .c{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:2px; padding:5px 9px }
.ident .r{ font-size:6.8px; font-weight:700; letter-spacing:.8px; text-transform:uppercase; color:var(--muted) }
.ident .v{ border-bottom:1px dotted #b9c2cc; height:13px; margin-top:2px }

.rodape{ margin-top:auto; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.4px; text-transform:uppercase }
"""

CURTA = 58  # perguntas ate este tamanho ficam na mesma linha do tracejado

def item_html(tipo, txt):
    if tipo == 'n':
        return ('<div class="nota"><span class="et">Padrão Valvic</span>'
                '<span class="tx">%s</span></div>' % txt)
    cls = 'it' if len(txt) <= CURTA else 'it wrap'
    return '<div class="%s"><span class="cx"></span><span class="q">%s</span><span class="ln"></span></div>' % (cls, txt)

def altura(tipo, txt):
    if tipo == 'n':
        return 23 + (14 if len(txt) > 78 else 0)
    return 16 if len(txt) <= CURTA else 28

# ---- paginacao: distribui as secoes pelas folhas do miolo
ALTURA_UTIL   = 920   # px aproximados de area util numa folha do miolo
ALTURA_P1     = 830   # a primeira folha do miolo tem o bloco de identificacao
CAB_SECAO     = 32

paginas, atual, usado = [], [], 0
for i, (titulo, itens) in enumerate(SECOES, 1):
    h = CAB_SECAO + sum(altura(t, x) for t, x in itens)
    limite = ALTURA_P1 if not paginas and not atual else ALTURA_UTIL
    if atual and usado + h > limite:
        paginas.append(atual); atual, usado = [], 0
    atual.append((i, titulo, itens)); usado += h
if atual: paginas.append(atual)

TOT = len(paginas) + 2   # capa + miolo + folha final

out = []
out.append('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Checklist de liberação de projeto — Valvic Marcenaria</title>
__FONTES__
<style>%s</style>
</head>
<body>''' % CSS)

# ---------- CAPA ----------
out.append('''
<div class="sheet capa">
  <div class="moldura"></div>
  <div class="in">
    <div class="mono">V</div>
    <div class="marca">Valvic Marcenaria<small>Vargas Decor Ltda · Belo Horizonte / MG</small></div>

    <h1>Checklist de<br><span>Liberação de Projeto</span></h1>
    <div class="sub">O roteiro de conferência que o projeto percorre antes de entrar na marcenaria.
    Para arquitetos, decoradores e parceiros da Valvic.</div>

    <div class="fio"><span class="ln"></span><span class="d"></span><span class="ln"></span></div>

    <div class="porque">
      Projeto que entra completo <b>sai no prazo</b>. A maior parte das interrupções de fabricação não
      nasce na fábrica — nasce de uma definição que ficou em aberto e só aparece na hora do corte.
      Quando isso acontece, o projeto para, volta para a prancheta e todo mundo perde tempo.
      <b>Este checklist existe para que essa conversa aconteça antes</b>, enquanto ainda é barata e rápida.
    </div>

    <div class="passos">
      <div class="passo"><div class="n">1</div><div class="t">Percorra as 13 seções com o projeto aberto, antes de enviar.</div></div>
      <div class="passo"><div class="n">2</div><div class="t">Marque o que está resolvido e anote a definição ao lado.</div></div>
      <div class="passo"><div class="n">3</div><div class="t">O que ficar em aberto, alinhe com a nossa equipe de projeto.</div></div>
    </div>

    <div class="assina">Elaborado por <b>Bruna</b> · Arquitetura e Projeto · Valvic Marcenaria</div>
  </div>
</div>''')

# ---------- MIOLO ----------
for pi, pag in enumerate(paginas, 1):
    out.append('<div class="sheet">')
    out.append('''  <div class="topo">
    <div class="marca2">valvic<small>Marcenaria</small></div>
    <div class="doc"><div class="t">Checklist de Liberação de Projeto</div>
    <div class="m">Para arquitetos, decoradores e parceiros · folha %d de %d</div></div>
  </div>''' % (pi + 1, TOT))
    if pi == 1:
        out.append('''  <div class="ident">
    <div class="c"><div class="r">Projeto / cliente</div><div class="v"></div></div>
    <div class="c"><div class="r">Arquiteto(a) responsável</div><div class="v"></div></div>
    <div class="c"><div class="r">Data da conferência</div><div class="v"></div></div>
  </div>''')
    for n, titulo, itens in pag:
        out.append('  <div class="sec"><span class="n">%d</span><span class="t">%s</span></div>' % (n, titulo))
        for t, x in itens:
            out.append('  ' + item_html(t, x))
    out.append('''  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Checklist de liberação de projeto</span></div>
</div>''')

# ---------- FOLHA FINAL ----------
grade = '\n'.join('      <div class="li"><span class="d"></span><span>%s</span></div>' % x for x in FECHAMENTO)
out.append('''
<div class="sheet">
  <div class="topo">
    <div class="marca2">valvic<small>Marcenaria</small></div>
    <div class="doc"><div class="t">Checklist de Liberação de Projeto</div>
    <div class="m">Para arquitetos, decoradores e parceiros · folha %d de %d</div></div>
  </div>

  <div class="encerra">
  <div class="fecha">
    <div class="cab">O que precisa estar explícito no detalhamento</div>
    <div class="in">
      <p class="intro">Estes itens não são pergunta — são o que a fábrica lê para cortar. Quando algum deles
      falta, a peça não entra em produção até a dúvida voltar resolvida.</p>
      <div class="grade">
%s
      </div>
    </div>
  </div>

  <div class="enc">
    <div class="t">Projeto conferido. E agora?</div>
    <div class="tx">Envie o projeto com este checklist preenchido. Os pontos que ficaram em aberto não
    impedem o envio — <b>só precisam vir sinalizados</b>, para que a nossa equipe de projeto resolva com você
    antes do corte, e não durante.</div>
  </div>

  <div class="enc" style="border-left-color:var(--navy)">
    <div class="t">Fale com a gente</div>
    <div class="tx">Equipe de Projeto · Valvic Marcenaria<br>
    <b>(31) 98524-8046</b> · Belo Horizonte / MG</div>
  </div>
  </div>

  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Construindo Legado</span></div>
</div>

</body>
</html>''' % (TOT, TOT, grade))

print('\n'.join(out))
