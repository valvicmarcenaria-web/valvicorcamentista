# -*- coding: utf-8 -*-
"""ORLANDO E IVONE — ESCOPO DE VENDA  [10/11/2026]

⭐ [Jonathan, 10/11/2026] "preciso que vc veja como feito o escopo de venda do
   projeto do Attos e faça o escopo do orlando".
⭐ O modelo é o `Valvic_Escopo_Venda_Attos.pdf` do Drive (06/11/2026), em duas folhas A4:
   · folha 1 · cabeçalho com cliente, obra, projeto e escopo · "como usar" ·
     ATENÇÃO, a prioridade da obra · medição, entrega e garantia · 1, OS ITENS
     CONTRATADOS, com a coluna OK;
   · folha 2 · 2, FERRAGENS, ESTRUTURA E O QUE FICA FORA · 3, A DEFINIR E A
     ALINHAR ANTES DE LIBERAR A PRODUÇÃO, com a coluna "definido em" ·
     assinaturas de Comercial, Gestão e Produção.
⭐ Documento INTERNO, para a gestão e a produção: leva contagem de peça e
   especificação técnica, e não leva preço (o do Attos também não leva).
⭐ A fonte é o fechamento de 21/10/2026, na linha PREMIUM
   (`proposta-orlando-ivone-fechamento.pdf`), e o dossiê `2026-orlando-ivone.md`.
⚠ A data de assinatura do contrato não está aqui: o campo sai em branco para o
  comercial preencher.
"""
import pathlib, subprocess, os, re, html

P = pathlib.Path(__file__).resolve().parent
E = lambda t: html.escape(str(t))

CLIENTE = 'Orlando e Ivone'
OBRA = 'Apartamento · Rua Passa Tempo, Belo Horizonte'
PROJETO = '[31] Apto Orlando e Ivone · Ana Maria Castro · Rev. 00'
LOCAL = 'Orlando e Ivone · Rua Passa Tempo, Belo Horizonte'
RODAPE = 'ESCOPO DE VENDA · BANHO SUÍTE MASTER · ORLANDO E IVONE'

ATENCAO = ('A bancada não apoia no armário', [
 ('Bancada de pedra', 'O armário inferior <b>não sustenta a bancada</b>. A pedra tem apoio e '
  'fixação próprios, de obra, e o móvel entra por baixo dela. <b>Alinhar com a marmoraria</b> '
  'antes de detalhar — a pedra é de terceiro.'),
 ('Projeto em estudo', 'As pranchas 31_.2 e 31_.6 estão na <b>Rev. 00</b>, carimbadas "não '
  'plotar, estudo enviado para análise". <b>Pedir à arquiteta a revisão liberada</b>; nada corta '
  'antes dela.'),
 ('Luz na espelheira', 'As três peças fixas recebem as <b>arandelas</b> e, por dentro, o '
  '<b>driver</b>. Berço e passagem são nossos; o modelo da arandela e do driver tem de chegar '
  'antes do corte.'),
])
CARDS = [
 ('Medição técnica', 'Até 7 dias corridos após a assinatura (___/___/______)'),
 ('Entrega', '50 dias corridos contados da medição — não da assinatura'),
 ('Linha contratada', 'Premium · MDF Ultra resistente à umidade · ferragem Hettich com amortecimento'),
 ('Garantia', '10 anos estrutura e ferragens · 2 anos instalação e regulagem · arandelas e driver '
  'pelo fabricante'),
]
ITENS = [
 ('BANHO SUÍTE', 'Armário inferior sob a bancada',
  'Duas portas de giro sob a cuba e quatro gavetas sobre corrediça oculta Hettich com amortecimento '
  '· frente em amadeirado fosco, caixaria em branco · puxador Zen Phenix 20 cm cromado · assenta no '
  'sóculo de alvenaria, sob a pedra, sem sustentá-la'),
 ('BANHO SUÍTE', 'Armário superior · espelheira',
  'Quatro folhas de espelho prata em perfil de alumínio, de giro, em dois vãos · puxador de trespasse '
  'de 1 cm, sem puxador aplicado · três peças fixas em amadeirado para as arandelas, com berço e '
  'passagem do driver · interior branco, com prateleiras'),
]
FERRAGENS = ('Corrediça oculta Hettich com amortecimento, uma por gaveta · dobradiça com amortecedor '
             'nas portas do inferior e nas folhas de espelho, que <b>não perdoam desalinho</b> · '
             'puxador Zen Phenix 20 cm cromado nas portas e gavetas do inferior · trespasse de 1 cm '
             'nas folhas de espelho, sem puxador aplicado')
