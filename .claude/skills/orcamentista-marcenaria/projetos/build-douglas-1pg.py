# -*- coding: utf-8 -*-
"""PROPOSTA DE FECHAMENTO — DOUGLAS · FOLHA ÚNICA  [07/10/2026]

⛔ UMA PÁGINA SÓ, autossuficiente. [Jonathan 07/10]
   "documento de uma página só evidenciando a oportunidade com o viés de
    parceria atrelado ao objetivo de fechamento da agenda do ano."
   Não substitui `build-douglas.py` (4 páginas) — é outro instrumento:
   aquele apresenta, este fecha.

⭐ A abertura é a conversa que o Jonathan teve com o cliente, nas palavras
   dele: olhamos além da marcenaria a ser entregue · prezamos pela qualidade
   mas nos importamos com histórias e relacionamentos de longo prazo ·
   entendemos o momento de investimento · é com isso que estruturamos a
   proposta, para viabilizar a execução.

Condição: entrada de 20% + 6 boletos a partir do dia 60 (cenário 3).
Números de `calculo-douglas.py`; nada digitado à mão.
⛔⛔ Sem metragem nem quantitativo de peça.
⛔ Classes novas levam sufixo U.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('dg', P/'calculo-douglas.py')
dg = importlib.util.module_from_spec(spec); sys.modules['dg'] = dg
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(dg)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br2 = lambda v: f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
CLIENTE, DATA = 'Douglas', '7 de outubro de 2026'
VALIDADE      = 'Sexta-feira, 9 de outubro'
PRAZO         = '60 dias de produção'

# vencimentos: 60, 90, 120, 150, 180 e 210 dias — da própria escada
DIAS = [d for d, _ in dg.FLUXO6[1:]]
VENC = ', '.join(str(d) for d in DIAS[:-1]) + f' e {DIAS[-1]}'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── folha única · Douglas ────────────────────────────────────────────── */
/* ⛔ flex:none em TODO bloco fechado: .pad é coluna flex e um box com
      overflow:hidden ENCOLHE em silêncio quando a coluna estoura. */
.topU{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4.5mm;border-bottom:1px solid var(--hair);flex:none;}
.topU .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;letter-spacing:.02em;}
.topU .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}

.leadU{color:var(--soft);font-size:9.2pt;line-height:1.56;flex:none;
  max-width:162mm;}   /* 172mm é medida larga demais para 9,2pt */
.leadU p{margin:0 0 2.6mm;}
.leadU p:last-child{margin-bottom:0;}
.leadU b{color:var(--ink);font-weight:600;}

.escopoU{margin-top:4.5mm;padding:3.6mm 0;border-top:1px solid var(--hair);
  border-bottom:1px solid var(--hair);font-size:8.2pt;color:var(--soft);
  line-height:1.54;flex:none;}
.escopoU b{color:var(--ink);font-weight:600;}

.ofU{margin-top:5mm;border:1.5px solid var(--gold);border-radius:6px;
  background:rgba(201,169,106,.07);padding:6mm;flex:none;}
.ofU .k{font-size:7.2pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.ofU .tot{font-family:'Cormorant Garamond',Georgia,serif;font-size:34pt;
  font-weight:700;line-height:1;margin-top:1.6mm;}
.ofU .sp{height:1px;background:var(--gold-lt);opacity:.55;margin:4.5mm 0 4mm;}
.ofU .duo{display:flex;gap:7mm;align-items:center;}
.ofU .duo > div{flex:1;}
.ofU .duo .x{flex:none;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:19pt;color:var(--gold);font-weight:700;}
.ofU .duo small{display:block;font-size:7.2pt;letter-spacing:.16em;
  text-transform:uppercase;color:var(--mut);font-weight:700;}
.ofU .duo b{display:block;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:23pt;font-weight:700;line-height:1.05;margin-top:1.3mm;}
.ofU .duo em{display:block;font-style:normal;font-size:8.1pt;color:var(--soft);
  margin-top:1mm;}
.ofU .venc{margin-top:4mm;padding-top:3mm;border-top:1px solid var(--hair);
  font-size:8.2pt;color:var(--soft);}
.ofU .venc b{color:var(--ink);font-weight:600;}

.valU{margin-top:5mm;padding:4.2mm 5.5mm;background:var(--ink);color:#fff;
  border-radius:4px;display:flex;align-items:baseline;gap:6mm;flex:none;}
.valU .k{flex:none;font-size:7.2pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;}
.valU .d{flex:none;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:14.5pt;font-weight:700;}
.valU .t{flex:1;font-size:8.1pt;color:#D7D0C3;line-height:1.5;text-align:right;}

.cndU{display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;margin-top:5mm;
  padding-top:3.6mm;border-top:1px solid var(--hair);flex:none;}
.cndU .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndU .d{color:var(--soft);font-size:8.2pt;margin-top:1mm;line-height:1.46;}
.cndU .d b{color:var(--ink);}
.notaU{margin-top:4.5mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.5;flex:none;}
.notaU b{color:var(--ink);}
""")

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<div class="page"><div class="pad">

  <div class="topU">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta de fechamento<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:7mm;" class="eyebrow">Agenda de produção · 2026</div>
  <div class="h-sec serif" style="font-size:27pt;">A sua obra,<br>
    <em>dentro da nossa agenda.</em></div>
  <div class="rule"></div>

  <div class="leadU">
    <p>{CLIENTE}, conforme a conversa que tivemos: somos uma empresa que
    <b>olha além da marcenaria a ser entregue</b>. Prezamos pela qualidade de
    cada entrega — mas o que nos move é <b>construir histórias e
    relacionamentos de longo prazo</b>.</p>

    <p>Entendemos o <b>momento de investimento</b> que a abertura de um
    empreendimento exige. É com essas informações em mãos que estruturamos
    esta proposta: para <b>viabilizar a execução do projeto</b> agora, com o
    desembolso acompanhando a abertura.</p>

    <p>Estamos fechando a agenda de produção do ano, e a sua obra é uma das
    que queremos dentro dela.</p>
  </div>

  <div class="escopoU"><b>O projeto inteiro, como apresentado:</b> balcão de
  recepção, painéis curvos com iluminação embutida, escaninho, prateleiras e
  rack suspenso, carrinho, banco, mesa, armário com prateleiras em haste de
  aço e os armários da copa. Do corte à instalação, com <b>equipe própria</b>
  da casa.</div>

  <div class="ofU">
    <div class="k">O investimento</div>
    <div class="tot">R$ {br(dg.TOTAL)}</div>
    <div class="sp"></div>
    <div class="duo">
      <div><small>Entrada · {dg.ENTRADA*100:.0f}%</small>
        <b>R$ {br(dg.VAL_ENT)}</b><em>na assinatura, reserva de agenda</em></div>
      <div class="x">+</div>
      <div><small>{dg.N_BOL6} boletos de</small>
        <b>R$ {br2(dg.VAL_BOL6)}</b><em>o primeiro só em {dg.DIA_1} dias</em></div>
    </div>
    <div class="venc"><b>Vencimentos</b> em {VENC} dias, contados da
    assinatura. Sem juros e sem acréscimo — o investimento é o mesmo do
    projeto apresentado.</div>
  </div>

  <div class="valU">
    <div class="k">Válida até</div>
    <div class="d">{VALIDADE}</div>
    <div class="t">É o prazo em que a vaga na agenda deste ano<br>
    ainda está reservada para você.</div>
  </div>

  <div class="cndU">
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, contados do início da execução, combinado na
      assinatura.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens, com ferragem Hettich e
      acabamento da linha Premium.</div></div>
    <div><div class="k">Projeto</div><div class="d">
      Medida conferida <b>no local</b> antes do corte.</div></div>
  </div>

  <div class="notaU"><b>Não inclusos:</b> alvenaria, elétrica e hidráulica,
  pintura de parede, gesso, revestimentos, pedras e bancadas, eletrodomésticos,
  luminárias e o mobiliário solto.</div>

  <div class="foot"><span>Valvic Marcenaria</span>
    <span>{CLIENTE} · proposta de fechamento</span>
    <span>{DATA}</span></div>

</div></div>
</body></html>"""

(P/'proposta-douglas-1pagina.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-douglas-1pagina.pdf')],
               check=True, env=env)
print('proposta-douglas-1pagina.pdf · 1 página')
print(f'  Investimento   R$ {br(dg.TOTAL)}')
print(f'  Entrada        R$ {br(dg.VAL_ENT)}  ({dg.ENTRADA*100:.0f}%)')
print(f'  {dg.N_BOL6} boletos de   R$ {br2(dg.VAL_BOL6)}   '
      f'(o último R$ {br2(dg.VAL_BOL6+dg.RESID6)}, fecha os centavos)')
print(f'  Vencimentos    {VENC} dias')
print(f'  Validade       {VALIDADE}')
