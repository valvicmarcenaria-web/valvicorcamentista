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
PRAZO     = '15 de novembro de 2026'   # ★ ver FLAG DATA no fim do arquivo
VALIDADE  = '2 de outubro de 2026'
NP        = 5

def img(n): return f'img-marcelo-tolentino/{n}.jpg'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read()
       + open(P/'css-proposta-img.css', encoding='utf-8').read() + """
/* ── proposta Marcelo Tolentino ───────────────────────────────────────── */
.amb{margin-top:4.5mm;}
.amb .num{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;
  color:var(--gold-lt);font-weight:600;line-height:1;}
.amb .t{font-size:11.8pt;font-weight:700;letter-spacing:-.01em;margin-top:.6mm;}
.amb .d{color:var(--soft);font-size:8.8pt;line-height:1.66;margin-top:2mm;}
.amb .d b{color:var(--ink);font-weight:600;}
.par{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin:0 -19mm;}
.par .ph{height:42mm;}
.solo{margin:0 -19mm;height:80mm;}
.banda{margin:0 -19mm;height:52mm;}

.lin2{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:6mm;}
.lin2.um{grid-template-columns:1fr;}
.lin2.um > div{display:grid;grid-template-columns:auto 1fr;gap:0 9mm;
  align-items:start;}
.lin2.um .cod{grid-row:1;}
.lin2.um .nm{grid-row:2;grid-column:1;}
.lin2.um ul{grid-row:1/4;grid-column:2;margin-top:1mm;columns:2;
  column-gap:8mm;}
.lin2.um li{break-inside:avoid;}
.lin2.um .gar{grid-row:3;grid-column:1;align-self:end;}
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

table.invA{width:100%;border-collapse:collapse;margin-top:4mm;font-size:8.6pt;}
table.invA th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.4mm;text-align:left;}
table.invA th.r,table.invA td.r{text-align:right;}
table.invA th.alt{color:var(--gold);}
table.invA td{padding:1.65mm 0;border-top:1px solid var(--hair);vertical-align:top;}
table.invA td.a{font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;padding-right:4mm;width:26mm;}
table.invA td.i{font-weight:600;}
table.invA td.alt{background:rgba(201,169,106,.07);padding-right:2.5mm;}
table.invA th.alt{padding-right:2.5mm;}
table.invA tr.tot td{border-top:1.6px solid var(--ink);padding-top:2.4mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;font-weight:700;}
table.invA tr.tot td.a,table.invA tr.tot td.i{font-family:inherit;font-size:9.4pt;}

.cndP{display:grid;grid-template-columns:1fr 1fr;gap:3.6mm 7mm;margin-top:4.5mm;}
.cndP .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndP .d{color:var(--soft);font-size:8.3pt;margin-top:1mm;line-height:1.46;}
.cndP .d b{color:var(--ink);}
.escP{margin-top:4mm;border:1px solid var(--line);border-radius:5px;
  overflow:hidden;flex:none;}  /* flex:none — sem isto o flex encolhe a
     caixa e o overflow:hidden come a última parcela em silêncio */
.escP .l{display:flex;justify-content:space-between;align-items:baseline;
  padding:2.1mm 5mm;border-bottom:1px solid var(--hair);font-size:8.8pt;}
.escP .l:last-child{border-bottom:none;}
.escP .l .p{font-weight:700;font-size:10.5pt;color:var(--gold);min-width:14mm;}
.escP .l .q{color:var(--soft);flex:1;padding-left:4mm;}
.nota{margin-top:4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:8pt;color:var(--soft);line-height:1.48;}
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
  <div class="cv-t serif">Marcenaria sob medida.</div>
  <div class="cv-nome serif">{CLIENTE}</div>
  <div class="cv-s">Estande de vendas e apartamento decorado —
  projeto {PROJETO}.</div>
  <div class="cv-meta">
    <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
    <div><div class="k">Obra</div><div class="v">{OBRA}</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
  </div>
  <div class="ph banda" style="margin:auto -19mm -16mm;height:86mm;">
    <img src="{img('capa-sala')}" alt=""></div>
</div></div>"""

