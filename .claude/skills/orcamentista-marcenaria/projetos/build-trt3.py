# -*- coding: utf-8 -*-
"""Proposta PREMIUM — TRT 3ª Região / Espaço de Convivência dos Desembargadores.
Cliente direto: MLQ Engenharia (licitante). 5 páginas, mesmo sistema visual do Apto CJ.
Copy Light Copy adaptada ao contexto B2B/obra pública."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

HERO   = open('/tmp/uri_trt_hero.txt').read()
BUFFET = open('/tmp/uri_trt_buffet.txt').read()
RIPADO = open('/tmp/uri_trt_ripado.txt').read()
DESC   = open('/tmp/uri_trt_desc.txt').read()
COZ    = open('/tmp/uri_trt_coz.txt').read()
CSS    = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  /* override da capa — favorece a faixa de madeira e reforça o véu no topo */
  .cover .hero-img img{{object-position:center 72%;}}
  .cover .veil{{background:linear-gradient(180deg,
      rgba(26,23,20,.92) 0%, rgba(26,23,20,.60) 22%, rgba(26,23,20,.34) 45%,
      rgba(26,23,20,.72) 74%, rgba(26,23,20,.95) 100%);}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover">
  <div class="hero-img"><img src="{HERO}" alt=""></div>
  <div class="veil"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de fornecimento · Movelaria</div>
      <div class="tit">Espaço de Convivência<br>dos Desembargadores.</div>
      <div class="sub">TRT 3ª Região · Edifício Anexo, 10º andar — Belo Horizonte/MG</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Para</div><div class="v">MLQ Engenharia</div></div>
      <div class="c"><div class="k">Escopo</div><div class="v">Grupo 16 — Marcenaria</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. COPY ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Antes do preço, o risco</div>
  <hr class="rule">
  <div class="big-q serif">Numa obra pública, o que estoura o cronograma<br>
  quase nunca é o preço. É o fornecedor que <b>some no meio</b>.</div>

  <p class="body-t" style="margin-top:6mm;">
  Vocês vão apresentar essa proposta ao TRT com o nome da MLQ nela. Se a movelaria atrasar, o problema
  não é do marceneiro — é de quem assinou o contrato.<br><br>
  Por isso esta proposta não começou por um preço por metro. Começou pela leitura do executivo da
  arquiteta <b>prancha a prancha</b>: cada armário, cada painel e cada ripa foi decomposto em
  <b>plano de corte</b> antes de qualquer número ser escrito.<br><br>
  Um exemplo do que isso encontra: o <b>painel do descanso tem 492,5 cm de largura</b> — não cabe em
  chapa nenhuma, em orientação nenhuma. Ele sai em <b>4 peças de 123,1 cm</b>, que é exatamente a
  modulação que a arquiteta desenhou. O projeto já estava pensado para a chapa. Quem orça por m²
  não enxerga isso — e descobre na serra, com a obra parada.</p>

  <div style="margin-top:7mm;" class="split2">
    <div>
      <div class="figure"><img src="{RIPADO}" alt=""></div>
      <div class="cap">Painel ripado · Louro Freijó — salão de mesas</div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:center;">
      <div class="pull">
        <div class="t">O que já conferimos<br>e vocês vão querer saber.</div>
        <div class="d">O executivo prevê <b>reforço em madeira embutido no drywall</b> para fixar os
        painéis e as prateleiras invisíveis. Esse reforço é do gesseiro — e precisa estar pronto antes
        da nossa instalação.<br><br>
        Está dito aqui, na proposta, e não numa conversa depois que a obra travar.</div>
      </div>
    </div>
  </div>

  <p class="body-t" style="margin-top:6mm;">
  <b>A premissa é essa:</b> vocês não precisam de um fornecedor barato. Precisam de um que entregue no
  prazo combinado, com a especificação que o TRT aprovou, e que avise o problema <b>antes</b> dele
  acontecer.</p>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>TRT 3ª Região · MLQ Engenharia</span></div>
</div></div>

<!-- ══════ 3. ESCOPO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Grupo 16 — Marcenaria</div>
  <div class="h-sec serif">Sete itens,<br><em>lidos do executivo.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:6mm;">Escopo conforme a planilha do TRT e o projeto executivo
  de 26/03/2026. Fornecimento e instalação.</p>

  <div class="amb">
    <div class="n">16.1 · Cozinha <span class="badge">maior item</span></div>
    <div class="s">MDF Branco · puxador slim inox 128 mm preto</div>
    <ul>
      <li>Armário inferior sob bancada — <b>2 trechos de 169 cm</b>, 8 portas, prateleira interna.</li>
      <li>Armário aéreo em L — <b>531 cm</b> (274 + 257), 11 módulos, 2 prateleiras internas cada.</li>
      <li>Prateleira suspensa em MDF branco.</li>
      <li><b>Acesso à caixa de gordura</b> executado no sóculo, conforme detalhe da prancha 08.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">16.2 e 16.3 · Buffet</div>
    <div class="s">MDF Duratex Unicolores Moss · prateleira em Louro Freijó com LED</div>
    <ul>
      <li>Armário sob bancada — <b>372 cm</b>, 7 módulos, com <b>vão inferior para ventilação da pista fria</b>.</li>
      <li>Prateleira superior — <b>4 tramos de 93,7 cm</b> em Louro Freijó, com fita <b>LED COB 3000 K contínua</b>
          e testeira que esconde a fonte de luz.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">16.4 · Armário alto — salão de mesas / lavatório</div>
    <div class="s">MDF Arauco Louro Freijó · 87 × 230 × 70 cm</div>
    <ul>
      <li>Porta frontal de <b>girar e correr com sistema de ferragem escamoteável</b> — a folha
          recolhe para dentro do corpo.</li>
      <li><b>Porta traseira de giro</b> (acesso pelos dois lados) e parte inferior cega.</li>
      <li>Prateleiras internas e puxadores slim inox preto.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">16.5, 16.6 e 16.7 · Painéis</div>
    <div class="s">Louro Freijó · MDF padrão fosco no shaft</div>
    <ul>
      <li><b>Painel ripado</b> 173 × 230 cm — ripas verticais de 5,5 cm com travessas de fixação.</li>
      <li><b>Painel do shaft</b> 315 × 230 cm — 4 módulos com <b>abertura fecho-toque</b>, sem puxador.</li>
      <li><b>Painel do descanso</b> em L — <b>492,5 + 266,5 cm</b> × 230 de altura, com friso de 1 × 1 cm
          no encontro de chapas e fechamento lateral recuado.</li>
    </ul>
  </div>

  <div class="split2" style="margin-top:1mm;">
    <div><div class="figure"><img src="{BUFFET}" alt=""></div>
      <div class="cap">Buffet · armário Moss e prateleira Louro Freijó</div></div>
    <div><div class="figure"><img src="{DESC}" alt=""></div>
      <div class="cap">Descanso · painel em L</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>TRT 3ª Região · MLQ Engenharia</span></div>
</div></div>

<!-- ══════ 4. TÉCNICO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:5mm;">Um espaço de convivência de tribunal é usado todos os dias,
  por muita gente. A diferença aparece no terceiro ano.</p>

  <table class="spec-tb">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Painéis e armários nobres</td><td><b>MDF Arauco Madeiras Brasileiras — Louro Freijó</b>,
        conforme especificação da planilha. Veio orientado e casado entre peças adjacentes.</td></tr>
      <tr><td>Buffet</td><td><b>MDF Duratex Unicolores Moss.</b> Shaft em <b>MDF padrão fosco</b>.
        Cozinha em <b>MDF Branco</b>.</td></tr>
      <tr><td>Estrutura</td><td>MDF <b>15 mm</b> em caixaria, portas e painéis · <b>18 mm</b> em
        prateleiras (evita flecha no vão longo) · <b>6 mm</b> em fundos.</td></tr>
      <tr><td>Dobradiças</td><td><b>Hettich Sensys</b>, com amortecimento integrado ao corpo.
        Fecho suave em qualquer velocidade.</td></tr>
      <tr><td>Corrediças</td><td><b>Hettich Quadro V6</b> — abertura total, retorno silencioso, carga plena.</td></tr>
      <tr><td>Porta escamoteável</td><td>Sistema de ferragem para porta de girar e correr que recolhe
        para dentro do corpo do armário — item 16.4.</td></tr>
      <tr><td>Puxadores</td><td>Slim em inox 128 mm, cor preta, conforme especificação.
        Shaft com <b>abertura fecho-toque</b>, sem ferragem aparente.</td></tr>
      <tr><td>Iluminação</td><td>Fita <b>LED COB 15 W/m · 12 V · 3000 K</b> contínua na prateleira do
        buffet, com testeira de ocultação.</td></tr>
      <tr><td>Fixação</td><td>Prateleiras invisíveis em <b>metalon com flange metálica</b>, ancoradas no
        reforço de madeira do drywall, conforme detalhe do executivo.</td></tr>
    </tbody>
  </table>

  <div class="split2" style="margin-top:5mm;">
    <div class="pull" style="background:var(--deep);border-left-color:var(--gold-lt);">
      <div class="t" style="color:#fff;">Ferragem alemã.<br>Hettich desde 1888.</div>
      <div class="d" style="color:#C6BFB2;">Alemã, fundada em 1888 — referência mundial em ferragem
      para móveis. Cada dobradiça é testada para <b style="color:#F0E7D6;">80 mil ciclos</b>: abrir e
      fechar a porta <b style="color:#F0E7D6;">10 vezes por dia durante 20 anos</b>.<br><br>
      Num espaço de uso coletivo, é o que separa a porta que continua macia da que começa a bater.</div>
    </div>
    <div class="pull" style="background:var(--cream);border-left-color:var(--ink);">
      <div class="t">10 anos de garantia</div>
      <div class="d"><b>10 anos</b> na marcenaria — estrutura, montagem e acabamento.<br>
      <b>2 anos</b> na instalação e regulagem.<br><br>
      Garantia formal em contrato.<br><br>
      <b>Equipe própria do corte à instalação</b>, com produção em CNC próprio — cada peça sai do plano
      de corte conferido, não do improviso de obra.</div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>TRT 3ª Região · MLQ Engenharia</span></div>
</div></div>

<!-- ══════ 5. INVESTIMENTO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:21pt;">Preço fechado,<br><em>por item da planilha.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">

  <div class="inv-hero">
    <div class="k">Grupo 16 — Marcenaria · total</div>
    <div class="v serif">R$ 73.900</div>
    <div class="c">Fornecimento e instalação dos 7 itens de marcenaria, com ferragens Hettich,
    iluminação LED e acabamento — por equipe própria Valvic.</div>
    <div class="alt">Valores <b>já fechados</b>, sem BDI. A composição de BDI da licitação fica a
    critério da MLQ Engenharia.</div>
  </div>

  <table class="item-tb">
    <thead><tr><th>Item da planilha</th><th class="r">Preço</th></tr></thead>
    <tbody>
      <tr><td class="nm">16.1 — Armário superior e inferior + prateleira suspensa<small>Cozinha · MDF branco</small></td><td class="r">R$ 13.300</td></tr>
      <tr><td class="nm">16.2 — Armário sob bancada<small>Buffet · MDF Duratex Moss</small></td><td class="r">R$ 8.000</td></tr>
      <tr><td class="nm">16.3 — Prateleira superior com LED<small>Buffet · MDF Louro Freijó</small></td><td class="r">R$ 2.250</td></tr>
      <tr><td class="nm">16.4 — Armário alto com porta escamoteável<small>Salão de mesas / lavatório · MDF Louro Freijó · inclui o sistema de ferragem escamoteável</small></td><td class="r">R$ 29.400</td></tr>
      <tr><td class="nm">16.5 — Painel ripado<small>Salão de mesas / lavatório · MDF Louro Freijó</small></td><td class="r">R$ 6.450</td></tr>
      <tr><td class="nm">16.6 — Painel com portas fecho-toque<small>Shaft · MDF padrão fosco</small></td><td class="r">R$ 3.700</td></tr>
      <tr><td class="nm">16.7 — Painel<small>Descanso · MDF Louro Freijó</small></td><td class="r">R$ 10.800</td></tr>
      <tr class="tot"><td>Total do grupo 16</td><td class="r">R$ 73.900</td></tr>
    </tbody>
  </table>

  <div class="terms">
    <div class="term"><div class="k">Prazo</div><div class="v">60 a 70<br>dias corridos</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">10 anos</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">15 dias<br>corridos</div></div>
  </div>

  <div class="note">
    <b>Incluso:</b> fornecimento, produção e instalação dos 7 itens do grupo 16 · ferragens Hettich ·
    fita LED e perfil · grelha de ventilação em inox · puxadores conforme especificação.<br>
    <b>Não incluso:</b> grupos 10 (portas e janela), 12 (bancadas em granito/quartzito) e 17 (persianas)
    da planilha · espelhos do lavatório · forro (gesso/pintura) · pontos elétricos e hidráulicos ·
    obra civil.<br>
    <b>Premissas:</b> medidas do executivo <b>conferidas no local</b> antes da produção ·
    <b>reforço em madeira no drywall executado pelo gesseiro</b> antes da nossa instalação ·
    acesso ao 10º andar por elevador de serviço em horário de obra · cor definitiva do painel do shaft
    e das linhas de MDF confirmadas em amostra antes do corte.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>TRT 3ª Região · MLQ Engenharia · 26/07/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-trt3.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-trt3.html', len(HTML))
