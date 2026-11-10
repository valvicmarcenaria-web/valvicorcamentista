# -*- coding: utf-8 -*-
"""ORLANDO E IVONE — ESCOPO DE VENDA, EM UMA PÁGINA  [10/11/2026]

⭐ [Jonathan, 10/11/2026] "preciso que vc veja como feito o escopo de venda do
   projeto do Attos e faça o escopo do orlando". O modelo é o
   `Valvic_Escopo_Venda_Attos.pdf` do Drive (06/11/2026): cabeçalho com cliente,
   obra, projeto e escopo · os itens com a coluna OK · ferragens e estrutura ·
   o que falta definir · assinaturas de Comercial, Gestão e Produção.
⭐ [Jonathan, 10/11/2026] primeira rodada de alterações:
   · "informe apenas as ferragens que serão utilizadas · corrediças Hettich -
     dobradiças Blum";
   · "definir cores com a arquiteta";
   · "prazo de entrega no cliente (finalizado) 04/12";
   · "criar cronograma de etapas (definições informacionais, programação,
     usinagem, pré-montagem, conferência, início de montagem) · preciso de um
     lugar para preencher a previsão de data para entrega de cada etapa".
⭐ [Jonathan, 10/11/2026] segunda rodada:
   · saem o "como usar" e o bloco de ATENÇÃO da obra;
   · "de mais destaque ao prazo de entrega";
   · sai da estrutura a lista do aparente e o "manter em 18";
   · "ponto de atenção perfil de alumínio extra fino (atenção ao prazo de pedido
     para o fornecedor devido ao prazo)";
   · sai o "fora do escopo";
   · no bloco a definir saem a revisão do projeto, o apoio da bancada, a cuba e
     o sifão, o perfil dos espelhos (já dito acima) e as medidas: "medição já
     foi feita";
   · "reformule para ficar tudo em uma página".
⭐ Documento INTERNO, para a gestão e a produção: leva contagem de peça e
   especificação técnica, e não leva preço.
⭐ A fonte é o fechamento de 21/10/2026, na linha PREMIUM
   (`proposta-orlando-ivone-fechamento.pdf`), e o dossiê `2026-orlando-ivone.md`.
"""
import pathlib, subprocess, os, re, html

P = pathlib.Path(__file__).resolve().parent
E = lambda t: html.escape(str(t))

CLIENTE = 'Orlando e Ivone'
OBRA = 'Apartamento · Rua Passa Tempo, Belo Horizonte'
PROJETO = '[31] Apto Orlando e Ivone · Ana Maria Castro · Rev. 00'
LOCAL = 'Orlando e Ivone · Rua Passa Tempo, Belo Horizonte'
RODAPE = 'ESCOPO DE VENDA · BANHO SUÍTE MASTER · ORLANDO E IVONE'
ENTREGA = '04/12/2026'

CARDS = [
 ('Medição técnica', 'Realizada'),
 ('Linha contratada', 'Premium · MDF Ultra resistente à umidade · corrediças Hettich · dobradiças Blum'),
 ('Garantia', '10 anos estrutura e ferragens · 2 anos instalação e regulagem · arandelas e driver '
  'pelo fabricante'),
]
ITENS = [
 ('BANHO SUÍTE', 'Armário inferior sob a bancada',
  'Duas portas de giro sob a cuba e quatro gavetas sobre corrediça oculta Hettich com amortecimento '
  '· frente e caixaria nas cores a definir com a arquiteta · puxador Zen Phenix 20 cm cromado · '
  'assenta no sóculo de alvenaria, sob a pedra, sem sustentá-la'),
 ('BANHO SUÍTE', 'Armário superior · espelheira',
  'Quatro folhas de espelho prata em perfil de alumínio extra fino, de giro, em dois vãos · puxador '
  'de trespasse de 1 cm, sem puxador aplicado · três peças fixas para as arandelas, com berço e '
  'passagem do driver · interior com prateleiras · cores a definir com a arquiteta'),
]
# ⭐ o cronograma: a previsão de cada etapa é preenchida à mão pela gestão
ETAPAS = [
 ('Definições informacionais', 'Cores, arandelas e driver, pedido do perfil extra fino'),
 ('Programação', 'Executivo de marcenaria aprovado e plano de corte'),
 ('Usinagem', 'Corte, fita de borda, furação e usinagem'),
 ('Pré-montagem', 'Módulos montados e regulados na fábrica, espelho no perfil'),
 ('Conferência', 'Conferência contra este escopo · embalagem e carga'),
 ('Início de montagem', 'Equipe na obra, com sóculo, pedra e ponto elétrico prontos'),
]
FERRAGENS = [('Corrediças', 'Hettich'), ('Dobradiças', 'Blum')]   # ⭐ apenas o que será usado
ESTRUTURA = ('MDF Ultra, resistente à umidade · <b>cores a definir com a arquiteta</b> · todo o '
             'aparente <b>em 18 mm</b> · espelho prata em perfil de alumínio extra fino, fornecido e '
             'alinhado por nós')
