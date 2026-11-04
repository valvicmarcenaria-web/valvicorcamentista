# -*- coding: utf-8 -*-
"""Proposta PORTO VERDE (Leonardo) V2 — escritório.
Valores FECHADOS pelo Jonathan (não calculados pelo motor). 5 páginas.
Capa tipográfica — trocar por render quando as imagens chegarem como arquivo."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  /* capa tipográfica — sem foto */
  .cover-t{{background:var(--deep); position:relative; overflow:hidden;}}
  .cover-t::before{{content:""; position:absolute; inset:0;
     background:radial-gradient(120% 80% at 18% 12%, rgba(201,169,106,.16) 0%, transparent 58%),
                radial-gradient(90% 70% at 88% 96%, rgba(201,169,106,.10) 0%, transparent 60%);}}
  .cover-t .rules{{position:absolute; inset:0;
     background:repeating-linear-gradient(90deg, rgba(255,255,255,.030) 0 1px, transparent 1px 34mm);}}
  .stats{{display:flex; gap:7mm; margin-top:8mm;}}
  .stats > div{{flex:1; border-top:2px solid var(--ink); padding-top:3.2mm;}}
  .stats .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:26pt;
      font-weight:700; line-height:1; color:var(--gold);}}
  .stats .n em{{font-style:normal; font-size:12.5pt;}}
  .stats .t{{font-size:8.3pt; color:var(--soft); line-height:1.52; margin-top:2mm;}}
  .stats .t b{{color:var(--ink);}}
  .p-esc .amb{{padding-top:2.6mm; margin-bottom:4.2mm;}}
  .p-esc .amb ul{{line-height:1.5; margin-top:1.8mm;}}
  .fora{{background:var(--cream); border-left:3px solid var(--ink); border-radius:0 5px 5px 0;
      padding:4mm 6mm; margin-top:4.5mm;}}
  .fora .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:13pt; font-weight:700;}}
  .fora .d{{font-size:8.5pt; color:var(--soft); line-height:1.6; margin-top:1.6mm;}}
  .fora .d b{{color:var(--ink);}}
  .warr-big{{background:var(--deep); border-radius:6px; padding:4.6mm 7mm; margin-top:4.5mm;
      position:relative; overflow:hidden; box-shadow:inset 0 0 0 1px rgba(201,169,106,.30);}}
  .warr-big::after{{content:""; position:absolute; left:0; top:0; bottom:0; width:4px;
      background:var(--gold-lt);}}
  .warr-big .k{{font-size:7.2pt; letter-spacing:.2em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700;}}
  .warr-big .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:22pt;
      font-weight:700; color:#fff; line-height:1.12; margin-top:1.6mm;}}
  .warr-big .d{{font-size:8.5pt; color:#C6BFB2; line-height:1.55; margin-top:2mm;}}
  .warr-big .d b{{color:#F0E7D6;}}
  .pay2{{display:flex; margin-top:3mm; padding-top:2.6mm;
      border-top:1px solid rgba(201,169,106,.28);}}
  .pay2 > div{{flex:1; padding-left:6mm; border-left:1px solid rgba(201,169,106,.18);}}
  .pay2 > div:first-child{{padding-left:0; border-left:0;}}
  .pay2 b{{display:block; font-family:'Cormorant Garamond',Georgia,serif; font-size:18pt;
      font-weight:700; color:var(--gold-lt); line-height:1;}}
  .pay2 span{{display:block; font-size:7.8pt; color:#C6BFB2; margin-top:1.2mm;}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover cover-t">
  <div class="rules"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria corporativa</div>
      <div class="tit">Porto Verde.</div>
      <div class="sub">Escritório · Leonardo — revisão sobre o projeto 3D</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">5 frentes</div></div>
      <div class="c"><div class="k">Execução</div><div class="v">Marcenaria · serralheria</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich · Alemanha</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. COPY ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Antes do preço</div>
  <hr class="rule">
  <div class="big-q serif">Num escritório, a marcenaria não decora.<br>
  Ela <b>é a arquitetura</b>.</div>

  <p class="body-t" style="margin-top:6mm;">
  Aqui os painéis não são revestimento — são as paredes que o seu cliente vê quando entra.
  A porta do banheiro e a da sala de reunião <b>somem dentro deles</b>. As portas altas
  abrem ao toque, <b>sem puxador quebrando o plano</b>. E a mesa central esconde
  <b>até 20 tomadas</b> dentro da própria estrutura.<br><br>
  Isso só fecha se marcenaria, serralheria e iluminação forem pensadas juntas, pela mesma
  mão. Quando são três fornecedores diferentes, a folga aparece sempre no mesmo lugar: o
  metalon que não bate com a caixaria, o LED que sobra no nicho, a porta mimetizada que
  denuncia o vão.<br><br>
  <b>Aqui é tudo nosso.</b> Uma equipe, um cronograma, um responsável.</p>

  <div class="pull" style="margin-top:6mm;">
    <div class="t">Duas portas que desaparecem.</div>
    <div class="d">A do banheiro e a da sala de reunião são <b>mimetizadas</b>: mesma folha,
    mesmo veio, mesma linha de sombra do painel. Fechadas, você não acha onde estão.
    Abertas, funcionam com <b>sistema pivotante e fecho rolete</b> — e por dentro levam
    <b>estrutura de aço anti-empeno</b>, porque folha de porta alta sem reforço entorta
    com o tempo e passa a raspar.</div>
  </div>

  <div class="stats">
    <div>
      <div class="n">5</div>
      <div class="t"><b>frentes num único contrato.</b> Da mesa central ao painel do
      banheiro, um só responsável pelo conjunto.</div>
    </div>
    <div>
      <div class="n">2</div>
      <div class="t"><b>ofícios sob o mesmo teto.</b> Marcenaria e serralheria saem da
      mesma produção, com a mesma conferência de medida.</div>
    </div>
    <div>
      <div class="n">10 <em>anos</em></div>
      <div class="t"><b>de garantia formal em contrato.</b> Equipe própria do corte à
      instalação.</div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Porto Verde · Leonardo</span></div>
</div></div>

<!-- ══════ 3. ESCOPO ══════ -->
<div class="page p-esc"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif">Cinco frentes,<br><em>um só conjunto.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:4mm;">Fornecimento, produção e instalação por equipe
  própria.</p>

  <div class="amb">
    <div class="n">Parede lado direito — completa <span class="badge">maior frente</span></div>
    <div class="s">Estante com torres e nichos iluminados</div>
    <ul>
      <li>Torres e <b>nichos iluminados</b>, com painéis complementares de acabamento
          fechando o conjunto de ponta a ponta.</li>
      <li>Estrutura com <b>3 gavetas</b> e <b>puxadores em cava</b> usinada.</li>
      <li><b>Prateleiras em serralheria</b> com <b>vidro incolor temperado 8 mm</b>.</li>
      <li><b>Portas com abertura por toque</b> — sem puxador aparente.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Mesas centrais</div>
    <div class="s">MDF melamínico fosco · estrutura em metalon</div>
    <ul>
      <li>Estrutura em <b>metalon</b> com <b>pé em acabamento treliçado</b>.</li>
      <li><b>2 gaveteiros volantes</b> com 3 gavetas cada.</li>
      <li><b>Caixas elétricas embutidas</b> — até <b>20 tomadas 10A</b> na própria mesa.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Sala de reunião — painéis</div>
    <div class="s">Painel de TV · painel com porta mimetizada</div>
    <ul>
      <li><b>Painel central para televisão.</b></li>
      <li><b>Painel com porta mimetizada</b> para a sala de reunião.</li>
      <li><b>3 prateleiras suspensas</b> com <b>suporte oculto</b>.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Sala de reunião — mesa oval</div>
    <div class="s">Tampo em MDF melamínico fosco · base cônica laqueada</div>
    <ul>
      <li>Mesa oval com <b>tampo em MDF melamínico fosco</b>.</li>
      <li><b>Base cônica</b> com acabamento <b>laqueado</b>.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Painel frontal do banheiro</div>
    <div class="s">Parede completa com porta mimetizada</div>
    <ul>
      <li>Painel de <b>parede completa</b>, com <b>porta mimetizada</b> integrada —
          pivotante, fecho rolete e estrutura de aço anti-empeno.</li>
    </ul>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Porto Verde · Leonardo</span></div>
</div></div>

<!-- ══════ 4. TÉCNICO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:4mm;">Um escritório é usado oito horas por dia,
  todos os dias. A diferença aparece no segundo ano.</p>

  <table class="spec-tb">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Painéis e caixaria</td><td><b>MDF melamínico fosco.</b> Linha e cor a definir
        com você na aprovação — <b>não contempla a linha Acetinato</b>.</td></tr>
      <tr><td>Serralheria</td><td>Metalon com <b>pintura eletrostática</b> — acabamento de
        forno, uniforme e muito mais resistente a risco que pintura líquida.</td></tr>
      <tr><td>Portas</td><td><b>Estrutura de aço anti-empeno</b> por dentro da folha.
        Porta alta sem reforço entorta com o tempo e passa a raspar no batente.</td></tr>
      <tr><td>Fechaduras e abertura</td><td><b>Fecho rolete</b> e <b>sistema pivotante</b>
        nas portas mimetizadas · <b>abertura por toque</b> nas portas altas.</td></tr>
      <tr><td>Puxadores</td><td><b>Cava usinada</b> no próprio MDF — sem ferragem aparente
        quebrando o plano do painel.</td></tr>
      <tr><td>Dobradiças</td><td><b>Hettich</b>, alemã, com amortecimento integrado ao corpo.
        Fecho suave em qualquer velocidade.</td></tr>
      <tr><td>Prateleiras da estante</td><td><b>Serralheria + vidro incolor temperado 8 mm</b>
        — vão livre sem montante no meio.</td></tr>
      <tr><td>Iluminação</td><td><b>Fita de LED</b> com perfil embutido nos nichos, alinhada
        com o elétrico da obra.</td></tr>
      <tr><td>Elétrica da mesa</td><td><b>Caixas embutidas para até 20 tomadas 10A</b>,
        com passagem usinada na própria estrutura.</td></tr>
    </tbody>
  </table>

  <div class="fora">
    <div class="t">O que não está incluído</div>
    <div class="d"><b>Esquadria de alumínio e vidros</b> — as divisórias e portas de vidro
    com perfil metálico que aparecem no projeto <b>não fazem parte desta proposta</b> e
    devem ser contratadas com o fornecedor de esquadrias.<br>
    Também fora: pontos elétricos e hidráulicos · gesso, pintura e obra civil ·
    mobiliário solto (cadeiras) · televisão e eletrodomésticos.</div>
  </div>

  <div class="warr-big">
    <div class="k">Garantia</div>
    <div class="big">10 anos. Em contrato.</div>
    <div class="d">Marcenaria sob medida costuma sair com <b>1 a 3 anos</b> de garantia —
    quando sai por escrito. A nossa é de <b>10 anos</b> sobre estrutura, montagem e
    acabamento, mais <b>2 anos</b> de instalação e regulagem.<br>
    Conseguimos assinar isso porque a equipe é <b>própria do corte à instalação</b> —
    não há terceiro para quem empurrar o defeito.</div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Porto Verde · Leonardo</span></div>
</div></div>

<!-- ══════ 5. INVESTIMENTO ══════ -->
<div class="page p-inv"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:21pt;">Preço fechado,<br><em>por frente.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">

  <div class="inv-hero" style="box-shadow:inset 0 0 0 1px rgba(201,169,106,.30);">
    <div class="k">Marcenaria completa · 5 frentes</div>
    <div class="v serif">R$ 57.800</div>
    <div class="c">Fornecimento, produção e instalação por equipe própria — marcenaria,
    serralheria com pintura eletrostática, ferragens Hettich e iluminação dos nichos.</div>
    <div class="pay2">
      <div><b>40%</b><span>na assinatura</span></div>
      <div><b>60%</b><span>na entrega</span></div>
    </div>
  </div>

  <table class="item-tb">
    <thead><tr><th>Frente</th><th class="r">Preço</th></tr></thead>
    <tbody>
      <tr><td class="nm">Parede lado direito — completa<small>Estante com torres e nichos iluminados · 3 gavetas · prateleiras em serralheria e vidro · portas touch</small></td><td class="r">R$ 22.500</td></tr>
      <tr><td class="nm">Mesas centrais<small>Metalon com pé treliçado · 2 gaveteiros volantes · até 20 tomadas 10A</small></td><td class="r">R$ 12.500</td></tr>
      <tr><td class="nm">Sala de reunião — painéis<small>Painel de TV · painel com porta mimetizada · 3 prateleiras com suporte oculto</small></td><td class="r">R$ 9.800</td></tr>
      <tr><td class="nm">Sala de reunião — mesa oval<small>Tampo em MDF melamínico fosco · base cônica laqueada</small></td><td class="r">R$ 8.700</td></tr>
      <tr><td class="nm">Painel frontal do banheiro<small>Parede completa com porta mimetizada</small></td><td class="r">R$ 4.300</td></tr>
      <tr class="tot"><td>Total</td><td class="r">R$ 57.800</td></tr>
    </tbody>
  </table>

  <div class="terms" style="margin-top:2.6mm;">
    <div class="term"><div class="k">Pagamento</div><div class="v">40% + 60%</div></div>
    <div class="term"><div class="k">Prazo</div><div class="v">35 a 45<br>dias úteis</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">10 anos</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">15 dias<br>corridos</div></div>
  </div>

  <div class="note">
    <b>Incluso:</b> fornecimento, produção e instalação das 5 frentes · serralheria com
    pintura eletrostática · vidro incolor temperado das prateleiras · ferragens Hettich ·
    abertura por toque nas portas altas · estrutura de aço anti-empeno nas portas ·
    fecho rolete e sistema pivotante · fita de LED com perfil nos nichos ·
    caixas elétricas embutidas na mesa central.<br>
    <b>Não incluso:</b> <b>esquadria de alumínio e vidros</b> (divisórias e portas de vidro
    com perfil metálico) · pontos elétricos e hidráulicos · gesso, pintura e obra civil ·
    mobiliário solto · televisão e eletrodomésticos.<br>
    <b>Premissas:</b> materiais e cores <b>a definir na aprovação</b>, sem contemplar a
    linha Acetinato · medidas conferidas no local antes da produção.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Porto Verde · Leonardo · 28/07/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-porto-verde-v2.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-porto-verde-v2.html', len(HTML))
