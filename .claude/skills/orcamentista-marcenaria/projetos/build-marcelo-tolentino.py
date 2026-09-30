# -*- coding: utf-8 -*-
"""PROPOSTA — MARCELO TOLENTINO · BRZ Nova Lima  [30/09/2026]

Dois cenários: linha Standard e linha Gold. Números vêm de
`corte-marcelo-tolentino.py`; nada é digitado à mão aqui.

⛔⛔ NUNCA PÔR METRAGEM NEM QUANTITATIVO NA PROPOSTA
   (referencias/proposta-comercial.md · SKILL.md FASE 3)
   Sem cota, sem m², sem contagem de porta, gaveta, prateleira ou nicho.
   ÚNICA EXCEÇÃO, pedida pelo Jonathan em 30/09: a ESPESSURA DA CHAPA
   (15 mm e 18 mm) aparece, porque é o que separa as duas linhas.
   O auditor no fim deste arquivo roda o regex e permite só essa.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('mt', P/'corte-marcelo-tolentino.py')
mt = importlib.util.module_from_spec(spec); sys.modules['mt'] = mt
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mt)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE   = 'Marcelo Tolentino'
OBRA      = 'BRZ · Nova Lima'
PROJETO   = 'Zilda Santiago e Anamaria Diniz'
DATA      = '30 de setembro de 2026'
PRAZO_ST  = '60 dias corridos'
PRAZO_DEC = '90 dias corridos'
VALIDADE  = '10 dias corridos'
NP        = 10

def img(n): return f'img-marcelo-tolentino/{n}.jpg'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read()
       + open(P/'css-proposta-img.css', encoding='utf-8').read() + """
/* ── proposta Marcelo Tolentino ───────────────────────────────────────── */
.amb{margin-top:6.5mm;}
.amb .num{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;
  color:var(--gold-lt);font-weight:600;line-height:1;}
.amb .t{font-size:11.8pt;font-weight:700;letter-spacing:-.01em;margin-top:.6mm;}
.amb .d{color:var(--soft);font-size:8.8pt;line-height:1.66;margin-top:2mm;}
.amb .d b{color:var(--ink);font-weight:600;}
.par{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:0 -19mm;}
.par .ph{height:75mm;}
.solo{margin:0 -19mm;height:80mm;}
.banda{margin:0 -19mm;height:52mm;}

.lin2{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:6mm;}
.lin2 > div{border:1.5px solid var(--line);border-radius:6px;padding:9mm 8mm;}
.lin2 > div.g{border-color:var(--gold);background:rgba(201,169,106,.07);}
.lin2 .cod{font-family:'Cormorant Garamond',Georgia,serif;font-size:26pt;
  color:var(--gold-lt);font-weight:600;line-height:1;}
.lin2 .nm{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
  font-weight:700;color:var(--ink);line-height:1.05;margin-top:1mm;}
.lin2 ul{margin:5mm 0 0;padding-left:4.2mm;color:var(--soft);font-size:8.6pt;
  line-height:1.72;}
.lin2 li{margin-bottom:1.6mm;}
.lin2 b{color:var(--ink);}
.lin2 .gar{margin-top:5mm;padding:3.4mm 4mm;background:var(--cream);
  border-radius:4px;font-size:8.4pt;color:var(--soft);}
.lin2 .gar b{font-size:12.5pt;color:var(--ink);}

.mesmo{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6mm;margin-top:7mm;
  padding-top:5mm;border-top:1px solid var(--hair);}
.mesmo .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.mesmo .d{color:var(--soft);font-size:8.3pt;line-height:1.5;margin-top:1.4mm;}
.mesmo .d b{color:var(--ink);}

