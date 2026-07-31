# -*- coding: utf-8 -*-
"""PROPOSTA PREMIUM — Quartos Mateus e Manuela (Larissa e Rafael · A Urbanística).
6 páginas: capa · conceitual (o ripado e a luz) · quarto Mateus · quarto Manuela ·
técnico · investimento. Preços: corte-quartos-larissa-rafael.py (MC 40%)."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

MT1 = open('/tmp/uri_q_mt1.txt').read()
MT2 = open('/tmp/uri_q_mt2.txt').read()
MN1 = open('/tmp/uri_q_mn1.txt').read()
MN2 = open('/tmp/uri_q_mn2.txt').read()
MTD = open('/tmp/uri_q_mt_det.txt').read()
MND = open('/tmp/uri_q_mn_det.txt').read()
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  .cover .hero-img img{{object-position:center 42%;}}
  .cover .veil{{background:linear-gradient(180deg,
      rgba(24,19,14,.86) 0%, rgba(24,19,14,.30) 24%, rgba(24,19,14,.12) 48%,
      rgba(24,19,14,.60) 74%, rgba(24,19,14,.95) 100%);}}

  /* ── conceitual (fundo escuro) */
  .concept{{background:var(--deep); color:#EFE9DC;}}
  .concept .pad{{padding:15mm 19mm 12mm;}}
  .concept .eyebrow{{color:var(--gold-lt);}}
  .concept .h-sec{{color:#fff;}}
  .concept .body-t{{color:#C9C2B4; font-size:9.2pt;}}
  .concept .body-t b{{color:#F0E7D6;}}
  .proc{{display:flex; gap:0; margin-top:5mm; border-top:1px solid rgba(201,169,106,.30);
      padding-top:3.4mm;}}
  .proc > div{{flex:1; padding:0 4.5mm; border-left:1px solid rgba(201,169,106,.16);}}
  .proc > div:first-child{{padding-left:0; border-left:0;}}
  .proc .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt; font-weight:700;
      color:var(--gold-lt); line-height:1;}}
  .proc .d{{font-size:7.9pt; color:#B9B1A2; line-height:1.5; margin-top:1.4mm;}}
  .proc .d b{{color:#F0E7D6;}}
  .duo2{{display:flex; gap:5mm; margin-top:5.5mm;}}
  .duo2 > div{{flex:1;}}
  .duo2 img{{width:100%; height:97mm; object-fit:cover; border-radius:5px; display:block;}}
  .duo2 .cap{{color:#8F8578; margin-top:2mm;}}

  /* ── páginas de quarto */
  .qhero{{border-radius:6px; overflow:hidden; margin-top:3mm;}}
  .qhero img{{width:100%; height:86mm; object-fit:cover; display:block;}}
  .qsplit{{display:flex; gap:6mm; margin-top:4.5mm;}}
  .qsplit .side{{flex:0 0 46mm;}}
  .qsplit .side img{{width:100%; height:78mm; object-fit:cover; border-radius:5px; display:block;}}
  .qsplit .side .cap{{margin-top:1.8mm;}}
  .mv{{border-top:1px solid var(--hair); padding:2.4mm 0;}}
  .mv:first-child{{border-top:2px solid var(--ink);}}
  .mv .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:12pt; font-weight:700;
      line-height:1.2;}}
  .mv .t span{{font-family:system-ui,sans-serif; font-size:7.4pt; font-weight:400;
      color:var(--mut); letter-spacing:.04em;}}
  .mv .d{{font-size:8.2pt; color:var(--soft); line-height:1.5; margin-top:.8mm;}}
  .mv .d b{{color:var(--ink);}}
  .palette{{display:flex; gap:0; margin-top:3.5mm; border-top:1px solid var(--line);
      border-bottom:1px solid var(--line); padding:2.6mm 0;}}
  .palette > div{{flex:1; padding-left:5mm; border-left:1px solid var(--line);}}
  .palette > div:first-child{{padding-left:0; border-left:0;}}
  .palette .k{{font-size:6.6pt; letter-spacing:.16em; text-transform:uppercase;
      color:var(--gold); font-weight:700;}}
  .palette .nm{{font-family:'Cormorant Garamond',Georgia,serif; font-size:12.5pt;
      font-weight:700; color:var(--ink); line-height:1.15; margin-top:.8mm;}}
  .palette .d{{font-size:7.6pt; color:var(--soft); line-height:1.4; margin-top:.6mm;}}

  /* ── investimento */
  .qcard{{display:flex; gap:5mm; margin-top:4mm;}}
  .qcard > div{{flex:1; border-radius:6px; padding:5mm 5.5mm; background:var(--gold-pale);}}
  .qcard .k{{font-size:6.8pt; letter-spacing:.18em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .qcard .nm{{font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt; font-weight:700;
      color:var(--ink); margin-top:1.2mm; line-height:1.15;}}
  .qcard .nm small{{display:block; font-family:system-ui,sans-serif; font-size:7.4pt;
      font-weight:400; color:var(--mut); margin-top:1mm; line-height:1.4;}}
  .qcard .v{{font-family:'Cormorant Garamond',Georgia,serif; font-size:19pt; font-weight:700;
      color:var(--gold); margin-top:2.6mm; line-height:1;}}
  .qcard .v small{{display:block; font-family:system-ui,sans-serif; font-size:7.4pt;
      font-weight:400; color:var(--soft); margin-top:1.2mm;}}
  .inv-tot{{background:var(--deep); border-radius:7px; padding:5.5mm 7mm; margin-top:4.5mm;
      position:relative; overflow:hidden; box-shadow:inset 0 0 0 1.5px rgba(201,169,106,.5);
      display:flex; justify-content:space-between; align-items:flex-end;}}
  .inv-tot .k{{font-size:6.8pt; letter-spacing:.2em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700;}}
  .inv-tot .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:29pt; font-weight:700;
      color:#fff; line-height:1.05; margin-top:1.4mm;}}
  .inv-tot .rt{{text-align:right;}}
  .inv-tot .rt .v{{font-family:'Cormorant Garamond',Georgia,serif; font-size:21pt;
      font-weight:700; color:var(--gold-lt); line-height:1.05;}}
  .inv-tot .rt .s{{font-size:7.6pt; color:#9C9288; margin-top:1mm;}}
  .pay{{margin-top:4.5mm;}}
  .pay .r{{display:flex; justify-content:space-between; align-items:baseline;
      border-top:1px solid var(--line); padding:2.5mm 0; font-size:8.8pt; color:var(--soft);}}
  .pay .r:first-child{{border-top:2px solid var(--ink);}}
  .pay .r b{{color:var(--ink);}}
  .pay .v{{font-family:'Cormorant Garamond',Georgia,serif; font-size:12.5pt; font-weight:700;
      color:var(--ink);}}
  .pay .r.g{{background:var(--gold-pale); margin:0 -3mm; padding:2.5mm 3mm; border-radius:4px;
      border-top-color:transparent;}}
  .pay .r.g .v{{color:var(--gold);}}
  .cond{{display:grid; grid-template-columns:1fr 1fr; gap:2.8mm 7mm; margin-top:4.5mm;
      border-top:2px solid var(--ink); padding-top:3.2mm;}}
  .cond .k{{font-size:6.8pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .cond .d{{font-size:8.2pt; color:var(--soft); line-height:1.45; margin-top:.6mm;}}
  .cond .d b{{color:var(--ink);}}
  .warr{{background:var(--deep); border-left:3px solid var(--gold-lt); border-radius:0 5px 5px 0;
      padding:4.2mm 6mm; margin-top:4mm;}}
  .warr .k{{font-size:6.8pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt);
      font-weight:700;}}
  .warr .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:18pt; font-weight:700;
      color:#fff; line-height:1.1; margin-top:1.2mm;}}
  .warr .d{{font-size:8.2pt; color:#C6BFB2; line-height:1.5; margin-top:1.6mm;}}
  .warr .d b{{color:#F0E7D6;}}
  .obs{{margin-top:4mm; padding-left:4mm; border-left:2px solid var(--gold-lt);
      font-size:7.4pt; color:var(--soft); line-height:1.55;}}
  .obs b{{color:var(--ink);}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover">
  <div class="hero-img"><img src="{MT1}" alt=""></div>
  <div class="veil"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Mateus &amp; Manuela.</div>
      <div class="sub">Dois quartos · Projeto A Urbanística · Belo Horizonte</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">11 móveis · 2 quartos</div></div>
      <div class="c"><div class="k">Destaque</div><div class="v">Ripado e luz indireta</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich · Alemanha</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. CONCEITUAL ══════ -->
<div class="page concept"><div class="pad">
  <div class="eyebrow">O que os dois quartos têm em comum</div>
  <div class="h-sec serif">A ripa e a luz,<br><em style="color:var(--gold-lt);">uma por vez.</em></div>
  <hr class="rule">
  <p class="body-t" style="margin-top:4mm;">
  A Paloma desenhou os dois quartos sobre os mesmos dois gestos: o <b>ripado</b> e a
  <b>luz indireta</b>. Nenhum dos dois é comprado pronto — os dois são feitos ripa por
  ripa e cava por cava, na marcenaria.<br><br>
  Só no quarto do Mateus são <b>119 ripas de 2 cm</b>: 72 nas portas do roupeiro, 30 no
  painel da TV, 17 no painel da porta. Cada uma é cortada, bordada nas duas faces longas
  e alinhada com <b>2 cm exatos de vão</b> — se uma sair torta, a parede inteira denuncia.
  É o item de mais artesania do projeto.</p>

  <div class="proc">
    <div><div class="n">01</div><div class="d"><b>Corte.</b> As ripas saem todas da
      mesma chapa, na mesma direção do veio — é o que garante que o tom não varie de
      uma para a outra.</div></div>
    <div><div class="n">02</div><div class="d"><b>Borda.</b> Cada ripa recebe fita nas
      duas faces longas. São <b>566 m de fita</b> só nos ripados dos dois quartos.</div></div>
    <div><div class="n">03</div><div class="d"><b>Cava.</b> A canaleta do LED é usinada
      na própria peça, na face de baixo — a luz aparece, a fita nunca.</div></div>
    <div><div class="n">04</div><div class="d"><b>Alinhamento.</b> Gabarito de montagem
      para os 2 cm de vão. É a etapa que separa ripado de marcenaria de ripado de
      catálogo.</div></div>
  </div>

  <div class="duo2">
    <div><img src="{MTD}" alt="" style="object-position:center 40%;">
      <div class="cap">Mateus · nichos com LED em cava, iluminação indireta</div></div>
    <div><img src="{MND}" alt="" style="object-position:center 35%;">
      <div class="cap">Manuela · nichos iluminados e espelho com perfil de LED</div></div>
  </div>

  <div class="big-q serif" style="color:#fff; font-size:16pt; margin-top:6mm;">
  São <em style="color:var(--gold-lt);">14,6 metros</em> de luz embutida<br>na marcenaria dos dois quartos.</div>

  <div class="pfoot" style="color:#8F8578;"><span class="bl" style="color:#EFE9DC;">valvic<span class="d">.</span> marcenaria</span><span>Mateus &amp; Manuela · A Urbanística</span></div>
</div></div>

<!-- ══════ 3. QUARTO MATEUS ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Quarto 1 · 16,00 m²</div>
  <div class="h-sec serif" style="font-size:22pt;">Mateus.<br><em>Carvalho e azul.</em></div>
  <hr class="rule" style="margin:8px 0 8px;">

  <div class="palette">
    <div><div class="k">MDF Duratex</div><div class="nm">Carvalho Hanover</div>
      <div class="d">Corpo, painéis, ripado e rebaixamento</div></div>
    <div><div class="k">MDF Duratex</div><div class="nm">Azul Astral</div>
      <div class="d">Portas do roupeiro, nicho da cama e painel da TV</div></div>
  </div>

  <div class="qhero"><img src="{MT2}" alt="" style="object-position:center 45%;"></div>
  <div class="cap">Painel ripado, móvel de TV e prateleiras com luz embutida</div>

  <div style="margin-top:4mm;">
    <div class="mv"><div class="t">Roupeiro com portas ripadas <span>290 × 266 × 55 cm</span></div>
      <div class="d">Cinco módulos, <b>4 gavetas</b>, 4 sapateiras basculantes, 2 cabideiros e
      nichos abertos com LED. As <b>72 ripas</b> das portas correm de ponta a ponta, sem
      interrupção nos encontros.</div></div>
    <div class="mv"><div class="t">Móvel de TV com painel ripado <span>275 × 263 cm</span></div>
      <div class="d">Painel ripado em carvalho e fundo em azul · <b>3 prateleiras
      iluminadas</b> (5,50 m de LED) · base de 6 portas com <b>puxador em cava usinada</b>.</div></div>
    <div class="mv"><div class="t">Nicho da cama <span>218 × 166 × 25 cm</span></div>
      <div class="d">Malha de nichos em azul, com <b>fita de LED em cava na face superior
      de cada nicho</b> — 4,95 m de luz indireta, exatamente como a prancha pede.</div></div>
    <div class="mv"><div class="t">Painel com porta mimetizada <span>264 × 122 cm</span></div>
      <div class="d">A porta de 210 × 54 cm <b>desaparece no painel</b>: mesma ripa, mesmo
      alinhamento, sem batente aparente.</div></div>
    <div class="mv"><div class="t">Cabeceira estofada <span>218 × 100 cm</span></div>
      <div class="d">Moldura em carvalho e <b>11 módulos estofados em linho cinza claro</b>,
      de 20 × 90 cm cada — executados por nós, não terceirizados.</div></div>
    <div class="mv"><div class="t">Mesinha de cabeceira e rebaixamento de MDF <span>45 × 40 · 394 × 100 cm</span></div>
      <div class="d">Mesinha com 2 gavetas e frente ripada em azul · forro de MDF em
      carvalho sobre o gesso, acompanhando o eixo da cama.</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Mateus &amp; Manuela · A Urbanística</span></div>
</div></div>

<!-- ══════ 4. QUARTO MANUELA ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Quarto 2 · 13,65 m²</div>
  <div class="h-sec serif" style="font-size:22pt;">Manuela.<br><em>Rosa e Bilbao.</em></div>
  <hr class="rule" style="margin:8px 0 8px;">

  <div class="palette">
    <div><div class="k">MDF Guararapes</div><div class="nm">Rosa Milkshake</div>
      <div class="d">Guarda-roupa, escrivaninha e rack</div></div>
    <div><div class="k">MDF Guararapes</div><div class="nm">Bilbao</div>
      <div class="d">Cabeceira, puxadores e nichos iluminados</div></div>
  </div>

  <div class="qsplit">
    <div class="side"><img src="{MN1}" alt="" style="object-position:center 55%;">
      <div class="cap">Cabeceira em Bilbao · painéis com moldura saliente</div></div>
    <div>
      <div class="mv" style="border-top:2px solid var(--ink);">
        <div class="t">Guarda-roupa <span>295 × 267 × 55 cm</span></div>
        <div class="d"><b>4 portas de abrir + 1 basculante</b> com pistão amortecido ·
        7 gavetas, 4 sapateiras, 3 cabideiros · <b>puxador em Bilbao</b> aplicado na
        própria porta, em contraste com o rosa.</div></div>
      <div class="mv"><div class="t">Cabeceira e painel <span>300 × 100 cm</span></div>
        <div class="d">Três painéis em Bilbao com <b>bordas salientes e miolo rebaixado</b> —
        moldura usinada na peça, não aplicada. <b>3,15 m de LED</b> na cabeceira e
        2,75 m no encontro com o gesso.</div></div>
      <div class="mv"><div class="t">Mesinha de cabeceira <span>50 × 40 × 50 cm</span></div>
        <div class="d">2 gavetas com corrediça oculta, frente ripada em rosa e
        <b>tampo em Bilbao</b>.</div></div>
    </div>
  </div>

  <div class="qhero" style="margin-top:4.5mm;"><img src="{MN2}" alt="" style="height:56mm;object-position:center 42%;"></div>
  <div class="cap">Escrivaninha, rack e os nichos iluminados</div>

  <div style="margin-top:3.5mm;">
    <div class="mv" style="border-top:2px solid var(--ink);">
      <div class="t">Escrivaninha e rack <span>290 × 267 cm · tampo 190 × 75 cm</span></div>
      <div class="d">Tampo de estudo em 18 mm com engrossamento de borda · <b>6 nichos
      iluminados</b> em Bilbao (2,34 m de perfil de LED) · rack com 4 portas e 3
      sapateiras · <b>espelho oval 140 × 47 cm com perfil de LED próprio</b>, executado
      por nós.</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Mateus &amp; Manuela · A Urbanística</span></div>
</div></div>

<!-- ══════ 5. TÉCNICO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">

  <table class="spec-tb" style="margin-top:3mm;">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Chapas</td><td><b>MDF melamínico fosco</b> — Duratex Carvalho Hanover e Azul
        Astral no Mateus · Guararapes Rosa Milkshake e Bilbao na Manuela, exatamente as
        cores do memorial.</td></tr>
      <tr><td>Estrutura</td><td><b>15 mm</b> em toda a caixaria · <b>6 mm</b> nos fundos ·
        <b>18 mm</b> em toda prateleira com mais de 70 cm de vão e nas portas — é o que
        evita o empeno que aparece no segundo verão.</td></tr>
      <tr><td>Dobradiças</td><td><b>Hettich</b> com amortecimento integrado, e
        <b>garantia vitalícia da ferragem</b> pelo fabricante.</td></tr>
      <tr><td>Corrediças</td><td><b>Ocultas com amortecimento</b> nas 13 gavetas dos dois
        quartos — a gaveta fecha sozinha nos últimos centímetros.</td></tr>
      <tr><td>Basculantes</td><td><b>Pistão com amortecimento</b> nas 4 sapateiras do
        Mateus e na porta basculante da Manuela.</td></tr>
      <tr><td>Puxadores</td><td><b>Cava usinada</b> no móvel de TV e nas mesinhas ·
        <b>puxador em MDF Bilbao</b> no guarda-roupa da Manuela · <b>puxador em carvalho</b>
        no roupeiro do Mateus, conforme prancha.</td></tr>
      <tr><td>Iluminação</td><td><b>14,6 m</b> de LED em perfil, embutido em cava usinada
        na marcenaria. Ligação aos pontos previstos no projeto elétrico.</td></tr>
      <tr><td>Estofado e espelho</td><td>Cabeceira do Mateus em <b>linho cinza claro</b> ·
        espelho oval iluminado da Manuela — <b>ambos executados por nós</b>, na mesma
        entrega e sob a mesma garantia.</td></tr>
    </tbody>
  </table>

  <div class="warr">
    <div class="k">Uma obra, um interlocutor</div>
    <div class="big">Quarto de criança<br>tem prazo de verdade.</div>
    <div class="d">São <b>11 móveis, 45 chapas e 4 cores</b> em dois quartos que dividem
    parede. Fabricação, estofamento, espelho e instalação saem da <b>mesma equipe</b> —
    não há um estofador esperando o marceneiro, nem um vidraceiro remarcando visita.
    Uma medição, uma entrega, um responsável.</div>
  </div>

  <div class="split2" style="margin-top:4.5mm;">
    <div><div class="figure"><img src="{MT1}" alt="" style="height:52mm;object-fit:cover;object-position:center 30%;"></div>
      <div class="cap">Mateus · o nicho da cama e o roupeiro ripado</div></div>
    <div><div class="figure"><img src="{MN1}" alt="" style="height:52mm;object-fit:cover;object-position:center 62%;"></div>
      <div class="cap">Manuela · a cabeceira em Bilbao</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Mateus &amp; Manuela · A Urbanística</span></div>
</div></div>

<!-- ══════ 6. INVESTIMENTO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:22pt;">Os dois quartos,<br><em>separados ou juntos.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:1mm;">Projeto executivo, fabricação, estofamento,
  espelho, entrega e instalação. Cada quarto pode ser contratado sozinho — mas os dois
  juntos dividem medição, corte e montagem.</p>

  <div class="qcard">
    <div>
      <div class="k">Quarto 1 · 16,00 m²</div>
      <div class="nm">Mateus<small>Roupeiro ripado · móvel de TV · nicho da cama · painel
        com porta mimetizada · cabeceira estofada · mesinha · rebaixamento</small></div>
      <div class="v">R$ 62.900<small>ou R$ 56.600 à vista</small></div>
    </div>
    <div>
      <div class="k">Quarto 2 · 13,65 m²</div>
      <div class="nm">Manuela<small>Guarda-roupa · cabeceira em Bilbao · mesinha ·
        escrivaninha e rack com nichos iluminados e espelho</small></div>
      <div class="v">R$ 41.200<small>ou R$ 37.100 à vista</small></div>
    </div>
  </div>

  <div class="inv-tot">
    <div>
      <div class="k">Os dois quartos · valor de tabela</div>
      <div class="big">R$ 104.200</div>
    </div>
    <div class="rt">
      <div class="v">R$ 93.800</div>
      <div class="s">à vista · economia de R$ 10.400</div>
    </div>
  </div>

  <div class="pay">
    <div class="r"><span>Entrada 30% + até 10× no cartão</span>
      <span><b>valor de tabela</b> &nbsp; <span class="v">R$ 104.200</span></span></div>
    <div class="r"><span>Entrada 50% + até 8× no cartão &nbsp;<b>−4%</b></span>
      <span class="v">R$ 100.000</span></div>
    <div class="r"><span>Entrada 70% + até 6× no cartão &nbsp;<b>−7%</b></span>
      <span class="v">R$ 96.900</span></div>
    <div class="r g"><span><b>À vista / transferência</b> &nbsp;<b>−10%</b></span>
      <span class="v">R$ 93.800</span></div>
  </div>

  <div class="cond">
    <div><div class="k">Garantia</div><div class="d"><b>10 anos</b> em contrato sobre
      estrutura, montagem e acabamento · <b>2 anos</b> de instalação e regulagem ·
      ferragem Hettich com garantia vitalícia do fabricante.</div></div>
    <div><div class="k">Prazo</div><div class="d"><b>55 a 65 dias corridos</b> para os
      dois quartos, após aprovação e medição final. Um quarto isolado: 40 a 50 dias.</div></div>
    <div><div class="k">Medição</div><div class="d">Conferida no local antes do corte.
      Nada é produzido sem a medição bater com a prancha.</div></div>
    <div><div class="k">Validade</div><div class="d"><b>15 dias corridos</b> a partir
      desta data.</div></div>
  </div>

  <div class="obs">
    <b>Não incluso:</b> tinta e gesso · papel de parede · spots, plafons e pendentes ·
    pontos elétricos · tapete, cadeiras, cortinas e o mapa-múndi decorativo — todos
    previstos no memorial da arquiteta, mas fora do escopo de marcenaria.<br>
    <b>A confirmar com a arquiteta:</b> as peças do nicho da cama do Mateus estão
    desenhadas com <b>5 cm de espessura</b> e foram orçadas assim, em caixa oca. Se a
    especificação admitir 3 cm, reapresentamos o valor antes da produção.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Larissa e Rafael · 31/07/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-quartos-larissa-rafael.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-quartos-larissa-rafael.html', len(HTML))
