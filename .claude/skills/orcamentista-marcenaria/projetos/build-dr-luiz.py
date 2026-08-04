# -*- coding: utf-8 -*-
"""PROPOSTA Dr. Luiz — novo espaço de atendimento (advocacia).
Valores FECHADOS pelo Jonathan (não passaram pelo motor). 4 páginas.
Capa tipográfica — não há render nem executivo, mesma situação do Porto Verde V2."""
import pathlib, base64
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

def uri(nome):
    b = (P/'img'/nome).read_bytes()
    return 'data:image/png;base64,' + base64.b64encode(b).decode()

BORDA = uri('borda-arredondada-45mm.png')   # detalhe da borda arredondada [Jonathan 04/08]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  /* capa tipográfica — sem foto */
  .cover-t{{background:var(--deep); position:relative; overflow:hidden;}}
  .cover-t::before{{content:""; position:absolute; inset:0;
     background:radial-gradient(120% 80% at 18% 12%, rgba(201,169,106,.16) 0%, transparent 58%),
                radial-gradient(90% 70% at 88% 96%, rgba(201,169,106,.10) 0%, transparent 60%);}}
  .cover-t .rules{{position:absolute; inset:0;
     background:repeating-linear-gradient(90deg, rgba(255,255,255,.030) 0 1px, transparent 1px 34mm);}}

  /* ambientes */
  .amb2{{border-top:1px solid var(--hair); padding:3.9mm 0;}}
  .amb2:first-child{{border-top:2px solid var(--ink);}}
  .amb2 .hd{{display:flex; justify-content:space-between; align-items:baseline;}}
  .amb2 .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:15.5pt; font-weight:700;
      line-height:1.15;}}
  .amb2 .q{{font-size:6.8pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700; white-space:nowrap; padding-left:5mm;}}
  .amb2 ul{{margin:2.2mm 0 0; padding-left:4.5mm; font-size:9.4pt; color:var(--soft);
      line-height:1.72;}}
  .amb2 ul b{{color:var(--ink);}}

  /* detalhe construtivo em destaque */
  .det{{display:flex; gap:0; margin-top:5.5mm; border-top:1px solid var(--line);
      border-bottom:1px solid var(--line); padding:4.4mm 0;}}
  .det > div{{flex:1; padding-left:6mm; border-left:1px solid var(--line);}}
  .det > div:first-child{{padding-left:0; border-left:0;}}
  .det .k{{font-size:6.6pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .det .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:14pt; font-weight:700;
      color:var(--ink); line-height:1.15; margin-top:1mm;}}
  .det .d{{font-size:8.6pt; color:var(--soft); line-height:1.6; margin-top:1.2mm;}}
  .det .d b{{color:var(--ink);}}

  /* investimento */
  .inv{{background:var(--deep); border-radius:7px; padding:14mm 9mm; margin-top:5mm;
      position:relative; overflow:hidden; box-shadow:inset 0 0 0 1.5px rgba(201,169,106,.5);}}
  .inv .k{{font-size:6.8pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt);
      font-weight:700;}}
  .inv .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:54pt; font-weight:700;
      color:#fff; line-height:1.02; margin-top:2.6mm;}}
  .inv .sub{{font-size:9.6pt; color:#C6BFB2; margin-top:3.4mm; line-height:1.6;}}
  .inv .sub b{{color:var(--gold-lt);}}
  .pay2{{display:flex; margin-top:6.5mm; padding-top:4.5mm;
      border-top:1px solid rgba(201,169,106,.28);}}
  .pay2 > div{{flex:1; padding-left:6mm; border-left:1px solid rgba(201,169,106,.18);}}
  .pay2 > div:first-child{{padding-left:0; border-left:0;}}
  .pay2 b{{display:block; font-family:'Cormorant Garamond',Georgia,serif; font-size:26pt;
      font-weight:700; color:var(--gold-lt); line-height:1;}}
  .pay2 span{{display:block; font-size:8.8pt; color:#C6BFB2; margin-top:2mm; line-height:1.55;}}

  .cond{{display:grid; grid-template-columns:1fr 1fr; gap:7.5mm 7mm; margin-top:11mm;
      border-top:2px solid var(--ink); padding-top:6mm;}}
  .cond .k{{font-size:6.8pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .cond .d{{font-size:9.4pt; color:var(--soft); line-height:1.6; margin-top:1.2mm;}}
  .cond .d b{{color:var(--ink);}}
  .warr{{background:var(--deep); border-left:3px solid var(--gold-lt);
      border-radius:0 5px 5px 0; padding:5mm 7mm; margin-top:6mm;}}
  .warr .k{{font-size:6.8pt; letter-spacing:.2em; text-transform:uppercase; color:var(--gold-lt);
      font-weight:700;}}
  .warr .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:23pt; font-weight:700;
      color:#fff; line-height:1.1; margin-top:1.6mm;}}
  .warr .d{{font-size:9pt; color:#C6BFB2; line-height:1.6; margin-top:2.2mm;}}
  .warr .d b{{color:#F0E7D6;}}
  .obs{{margin-top:6mm; padding-left:4.5mm; border-left:2px solid var(--gold-lt);
      font-size:8.4pt; color:var(--soft); line-height:1.7;}}
  .obs b{{color:var(--ink);}}

  .spec-tb td:first-child{{width:44mm;}}
  .spec-tb td{{padding:2.9mm 0;}}
  .spec-tb{{font-size:9.2pt;}}

  /* figura de detalhe + texto — a legenda vai na coluna de texto: a coluna da figura fica só com a imagem,
     senão o figcaption desce e bate no rodapé */
  .figrow{{display:flex; gap:0; margin-top:5mm; align-items:center;}}
  .fig{{width:34mm; flex:none; margin:0;}}
  .fig img{{width:34mm; height:34mm; object-fit:cover; display:block;
      border-radius:4px; box-shadow:0 1px 5px rgba(0,0,0,.10);}}
  .ftxt{{flex:1; margin-left:7mm; padding-left:5mm; border-left:2px solid var(--gold-lt);
      font-size:8.6pt; color:var(--soft); line-height:1.7;}}
  .ftxt b{{color:var(--ink);}}
  .ftxt .fk{{font-size:6.4pt; letter-spacing:.16em; text-transform:uppercase;
      color:var(--gold); font-weight:700; margin-bottom:1.8mm;}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover cover-t">
  <div class="rules"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria corporativa</div>
      <div class="tit">Dr. Luiz.</div>
      <div class="sub">Novo espaço de atendimento · Advocacia</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">5 ambientes</div></div>
      <div class="c"><div class="k">Execução</div><div class="v">Marcenaria · serralheria</div></div>
      <div class="c"><div class="k">Entrega</div><div class="v">45 dias corridos</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. ESCOPO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif" style="font-size:26pt;">Cinco ambientes,<br><em>uma linguagem só.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:2mm;">Fornecimento, entrega e instalação. Todo o
  revestimento em <b>MDF melamínico fosco</b>, com o mesmo acabamento de bancada em
  todos os ambientes — de modo que as salas conversem entre si.</p>

  <div style="margin-top:3mm;">
    <div class="amb2">
      <div class="hd"><div class="t">Salas de atendimento compactas</div>
        <div class="q">2 salas</div></div>
      <ul>
        <li><b>Revestimento parcial da bancada de pedra existente</b> — a pedra permanece;
            a marcenaria envolve o que fica aparente e integra a peça ao ambiente.</li>
        <li><b>Bancada acoplada</b> em cada sala, encostada na existente, ampliando a
            superfície de trabalho sem obra.</li>
      </ul>
    </div>

    <div class="amb2">
      <div class="hd"><div class="t">Sala principal</div>
        <div class="q">bancada nova</div></div>
      <ul>
        <li><b>Revestimento da bancada de pedra existente</b>, no mesmo padrão das salas
            compactas.</li>
        <li><b>Bancada nova</b> executada sob medida — a peça de maior presença do
            conjunto.</li>
      </ul>
    </div>

    <div class="amb2">
      <div class="hd"><div class="t">Sala de apoio</div>
        <div class="q">2 bancadas suspensas</div></div>
      <ul>
        <li>Duas <b>bancadas suspensas</b>, fixadas na alvenaria — piso livre por baixo,
            limpeza mais simples e a sala parece maior do que é.</li>
      </ul>
    </div>

    <div class="amb2">
      <div class="hd"><div class="t">Copa</div>
        <div class="q">3 módulos</div></div>
      <ul>
        <li><b>Armário inferior sob a pia</b> e <b>armário superior</b>, fechando a
            parede da bancada.</li>
        <li><b>Torre de apoio</b>, em frente, com vãos dedicados: <b>frigobar</b>,
            <b>nicho da cafeteira</b>, <b>nicho do micro-ondas</b> e módulo de
            <b>armazenagem</b> — cada equipamento com o seu lugar, nada em cima da
            bancada.</li>
      </ul>
    </div>
  </div>

  <div class="det">
    <div><div class="k">Bancadas</div><div class="t">Tampo de 45 mm</div>
      <div class="d">Borda <b>arredondada</b>, sem chanfro — raio usinado na peça.
      <b>Quina que não machuca</b> e não lasca com o uso.</div></div>
    <div><div class="k">Estrutura</div><div class="t">Pé em serralheria</div>
      <div class="d">Metal com <b>pintura eletrostática fosca</b>, no mesmo tom em todas
      as bancadas.</div></div>
    <div><div class="k">Revestimento</div><div class="t">Melamínico fosco</div>
      <div class="d">Linha fosca, <b>sem acetinato e sem a linha Aris</b> — superfície
      uniforme e de manutenção fácil.</div></div>
  </div>

  <div class="pull" style="margin-top:5mm;">
    <div class="t">Onze peças,<br>um só desenho.</div>
    <div class="d">São <b>11 elementos</b> em cinco ambientes — e quem atravessa o espaço
    precisa enxergar <b>um conjunto</b>, não cinco compras separadas. A mesma cor, a mesma
    borda e o mesmo pé repetem em tudo: é a repetição que faz o espaço parecer projetado.</div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Dr. Luiz · novo espaço de atendimento</span></div>
</div></div>

<!-- ══════ 3. TÉCNICO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">

  <table class="spec-tb" style="margin-top:3mm;">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Revestimento</td><td><b>MDF melamínico fosco</b> em todo o conjunto —
        <b>sem a linha acetinato e sem a linha Aris</b>, conforme definido.</td></tr>
      <tr><td>Bancadas</td><td>Tampo com <b>45 mm de espessura</b> e <b>borda
        arredondada</b>, com o raio usinado na própria peça — <b>sem acabamento
        chanfrado</b>. É o detalhe que define o toque do móvel e o que mais aparece
        num espaço de atendimento.</td></tr>
      <tr><td>Estrutura</td><td>Pé em <b>serralheria</b> com <b>pintura eletrostática
        fosca</b> — a pintura é curada em estufa, não é tinta aplicada com pincel:
        não descasca no encosto da cadeira.</td></tr>
      <tr><td>Bancadas suspensas</td><td>Fixação estrutural na alvenaria, dimensionada
        para uso contínuo — <b>sem pé no chão</b>, piso livre.</td></tr>
      <tr><td>Bancadas de pedra</td><td>As pedras existentes são <b>mantidas</b>. A
        marcenaria reveste as faces aparentes e acopla as bancadas novas ao conjunto.</td></tr>
      <tr><td>Copa · torre</td><td>Vãos dimensionados para <b>frigobar</b>, <b>cafeteira</b>
        e <b>micro-ondas</b> — com folga de ventilação e passagem de tomada por trás de
        cada nicho.</td></tr>
      <tr><td>Ferragens</td><td><b>Hettich</b>, com amortecimento nas portas dos armários
        da copa.</td></tr>
      <tr><td>Instalação</td><td>Equipe própria, do corte ao parafuso final. Medição
        conferida no local antes da produção.</td></tr>
    </tbody>
  </table>

  <div class="warr">
    <div class="k">Garantia</div>
    <div class="big">5 anos. Em contrato.</div>
    <div class="d">Marcenaria sob medida costuma sair com <b>1 a 3 anos</b> de garantia —
    quando sai por escrito. A nossa é de <b>5 anos</b> sobre estrutura, montagem,
    acabamento e instalação. Conseguimos assinar isso porque a equipe é <b>própria do
    corte à instalação</b> — inclusive a serralheria dos pés, que sai coordenada com a
    marcenaria e não como um fornecedor à parte.</div>
  </div>

  <div class="figrow">
    <figure class="fig">
      <img src="{BORDA}" alt="Detalhe da borda arredondada do tampo de 45 mm">
    </figure>
    <div class="ftxt">
      <div class="fk">Borda arredondada · tampo de 45 mm</div>
      <b>Um espaço de atendimento tem uma exigência que uma casa não tem:</b> a bancada é a
      primeira coisa que o cliente toca quando senta. É por isso que a borda arredondada e a
      pintura eletrostática não são detalhes de acabamento aqui — são o que mantém o móvel
      com cara de novo depois de centenas de atendimentos.
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Dr. Luiz · novo espaço de atendimento</span></div>
</div></div>

<!-- ══════ 4. INVESTIMENTO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:26pt;">O conjunto<br><em>completo.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:1mm;">Os cinco ambientes, com fornecimento,
  entrega e instalação inclusos.</p>

  <div class="inv">
    <div class="k">Investimento total · 5 ambientes</div>
    <div class="big">R$ 27.000</div>
    <div class="sub">Duas salas compactas · sala principal · sala de apoio · copa
      &nbsp;·&nbsp; <b>50% na assinatura + 50% na entrega</b></div>
    <div class="pay2">
      <div><b>50%</b><span>na assinatura do contrato — libera a compra de material
        e a entrada na fila de produção</span></div>
      <div><b>50%</b><span>na entrega, com o conjunto instalado e conferido no local</span></div>
    </div>
  </div>

  <div class="cond">
    <div><div class="k">Prazo de entrega</div><div class="d"><b>45 dias corridos</b>
      após a assinatura e a medição final no local.</div></div>
    <div><div class="k">Garantia</div><div class="d"><b>5 anos</b> em contrato — estrutura,
      montagem, acabamento e instalação.</div></div>
    <div><div class="k">Execução</div><div class="d">Equipe própria — marcenaria,
      serralheria e instalação sob a mesma responsabilidade.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d"><b>15 dias corridos</b>
      a partir desta data.</div></div>
  </div>

  <div class="det" style="margin-top:12mm; padding:6mm 0;">
    <div><div class="k">Passo 1</div><div class="t">Aceite</div>
      <div class="d">Assinatura do contrato e os primeiros <b>50%</b>. É o que reserva a
      data de produção.</div></div>
    <div><div class="k">Passo 2</div><div class="t">Medição</div>
      <div class="d">Visita ao local para conferir cada vão e as pedras existentes,
      <b>antes de cortar</b>.</div></div>
    <div><div class="k">Passo 3</div><div class="t">Entrega</div>
      <div class="d"><b>45 dias corridos</b> · instalação por equipe própria e conferência
      no local.</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Dr. Luiz · 04/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-dr-luiz.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-dr-luiz.html', len(HTML))
