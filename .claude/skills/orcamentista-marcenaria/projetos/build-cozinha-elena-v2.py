# -*- coding: utf-8 -*-
"""PROPOSTA — Cozinha (projeto Rizzi Interiores) · LAYOUT PREMIUM COM RENDERS.

Substitui a versão tipográfica (`build-cozinha-elena.py`): o Jonathan pediu o
estilo que usa imagens do próprio projeto — o mesmo da Nádia.

Números de `corte-cozinha-elena.py`: custo direto R$ 15.721,49 · MC 30% ·
COM RT · Hardt → bancada R$ 13.300 · demais R$ 24.800 · total R$ 38.100.
Escada só até −3% (28,7%): a −5% e −7% a MC fura o piso de 28% da casa.

⚠️ SLOTS DE IMAGEM. Os renders do projeto ainda NÃO estão em disco — as capturas
   chegaram na conversa, não como arquivo. Cada slot abaixo cai num placeholder
   nomeado enquanto o .jpg não existir em projetos/img/. Basta salvar os
   arquivos com esses nomes e rodar de novo: nada mais muda.
"""
import pathlib, base64
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""', 1)[0]

SLOTS = {
  'elena-capa.jpg':      'vista ampla — cozinha e sala de jantar',
  'elena-bancada.jpg':   'bancada, janela e cooktop',
  'elena-torre.jpg':     'torre quente, forno e geladeira',
  'elena-nicho.jpg':     'nicho em freijó e básculas',
  'elena-ripado.jpg':    'painel ripado e mesa',
  'elena-elevacao.jpg':  'elevação etiquetada do projeto',
}
FALTANDO = []
def img(n):
    f = P/'img'/n
    if f.exists():
        return ('<img src="data:image/jpeg;base64,'
                + base64.b64encode(f.read_bytes()).decode() + '" alt="">')
    FALTANDO.append(n)
    return f'<div class="ph"><span>{n}</span><small>{SLOTS[n]}</small></div>'

AZ, FR, CZ = '#5D7480', '#B08856', '#E4E0D8'

SVG_ESTR = """<svg viewBox="0 0 260 132" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="30" y="14" width="9" height="104" fill="#3A322A"/>
 <rect x="196" y="14" width="9" height="104" fill="#3A322A"/>
 <rect x="39" y="14" width="157" height="9" fill="#3A322A"/>
 <rect x="39" y="109" width="157" height="9" fill="#3A322A"/>
 <rect x="39" y="60" width="157" height="11" fill="#C9A96A"/>
 <rect x="205" y="14" width="4" height="104" fill="#B9AC93"/>
 <rect x="213" y="10" width="11" height="112" fill="#6E6250"/>
 <text x="46" y="36" font-size="9" fill="#241E18" font-family="system-ui" font-weight="700">15 mm</text>
 <text x="46" y="48" font-size="8" fill="#8C7B5E" font-family="system-ui">caixaria interna</text>
 <text x="82" y="69" font-size="8" fill="#241E18" font-family="system-ui" font-weight="700">18 mm · prateleira</text>
 <text x="46" y="103" font-size="8" fill="#8C7B5E" font-family="system-ui">base 15 mm</text>
 <path d="M209 128 H205" stroke="#8C7B5E"/><text x="150" y="130" font-size="7.5" fill="#8C7B5E" font-family="system-ui">fundo 6 mm →</text>
 <text x="228" y="66" font-size="8" fill="#241E18" font-family="system-ui" font-weight="700">18 mm</text>
 <text x="228" y="77" font-size="7.5" fill="#8C7B5E" font-family="system-ui">frente</text>
</svg>"""