table.invA{width:100%;border-collapse:collapse;margin-top:5mm;font-size:8.8pt;}
table.invA th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.4mm;text-align:left;}
table.invA th.r,table.invA td.r{text-align:right;}
table.invA th.alt{color:var(--gold);}
table.invA td{padding:3.1mm 0;border-top:1px solid var(--hair);vertical-align:top;}
table.invA td.a{font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;padding-right:4mm;width:26mm;}
table.invA td.i{font-weight:600;}
table.invA td.alt{background:rgba(201,169,106,.07);padding-right:2.5mm;}
table.invA th.alt{padding-right:2.5mm;}
table.invA tr.tot td{border-top:1.6px solid var(--ink);padding-top:3.4mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;font-weight:700;}
table.invA tr.tot td.a,table.invA tr.tot td.i{font-family:inherit;font-size:9.4pt;}

.cndP{display:grid;grid-template-columns:1fr 1fr;gap:5mm 7mm;margin-top:6mm;}
.cndP .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndP .d{color:var(--soft);font-size:8.6pt;margin-top:1.2mm;line-height:1.5;}
.cndP .d b{color:var(--ink);}
.escP{margin-top:5mm;border:1px solid var(--line);border-radius:5px;overflow:hidden;}
.escP .l{display:flex;justify-content:space-between;align-items:baseline;
  padding:3mm 5mm;border-bottom:1px solid var(--hair);font-size:8.8pt;}
.escP .l:last-child{border-bottom:none;}
.escP .l .p{font-weight:700;font-size:10.5pt;color:var(--gold);min-width:14mm;}
.escP .l .q{color:var(--soft);flex:1;padding-left:4mm;}
.nota{margin-top:5mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:8.2pt;color:var(--soft);line-height:1.5;}
.nota b{color:var(--ink);}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · {OBRA}</span><span>{n} / {NP}</span></div>')

def amb(num, titulo, desc):
    return (f'<div class="amb"><div class="num serif">{num}</div>'
            f'<div class="t">{titulo}</div><div class="d">{desc}</div></div>')

# ── 1 · capa ──────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="pad">
  <div class="eyebrow">Proposta comercial</div>
  <div class="cv-t serif">Um estande que vende<br>e um decorado que convence.</div>
  <div class="cv-nome serif">{CLIENTE}</div>
  <div class="cv-s">Marcenaria sob medida do estande de vendas e do
  apartamento decorado — projeto {PROJETO}.</div>
  <div class="cv-meta">
    <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
    <div><div class="k">Obra</div><div class="v">{OBRA}</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
  </div>
  <div class="ph banda" style="margin:auto -19mm -16mm;height:86mm;">
    <img src="{img('capa-sala')}" alt=""></div>
</div></div>"""

# ── 2 · o contrato ────────────────────────────────────────────────────────
p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O contrato</div>
  <div class="h-sec serif">Duas frentes,<br><em>uma marcenaria só.</em></div>
  <div class="rule"></div>
  <p class="lead">O estande recebe quem chega e o decorado é o que fecha a
  venda. São dois canteiros, dois prazos e um único responsável: a Valvic
  desenha o executivo de marcenaria, corta, monta e coordena os terceiros
  de pedra, vidro, laca e estofado.</p>

  <div class="ph solo" style="margin-top:6mm;"><img src="{img('capa-sala')}" alt="">
    <div class="cap">Sala do apartamento decorado.</div>
  </div>

  <div class="mesmo" style="margin-top:7mm;border-top:none;padding-top:0;">
    <div><div class="k">No estande</div><div class="d">Copa, sala de reunião,
      sala de ativos, lounge e a bancada gourmet. <b>Painelaria de parede,
      bancadas de trabalho e armazenamento</b> — o que o visitante vê
      primeiro.</div></div>
    <div><div class="k">No decorado</div><div class="d">Cozinha com área de
      serviço, sala e varanda, os dois quartos e os dois banheiros.
      <b>É o apartamento que o cliente compra</b>, então nada pode parecer
      provisório.</div></div>
    <div><div class="k">Quem faz</div><div class="d"><b>Equipe própria</b>, do
      corte à instalação, com a medida conferida no local antes de qualquer
      peça ir para a serra.</div></div>
  </div>

  <div class="nota" style="margin-top:auto;"><b>O que não é marcenaria e não
  está neste valor:</b> as pedras (mármore verde Alpi, granito cinza
  andorinha, granito branco Siena e o granito marrom tabaco do lounge), a
  alvenaria da bancada gourmet, a bancada e o sóculo existentes da copa,
  louças, metais, eletrodomésticos, esquadrias, forro de gesso, pintura,
  papel de parede, persianas, elétrica, hidráulica e o mobiliário solto.</div>
  {foot(2)}
</div></div>"""