ESTRUTURA = ('MDF Ultra, resistente à umidade · caixaria em branco · todo o aparente em amadeirado '
             'fosco <b>em 18 mm</b>: portas, frentes de gaveta, as três peças fixas, a lateral direita '
             'dos dois móveis e a base da espelheira — <b>manter em 18</b>: em 15 entra uma chapa a '
             'mais · espelho prata em perfil de alumínio, fornecido e alinhado por nós')
FORA = ('<b>Pedra:</b> bancada e o seu apoio e fixação, rodabanca, testeira, acabamento do sóculo e '
        'o nicho do box — marmoraria. <b>Obra:</b> o sóculo em alvenaria, o porcelanato e as '
        'soleiras. <b>Box de correr, louças, metais e acessórios.</b> <b>Arandelas, driver e a '
        'instalação elétrica</b> — nossa é só a usinagem da passagem e o berço na peça fixa.')
DEFINIR = [
 ('Padrão do amadeirado', 'A legenda da prancha diz "MDF a definir"; o fechamento vendeu '
  '<b>amadeirado fosco</b>. Definir o padrão com o cliente e a arquiteta <b>antes de comprar chapa</b>.'),
 ('Revisão final do projeto', 'Rev. 00, estudo. <b>Pedir à arquiteta a revisão liberada para '
  'execução</b> e conferir se a marcenaria mudou.'),
 ('Arandelas e driver', 'Modelo e medida das arandelas e do driver, para o berço e a passagem na '
  'peça fixa. <b>Ponto elétrico posicionado pela obra</b> — sem ele, não há luz na entrega.'),
 ('Apoio da bancada', 'Confirmar com a marmoraria o <b>apoio e a fixação próprios da pedra</b>. O '
  'armário entra por baixo e não carrega.'),
 ('Cuba e sifão', 'A cuba cai sobre o vão das portas: conferir na medição a posição do sifão e da '
  'hidráulica, para as <b>gavetas ficarem livres</b>.'),
 ('Perfil das folhas de espelho', 'A prancha diz só "perfil de alumínio". <b>Definir o acabamento '
  'do perfil</b> com a arquiteta.'),
 ('Medidas que fecham na medição', 'Altura do sóculo e da bancada, largura entre paredes e altura '
  'livre entre a bancada e o forro para a espelheira.'),
]

CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{--navy:#14233B;--gold:#B8913F;--gold-lt:#E2C98E;--ink:#1B1F27;--soft:#4A515E;--mut:#8A909B;
      --line:#DADDE2;--cream:#F6EEDB;--paper:#FFFDF8;--red:#B23A2E;--redbg:#FCF1EF}
body{font-family:'DM Sans',system-ui,sans-serif;color:var(--ink);font-size:7.6pt;line-height:1.45}
.page{width:210mm;height:297mm;padding:11mm 12mm 9mm;display:flex;flex-direction:column;
      page-break-after:always;overflow:hidden;position:relative}
.page:last-child{page-break-after:auto}
.hd{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:2.6mm;
    border-bottom:2px solid var(--navy)}
.hd .lg{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;font-weight:700;line-height:.9}
.hd .lg small{display:block;font-family:'DM Sans',sans-serif;font-size:5.6pt;letter-spacing:.42em;
    color:var(--gold);font-weight:700;margin-top:1.6mm}
.hd .r{text-align:right}
.hd .r .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;font-weight:700;line-height:1}
.hd .r .s{font-size:6.4pt;color:var(--mut);margin-top:1.2mm}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:2.4mm;margin-top:3.4mm}
.cards>div{border:1px solid var(--line);border-radius:2px;padding:2mm 2.6mm}
.cards .k{font-size:5.4pt;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);font-weight:600}
.cards .v{font-size:7.6pt;font-weight:700;margin-top:.8mm;line-height:1.3}
.uso{margin-top:3mm;background:var(--cream);border-left:3px solid var(--gold);padding:2.6mm 3.4mm;
     font-size:7.2pt;color:var(--soft)}
