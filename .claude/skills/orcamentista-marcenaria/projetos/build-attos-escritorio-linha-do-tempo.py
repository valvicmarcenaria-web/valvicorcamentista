# -*- coding: utf-8 -*-
"""ATTOS · COSTA LAGUNA — LINHA DO TEMPO DO ESCRITÓRIO, EM A3 PAISAGEM  [11/11/2026]

⭐ [Jonathan, 11/11/2026] "vamos fazer o mesmo com o projeto do Attos. vamos
   salientar as necessidades já mapeadas no escopo relacionando com cada etapa."
⭐ É a linha do tempo do Orlando (`build-orlando-ivone-linha-do-tempo.py`), com as
   datas do anexo `CRONOGRAMA_ESCRITÓRIO_ATTOS.pdf`, assinado por Bruna Castro:
     definições até 12/11 · programação até 19/11 · aprovação da arquiteta de 19
     a 22 · usinagem começa 23/11 · pré-montagem 30/11 · conferência 04/12 ·
     início de montagem 07/12 · entrega 10/12.
⭐ As NECESSIDADES MAPEADAS saem do escopo de venda do Attos
   (`Valvic_Escopo_Venda_Attos.pdf`, 06/11/2026) e do cronograma do escritório
   (`build-attos-escritorio-cronograma.py`), cada uma na etapa em que tem de
   estar resolvida. Vêm impressas, com caixa de marcar; embaixo delas fica o
   espaço pautado para o que surgir.
⛔ Dobradiça Hettich NOVISYS, não Sensys [Jonathan, 10/11/2026].
⭐ [Jonathan, 11/11/2026] correções:
   · etapa 2: "medidas já foram tiradas" · "o apoio metálico é estrutural" ·
     "painel ripado não precisa dessa informação";
   · etapa 3: sai a divergência do render (resolvida na etapa 1) e a
     confirmação por escrito; entra "compra do material e pedido da
     serralheria sai logo após aprovação da arquiteta/cliente";
   · "não precisa dessa descrição Silent System";
   · saem as necessidades mapeadas das etapas 5, 6 e 7;
   · mais destaque para o NOME DO CLIENTE;
   · as FERRAGENS ganham uma caixa como a da data, grande no topo, mas sem o
     fundo de cor cheia.
⭐ O anexo marca só o INÍCIO de cada etapa (ou o fim, nas duas primeiras): na
   barra, cada etapa corre até a véspera da seguinte.
"""
import pathlib, subprocess, os, re, html, datetime as dt

P = pathlib.Path(__file__).resolve().parent
E = lambda t: html.escape(str(t))
D = dt.date

CLIENTE = 'Attos Henrique Salles'
AMBIENTE = 'Escritório'
OBRA = 'Costa Laguna · Alphaville, Nova Lima'
RESP = ('Bruna Castro', 'Arquiteta e urbanista · responsável pelo projeto')
INICIO, FIM = D(2026, 11, 11), D(2026, 12, 10)