# ── 2 · estande ───────────────────────────────────────────────────────────
p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Estande de vendas</div>
  <div class="h-sec serif">A marcenaria<br>do estande.</div>
  <div class="rule"></div>

  <div class="par" style="margin-top:6mm;">
    <div class="ph"><img src="{img('lounge')}" alt=""></div>
    <div class="ph"><img src="{img('ativos')}" alt=""></div>
  </div>

  {amb('01', 'Salão principal',
       'A parede do salão inteira em <b>armário ripado de MDF Tauari '
       'Guararapes</b>, do piso ao teto e <b>sem puxador</b>: as portas abrem '
       'ao toque, com <b>fecho toque da Blum</b>. Na entrada, armário liso com '
       'a porta rente à parede e painel do piso ao teto no mesmo Tauari. O '
       'pilar do hidrante desaparece dentro de um revestimento em <b>MDF Preto '
       'Absoluto Duratex</b> com <b>bite usinado entre as folhas</b>, e a '
       'recepção recebe <b>bancada em Tauari com frente inclinada</b>.')}
  {amb('02', 'Lounge',
       'Painel liso do piso ao teto em <b>MDF Carvalho Munique Duratex</b>, e '
       'painel em <b>MDF Tauari Guararapes</b> com <b>porta de passagem '
       'embutida e puxador cava</b> — fechada, a porta desaparece no painel.')}
  {amb('03', 'Sala de ativos',
       'Bancadas de trabalho em <b>MDF Carvalho Munique Guararapes</b> com '
       '<b>canaleta de fiação usinada sob o tampo</b>. Divisórias entre '
       'estações em <b>MDF Cinza Pixel Guararapes</b> e aparador no mesmo '
       'carvalho.')}
  {amb('04', 'Sala de reunião',
       'Aparador para cafeteira em <b>MDF Cerrado Bold Arauco</b>, com frentes '
       'em <b>fecho toque</b> e nicho preparado para o porcelanato.')}
  {amb('05', 'Bancada gourmet',
       'Painéis lisos e <b>forro</b> em <b>MDF Tauari Guararapes</b> — teto e '
       'parede no mesmo desenho. Sob a bancada de granito, armários em Tauari '
       'com nicho para os frigobares.')}
  {amb('06', 'Copa',
       'Painel do piso ao teto em <b>Tauari</b> com porta embutida e puxador '
       'cava, armário inferior em <b>fórmica branca</b> e ilha central.')}
  {foot(2)}
</div></div>"""

# ── 3 · decorado ──────────────────────────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Apartamento decorado</div>
  <div class="h-sec serif">A marcenaria<br>do decorado.</div>
  <div class="rule"></div>

  <div class="par" style="margin-top:6mm;">
    <div class="ph"><img src="{img('cozinha')}" alt=""></div>
    <div class="ph"><img src="{img('quarto-casal')}" alt=""></div>
  </div>

  {amb('07', 'Cozinha e área de serviço',
       'Base em <b>MDF Tauari Guararapes</b>. Superiores em <b>fecho toque</b> '
       'com <b>LED embutido</b>; torre de eletros com <b>porta escamoteável</b>; '
       'inferiores da bancada principal em <b>laca fosca verde com puxador '
       'cava</b>, com a <b>caixa interna em melamínico de cor próxima à da '
       'laca</b>. Cristaleira e divisória de correr em <b>perfil de alumínio '
       'preto fosco com vidro canelado</b>.')}
  {amb('08', 'Sala e varanda',
       'Estante do piso ao teto em <b>Tauari</b>, com <b>nichos em Carvalho '
       'Munique Duratex avançando do plano</b> e <b>LED sob eles</b>. Painel '
       'liso com <b>bite usinado</b> entre as folhas e mesa de jantar em '
       'Tauari com <b>chanfro usinado no tampo</b>.')}
  {amb('09', 'Quarto casal',
       'Guarda-roupa em Tauari com <b>portas de correr em vidro e perfil de '
       'alumínio bronze</b>. Cabeceira e peseira baú <b>estofadas em linho</b> '
       'sobre estrutura de marcenaria, e prateleiras suspensas em <b>tubo de '
       'alumínio preto</b>.')}
  {amb('10', 'Quarto solteiro',
       'Guarda-roupa em Tauari com <b>portas de correr em vidro bronze e '
       'perfil bronze</b>. Escrivaninha, nicho na cabeceira e prateleiras '
       'suspensas com <b>nichos em Cinza Essencial Duratex</b>.')}
  {amb('11', 'Banheiros',
       'No casal, gabinete em Tauari com puxador cava, <b>espelho com moldura '
       'em Tauari</b> e torre de prateleiras com <b>fundo em muxarabi</b> '
       'usinado. No social, gabinete em Tauari, espelho prata colado sobre '
       'chapa e prateleiras com <b>LED embutido na lateral</b>.')}
  {foot(3)}
</div></div>"""

