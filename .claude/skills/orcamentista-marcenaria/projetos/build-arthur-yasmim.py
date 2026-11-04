# -*- coding: utf-8 -*-
"""ARTHUR & YASMIM — proposta · closet  [14/10/2026]

⭐ [Jonathan 13-14/10] porta comprada pronta · dobradiça nossa R$ 12 ·
   portas pela política C (cascata de revenda + margem fixa por folha) ·
   marcenaria e iluminação a MC 30% · sem RT · ILUMINAÇÃO EM LINHA SEPARADA
   · principal com corrediça oculta Hettich e downgrade para telescópica.

⛔⛔ A CONTAGEM DE PORTAS FICA — e é exceção consciente. A cliente definiu
   os três cenários POR NÚMERO DE PORTA ("5 no reflecta bronze, 11 no
   fendi"). Sem o número, a versão 1 não se entende. É briefing dela
   voltando para ela, não quantitativo nosso vazando. O auditor roda com
   `--excecoes`. Todo o resto segue sem metragem.

Números de `corte-ay-closet.py`; nada digitado à mão.
⛔ Classes novas levam sufixo AY.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ay', P/'corte-ay-closet.py')
ay = importlib.util.module_from_spec(spec); sys.modules['ay'] = ay
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(ay)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, DATA = 'Arthur e Yasmim', '14 de outubro de 2026'
PRAZO, VALIDADE = '60 dias corridos', '7 dias úteis'
NP = 3

def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-arthur-yasmim'/n).read_bytes()).decode())
IMG1, IMG2, IMG3 = uri('ay-fundo.jpg'), uri('ay-sapateira.jpg'), uri('ay-bolsas.jpg')

MARC, LED = ay.OCULTA['TOT'], ay.LED_PV
MARC_T    = ay.TELESC['TOT']
CEN = [('1', 'Mista', 5, 11,
        'Cinco portas em <b>fumê</b> e onze em <b>MDF Fendi</b>, com a '
        'sapateira em espelho.'),
       ('2', 'Como o projeto', 16, 0,
        'Todas as portas em <b>fumê</b>, como a arquiteta desenhou, com a '
        'sapateira em espelho.'),
       ('3', 'Toda em Fendi', 0, 16,
        'Todas as portas em <b>MDF Fendi</b>, com a sapateira em espelho.')]
LIN = [(n, t, ay.portas(nf, nd), MARC + ay.portas(nf, nd) + LED,
        MARC_T + ay.portas(nf, nd) + LED, d) for n, t, nf, nd, d in CEN]

# ⛔⛔ TRAVA DE SOMA: cada cenário tem de fechar com as três linhas.
for n, t, pt, tot, tot_t, _d in LIN:
    assert abs((MARC + pt + LED) - tot) < 0.5, f'⛔ CENÁRIO {n} NÃO FECHA'
    assert abs((MARC_T + pt + LED) - tot_t) < 0.5, f'⛔ CENÁRIO {n}·T NÃO FECHA'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
.topAY{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4mm;border-bottom:1px solid var(--hair);flex:none;}
.topAY .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;letter-spacing:.02em;}
.topAY .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}
.leadAY{color:var(--soft);font-size:9.2pt;line-height:1.56;max-width:162mm;flex:none;}
.leadAY b{color:var(--ink);font-weight:600;}
.parAY{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:3.4mm;
  margin-top:4.4mm;flex:none;}
.parAY .ph{border-radius:5px;overflow:hidden;line-height:0;
  border:1px solid var(--hair);}
.parAY .ph img{display:block;width:100%;height:46mm;object-fit:cover;}
.capAY{font-size:7pt;color:var(--mut);letter-spacing:.04em;margin-top:1.6mm;flex:none;}
.itAY{margin-top:4.4mm;flex:none;}
.itAY .r{display:flex;gap:6mm;padding:2.4mm 0;border-top:1px solid var(--hair);}
.itAY .a{flex:none;width:28mm;font-size:6.9pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--gold);font-weight:700;padding-top:1mm;}
.itAY .t{flex:1;}
.itAY .n{font-weight:600;font-size:10pt;}
.itAY .d{color:var(--soft);font-size:8.4pt;line-height:1.5;margin-top:1mm;}
.itAY .d b{color:var(--ink);font-weight:600;}
.tecAY{display:grid;grid-template-columns:repeat(2,1fr);gap:2.8mm 7mm;
  margin-top:4mm;padding-top:3.2mm;border-top:1px solid var(--hair);flex:none;}
.tecAY .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.tecAY .d{color:var(--soft);font-size:8.3pt;margin-top:1mm;line-height:1.5;}
.tecAY .d b{color:var(--ink);}

.cenAY{border:1.2px solid var(--line);border-radius:5px;padding:4mm 5mm;
  margin-top:4mm;flex:none;}
.cenAY.hi{border-color:var(--gold-lt);background:rgba(201,169,106,.07);}
.cenAY .h{display:flex;align-items:baseline;gap:4mm;}
.cenAY .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  color:var(--gold);font-weight:700;line-height:1;}
.cenAY .t{font-size:12pt;font-weight:600;}
.cenAY .v{margin-left:auto;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:19pt;font-weight:700;white-space:nowrap;}
.cenAY .x{color:var(--soft);font-size:8.5pt;margin-top:1.6mm;}
.cenAY .x b{color:var(--ink);font-weight:600;}
.cenAY .l{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;
  margin-top:3mm;padding-top:2.6mm;border-top:1px solid var(--hair);}
.cenAY .l .k{font-size:6.7pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.cenAY .l .d{font-size:9pt;margin-top:.8mm;font-variant-numeric:tabular-nums;}

.optAY{margin-top:5mm;padding:4mm 5mm;background:var(--cream);
  border-left:2.5px solid var(--gold);flex:none;}
.optAY .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.optAY .d{color:var(--soft);font-size:8.5pt;margin-top:1.6mm;line-height:1.52;}
.optAY .d b{color:var(--ink);font-weight:600;}
.optAY table{width:100%;margin-top:2.6mm;font-size:8.6pt;border-collapse:collapse;}
.optAY td{padding:1.6mm 0;border-top:1px solid var(--line);}
.optAY td.r{text-align:right;font-weight:600;font-variant-numeric:tabular-nums;}

.escAY{margin-top:5mm;flex:none;}
.escAY .ttl{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding-bottom:1.6mm;}
.escAY .l{display:flex;justify-content:space-between;align-items:baseline;
  gap:6mm;padding:1.8mm 0;border-top:1px solid var(--hair);font-size:8.5pt;
  color:var(--soft);}
.escAY .l .x{flex:none;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndAY{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:5mm;
  padding-top:3.4mm;border-top:1px solid var(--hair);flex:none;}
.cndAY .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndAY .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.44;}
.cndAY .d b{color:var(--ink);}
.notaAY{margin-top:4.4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.52;flex:none;}
.notaAY b{color:var(--ink);}
.notaAY .h{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;margin-bottom:1.2mm;}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · closet</span><span>{n} / {NP}</span></div>')

ITENS = [
 ('Guardar', 'Os módulos do closet',
  'Do piso ao teto, em volta do quarto todo: <b>maleiro</b> no alto, '
  '<b>cabideiro</b> na altura de pendurar, <b>prateleiras</b> e, nos que '
  'pedem, <b>gaveteiro interno</b> — as gavetas ficam atrás do vidro, à '
  'vista, e por isso são feitas para serem vistas.'),
 ('Sentar', 'A penteadeira',
  'No centro da parede do fundo: <b>painel ripado</b>, <b>espelho com luz '
  'em todo o contorno</b>, bancada e os <b>dois blocos de gaveta</b> que '
  'ladeiam quem senta.'),
 ('Calçar', 'A sapateira',
  'Fora do closet, ao lado da porta. <b>Prateleiras inclinadas</b>, para o '
  'sapato aparecer inteiro, cada uma <b>com luz própria</b>, '
  '<b>porta-botas</b> no alto e uma <b>coluna lateral</b> para o miúdo.'),
 ('Fechar', 'As portas',
  'Folhas em <b>perfil de alumínio</b>, com o <b>puxador no próprio '
  'perfil</b> — sem puxador aplicado. A sapateira fecha em <b>espelho</b>.'),
]
itens = ''.join(
    f'<div class="r"><div class="a">{a}</div><div class="t">'
    f'<div class="n">{n}</div><div class="d">{d}</div></div></div>'
    for a, n, d in ITENS)

p1 = f"""<div class="page"><div class="pad">
  <div class="topAY">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>
  <div style="margin-top:6mm;" class="eyebrow">Closet</div>
  <div class="h-sec serif" style="font-size:24pt;">Um quarto inteiro<br>
    <em>para se vestir.</em></div>
  <div class="rule"></div>
  <div class="leadAY">Arthur, Yasmim — o closet de vocês ocupa as quatro
  paredes e se fecha em vidro, com a penteadeira no meio e a luz acesa em
  cada prateleira. É um móvel só, feito em <b>dez módulos</b>, e é assim
  que ele está orçado.</div>

  <div class="parAY">
    <div class="ph"><img src="{IMG1}" alt=""></div>
    <div class="ph"><img src="{IMG3}" alt=""></div>
    <div class="ph"><img src="{IMG2}" alt=""></div>
  </div>
  <div class="capAY">As imagens do projeto de vocês</div>

  <div class="itAY">{itens}</div>

  <div class="tecAY">
    <div><div class="k">As portas vêm prontas</div><div class="d">
      Folha de vidro em perfil de alumínio <b>não se monta em marcenaria</b>:
      vem pronta do fabricante de esquadria, e é o que garante o esquadro e
      o alinhamento. Nós recebemos, instalamos, alinhamos e respondemos
      por elas.</div></div>
    <div><div class="k">A gaveta atrás do vidro</div><div class="d">
      Num closet envidraçado a gaveta fica <b>à mostra o tempo todo</b>.
      Por isso a corrediça é <b>oculta</b>: não se vê trilho pela lateral,
      e a gaveta parece flutuar.</div></div>
  </div>
  {foot(1)}
