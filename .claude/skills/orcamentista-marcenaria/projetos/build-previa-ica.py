# -*- coding: utf-8 -*-
"""Prévia do layout da proposta ICA · Jéssica e Michell.
   Padrão da casa: css-apresentacao.css (referência "APRESENTAÇÃO — JUNIOR
   LAGOA SANTA OFICIAL"). Três spreads: capa, ambiente e investimento."""
import pathlib

CSS = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/'
                   'orcamentista-marcenaria/projetos/css-apresentacao.css').read_text()

BASE, MC, DIAS = 0.84875, 0.60, 90

AMB = [
 ("Living",18,"R$ 34.683,32"),("Cozinha",15,"R$ 25.790,08"),
 ("Lavanderia",17,"R$ 21.899,18"),("Quarto",11,"R$ 12.240,10"),
 ("Lavabo",2,"R$ 0,00"),("Área gourmet",11,"R$ 15.791,97"),
 ("Banho gourmet",6,"R$ 2.320,35"),("Home office",10,"R$ 10.313,77"),
 ("Suíte hóspedes",14,"R$ 14.910,01"),("Banho hóspedes",6,"R$ 3.591,46"),
 ("Sala de cinema e ateliê",17,"R$ 30.627,78"),("Suíte master",12,"R$ 15.616,14"),
 ("Closet master",13,"R$ 28.226,46"),("Banho master",11,"R$ 5.115,63"),
 ("Suíte Mariana",15,"R$ 24.726,87"),("Closet Mariana",9,"R$ 16.428,09"),
 ("Banho Mariana",7,"R$ 3.493,62"),("Suíte 03",14,"R$ 29.613,03"),
 ("Closet 03",8,"R$ 13.320,91"),("Banho 03",6,"R$ 2.833,13"),
]

def n(s):  return float(s.replace("R$ ","").replace(".","").replace(",","."))
def br(v): return "R$ " + f"{v:,.2f}".replace(",","@").replace(".",",").replace("@",".")

linhas, total = [], 0.0
for nome, itens, custo in AMB:
    preco = n(custo) / (BASE - MC)
    total += preco
    linhas.append((nome, itens, preco))

# Suíte Mariana — os 12 itens do módulo, para a página de ambiente
MARIANA = [
 ("Estante com armário","350 × 300 × 30 · nichos e portas"),
 ("Casinha","350 × 219 × 25 · ripado e iluminação embutida"),
 ("Cama montessoriana","207 × 107 × 57 · base em serralheria e malha de cordas"),
 ("Escrivaninha montessoriana","91 × 64 × 40"),
 ("Mesa com armário","235 × 66 × 50"),
 ("Mesa lateral","83 × 60 × 50"),
 ("Painel com suporte de papel","105 × 145 × 19"),
 ("Painel 1 e Painel 2","105 × 135 e 330 × 145 · ripado"),
 ("Prateleira","114 × 15 × 8"),
 ("Caixa organizadora","50 × 35 × 46 · duas"),
 ("Nome “Mariana”","letra em router, elevação 04"),
]

mv = "\n".join(
  f'    <div class="mv"><span class="b"></span><span><span class="t">{t}</span>'
  f' <span class="d">{d}</span></span></div>' for t, d in MARIANA)

col = lambda ls: "\n".join(
  f'      <tr><td class="l">{nome}</td><td class="hi">{br(p)}</td></tr>'
  for nome, _, p in ls)
inv_a, inv_b = col(linhas[:10]), col(linhas[10:])