# ── 3 · estande, parte 1 ──────────────────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Estande de vendas</div>
  <div class="h-sec serif">O que recebe<br>quem chega.</div>
  <div class="rule"></div>
  <p class="lead">Leitura fiel do caderno das arquitetas — planta, elevações e
  detalhes. Cada peça saiu da prancha, não de estimativa por área.</p>

  <div class="par" style="margin-top:6mm;">
    <div class="ph"><img src="{img('lounge')}" alt=""></div>
    <div class="ph"><img src="{img('ativos')}" alt=""></div>
  </div>

  {amb('01', 'Lounge',
       'Painel liso do piso ao teto em <b>MDF Carvalho Munique Duratex</b> '
       'vestindo as paredes, e um segundo painel em <b>MDF Tauari Guararapes</b> '
       'com a <b>porta de passagem embutida e puxador cava</b> — fechada, a porta '
       'desaparece no painel. Onde o granito sobe, a marcenaria morre nele com '
       'junta seca.')}
  {amb('02', 'Sala de ativos',
       'Bancadas de trabalho em <b>MDF Carvalho Munique Guararapes</b> correndo '
       'nas três paredes, com <b>canaleta de fiação usinada sob o tampo</b> para '
       'a rede e a tomada de cada estação sumirem. Entre as estações, divisórias '
       'em <b>MDF Cinza Pixel Guararapes</b>. Completa o ambiente um aparador de '
       'apoio, no mesmo carvalho das bancadas.')}
  {amb('03', 'Sala de reunião',
       'Aparador para cafeteira em <b>MDF Cerrado Bold Arauco</b>, com nicho '
       'preparado para receber o porcelanato do piso e frentes em <b>fecho toque'
       '</b> — sem puxador, o conjunto lê como um volume só.')}
  {foot(3)}
</div></div>"""

# ── 4 · estande, parte 2 ──────────────────────────────────────────────────
p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Estande de vendas</div>
  <div class="h-sec serif">A copa e<br>o gourmet.</div>
  <div class="rule"></div>

  <div class="ph solo" style="margin-top:6mm;"><img src="{img('lounge-tv')}" alt="">
    <div class="cap">Lounge · painel do piso ao teto.</div>
  </div>

  {amb('04', 'Bancada gourmet',
       'Painéis lisos em <b>MDF Tauari Guararapes</b> do piso ao teto, e o '
       '<b>forro do ambiente também em Tauari</b> — teto e parede no mesmo '
       'desenho, com o encontro alinhado. Sob a bancada de granito, armários '
       'em Tauari com nicho para os frigobares e portas de abrir. A bancada é '
       'de alvenaria pré-executada: a marcenaria se ajusta a ela no local.')}
  {amb('05', 'Copa',
       'Painel de parede do piso ao teto em <b>MDF Tauari Guararapes</b>, com '
       '<b>porta de abrir embutida e puxador cava</b>. Sob a bancada existente, '
       'armário madeirado em <b>fórmica branca</b> com gaveteiro; e a ilha '
       'central, que recebe o tampo de pedra e guarda o micro-ondas embutido. '
       'A bancada, a rodobanca e o sóculo existentes são aproveitados.')}

  <div class="nota" style="margin-top:auto;"><b>A bancada do gourmet é
  alvenaria pré-executada</b> e a prancha manda ajustar a marcenaria a ela.
  Conferimos a medida no local antes de cortar; se a alvenaria sair fora do
  previsto, avisamos antes de produzir.</div>
  {foot(4)}
</div></div>"""

