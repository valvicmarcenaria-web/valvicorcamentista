# -*- coding: utf-8 -*-
"""Proposta PREMIUM — Casa L&M · Alphaville. 5 páginas, sistema visual Apto CJ/TRT.
Renders extraídos do próprio caderno técnico da arquiteta."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

HERO  = open('/tmp/uri_lm_p31_0.txt').read()   # closet suíte — capa
SALA  = open('/tmp/uri_lm_p08_3.txt').read()   # sala de jantar / painel
COZ   = open('/tmp/uri_lm_p18_1.txt').read()   # cozinha
BANHO = open('/tmp/uri_lm_p39_4.txt').read()   # banheiro
SUITE = open('/tmp/uri_lm_p31_3.txt').read()   # suíte
CLOS2 = open('/tmp/uri_lm_p31_1.txt').read()   # closet 2
CSS   = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .cover .hero-img img{{object-position:center 55%;}}
  .cover .veil{{background:linear-gradient(180deg,
      rgba(22,17,14,.86) 0%, rgba(22,17,14,.34) 26%, rgba(22,17,14,.12) 48%,
      rgba(22,17,14,.55) 76%, rgba(22,17,14,.93) 100%);}}
  .cover .hero-img img{{filter:brightness(1.28) saturate(1.06);}}
  .p-esc .h-sec{{font-size:20pt;}}
  .p-esc .amb{{padding-top:2.2mm; margin-bottom:2.5mm;}}
  .p-esc .amb ul{{line-height:1.44; margin-top:1.5mm; font-size:8.9pt;}}
  .p-esc .amb li{{margin:.5mm 0;}}
  .band{{height:100%; padding:4.5mm 5.5mm;}}
  .band .t{{font-size:12.5pt;}}
  .band .d{{font-size:8.5pt; line-height:1.55; margin-top:1.6mm;}}
  .amb .n small{{font-family:system-ui,sans-serif; font-size:7.4pt; font-weight:400;
      letter-spacing:.02em; color:var(--mut); margin-left:2mm;}}
  /* prova em números — benefícios com evidência */
  .stats{{display:flex; gap:7mm; margin-top:9mm;}}
  .stats > div{{flex:1; border-top:2px solid var(--ink); padding-top:3.2mm;}}
  .stats .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:27pt;
      font-weight:700; line-height:1; color:var(--gold);}}
  .stats .n em{{font-style:normal; font-size:13pt;}}
  .stats .t{{font-size:8.3pt; color:var(--soft); line-height:1.52; margin-top:2mm;}}
  .stats .t b{{color:var(--ink);}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover">
  <div class="hero-img"><img src="{HERO}" alt=""></div>
  <div class="veil"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Casa L&amp;M.</div>
      <div class="sub">Alphaville · projeto executivo 07/2026 — 40 pranchas</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">14 móveis · 6 ambientes</div></div>
      <div class="c"><div class="k">Acabamento</div><div class="v">Duratex Carvalho</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich · Alemanha</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. COPY ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Antes do preço</div>
  <hr class="rule">
  <div class="big-q serif">Num projeto deste tamanho, o orçamento<br>
  mais barato quase sempre é o que <b>leu menos</b>.</div>

  <p class="body-t" style="margin-top:6mm;">
  O caderno da sua arquiteta tem <b>40 pranchas</b>. E quase metade dos móveis
  encosta em algo que <b>já existe</b> na casa: bancada de granito, armário da
  cozinha, prateleira da despensa, gaveta do banheiro.<br><br>
  Quem orça por metro linear tem só dois caminhos, e os dois custam caro para você:
  <b>cobrar pelo que você já tem</b>, ou descobrir na montagem que a bancada existente
  não bate com o móvel novo — com a obra parada e o marceneiro pedindo aditivo.<br><br>
  Por isso esta proposta não começou por um preço. Começou pela leitura
  <b>prancha a prancha</b>: cada armário decomposto em <b>plano de corte</b>, cada
  ferragem contada uma a uma, antes de qualquer número ser escrito.</p>

  <div style="margin-top:6mm;" class="split2">
    <div>
      <div class="figure"><img src="{SALA}" alt=""></div>
      <div class="cap">Sala de jantar · painel em Carvalho Batur</div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:center;">
      <div class="pull">
        <div class="t">O que a leitura<br>encontrou.</div>
        <div class="d">As bandejas da sapateira têm <b>24,5 cm de profundidade</b> — e
        <b>não existe corrediça oculta nessa medida</b>. Especificamos telescópica ali,
        e mantivemos a oculta nas 20 gavetas do closet, que têm profundidade para isso.<br><br>
        Achamos <b>antes</b>. O jeito caro de descobrir isso é com a ferragem comprada
        e a gaveta pronta.</div>
      </div>
    </div>
  </div>

  <p class="body-t" style="margin-top:5mm;">
  <b>A premissa é essa:</b> você não precisa do marceneiro mais barato. Precisa de um
  que leia o projeto inteiro, diga o que já está pronto e <b>não te venda o que você já tem</b>.</p>

  <div class="stats">
    <div>
      <div class="n">40</div>
      <div class="t"><b>pranchas lidas, uma a uma.</b> Plantas, elevações, cortes e
      detalhes — inclusive os que dizem o que já existe na casa.</div>
    </div>
    <div>
      <div class="n">70</div>
      <div class="t"><b>chapas calculadas no plano de corte.</b> Peça a peça, encaixadas
      na chapa de 2,75 × 1,85 m. Nada foi estimado por metro linear.</div>
    </div>
    <div>
      <div class="n">10 <em>anos</em></div>
      <div class="t"><b>de garantia formal em contrato.</b> Equipe própria do corte à
      instalação, com CNC próprio — sem terceirizar a sua obra.</div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville</span></div>
</div></div>

<!-- ══════ 3. ESCOPO ══════ -->
<div class="page p-esc"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif">Catorze móveis,<br><em>lidos do executivo.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:2.5mm;font-size:12pt;">Fornecimento e instalação, conforme o caderno
  técnico de 07/2026.</p>

  <div class="amb">
    <div class="n">Sala de jantar <span class="badge">Carvalho Batur</span></div>
    <div class="s">Painel de 30 mm · três faces</div>
    <ul>
      <li><b>Painel de 850 cm</b> no total (382 + 288 + 180), com 256 de altura, sobre
          estrutura de fixação própria e afastado do piso.</li>
      <li><b>Porta pivotante mimetizada</b> 86,5 × 210 — some no painel, com puxador em
          cava usinado e alça em inox preto do lado da cozinha.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Cozinha <span class="badge">Branco Ártico + Grafite</span></div>
    <div class="s">Aéreo em L · torre e gabinete</div>
    <ul>
      <li><b>Aéreo em L de 329 cm</b> em Branco Ártico, com recorte para a coifa de embutir
          e fita de LED sob a base.</li>
      <li><b>Torre e gabinete de 234 cm</b> na cor grafite do existente, com gavetões,
          porta-tempero e <b>6 prateleiras sobre corrediça</b>.</li>
      <li>Reorganização dos <b>módulos existentes</b> e sóculo novo no mesmo padrão.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Despensa</div>
    <div class="s">Armário alto, baixo e piso-teto</div>
    <ul>
      <li><b>292 cm de armário alto</b> (8 portas) e <b>292 cm de gaveteiro</b> —
          11 gavetas, três delas com <b>fundo em chapa metálica perfurada preta</b>.</li>
      <li><b>Piso-teto de 286 cm</b> com 5 bandejas deslizantes e ganchos de limpeza.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Suíte <span class="badge">maior conjunto</span></div>
    <div class="s">Closet em U · roupeiro · sapateira — Carvalho Brun</div>
    <ul>
      <li><b>Closet em U de 241,5 × 220 cm</b>, 280 de altura: 20 gavetas com corrediça
          oculta, 13 prateleiras, cabideiros em metal e <b>prateleiras iluminadas</b>.</li>
      <li><b>Roupeiro de 151 cm</b> com lateral curva e <b>sapateira de 113 cm</b> com
          13 bandejas e LED vertical de 267 cm.</li>
      <li><b>8 portas em vidro reflecta</b> com estrutura metálica cinza grafite.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Banheiros e lavabo <span class="badge">5 ambientes</span></div>
    <div class="s">Carvalho Brun · puxador em cava 45°</div>
    <ul>
      <li>Armários da <b>suíte, visita, banho 02, banho 03 e lavabo</b>, com gavetas sobre
          corrediça telescópica e cesto de roupa embutido.</li>
      <li>Todos ajustados às <b>bancadas de granito existentes</b>, com furo de sifão
          conferido no local.</li>
    </ul>
  </div>

  <div class="split2" style="margin-top:1mm;">
    <div><div class="figure"><img src="{COZ}" alt="" style="height:30mm;object-fit:cover;object-position:center 45%;"></div>
      <div class="cap">Cozinha · aéreo em L e torre grafite</div></div>
    <div><div class="figure"><img src="{BANHO}" alt="" style="height:30mm;object-fit:cover;object-position:center 62%;"></div>
      <div class="cap">Banheiro · gaveteiro em Carvalho Brun</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville</span></div>
</div></div>

<!-- ══════ 4. TÉCNICO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:5mm;">Uma casa inteira é usada todos os dias, por
  todo mundo. A diferença aparece no terceiro ano.</p>

  <table class="spec-tb">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Painéis e armários</td><td><b>MDF Duratex</b> — Carvalho Batur na sala,
        Carvalho Brun na suíte e banheiros, Branco Ártico e Cinza Chumbo na cozinha
        e despensa. Veio orientado e casado entre peças adjacentes.</td></tr>
      <tr><td>Estrutura</td><td><b>15 mm</b> em caixaria, portas e gavetas · <b>18 mm</b>
        em prateleiras longas, que evita a flecha no vão de 1,60 m · <b>6 mm</b> em fundos.</td></tr>
      <tr><td>Dobradiças</td><td><b>Hettich Sensys Black</b>, com amortecimento integrado
        ao corpo. Fecho suave em qualquer velocidade.</td></tr>
      <tr><td>Corrediças</td><td><b>Hettich Quadro — corrediça oculta</b> nas gavetas do
        closet, do piso-teto e do banho da suíte: a gaveta abre inteira e a ferragem
        desaparece. <b>Telescópica</b> onde a profundidade não comporta a oculta.</td></tr>
      <tr><td>Portas em vidro</td><td><b>Reflecta com estrutura metálica cinza grafite</b>,
        8 folhas de 2,71 m — cotadas e fechadas com o fornecedor <b>antes</b> desta proposta,
        não estimadas.</td></tr>
      <tr><td>Puxadores</td><td><b>Cava usinada a 45°</b> no próprio MDF em 46 peças — sem
        ferragem aparente. Metálico cinza grafite nas portas de vidro.</td></tr>
      <tr><td>Iluminação</td><td><b>Fita LED 3000K e 4000K</b> com <b>lente difusora</b> e
        perfil de embutir de 15 mm — <b>20,9 m</b> no closet, na sapateira e na cozinha.
        Luz contínua, sem ponto quente.</td></tr>
      <tr><td>Detalhe especial</td><td><b>Chapa metálica perfurada 3 mm preta</b> no fundo
        de três gavetas da despensa, com quadro em MDF — ventilação para o que não pode abafar.</td></tr>
    </tbody>
  </table>

  <div class="split2" style="margin-top:5mm;">
    <div class="pull" style="background:var(--deep);border-left-color:var(--gold-lt);">
      <div class="t" style="color:#fff;">Ferragem alemã.<br>Hettich desde 1888.</div>
      <div class="d" style="color:#C6BFB2;">Cada dobradiça é testada para
      <b style="color:#F0E7D6;">80 mil ciclos</b>: abrir e fechar a porta 10 vezes por dia
      durante 20 anos. Numa casa com cinco banheiros e uma cozinha em uso diário, é o que
      separa a porta que continua macia da que começa a bater.</div>
    </div>
    <div class="pull" style="background:var(--cream);border-left-color:var(--ink);">
      <div class="t">10 anos de garantia</div>
      <div class="d"><b>10 anos</b> na marcenaria — estrutura, montagem e acabamento.<br>
      <b>2 anos</b> na instalação e regulagem. Garantia formal em contrato.<br><br>
      <b>Equipe própria do corte à instalação</b>, com CNC próprio — cada peça sai do plano
      de corte conferido, não do improviso de obra.</div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville</span></div>
</div></div>

<!-- ══════ 5. INVESTIMENTO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:21pt;">Preço fechado,<br><em>por ambiente.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">

  <div class="inv-hero">
    <div class="k">Marcenaria completa · à vista</div>
    <div class="v serif">R$ 191.400</div>
    <div class="c">Catorze móveis em seis ambientes — fornecimento, produção e instalação
    por equipe própria, com ferragens Hettich, portas em vidro e iluminação LED.</div>
    <div class="alt">Ou <b>R$ 212.700</b> em <b>50% na assinatura + 50% na entrega</b>.
    O valor à vista já traz <b>10% de desconto</b>.</div>
  </div>

  <table class="item-tb">
    <thead><tr><th>Ambiente</th><th class="r">Preço</th></tr></thead>
    <tbody>
      <tr><td class="nm">Suíte — closet, roupeiro e sapateira<small>Carvalho Brun · 8 portas em vidro reflecta · 20 gavetas com corrediça oculta</small></td><td class="r">R$ 124.500</td></tr>
      <tr><td class="nm">Cozinha — aéreo em L, torre e gabinete<small>Branco Ártico e Cinza Chumbo · inclui reorganizar os módulos existentes</small></td><td class="r">R$ 30.300</td></tr>
      <tr><td class="nm">Sala de jantar — painel e porta pivotante<small>Carvalho Batur 30 mm · 850 cm de painel</small></td><td class="r">R$ 24.800</td></tr>
      <tr><td class="nm">Banheiros e lavabo — 5 ambientes<small>Carvalho Brun · sobre as bancadas de granito existentes</small></td><td class="r">R$ 19.300</td></tr>
      <tr><td class="nm">Despensa — armário alto, gaveteiro e piso-teto<small>11 gavetas · três com fundo em chapa perfurada</small></td><td class="r">R$ 13.800</td></tr>
      <tr class="tot"><td>Total · à vista</td><td class="r">R$ 191.400</td></tr>
    </tbody>
  </table>

  <div class="terms">
    <div class="term"><div class="k">Pagamento</div><div class="v">À vista<br>−10%</div></div>
    <div class="term"><div class="k">Prazo</div><div class="v">70 a 90<br>dias corridos</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">10 anos</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">15 dias<br>corridos</div></div>
  </div>

  <div class="note">
    <b>Incluso:</b> fornecimento, produção e instalação dos 14 móveis · ferragens Hettich ·
    8 portas em vidro reflecta com estrutura metálica · fita LED com perfil e lente difusora ·
    chapa metálica perfurada · reorganização dos módulos existentes da cozinha.<br>
    <b>Não incluso — já existe ou é de outro fornecedor:</b> bancadas em granito (cozinha e
    banheiros) · forro de gesso, tabica e cortineiro iluminado · espelhos · armários inferiores
    e prateleiras existentes · coifa, cooktop e demais eletrodomésticos · cesta elevatória ·
    pontos elétricos e hidráulicos · obra civil.<br>
    <b>Premissas:</b> medidas do executivo <b>conferidas no local</b> antes da produção —
    em especial as bancadas existentes e o furo de sifão · elevação V1 do closet a confirmar
    com a arquiteta (se for um conjunto adicional de portas, será orçado à parte) ·
    cores confirmadas em amostra antes do corte.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville · 28/07/2026</span></div>
</div></div>

</body></html>"""

(P/'casa-lm'/'proposta-casa-lm.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-casa-lm.html', len(HTML))
