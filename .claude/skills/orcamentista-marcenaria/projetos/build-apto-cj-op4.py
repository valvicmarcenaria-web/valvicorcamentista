# -*- coding: utf-8 -*-
"""APTO CJ — VERSÃO REDUZIDA DA OPÇÃO 4  [Jonathan 04/08/2026]

A cliente optou pela configuração 4 do folder de 8 páginas:
  entrada e varanda em LÂMINA NATURAL (mantidas) + estante 100% MELAMÍNICO FOSCO
  NA COR (sem laca, dentro e fora) + adega em serralheria.
  R$ 48.700 à vista — valor MANTIDO, sem recálculo.

Fechado 4 páginas: capa · ambientes · técnico · investimento.
Fora: as 6 configurações, a tabela por item e a página conceitual da laca —
a laca saiu do escopo, vender laca aqui seria vender o que não vai ser feito.

ALTERAÇÃO DE LAYOUT: as portas inferiores da estante, antes DE CORRER, passam a
ser DE GIRO com dobradiças Hettich. O motor nunca carregou sistema deslizante —
`FERR[C]` sempre teve 26 Sensys, das quais 2×3 são exatamente essas portas da
base. Custo inalterado (e de giro sai ~R$ 193 mais barato que o deslizante seria).

Só a coluna À VISTA, a pedido.
"""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HERO    = open('/tmp/uri_cj_hero.txt').read()      # entrada em freijó — capa
GOURMET = open('/tmp/uri_cj_gourmet.txt').read()   # varanda gourmet ambientada
ELEV    = open('/tmp/uri_cj_elev.txt').read()      # render frontal 636 cm na cor
EST2    = open('/tmp/uri_cj_est2.txt').read()      # cristaleira + nicho + bancada
EST3    = open('/tmp/uri_cj_est3.txt').read()      # painel de TV + portas altas

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  .texband{{margin-top:4mm; border-radius:5px; overflow:hidden;}}
  .texband img{{width:100%; height:54mm; object-fit:cover; object-position:center 45%; display:block;}}

  .swap{{display:flex; gap:0; margin-top:4.5mm; border-top:2px solid var(--ink);
      border-bottom:1px solid var(--line); padding:4.6mm 0;}}
  .swap > div{{flex:1; padding-left:7mm; border-left:1px solid var(--line);}}
  .swap > div:first-child{{padding-left:0; border-left:0;}}
  .swap .k{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase;
      color:var(--gold); font-weight:700;}}
  .swap .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:14pt; font-weight:700;
      color:var(--ink); line-height:1.15; margin-top:1mm;}}
  .swap .d{{font-size:8.6pt; color:var(--soft); line-height:1.6; margin-top:1.3mm;}}
  .swap .d b{{color:var(--ink);}}

  .warr-big{{background:var(--deep); border-left:3px solid var(--gold-lt);
      border-radius:0 5px 5px 0; padding:5.5mm 7mm; margin-top:6mm;}}
  .warr-big .k{{font-size:6.8pt; letter-spacing:.2em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700;}}
  .warr-big .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:23pt;
      font-weight:700; color:#fff; line-height:1.1; margin-top:1.6mm;}}
  .warr-big .d{{font-size:8.8pt; color:#C6BFB2; line-height:1.6; margin-top:2.2mm;}}
  .warr-big .d b{{color:#F0E7D6;}}

  .cond2{{display:grid; grid-template-columns:1fr 1fr; gap:6mm 8mm; margin-top:9mm;
      border-top:2px solid var(--ink); padding-top:5mm;}}
  .cond2 .k{{font-size:6.6pt; letter-spacing:.16em; text-transform:uppercase;
      color:var(--gold); font-weight:700;}}
  .cond2 .d{{font-size:9.4pt; color:var(--soft); line-height:1.6; margin-top:1.2mm;}}
  .cond2 .d b{{color:var(--ink);}}

  .spec-tb td:first-child{{width:42mm;}}
  .spec-tb td{{padding:2.2mm 0;}}
  .spec-tb{{font-size:9.1pt;}}

  .inv-hero{{padding:13mm 8mm !important;}}
  .inv-hero .v{{font-size:52pt !important; margin:2.5mm 0 1.5mm !important;}}
  .itn{{display:flex; margin-top:6.5mm; padding-top:5mm;
      border-top:1px solid rgba(201,169,106,.30);}}
  .itn > div{{flex:1; padding-left:6mm; border-left:1px solid rgba(201,169,106,.18);}}
  .itn > div:first-child{{padding-left:0; border-left:0;}}
  .itn b{{display:block; font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt;
      font-weight:700; color:var(--gold-lt); line-height:1.1;}}
  .itn span{{display:block; font-size:8.2pt; color:#C6BFB2; margin-top:1.6mm; line-height:1.5;}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover">
  <div class="hero-img"><img src="{HERO}" alt=""></div>
  <div class="veil"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Apartamento CJ.</div>
      <div class="sub">Projeto B+G Estúdio · Belo Horizonte</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">3 ambientes + adega</div></div>
      <div class="c"><div class="k">Destaque</div><div class="v">Lâmina natural de Freijó</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich · Alemanha</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. OS AMBIENTES ══════ -->
<div class="page p-esc"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif">Três ambientes,<br><em>e uma adega.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:3mm;">Conforme o projeto executivo do B+G Estúdio.
  <b>A lâmina natural permanece</b> na entrada e na varanda; a estante vai em
  <b>melamínico fosco na cor</b>, dentro e fora.</p>

  <div class="amb">
    <div class="n">Entrada <span class="badge">lâmina natural</span></div>
    <div class="s">Móvel suspenso em Freijó</div>
    <ul>
      <li>Móvel suspenso com <b>2 gavetões para sapatos</b> e 2 portas, frentes em
          <b>lâmina natural de Freijó</b> com veio contínuo.</li>
      <li><b>Puxador em cava 45°</b> usinado no próprio móvel · interior em Freijó melamínico.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Varanda gourmet <span class="badge">lâmina natural</span></div>
    <div class="s">Ripado em Freijó · bancada de granito da marmoraria</div>
    <ul>
      <li>Armário superior e inferior com <b>portas ripadas em lâmina natural</b> —
          cada ripa acabada individualmente, nas três faces.</li>
      <li>Vão dimensionado para <b>cervejeira</b> · apoio para a bancada de granito.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Salas de TV e jantar <span class="badge">melamínico fosco na cor</span></div>
    <div class="s">636 × 232 cm · na cor do projeto, por inteiro</div>
    <ul>
      <li><b>Estante de parede inteira</b>: painel de TV, armários altos, gavetas,
          nichos e <b>cristaleira com 4 portas de vidro</b> e puxadores dourados.</li>
      <li>Executada como <b>móvel novo</b>, em melamínico fosco <b>na mesma cor por
          dentro e por fora</b> — o tom não muda ao abrir a porta.</li>
      <li>As <b>portas inferiores são de giro</b>, com dobradiças <b>Hettich</b> de
          amortecimento integrado.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Adega <span class="badge">serralheria</span></div>
    <div class="s">Estrutura metálica para vinhos</div>
    <ul>
      <li>Adega vertical em serralheria, integrada à parede da entrada.</li>
    </ul>
  </div>

  <div class="split2" style="margin-top:2mm;">
    <div><div class="figure"><img src="{GOURMET}" alt="" style="height:33mm;object-fit:cover;object-position:center 42%;"></div>
      <div class="cap">Varanda gourmet · ripado em Freijó</div></div>
    <div><div class="figure"><img src="{EST3}" alt="" style="height:33mm;object-fit:cover;object-position:center 55%;"></div>
      <div class="cap">Salas · painel de TV e portas altas</div></div>
    <div><div class="figure"><img src="{EST2}" alt="" style="height:33mm;object-fit:cover;object-position:center 42%;"></div>
      <div class="cap">Cristaleira, nichos e bancada</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 3. TÉCNICO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif" style="font-size:26pt;">A mesma cor,<br><em>o mesmo desenho.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">

  <div class="texband"><img src="{ELEV}" alt=""></div>
  <div class="cap" style="margin-top:1.8mm;">Estante das salas · 636 cm de parede na cor
    definida pelo B+G Estúdio</div>

  <div class="swap">
    <div><div class="k">O que permanece</div><div class="t">A lâmina.</div>
      <div class="d">Entrada e varanda seguem em <b>lâmina natural de Freijó</b> — veio
      contínuo, ripado acabado peça a peça. É a madeira de verdade, e ela não saiu.</div></div>
    <div><div class="k">Na estante</div><div class="t">Melamínico fosco.</div>
      <div class="d">A cor é a mesma do projeto, <b>dentro e fora</b>. O acabamento vem
      curado de fábrica — uniforme em toda a peça e mais <b>resistente à abrasão do dia
      a dia</b> que uma pintura aplicada em obra.</div></div>
    <div><div class="k">Honestidade</div><div class="t">A borda aparece.</div>
      <div class="d">O melamínico tem <b>fita de borda</b>: existe a linha onde a face
      termina. É a diferença real para a laca — e é dela que vem a economia.</div></div>
  </div>

  <table class="spec-tb" style="margin-top:5mm;">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Entrada e varanda</td><td><b>Lâmina natural de Freijó</b> nas frentes, com
        veio contínuo · interior em Freijó melamínico — o tom continua ao abrir.</td></tr>
      <tr><td>Estante das salas</td><td><b>Melamínico fosco na cor do projeto</b>, faces
        externas e interior. <b>Sem laca.</b></td></tr>
      <tr><td>Estrutura</td><td><b>15 mm</b> na caixaria · <b>18 mm</b> nas portas e em
        toda prateleira de vão longo — é o que evita o empeno que aparece no segundo verão.</td></tr>
      <tr><td>Portas inferiores</td><td><b>De giro</b>, com dobradiças <b>Hettich Sensys</b>
        de amortecimento integrado — a porta desacelera sozinha e encosta macia em
        qualquer velocidade.</td></tr>
      <tr><td>Portas altas e cristaleira</td><td><b>Hettich Sensys</b> · as 4 portas de
        vidro da cristaleira com <b>caixilho</b> e puxador em <b>dourado fosco</b>.</td></tr>
      <tr><td>Gavetas</td><td>Corrediça <b>oculta com amortecimento</b> · puxador em
        <b>cava 45°</b> usinada na própria frente, sem nada aplicado.</td></tr>
      <tr><td>Adega</td><td><b>Serralheria</b> sob medida, integrada à parede da entrada.</td></tr>
      <tr><td>Instalação</td><td>Equipe própria, do corte ao parafuso final. Medição
        conferida no local antes da produção.</td></tr>
    </tbody>
  </table>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 4. INVESTIMENTO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:26pt;">Os quatro móveis,<br><em>instalados.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:4mm;">Fornecimento, ferragens Hettich, entrega e
  instalação inclusos.</p>

  <div class="inv-hero">
    <div class="k">Apartamento CJ · 3 ambientes + adega</div>
    <div class="v">R$ 48.700</div>
    <div class="c">Entrada e varanda em lâmina natural de Freijó · estante das salas em
      melamínico fosco na cor · adega em serralheria</div>
    <div class="itn">
      <div><b>Entrada</b><span>móvel suspenso em lâmina natural</span></div>
      <div><b>Varanda</b><span>ripado em lâmina natural, vão de cervejeira</span></div>
      <div><b>Salas</b><span>estante de 636 cm na cor</span></div>
      <div><b>Adega</b><span>serralheria sob medida</span></div>
    </div>
  </div>

  <div class="cond2">
    <div><div class="k">Condição</div><div class="d"><b>À vista / transferência.</b>
      Valor fechado, sem acréscimo.</div></div>
    <div><div class="k">Prazo de entrega</div><div class="d"><b>50 a 60 dias corridos</b>
      após a aprovação e a medição final no local.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d"><b>15 dias corridos</b>
      a partir desta data.</div></div>
    <div><div class="k">Ferragens</div><div class="d"><b>Hettich</b> · Alemanha, em todo
      o projeto.</div></div>
  </div>

  <div class="warr-big">
    <div class="k">Garantia</div>
    <div class="big">10 anos. Em contrato.</div>
    <div class="d">Marcenaria sob medida costuma sair com <b>1 a 3 anos</b> de garantia —
    quando sai por escrito. A nossa é de <b>10 anos</b> sobre estrutura, montagem e
    acabamento, mais <b>2 anos</b> de instalação e regulagem. Conseguimos assinar isso
    porque a equipe é <b>própria do corte à instalação</b>.</div>
  </div>

  <div class="note" style="margin-top:5.5mm;">
    <b>Não incluso:</b> espelhos · relaqueamento do móvel existente (avaliação in loco) ·
    granito e frontão (marmoraria) · pontos elétricos.<br>
    <b>Medição:</b> conferida no local antes do corte — nada entra em máquina sem conferência.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · 04/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-apto-cj-op4.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-apto-cj-op4.html', len(HTML))