# ── 5 · decorado · cozinha ────────────────────────────────────────────────
p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Apartamento decorado</div>
  <div class="h-sec serif">A cozinha é<br><em>o argumento de venda.</em></div>
  <div class="rule"></div>
  <p class="lead">É o ambiente que o comprador olha primeiro e o que mais
  recebe crítica. Aqui a marcenaria não pode parecer cenário.</p>

  <div class="par" style="margin-top:6mm;">
    <div class="ph"><img src="{img('cozinha')}" alt=""></div>
    <div class="ph"><img src="{img('cozinha-torre')}" alt=""></div>
  </div>

  {amb('06', 'Cozinha e área de serviço',
       'Base em <b>MDF Tauari Guararapes</b>. Os armários superiores abrem por '
       '<b>fecho toque</b>, com <b>LED embutido sob eles</b> iluminando a '
       'bancada. A torre de eletros recebe forno e micro-ondas embutidos e '
       '<b>porta escamoteável</b>, que some dentro do próprio móvel quando '
       'aberta. Os armários inferiores da bancada principal saem em <b>laca '
       'fosca verde com puxador cava</b>; os demais, em Tauari com a mesma '
       'cava usinada. Fecham o ambiente a <b>cristaleira com porta em perfil '
       'de alumínio preto fosco e vidro canelado</b> e a <b>divisória de '
       'correr</b>, no mesmo vidro e no mesmo perfil, separando a área de '
       'serviço sem fechar a luz. Onde o sóculo da construtora não alcança, '
       'completamos em marcenaria.')}

  <div class="nota" style="margin-top:auto;"><b>A bancada slim, a rodobanca e
  o rebaixo italiano são de mármore verde Alpi escovado</b> e não estão neste
  valor — a marcenaria entrega o corpo, o recorte da cuba e o encosto na
  pedra. Eletrodomésticos, cuba, tanque e metais são de fornecimento do
  cliente.</div>
  {foot(5)}
</div></div>"""

# ── 6 · decorado · sala ───────────────────────────────────────────────────
p6 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Apartamento decorado</div>
  <div class="h-sec serif">A sala, a varanda<br>e a mesa.</div>
  <div class="rule"></div>

  <div class="par" style="margin-top:6mm;">
    <div class="ph"><img src="{img('sala-estante')}" alt=""></div>
    <div class="ph"><img src="{img('sala-jantar')}" alt=""></div>
  </div>

  {amb('07', 'Sala e varanda',
       'A <b>estante do piso ao teto</b> é a peça que dá caráter ao '
       'apartamento: malha de montantes e prateleiras em <b>MDF Tauari '
       'Guararapes</b> dobrando na parede lateral, com <b>nichos em MDF '
       'Carvalho Munique Duratex avançando do plano</b> e <b>LED sob eles</b> '
       '— a luz nasce do próprio nicho, sem perfil à vista. Na parede oposta, '
       'painel liso do piso ao teto em Tauari, com as folhas separadas por '
       '<b>bite usinado</b> no lugar da junta aparente. E a <b>mesa de jantar '
       'em Tauari maciço aparente, com chanfro usinado no tampo</b> — não é '
       'mesa comprada, é marcenaria.')}

  <div class="nota" style="margin-top:auto;">A varanda não recebe marcenaria
  neste escopo. A TV, os quadros, o tapete e o mobiliário solto são de
  fornecimento do cliente.</div>
  {foot(6)}
</div></div>"""

