# -*- coding: utf-8 -*-
"""SANDRA DUARTE — proposta · rack da sala  [14/10/2026]

⭐ [Jonathan 14/10] "adicione a rt e pode fazer a proposta de 2 paginas
   apenas" + "pagamento 50% entrada + 50% na entrega".

   → DUAS PÁGINAS. Página 1 escura: a capa E o valor, porque com duas
     folhas não cabe uma capa muda. Página 2 clara: o móvel, o preço e as
     condições. Uma condição só de pagamento, como instruído.
   → CSS PRÓPRIO, paleta do próprio móvel: espresso, champagne e pérola —
     Metalic Champagne e vidro reflecta champagne.
   → ⛔ SEM IMAGEM. A única arte da pasta é a prancha técnica, cotada de
     ponta a ponta, e metragem não vai para proposta — nem desenhada.

Números de `corte-sandra-rack.py`; nada digitado à mão.
⛔ Sem metragem e sem contagem. A única espessura citada é a do vidro do
   tampo, liberada por Jonathan em 07/10 como ESPECIFICAÇÃO de material.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('sr', P/'corte-sandra-rack.py')
sr = importlib.util.module_from_spec(spec); sys.modules['sr'] = sr
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(sr)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA, DATA = 'Sandra Duarte', 'Sala de estar', '16 de outubro de 2026'
ARQ = 'Junia Ordones'
PRAZO, VALIDADE, GARANTIA = '60 dias corridos', '7 dias úteis', '10 anos'
NP = 2
RACK, PAINEL, TOTAL = sr.PV, sr.PAINEL_PV, sr.TOTAL

# ⛔⛔ TRAVA. Não há soma de itens para fechar — há UM móvel. O que pode
#   mudar calado embaixo da proposta é a BASE do preço: se alguém desligar
#   o RT ou mexer na MC no motor, a folha sai com outro número sem avisar.
assert sr.RT_ON is True,            '⛔ O RT SAIU DO MOTOR [Jonathan 14/10 pediu COM RT]'
assert abs(sr.MC_ALVO - 0.30) < 1e-9, f'⛔ A MC MUDOU: {sr.MC_ALVO:.3f} ≠ 0,300'
assert RACK == sr.PV and RACK > 0,  '⛔ O PREÇO NÃO VEIO DO MOTOR'
assert PAINEL == 2300,              '⛔ O PAINEL NÃO ESTÁ NO PREÇO DO JONATHAN'
assert abs(RACK + PAINEL - TOTAL) < 0.5, (
    f'⛔ O TOTAL NÃO FECHA: {RACK:,.0f} + {PAINEL:,.0f} ≠ {TOTAL:,.0f}')

ITENS = [
 ('Corpo', 'Em MDF Guararapes linha Metalic, cor champagne, com nicho aberto '
  'à frente e o interior no mesmo padrão. Base recuada sobre <b>rodízios '
  'giratórios ocultos</b>: sai do lugar para limpar e passar fiação, e '
  'volta alinhado.'),
 ('Portas', 'De giro em <b>vidro temperado reflecta champagne</b>, '
  'enquadradas em perfil de alumínio slim, sobre dobradiça própria para '
  'vidro, com regulagem nos três sentidos.'),
 ('Tampo', 'Em <b>vidro temperado de 10 mm</b>, com bisotê na frente e na '
  'lateral aparente e lapidação reta ao fundo — a borda é trabalhada onde '
  'a vista alcança.'),
 ('Prateleira', 'Superior em MDF no mesmo padrão, apoiada na lateral que sobe '
  'e em <b>suporte de metal tubular champagne</b>, sem mão-francesa aparente.'),
 ('Luz', 'Fita <b>2700 K</b> em perfil de alumínio com difusor leitoso, '
  'embutida em cava usinada na própria peça e voltada para o fundo, para '
  'iluminar sem espelhar no vidro. <b>Entregue acesa.</b>'),
]

CSS = """
:root{
  --esp:#2A2724; --esp-d:#1A1816; --cha:#B2934F; --cha-lt:#E0C89D;
  --pearl:#F6F1E8; --ink:#1C1A18; --soft:#5C564E; --mut:#938C81;
  --hair:#EAE3D8; --line:#D9D1C4; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.5pt;line-height:1.6;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:19mm 19mm 14mm;height:100%;display:flex;flex-direction:column;}
.pad.p2{padding-top:15mm;}
.foot{margin-top:auto;padding-top:7mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:7pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}

/* ── página 1 · escura: a capa e o valor ────────────────────────────── */
.dk{background:var(--esp);color:#F3EDE3;}
.dk .foot{border-top:1px solid rgba(255,255,255,.16);color:#8E867A;}
.mark{font-size:8.4pt;letter-spacing:.42em;text-transform:uppercase;
  color:#EFE6D6;font-weight:700;flex:none;}
.kick{font-size:7pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--cha-lt);font-weight:700;flex:none;}
.dk h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:54pt;
  line-height:.98;font-weight:600;letter-spacing:-.025em;margin:4mm 0 0;flex:none;}
.dk .sub{font-size:11pt;color:#C6BEB2;margin-top:5mm;font-weight:300;flex:none;}
.dk .sub b{color:#EBE3D6;font-weight:500;}
.vrow{display:grid;grid-template-columns:34mm 1fr;gap:7mm;align-items:baseline;
  padding:6.4mm 0;border-top:1px solid rgba(255,255,255,.14);flex:none;}
.vrow:first-of-type{border-top:none;}
.vrow .k{font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--cha-lt);font-weight:700;padding-top:2.6mm;}
.vrow .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:24pt;
  font-weight:600;line-height:1.05;letter-spacing:-.01em;color:#fff;}
.vrow .d{color:#BDB5A8;font-size:9pt;line-height:1.56;margin-top:2mm;
  max-width:120mm;}
.vrow .d b{color:#F1EADD;font-weight:600;}
.meta{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;
  padding-top:6mm;border-top:1px solid rgba(255,255,255,.3);flex:none;}
.meta .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--cha-lt);font-weight:700;}
.meta .v{font-size:11pt;font-weight:600;margin-top:1.4mm;color:#F3EDE3;}

/* ── página 2 · clara: o móvel, o preço, as condições ───────────────── */
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.6px solid var(--ink);padding-bottom:3.4mm;flex:none;}
.hd .b{font-size:8pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:7pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--cha);font-weight:700;margin-top:4mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:24pt;
  line-height:1.04;font-weight:600;letter-spacing:-.02em;margin-top:2mm;flex:none;}
.grp{margin-top:4.5mm;flex:none;}
.gh{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  border-top:1.6px solid var(--ink);padding-top:3.4mm;}
.gh .gt{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:600;letter-spacing:-.01em;line-height:1;}
.gh .gs{color:var(--soft);font-size:8.6pt;line-height:1.46;margin-top:2mm;
  max-width:116mm;}
.gh .gs b{color:var(--ink);font-weight:600;}
.gh .gv{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:700;text-align:right;line-height:1;white-space:nowrap;
  font-variant-numeric:tabular-nums;}
.rows{margin-top:0;flex:none;}
.row{display:grid;grid-template-columns:26mm 1fr;gap:6mm;align-items:baseline;
  padding:2.5mm 0;border-top:1px solid var(--line);}
.row:first-child{border-top:1px solid var(--line);}
.row .k{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;
  font-weight:700;color:var(--cha);line-height:1;padding-top:.6mm;}
.row .d{color:var(--soft);font-size:8.6pt;line-height:1.46;}
.row .d b{color:var(--ink);font-weight:600;}

.band{margin-top:5mm;background:var(--esp);color:#F3EDE3;border-radius:3px;
  padding:5mm 7mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.band .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--cha-lt);font-weight:700;}
