# -*- coding: utf-8 -*-
"""PROPOSTA DE FECHAMENTO — DOUGLAS  [07/10/2026]

⛔ É PROPOSTA DE FECHAMENTO, NÃO DE APRESENTAÇÃO. [Jonathan 07/10]
   Sem cases, sem linha do tempo, sem "por que a Valvic", sem a página de
   configuração técnica. O cliente já viu tudo isso na v1. Aqui: o que é,
   quanto é, e como fechar.

Números de `calculo-douglas.py`; nada digitado à mão.
⛔⛔ Sem metragem nem quantitativo de peça. Contagem de ENTREGÁVEL
   ("três conjuntos") é escopo e fica.
⛔ Classes novas levam sufixo D.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('dg', P/'calculo-douglas.py')
dg = importlib.util.module_from_spec(spec); sys.modules['dg'] = dg
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(dg)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br2 = lambda v: f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
CLIENTE, DATA = 'Douglas', '7 de outubro de 2026'
PRAZO, VALID  = '60 dias de produção', '5 dias úteis'
NP = 3

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── proposta de fechamento · Douglas ─────────────────────────────────── */
table.invD{width:100%;border-collapse:collapse;margin-top:4mm;font-size:8.8pt;}
table.invD th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.4mm;text-align:left;}
table.invD th.r,table.invD td.r{text-align:right;}
table.invD td{padding:1.9mm 0;border-top:1px solid var(--hair);vertical-align:top;}
table.invD td.c{font-size:7.4pt;letter-spacing:.1em;color:var(--gold-lt);
  font-weight:700;width:20mm;padding-right:3mm;}
table.invD td.i{font-weight:600;}
table.invD td.i span{display:block;font-weight:400;font-size:8pt;
  color:var(--soft);margin-top:.6mm;}
table.invD tr.tot td{border-top:1.6px solid var(--ink);padding-top:3mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;font-weight:700;}
table.invD tr.tot td.c,table.invD tr.tot td.i{font-family:inherit;font-size:9.6pt;}

.cenD{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:5mm;}
.cenD > div{border:1.5px solid var(--line);border-radius:6px;padding:7mm 7mm 6mm;
  display:flex;flex-direction:column;}
.cenD > div.g{border-color:var(--gold);background:rgba(201,169,106,.07);}
.cenD .cod{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cenD .nm{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;
  font-weight:700;line-height:1.1;margin-top:1.5mm;}
.cenD .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;
  font-weight:700;line-height:1;margin-top:5mm;}
.cenD .big small{display:block;font-family:'DM Sans',sans-serif;font-size:7.6pt;
  letter-spacing:.14em;text-transform:uppercase;color:var(--mut);
  font-weight:700;margin-bottom:1.6mm;}
.cenD .mais{font-size:9pt;color:var(--soft);margin-top:4mm;line-height:1.6;}
.cenD .mais b{color:var(--ink);font-weight:700;}
.cenD .sel{margin-top:auto;padding-top:4mm;font-size:8.2pt;color:var(--soft);
  line-height:1.5;}
.cenD .sel b{color:var(--ink);}

.cndD{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm 6mm;margin-top:6mm;
  padding-top:4mm;border-top:1px solid var(--hair);flex:none;}
.cndD .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndD .d{color:var(--soft);font-size:8.2pt;margin-top:1mm;line-height:1.46;}
.cndD .d b{color:var(--ink);}
.notaD{margin-top:4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:8pt;color:var(--soft);line-height:1.5;flex:none;}
.notaD b{color:var(--ink);}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · proposta de fechamento</span>'
            f'<span>{n} / {NP}</span></div>')

# ── 1 · capa ──────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="pad">
  <div class="eyebrow">Proposta de fechamento</div>
  <div class="cv-t serif">Sua agenda,<br>reservada.</div>
  <div class="cv-nome serif" style="font-size:62pt;">{CLIENTE}</div>
  <div class="cv-s">O projeto inteiro, fechado agora — e pago ao longo da
  abertura do seu empreendimento.</div>
  <div class="cv-meta">
    <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
    <div><div class="k">Investimento</div><div class="v">R$ {br(dg.TOTAL)}</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
  </div>
  <div style="margin-top:auto;"><div class="cv-brand">Valvic Marcenaria</div></div>
</div></div>"""