# ── 7 · decorado · quartos e banheiros ────────────────────────────────────
p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Apartamento decorado</div>
  <div class="h-sec serif">Os quartos<br>e os banheiros.</div>
  <div class="rule"></div>

  <div class="par" style="margin-top:6mm;">
    <div class="ph"><img src="{img('quarto-casal')}" alt=""></div>
    <div class="ph"><img src="{img('quarto-solteiro')}" alt=""></div>
  </div>

  {amb('08', 'Quarto casal',
       'Guarda-roupa em <b>MDF Tauari Guararapes com portas de correr em vidro '
       'e perfil de alumínio bronze</b>, interno completo com maleiro, '
       'cabideiro, gavetas e sapateira. Acompanham a <b>cabeceira estofada em '
       'linho</b>, a <b>peseira baú</b> no mesmo linho sobre estrutura de '
       'marcenaria, e as <b>prateleiras suspensas em tubo de alumínio preto</b> '
       'com a mesa de cabeceira flutuando na parede.')}
  {amb('09', 'Quarto solteiro',
       'Guarda-roupa em Tauari com <b>portas de correr em vidro bronze e perfil '
       'bronze</b>, interno com maleiro, cabideiro, gavetas e sapateiras. '
       'Escrivaninha em Tauari, nicho na altura da cabeceira, cabeceira '
       'estofada e <b>prateleiras suspensas com nichos em MDF Cinza Essencial '
       'Duratex</b>.')}
  {amb('10', 'Banheiros',
       'No <b>banheiro casal</b>, gabinete em Tauari com puxador cava, '
       '<b>espelho com moldura em Tauari</b> e uma torre de prateleiras com '
       '<b>fundo em muxarabi</b> — ripado fino usinado peça a peça, que filtra '
       'a luz e é o detalhe mais trabalhoso do apartamento. No <b>banheiro '
       'social</b>, gabinete em Tauari, <b>espelho prata colado sobre chapa</b> '
       'e torre de prateleiras com <b>LED embutido na lateral</b>.')}
  {foot(7)}
</div></div>"""

# ── 8 · as duas linhas ────────────────────────────────────────────────────
def card(cen, g=False):
    esp = '15 mm' if cen == 'standard' else '18 mm'
    itens = {
      'standard': [
        'Dobradiça <b>Hettich Novisys</b> em todas as portas',
        'Corrediça <b>telescópica</b> em todas as gavetas',
        'Roupeiro em <b>sistema de correr RO65 Prime, da Rometal</b>',
        'Estrutura, portas e prateleiras em <b>MDF de&nbsp;15&nbsp;mm</b>'],
      'gold': [
        'Dobradiça <b>Hettich Sensys</b> — a linha premiada da marca, com '
        'pistão em gel e regulagem nos três eixos',
        'Corrediça <b>oculta Quadro, da Hettich</b>, com Silent System: a '
        'gaveta some sob a frente e fecha sozinha',
        'Roupeiro em <b>sistema de correr Dominus, da Rometal</b>',
        'Portas e prateleiras em <b>MDF de&nbsp;18&nbsp;mm</b> — mais rígidas, '
        'assentam melhor e não barrigam com o tempo'],
    }[cen]
    li = ''.join(f'<li>{x}</li>' for x in itens)
    return f"""<div class="{'g' if g else ''}">
      <div class="cod serif">{'02' if g else '01'}</div>
      <div class="nm serif">Linha<br>{'Gold' if g else 'Standard'}</div>
      <ul>{li}</ul>
      <div class="gar">Garantia Valvic de <b>{mt.GARANTIA[cen]}</b> sobre
        estrutura e ferragens</div>
    </div>"""

p8 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">As duas linhas</div>
  <div class="h-sec serif">A mesma marcenaria.<br><em>A ferragem e a chapa decidem.</em></div>
  <div class="rule"></div>
  <p class="lead">O desenho, os ambientes, as chapas de acabamento, os
  espelhos, os vidros, a laca, o estofado e o LED são <b>idênticos</b> nas
  duas linhas. O que muda é a ferragem que você abre todos os dias, a
  espessura da porta e da prateleira — e, com elas, o tempo de garantia.</p>

  <div class="lin2">{card('standard')}{card('gold', g=True)}</div>

  <div class="mesmo">
    <div><div class="k">O que não muda</div><div class="d"><b>O desenho.</b>
      Mesmos ambientes, mesma modulação, mesma distribuição interna nos dois
      casos.</div></div>
    <div><div class="k">Também não muda</div><div class="d"><b>Acabamento.</b>
      Tauari, Carvalho Munique, Cinza Pixel, Cerrado Bold e Cinza Essencial,
      a laca verde, os vidros, os espelhos e o mesmo LED instalado.</div></div>
    <div><div class="k">Nem muda</div><div class="d"><b>Quem faz.</b> Equipe
      própria do corte à instalação, com a medida conferida no local antes do
      corte.</div></div>
  </div>

  <div class="nota" style="margin-top:auto;">A garantia é <b>termo da Valvic
  sobre o conjunto que fornecemos e instalamos</b> — não é repasse de garantia
  de fabricante. A diferença entre as linhas está nos <b>ciclos testados de
  abertura, no amortecimento e na regulagem</b>, e é isso que sustenta os
  {mt.GARANTIA['gold']} da linha Gold.</div>
  {foot(8)}
</div></div>"""