.band .s{font-size:9pt;color:#C2BAAD;margin-top:2.4mm;max-width:92mm;}
.band .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:34pt;
  font-weight:700;color:#fff;line-height:.92;letter-spacing:-.025em;
  font-variant-numeric:tabular-nums;white-space:nowrap;}
.pay{margin-top:4mm;display:flex;justify-content:space-between;
  align-items:baseline;gap:6mm;padding-top:3.6mm;
  border-top:1.6px solid var(--ink);font-size:10pt;color:var(--soft);flex:none;}
.pay b{color:var(--ink);font-weight:600;}
.pay .x{flex:none;font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--cha);font-weight:700;}
.strip{margin-top:4.5mm;padding-top:3.4mm;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;gap:5mm;font-size:8.6pt;
  color:var(--soft);flex:none;}
.strip span{white-space:nowrap;}
.strip b{color:var(--ink);font-weight:600;}
.strip .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--cha);font-weight:700;}
.notes{margin-top:4.5mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;
  flex:none;}
.notes .bx{background:var(--pearl);border-radius:3px;padding:4.5mm 5mm;}
.notes .bx.w{background:#fff;border:1px solid var(--line);}
.notes .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--cha);font-weight:700;}
.notes .d{color:var(--soft);font-size:7.6pt;line-height:1.4;margin-top:1.6mm;}
.notes .d b{color:var(--ink);font-weight:600;}
"""

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · sala de estar</span><span>{n} / {NP}</span></div>')

p1 = f"""<div class="page dk"><div class="pad">
  <div class="mark">Valvic Marcenaria</div>
  <div style="height:26mm;flex:none;"></div>
  <div class="kick">Proposta comercial</div>
  <h1>Rack<br>e painel.</h1>
  <div class="sub"><b>{CLIENTE}</b> · {OBRA}<br>Projeto <b>{ARQ}</b></div>

  <div class="vrow" style="margin-top:13mm;">
    <div class="k">Garantia</div>
    <div><div class="t serif">Dez anos.</div>
      <div class="d">Estrutura e ferragens, em termo nosso. Não é selo de
      catálogo: é o prazo em que respondemos pelo que entregamos, com
      <b>equipe própria</b>, do corte à instalação.</div></div>
  </div>
  <div class="vrow">
    <div class="k">Vidro e metal</div>
    <div><div class="t serif">Borda trabalhada,<br>metal champagne.</div>
      <div class="d">O tampo é <b>vidro temperado</b> com a borda bisotada
      onde a vista alcança, e lapidada onde ela não chega. As portas correm
      em <b>dobradiça própria para vidro</b>, com regulagem — é o que
      decide se a porta ainda fecha no prumo no décimo ano.</div></div>
  </div>
  <div class="vrow">
    <div class="k">Iluminação</div>
    <div><div class="t serif">Entregue acesa.</div>
      <div class="d">Fita e perfil <b>usinados dentro da própria peça</b>,
      não aparafusados depois, e voltados para o fundo para iluminar sem
      espelhar no vidro. <b>A nossa parte chega instalada</b> — a obra só
      liga o circuito.</div></div>
  </div>

  <div class="meta">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Garantia</div><div class="v">{GARANTIA}</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
  {foot(1)}