</div></div>"""

cen = ''.join(
    f'<div class="cenAY{" hi" if n == "2" else ""}">'
    f'<div class="h"><div class="n">{n}</div><div class="t">{t}</div>'
    f'<div class="v">R$ {br(tot)}</div></div>'
    f'<div class="x">{d}</div>'
    f'<div class="l">'
    f'<div><div class="k">Marcenaria</div><div class="d">R$ {br(MARC)}</div></div>'
    f'<div><div class="k">Portas</div><div class="d">R$ {br(pt)}</div></div>'
    f'<div><div class="k">Iluminação</div><div class="d">R$ {br(LED)}</div></div>'
    f'</div></div>'
    for n, t, pt, tot, _tt, d in LIN)

p2 = f"""<div class="page"><div class="pad">
  <div class="topAY">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>
  <div style="margin-top:6mm;" class="eyebrow">As três formas</div>
  <div class="h-sec serif" style="font-size:24pt;">O closet é o mesmo.<br>
    <em>O que muda é a porta.</em></div>
  <div class="rule"></div>
  <div class="leadAY">Vocês pediram para ver de três jeitos. A marcenaria e
  a iluminação são <b>idênticas</b> nos três — o que anda é só o que se vê
  de fora. A sapateira fecha em <b>espelho</b> em todos.</div>
  {cen}

  <div class="optAY">
    <div class="k">Uma alternativa na ferragem</div>
    <div class="d">A corrediça <b>oculta</b> acima é a que recomendamos:
    num closet de portas de vidro, ela é o que faz a gaveta parecer
    flutuar. Com <b>corrediça telescópica</b>, que mostra o trilho pela
    lateral, o investimento fica:</div>
    <table>
      {''.join(f'<tr><td>{n} · {t}</td><td class="r">R$ {br(tt)}</td></tr>'
               for n, t, _pt, _tot, tt, _d in LIN)}
    </table>
  </div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="topAY">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>
  <div style="margin-top:6mm;" class="eyebrow">Condições</div>
  <div class="h-sec serif" style="font-size:25pt;">Como fazemos.</div>
  <div class="rule"></div>

  <div class="tecAY" style="margin-top:1mm;border-top:none;padding-top:0;">
    <div><div class="k">A luz é parte do móvel</div><div class="d">
      A fita e o perfil entram <b>usinados na própria peça</b>, não
      aparafusados depois. Está em <b>linha separada</b> no investimento,
      para vocês verem exatamente quanto ela custa.</div></div>
    <div><div class="k">Medição no local</div><div class="d">
      <b>Antes de cortar.</b> O caderno é de apresentação, e num móvel que
      dá a volta no quarto o prumo e o esquadro das paredes decidem a
      medida de cada módulo.</div></div>
  </div>

  <div class="escAY">
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

  <div class="cndAY">
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, contados do aceite e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Validade</div><div class="d">
      <b>{VALIDADE}</b> a partir desta data.</div></div>
  </div>

  <div class="notaAY">
    <div class="h">O que está e o que não está nesta proposta</div>
    <b>Está:</b> os dez módulos do closet com todo o interno, a penteadeira,
    a sapateira, as portas com a ferragem, a iluminação de marcenaria —
    fita, perfil e usinagem —, a medição no local, a entrega e a
    instalação.<br>
    <b>Não está:</b> a <b>fonte, o driver, o circuito e o interruptor</b> da
    iluminação, que são elétrica de obra; a <b>cadeira</b> da penteadeira;
    a pintura e o acabamento das paredes; o piso; e as <b>luminárias de
    teto</b>.<br>
    <b>A conferir antes da produção:</b> o <b>padrão do vidro</b> — o
    projeto indica reflecta e o fornecimento foi cotado em fumê, que são
    vidros diferentes; e o <b>vão da sapateira</b>, que fecha em
    <b>duas folhas</b> de espelho e não em uma, pelo peso de uma folha
    inteira nessa altura.</div>
  {foot(3)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + '</body></html>')

(P/'proposta-arthur-yasmim.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-arthur-yasmim.pdf')],
               check=True, env=env)
print(f'proposta-arthur-yasmim.pdf · {NP} páginas')
for n, t, pt, tot, tt, _d in LIN:
    print(f'  {n} · {t:<20} R$ {br(tot):>8}   (telescópica R$ {br(tt)})')
