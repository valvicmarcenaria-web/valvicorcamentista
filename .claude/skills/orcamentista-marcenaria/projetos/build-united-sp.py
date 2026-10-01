# -*- coding: utf-8 -*-
"""PROPOSTA — UNITED SP · pavimentos 8 e 9  [01/10/2026]

Números vêm de `corte-united-sp.py`; nada é digitado à mão aqui.

⛔⛔ NUNCA PÔR METRAGEM NEM QUANTITATIVO NA PROPOSTA
   (referencias/proposta-comercial.md · SKILL.md FASE 3)
   Sem cota, sem m², sem contagem de porta, painel, prateleira ou suporte.
   ⭐ EXCEÇÃO ÚNICA, autorizada pelo Jonathan em 01/10: a ALTURA DO PANO
   RIPADO DO HALL (2,73 m) aparece, porque é a informação que explica por
   que o painel não encosta no teto. O auditor libera só ela.
⛔ Classes novas levam sufixo U: `.invU`, `.escU`, `.cndU`, `.phU`, `.itU`.
   (`css-proposta.css` já define `.inv`, `.pay`, `.it`, `.esc`, `.cnd`.)
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('u', P/'corte-united-sp.py')
u = importlib.util.module_from_spec(spec); sys.modules['u'] = u
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(u)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE = 'United'
OBRA    = 'São Paulo · pavimentos 8 e 9'
PROJETO = 'VD Arquitetura'
DATA    = '1º de outubro de 2026'
PRAZO   = '75 dias corridos'
VALID   = '10 dias corridos'
NP      = 4

def img(n): return f'img-united-sp/{n}.jpg'

CSS = (open(P/'css-proposta.css', encoding='utf-8').read()
       + open(P/'css-proposta-img.css', encoding='utf-8').read() + """
/* ── proposta United SP ───────────────────────────────────────────────── */
.phU{background:#fff;overflow:hidden;position:relative;
  border:1px solid var(--hair);}
.phU img{display:block;width:100%;height:100%;object-fit:cover;object-position:center;}
.phU img.ct{object-fit:contain;}

.itU{margin-top:5.4mm;}
.itU .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;
  color:var(--gold-lt);font-weight:600;line-height:1;}
.itU .t{font-size:11.4pt;font-weight:700;letter-spacing:-.01em;margin-top:.6mm;}
.itU .d{color:var(--soft);font-size:8.7pt;line-height:1.64;margin-top:1.8mm;}
.itU .d b{color:var(--ink);font-weight:600;}
.parU{display:grid;grid-template-columns:1fr 1fr;gap:4mm;}
.parU .phU{height:62mm;}
.bandaU{height:46mm;}

.exU{display:grid;grid-template-columns:1fr 1fr;gap:5mm 7mm;margin-top:5mm;}
.exU > div{border-top:1.5px solid var(--line);padding-top:3.2mm;}
.exU .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.exU .d{color:var(--soft);font-size:8.6pt;line-height:1.6;margin-top:1.6mm;}
.exU .d b{color:var(--ink);font-weight:600;}

table.invU{width:100%;border-collapse:collapse;margin-top:4mm;font-size:9pt;}
table.invU th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.4mm;text-align:left;}
table.invU th.r,table.invU td.r{text-align:right;}
table.invU td{padding:1.7mm 0;border-top:1px solid var(--hair);vertical-align:top;}
table.invU td.a{font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;padding-right:4mm;width:30mm;}
table.invU td.i{font-weight:600;}
table.invU tr.sub td{border-top:1px solid var(--line);color:var(--soft);
  font-size:8pt;padding:1.3mm 0;}
table.invU tr.tot td{border-top:1.6px solid var(--ink);padding-top:2.2mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;font-weight:700;}
table.invU tr.tot td.a,table.invU tr.tot td.i{font-family:inherit;font-size:9.6pt;}

.escU{margin-top:4mm;border:1px solid var(--line);border-radius:5px;
  overflow:hidden;flex:none;}