PERFIL = ('As folhas de espelho levam <b>perfil de alumínio extra fino</b>. <b>Atenção ao prazo de '
          'pedido ao fornecedor:</b> o pedido sai na etapa de definições, para o perfil chegar a tempo '
          f'da entrega em {ENTREGA}.')
DEFINIR = [
 ('Cores e padrões de MDF', '<b>Definir as cores com a arquiteta</b> antes de comprar chapa: o '
  'aparente dos dois móveis, as peças fixas da espelheira e a caixaria.'),
 ('Arandelas e driver', 'Modelo e medida das arandelas e do driver, para o berço e a passagem na '
  'peça fixa. <b>Ponto elétrico posicionado pela obra</b> — sem ele, não há luz na entrega.'),
]

CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{--navy:#14233B;--gold:#B8913F;--gold-lt:#E2C98E;--ink:#1B1F27;--soft:#4A515E;--mut:#8A909B;
      --line:#DADDE2;--cream:#F6EEDB;--paper:#FFFDF8}
body{font-family:'DM Sans',system-ui,sans-serif;color:var(--ink);font-size:7.6pt;line-height:1.45}
.page{width:210mm;height:297mm;padding:9mm 12mm 7mm;display:flex;flex-direction:column;overflow:hidden}
.hd{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:2.6mm;
    border-bottom:2px solid var(--navy)}
.hd .lg{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;font-weight:700;line-height:.9}
.hd .lg small{display:block;font-family:'DM Sans',sans-serif;font-size:5.6pt;letter-spacing:.42em;
    color:var(--gold);font-weight:700;margin-top:1.6mm}
.hd .r{text-align:right}
.hd .r .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;font-weight:700;line-height:1}
.hd .r .s{font-size:6.4pt;color:var(--mut);margin-top:1.2mm}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:2.4mm;margin-top:3.2mm}
.cards>div{border:1px solid var(--line);border-radius:2px;padding:2mm 2.6mm}
.k{font-size:5.4pt;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);font-weight:600}
.cards .v{font-size:7.6pt;font-weight:700;margin-top:.8mm;line-height:1.3}
.prazo{margin-top:2.8mm;background:var(--navy);color:#fff;border-radius:3px;padding:2.8mm 5mm;
       display:flex;align-items:center;gap:7mm}