.uso b{color:var(--ink)}
.at{margin-top:3mm;border:1.5px solid var(--gold);border-radius:3px;background:var(--paper);
    padding:2.8mm 3.6mm 1.4mm}
.at .e{font-size:5.6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700}
.at .h{font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;font-weight:700;margin:.6mm 0 1.6mm}
.at .rw{display:grid;grid-template-columns:4mm 33mm 1fr;gap:2.4mm;padding:1.8mm 0;
        border-top:1px solid #EFE6D2;align-items:start}
.box{width:3.2mm;height:3.2mm;border:1.2px solid var(--ink);border-radius:.6mm;display:inline-block}
.at .rw .k{font-weight:700;font-size:7.2pt}
.at .rw .d{color:var(--soft);font-size:7.2pt}
.at .rw .d b,.uso b{color:var(--ink)}
.info{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm;margin-top:3mm}
.info>div{border:1px solid var(--line);border-left:3px solid var(--navy);padding:2mm 3mm}
.info .k{font-size:5.4pt;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);font-weight:600}
.info .v{font-size:7.4pt;margin-top:.8mm}
.sec{margin-top:4mm;background:var(--navy);color:#fff;padding:2mm 3mm;font-size:6.6pt;
     letter-spacing:.24em;text-transform:uppercase;font-weight:600}
.sec b{color:var(--gold-lt);font-weight:600}
table{width:100%;border-collapse:collapse;margin-top:0}
th{background:var(--navy);color:var(--gold-lt);font-size:5.4pt;letter-spacing:.2em;text-transform:uppercase;
   text-align:left;padding:1.6mm 2.4mm;font-weight:600}
