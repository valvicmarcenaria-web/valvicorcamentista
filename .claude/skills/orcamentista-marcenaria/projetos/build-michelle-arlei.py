# -*- coding: utf-8 -*-
"""MICHELLE E ARLEI — proposta · casa completa  [19/10/2026]

⭐ [Jonathan 19/10] "pode montar a proposta. Não estenda textos demais, mas
   use bastante imagens do projeto em 3D. Dê uma certa ênfase para o valor
   com desconto à vista. Apresente de forma sucinta a versão na linha
   premium da Hettich, mostrando a vantagem de tempo de garantia atrelado
   aos benefícios."

   → PROPOSTA CONDUZIDA POR IMAGEM: quinze renders do caderno da Inédita,
     um ambiente por página, uma linha de texto por ambiente.
   → O preço à vista é o número grande; o cheio fica ao lado, menor.
   → A página da Hettich é UMA, e o argumento é a garantia: 2 → 10 anos.

Números de `corte-michelle-arlei.py`; nada digitado à mão.
⛔ Sem metragem e sem contagem em nenhuma descrição.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ma', P/'corte-michelle-arlei.py')
ma = importlib.util.module_from_spec(spec); sys.modules['ma'] = ma
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(ma)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA, DATA = 'Michelle e Arlei', 'Residência', '19 de outubro de 2026'
ARQ = 'Inédita Arquitetura'
PRAZO, VALIDADE = '90 dias corridos', '7 dias úteis'
GAR_E, GAR_P = ma.GARANTIA['essencial'], ma.GARANTIA['premium']
TOT, VISTA = ma.TOTAL, ma.VISTA
TOT_P, VISTA_P = ma.TOTAL_PREM, ma.VISTA_PREM
DESC = ma.DESC_VISTA

def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-michelle-arlei'/n).read_bytes()).decode())
IMG = {n.stem: uri(n.name) for n in sorted((P/'img-michelle-arlei').iterdir())}

# ── os ambientes, na ordem das páginas ──────────────────────────────────
PG = [
 ('Sala e área gourmet', ['sala-02', 'sala-03'], [
   ('Sala', 'Painel de TV liso e ripado em MDF Gianduia Natural, com rack '
    'suspenso e puxador passante usinado na própria peça.'),
   ('Área gourmet', 'Armário inferior com portas ripadas e gaveta de '
    'espetos, em MDF Gianduia Natural.')]),
 ('Cozinha', ['cozinha-01', 'cozinha-02'], [
   ('Cozinha', 'Armário inferior em “U”, torre quente com básculas e nichos '
    'de embutir, armário superior, prateleira iluminada, bancada de lanche '
    'e os cachepôs de temperos em estrutura metálica preta. MDF Gianduia '
    'Natural e Itapuã.')]),
 ('Lavanderia e banhos', ['lavanderia', 'banho-social', 'casal-04'], [
   ('Lavanderia', 'Armário de básculas iluminado, armário inferior e mesa '
    'de apoio em estrutura metálica preta. MDF Itapuã e Gianduia Natural.'),
   ('Banho social', 'Armário de bancada com portas de giro e gavetas, em '
    'MDF Itapuã.'),
   ('Banho do casal', 'Armário de bancada com portas de giro e gavetas, em '
    'MDF Areia.')]),
 ('Quarto Gabriel', ['gabriel-01', 'gabriel-02'], [
   ('Quarto Gabriel', 'Painel liso e ripado com prateleira iluminada e '
    'escrivaninha, armário suspenso com abertura ao toque e cabeceira '
    'ripada iluminada. MDF Brisa e Itapuã.')]),
 ('Quarto das gêmeas', ['gemeas-01', 'gemeas-02'], [
   ('Quarto das gêmeas', 'Painel de TV com armário superior e escrivaninha '
    'de gavetas, cabeceira iluminada, armário, baú e as mesas de cabeceira. '
    'MDF Brisa e Alecrim.')]),
 ('Suíte master', ['casal-01', 'casal-02', 'casal-03'], [
   ('Suíte master', 'Cabeceira iluminada, painel de TV do piso ao forro com '
    'porta de correr embutida e detalhe ripado, e o closet aberto com banco '
    'estofado e prateleira iluminada. MDF Itapuã e Areia.')]),
]
# ⛔⛔ TRAVA DE SOMA E DE COBERTURA
_amb_pg = [a for _t, _i, bl in PG for a, _d in bl]
assert set(_amb_pg) == set(ma.AMBS), (
    f'⛔ A PROPOSTA NÃO COBRE OS MESMOS AMBIENTES DO MOTOR: '
    f'{set(_amb_pg) ^ set(ma.AMBS)}')
assert abs(sum(ma.PV_AMB[a] for a in _amb_pg) - TOT) < 0.5, '⛔ O TOTAL NÃO FECHA'
assert abs(ma.MC_ALVO - 0.40) < 1e-9, f'⛔ A MC MUDOU: {ma.MC_ALVO:.3f}'
assert ma.RT_ON is True, '⛔ O RT SAIU DO MOTOR'
assert VISTA == round(TOT*(1-DESC)/10)*10, '⛔ O À VISTA NÃO FECHA'
NP = len(PG) + 4

CSS = """
:root{
  --ink:#1E1B17; --soft:#5E574E; --mut:#9A9287; --line:#E0D8CB;
  --hair:#EFE9DF; --sand:#F6F1E8; --wood:#A8794A; --wood-lt:#D9BD96;
  --dk:#262220; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.5pt;line-height:1.55;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:15mm 17mm 14mm;height:100%;display:flex;flex-direction:column;}
.foot{margin-top:auto;padding-top:6mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:6.8pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}

/* ── capa ───────────────────────────────────────────────────────────── */
.cv{height:297mm;display:flex;flex-direction:column;}
.cv .ph{flex:1;overflow:hidden;line-height:0;background:#000;}
.cv .ph img{width:100%;height:100%;object-fit:cover;}
.cv .bt{background:var(--dk);color:#F4EFE6;padding:13mm 17mm 12mm;flex:none;}
.cv .mark{font-size:8pt;letter-spacing:.42em;text-transform:uppercase;
  color:#EFE6D6;font-weight:700;}
.cv h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:42pt;
  line-height:1;font-weight:600;letter-spacing:-.02em;margin:5mm 0 0;}
.cv .sub{font-size:10.5pt;color:#C6BDB0;margin-top:4mm;font-weight:300;}
.cv .sub b{color:#EFE7DA;font-weight:500;}

/* ── páginas de ambiente ────────────────────────────────────────────── */
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.4px solid var(--ink);padding-bottom:3mm;flex:none;}
.hd .b{font-size:7.6pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:6.8pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--wood);font-weight:700;margin-top:5mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;
  line-height:1.03;font-weight:600;letter-spacing:-.02em;margin-top:1.5mm;flex:none;}
.gal{margin:5mm -17mm 0;line-height:0;min-height:0;}
.gal img{width:100%;display:block;object-fit:cover;}
.gal.col{flex:1;display:flex;flex-direction:column;gap:2mm;}
.gal.col img{flex:1;min-height:0;}
.gal.four{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:2mm;}
.gal.four img{height:100%;min-height:0;}
.gal.fix{flex:none;}
.gal.fix img{height:62mm;}
.gal.two-up{display:grid;grid-template-columns:1fr 1fr;gap:2mm;}
.gal.two-up img{height:48mm;}
.it{display:grid;grid-template-columns:1fr 32mm;gap:6mm;align-items:baseline;
  padding:3.6mm 0;border-top:1px solid var(--line);flex:none;}
.it:first-of-type{border-top:1.4px solid var(--ink);margin-top:6mm;}
.it .t{font-size:11.5pt;font-weight:600;letter-spacing:-.01em;}
.it .d{color:var(--soft);font-size:8.4pt;line-height:1.45;margin-top:1mm;}
.it .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:700;text-align:right;line-height:1;font-variant-numeric:tabular-nums;}

/* ── valores ────────────────────────────────────────────────────────── */
.rows{margin-top:6mm;flex:none;}
.row{display:flex;justify-content:space-between;align-items:baseline;
  padding:2.4mm 0;border-top:1px solid var(--line);font-size:10pt;}
.row:first-child{border-top:1.4px solid var(--ink);}
.row .v{font-variant-numeric:tabular-nums;font-weight:600;}
.vista{margin-top:7mm;background:var(--dk);color:#F4EFE6;border-radius:3px;
  padding:9mm 9mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.vista .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--wood-lt);font-weight:700;}
.vista .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:44pt;
  font-weight:700;color:#fff;line-height:.9;letter-spacing:-.03em;
  margin-top:3mm;font-variant-numeric:tabular-nums;}