.prazo .k{color:var(--gold-lt);font-size:6.4pt;letter-spacing:.24em;white-space:nowrap}
.prazo .d{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;font-weight:700;line-height:1;
          color:#fff;white-space:nowrap}
.prazo .t{font-size:7.6pt;color:#D5D9E0;line-height:1.5;border-left:1px solid rgba(255,255,255,.25);
          padding-left:6mm}
.prazo .t b{color:#fff}
.info{display:grid;grid-template-columns:.6fr 1.2fr 1.2fr;gap:2.4mm;margin-top:2.6mm}
.info>div{border:1px solid var(--line);border-left:3px solid var(--navy);padding:1.8mm 3mm}
.info .v{font-size:7.4pt;margin-top:.7mm}
.sec{margin-top:2.8mm;background:var(--navy);color:#fff;padding:1.8mm 3mm;font-size:6.6pt;
     letter-spacing:.24em;text-transform:uppercase;font-weight:600}
.sec b{color:var(--gold-lt);font-weight:600}
table{width:100%;border-collapse:collapse}
th{background:var(--navy);color:var(--gold-lt);font-size:5.4pt;letter-spacing:.2em;text-transform:uppercase;
   text-align:left;padding:1.4mm 2.4mm;font-weight:600}
td{padding:1.25mm 2.4mm;border-bottom:1px solid var(--line);vertical-align:top;font-size:7.2pt}
tr:nth-child(even) td{background:#F7F8FA}
td.amb{font-family:'DM Mono',ui-monospace,monospace;font-size:6.4pt;letter-spacing:.06em;white-space:nowrap}
td.it{font-weight:700;width:44mm}
td.sp{color:var(--soft)}
td.ok,th.ok{width:9mm;text-align:center}
td.n{width:7mm;font-family:'DM Mono',ui-monospace,monospace;color:var(--gold)}
td.dt,th.dt{width:26mm;white-space:nowrap}
td.dt{color:var(--mut)}
td.def{width:30mm;color:var(--mut);white-space:nowrap}
tr.fim td{background:var(--cream)!important;font-weight:700;border-bottom:none}
tr.fim td.dd{color:var(--ink);font-size:8.4pt}
tr.fim td.dt:not(.dd){font-weight:400}
.cr{table-layout:fixed}
.cr td.dt{font-size:6.6pt}
.box{width:3.2mm;height:3.2mm;border:1.2px solid var(--ink);border-radius:.6mm;display:inline-block}
.fer{display:flex;gap:2.4mm;margin-top:2.2mm}
.fer>div{flex:1;border:1px solid var(--line);border-left:3px solid var(--navy);padding:2mm 3.4mm;
         display:flex;align-items:baseline;gap:3mm}
.fer .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;font-weight:700;line-height:1}
.bl{margin-top:2.2mm;border:1px solid var(--line);border-left:3px solid var(--navy);padding:2.2mm 3.4mm;
    font-size:7.2pt;color:var(--soft)}
.bl b{color:var(--ink)}
.bl .h{color:var(--ink);font-weight:700}
.at{margin-top:2.2mm;border:1.5px solid var(--gold);border-radius:3px;background:var(--paper);
    padding:2.2mm 3.4mm;font-size:7.2pt;color:var(--soft);display:grid;grid-template-columns:auto 1fr;
    gap:4mm;align-items:center}
.at .e{font-size:5.6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700;
       white-space:nowrap}
.at b{color:var(--ink)}
.sig{display:grid;grid-template-columns:repeat(3,1fr);gap:9mm;margin-top:auto;padding-top:4mm}
.sig>div{border-top:1px solid var(--ink);padding-top:1.4mm;text-align:center}
.sig .h{font-weight:700;font-size:7.4pt}
.sig .d{font-size:6.6pt;color:var(--soft)}
.ft{display:flex;justify-content:space-between;border-top:1px solid var(--line);margin-top:2.6mm;
    padding-top:2mm;font-size:5.6pt;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}
"""

BOX = '<span class="box"></span>'
DATA_V = '___/___/______'
cards = ''.join(f'<div><div class="k">{E(k)}</div><div class="v">{E(v)}</div></div>' for k, v in CARDS)
itens = ''.join(f'<tr><td class="amb">{E(a)}</td><td class="it">{E(i)}</td><td class="sp">{E(s)}</td>'
                f'<td class="ok">{BOX}</td></tr>' for a, i, s in ITENS)
crono = ''.join(f'<tr><td class="n">{n:02d}</td><td class="it">{E(k)}</td><td class="sp">{E(d)}</td>'
                f'<td class="dt">{DATA_V}</td><td class="dt">{DATA_V}</td><td class="ok">{BOX}</td></tr>'
                for n, (k, d) in enumerate(ETAPAS, 1))
crono += (f'<tr class="fim"><td class="n">{len(ETAPAS) + 1:02d}</td><td class="it">Entrega no cliente</td>'
          f'<td class="sp">Obra finalizada e conferida · termo de garantia assinado</td>'
          f'<td class="dt dd">{ENTREGA}</td><td class="dt">{DATA_V}</td><td class="ok">{BOX}</td></tr>')
fer = ''.join(f'<div><div class="k">{E(k)}</div><div class="v">{E(v)}</div></div>' for k, v in FERRAGENS)
defs = ''.join(f'<tr><td class="ok">{BOX}</td><td class="it">{E(k)}</td><td class="sp">{d}</td>'
               f'<td class="def">……………………</td></tr>' for k, d in DEFINIR)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Escopo de Venda · {E(CLIENTE)}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="page">
 <div class="hd"><div class="lg">valvic<small>MARCENARIA</small></div>
  <div class="r"><div class="t">Escopo de Venda</div><div class="s">{E(LOCAL)} · folha 1 de 1</div></div></div>

 <div class="cards">
  <div><div class="k">Cliente</div><div class="v">{E(CLIENTE)}</div></div>
  <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
  <div><div class="k">Projeto</div><div class="v">{E(PROJETO)}</div></div>
  <div><div class="k">Escopo</div><div class="v">{len(ITENS)} itens no banho da suíte master</div></div>
 </div>

 <div class="prazo"><div><div class="k">Entrega no cliente · finalizada</div>
   <div class="d">{ENTREGA}</div></div>
  <div class="t">É a data da <b>obra pronta e conferida</b>, não a da carga. Todas as etapas do
   cronograma abaixo trabalham para ela — a previsão de cada uma tem de caber antes desta data.</div></div>

 <div class="info">{cards}</div>

 <div class="sec">1 · <b>Os {len(ITENS)} itens contratados</b>, no banho da suíte master</div>
 <table><tr><th>Ambiente</th><th>Item</th><th>Especificação</th><th class="ok">OK</th></tr>{itens}</table>

 <div class="sec">2 · <b>Cronograma de etapas</b> · previsão de entrega de cada etapa</div>
 <table class="cr"><colgroup><col style="width:8mm"><col style="width:38mm"><col><col style="width:23mm">
  <col style="width:23mm"><col style="width:8mm"></colgroup><tr><th>Nº</th><th>Etapa</th><th>O que fecha a etapa</th><th class="dt">Previsão</th>
  <th class="dt">Realizado</th><th class="ok">✓</th></tr>{crono}</table>

 <div class="sec">3 · Ferragens que serão utilizadas e estrutura</div>
 <div class="fer">{fer}</div>
 <div class="bl"><span class="h">Estrutura e chapas.</span> {ESTRUTURA}</div>
 <div class="at"><div class="e">Ponto de atenção</div><div>{PERFIL}</div></div>

 <div class="sec">4 · A definir antes de liberar a produção</div>
 <table><tr><th class="ok">✓</th><th>O que</th><th>Condição</th><th>Definido em</th></tr>{defs}</table>

 <div class="sig">
  <div><div class="h">Comercial</div><div class="d">Repassado em ___/___/______</div></div>
  <div><div class="h">Gestão</div><div class="d">Recebido e conferido em ___/___/______</div></div>
  <div><div class="h">Produção</div><div class="d">Liberado em ___/___/______</div></div>
 </div>
 <div class="ft"><span>Valvic Marcenaria · Vargas Decor LTDA</span><span>{E(RODAPE)}</span></div>
</div>
</body></html>"""

# ── as travas ───────────────────────────────────────────────────────────
_t = re.sub(r'<[^>]+>', ' ', HTML.split('<body>')[1])
for _c in ('Attos', 'Costa Laguna', 'Haverson', 'Ana Carolina', 'Alexandre', 'Gisele', 'Gustavo', 'Phillip'):
    assert _c not in _t, f'⛔ vestígio de outro cliente: {_c}'
assert 'R$' not in _t, '⛔ o escopo de venda não leva preço'
assert not [c for c in '⭐⛔⚠' if c in _t], '⛔ marcação interna'
assert 'amadeirado' not in _t, '⛔ as cores são definidas com a arquiteta'
for _fora in ('Como usar', 'Fora do escopo', 'Revisão final', 'Apoio da bancada', 'Cuba e sifão',
              'Perfil das folhas', 'Medidas que fecham', 'manter em 18', 'frentes de gaveta'):
    assert _fora not in _t, f'⛔ saiu da folha [Jonathan, 10/11/2026]: {_fora}'
assert 'extra fino' in _t and all(e in _t for e, _d in ETAPAS) and ENTREGA in _t

R = P / 'orlando-ivone'
R.mkdir(exist_ok=True)
OUT = R / 'escopo-venda-orlando-ivone.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'Valvic_Escopo_Venda_Orlando_Ivone.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDF)], capture_output=True,
                                                       text=True).stdout).group(1))
assert npg == 1, f'⛔ "reformule para ficar tudo em uma página": saiu com {npg}'
print(f'{PDF.name} · 1 folha · {len(ITENS)} itens · {len(ETAPAS) + 1} etapas · {len(DEFINIR)} pontos a definir')