# (etapa, quando, de, até, o que fecha a etapa, necessidades já mapeadas no escopo)
ETAPAS = [
 ('Definições informacionais', 'até 12/11', D(2026, 11, 11), D(2026, 11, 12),
  'Tudo o que o executivo precisa saber antes de ser desenhado.',
  ['Cores e padrões de MDF definidos com o cliente, antes de comprar chapa',
   'Perfil de alumínio na base do painel ripado: levar ao cliente em protótipo',
   'Divergência entre o render e o executivo resolvida — nada corta antes']),
 ('Programação', 'até 19/11', D(2026, 11, 13), D(2026, 11, 19),
  'Executivo de marcenaria e plano de corte.',
  ['Fixação da pedra alinhada com a marmoraria — a pedra é de terceiro',
   'Apoio metálico estrutural da ponta da mesa desenhado']),
 ('Aprovação da arquiteta', '19 a 22/11', D(2026, 11, 19), D(2026, 11, 22),
  'Executivo aprovado pela arquiteta.',
  ['Compra do material e pedido da serralheria logo após a aprovação da arquiteta e do cliente']),
 ('Usinagem', 'começa 23/11', D(2026, 11, 23), D(2026, 11, 29),
  'Corte, fita de borda, ripas e usinagem.',
  ['Janela própria na produção: fora da fila dos 70 dias da casa',
   'Chapa comprada nos padrões aprovados']),
 ('Pré-montagem', '30/11', D(2026, 11, 30), D(2026, 12, 3),
  'Armários montados e regulados na fábrica.',
  []),
 ('Conferência', '04/12', D(2026, 12, 4), D(2026, 12, 6),
  'Conferência contra o escopo · embalagem e carga.',
  []),
 ('Início de montagem', '07/12', D(2026, 12, 7), D(2026, 12, 9),
  'Equipe na obra.',
  []),
 ('Entrega', '10/12', D(2026, 12, 10), D(2026, 12, 10),
  'Escritório instalado e conferido.',
  ['Instalado até 10/12/2026 — prazo contratual',
   'Termo de garantia: 10 anos marcenaria e ferragem']),
]
assert ETAPAS[0][2] == INICIO and ETAPAS[-1][3] == FIM

DIAS = [INICIO + dt.timedelta(n) for n in range((FIM - INICIO).days + 1)]
SEM = 'STQQSSD'   # segunda a domingo
N = len(DIAS)
CAB = 46          # mm da coluna dos nomes no gráfico

cols = ''.join(
    f'<div class="d{" fs" if d.weekday() >= 5 else ""}"><b>{SEM[d.weekday()]}</b>'
    f'<span>{d.day:02d}/{d.month:02d}</span></div>' for d in DIAS)
fundo = ''.join(f'<div class="{"fs" if d.weekday() >= 5 else ""}"></div>' for d in DIAS)

def barra(n, a, b, ultimo):
    i = (a - INICIO).days
    w = (b - a).days + 1
    cls = 'bar fim' if ultimo else ('bar ms' if w == 1 else 'bar')
    return (f'<div class="ln"><div class="nm"><span class="n">{n:02d}</span>{E(ETAPAS[n - 1][0])}</div>'
            f'<div class="tr"><div class="bg">{fundo}</div>'
            f'<div class="{cls}" style="left:calc({i} * 100% / {N});width:calc({w} * 100% / {N})">'
            f'<span>{E(ETAPAS[n - 1][1])}</span></div></div></div>')

gantt = ''.join(barra(n, a, b, n == len(ETAPAS)) for n, (_k, _q, a, b, _d, _m) in enumerate(ETAPAS, 1))

LINHAS, LINHAS_SEM = 6, 15
FERRAGENS = [('Corrediças', 'Hettich'), ('Dobradiças', 'Hettich Novisys')]
def mapeadas(m):
    if not m:
        return ''
    li = ''.join(f'<li><span class="bx"></span>{E(x)}</li>' for x in m)
    return f'<div class="nk">Necessidades mapeadas no escopo</div><ul class="mp">{li}</ul>'
cards = ''.join(
    f'''<div class="cd{" fim" if n == len(ETAPAS) else ""}">
     <div class="ch"><span class="n">{n:02d}</span><span class="box"></span></div>
     <div class="t">{E(k)}</div><div class="q">{E(q)}</div>
     <div class="o">{E(o)}</div>
     <div class="rz"><span>Realizado em</span> ___/___</div>
     {mapeadas(m)}
     <div class="nk">{"Outras necessidades e pendências" if m else "Necessidades e pendências"}</div>
     <div class="pt">{"<div></div>" * (LINHAS if m else LINHAS_SEM)}</div></div>'''
    for n, (k, q, _a, _b, o, m) in enumerate(ETAPAS, 1))

