# -*- coding: utf-8 -*-
"""PROPOSTA — PÓRTICO E MÓVEL RIPADO · FOLHA ÚNICA  [07/10/2026]

Escopo, nas palavras do Jonathan:
  · Pórtico de acabamento em vão da sala
  · Estrutura de móvel ripado com duas portas de giro e laterais, sendo ambas
    vazadas com usinagem em Router CNC. Réguas de 50mm de largura com
    espaçamento de 15mm, sem laminação nos vãos internos das usinagens.
    Em MDF amadeirado Ultra (mais resistente a umidade).
  · R$ 6.500 · 60 dias · entrada de 40%, restante na entrega.

⛔⛔ EXCEÇÃO AUTORIZADA À REGRA DE METRAGEM
   "réguas de 50 mm com espaçamento de 15 mm" é ESPECIFICAÇÃO DO DESENHO,
   não quantitativo — o mesmo caso da espessura de chapa (15/18 mm) já
   liberada. Sem ela o cliente não sabe o que está comprando: o passo do
   ripado é o produto. Idem "duas portas de giro", que delimita o escopo
   do móvel. Pedido explícito do Jonathan em 07/10. Registrar em
   `referencias/proposta-comercial.md`.

⛔ As imagens vieram recortadas: a do ripado trazia rótulos de um gráfico
   comparativo de outra fonte e dois painéis cortados à direita.
⛔ Classes novas levam sufixo R. Não reaproveitar .inv/.pay/.esc/.cnd do
   `css-proposta.css` — ali a colisão já mordeu duas vezes.
"""
import pathlib, subprocess, base64, os

P = pathlib.Path(__file__).resolve().parent
br = lambda v: f'{v:,.0f}'.replace(',', '.')

def uri(nome):
    b = (P/'img'/nome).read_bytes()
    return 'data:image/jpeg;base64,' + base64.b64encode(b).decode()

IMG_PORTICO = uri('portico-vao.jpg')
IMG_RIPADO  = uri('movel-ripado.jpg')

DATA   = '7 de outubro de 2026'
TOTAL  = 6500.0
P_ENT  = 0.40                      # entrada; o restante na entrega
VAL_ENT = TOTAL*P_ENT
VAL_SLD = TOTAL - VAL_ENT
PRAZO   = '60 dias'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── pórtico e móvel ripado · folha única ─────────────────────────────── */
/* ⛔ flex:none em TODO bloco fechado: .pad é coluna flex e um box com
      overflow:hidden ENCOLHE em silêncio quando a coluna estoura. */
.topR{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4.5mm;border-bottom:1px solid var(--hair);flex:none;}
.topR .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;letter-spacing:.02em;}
.topR .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}

.leadR{color:var(--soft);font-size:9.2pt;line-height:1.56;max-width:158mm;
  flex:none;}
.leadR b{color:var(--ink);font-weight:600;}

.blkR{display:flex;gap:7mm;align-items:flex-start;margin-top:5.5mm;flex:none;}
.blkR.rev{flex-direction:row-reverse;}
.blkR .fig{flex:none;border-radius:5px;overflow:hidden;line-height:0;}
.blkR .fig img{display:block;width:100%;height:auto;}
.blkR .cap{line-height:1.4;font-size:7pt;color:var(--mut);margin-top:1.8mm;
  letter-spacing:.04em;}
.blkR .txt{flex:1;}
.blkR .n{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.blkR .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;
  font-weight:700;line-height:1.15;margin-top:1.4mm;}
.blkR .d{color:var(--soft);font-size:8.4pt;line-height:1.5;margin-top:2.2mm;}
.blkR .d b{color:var(--ink);font-weight:600;}
.blkR .d p{margin:0 0 1.8mm;}
.blkR .d p:last-child{margin-bottom:0;}

.invR{margin-top:5.5mm;border:1.5px solid var(--gold);border-radius:6px;
  background:rgba(201,169,106,.07);padding:5mm;display:flex;gap:5.5mm;
  align-items:stretch;flex:none;}
.invR > div{flex:1;}
.invR > div + div{border-left:1px solid var(--gold-lt);padding-left:6mm;}
.invR .k{font-size:7pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.invR .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
  font-weight:700;line-height:1.05;margin-top:1.6mm;}
.invR .v.sm{font-size:16pt;}
.invR .s{font-size:8.1pt;color:var(--soft);margin-top:1.6mm;line-height:1.5;}
.invR .s b{color:var(--ink);font-weight:600;}