# ── 9 · investimento e condições ──────────────────────────────────────────
NOME_AMB = {'Copa':'Copa','Sala de reunião':'Sala de reunião',
            'Sala de ativos':'Sala de ativos','Lounge':'Lounge',
            'Gourmet':'Bancada gourmet','Cozinha':'Cozinha e área de serviço',
            'Sala':'Sala e varanda','Quarto casal':'Quarto casal',
            'Quarto solteiro':'Quarto solteiro','Banheiro social':'Banheiro social',
            'Banheiro casal':'Banheiro casal'}

# espelho sai do ambiente e vira linha própria, como pedido
ESP_PV = {c: {am: round(mt.ESP_AMB[am]/(mt.BASE - mt.MC_ALVO[c][am])/10)*10
              for am in mt.AMBS} for c in mt.CEN}
AMB_PV = {c: {am: mt.PV[c][am] - ESP_PV[c][am] for am in mt.AMBS} for c in mt.CEN}
ESP_TOT_PV = {c: sum(ESP_PV[c].values()) for c in mt.CEN}

linhas, _fr = '', None
for am in mt.AMBS:
    fr = mt.FR_DE[am]
    if fr != _fr:
        linhas += (f'<tr><td class="a">{"Estande" if fr=="Stand" else "Decorado"}</td>'
                   f'<td class="i">{NOME_AMB[am]}</td>'
                   f'<td class="r">R$ {br(AMB_PV["standard"][am])}</td>'
                   f'<td class="r alt">R$ {br(AMB_PV["gold"][am])}</td></tr>')
        _fr = fr
    else:
        linhas += (f'<tr><td class="a"></td><td class="i">{NOME_AMB[am]}</td>'
                   f'<td class="r">R$ {br(AMB_PV["standard"][am])}</td>'
                   f'<td class="r alt">R$ {br(AMB_PV["gold"][am])}</td></tr>')
linhas += (f'<tr><td class="a">Terceiros</td>'
           f'<td class="i">Espelhos <small>· fornecimento e instalação</small></td>'
           f'<td class="r">R$ {br(ESP_TOT_PV["standard"])}</td>'
           f'<td class="r alt">R$ {br(ESP_TOT_PV["gold"])}</td></tr>')

TOT_ST, TOT_GO = mt.TOT['standard'], mt.TOT['gold']

p9 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Ambiente a ambiente,<br>duas linhas.</div>
  <div class="rule"></div>

  <table class="invA">
    <thead><tr><th></th><th></th>
      <th class="r">Standard<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">{mt.GARANTIA['standard']} de garantia</span></th>
      <th class="r alt">Gold<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">{mt.GARANTIA['gold']} de garantia</span></th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="a"></td><td class="i">Investimento total</td>
        <td class="r">R$ {br(TOT_ST)}</td>
        <td class="r alt">R$ {br(TOT_GO)}</td></tr>
    </tbody>
  </table>

  <div class="nota" style="margin-top:auto;">Os valores acima são por
  ambiente e incluem projeto executivo de marcenaria, material, ferragens,
  transporte e <b>montagem por equipe própria</b>. Os espelhos aparecem em
  linha separada por serem fornecimento de terceiro coordenado pela Valvic.</div>
  {foot(9)}