</div></div>"""

rows = ''.join(f'<div class="row"><div class="k">{k}</div>'
               f'<div class="d">{d}</div></div>' for k, d in ITENS)

p2 = f"""<div class="page"><div class="pad p2">
  <div class="hd"><div class="b">Valvic Marcenaria</div>
    <div class="m">{CLIENTE} · {DATA}</div></div>
  <div class="eye">O móvel</div>
  <div class="h1 serif">O que entra, e quanto é.</div>
  <div class="grp">
    <div class="gh"><div class="gt">Rack da sala</div>
      <div class="gv">R$ {br(RACK)}</div></div>
    <div class="rows">{rows}</div>
  </div>

  <div class="grp">
    <div class="gh">
      <div><div class="gt">Painel de TV</div>
        <div class="gs">Liso, no mesmo padrão champagne, <b>apoiado no
        rodapé</b> e fixado à parede, <b>em peça única, sem emenda
        aparente</b>, com a passagem de cabos por trás.</div></div>
      <div class="gv">R$ {br(PAINEL)}</div></div>
  </div>

  <div class="band">
    <div><div class="lab">Investimento total</div>
      <div class="s">Os dois itens no padrão especificado pela arquiteta,
      com iluminação instalada e montagem no local.</div></div>
    <div class="big">R$ {br(TOTAL)}</div>
  </div>

  <div class="pay">
    <div><b>50%</b> de entrada + <b>50%</b> na entrega</div>
    <div class="x">condição única</div>
  </div>

  <div class="strip">
    <span><span class="k">Prazo</span> <b>{PRAZO}</b></span>
    <span><span class="k">Garantia</span> <b>{GARANTIA}</b></span>
    <span><span class="k">Execução</span> <b>Equipe própria</b></span>
    <span><span class="k">Validade</span> <b>{VALIDADE}</b></span>
  </div>

  <div class="notes">
    <div class="bx"><div class="k">O que não está incluso</div>
      <div class="d">A <b>televisão, os equipamentos</b> e o seu
      cabeamento. O <b>ponto de tomada, o circuito e o interruptor</b>, que
      são elétrica de obra. A <b>retirada do painel existente</b>, se o
      novo tomar o lugar dele. <b>Alvenaria, pintura e iluminação de
      teto.</b></div></div>
    <div class="bx w"><div class="k">A confirmar antes da produção</div>
      <div class="d">A prancha pede <b>conferir as medidas e o ponto de
      energia no local</b> — fazemos a medição antes do corte. O
      <b>puxador</b>: recomendamos o perfil slim colado, porque furo em
      vidro temperado é feito antes da têmpera e não admite ajuste depois da medição. A <b>altura do painel</b>, que a medição fecha
      — é ela que confirma a peça única. E <b>amostra</b> do padrão
      champagne, no MDF e no vidro.</div></div>
  </div>
  {foot(2)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + '</body></html>')

(P/'proposta-sandra-rack.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-sandra-rack.pdf')],
               check=True, env=env)
print(f'proposta-sandra-rack.pdf · {NP} páginas')
print(f'  MC {sr.MC_ALVO*100:.0f}% · COM RT · base {sr.BASE*100:.2f}%')
print(f'  custo direto      R$ {br(sr.CD + sr.CD_PAINEL):>7}')
print(f'  rack              R$ {br(RACK):>7}')
print(f'  painel de TV      R$ {br(PAINEL):>7}  ⭐ preço do Jonathan · '
      f'MC {sr.MC_PAINEL:.1%}')
print(f'  INVESTIMENTO      R$ {br(TOTAL):>7}')
print(f'  pagamento         50% de entrada + 50% na entrega')
