# -*- coding: utf-8 -*-
"""REGINA — proposta · home office  [20/10/2026]

⭐ Segue a ordem que o Jonathan fixou em 19/10: **nenhum preço antes de
   gerar valor**. Empresa e processo primeiro, o projeto item a item
   depois, e o investimento só na última página.

⛔ A ÚNICA IMAGEM É A REFERÊNCIA QUE A PRÓPRIA CLIENTE MANDOU, recortada
   do print de WhatsApp. Vai nomeada como referência dela — não como
   render nosso, que não existe.

Números de `corte-regina-home-office.py`; nada digitado à mão.
⛔ Sem metragem e sem contagem de peça nas descrições.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('rg', P/'corte-regina-home-office.py')
rg = importlib.util.module_from_spec(spec); sys.modules['rg'] = rg
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(rg)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA, DATA = 'Regina', 'Home office', '20 de outubro de 2026'
PRAZO, VALIDADE, GARANTIA = '60 dias corridos', '7 dias úteis', rg.GARANTIA
TOT, DESC = rg.TOTAL, 0.07
VISTA = round(TOT*(1 - DESC)/10)*10
NP = 4
REF = ('data:image/jpeg;base64,'
       + base64.b64encode((P/'img-regina-referencia.jpg').read_bytes()).decode())

ITENS = [
 ('Mesa', 'Tampo em MDF melamínico com a <b>espessura aparente de cinco '
  'centímetros</b> que você pediu — face e testeira montadas em caixa, '
  'sobre alma interna. '
  'Apoiada no gaveteiro de um lado e em lateral do outro.'),
 ('Gaveteiro', 'Gavetas pequenas e <b>gaveta arquivo</b>, todas sobre '
  '<b>corrediça oculta Hettich</b>, com amortecimento. Frentes em MDF '
  'melamínico e puxador em barra preta.'),
 ('Móvel do PC', 'Nicho acoplado sob o tampo, para o computador sair do '
  'chão e os cabos ficarem guiados.'),
 ('Painel', 'No fundo da bancada, na mesma espessura aparente da mesa, '
  'com os <b>recortes das tomadas</b> previstos na peça e a fiação '
  'passando por trás.'),
 ('Prateleira', 'Fecha o painel por cima, na mesma espessura aparente, '
  'sobre <b>suporte oculto</b> — sem mão-francesa à vista.'),
]
ETAPAS = [
 ('Medição', 'Vamos ao local antes de cortar. É a medição que confirma os '
  'comprimentos e trava o corte.'),
 ('Detalhamento', 'Compatibilizamos a marcenaria com a elétrica antes do '
  'corte: é o que faz o recorte da tomada cair no lugar certo.'),
 ('Corte', 'CNC próprio, com furação oculta — a cavilha só aparece onde '
  'ninguém vê, e a face fica limpa.'),
 ('Montagem', 'Equipe nossa, não terceirizada. Quem monta responde pelo que '
  'cortou.'),
 ('Entrega', 'Regulagem de cada gaveta e a marcenaria pronta para a elétrica '
  'ligar as tomadas.'),
]
# ⛔⛔ TRAVAS
assert set(i for i, _ in ITENS) == set(rg.MOVEIS), (
    f'⛔ A PROPOSTA NÃO COBRE OS MESMOS MÓVEIS DO MOTOR: '
    f'{set(i for i, _ in ITENS) ^ set(rg.MOVEIS)}')
assert abs(sum(rg.PV[i] for i, _ in ITENS) - TOT) < 0.5, '⛔ O TOTAL NÃO FECHA'
assert abs(rg.MC_ALVO - 0.35) < 1e-9, f'⛔ A MC MUDOU: {rg.MC_ALVO:.3f}'
assert rg.RT_ON is False,           '⛔ ENTROU RT [Jonathan pediu SEM]'
assert rg.CORR_OC == 190.0,         '⛔ A CORREDIÇA NÃO É MAIS A HETTICH'
assert VISTA == round(TOT*(1-DESC)/10)*10, '⛔ O À VISTA NÃO FECHA'

CSS = """
:root{
  --ink:#1E1B17; --soft:#5E574E; --mut:#9A9287; --line:#E0D8CB;
  --hair:#EFE9DF; --sand:#F6F1E8; --wood:#A8794A; --wood-lt:#D9BD96;
  --dk:#262220; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.5pt;line-height:1.55;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:15mm 17mm 14mm;height:100%;display:flex;flex-direction:column;}
.foot{margin-top:auto;padding-top:6mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:6.8pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.4px solid var(--ink);padding-bottom:3mm;flex:none;}
.hd .b{font-size:7.6pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:6.8pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--wood);font-weight:700;margin-top:5mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;
  line-height:1.03;font-weight:600;letter-spacing:-.02em;margin-top:1.5mm;flex:none;}
