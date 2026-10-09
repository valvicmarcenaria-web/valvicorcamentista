# -*- coding: utf-8 -*-
"""RAQUEL FRANCO — proposta · quarto e banheiro  [09/10/2026]

⭐ [Jonathan 09/10] "considere acabamento em laca conforme nosso motor ·
   palinha considere 950,00 o mt quadrado instalada."

Projeto PRJ_EXEC_RAQUEL_O_rn, designer Rubia Nascimento, Belo Horizonte.
Prazo de 60 dias corridos · validade de 7 dias úteis (até 20/10) — aceite
no limite + 60 corridos cai em 19/12, ainda em 2026, com 12 dias de folga.

Números de `corte-raquel.py`; nada digitado à mão.
⛔⛔ Sem metragem nem quantitativo de peça. "Cinco prateleiras de canto" é
   ENTREGÁVEL — é um dos quatro itens cotados —, não contagem de peça.
⛔ Classes novas levam sufixo RQ.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fr', P/'corte-raquel-franco.py')
fr = importlib.util.module_from_spec(spec); sys.modules['fr'] = fr
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(fr)
# ⭐ [Jonathan 09/10] duas versões, cada uma no SEU PDF. Lado a lado elas
#   mostrariam a cama com dois preços — a sobra de chapa dilui diferente
#   quando se compram 12 chapas em vez de 4 — e isso só confunde o cliente.
br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, DATA = 'Raquel Franco', '9 de outubro de 2026'
DESIGNER = 'Rubia Nascimento'
PRAZO, VALIDADE = '60 dias corridos', '7 dias úteis'
NP = 3   # ⭐ o roupeiro ganha página própria [Jonathan 09/10]

def uri(nome):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img'/nome).read_bytes()).decode())
IMG = uri('franco-render.jpg')      # ⭐ o render do próprio caderno

G, L = fr.NOVOV['PV'], fr.LAQUEADO['PV']
# ⛔ descrições curtas: são oito itens. O que o cliente não deduz sozinho
#   fica na faixa técnica; aqui, uma linha por peça.
ITENS = [
 ('Quarto', 'Escrivaninha em L', G['Escrivaninha em L'], G['Escrivaninha em L'],
  'Tampo em <b>MDF Noce Amêndoa</b> de corpo cheio, com as gavetas '
  '<b>embutidas na própria espessura</b>, <b>caixa de tomadas</b> e nicho.'),
 ('Quarto', 'Armários aéreos', G['Armário aéreo menor'] + G['Armário aéreo maior'],
  G['Armário aéreo menor'] + G['Armário aéreo maior'],
  'Dois volumes suspensos em <b>MDF Lume</b>, de cantos arredondados e '
  '<b>puxador passante</b> — sem ferragem aparente.'),
 ('Quarto', 'Prateleira superior', G['Prateleira superior'], G['Prateleira superior'],
  'Em <b>MDF Cancún</b>, de corpo cheio, sobre <b>suporte invisível</b>.'),
 ('Quarto', 'Módulos cama e mesa', G['Módulo cama'] + G['Módulo mesa'],
  G['Módulo cama'] + G['Módulo mesa'],
  'Em <b>MDF Lume</b>, com a <b>face curva</b> do desenho e o recuo para '
  'descer a persiana.'),
 ('Quarto', 'Painel de cabeceira', G['Painel de cabeceira'], G['Painel de cabeceira'],
  'Em L pelas duas paredes, em <b>MDF Cancún</b> e <b>Sal Rosa</b>.'),
 ('Quarto', 'Roupeiro novo', L['Roupeiro'], G['Roupeiro'],
  'Prateleiras, gavetas, <b>duas sapateiras deslizantes</b>, cabideiro '
  'oval e o vão como puxador. <b>Laqueado ou em melamínico: página 3.</b>'),
 ('Banheiro', 'Armário sob a cuba', G['Banheiro · armário inferior'], G['Banheiro · armário inferior'],
  'Em <b>MDF Verde Ultra</b>, resistente à umidade, com puxadores de '
  '<b>porcelana</b>.'),
 ('Banheiro', 'Armário-torre', G['Banheiro · armário superior'], G['Banheiro · armário superior'],
  'Em <b>MDF Verde Ultra</b>, do piso ao teto, com <b>puxador passante</b>.'),
 ('Banheiro', 'Espelho', G['Banheiro · espelho'], G['Banheiro · espelho'],
  '⭐ <b>Fornecido por nós</b> — não é item à parte para comprar depois. '
  'Vem com o <b>recorte escalopado</b> na borda inferior, usinado conforme '
  'o detalhe da prancha, e instalado junto da marcenaria.'),
]
_TOT_MOTOR = (fr.LAQUEADO['TOT'], fr.NOVOV['TOT'])
TOT_LQ = sum(it[2] for it in ITENS)
TOT_ML = sum(it[3] for it in ITENS)
# ⛔⛔ TRAVA DE SOMA — ver nota no build da Raquel Oliveira.
for _t, _i in ((TOT_LQ, 2), (TOT_ML, 3)):
    _s = sum(it[_i] for it in ITENS)
    assert abs(_s - _t) < 0.5, (
        f'⛔ A TABELA NÃO FECHA: as linhas somam {_s:,.0f} e o total diz '
        f'{_t:,.0f}. Falta ou sobra item na lista.')

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── Raquel · quarto infantil ─────────────────────────────────────────── */
/* ⛔ flex:none em TODO bloco fechado: .pad é coluna flex e um box com
      overflow:hidden ENCOLHE em silêncio quando a coluna estoura. */
.topRQ{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4.2mm;border-bottom:1px solid var(--hair);flex:none;}
.topRQ .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;letter-spacing:.02em;}
.topRQ .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}

.leadRQ{color:var(--soft);font-size:9pt;line-height:1.5;max-width:160mm;
  flex:none;}
.leadRQ b{color:var(--ink);font-weight:600;}

.heroRQ{margin-top:4.2mm;border-radius:5px;overflow:hidden;line-height:0;
  border:1px solid var(--hair);flex:none;}
.heroRQ img{display:block;width:100%;height:38mm;object-fit:cover;
  object-position:center 68%;}
.capRQ{font-size:7pt;color:var(--mut);letter-spacing:.04em;margin-top:1.6mm;
  flex:none;}
.itRQ{margin-top:4mm;flex:none;}
.itRQ .r{display:flex;gap:6mm;padding:1.6mm 0;border-top:1px solid var(--hair);}
.itRQ .a{flex:none;width:26mm;font-size:6.9pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--gold);font-weight:700;padding-top:1mm;}
.itRQ .t{flex:1;}
.itRQ .n{font-weight:600;font-size:9.4pt;}
.itRQ .d{color:var(--soft);font-size:8.1pt;line-height:1.44;margin-top:.8mm;}
.itRQ .d b{color:var(--ink);font-weight:600;}

.tecRQ{display:grid;grid-template-columns:repeat(2,1fr);gap:3mm 7mm;
  margin-top:3.4mm;padding-top:2.8mm;border-top:1px solid var(--hair);flex:none;}
.tecRQ .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.tecRQ .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.45;}
.tecRQ .d b{color:var(--ink);}

table.invRQ{width:100%;border-collapse:collapse;margin-top:3.4mm;font-size:9pt;}
table.invRQ th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.2mm;text-align:left;}
table.invRQ th.r,table.invRQ td.r{text-align:right;}
table.invRQ td{padding:2mm 0;border-top:1px solid var(--hair);vertical-align:top;}
table.invRQ td.a{font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold);font-weight:700;width:28mm;padding-top:2.6mm;}
table.invRQ td.i{font-weight:600;}
table.invRQ tr.tot td{border-top:1.6px solid var(--ink);padding-top:3mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;font-weight:700;}
table.invRQ tr.tot td.a,table.invRQ tr.tot td.i{font-family:inherit;
  font-size:9.6pt;}

.escRQ{margin-top:4.5mm;flex:none;}
.escRQ .ttl{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding-bottom:1.6mm;}
.escRQ .l{display:flex;justify-content:space-between;align-items:baseline;
  gap:6mm;padding:1.6mm 0;border-top:1px solid var(--hair);font-size:8.5pt;
  color:var(--soft);}
.escRQ .l .x{flex:none;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}

.invRQ th.g,.invRQ td.g{color:var(--gold);}
.duasRQ{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:4.5mm;
  flex:none;}
.duasRQ > div{border:1.2px solid var(--line);border-radius:5px;padding:3.6mm;}
.duasRQ > div.g{border-color:var(--gold);background:rgba(201,169,106,.07);}
.duasRQ .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.duasRQ .d{color:var(--soft);font-size:8.3pt;margin-top:1.4mm;line-height:1.5;}
.duasRQ .d b{color:var(--ink);font-weight:600;}
.invRQ th.g,.invRQ td.g{color:var(--gold);}
.cmpRQ{margin-top:4.5mm;flex:none;}
.cmpRQ .l{display:flex;justify-content:space-between;align-items:center;
  gap:6mm;padding:3mm 4mm;border:1.2px solid var(--line);border-radius:5px;
  margin-bottom:2.6mm;}
.cmpRQ .l.g{border-color:var(--gold);background:rgba(201,169,106,.07);}
.cmpRQ .q{font-size:8.4pt;color:var(--soft);line-height:1.45;}
.cmpRQ .q b{color:var(--ink);font-weight:600;}
.cmpRQ .v{flex:none;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:17pt;font-weight:700;}
.cmpRQ .l.g .v{color:var(--gold);}
.porqueRQ{margin-top:4.5mm;border:1.5px solid var(--gold);border-radius:5px;
  background:rgba(201,169,106,.07);padding:4.6mm 5mm;flex:none;}
.porqueRQ .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.porqueRQ .d{color:var(--soft);font-size:8.3pt;margin-top:1.6mm;
  line-height:1.52;}
.porqueRQ .d b{color:var(--ink);font-weight:600;}
.valRQ{margin-top:4.5mm;padding:4mm 5.5mm;background:var(--ink);color:#fff;
  border-radius:4px;display:flex;align-items:baseline;gap:6mm;flex:none;}
.valRQ .k{flex:none;font-size:7.2pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;}
.valRQ .d{flex:none;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:14.5pt;font-weight:700;}
.valRQ .t{flex:1;font-size:8.1pt;color:#D7D0C3;line-height:1.5;text-align:right;}

.cndRQ{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:4.5mm;
  padding-top:3.2mm;border-top:1px solid var(--hair);flex:none;}
.cndRQ .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndRQ .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.44;}
.cndRQ .d b{color:var(--ink);}
.notaRQ{margin-top:3.6mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.5;flex:none;}
.notaRQ b{color:var(--ink);}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · quarto e banheiro</span><span>{n} / {NP}</span></div>')

itens = ''.join(
    f'<div class="r"><div class="a">{a}</div><div class="t">'
    f'<div class="n">{n}</div><div class="d">{d}</div></div></div>'
    for a, n, _pl, _pm, d in ITENS)

linhas = ''.join(
    f'<tr><td class="a">{a}</td><td class="i">{n}</td>'
    f'<td class="r">R$ {br(pl)}</td><td class="r g">R$ {br(pm)}</td></tr>'
    for a, n, pl, pm, _d in ITENS)

p1 = f"""<div class="page"><div class="pad">
  <div class="topRQ">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:6mm;" class="eyebrow">Quarto e banheiro</div>
  <div class="h-sec serif" style="font-size:24pt;">O quarto inteiro,<br>
    <em>curva por curva.</em></div>
  <div class="rule"></div>
  <div class="leadRQ">Raquel, o projeto da <b>{DESIGNER}</b> chegou
  completo — onze pranchas, com cada curva e cada nicho desenhados. Esta
  proposta executa o <b>quarto e o banheiro</b>, do painel de cabeceira ao
  armário-torre.</div>

  <div class="heroRQ"><img src="{IMG}" alt=""></div>
  <div class="capRQ">O projeto da {DESIGNER}</div>

  <div class="itRQ">{itens}</div>

  {foot(1)}
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="topRQ">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:6mm;" class="eyebrow">O investimento</div>
  <div class="h-sec serif" style="font-size:25pt;">Peça a peça.</div>
  <div class="rule"></div>

  <table class="invRQ">
    <thead><tr><th></th><th></th>
      <th class="r">Roupeiro laqueado</th>
      <th class="r g">Roupeiro melamínico</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="a"></td><td class="i">Investimento total</td>
        <td class="r">R$ {br(TOT_LQ)}</td>
        <td class="r g">R$ {br(TOT_ML)}</td></tr>
    </tbody>
  </table>

  <div class="valRQ">
    <div class="k">Entrega</div>
    <div class="d">Ainda em 2026</div>
    <div class="t">Estamos fechando a agenda de produção do ano —<br>
    e há uma vaga reservada para o quarto.</div>
  </div>

  <div class="escRQ">
    <div class="ttl">Condições de pagamento</div>
    <div class="l"><div>30% de entrada + restante em até 10× no cartão</div>
      <div class="x">sem desconto</div></div>
    <div class="l"><div>50% de entrada + restante em até 8× no cartão</div>
      <div class="x">−3%</div></div>
    <div class="l"><div>70% de entrada + restante em até 6× no cartão</div>
      <div class="x">−5%</div></div>
    <div class="l"><div>70% de entrada + saldo por transferência</div>
      <div class="x">−7%</div></div>
  </div>

  <div class="cndRQ">
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, contados do aceite e da medição.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens das peças
      novas.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Validade</div><div class="d">
      <b>{VALIDADE}</b> a partir desta data.</div></div>
  </div>

  <div class="notaRQ"><b>Não inclusos:</b> cama e cabeceira estofada,
  cadeira, colchão, luminárias e pendentes, persiana, espelho, tapete,
  papel de parede e o mobiliário solto. A <b>elétrica</b> é de terceiro —
  nossa é a usinagem da passagem e a caixa de tomadas do tampo.</div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="topRQ">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:6mm;" class="eyebrow">Uma recomendação técnica</div>
  <div class="h-sec serif" style="font-size:24pt;">O roupeiro<br>
    <em>sai novo.</em></div>
  <div class="rule"></div>
  <div class="leadRQ">É a única coisa em que nos afastamos do caderno — e
  vale explicar por quê, porque a recomendação <b>não é de preço</b>.</div>

  <div class="cmpRQ">
    <div class="l"><div class="q"><b>Novo, laqueado</b> — corpo em Branco
      TX e acabamento em <b>laca fosca Sayerlack J029</b>, a cor que a
      designer especificou</div>
      <div class="v">R$ {br(fr.LAQUEADO['PV']['Roupeiro'])}</div></div>
    <div class="l g"><div class="q"><b>Novo, em melamínico</b> —
      revestimento de fábrica, que não pede repintura ao longo da vida do
      móvel</div>
      <div class="v">R$ {br(fr.NOVOV['PV']['Roupeiro'])}</div></div>
  </div>
  <div class="capRQ">Os dois são <b>roupeiros novos</b>. O que muda é o
  acabamento: a laca dá a cor exata do projeto; o melamínico dá
  durabilidade e custa
  <b>R$ {br(fr.LAQUEADO['PV']['Roupeiro'] - fr.NOVOV['PV']['Roupeiro'])} a menos</b>.</div>

  <div class="porqueRQ">
    <div class="k">Por que o roupeiro sai novo</div>
    <div class="d">O caderno sugere <b>preservar a estrutura e reaproveitar
    as portas</b>, com preparo de superfície e laca. <b>Não recomendamos</b>
    — e, ao contrário do que parece, <b>não é um caminho mais barato</b>.
    Preparar e lacar portas antigas exige lixamento, selagem e cura, e
    ainda acrescenta vistoria da estrutura, desmontagem, transporte e
    remedição do vão. O que se economiza em chapa volta em processo.<br><br>
    O que pesa mais, porém, é o <b>risco</b>. Aproveitando, a Valvic passa a
    responder por uma <b>estrutura que não construiu</b> e não consegue
    inspecionar por dentro, pela <b>aderência da laca sobre madeira antiga
    já envernizada</b> e pela <b>compatibilidade</b> do interior novo com um
    vão que o próprio projeto manda conferir antes de fabricar. Se a
    estrutura reprovar depois de desmontada, a obra para.<br><br>
    <b>A nossa garantia de 10 anos não alcança peça de terceiro.</b> Com o
    roupeiro novo, ela alcança tudo.</div>
  </div>


  <div class="tecRQ">
    <div><div class="k">As curvas</div><div class="d">
      Os módulos da cama e da mesa têm <b>face curva</b>, e os aéreos têm
      <b>cantos arredondados</b>. Não é corte: é <b>usinagem e lâmina
      flexível</b>, peça a peça — o que o desenho pede e o que separa este
      projeto de um armário reto.</div></div>
    <div><div class="k">O banheiro</div><div class="d">
      <b>MDF Verde Ultra</b> nos dois armários, <b>resistente à
      umidade</b>, como a prancha especifica. Em banheiro, chapa comum
      incha pela borda em poucos anos.</div></div>
  </div>
  <div class="tecRQ">
    <div><div class="k">O que ganhamos</div><div class="d">
      Portas <b>novas e no esquadro</b>, interior desenhado sem a amarra do
      vão existente, <b>dobradiça nova</b> e acabamento de fábrica em toda
      a peça.</div></div>
    <div><div class="k">O que a Raquel ganha</div><div class="d">
      <b>Dez anos de garantia sobre o roupeiro inteiro</b> — estrutura,
      portas e ferragem —, e um prazo que não depende do que se vai
      encontrar quando o móvel antigo for aberto.</div></div>
  </div>
  {foot(3)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + '</body></html>')

(P/'proposta-raquel-franco.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-raquel-franco.pdf')],
               check=True, env=env)
print(f'proposta-raquel-franco.pdf · {NP} páginas')
print(f'  {"":<28}{"laqueado":>11}{"melamínico":>13}')
for _, n, pl, pm, _d in ITENS:
    print(f'  {n:<28}{br(pl):>11}{br(pm):>13}')
print(f'  {"INVESTIMENTO":<28}{br(TOT_LQ):>11}{br(TOT_ML):>13}')
print(f'  {"MC":<28}'
      f'{(fr.BASE - fr.LAQUEADO["CD"]/TOT_LQ)*100:>10.1f}%'
      f'{(fr.BASE - fr.NOVOV["CD"]/TOT_ML)*100:>12.1f}%   com RT')