# ── 4 · as duas linhas ────────────────────────────────────────────────────
def card(cen, g=False):
    itens = {
      'standard': [
        'Dobradiça <b>Hettich Novisys</b>',
        'Corrediça <b>telescópica</b>',
        'Roupeiro em <b>sistema de correr RO65 Prime, da Rometal</b>',
        'Estrutura, portas e prateleiras em <b>MDF de&nbsp;15&nbsp;mm</b>'],
      'gold': [
        'Dobradiça <b>Hettich Sensys</b> — pistão em gel e regulagem nos '
        'três eixos',
        'Corrediça <b>oculta Quadro, da Hettich</b>, com Silent System',
        'Roupeiro em <b>sistema de correr Dominus, da Rometal</b>',
        'Portas e prateleiras em <b>MDF de&nbsp;18&nbsp;mm</b> — mais rígidas, '
        'assentam melhor e não barrigam'],
    }[cen]
    li = ''.join(f'<li>{x}</li>' for x in itens)
    return f"""<div class="{'g' if g else ''}">
      <div class="nm serif">Linha<br>{'Gold' if g else 'Standard'}</div>

      <ul>{li}</ul>
      <div class="gar">Garantia Valvic de <b>{mt.GARANTIA[cen]}</b> sobre
        estrutura e ferragens</div>
    </div>"""

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">A especificação</div>
  <div class="h-sec serif">O que entra<br><em>em cada peça.</em></div>
  <div class="rule"></div>
  <p class="lead">A ferragem, a chapa e a construção que entram em cada peça
  desta proposta.</p>

  <div class="lin2 um">{card('standard')}</div>

  <div class="mesmo">
    <div><div class="k">Modulação</div><div class="d">A mesma em todo o
      conjunto, do estande ao decorado — <b>distribuição interna desenhada
      peça a peça</b>, não adaptada de módulo pronto.</div></div>
    <div><div class="k">Acabamento</div><div class="d"><b>Tauari, Carvalho
      Munique, Preto Absoluto, Cinza Pixel, Cerrado Bold e Cinza Essencial</b>,
      mais a laca verde, os vidros e os espelhos.</div></div>
    <div><div class="k">Quem faz</div><div class="d"><b>Equipe própria</b> do
      corte à instalação, com a medida conferida no local antes de
      cortar.</div></div>
  </div>

  <div class="nota"><b>Onde há laca, a caixa acompanha.</b> Nos armários da
  cozinha com frente em <b>laca fosca verde</b>, a estrutura interna sai em
  <b>MDF melamínico de cor próxima à da laca</b>, não em branco. É o que
  impede a caixa branca de aparecer na fresta entre as frentes e no vão da
  porta aberta — a peça lê a mesma cor por fora e por dentro.</div>

  <div class="nota">A garantia é <b>termo da Valvic
  sobre o conjunto que fornecemos e instalamos</b>, não repasse de garantia de
  fabricante, e cobre <b>estrutura e ferragens</b>.</div>
  {foot(4)}