.lead{color:var(--soft);font-size:9.6pt;line-height:1.5;margin-top:3mm;
  max-width:134mm;flex:none;}
.lead b{color:var(--ink);font-weight:600;}

.cv{height:297mm;display:flex;flex-direction:column;}
.cv .ph{flex:1;overflow:hidden;line-height:0;background:#000;}
.cv .ph img{width:100%;height:100%;object-fit:cover;}
.cv .cap{position:absolute;right:17mm;color:#fff;font-size:6.6pt;
  letter-spacing:.2em;text-transform:uppercase;opacity:.7;}
.cv .bt{background:var(--dk);color:#F4EFE6;padding:13mm 17mm 12mm;flex:none;}
.cv .mark{font-size:8pt;letter-spacing:.42em;text-transform:uppercase;
  color:#EFE6D6;font-weight:700;}
.cv h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:42pt;
  line-height:1;font-weight:600;letter-spacing:-.02em;margin:5mm 0 0;}
.cv .sub{font-size:10.5pt;color:#C6BDB0;margin-top:4mm;font-weight:300;}
.cv .sub b{color:#EFE7DA;font-weight:500;}

.step{display:grid;grid-template-columns:9mm 1fr;gap:4mm;padding:5mm 0;
  border-top:1px solid var(--line);}
.step:first-of-type{border-top:1.4px solid var(--ink);}
.step .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:700;color:var(--wood-lt);line-height:.9;}
.step .t{font-size:10.5pt;font-weight:600;}
.step .d{color:var(--soft);font-size:8.4pt;line-height:1.42;margin-top:.8mm;}
.sel{background:var(--sand);border-radius:3px;padding:9mm;flex:none;}
.sel .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.sel .d{color:var(--soft);font-size:8.8pt;line-height:1.5;margin-top:2mm;}
.sel .d b{color:var(--ink);font-weight:600;}
.gar{display:grid;grid-template-columns:34mm 1fr;gap:7mm;align-items:baseline;
  margin-top:6mm;padding-top:5mm;border-top:1.4px solid var(--ink);flex:none;}
.gar .g{font-family:'Cormorant Garamond',Georgia,serif;font-size:40pt;
  font-weight:700;line-height:.9;letter-spacing:-.02em;}
.gar .gl{font-size:7pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;margin-top:1.5mm;}
.gar .d{color:var(--soft);font-size:9pt;line-height:1.5;}
.gar .d b{color:var(--ink);font-weight:600;}

.ph2{margin:6mm -17mm 0;line-height:0;flex:none;}
.ph2 img{width:100%;height:86mm;object-fit:cover;display:block;}
.ph2 .c{padding:2mm 17mm 0;font-size:6.6pt;letter-spacing:.2em;
  text-transform:uppercase;color:var(--mut);font-weight:700;}
.li{padding:4.6mm 0 4.6mm 5mm;border-left:2px solid var(--wood-lt);
  margin-bottom:3.4mm;break-inside:avoid;}
.li .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  font-weight:600;line-height:1.1;letter-spacing:-.01em;}
.li .d{color:var(--soft);font-size:8.6pt;line-height:1.45;margin-top:1.2mm;}
.li .d b{color:var(--ink);font-weight:600;}

.rows{margin-top:6mm;flex:none;}
.row{display:flex;justify-content:space-between;align-items:baseline;
  padding:2.8mm 0;border-top:1px solid var(--line);font-size:10pt;}
.row:first-child{border-top:1.4px solid var(--ink);}
.row .v{font-variant-numeric:tabular-nums;font-weight:600;}
.vista{margin-top:6mm;background:var(--dk);color:#F4EFE6;border-radius:3px;
  padding:8mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.vista .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--wood-lt);font-weight:700;}
.vista .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:40pt;
  font-weight:700;color:#fff;line-height:.9;letter-spacing:-.03em;
  margin-top:3mm;font-variant-numeric:tabular-nums;}