CSS = f"""
@page{{size:A3 landscape;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{--navy:#14233B;--gold:#B8913F;--gold-lt:#E2C98E;--ink:#1B1F27;--soft:#4A515E;--mut:#8A909B;
      --line:#DADDE2;--cream:#F6EEDB;--paper:#FFFDF8;--fs:#EEF0F3}}
body{{font-family:'DM Sans',system-ui,sans-serif;color:var(--ink);font-size:8.6pt;line-height:1.4}}
.page{{width:420mm;height:297mm;padding:12mm 14mm 10mm;display:flex;flex-direction:column;overflow:hidden}}
.hd{{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:3mm;
    border-bottom:2.4px solid var(--navy)}}
.lg{{font-family:'Cormorant Garamond',Georgia,serif;font-size:28pt;font-weight:700;line-height:.9}}
.lg small{{display:block;font-family:'DM Sans',sans-serif;font-size:6.8pt;letter-spacing:.46em;
    color:var(--gold);font-weight:700;margin-top:2mm}}
.tt{{text-align:center}}
.tt .e{{font-size:7.6pt;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);font-weight:700}}
.tt .t{{font-family:'Cormorant Garamond',Georgia,serif;font-size:36pt;font-weight:700;line-height:1;
       margin-top:1mm;color:var(--navy)}}
.tt .s{{font-size:8pt;letter-spacing:.24em;text-transform:uppercase;color:var(--mut);margin-top:1.4mm}}
.tops{{display:flex;gap:3mm;align-items:stretch}}
.fer{{display:flex;border:1.8px solid var(--navy);border-radius:3px;background:#fff}}
.fer>div{{padding:2.6mm 5mm;text-align:left}}
.fer>div+div{{border-left:1px solid var(--line)}}
.fer .k{{font-size:6.6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700}}
.fer .v{{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;font-weight:700;line-height:1;
        color:var(--navy);margin-top:1mm;white-space:nowrap}}
.ent{{background:var(--navy);color:#fff;border-radius:3px;padding:2.6mm 5mm;text-align:right}}
.ent .k{{font-size:6.6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt);font-weight:600}}
.ent .d{{font-family:'Cormorant Garamond',Georgia,serif;font-size:26pt;font-weight:700;line-height:1}}
.sec{{margin-top:4mm;background:var(--navy);color:#fff;padding:2mm 3.4mm;font-size:7.6pt;
     letter-spacing:.24em;text-transform:uppercase;font-weight:600;display:flex;justify-content:space-between}}
.sec b{{color:var(--gold-lt);font-weight:600}}
.sec i{{font-style:normal;color:#C9CFD8;letter-spacing:.12em}}
.ax,.ln{{display:grid;grid-template-columns:{CAB}mm 1fr}}
.ax .d{{display:flex;flex-direction:column;align-items:center;padding:1.4mm 0;border-left:1px solid var(--line);
       font-size:6.8pt;color:var(--soft)}}
.ax .d b{{font-size:6.2pt;color:var(--mut);letter-spacing:.1em}}
.ax .d.fs{{background:var(--fs)}}
.ax .dias{{display:grid;grid-template-columns:repeat({N},1fr);border-bottom:1.4px solid var(--navy)}}
.ax .lb{{font-size:6.4pt;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);align-self:end;
        padding:0 0 1.6mm 1mm}}
.ln{{border-bottom:1px solid var(--line);min-height:8.2mm}}
.nm{{display:flex;align-items:center;gap:2.4mm;font-weight:700;font-size:8.2pt;padding-left:1mm}}
.nm .n,.cd .n{{font-family:'DM Mono',ui-monospace,monospace;color:var(--gold);font-weight:500}}
.tr{{position:relative}}
.bg{{position:absolute;inset:0;display:grid;grid-template-columns:repeat({N},1fr)}}
.bg div{{border-left:1px solid var(--line)}}
.bg .fs{{background:var(--fs)}}
.bar{{position:absolute;top:1.6mm;bottom:1.6mm;background:var(--navy);border-radius:2px;display:flex;
     align-items:center;padding:0 2mm;overflow:visible}}
.bar span{{color:#fff;font-size:7pt;font-weight:600;white-space:nowrap}}
.bar.ms{{background:var(--gold)}}
.bar.ms span,.bar.fim span{{position:absolute;left:calc(100% + 1.6mm);color:var(--ink)}}
.bar.fim{{background:var(--gold);box-shadow:0 0 0 1.6px var(--navy)}}
.bar.fim span{{left:auto;right:calc(100% + 1.6mm);font-weight:700}}
.cards{{display:grid;grid-template-columns:repeat({len(ETAPAS)},1fr);gap:3mm;margin-top:3mm;flex:1;min-height:0}}
.cd{{border:1px solid var(--line);border-top:3px solid var(--navy);border-radius:2px;padding:2.6mm 3mm;
    display:flex;flex-direction:column;min-height:0;background:#fff}}
.cd.fim{{border-top-color:var(--gold);background:var(--paper)}}
.ch{{display:flex;justify-content:space-between;align-items:center}}
.ch .n{{font-size:12pt}}
.box{{width:4.2mm;height:4.2mm;border:1.4px solid var(--ink);border-radius:.8mm;display:inline-block}}
.cd .t{{font-weight:700;font-size:9.4pt;margin-top:1.2mm;line-height:1.2;min-height:2.4em}}
.cd .q{{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;font-weight:700;color:var(--navy);
       line-height:1.1;margin-top:.8mm}}
.cd.fim .q{{color:var(--gold)}}
.cd .o{{font-size:7.4pt;color:var(--soft);margin-top:1.4mm;min-height:7mm}}
.mp{{list-style:none;margin-top:1.2mm;padding:1.6mm 2mm;background:var(--cream);border-radius:2px;
    min-height:46mm}}
.mp li{{display:grid;grid-template-columns:3.4mm 1fr;gap:1.4mm;font-size:7.2pt;line-height:1.3;
       color:var(--ink);padding:.9mm 0;border-bottom:1px solid #E9DFC6}}
.mp li:last-child{{border-bottom:none}}
.mp .bx{{width:3mm;height:3mm;border:1.1px solid var(--ink);border-radius:.6mm;margin-top:.3mm}}
.cd .rz{{font-size:7.4pt;color:var(--mut);margin-top:1.6mm;padding-top:1.4mm;border-top:1px solid var(--line)}}
.cd .rz span{{letter-spacing:.14em;text-transform:uppercase;font-size:6pt;font-weight:600}}
.cd .nk{{font-size:6pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:2.4mm}}
.pt{{flex:1;display:flex;flex-direction:column;justify-content:space-between;margin-top:1mm}}
.pt div{{border-bottom:1px dotted #B9BEC6;flex:1}}
.rod{{display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:10mm;margin-top:5mm;align-items:end}}
.rod .lgd{{font-size:7pt;color:var(--soft);display:flex;gap:5mm;align-items:center}}
.rod .lgd i{{display:inline-block;width:7mm;height:3mm;border-radius:1px;margin-right:1.4mm;vertical-align:middle}}
.rod .sg{{border-top:1px solid var(--ink);padding-top:1.4mm;text-align:center}}
.rod .sg b{{display:block;font-size:8.2pt}}
.rod .sg span{{font-size:7pt;color:var(--soft)}}
.ft{{display:flex;justify-content:space-between;border-top:1px solid var(--line);margin-top:3mm;
    padding-top:2mm;font-size:6.4pt;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}}
"""

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Linha do tempo · {E(CLIENTE)}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="page">
 <div class="hd">
  <div class="lg">valvic<small>MARCENARIA</small></div>
  <div class="tt"><div class="e">Linha do tempo da obra · {E(AMBIENTE)}</div>
   <div class="t">{E(CLIENTE)}</div><div class="s">{E(OBRA)}</div></div>
  <div class="tops">
   <div class="fer">{''.join(f'<div><div class="k">{E(k)}</div><div class="v">{E(v)}</div></div>' for k, v in FERRAGENS)}</div>
   <div class="ent"><div class="k">Entrega no cliente · finalizada</div>
    <div class="d">{FIM.strftime('%d/%m/%Y')}</div></div></div>
 </div>

 <div class="sec"><span>1 · <b>O caminho até a entrega</b>, dia a dia</span>
  <i>De {INICIO.strftime('%d/%m')} a {FIM.strftime('%d/%m/%Y')} · fins de semana sombreados</i></div>
 <div class="ax"><div class="lb">Etapa</div><div class="dias">{cols}</div></div>
 {gantt}

 <div class="sec"><span>2 · <b>Acompanhamento de cada etapa</b></span>
  <i>Marque a caixa ao concluir · anote à mão o que a etapa precisa</i></div>
 <div class="cards">{cards}</div>

 <div class="rod">
  <div class="lgd"><span><i style="background:var(--navy)"></i>Etapa</span>
   <span><i style="background:var(--gold)"></i>Marco de um dia</span>
   <span><i style="background:var(--gold);box-shadow:0 0 0 1.4px var(--navy)"></i>Entrega</span></div>
  <div class="sg"><b>{E(RESP[0])}</b><span>{E(RESP[1])}</span></div>
  <div class="sg"><b>Produção</b><span>Visto em ___/___/______</span></div>
  <div class="sg"><b>Gestão</b><span>Visto em ___/___/______</span></div>
 </div>
 <div class="ft"><span>Valvic Marcenaria · Vargas Decor LTDA</span>
  <span>Linha do tempo · {E(AMBIENTE)} · {E(CLIENTE)}</span></div>