.escU .l{display:flex;justify-content:space-between;align-items:baseline;
  padding:2mm 5mm;border-bottom:1px solid var(--hair);font-size:9pt;}
.escU .l:last-child{border-bottom:none;}
.escU .l .p{font-weight:700;font-size:11pt;color:var(--gold);min-width:14mm;}
.escU .l .q{color:var(--soft);flex:1;padding-left:4mm;}

.mobU{margin-top:4mm;border:1.5px solid var(--gold);border-radius:5px;
  background:var(--gold-pale);padding:3.6mm 5.2mm;display:grid;
  grid-template-columns:1fr auto;gap:2mm 7mm;align-items:start;flex:none;}
.mobU .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.mobU .t{font-size:11pt;font-weight:700;margin-top:1mm;}
.mobU .d{color:var(--soft);font-size:8.3pt;line-height:1.56;margin-top:1.8mm;
  grid-column:1/2;grid-row:2/3;}
.mobU .d b{color:var(--ink);font-weight:600;}
.mobU .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;
  font-weight:700;white-space:nowrap;grid-column:2/3;grid-row:1/3;
  align-self:center;text-align:right;}
.totU{display:flex;justify-content:space-between;align-items:baseline;
  margin-top:3.6mm;padding-top:2.4mm;border-top:1.6px solid var(--ink);flex:none;}
.totU .l{font-size:9.6pt;font-weight:600;}
.totU .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
  font-weight:700;}

.cndU{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm 5mm;margin-top:4mm;
  flex:none;}
.cndU .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndU .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.42;}
.cndU .d b{color:var(--ink);}
.notaU{margin-top:4.5mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:8pt;color:var(--soft);line-height:1.5;flex:none;}
.notaU b{color:var(--ink);}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · {OBRA}</span><span>{n} / {NP}</span></div>')

def it(num, titulo, desc):
    return (f'<div class="itU"><div class="n serif">{num}</div>'
            f'<div class="t">{titulo}</div><div class="d">{desc}</div></div>')

# ── 1 · capa ──────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="cv2">
  <div class="txt">
    <div class="eyebrow">Proposta comercial</div>
    <div class="cv-t serif">Marcenaria corporativa.</div>
    <div class="cv-nome serif" style="font-size:52pt;">{CLIENTE}</div>
    <div class="cv-s">Pavimentos 8 e 9 — copas, halls dos elevadores,
    prateleiras e fechamentos. Projeto {PROJETO}.</div>
    <div class="cv-meta">
      <div><div class="k">Cliente</div><div class="v">{CLIENTE}</div></div>
      <div><div class="k">Obra</div><div class="v">São Paulo · SP</div></div>
      <div><div class="k">Projeto</div><div class="v">{PROJETO}</div></div>
      <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    </div>
    <div style="margin-top:auto;"><div class="cv-brand">Valvic Marcenaria</div></div>
  </div>
  <div class="ph"><img src="{img('painel-nichos')}" alt=""></div>