</div></div>"""

# ── 5 · investimento e condições ──────────────────────────────────────────
NOME_AMB = {'Salão principal':'Salão principal','Copa':'Copa',
            'Sala de reunião':'Sala de reunião',
            'Sala de ativos':'Sala de ativos','Lounge':'Lounge',
            'Gourmet':'Bancada gourmet','Cozinha':'Cozinha e área de serviço',
            'Sala':'Sala e varanda','Quarto casal':'Quarto casal',
            'Quarto solteiro':'Quarto solteiro','Banheiro social':'Banheiro social',
            'Banheiro casal':'Banheiro casal'}

ESP_PV = {c: {am: round(mt.ESP_AMB[am]/(mt.BASE - (mt.MC_ALVO[c][am]
                                                  + mt.DELTA_FECH[c]))/10)*10
              for am in mt.AMBS} for c in mt.CEN}
AMB_PV = {c: {am: mt.PV[c][am] - ESP_PV[c][am] for am in mt.AMBS} for c in mt.CEN}
ESP_TOT_PV = {c: sum(ESP_PV[c].values()) for c in mt.CEN}

linhas, _fr = '', None
for am in mt.AMBS:
    fr = mt.FR_DE[am]
    rot = ('Estande' if fr == 'Stand' else 'Decorado') if fr != _fr else ''
    _fr = fr
    linhas += (f'<tr><td class="a">{rot}</td><td class="i">{NOME_AMB[am]}</td>'
               f'<td class="r">R$ {br(AMB_PV["standard"][am])}</td></tr>')
linhas += (f'<tr><td class="a">Terceiros</td><td class="i">Espelhos</td>'
           f'<td class="r">R$ {br(ESP_TOT_PV["standard"])}</td></tr>')

TOT_ST, TOT_GO = mt.TOT['standard'], mt.TOT['gold']

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Ambiente a ambiente.</div>
  <div class="rule"></div>

  <table class="invA">
    <thead><tr><th></th><th></th>
      <th class="r">Investimento<br><span style="font-weight:400;text-transform:none;letter-spacing:0;">linha Standard · {mt.GARANTIA['standard']} de garantia</span></th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="a"></td><td class="i">Investimento total</td>
        <td class="r">R$ {br(TOT_ST)}</td></tr>
    </tbody>
  </table>

  <div class="escP">
    <div class="l"><span class="p">50%</span><span class="q">de entrada, na assinatura</span></div>
    <div class="l"><span class="p">20%</span><span class="q">no início da montagem</span></div>
    <div class="l"><span class="p">15%</span><span class="q">na entrega</span></div>
    <div class="l"><span class="p">15%</span><span class="q">30 dias após a entrega</span></div>
  </div>

  <div class="cndP">
    <div><div class="k">Prazo de entrega</div><div class="d">
      <b>Até {PRAZO}</b>, contado da assinatura, da entrada e da medição
      final no local.</div></div>
    <div><div class="k">Escopo Valvic</div><div class="d">
      Do corte à instalação com <b>equipe própria</b>, e os terceiros de pedra,
      vidro, laca, espelho e estofado <b>entregues instalados</b>.</div></div>
    <div><div class="k">Validade da proposta</div><div class="d">
      <b>Até {VALIDADE}</b>.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>{mt.GARANTIA['standard']}</b> sobre estrutura e ferragens, na linha
      desta proposta.</div></div>
  </div>

  <div class="nota"><b>Não inclusos:</b> pedras e bancadas, alvenaria de apoio,
  rodapé, bancada e sóculo existentes da copa, louças, metais,
  eletrodomésticos, esquadrias em vidro e alumínio, box, gesso, pintura,
  revestimentos, comunicação visual, elétrica, hidráulica e o mobiliário
  solto.</div>

  {foot(5)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + p4 + p5 + '</body></html>')

(P/'proposta-marcelo-tolentino.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-marcelo-tolentino/', f'src="file://{P}/img-marcelo-tolentino/')
open('/tmp/in.html', 'w', encoding='utf-8').write(tmp)
import os
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-marcelo-tolentino.pdf')],
               check=True, env=env)

print(f'proposta-marcelo-tolentino.pdf · {NP} páginas')
print(f'  Investimento  R$ {br(TOT_ST):>9}   (linha Standard)')
print(f'  Prazo         {PRAZO}')
print(f'  Validade      até {VALIDADE}')
assert abs(sum(AMB_PV['standard'].values()) + ESP_TOT_PV['standard']
           - mt.TOT['standard']) < 1
print('  soma confere com o total')