</div>
</body></html>"""

# ── as travas ───────────────────────────────────────────────────────────
_t = re.sub(r'<[^>]+>', ' ', HTML.split('<body>')[1])
assert 'R$' not in _t and not [c for c in '⭐⛔⚠' if c in _t]
for _k, _q, _a, _b, _o, _m in ETAPAS:
    assert _a <= _b and _k in _t and _q in _t
for _a, _b in zip(ETAPAS, ETAPAS[1:]):
    assert _b[2] >= _a[2], '⛔ etapa fora de ordem'
assert '10/12/2026' in _t and 'Bruna Castro' in _t and 'Novisys' in _t and 'Sensys' not in _t
for _fora in ('Silent', 'Medição técnica', 'mesma cadência', 'divergência do render', 'por escrito'):
    assert _fora not in _t, f'⛔ saiu da folha [Jonathan, 11/11/2026]: {_fora}'
assert not any(_m for *_r, _m in ETAPAS[4:7]), '⛔ as etapas 5, 6 e 7 ficam sem necessidade mapeada'
for _c in ('Orlando', 'Ivone', 'Haverson', 'Ana Carolina', 'Alexandre', 'Gisele'):
    assert _c not in _t, f'⛔ vestígio de outro cliente: {_c}'

R = P / 'attos-costa-laguna'
OUT = R / 'linha-do-tempo-escritorio-attos.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'Valvic_Linha_do_Tempo_Escritorio_Attos_A3.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF), 'A3', 'paisagem'], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
info = subprocess.run(['pdfinfo', str(PDF)], capture_output=True, text=True).stdout
npg = int(re.search(r'Pages:\s+(\d+)', info).group(1))
assert npg == 1, f'⛔ a linha do tempo tem de caber em UM A3: saiu com {npg}'
print(f'{PDF.name} · {re.search(r"Page size:\s+(.*)", info).group(1)} · {len(ETAPAS)} etapas · '
      f'{N} dias, de {INICIO:%d/%m} a {FIM:%d/%m/%Y}')