</div></div>"""

# ── 10 · condições ────────────────────────────────────────────────────────
p10 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="h-sec serif">Pagamento, prazo<br>e fronteiras.</div>
  <div class="rule"></div>
  <p class="lead">A entrada libera a compra do material e a entrada do projeto
  na fila de produção. O restante acompanha o andamento da obra.</p>

  <div class="escP">
    <div class="l"><span class="p">40%</span><span class="q">na assinatura —
      libera a compra do material e a entrada na fila de produção</span></div>
    <div class="l"><span class="p">20%</span><span class="q">no início das
      montagens</span></div>
    <div class="l"><span class="p">20%</span><span class="q">na entrega
      final</span></div>
    <div class="l"><span class="p">20%</span><span class="q">em boleto, 30 dias
      após a entrega</span></div>
  </div>

  <div class="cndP">
    <div><div class="k">Prazo de entrega</div><div class="d">
      <b>Estande: {PRAZO_ST}</b><br><b>Decorado: {PRAZO_DEC}</b><br>
      contados da assinatura, do pagamento da entrada e da medição final no
      local.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>Linha Standard: {mt.GARANTIA['standard']}</b><br>
      <b>Linha Gold: {mt.GARANTIA['gold']}</b><br>
      sobre estrutura e ferragens, termo da Valvic.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d">
      <b>{VALIDADE}</b> a partir desta data.</div></div>
    <div><div class="k">Escopo Valvic</div><div class="d">
      Do corte à instalação com <b>equipe própria</b>, e os terceiros de pedra,
      vidro, laca, espelho e estofado <b>coordenados e entregues
      instalados</b>.</div></div>
  </div>

  <div class="nota"><b>Não inclusos:</b> pedras e bancadas, alvenaria da
  bancada gourmet, bancada e sóculo existentes da copa, louças, metais,
  eletrodomésticos, esquadrias de alumínio de fachada, box, porta de vidro do
  estande, forro de gesso, pintura, papel de parede, persianas, cortinas,
  tapetes, quadros, pontos elétricos e hidráulicos e o mobiliário solto.</div>

  <div class="ph banda" style="margin-top:auto;height:56mm;">
    <img src="{img('fecho')}" alt="">
    <div class="cap">Estande de vendas · lounge.</div>
  </div>
  <div class="eyebrow" style="margin-top:5mm;">{PROJETO}</div>
  {foot(10)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + '</body></html>')

(P/'proposta-marcelo-tolentino.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-marcelo-tolentino/', f'src="file://{P}/img-marcelo-tolentino/')
assert '{' not in tmp[tmp.index('<body>'):].split('src="')[1][:200]
open('/tmp/in.html', 'w', encoding='utf-8').write(tmp)
import os
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-marcelo-tolentino.pdf')],
               check=True, env=env)

print(f'proposta-marcelo-tolentino.pdf · {NP} páginas')
print(f'  Standard  R$ {br(TOT_ST):>9}   MC {(mt.BASE-mt.CD["standard"]/TOT_ST)*100:.1f}%')
print(f'  Gold      R$ {br(TOT_GO):>9}   MC {(mt.BASE-mt.CD["gold"]/TOT_GO)*100:.1f}%')
print(f'  espelhos em linha própria: R$ {br(ESP_TOT_PV["standard"])} / '
      f'R$ {br(ESP_TOT_PV["gold"])}')
for c in mt.CEN:
    assert abs(sum(AMB_PV[c].values()) + ESP_TOT_PV[c] - mt.TOT[c]) < 1, c
print('  soma da tabela confere com o total')