SVG_CAVA = """<svg viewBox="0 0 200 104" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="18" y="30" width="150" height="44" fill="#EFE7D8" stroke="#3A322A" stroke-width="1.5"/>
 <path d="M168 30 h14 v13 h-10 v18 h10 v13 h-14 z" fill="#C9A96A" stroke="#3A322A" stroke-width="1.2"/>
 <path d="M174 52 h-8" stroke="#3A322A" stroke-width="1" stroke-dasharray="2 2"/>
 <path d="M182 22 v-8" stroke="#8C7B5E"/>
 <text x="112" y="12" font-size="8" fill="#8C7B5E" font-family="system-ui">cava usinada na CNC</text>
 <text x="20" y="90" font-size="8" fill="#8C7B5E" font-family="system-ui">a mão entra na própria frente — nada aplicado</text>
</svg>"""

MOVEIS = [
 ('Armário de bancada', '77 × 272 × 60 cm', 'Portas de giro e gavetas em cava', 'Azul Ardósia'),
 ('Armário de bancada', '77 × 150 × 60 cm', 'Completa o “L”', 'Azul Ardósia'),
 ('Nicho', '110 × 150 cm', 'Com prateleira', 'Freijó'),
 ('Aéreo de básculas', '40 × 147 × 45 cm', 'Três básculas em cava', 'Freijó'),
 ('Aéreo', '70 × 150 × 60 cm', 'Três portas de giro em cava', 'Azul Ardósia'),
 ('Torre quente', '270 × 70 × 60 cm', 'Básculas, gavetas e tomadas embutidas', 'Cinza Urban'),
 ('Aéreo da geladeira', '70 × 80 × 60 cm', 'Duas portas de giro em cava', 'Cinza Urban'),
 ('Painel ripado', 'integra a cozinha à sala', 'Ripas em freijó', 'Freijó'),
 ('Mesa', 'apoio na lateral esquerda', 'Tampo em freijó', 'Freijó'),
]
tb_moveis = ''.join(
  f'<tr><td class="nm">{n}<small>{d}</small></td><td>{m}</td>'
  f'<td class="r" style="font-weight:600;">{c}</td></tr>' for n, m, d, c in MOVEIS)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  /* slot de imagem ainda não preenchido */
  .ph{{width:100%; height:100%; min-height:34mm; background:repeating-linear-gradient(
       45deg,#EFEAE0 0 8px,#E7E1D4 8px 16px); border:1px dashed #B9AC93; border-radius:4px;
       display:flex; flex-direction:column; align-items:center; justify-content:center;
       text-align:center; padding:3mm; gap:1.5mm;}}
  .ph span{{font-size:7.4pt; font-weight:700; color:#8C7B5E; letter-spacing:.06em;}}
  .ph small{{font-size:6.6pt; color:#A79C88; line-height:1.35; max-width:52mm;}}

  .cover-t{{background:var(--deep); position:relative; overflow:hidden;}}
  .cover-t::before{{content:""; position:absolute; inset:0;
     background:radial-gradient(120% 80% at 16% 10%, rgba(201,169,106,.17) 0%, transparent 58%),
                radial-gradient(90% 70% at 90% 96%, rgba(201,169,106,.11) 0%, transparent 60%);}}
  .cover-t .rules{{position:absolute; inset:0;
     background:repeating-linear-gradient(90deg, rgba(255,255,255,.030) 0 1px, transparent 1px 34mm);}}
  .mos{{position:absolute; inset:0; pointer-events:none; z-index:1;}}
  .mos figure{{position:absolute; margin:0; overflow:hidden; border-radius:3px;
      box-shadow:0 8px 30px rgba(0,0,0,.5);}}
  .mos figure img{{width:100%; height:100%; object-fit:cover; display:block;}}
  .mos .a{{top:2mm; right:-16mm; width:118mm; height:86mm;}}
  .mos .b{{top:66mm; right:56mm; width:68mm; height:78mm;}}
  .mos .c{{top:104mm; right:-10mm; width:88mm; height:62mm;}}
  .mos .ln{{position:absolute; background:var(--gold-lt); opacity:.9;}}
  .mos .l1{{top:74mm; right:130mm; width:38mm; height:1.4px;}}
  .mos .l2{{top:102mm; right:143mm; width:1.4px; height:46mm;}}
  .cover-t .scrim{{position:absolute; left:0; right:0; bottom:0; height:60%;
     background:linear-gradient(to bottom, rgba(26,21,16,0) 0%, rgba(26,21,16,.86) 34%,
                var(--deep) 62%); z-index:2;}}
  .cover-t .inner{{position:relative; z-index:3; justify-content:flex-start;}}
  .cover-t .mid{{max-width:122mm; margin-top:auto; margin-bottom:15mm; flex:none;}}
  .cover-t .strip{{flex:none;}}

  .rend3{{display:flex; gap:5mm; margin-top:7mm;}}
  .rend3 > div{{flex:1;}}
  .rend3 .fr{{height:50mm; border-radius:4px; overflow:hidden;
      box-shadow:0 1px 6px rgba(0,0,0,.12);}}
  .rend3 .fr img{{width:100%; height:100%; object-fit:cover; display:block;}}
  .rend3 .cp{{font-size:6.2pt; letter-spacing:.13em; text-transform:uppercase; color:var(--gold);
      font-weight:700; margin-top:1.8mm;}}

  .cores{{display:flex; gap:6mm; margin-top:5mm;}}
  .cores .c{{flex:1; display:flex; align-items:center; gap:3mm;}}
  .cores .sw{{width:13mm; height:13mm; border-radius:3px; flex:none;
      box-shadow:inset 0 0 0 1px rgba(0,0,0,.14);}}
  .cores .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:12pt; font-weight:700; line-height:1.15;}}
  .cores .u{{font-size:7.2pt; letter-spacing:.12em; text-transform:uppercase; color:var(--mut);
      font-weight:700; margin-top:.6mm;}}

  .fer{{display:flex; gap:8mm; margin-top:4.5mm; border-top:1px solid var(--line); padding-top:4mm;}}
  .fer > div{{flex:1;}}
  .fer svg{{width:100%; height:auto; display:block;}}
  .fer .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:12.5pt; font-weight:700; margin-bottom:1.5mm;}}
  .fer .d{{font-size:8.4pt; color:var(--soft); line-height:1.55; margin-top:2mm;}}
  .fer .d b{{color:var(--ink);}}
  .item-tb td{{padding:1.5mm 0;}}
  .pay-tb td{{padding:1.5mm 0;}}
  .spec-tb td{{padding:1.7mm 0;}}
  .amb ul{{font-size:8.8pt; line-height:1.52;}}
</style></head><body>

<!-- 1 · CAPA -->
<div class="page cover cover-t">
  <div class="rules"></div>
  <div class="mos">
    <figure class="a">{img('elena-capa.jpg')}</figure>
    <figure class="b">{img('elena-bancada.jpg')}</figure>
    <figure class="c">{img('elena-torre.jpg')}</figure>
    <div class="ln l1"></div><div class="ln l2"></div>
  </div>
  <div class="scrim"></div>
  <div class="inner">
    <div>
      <div class="brand serif">VALVIC<span class="d">.</span></div>
      <div class="bsub">MARCENARIA</div>
    </div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria</div>
      <div class="tit">Sua cozinha,<br>executada.</div>
      <div class="sub">Projeto Rizzi Interiores · nove móveis, três cores</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Móveis</div><div class="v serif">9</div></div>
      <div class="c"><div class="k">Cores</div><div class="v serif">3</div></div>
      <div class="c"><div class="k">Prazo</div><div class="v serif">60 dias</div></div>
      <div class="c"><div class="k">Garantia</div><div class="v serif">10 anos</div></div>
      <div class="c"><div class="k">Data</div><div class="v serif">07.08.2026</div></div>
    </div>
  </div>
</div>

<!-- 2 · O PROJETO -->
<div class="page"><div class="pad">
  <div class="eyebrow">O projeto</div><hr class="rule">
  <div class="h-sec">Do desenho da Rizzi<br>para a <em>bancada da fábrica</em>.</div>
  <p class="lead" style="margin-top:5mm;">O projeto já definiu cada móvel, cada cor e cada
  medida. O nosso trabalho é traduzir isso em chapa, ferragem e montagem — sem reinterpretar
  o que já foi decidido.</p>

  <div class="rend3">
    <div><div class="fr">{img('elena-bancada.jpg')}</div><div class="cp">Bancada · janela · cooktop</div></div>
    <div><div class="fr">{img('elena-nicho.jpg')}</div><div class="cp">Nicho em freijó · básculas</div></div>
    <div><div class="fr">{img('elena-torre.jpg')}</div><div class="cp">Torre quente · geladeira</div></div>
  </div>

  <div class="cores">
    <div class="c"><div class="sw" style="background:{AZ};"></div>
      <div><div class="n">Azul Ardósia</div><div class="u">bancadas e aéreo</div></div></div>
    <div class="c"><div class="sw" style="background:{FR};"></div>
      <div><div class="n">Freijó</div><div class="u">nicho · básculas · ripado</div></div></div>
    <div class="c"><div class="sw" style="background:{CZ};"></div>
      <div><div class="n">Cinza Urban</div><div class="u">torre e aéreo da geladeira</div></div></div>
  </div>

  <div class="figure" style="margin-top:6mm; height:52mm;">{img('elena-elevacao.jpg')}</div>
  <div class="cap">Elevação etiquetada do projeto — giro, báscula, gaveta e porta</div>

  <div class="pull" style="margin-top:5mm;">
    <div class="t">Três cores nunca dividem chapa.</div>
    <div class="d">Azul Ardósia, Freijó e Cinza Urban são compradas e cortadas em separado —
    cada cor tem seu próprio plano de corte. É o que garante que o tom de uma porta seja
    exatamente o da porta ao lado, e é por isso que um projeto tricolor não custa o mesmo que
    um monocromático.</div>
  </div>

  <div class="note"><b>A medição no local vem antes do corte.</b> O documento de consultoria
  informa que suas cotas foram tiradas de planta baixa e não servem como referência para
  compra final. Nossa medição confirma cada vão antes de qualquer chapa ser cortada — e está
  inclusa nesta proposta.</div>

  <div class="pfoot"><span class="bl">VALVIC<span class="d">.</span></span>
    <span>Cozinha · projeto Rizzi Interiores</span></div>
</div></div>

<!-- 3 · ESPECIFICAÇÃO -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação</div><hr class="rule">
  <div class="h-sec">Os <em>nove móveis</em>.</div>

  <table class="spec-tb" style="margin-top:5mm;">
    <tr><th>Móvel</th><th>Medidas e configuração</th><th style="text-align:right;">Cor</th></tr>
    {tb_moveis}
  </table>

  <div class="fer">
    <div>
      <div class="t">A estrutura, por espessura</div>
      {SVG_ESTR}
      <div class="d"><b>15 mm</b> na caixaria, <b>18 mm</b> nas prateleiras e nas frentes,
      <b>6 mm</b> nos fundos. Fita de borda em <b>todas</b> as faces aparentes — inclusive as
      que só aparecem com a porta aberta.</div>
    </div>
    <div>
      <div class="t">Cava em todas as frentes</div>
      {SVG_CAVA}
      <div class="d">São <b>16,94 m</b> de cava usinada na CNC. O puxador é a própria frente:
      nada aplicado, nada para desalinhar com o tempo. Nas três cores, com o mesmo perfil.</div>
    </div>
  </div>

  <div class="split2" style="margin-top:4mm;">
    <div>
      <div class="amb"><div class="n">Ferragens</div><div class="s">Linha Hardt</div>
        <ul>
          <li><b>18 dobradiças</b> com amortecimento</li>
          <li><b>14 corrediças ocultas</b> com amortecimento</li>
          <li><b>5 articuladores</b> de báscula</li>
          <li>Suportes metálicos de prateleira</li>
        </ul>
      </div>
    </div>
    <div>
      <div class="amb"><div class="n">Não incluso</div><div class="s">Outras frentes</div>
        <ul>
          <li>Granito, cuba e misturador</li>
          <li>Porcelanato e demais revestimentos</li>
          <li>Eletrodomésticos, coifa e luminária</li>
          <li>Pontos elétricos, hidráulicos e gesso</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">VALVIC<span class="d">.</span></span>
    <span>Cozinha · projeto Rizzi Interiores</span></div>
</div></div>

<!-- 4 · INVESTIMENTO -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div><hr class="rule">
  <div class="h-sec">A cozinha <em>completa</em>.</div>

  <div class="inv-hero" style="margin-top:4mm;">
    <div class="k">Investimento total</div>
    <div class="v">R$ 38.100</div>
    <div class="c">Entrada de 30% + saldo em até 10× no cartão</div>
    <div class="alt">Projeto, medição, produção, entrega e instalação pela
    <b>equipe própria Valvic</b>.</div>
  </div>

  <table class="item-tb">
    <tr><th>Composição</th><th style="text-align:right;">Valor</th></tr>
    <tr><td class="nm">Armários inferiores da bancada<small>272 + 150 cm · 11 gavetas em corrediça oculta</small></td>
        <td class="r">R$ 13.300</td></tr>
    <tr><td class="nm">Demais móveis<small>aéreos, nicho em freijó, torre quente, painel ripado e mesa</small></td>
        <td class="r">R$ 24.800</td></tr>
    <tr class="tot"><td>Total</td><td class="r">R$ 38.100</td></tr>
  </table>

  <table class="pay-tb">
    <tr><th>Forma de pagamento</th><th style="text-align:right;">Investimento</th></tr>
    <tr><td>Entrada de 30% + saldo em até 10× no cartão</td><td class="r">R$ 38.100</td></tr>
    <tr class="best"><td>Entrada de 50% + saldo em até 8× no cartão</td><td class="r">R$ 37.000</td></tr>
  </table>

  <div class="pull" style="margin-top:4mm;">
    <div class="t">Os armários da bancada em linha própria.</div>
    <div class="d">Eles aparecem separados porque são o maior bloco isolado do projeto e o mais
    fácil de faseiar. <b>Se forem executados depois</b>, o restante da cozinha fica em
    <b>R$ 26.600</b> — e não nos R$ 24.800 acima: chapa comprada para o conjunto não encolhe na
    mesma proporção quando o conjunto diminui, e a instalação continua sendo uma cozinha inteira.</div>
  </div>

  <div class="figure" style="margin-top:4mm; height:19mm;">{img('elena-ripado.jpg')}</div>
  <div class="cap">Painel ripado e mesa · integrando a cozinha à sala de jantar</div>

  <div class="terms">
    <div class="term"><div class="k">Prazo</div><div class="v">60 dias<br>corridos</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">10 anos<br>estrutura e ferragens</div></div>
    <div class="term"><div class="k">Corrediças</div><div class="v">2 anos<br>de garantia</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">7 dias<br>desta proposta</div></div>
  </div>

  <div class="note"><b>Medição final antes do corte.</b> As medidas desta proposta vêm do
  documento de consultoria, que declara não servir como referência para compra final. Nossa
  medição no local é feita antes da liberação do corte, e eventuais ajustes de dimensão são
  acertados ali — com a proposta revisada por escrito antes de a produção começar.</div>

  <div class="pfoot"><span class="bl">VALVIC<span class="d">.</span></span>
    <span>Cozinha · projeto Rizzi Interiores · 07/08/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-cozinha-elena-v2.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-cozinha-elena-v2.html', len(HTML))
if FALTANDO:
    print('\n⚠ SLOTS VAZIOS — salvar em projetos/img/ e rodar de novo:')
    for n in dict.fromkeys(FALTANDO):
        print(f'   {n:<22} {SLOTS[n]}')
