# -*- coding: utf-8 -*-
"""ISABELA LEÃO — proposta · home office  [09/10/2026]

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
spec = importlib.util.spec_from_file_location('iz', P/'corte-isabela.py')
iz = importlib.util.module_from_spec(spec); sys.modules['iz'] = iz
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(iz)
# ⭐ [Jonathan 09/10] duas versões, cada uma no SEU PDF. Lado a lado elas
#   mostrariam a cama com dois preços — a sobra de chapa dilui diferente
#   quando se compram 12 chapas em vez de 4 — e isso só confunde o cliente.
br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, DATA = 'Isabela Leão', '9 de outubro de 2026'
DESIGNER = 'Rubia Nascimento'
PRAZO, VALIDADE = '60 dias corridos', '7 dias úteis'
NP = 2

def uri(nome):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img'/nome).read_bytes()).decode())
# ⛔ só vistas SEM cota dentro do quadro. Os desenhos de produto (estante,
#   mesa, gaveteiro) trazem as medidas no próprio desenho e ficam de fora:
#   metragem não vai para proposta, nem desenhada.
IMG1, IMG4 = uri('isabela-vista2.jpg'), uri('isabela-vista3.jpg')

ITENS = [
 ('Guardar', 'Estante', iz.PV['Estante'],
  'A <b>parede inteira</b>, do piso ao teto, em <b>MDF Azul Vel '
  'Berneck</b>: vinte e cinco nichos, prateleiras em quase todos e os '
  '<b>arcos</b> que a designer desenhou no fundo. Na base, <b>portas</b> '
  'para o que não fica à mostra.'),
 ('Trabalhar', 'Mesa em L', iz.PV['Mesa em L'],
  'Tampo em <b>MDF Peroba Guararapes</b>, de <b>corpo cheio</b>, sobre '
  'apoio em <b>Azul Vel Berneck</b> — o mesmo azul da estante. O retorno '
  'acompanha a cadeira e termina em <b>ponta curva</b>.'),
 ('Arquivar', 'Gaveteiro com arquivo', iz.PV['Gaveteiro com arquivo'],
  '<b>Sobre rodízio</b>, para entrar e sair de debaixo da mesa. Gaveta '
  'rasa em cima e, embaixo, a <b>gaveta-arquivo com quadro para pasta '
  'suspensa</b>. Puxador <b>Tinyhob</b>, como especificado.'),
]
TOTAL = iz.TOT

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

.leadRQ{color:var(--soft);font-size:9.2pt;line-height:1.56;max-width:160mm;
  flex:none;}
.leadRQ b{color:var(--ink);font-weight:600;}

.parRQ{display:grid;grid-template-columns:1.10fr 1.04fr;gap:4mm;
  margin-top:4.2mm;flex:none;}
.parRQ .phRQ{border-radius:5px;overflow:hidden;line-height:0;
  border:1px solid var(--hair);}
.parRQ .phRQ img{display:block;width:100%;height:62mm;object-fit:cover;
  object-position:center;}
.capRQ{font-size:7pt;color:var(--mut);letter-spacing:.04em;margin-top:1.6mm;
  flex:none;}
.itRQ{margin-top:4mm;flex:none;}
.itRQ .r{display:flex;gap:6mm;padding:2.5mm 0;border-top:1px solid var(--hair);}
.itRQ .a{flex:none;width:26mm;font-size:6.9pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--gold);font-weight:700;padding-top:1mm;}
.itRQ .t{flex:1;}
.itRQ .n{font-weight:600;font-size:10pt;}
.itRQ .d{color:var(--soft);font-size:8.4pt;line-height:1.5;margin-top:1mm;}
.itRQ .d b{color:var(--ink);font-weight:600;}

.tecRQ{display:grid;grid-template-columns:repeat(2,1fr);gap:3.2mm 7mm;
  margin-top:4mm;padding-top:3.2mm;border-top:1px solid var(--hair);flex:none;}
.tecRQ .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.tecRQ .d{color:var(--soft);font-size:8.3pt;margin-top:1mm;line-height:1.5;}
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
            f'<span>{CLIENTE} · home office</span><span>{n} / {NP}</span></div>')

itens = ''.join(
    f'<div class="r"><div class="a">{a}</div><div class="t">'
    f'<div class="n">{n}</div><div class="d">{d}</div></div></div>'
    for a, n, _p, d in ITENS)

linhas = ''.join(
    f'<tr><td class="a">{a}</td><td class="i">{n}</td>'
    f'<td class="r">R$ {br(p)}</td></tr>' for a, n, p, _d in ITENS)

p1 = f"""<div class="page"><div class="pad">
  <div class="topRQ">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:6mm;" class="eyebrow">Home office</div>
  <div class="h-sec serif" style="font-size:24pt;">Uma parede<br>
    <em>que trabalha.</em></div>
  <div class="rule"></div>
  <div class="leadRQ">Isabela, o projeto da <b>{DESIGNER}</b> chegou
  detalhado — e a marcenaria dele é o que fica: a estante que ocupa a
  parede, a mesa em L e o gaveteiro que entra debaixo dela.</div>

  <div class="parRQ">
    <div class="phRQ"><img src="{IMG1}" alt=""></div>
    <div class="phRQ"><img src="{IMG4}" alt=""></div>
  </div>
  <div class="capRQ">As vistas do caderno da {DESIGNER}</div>

  <div class="itRQ">{itens}</div>

  <div class="tecRQ">
    <div><div class="k">Estante</div><div class="d">
      <b>MDF Azul Vel Berneck</b> em toda a peça, <b>fundo na mesma cor</b>
      — nicho aberto não mostra chapa branca atrás. Fita de borda em todas
      as bordas aparentes.</div></div>
    <div><div class="k">Mesa</div><div class="d">
      Tampo em <b>MDF Peroba Guararapes</b> de <b>corpo cheio</b>,
      construído em camadas para chegar à espessura do desenho.</div></div>
    <div><div class="k">Bordas · o que muda</div><div class="d">
      A <b>ponta curva</b> do retorno é feita e recebe <b>fita flexível</b>.
      Já a <b>quina não abaúla</b>: em melamínico o revestimento é um filme
      de superfície, e arredondar a aresta expõe o miolo.</div></div>
    <div><div class="k">Medição</div><div class="d">
      <b>No local, antes do corte.</b> O caderno pede isso em todas as
      pranchas — e numa estante de parede inteira o prumo decide.</div></div>
  </div>
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
    <thead><tr><th></th><th></th><th class="r">Investimento</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="a"></td><td class="i">Investimento total</td>
        <td class="r">R$ {br(TOTAL)}</td></tr>
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

  <div class="notaRQ"><b>Não inclusos:</b> poltrona, cadeira, luminárias
  e pendentes, quadros, plantas, tapete, livros e o mobiliário solto.
  A <b>transferência dos pontos de tomada</b> é elétrica de terceiro —
  nossa é a usinagem da passagem na peça.</div>
  {foot(2)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + '</body></html>')

(P/'proposta-isabela.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-isabela.pdf')],
               check=True, env=env)
print(f'proposta-isabela.pdf · {NP} páginas')
for _, n, p, _d in ITENS: print(f'  {n:<28} R$ {br(p):>8}')
print(f'  {"INVESTIMENTO":<28} R$ {br(TOTAL):>8}'
      f'   MC {(iz.BASE - iz.CD/TOTAL)*100:.1f}%  ·  com RT')