td{padding:2mm 2.4mm;border-bottom:1px solid var(--line);vertical-align:top;font-size:7.2pt}
tr:nth-child(even) td{background:#F7F8FA}
td.amb{font-family:'DM Mono',ui-monospace,monospace;font-size:6.4pt;letter-spacing:.06em;font-weight:500;
       white-space:nowrap}
td.it{font-weight:700;width:46mm}
td.sp{color:var(--soft)}
td.ok,th.ok{width:9mm;text-align:center}
td.def{width:30mm;color:var(--mut);white-space:nowrap}
.bl{margin-top:2.6mm;border:1px solid var(--line);border-left:3px solid var(--navy);padding:2.6mm 3.4mm;
    font-size:7.2pt;color:var(--soft)}
.bl b{color:var(--ink)}
.bl .k{color:var(--ink);font-weight:700}
.bl.fora{background:var(--redbg);border-left-color:var(--red)}
.bl.fora .k{color:var(--red)}
.sig{display:grid;grid-template-columns:repeat(3,1fr);gap:9mm;margin-top:auto;padding-top:6mm}
.sig>div{border-top:1px solid var(--ink);padding-top:1.4mm;text-align:center}
.sig .k{font-weight:700;font-size:7.4pt}
.sig .d{font-size:6.6pt;color:var(--soft)}
.ft{display:flex;justify-content:space-between;border-top:1px solid var(--line);margin-top:4mm;
    padding-top:2mm;font-size:5.6pt;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}
.pg1 .ft{margin-top:auto}
"""

def cab(n, tot):
    return f'''<div class="hd"><div class="lg">valvic<small>MARCENARIA</small></div>
  <div class="r"><div class="t">Escopo de Venda</div>
   <div class="s">{E(LOCAL)} · folha {n} de {tot}</div></div></div>'''

FT = f'<div class="ft"><span>Valvic Marcenaria · Vargas Decor LTDA</span><span>{E(RODAPE)}</span></div>'
BOX = '<span class="box"></span>'

at_rows = ''.join(f'<div class="rw">{BOX}<div class="k">{E(k)}</div><div class="d">{d}</div></div>'
                  for k, d in ATENCAO[1])
cards = ''.join(f'<div><div class="k">{E(k)}</div><div class="v">{E(v)}</div></div>' for k, v in CARDS)
itens = ''.join(f'<tr><td class="amb">{E(a)}</td><td class="it">{E(i)}</td><td class="sp">{E(s)}</td>'
                f'<td class="ok">{BOX}</td></tr>' for a, i, s in ITENS)
defs = ''.join(f'<tr><td class="ok">{BOX}</td><td class="it">{E(k)}</td><td class="sp">{d}</td>'
               f'<td class="def">……………………</td></tr>' for k, d in DEFINIR)
N_IT = {1: 'O ITEM CONTRATADO', 2: 'OS 2 ITENS CONTRATADOS'}.get(len(ITENS), f'OS {len(ITENS)} ITENS CONTRATADOS')

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Escopo de Venda · {E(CLIENTE)}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<div class="page pg1">
 {cab(1, 2)}
 <div class="cards">
  <div><div class="k">Cliente</div><div class="v">{E(CLIENTE)}</div></div>
  <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
  <div><div class="k">Projeto</div><div class="v">{E(PROJETO)}</div></div>
  <div><div class="k">Escopo</div><div class="v">{len(ITENS)} itens no banho da suíte master</div></div>
 </div>
 <div class="uso"><b>Como usar.</b> Escopo da venda em especificação técnica, montado a partir da
  <b>proposta de fechamento de 21/10/2026, linha Premium</b>. Leia cruzando com as <b>pranchas 31_.2 e
  31_.6 do projeto [31], Rev. 00</b>. Onde esta lista divergir do projeto, <b>não libere a produção</b>:
  registre e devolva ao comercial. <b>Alteração de projeto só vale por escrito</b> e pode gerar aditivo
  de prazo e de preço.</div>
 <div class="at"><div class="e">Atenção · prioridade da obra</div><div class="h">{E(ATENCAO[0])}</div>
  {at_rows}</div>
 <div class="info">{cards}</div>
 <div class="sec">1 · <b>{N_IT}</b>, no banho da suíte master</div>
 <table><tr><th>Ambiente</th><th>Item</th><th>Especificação</th><th class="ok">OK</th></tr>{itens}</table>
 {FT}
</div>

<div class="page">
 {cab(2, 2)}
 <div class="sec">2 · Ferragens, estrutura e o que fica fora</div>
 <div class="bl"><span class="k">Ferragens.</span> {FERRAGENS}</div>
 <div class="bl"><span class="k">Estrutura e chapas.</span> {ESTRUTURA}</div>
 <div class="bl fora"><span class="k">Fora do escopo.</span> {FORA}</div>
 <div class="sec">3 · A definir e a alinhar antes de liberar a produção</div>
 <table><tr><th class="ok">✓</th><th>O que</th><th>Condição</th><th>Definido em</th></tr>{defs}</table>
 <div class="sig">
  <div><div class="k">Comercial</div><div class="d">Repassado em ___/___/______</div></div>
  <div><div class="k">Gestão</div><div class="d">Recebido e conferido em ___/___/______</div></div>
  <div><div class="k">Produção</div><div class="d">Liberado em ___/___/______</div></div>
 </div>
 {FT}
</div>
</body></html>"""

# ── as travas ───────────────────────────────────────────────────────────
_t = re.sub(r'<[^>]+>', ' ', HTML.split('<body>')[1])
for _c in ('Attos', 'Costa Laguna', 'Haverson', 'Ana Carolina', 'Alexandre', 'Gisele', 'Gustavo', 'Phillip'):
    assert _c not in _t, f'⛔ vestígio de outro cliente: {_c}'
assert 'R$' not in _t, '⛔ o escopo de venda não leva preço'
assert not [c for c in '⭐⛔⚠' if c in _t], '⛔ marcação interna'

R = P / 'orlando-ivone'
R.mkdir(exist_ok=True)
OUT = R / 'escopo-venda-orlando-ivone.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'Valvic_Escopo_Venda_Orlando_Ivone.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDF)], capture_output=True,
                                                       text=True).stdout).group(1))
assert npg == 2, f'⛔ o escopo tem duas folhas, como o do Attos: saiu com {npg}'
print(f'{PDF.name} · {npg} folhas · {len(ITENS)} itens · {len(DEFINIR)} pontos a definir')
