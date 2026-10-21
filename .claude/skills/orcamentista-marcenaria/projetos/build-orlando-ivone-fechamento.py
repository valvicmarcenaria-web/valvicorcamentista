# -*- coding: utf-8 -*-
"""ORLANDO E IVONE — folha de fechamento  [21/10/2026]

⭐ [Jonathan 21/10] A arquiteta: *"eles vão fechar com vocês com 50% de
   entrada e restante no cartão de 6×. Você atualiza pra mim?"* —
   "aplique o desconto de 5% e gere uma nova proposta com os valores e
   informações importantes, tudo em uma única página."

⚠ A ESCADA DA CASA DARIA 3% NESSA CONDIÇÃO, NÃO 5%: 50% de entrada + 8× no
  cartão vale 3%; os 5% são de 70% de entrada + 6×. Eles estão pedindo a
  entrada menor E as parcelas menores. ⭐ O Jonathan mandou dar os 5% — é
  decisão dele, registrada aqui e no dossiê.

⛔⛔ VALOR DE ITEM NÃO SE MEXE (regra de 21/10). Os dois móveis mantêm os
   números da proposta Premium: R$ 5.020 e R$ 7.640. O desconto incide
   sobre o TOTAL e aparece como linha própria — o cliente vê de onde saiu.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('oi', P/'corte-orlando-ivone.py')
oi = importlib.util.module_from_spec(spec); sys.modules['oi'] = oi
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(oi)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br2 = lambda v: f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
CLIENTE, DATA = 'Orlando e Ivone', '21 de outubro de 2026'
ARQ = 'Ana Maria Castro'
V = oi.VERSAO['premium']
PRAZO, GARANTIA, VALIDADE = V['prazo'], V['garantia'], '7 dias úteis'

ITENS = [
 ('Sob a bancada', 'Armário inferior',
  'Frente em amadeirado fosco, caixaria em branco. Portas de giro e '
  'gavetas sobre <b>corrediça oculta Hettich</b>, com amortecimento. '
  'Puxador Zen Phenix cromado.',
  oi.PREMIUM['PV']['Armário inferior']),
 ('Espelheira', 'Armário superior, com espelho',
  'Folhas em <b>espelho prata</b> com perfil de alumínio, fornecidas e '
  'alinhadas por nós. Interior em branco, com prateleiras.',
  oi.PREMIUM['PV']['Armário superior']),
]
BRUTO = sum(i[3] for i in ITENS)
DESC  = 0.05                      # ⭐ [Jonathan 21/10]
LIQ   = round(BRUTO*(1 - DESC), 2)
ENTRADA = round(LIQ/2, 2)
N_PARC  = 6
PARCELA = round((LIQ - ENTRADA)/N_PARC, 2)

# ⛔⛔ TRAVAS
assert BRUTO == oi.PREMIUM['TOT'] == 12660, f'⛔ O BRUTO MUDOU: {BRUTO}'
assert abs(ENTRADA + PARCELA*N_PARC - LIQ) < 0.05, '⛔ O PARCELAMENTO NÃO FECHA'
assert V['prazo'] == '50 dias corridos', '⛔ O PRAZO MUDOU'

def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-orlando-ivone'/n).read_bytes()).decode())
IMG = uri('render-geral.jpg')

CSS = """
:root{--ink:#1C1A17;--soft:#5C564E;--mut:#948D83;--line:#DFD8CB;
      --hair:#EEE8DE;--sand:#F6F2EA;--ac:#A07C4B;--ac-lt:#D7BC92;--dk:#262220;}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.3pt;line-height:1.5;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;background:#fff;}
.pad{padding:12mm 16mm 12mm;height:100%;display:flex;flex-direction:column;}
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.4px solid var(--ink);padding-bottom:3mm;flex:none;}
.hd .b{font-size:7.6pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:6.6pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;line-height:1.5;}
.eye{font-size:6.6pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--ac);font-weight:700;margin-top:4mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
  line-height:1.03;font-weight:600;letter-spacing:-.02em;margin-top:1.5mm;flex:none;}
.ph{margin:4mm -16mm 0;line-height:0;flex:none;}
.ph img{width:100%;height:32mm;object-fit:cover;display:block;}
.it{display:grid;grid-template-columns:24mm 1fr 26mm;gap:5mm;
  padding:3mm 0;border-top:1px solid var(--line);align-items:baseline;flex:none;}
.it:first-of-type{border-top:1.4px solid var(--ink);margin-top:6mm;}
.it .k{font-size:6.4pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ac);font-weight:700;}
.it .t{font-size:10.4pt;font-weight:600;}
.it .d{color:var(--soft);font-size:7.6pt;line-height:1.38;margin-top:.8mm;}
.it .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  font-weight:700;text-align:right;font-variant-numeric:tabular-nums;}
.sum{margin-top:4mm;flex:none;}
.sum .r{display:flex;justify-content:space-between;align-items:baseline;
  padding:1.7mm 0;font-size:9.6pt;color:var(--soft);}
.sum .r b{color:var(--ink);font-weight:600;}
.sum .r.d{color:var(--ac);font-weight:600;}
.band{margin-top:4mm;background:var(--dk);color:#F4EFE6;border-radius:3px;
  padding:6mm 7mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.band .lab{font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--ac-lt);font-weight:700;}
.band .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:33pt;
  font-weight:700;color:#fff;line-height:.92;letter-spacing:-.03em;
  margin-top:2mm;font-variant-numeric:tabular-nums;}
