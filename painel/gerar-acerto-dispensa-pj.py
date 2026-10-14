# -*- coding: utf-8 -*-
"""Acerto de dispensa de prestador PJ — folha A4 de apuração e quitação.

Modelo reaproveitável: trocar o bloco DADOS e gerar de novo. O documento é editado
AQUI, nunca no HTML final — a próxima geração apaga qualquer mudança feita lá.

    python3 painel/gerar-acerto-dispensa-pj.py > painel/acerto-dispensa-pj.html
"""

# ---------------------------------------------------------------- dados do caso
DADOS = dict(
    prestador      = 'Jackson Martins Duarte Neto',
    cnpj           = '',                 # em branco: preencher à mão ou aqui
    funcao         = 'Marceneiro Pleno · PJ',
    ultimo_dia     = '14/10/2026',
    periodo        = '01 a 14/10/2026',
    emissao        = '14/10/2026',
    fixo_mensal    = 3600.00,
    dias_periodo   = 14,                 # dias corridos de 01 até o último dia
    dias_nao_prest = 2,
    comissao       = 650.00,
    pecas          = [                   # material comprado pela empresa para serviço próprio
        ('2 chapas Branco TX 15 mm',        440.00),
        ('1 chapa Branco TX 6 mm',          175.00),
        ('50 m de fita de borda Branco TX 22 mm', 28.00),
    ],
)

D = DADOS
D['diaria']     = D['fixo_mensal'] / 30            # regra dos 30 avos
D['dias_remun'] = D['dias_periodo'] - D['dias_nao_prest']
D['servico']    = D['dias_remun'] * D['diaria']
D['divida_mdf'] = sum(v for _, v in D['pecas'])
D['bruto']      = D['servico'] + D['comissao']
D['liquido']    = D['bruto'] - D['divida_mdf']
# método alternativo, só para a caixa de comparação
D['diaria_u']   = D['fixo_mensal'] / 22
D['liquido_u']  = 8 * D['diaria_u'] + D['comissao'] - D['divida_mdf']

def brl(v):
    return f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea;
  --ok:#2F7D4F; --red:#B0413F; --blue:#2F5D8C; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:12mm 13mm 11mm; display:flex; flex-direction:column;
  page-break-after:always; overflow:hidden }
.sheet:last-child{ page-break-after:auto }
@media print{ body{ background:#fff } .sheet{ margin:0 } }

.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:9px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:25px; font-weight:700;
  color:var(--navy); letter-spacing:.5px; line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7.5px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-top:3px }
.doc{ text-align:right }
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:19px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:8px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.ident{ display:grid; grid-template-columns:repeat(5,1fr); gap:6px; margin-bottom:9px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold);
  border-radius:2px; padding:6px 8px }
.ident .r{ font-size:7px; letter-spacing:1.3px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:10.5px; font-weight:700; color:var(--navy); margin-top:2px; min-height:13px }
.ident .v.b{ font-weight:400; color:var(--linha); letter-spacing:1px }

.faixa{ background:var(--navy); color:var(--goldsoft); font-size:8.5px; font-weight:600;
  letter-spacing:2px; text-transform:uppercase; padding:5px 9px; margin:9px 0 6px; border-radius:2px }

table.tb{ width:100%; border-collapse:collapse; font-size:9px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:7.5px; font-weight:600;
  letter-spacing:.8px; text-transform:uppercase; padding:5px 7px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:5px 7px; vertical-align:top }