.vista .s{font-size:8.8pt;color:#C2BAAD;margin-top:3mm;max-width:92mm;}
.vista .rt{text-align:right;flex:none;}
.vista .rt .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:#8E867A;font-weight:700;}
.vista .rt .v{font-size:15pt;color:#B6AEA1;margin-top:1.5mm;
  font-variant-numeric:tabular-nums;}
.pay{margin-top:5mm;flex:none;}
.pay .r{display:flex;justify-content:space-between;align-items:baseline;gap:6mm;
  padding:2.4mm 0;border-top:1px solid var(--line);font-size:9pt;color:var(--soft);}
.pay .r:first-child{border-top:1.4px solid var(--ink);}
.pay .r b{color:var(--ink);font-weight:600;}
.pay .r .x{flex:none;font-size:8.4pt;color:var(--wood);font-weight:700;}
.pay .r.on{color:var(--ink);}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:5mm;
  padding-top:4mm;border-top:1px solid var(--line);flex:none;}
.four .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.four .v{font-size:11pt;font-weight:600;margin-top:1.2mm;}
.notes{margin-top:5mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;
  flex:none;}
.notes .bx{background:var(--sand);border-radius:3px;padding:5.5mm 6mm;}
.notes .bx.w{background:#fff;border:1px solid var(--line);}
.notes .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.notes .d{color:var(--soft);font-size:8pt;line-height:1.45;margin-top:2mm;}
.notes .d b{color:var(--ink);font-weight:600;}
"""

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · {OBRA}</span><span>{n} / {NP}</span></div>')
def head():
    return (f'<div class="hd"><div class="b">Valvic Marcenaria</div>'
            f'<div class="m">{CLIENTE} · {DATA}</div></div>')

steps = ''.join(f'<div class="step"><div class="n serif">{i:02d}</div>'
                f'<div><div class="t">{t}</div><div class="d">{d}</div></div>'
                f'</div>' for i, (t, d) in enumerate(ETAPAS, 1))
lis = ''.join(f'<div class="li"><div class="t">{t}</div>'
              f'<div class="d">{rg and d}</div></div>' for t, d in ITENS)
rows = ''.join(f'<div class="row"><span>{t}</span>'
               f'<span class="v">{br(rg.PV[t])}</span></div>' for t, _d in ITENS)

p1 = f"""<div class="page"><div class="cv">
  <div class="ph"><img src="{REF}" alt=""></div>
  <div class="bt">
    <div class="mark">Valvic Marcenaria</div>
    <h1>Home<br>office.</h1>
    <div class="sub"><b>{CLIENTE}</b> · {OBRA}<br>Sobre a referência que
    você nos enviou</div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Quem faz</div>
  <div class="h1 serif">Marcenaria própria,<br>do corte à regulagem.</div>
  <div class="lead">A Valvic é marcenaria de <b>fábrica própria em Belo
  Horizonte</b>. Corte, montagem e instalação saem da mesma casa — entre a
  medição e a última gaveta regulada <b>não entra terceiro nenhum</b>.</div>
  <div style="margin-top:6mm;flex:none;">{steps}</div>

  <div class="gar" style="margin-top:8mm;">
    <div><div class="g serif">{GARANTIA}</div>
      <div class="gl">de garantia</div></div>
    <div class="d">As gavetas correm em <b>corrediça oculta Hettich</b>,
    alemã, com amortecimento: o trilho some por baixo, a gaveta abre
    inteira e não mostra ferragem na lateral. É a peça que decide se o
    móvel ainda fecha bem no décimo ano — e é por isso que o prazo de
    garantia é esse.</div>
  </div>

  <div class="sel" style="margin-top:6mm;">
    <div class="k">A espessura aparente</div>
    <div class="d">A mesa, o painel e a prateleira têm <b>a espessura
    robusta que você pediu</b>. Nós a construímos em <b>caixa</b> — face e
    testeira montadas sobre alma interna — e não empilhando chapa: o
    desenho é o mesmo, o móvel fica <b>leve o bastante para a parede
    segurar</b> e a borda sai sem emenda à vista.</div>
  </div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">O projeto</div>
  <div class="h1 serif">Peça por peça.</div>
  <div class="ph2"><img src="{REF}" alt="">
    <div class="c">Referência enviada por você</div></div>
  <div style="margin-top:5mm;flex:none;">{lis}</div>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento</div>
  <div class="h1 serif">O conjunto.</div>
  <div class="rows">{rows}
    <div class="row"><b>Total</b><span class="v">R$ {br(TOT)}</span></div>
  </div>
  <div class="vista">
    <div><div class="lab">À vista · {DESC:.0%} de desconto</div>
      <div class="big">R$ {br(VISTA)}</div>
      <div class="s">Entrada e saldo por transferência, sem cartão —
      devolvemos a taxa que deixamos de pagar.</div></div>
    <div class="rt"><div class="k">Valor cheio</div>
      <div class="v">R$ {br(TOT)}</div></div>
  </div>
  <div class="pay">
    <div class="r on"><div>Entrada <b>70%</b> + saldo por transferência</div>
      <div class="x">−{DESC:.0%} · R$ {br(VISTA)}</div></div>
    <div class="r"><div>Entrada <b>70%</b> + saldo em até seis vezes no cartão</div>
      <div class="x">−5%</div></div>
    <div class="r"><div>Entrada <b>50%</b> + saldo em até oito vezes no cartão</div>
      <div class="x">−3%</div></div>
    <div class="r"><div>Entrada <b>30%</b> + saldo em até dez vezes no cartão</div>
      <div class="x">R$ {br(TOT)}</div></div>
  </div>
  <div class="four">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Garantia</div><div class="v">{GARANTIA}</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
  <div class="notes">
    <div class="bx"><div class="k">O que não está incluso</div>
      <div class="d">A <b>elétrica</b> — ponto, circuito, tomada e
      interruptor. Deixamos os <b>recortes prontos</b> no painel. O
      <b>computador, o monitor e o suporte</b>. A <b>cadeira</b>, o
      <b>sofá</b>, o <b>tapete</b> e a <b>cortina</b>. <b>Pintura, piso e
      forro.</b></div></div>
    <div class="bx w"><div class="k">A confirmar antes da produção</div>
      <div class="d">A <b>medição no local</b>, que trava o corte. O
      <b>padrão do MDF</b>, com amostra aprovada por você. E a
      <b>posição das tomadas</b>, para os recortes caírem no lugar
      certo.</div></div>
  </div>
  {foot(NP)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + p4 + '</body></html>')
# ⛔⛔ nenhum preço antes da página do investimento
assert 'R$' not in (p1 + p2 + p3), '⛔⛔ TEM PREÇO ANTES DA PÁGINA DE VALOR'

(P/'proposta-regina.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-regina.pdf')],
               check=True, env=env)
print(f'proposta-regina.pdf · {NP} páginas · '
      f'{(P/"proposta-regina.pdf").stat().st_size//1024} kB')
for t, _d in ITENS: print(f'  {t:<16} R$ {br(rg.PV[t]):>7}')
print(f'  {"TOTAL":<16} R$ {br(TOT):>7}')
print(f'  {"À VISTA −"+f"{DESC:.0%}":<16} R$ {br(VISTA):>7}')