.band .s{font-size:8.6pt;color:#C2BAAD;margin-top:2.4mm;}
.band .rt{text-align:right;flex:none;}
.band .rt .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:#8E867A;font-weight:700;}
.band .rt .v{font-size:13pt;color:#B6AEA1;margin-top:1.2mm;
  text-decoration:line-through;font-variant-numeric:tabular-nums;}
.pay{margin-top:5mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;flex:none;}
.pay .c{border:1px solid var(--line);border-radius:3px;padding:4.6mm 5.5mm;}
.pay .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--ac);font-weight:700;}
.pay .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;
  font-weight:700;margin-top:1.5mm;line-height:1;font-variant-numeric:tabular-nums;}
.pay .s{color:var(--soft);font-size:7.8pt;margin-top:1.2mm;line-height:1.36;}
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:4mm;
  padding-top:3.4mm;border-top:1.4px solid var(--ink);flex:none;}
.four .k{font-size:6.4pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--ac);font-weight:700;}
.four .v{font-size:10.6pt;font-weight:600;margin-top:1.2mm;}
.four .s{color:var(--soft);font-size:7.4pt;margin-top:.6mm;line-height:1.35;}
.notes{margin-top:4mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;flex:none;}
.notes .bx{background:var(--sand);border-radius:3px;padding:4.4mm 5mm;}
.notes .bx.w{background:#fff;border:1px solid var(--line);}
.notes .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--ac);font-weight:700;}
.notes .d{color:var(--soft);font-size:7.1pt;line-height:1.34;margin-top:1.4mm;}
.notes .d b{color:var(--ink);font-weight:600;}
.foot{margin-top:auto;padding-top:5mm;border-top:1px solid var(--hair);
  display:flex;justify-content:space-between;font-size:6.6pt;
  letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}
"""

itens = ''.join(
 f'<div class="it"><div class="k">{k}</div>'
 f'<div><div class="t">{t}</div><div class="d">{d}</div></div>'
 f'<div class="v">{br(v)}</div></div>' for k, t, d, v in ITENS)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="page"><div class="pad">
  <div class="hd"><div class="b">Valvic Marcenaria</div>
    <div class="m">{CLIENTE} · Banho suíte master<br>{DATA}</div></div>
  <div class="eye">Fechamento</div>
  <div class="h1 serif">Banho suíte master.</div>
  <div class="ph"><img src="{IMG}" alt=""></div>

  {itens}

  <div class="sum">
    <div class="r"><span>Soma dos móveis</span>
      <span><b>R$ {br2(BRUTO)}</b></span></div>
    <div class="r d"><span>Desconto da condição de pagamento · {DESC:.0%}</span>
      <span>− R$ {br2(BRUTO - LIQ)}</span></div>
  </div>

  <div class="band">
    <div><div class="lab">Investimento</div>
      <div class="big">R$ {br2(LIQ)}</div>
      <div class="s">Com o desconto já aplicado.</div></div>
    <div class="rt"><div class="k">Sem desconto</div>
      <div class="v">R$ {br2(BRUTO)}</div></div>
  </div>

  <div class="pay">
    <div class="c"><div class="k">Entrada · 50%</div>
      <div class="v serif">R$ {br2(ENTRADA)}</div>
      <div class="s">Na assinatura. É ela que libera a compra do MDF, do
      espelho e da ferragem, e abre a vaga na produção.</div></div>
    <div class="c"><div class="k">Saldo · {N_PARC}× no cartão</div>
      <div class="v serif">{N_PARC} × R$ {br2(PARCELA)}</div>
      <div class="s">Sem juros para vocês. O cartão pode ser passado na
      assinatura ou na medição.</div></div>
  </div>

  <div class="four">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div>
      <div class="s">Do aceite e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">{GARANTIA}</div>
      <div class="s">Estrutura e ferragens.</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div>
      <div class="s">Do corte à instalação.</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div>
      <div class="s">A partir desta data.</div></div>
  </div>

  <div class="notes">
    <div class="bx w"><div class="k">Está nesta proposta</div>
      <div class="d">Os <b>dois móveis</b> com a ferragem, o <b>espelho
      prata</b> e o <b>perfil de alumínio</b> das folhas, a <b>medição no
      local</b>, a <b>entrega</b> e a <b>instalação</b>. Projeto na
      <b>revisão 00</b>, da arquiteta {ARQ}.</div></div>
    <div class="bx"><div class="k">Não está</div>
      <div class="d">A <b>bancada</b> e o <b>seu apoio e fixação</b>, a
      rodabanca, a testeira, o acabamento do sóculo e o nicho do box —
      todos de <b>marmoraria</b> e de obra. O <b>sóculo em alvenaria</b>; o
      <b>box de correr</b>; as <b>louças, metais e acessórios</b>; as
      <b>arandelas, o driver e a instalação elétrica</b> — nossa é a
      usinagem da passagem e o berço na peça fixa; o <b>porcelanato e as
      soleiras</b>.</div></div>
  </div>

  <div class="foot"><span>Valvic Marcenaria</span>
    <span>{CLIENTE} · Banho suíte master</span><span>1 / 1</span></div>
</div></div></body></html>"""

(P/'proposta-orlando-ivone-fechamento.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-orlando-ivone-fechamento.pdf')],
               check=True, env=env)
print('proposta-orlando-ivone-fechamento.pdf · 1 página')
for _k, n, _d, v in ITENS: print(f'  {n:<32} R$ {br2(v):>10}')
print(f'  {"soma":<32} R$ {br2(BRUTO):>10}')
print(f'  {"desconto " + f"{DESC:.0%}":<32} − R$ {br2(BRUTO-LIQ):>8}')
print(f'  {"INVESTIMENTO":<32} R$ {br2(LIQ):>10}')
print(f'  {"entrada 50%":<32} R$ {br2(ENTRADA):>10}')
print(f'  {f"{N_PARC}× no cartão":<32} R$ {br2(PARCELA):>10}')