.vista .s{font-size:9pt;color:#C2BAAD;margin-top:3mm;}
.vista .rt{text-align:right;flex:none;}
.vista .rt .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:#8E867A;font-weight:700;}
.vista .rt .v{font-size:15pt;color:#B6AEA1;margin-top:1.5mm;
  font-variant-numeric:tabular-nums;}
.pay{margin-top:6mm;flex:none;}
.pay .r{display:flex;justify-content:space-between;align-items:baseline;gap:6mm;
  padding:2.6mm 0;border-top:1px solid var(--line);font-size:9.2pt;color:var(--soft);}
.pay .r:first-child{border-top:1.4px solid var(--ink);}
.pay .r b{color:var(--ink);font-weight:600;}
.pay .r .x{flex:none;font-size:8.6pt;letter-spacing:.06em;color:var(--wood);
  font-weight:700;}
.pay .r.on{color:var(--ink);}
.pay .r.on .x{font-size:10pt;}

/* ── premium ────────────────────────────────────────────────────────── */
.vs{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:6mm;flex:none;}
.vs .c{border:1px solid var(--line);border-radius:3px;padding:7mm 7mm 6mm;}
.vs .c.on{background:var(--dk);border-color:var(--dk);color:#F4EFE6;}
.vs .k{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.vs .c.on .k{color:var(--wood-lt);}
.vs .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;
  font-weight:600;margin-top:2mm;line-height:1;}
.vs .g{font-family:'Cormorant Garamond',Georgia,serif;font-size:34pt;
  font-weight:700;line-height:1;margin-top:5mm;letter-spacing:-.02em;}
.vs .gl{font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;margin-top:1.5mm;}
.vs .c.on .gl{color:#9A9287;}
.vs .p{margin-top:6mm;padding-top:4mm;border-top:1px solid var(--line);
  font-size:9pt;color:var(--soft);}
.vs .c.on .p{border-top:1px solid rgba(255,255,255,.2);color:#BDB5A8;}
.vs .p b{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
  font-weight:700;color:var(--ink);display:block;margin-top:1mm;
  font-variant-numeric:tabular-nums;}
.vs .c.on .p b{color:#fff;}
.ben{margin-top:6mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm 7mm;
  flex:none;}
.ben .k{font-size:6.8pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.ben .d{color:var(--soft);font-size:8.6pt;line-height:1.45;margin-top:1mm;}
.ben .d b{color:var(--ink);font-weight:600;}

/* ── condições ──────────────────────────────────────────────────────── */
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:6mm;
  padding-top:4mm;border-top:1.4px solid var(--ink);flex:none;}
.four .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.four .v{font-size:11pt;font-weight:600;margin-top:1.2mm;}
.four .s{color:var(--soft);font-size:7.6pt;margin-top:.8mm;line-height:1.35;}
.notes{margin-top:6mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;
  flex:none;}
.notes .bx{background:var(--sand);border-radius:3px;padding:5.5mm 6mm;}
.notes .bx.w{background:#fff;border:1px solid var(--line);}
.notes .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.notes .d{color:var(--soft);font-size:8pt;line-height:1.45;margin-top:2mm;}
.notes .d b{color:var(--ink);font-weight:600;}
"""

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · {OBRA}</span><span>{n} / {NP}</span></div>')

def head():
    return (f'<div class="hd"><div class="b">Valvic Marcenaria</div>'
            f'<div class="m">{CLIENTE} · {DATA}</div></div>')

paginas = [f"""<div class="page"><div class="cv">
  <div class="ph"><img src="{IMG['sala-01']}" alt=""></div>
  <div class="bt">
    <div class="mark">Valvic Marcenaria</div>
    <h1>A casa<br>inteira.</h1>
    <div class="sub"><b>{CLIENTE}</b> · {OBRA}<br>Projeto <b>{ARQ}</b></div>
  </div>
</div></div>"""]

for n, (titulo, imgs, blocos) in enumerate(PG, start=2):
    cls = 'four' if len(imgs) == 4 else 'col'
    gal = ''.join(f'<img src="{IMG[i]}" alt="">' for i in imgs)
    itens = ''.join(
        f'<div class="it"><div><div class="t">{t}</div>'
        f'<div class="d">{d}</div></div>'
        f'<div class="v">{br(ma.PV_AMB[t])}</div></div>' for t, d in blocos)
    paginas.append(f"""<div class="page"><div class="pad">
      {head()}
      <div class="eye">Ambiente</div>
      <div class="h1 serif">{titulo}</div>
      <div class="gal {cls}">{gal}</div>
      {itens}
      {foot(n)}
    </div></div>""")

# ── página de valores · o à vista é o número grande ─────────────────────
rows = ''.join(f'<div class="row"><span>{a}</span>'
               f'<span class="v">{br(ma.PV_AMB[a])}</span></div>'
               for a in ma.AMBS)
NV = len(PG) + 2
paginas.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento</div>
  <div class="h1 serif">Ambiente por ambiente.</div>
  <div class="rows">{rows}
    <div class="row"><b>Total</b><span class="v">R$ {br(TOT)}</span></div>
  </div>
  <div class="vista">
    <div><div class="lab">À vista · {DESC:.0%} de desconto</div>
      <div class="big">R$ {br(VISTA)}</div>
      <div class="s">Entrada e saldo por transferência, sem cartão —
      devolvemos a taxa que deixamos de pagar.</div></div>
    <div class="rt"><div class="k">Valor cheio</div>
      <div class="v">R$ {br(TOT)}</div></div>
  </div>
  <div class="pay">
    <div class="r on"><div>Entrada <b>70%</b> + saldo por transferência</div>
      <div class="x">−{DESC:.0%} · R$ {br(VISTA)}</div></div>
    <div class="r"><div>Entrada <b>70%</b> + saldo em até seis vezes no cartão</div>
      <div class="x">−5%</div></div>
    <div class="r"><div>Entrada <b>50%</b> + saldo em até oito vezes no cartão</div>
      <div class="x">−3%</div></div>
    <div class="r"><div>Entrada <b>30%</b> + saldo em até dez vezes no cartão</div>
      <div class="x">R$ {br(TOT)}</div></div>
  </div>
  {foot(NV)}
</div></div>""")

# ── página da linha premium · sucinta, o argumento é a garantia ─────────
paginas.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Uma escolha</div>
  <div class="h1 serif">Dois anos, ou dez.</div>

  <div class="vs">
    <div class="c"><div class="k">Essencial</div>
      <div class="n serif">Corrediça telescópica</div>
      <div class="g serif">{GAR_E}</div>
      <div class="gl">de garantia</div>
      <div class="p">À vista<b>R$ {br(VISTA)}</b></div></div>
    <div class="c on"><div class="k">Premium · Hettich</div>
      <div class="n serif">Corrediça oculta,<br>alemã</div>
      <div class="g serif">{GAR_P}</div>
      <div class="gl">de garantia</div>
      <div class="p">À vista<b>R$ {br(VISTA_P)}</b></div></div>
  </div>

  <div class="ben">
    <div><div class="k">A gaveta</div>
      <div class="d">O trilho <b>some por baixo</b>: a gaveta abre inteira,
      fecha amortecida e não mostra ferragem na lateral.</div></div>
    <div><div class="k">A porta</div>
      <div class="d">Dobradiça alemã com amortecedor e <b>regulagem nos três
      sentidos</b> — é o que decide se a porta ainda fecha no prumo no
      décimo ano.</div></div>
    <div><div class="k">As básculas</div>
      <div class="d">Articulador premium: a porta sobe sozinha, <b>para onde
      você soltar</b> e desce sem bater.</div></div>
    <div><div class="k">A luz</div>
      <div class="d">Fita e perfil de linha profissional, com <b>difusor sem
      pontos</b> e cor estável ao longo do tempo.</div></div>
  </div>

  <div class="gal fix two-up" style="margin-top:6mm;">
    <img src="{IMG['casal-03']}" alt=""><img src="{IMG['cozinha-01']}" alt="">
  </div>

  <div class="vista" style="padding:7mm 9mm;">
    <div><div class="lab">A diferença</div>
      <div class="big" style="font-size:38pt;">R$ {br(TOT_P-TOT)}</div>
      <div class="s">Sobre o valor cheio — <b>{(TOT_P/TOT-1):.0%} a mais</b>
      pela ferragem que fica.</div></div>
    <div class="rt"><div class="k">Garantia</div>
      <div class="v" style="font-size:19pt;color:#fff;">{GAR_E} → {GAR_P}</div></div>
  </div>
  {foot(NV+1)}
</div></div>""")

# ── condições ───────────────────────────────────────────────────────────
paginas.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Condições</div>
  <div class="h1 serif">Como fechamos.</div>

  <div class="gal col" style="margin-top:5mm;">
    <img src="{IMG['sala-01']}" alt=""><img src="{IMG['gemeas-01']}" alt="">
  </div>

  <div class="four">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div>
      <div class="s">Do aceite e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">{GAR_E} · {GAR_P}</div>
      <div class="s">Essencial e Premium.</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div>
      <div class="s">Do corte à instalação.</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div>
      <div class="s">A partir desta data.</div></div>
  </div>

  <div class="notes">
    <div class="bx"><div class="k">O que não está incluso</div>
      <div class="d">As <b>bancadas e os rodapés em granito</b>, que são
      marmoraria. Os <b>eletrodomésticos</b>, as <b>cubas, torneiras e
      louças</b>. A <b>elétrica</b> — pontos, circuitos, drivers e
      interruptores. Os <b>espelhos de parede</b>, os <b>cobogós</b>, as
      <b>esquadrias</b>, o <b>forro de gesso</b>, o <b>piso</b> e a
      <b>pintura</b>.</div></div>
    <div class="bx w"><div class="k">A confirmar antes da produção</div>
      <div class="d">O projeto pede <b>conferir todas as medidas no
      local</b> — fazemos a medição antes do corte, e é ela que fecha a
      altura dos móveis do piso ao forro. O <b>forno e o micro-ondas</b>
      precisam estar definidos para a torre da cozinha. E <b>amostra</b>
      dos cinco padrões de MDF, aprovada por vocês e pela
      arquiteta.</div></div>
  </div>
  {foot(NP)}
</div></div>""")

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + ''.join(paginas) + '</body></html>')
assert len(paginas) == NP, f'⛔ {len(paginas)} páginas, o rodapé diz {NP}'

(P/'proposta-michelle-arlei.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-michelle-arlei.pdf')],
               check=True, env=env)
print(f'proposta-michelle-arlei.pdf · {NP} páginas · '
      f'{(P/"proposta-michelle-arlei.pdf").stat().st_size//1024} kB')
for a in ma.AMBS: print(f'  {a:<22} R$ {br(ma.PV_AMB[a]):>8}')
print(f'  {"TOTAL":<22} R$ {br(TOT):>8}')
print(f'  {"À VISTA −"+f"{DESC:.0%}":<22} R$ {br(VISTA):>8}')
print(f'  {"Premium Hettich":<22} R$ {br(TOT_P):>8}  (à vista {br(VISTA_P)})')