</div></div>"""

# ── 2 · escopo ────────────────────────────────────────────────────────────
p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O escopo</div>
  <div class="h-sec serif">O que a Valvic<br>faz nos dois andares.</div>
  <div class="rule"></div>

  <div class="parU" style="margin-top:5mm;">
    <div class="phU"><img class="ct" src="{img('cozinha-9')}" alt=""></div>
    <div class="phU"><img class="ct" src="{img('cozinha-8')}" alt=""></div>
  </div>

  {it('01', 'Copas',
      'Bancadas corridas em <b>MDF Guararapes Tauari</b>, com <b>ferragem '
      'Hettich</b> — dobradiça Sensys e corrediça oculta Quadro. Os aéreos em '
      '<b>puxador passante</b> e os inferiores em <b>puxador cava</b> — nenhuma '
      'alça aparente. Prateleiras e aéreos em <b>MDF Guararapes Dual Black</b> '
      'desenham a faixa escura sobre a pedra. No oitavo andar entram ainda o '
      'módulo da cuba e a <b>bancada alta em Dual Black</b> para as banquetas.')}

  {it('02', 'Halls dos elevadores',
      'Painel do piso ao teto em <b>MDF Guararapes Azul Petróleo com '
      'acabamento ripado</b>, que absorve as <b>portas mimetizadas do hidrante '
      'e da escada</b> — o puxador é usinado na própria ripa e some no desenho. '
      'Nichos em <b>MDF Arauco Attena</b> e <b>iluminação indireta embutida na '
      'sanca</b>. No lado oposto, painel liso em Tauari emoldurando a porta de '
      'vidro. O conjunto se repete nos dois pavimentos.')}

  {it('03', 'Prateleiras suspensas',
      'Prateleiras em <b>Tauari de corpo cheio</b>, fixadas em <b>suporte '
      'oculto</b> — nenhuma mão-francesa aparente, nenhum parafuso à vista. '
      'Distribuídas pelas salas de reunião, lounges e áreas de apoio dos dois '
      'andares, inclusive uma em L.')}

  {it('04', 'Fechamento dos quadros de energia',
      'Fechamento em <b>MDF Guararapes Azul Petróleo</b> no mesmo tom do painel '
      'do hall, com <b>porta e tranca por chave</b>, alinhado às portas '
      'existentes. Nos dois pavimentos.')}
  {foot(2)}
</div></div>"""

# ── 3 · como é feito ──────────────────────────────────────────────────────
p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Como é feito</div>
  <div class="h-sec serif">O que sustenta<br><em>o desenho.</em></div>
  <div class="rule"></div>
  <p class="lead">O projeto pede volume: laterais, montantes e prateleiras com
  corpo, não chapa fina. É isso que define o método de produção, e é onde está
  a diferença entre executar o desenho e apenas aproximá-lo.</p>

  <div class="exU">
    <div><div class="k">Montantes encorpados</div><div class="d">
      Laterais aparentes, travessas e prateleiras são <b>construídas em
      camadas</b> — faces e miolo estruturado — para chegar ao corpo que o
      projeto desenha. É o que dá a leitura de volume maciço nas bordas.</div></div>

    <div><div class="k">O painel sem emenda</div><div class="d">
      O painel do hall sobe em duas partes: o <b>pano ripado, que fecha em
      2,73&nbsp;m</b>, e acima dele a <b>sanca que recebe a luz indireta</b>
      até o teto. A divisão não é estética — é o que permite entregar o
      ripado <b>inteiro, sem emenda horizontal atravessando o hall na altura
      dos olhos</b>.</div></div>

    <div><div class="k">Ferragem especificada · Hettich</div><div class="d">
      Dobradiça <b>Hettich Sensys</b>, com <b>amortecimento integrado</b> e
      regulagem nos três eixos. Corrediça <b>Hettich Quadro oculta</b>, de
      <b>extração total</b>, com <b>Silent System</b>. Em copa corporativa a
      ferragem abre e fecha o dia inteiro — é ela que decide a vida útil do
      móvel, e é ela que sustenta a garantia de dez anos.</div></div>

    <div><div class="k">Iluminação</div><div class="d">
      <b>LED COB em perfil</b>, embutido na sanca dos painéis dos dois halls,
      entregue instalado e alinhado ao pano de marcenaria.</div></div>

    <div><div class="k">Medição</div><div class="d">
      <b>Uma medição por pavimento</b>, no local, antes do corte. O próprio
      projeto adverte que os dois andares têm variação construtiva — painel de
      hall não perdoa diferença de prumo.</div></div>

    <div><div class="k">Equipe própria</div><div class="d">
      Do corte à instalação, <b>com equipe da casa</b>. A obra é em São Paulo:
      transporte, hospedagem e permanência da equipe já estão dentro do
      investimento.</div></div>
  </div>

  <div class="parU" style="margin-top:auto;">
    <div class="phU bandaU"><img class="ct" src="{img('modulo-cuba')}" alt=""></div>
    <div class="phU bandaU"><img class="ct" src="{img('bistro')}" alt=""></div>
  </div>
  {foot(3)}