table.tb tr:nth-child(even) td{ background:#f7f9fb }
.num{ text-align:right; font-variant-numeric:tabular-nums }
.ob{ color:var(--muted); font-size:8px }
tr.tot td{ background:var(--goldbg) !important; font-weight:700; color:var(--navy);
  border-bottom:1px solid var(--gold) }
tr.liq td{ background:var(--navy) !important; color:#fff; font-weight:700; font-size:10px }
tr.liq td.num{ color:var(--goldsoft); font-size:12px }

.kpis{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin:9px 0 2px }
.kpi{ background:var(--navy); color:#fff; border-radius:3px; padding:7px 9px }
.kpi .r{ font-size:7px; letter-spacing:1.3px; text-transform:uppercase; color:var(--goldsoft) }
.kpi .v{ font-size:16px; font-weight:700; font-family:'Cormorant Garamond',serif; margin-top:1px }
.kpi .o{ font-size:7px; color:#b9c3cf; margin-top:1px }

.card{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:2px;
  padding:7px 10px; margin-top:7px }
.card.r{ border-left-color:var(--red) } .card.b{ border-left-color:var(--blue) }
.duo{ display:grid; grid-template-columns:1fr 1fr; gap:7px }
.duo .card{ margin-top:7px }
.card h3{ margin:0 0 3px; font-size:9px; color:var(--navy); font-weight:700 }
.card p{ margin:0; font-size:8.5px; line-height:1.45; color:#45525f }
.card p + p{ margin-top:3px }

.dev{ display:grid; grid-template-columns:1fr 1fr; gap:5px 14px; margin-top:5px }
.dev div{ font-size:8.5px; display:flex; gap:6px; align-items:center }
.cx{ display:inline-block; width:10px; height:10px; border:1.3px solid var(--navy);
  border-radius:2px; flex:0 0 auto }

.assina{ display:grid; grid-template-columns:1fr 1fr; gap:22px; margin-top:auto; padding-top:10px; margin-bottom:2px }
.assina > div{ border-top:1px solid var(--ink); padding-top:3px; text-align:center }
.assina .n{ font-size:8.5px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:7.5px; color:var(--muted) }

.rodape{ margin-top:12px; border-top:1px solid var(--linha); padding-top:4px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

LINHA_PECA = ('    <tr><td style="padding-left:22px" class="ob">__ITEM__</td>'
              '<td class="ob">compra de material</td>'
              '<td class="num ob">__VALOR__</td></tr>')
PECAS_HTML = '\n'.join(
    LINHA_PECA.replace('__ITEM__', n).replace('__VALOR__', 'R$ ' + brl(v))
    for n, v in DADOS['pecas'])


def cel(v):
    return f'<div class="v">{v}</div>' if v else '<div class="v b">____________</div>'

HTML = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Acerto de dispensa — prestador PJ</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Acerto de Dispensa — Prestador PJ</h1>
      <div class="m">Vargas Decor Ltda · CNPJ 17.269.304/0001-51 · emitido em __EMISSAO__ · uso restrito</div></div>
  </div>

  <div class="ident">
    <div class="c" style="grid-column:span 2"><div class="r">Prestador</div>__PRESTADOR__</div>
    <div class="c"><div class="r">CNPJ</div>__CNPJ__</div>
    <div class="c"><div class="r">Função · contrato</div><div class="v" style="font-size:9px">__FUNCAO__</div></div>
    <div class="c"><div class="r">Último dia prestado</div><div class="v">__ULTIMO__</div></div>
  </div>

  <div class="faixa">1 · Apuração do serviço — período __PERIODO__</div>

  <table class="tb">
    <tr><th style="width:46%">Conta</th><th style="width:34%">Como se chega</th><th class="num">Valor</th></tr>
    <tr><td>Fixo mensal contratado</td><td class="ob">valor cheio do mês</td><td class="num">R$ __FIXO__</td></tr>
    <tr><td>Base diária — regra dos 30 avos</td><td class="ob">__FIXO__ ÷ 30</td><td class="num">R$ __DIARIA__</td></tr>
    <tr><td>Dias do período</td><td class="ob">01 até o último dia prestado</td><td class="num">__DIAS__</td></tr>
    <tr><td>Dias não prestados</td><td class="ob">dias sem serviço no período</td><td class="num">− __NAO__</td></tr>
    <tr class="tot"><td>Dias a remunerar</td><td class="ob">__DIAS__ − __NAO__</td><td class="num">__REMUN__</td></tr>
    <tr class="tot"><td>Serviço do período</td><td class="ob">__REMUN__ × R$ __DIARIA__</td><td class="num">R$ __SERVICO__</td></tr>
  </table>

  <div class="faixa">2 · Composição do acerto</div>

  <table class="tb">
    <tr><th style="width:46%">Lançamento</th><th style="width:34%">Natureza</th><th class="num">Valor</th></tr>
    <tr><td>Serviço prestado — __PERIODO__</td><td class="ob">prestação de serviços</td><td class="num">R$ __SERVICO__</td></tr>
    <tr><td>Comissão em aberto</td><td class="ob">variável já apurada</td><td class="num">R$ __COMISSAO__</td></tr>
    <tr class="tot"><td>Bruto do acerto</td><td class="ob">serviço + comissão</td><td class="num">R$ __BRUTO__</td></tr>
    <tr><td>Compensação — material comprado pela empresa</td>
        <td class="ob">destinado a <b>serviço próprio do prestador</b> — não aplicado em obra da Valvic</td>
        <td class="num">− R$ __MDF__</td></tr>
__PECAS__
    <tr class="liq"><td>Líquido a pagar no acerto</td><td class="ob" style="color:#b9c3cf">mediante nota fiscal</td><td class="num">R$ __LIQUIDO__</td></tr>
  </table>

  <div class="kpis">
    <div class="kpi"><div class="r">Serviço</div><div class="v">__SERVICO__</div><div class="o">__REMUN__ dias × __DIARIA__</div></div>
    <div class="kpi"><div class="r">Comissão</div><div class="v">__COMISSAO__</div><div class="o">já apurada</div></div>
    <div class="kpi"><div class="r">Compensação</div><div class="v">− __MDF__</div><div class="o">material · serviço próprio</div></div>
    <div class="kpi" style="background:var(--gold);color:var(--navy)">
      <div class="r" style="color:var(--navy2)">Líquido a pagar</div><div class="v">__LIQUIDO__</div>
      <div class="o" style="color:var(--navy2)">com nota fiscal</div></div>
  </div>

  <div class="card r">
    <h3>O que confirmar antes de pagar — pode mudar este número</h3>
    <p><b>1 · Aviso prévio contratual.</b> Contrato de prestação de serviços costuma prever
    aviso de 30 dias. Se o contrato tiver essa cláusula e a dispensa for imediata, há indenização
    a somar — pelo fixo atual, R$ __FIXO__. <b>Ler o contrato assinado antes de fechar o valor.</b></p>
    <p><b>2 · Nota fiscal.</b> Pagamento de PJ só sai contra NF emitida no valor do acerto.
    Pedir a nota antes de agendar o pagamento, e conferir a descrição do serviço.</p>
    <p><b>3 · Fechamento da comissão.</b> A remuneração variável dele é <b>2,5% de fabricação + 2,5%
    de montagem</b>, por obra. Conferir se os R$ __COMISSAO__ cobrem tudo que venceu até __ULTIMO__ —
    inclusive montagem concluída e ainda não lançada.</p>
    <p><b>4 · Aceite do desconto do material.</b> Compensar os R$ __MDF__ exige concordância por
    escrito do prestador — é o que a assinatura desta folha registra. Sem o aceite, paga-se
    R$ __BRUTO__ e a dívida é cobrada em separado.</p>
  </div>

  <div class="duo">
    <div class="card b">
      <h3>PJ não gera verba rescisória</h3>
      <p>Sem aviso prévio legal, 13º, férias + 1/3, FGTS ou multa de 40% — isso é de contrato CLT.
      O acerto de prestador é <b>serviço + variáveis em aberto − compensações</b>, como apurado acima.</p>
    </div>
    <div class="card">
      <h3>Vocabulário do lançamento</h3>
      <p>Em contrato PJ não existe "falta": existe <b>dia não prestado</b>. Controlar falta é registro
      de subordinação — o mesmo risco já apontado no alinhamento do César. O valor não muda.</p>
    </div>
  </div>

  <div class="assina">
    <div><div class="n">Prestador</div><div class="s">Dou plena quitação e concordo com a compensação · ___/___/______</div></div>
    <div><div class="n">Valvic Marcenaria — Vargas Decor Ltda</div><div class="s">Autorização de pagamento · Jonathan ou Paulo</div></div>
  </div>


</body>
</html>'''

for k, v in [
    ('__CSS__', CSS), ('__EMISSAO__', D['emissao']), ('__ULTIMO__', D['ultimo_dia']),
    ('__PERIODO__', D['periodo']), ('__PRESTADOR__', cel(D['prestador'])),
    ('__CNPJ__', cel(D['cnpj'])), ('__FUNCAO__', D['funcao']), ('__FIXO__', brl(D['fixo_mensal'])),
    ('__DIARIA__', brl(D['diaria'])), ('__DIAS__', str(D['dias_periodo'])),
    ('__NAO__', str(D['dias_nao_prest'])), ('__REMUN__', str(D['dias_remun'])),
    ('__SERVICO__', brl(D['servico'])), ('__COMISSAO__', brl(D['comissao'])),
    ('__BRUTO__', brl(D['bruto'])), ('__MDF__', brl(D['divida_mdf'])), ('__PECAS__', PECAS_HTML),
    ('__LIQUIDO__', brl(D['liquido'])),
]:
    HTML = HTML.replace(k, v)

print(HTML)