PG = """<meta name="claude:viewport-fit-sides" content="cover">
<title>Prévia · Proposta ICA</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">
<style>
__CSS__

/* ── só para ver a prévia na tela: a folha A4 deitada escalada ao vão ──── */
body.previa{background:#2A2622;margin:0;padding:26px 16px 60px;}
.wrap{max-width:1180px;margin:0 auto;}
.hd{color:#E7E0D2;font-family:'DM Sans',Arial,sans-serif;margin:0 0 26px;}
.hd h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;
       font-size:clamp(26px,5vw,40px);line-height:1.1;margin:8px 0 10px;
       letter-spacing:-.015em;}
.hd .eb{font-size:11px;letter-spacing:.3em;text-transform:uppercase;
        color:#C6A567;font-weight:600;}
.hd p{color:#A79E8E;font-size:15px;line-height:1.6;max-width:62ch;margin:0;}
.cap{color:#C6A567;font-family:'DM Sans',Arial,sans-serif;font-size:11px;
     letter-spacing:.26em;text-transform:uppercase;font-weight:600;
     margin:34px 0 9px;}
.stage{position:relative;width:100%;aspect-ratio:297/210;overflow:hidden;
       box-shadow:0 18px 44px rgba(0,0,0,.42);background:#fff;}
.stage .slide{position:absolute;top:0;left:0;transform-origin:top left;
              transform:scale(var(--s,1));}
.nota{background:#352F29;border-left:3px solid #C6A567;color:#CFC6B4;
      font-family:'DM Sans',Arial,sans-serif;font-size:14px;line-height:1.62;
      padding:16px 20px;margin-top:34px;border-radius:2px;}
.nota b{color:#F1E9D9;}
@media (max-width:620px){.stage{box-shadow:0 10px 24px rgba(0,0,0,.4)}}
</style>
<body class="previa"><div class="wrap">

<div class="hd">
  <div class="eb">Valvic · Prévia de layout</div>
  <h1>Jéssica e Michell · ICA</h1>
  <p>Três folhas do caderno, no padrão da casa — A4 deitado, conduzido por
     imagem, uma abertura por ambiente. As perspectivas são as do executivo da
     Iara Cezar, em 1760 × 1328: dá para sangrar a página inteira.</p>
</div>

<div class="cap">01 · Capa</div>
<div class="stage"><div class="slide dark"><div class="cv">
  <div class="cv-l" style="padding-bottom:20mm">
    <div class="cv-brand">Valvic Marcenaria</div>
    <div class="cv-nome">Jéssica<br>e Michell</div>
    <div class="cv-s">Vinte ambientes, uma casa inteira,<br>
        uma só marcenaria do projeto à instalação.</div>
    <div class="cv-meta">
      <div><div class="k">Projeto</div><div class="v">Iara Cezar Arquitetura</div></div>
      <div><div class="k">Local</div><div class="v">Manhumirim · MG</div></div>
      <div><div class="k">Ambientes</div><div class="v">20</div></div>
      <div><div class="k">Cenários</div><div class="v">Blum · Hettich</div></div>
    </div>
  </div>
  <div class="cv-r"><img src="img/capa.jpg" alt="Living"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)"><span>Valvic&nbsp;·&nbsp;Jéssica e Michell</span><span>Outubro de 2026</span></div>
</div></div>

<div class="cap">02 · Abertura de ambiente</div>
<div class="stage"><div class="slide"><div class="amb">
  <div class="amb-img"><img src="img/amb.jpg" alt="Suíte Mariana">
    <div class="tag">Suíte Mariana</div></div>
  <div class="amb-txt">
    <div class="amb-n">15</div>
    <div class="eyebrow">Ambiente</div><div class="rule"></div>
    <h2 class="h2" style="margin:1mm 0 4mm">Suíte Mariana</h2>
__MV__
    <div class="amb-nota"><div class="t">Nota de execução</div>
      <p>A base da cama em serralheria com malha de cordas sai no mesmo
         contrato da marcenaria: você não contrata mais ninguém. A casinha
         leva ripado em Nogueira Caiena com LED embutido na testeira.</p></div>
  </div>
</div>
<div class="foot r"><span>Valvic&nbsp;·&nbsp;Jéssica e Michell</span><span>15 / 28</span></div>
</div></div>

<div class="cap">03 · Investimento</div>
<div class="stage"><div class="slide"><div class="pad">
  <div class="eyebrow">Investimento</div><div class="rule"></div>
  <h2 class="h2" style="margin-bottom:5mm">Ambiente a ambiente.</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:9mm;flex:none;align-items:start">
   <table class="inv">
    <tr><th class="l">Ambiente</th><th class="hi">Investimento</th></tr>
__INVA__
   </table>
   <table class="inv">
    <tr><th class="l">Ambiente</th><th class="hi">Investimento</th></tr>
__INVB__
   </table>
   <div style="display:flex;flex-direction:column;gap:4mm">
     <div class="box" style="margin-top:0"><div class="t">O que está incluso</div>
       <p>Projeto executivo de marcenaria, material, usinagem, ferragens,
          iluminação embutida, frete, montagem e instalação — com um só
          interlocutor do primeiro desenho à entrega da chave.</p></div>
     <div class="box" style="margin-top:0"><div class="t">Garantia</div>
       <p>Cinco anos de garantia Valvic sobre a marcenaria, contra defeito
          de fabricação e de montagem.</p></div>
     <div style="margin-top:6mm;border-top:1.5px solid var(--ink);padding-top:3mm">
       <div style="font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;
                   color:var(--mut);font-weight:600">Total do investimento</div>
       <div class="serif" style="font-size:24pt;line-height:1.1;margin-top:1.5mm;
                   font-variant-numeric:tabular-nums">__TOT__</div>
       <div style="color:var(--soft);font-size:7.8pt;margin-top:1.5mm">
          Vinte ambientes · a casa completa</div>
     </div>
   </div>
  </div>
  <div class="mos" style="grid-template-columns:repeat(3,1fr);height:44mm;flex:none;margin-top:4mm">
    <figure><img src="img/m1.jpg" alt=""><figcaption>Área gourmet</figcaption></figure>
    <figure><img src="img/m2.jpg" alt=""><figcaption>Closet Mariana</figcaption></figure>
    <figure><img src="img/m3.jpg" alt=""><figcaption>Banho master</figcaption></figure>
  </div>
</div>
<div class="foot"><span>Valvic&nbsp;·&nbsp;Jéssica e Michell</span><span>26 / 28</span></div>
</div></div>

<div class="nota">
  <b>O que mudou desde a prévia anterior.</b> O layout saiu da linguagem que eu
  tinha inventado e voltou para o padrão da casa — o mesmo caderno do Junior
  Lagoa Santa, já aplicado no Carol e Vinícius e na Carla. E as perspectivas
  do executivo não eram pequenas: as folhas de foto de cada ambiente trazem
  renders em <b>1760 × 1328</b> (o banho master em 2400 × 1792). Não é preciso
  pedir nada para a Iara.<br><br>
  <b>Os valores acima são o cenário Blum a 60 % de MC</b> — total
  <b>__TOT__</b>. Confirme o cenário e eu monto as 28 folhas.
</div>

</div>
<script>
  const fit = () => document.querySelectorAll('.stage').forEach(s =>
    s.style.setProperty('--s', s.clientWidth / (297 / 25.4 * 96)));
  addEventListener('resize', fit); addEventListener('load', fit); fit();
</script>
"""

html = (PG.replace('__CSS__', CSS).replace('__MV__', mv)
          .replace('__INVA__', inv_a).replace('__INVB__', inv_b).replace('__TOT__', br(total)))
out = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                   '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad/previa-ica.html')
out.write_text(html)
print(out, len(html), 'chars · total', br(total))