</div></div>"""

# ── 4 · investimento e condições ──────────────────────────────────────────
NOME = {'Cozinha 8°':'Copa', 'Hall 8°':'Hall dos elevadores',
        'Prateleiras 8°':'Prateleiras suspensas',
        'Quadros de energia 8°':'Fechamento dos quadros de energia',
        'Cozinha 9°':'Copa', 'Hall 9°':'Hall dos elevadores',
        'Prateleiras 9°':'Prateleiras suspensas',
        'Quadros de energia 9°':'Fechamento dos quadros de energia'}

linhas, _pv = '', None
for pv in ('8° pavimento', '9° pavimento'):
    for am in u.AMBS:
        if u.PAV[am] != pv: continue
        rot = pv.replace(' pavimento', '° andar').replace('°°', '°') if pv != _pv else ''
        rot = ('8º andar' if pv.startswith('8') else '9º andar') if pv != _pv else ''
        _pv = pv
        linhas += (f'<tr><td class="a">{rot}</td><td class="i">{NOME[am]}</td>'
                   f'<td class="r">R$ {br(u.PV[am])}</td></tr>')
linhas += (f'<tr class="tot"><td class="a"></td><td class="i">Marcenaria</td>'
           f'<td class="r">R$ {br(u.TOT_MOV)}</td></tr>')

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Andar a andar.</div>
  <div class="rule"></div>

  <table class="invU">
    <thead><tr><th></th><th></th><th class="r">Investimento</th></tr></thead>
    <tbody>{linhas}</tbody>
  </table>

  <div class="mobU">
    <div><div class="k">Obra fora de sede</div>
      <div class="t">Mobilização e logística de obra</div></div>
    <div class="v">R$ {br(u.PV_MOB)}</div>
    <div class="d">Equipe própria da Valvic em São Paulo: <b>transporte e
    carreto de entrega</b>, <b>deslocamento da equipe</b>, <b>hospedagem e
    alimentação</b> durante toda a permanência e <b>jornada estendida</b> para
    cumprir o prazo nos dois pavimentos. Linha destacada de propósito — o
    preço da marcenaria acima não a embute.</div>
  </div>

  <div class="totU">
    <span class="l">Investimento total</span>
    <span class="v">R$ {br(u.TOT)}</span>
  </div>

  <div class="escU">
    <div class="l"><span class="p">40%</span><span class="q">na assinatura</span></div>
    <div class="l"><span class="p">30%</span><span class="q">no início das montagens</span></div>
    <div class="l"><span class="p">30%</span><span class="q">após a finalização</span></div>
  </div>

  <div class="cndU">
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, da assinatura, da entrada e da medição final.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Validade</div><div class="d">
      <b>{VALID}</b> a partir desta data.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragem <b>Hettich</b>.</div></div>
  </div>

  <div class="notaU"><b>Não inclusos:</b> pedras, cubas, torneiras,
  eletrodomésticos, vidros e esquadrias, as estações de trabalho do contact
  center, piso e luminárias dos halls, comunicação visual, gesso, pintura,
  revestimentos, elétrica e hidráulica.</div>

  {foot(4)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + p3 + p4 + '</body></html>')

(P/'proposta-united-sp.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-united-sp/', f'src="file://{P}/img-united-sp/')
open('/tmp/in.html', 'w', encoding='utf-8').write(tmp)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-united-sp.pdf')],
               check=True, env=env)
print(f'proposta-united-sp.pdf · {NP} páginas')
print(f'  Marcenaria      R$ {br(u.TOT_MOV):>9}')
print(f'  Mobilização     R$ {br(u.PV_MOB):>9}')
print(f'  TOTAL           R$ {br(u.TOT):>9}')
assert abs(sum(u.PV.values()) + u.PV_MOB - u.TOT) < 1
print('  soma confere com o total')