# ── 2 · o investimento ────────────────────────────────────────────────────
DESC = {
 'M01':'Estrutura em MDF Areia, acabamento curvo com duplo acabamento e LED instalado',
 'M02':'MDF Carvalho Malva com acabamento curvo, perfil de LED e perfil metálico',
 'M03':'Prateleiras em MDF Marsala com LED e rack suspenso em Areia com portas ripadas vazadas',
 'M04':'MDF Carvalho Malva com detalhes em Marsala sobre estrutura metálica com pintura automotiva',
 'M05':'MDF Carvalho Malva',
 'M06':'MDF Carvalho Malva Duratex e Marsala Guararapes',
 'M07':'Painel curvo com iluminação embutida em MDF Areia e armário baixo com puxador cava — <b>três conjuntos</b>',
 'M08':'MDF Preto TX com caixa de tomada embutida',
 'M09':'Armário baixo em MDF Areia e prateleiras suspensas em haste de aço com pintura eletrostática',
 'M10/11/13':'Armários sob a bancada em MDF Branco TX com puxador cava',
 'M14':'MDF Areia com iluminação de LED instalada',
}
linhas = ''
for c, n, v, q, _ in dg.ITENS:
    linhas += (f'<tr><td class="c">{c}</td>'
               f'<td class="i">{n}<span>{DESC[c]}</span></td>'
               f'<td class="r">R$ {br(v*q)}</td></tr>')

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O investimento</div>
  <div class="h-sec serif">O projeto inteiro.</div>
  <div class="rule"></div>

  <table class="invD">
    <thead><tr><th></th><th></th><th class="r">Investimento</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="c"></td><td class="i">Investimento total</td>
        <td class="r">R$ {br(dg.TOTAL)}</td></tr>
    </tbody>
  </table>

  <div class="notaD" style="margin-top:auto;"><b>Ferragem e acabamento da
  linha Premium</b>, como especificado: dobradiças Hettich, sistema deslizante
  Rometal, corrediças ocultas com fechamento suave, articuladores premium e
  fita de borda extra fina. <b>Garantia de 10 anos.</b></div>
  {foot(2)}
</div></div>"""

# ── 3 · como fechar ───────────────────────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Como fechar</div>
  <div class="h-sec serif">Duas formas.<br><em>O mesmo valor.</em></div>
  <div class="rule"></div>
  <p class="lead">A entrada reserva sua vaga na produção e o restante acompanha
  a abertura do empreendimento. <b>O investimento é o mesmo nas duas</b> —
  o que muda é só o ritmo.</p>

  <div class="cenD">
    <div>
      <div class="cod">Cenário 1 · cartão</div>
      <div class="nm">Parcela<br>menor</div>
      <div class="big"><small>Entrada</small>R$ {br(dg.VAL_ENT)}</div>
      <div class="mais">e mais<br>
        <b style="font-size:15pt;">10 parcelas de R$ {br2(dg.C1_PARCELA)}</b><br>
        no cartão de crédito</div>
      <div class="sel">Para quem prefere <b>diluir ao máximo</b> o desembolso
      mensal, em dez parcelas a partir do mês seguinte.</div>
    </div>
    <div class="g">
      <div class="cod">Cenário 2 · boleto · recomendado</div>
      <div class="nm">Começa<br>em 60 dias</div>
      <div class="big"><small>Entrada</small>R$ {br(dg.VAL_ENT)}</div>
      <div class="mais">e mais<br>
        <b style="font-size:15pt;">4 boletos de R$ {br(dg.VAL_BOL)}</b><br>
        o primeiro só em 60 dias</div>
      <div class="sel"><b>Cinco pagamentos iguais</b> e nenhum desembolso nos
      dois primeiros meses — começa a pesar só quando o empreendimento já
      estiver de pé.</div>
    </div>
  </div>

  <div class="cndD">
    <div><div class="k">Reserva de agenda</div><div class="d">
      A entrada <b>reserva sua vaga na produção</b>. A data de início é
      combinada na assinatura.</div></div>
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, contados do início da execução.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Validade</div><div class="d">
      <b>{VALID}</b> a partir desta data.</div></div>
    <div><div class="k">Projeto</div><div class="d">
      Medida conferida <b>no local</b> antes do corte.</div></div>
  </div>

  <div class="notaD"><b>Não inclusos:</b> alvenaria, elétrica e hidráulica,
  pintura de parede, gesso, revestimentos, pedras e bancadas, eletrodomésticos,
  luminárias e o mobiliário solto.</div>
  {foot(3)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + '</body></html>')

(P/'proposta-douglas.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-douglas.pdf')], check=True, env=env)
print(f'proposta-douglas.pdf · {NP} páginas')
print(f'  Investimento   R$ {br(dg.TOTAL)}')
print(f'  Cenário 1      entrada {br(dg.VAL_ENT)} + 10 × {br2(dg.C1_PARCELA)}')
print(f'  Cenário 2      entrada {br(dg.VAL_ENT)} + 4 × {br(dg.VAL_BOL)}')