.cndR{display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;margin-top:4.5mm;
  padding-top:3.2mm;border-top:1px solid var(--hair);flex:none;}
.cndR .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndR .d{color:var(--soft);font-size:8.2pt;margin-top:1mm;line-height:1.46;}
.cndR .d b{color:var(--ink);}
.notaR{margin-top:4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.5;flex:none;}
.notaR b{color:var(--ink);}
""")

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<div class="page"><div class="pad">

  <div class="topR">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta<br>{DATA}</div>
  </div>

  <div style="margin-top:5mm;" class="eyebrow">Sala e varanda</div>
  <div class="h-sec serif" style="font-size:24pt;">Pórtico e móvel ripado.</div>
  <div class="rule"></div>
  <div class="leadR">Dois serviços que resolvem a mesma passagem: o
  <b>arremate do vão</b> pelo lado da sala e o <b>fechamento ripado</b> do
  que fica atrás dele. Um vira moldura, o outro vira parede — e os dois são
  feitos na mesma madeira.</div>

  <div class="blkR">
    <div class="fig" style="width:80mm;">
      <img src="{IMG_PORTICO}" alt="">
      <div class="cap">O vão da sala, arrematado em madeira</div>
    </div>
    <div class="txt">
      <div class="n">01</div>
      <div class="t">Pórtico de<br>acabamento</div>
      <div class="d">
        <p>Acabamento do <b>vão da sala</b>. O pórtico arremata a passagem em
        marcenaria, no lugar do acabamento de obra — e dá ao vão a mesma
        madeira que corre pelo resto do ambiente.</p>
      </div>
    </div>
  </div>

  <div class="blkR rev">
    <div class="fig" style="width:48mm;">
      <img src="{IMG_RIPADO}" alt="">
      <div class="cap">O ripado vazado, com iluminação embutida</div>
    </div>
    <div class="txt">
      <div class="n">02</div>
      <div class="t">Móvel ripado</div>
      <div class="d">
        <p>Estrutura com <b>duas portas de giro e laterais</b>, todas vazadas
        com usinagem em <b>Router CNC</b> — o mesmo desenho corre pela frente
        e pelas laterais do móvel.</p>
        <p>Réguas de <b>50 mm de largura com espaçamento de 15 mm</b>. Os vãos
        internos das usinagens não recebem laminação.</p>
        <p>Executado em <b>MDF amadeirado Ultra</b>, escolhido pela
        <b>resistência à umidade</b> — é o que o ambiente pede, e é o que
        mantém o ripado estável com o tempo.</p>
      </div>
    </div>
  </div>

  <div class="invR">
    <div>
      <div class="k">O investimento</div>
      <div class="v">R$ {br(TOTAL)}</div>
    </div>
    <div>
      <div class="k">Forma de pagamento</div>
      <div class="v sm">R$ {br(VAL_ENT)}<span style="font-size:10pt;
        font-family:'DM Sans',sans-serif;font-weight:400;color:var(--soft);
        "> de entrada</span></div>
      <div class="s">e <b>R$ {br(VAL_SLD)}</b> na entrega do projeto.</div>
    </div>
    <div>
      <div class="k">Prazo de entrega</div>
      <div class="v sm">{PRAZO}</div>
      <div class="s">contados do aceite e da conferência de medidas no
      local.</div>
    </div>
  </div>

  <div class="cndR">
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens.</div></div>
    <div><div class="k">Projeto</div><div class="d">
      Medida conferida <b>no local</b> antes do corte.</div></div>
  </div>

  <div class="notaR"><b>Não inclusos:</b> alvenaria, elétrica e hidráulica,
  pintura de parede, gesso, revestimentos, iluminação e o mobiliário solto.</div>

  <div class="foot"><span>Valvic Marcenaria</span>
    <span>Pórtico e móvel ripado</span>
    <span>{DATA}</span></div>

</div></div>
</body></html>"""

(P/'proposta-portico-ripado.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-portico-ripado.pdf')],
               check=True, env=env)
print('proposta-portico-ripado.pdf · 1 página')
print(f'  Investimento   R$ {br(TOTAL)}')
print(f'  Entrada {P_ENT*100:.0f}%    R$ {br(VAL_ENT)}')
print(f'  Na entrega     R$ {br(VAL_SLD)}')
print(f'  Prazo          {PRAZO}')
