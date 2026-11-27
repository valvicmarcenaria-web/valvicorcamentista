# -*- coding: utf-8 -*-
"""Comunicado de Acordo — Comissoes de Projeto (projetistas). 2 folhas A4."""
import io, re
CSS = re.search(r'(?is)<style.*?</style>',
                io.open('escopo-marceneiro.html', encoding='utf-8').read()).group(0)

EXTRA = """<style>
.body{padding:4.5mm 14mm 2mm}
.duas{display:flex;gap:6mm}.duas>div{flex:1;min-width:0}
.cmp li{font-size:7.6pt;line-height:1.42;margin-bottom:1mm;padding-left:3.4mm}
.cmp li::before{top:1.5mm;width:1.5mm;height:1.5mm}
ul.cmp{padding-left:0}
.mini{font-size:6.2pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);
  font-weight:800;margin:0 0 1.6mm;display:flex;align-items:center;gap:2mm}
.mini::after{content:'';flex:1;height:.25mm;background:var(--line)}
.fichaL{display:flex;border:.3mm solid var(--navy2);margin:0 0 3.4mm}
.fichaL .f{flex:1;padding:1.7mm 2.8mm;border-right:.25mm solid var(--line);min-width:0}
.fichaL .f:last-child{border-right:0}
.fichaL .k{font-size:5.4pt;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);font-weight:700}
.fichaL .v{font-size:7.8pt;font-weight:700;color:var(--navy);margin-top:.5mm;line-height:1.2}
.et{display:grid;grid-template-columns:7mm 1fr;gap:2.6mm;margin-bottom:1.6mm}
.et .n{font-family:'Cormorant Garamond',serif;font-size:11pt;font-weight:700;color:var(--goldsoft);line-height:1.1;text-align:right}
.et .t{font-size:7.8pt;line-height:1.4}
.et .t b{color:var(--navy)}
.gatilho{background:var(--navy);color:#fff;padding:3mm 4mm;border-radius:1mm;margin:1mm 0 3.4mm}
.gatilho .h{font-size:6.2pt;letter-spacing:.18em;text-transform:uppercase;color:var(--goldsoft);font-weight:800;margin-bottom:1.4mm}
.gatilho p{font-size:9pt;line-height:1.5;margin:0;color:#fff}
.gatilho b{color:var(--goldsoft)}
.sim{background:#F4F8F5;border-left:1.1mm solid var(--ok);padding:2.2mm 3mm}
.nao{background:#FAF6F6;border-left:1.1mm solid var(--red);padding:2.2mm 3mm}
.sim .hh,.nao .hh{font-size:6.2pt;letter-spacing:.16em;text-transform:uppercase;font-weight:800;margin-bottom:1.4mm}
.sim .hh{color:var(--ok)}.nao .hh{color:var(--red)}
.sim li,.nao li{font-size:7.4pt;line-height:1.38;margin-bottom:.9mm;padding-left:3.2mm}
.sim li::before,.nao li::before{top:1.3mm;width:1.3mm;height:1.3mm}
.sim ul,.nao ul{padding-left:0}
.passo{display:grid;grid-template-columns:7mm 1fr;gap:2.6mm;margin-bottom:2mm}
.passo .n{width:5.6mm;height:5.6mm;border-radius:50%;background:var(--navy);color:#fff;display:flex;
  align-items:center;justify-content:center;font-size:6.6pt;font-weight:800}
.passo .t{font-size:7.8pt;line-height:1.42}
.passo .t b{color:var(--navy)}
.falta{background:var(--goldbg);color:#7A5B17;font-weight:700;padding:0 1mm;border-radius:.6mm}
.flx{display:flex;align-items:stretch;gap:0;margin:1mm 0 2mm}
.flx .cx{flex:1;min-width:0;display:flex;flex-direction:column}
.flx .lane{font-size:5.4pt;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);
  font-weight:800;text-align:center;margin-bottom:1.2mm;min-height:3mm}
.flx .bx{flex:1;border:.35mm solid var(--gold);background:#FFFCF4;border-radius:1mm;
  padding:2.4mm 2mm;display:flex;align-items:center;justify-content:center;text-align:center;
  font-size:7.4pt;font-weight:700;color:var(--navy);line-height:1.25}
.flx .dia{flex:1;border:.35mm solid #7FA6CC;background:#EEF4FA;border-radius:1mm;
  padding:2.4mm 2mm;display:flex;align-items:center;justify-content:center;text-align:center;
  font-size:7.4pt;font-weight:800;color:#204A73;line-height:1.25}
.flx .ar{display:flex;align-items:center;justify-content:center;width:5mm;flex:0 0 5mm;
  color:var(--gold);font-size:10pt;font-weight:700;padding-top:4mm}
.ramos{display:flex;gap:4mm;margin:0 0 3mm}
.ramo{flex:1;border-radius:1mm;padding:2.4mm 3mm;font-size:7.6pt;line-height:1.4}
.ramo .q{font-size:6pt;letter-spacing:.18em;text-transform:uppercase;font-weight:800;margin-bottom:1.2mm}
.ramo.s{background:#F0F6F2;border-left:1.1mm solid var(--ok)}
.ramo.s .q{color:var(--ok)}
.ramo.n{background:#FBF6EF;border-left:1.1mm solid var(--gold)}
.ramo.n .q{color:#8A6A1E}
.ramo b{color:var(--navy)}
.obs{display:flex;gap:4mm;font-size:6.8pt;line-height:1.35;color:#7A5B17;margin:0 0 3mm}
.obs div{flex:1;background:var(--goldbg);border-radius:1mm;padding:1.6mm 2.4mm}
.obs b{color:#5E4512}
</style>"""

HEAD = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Valvic &middot; Comunicado de Acordo &mdash; Comiss&otilde;es de Projeto</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
""" + CSS + EXTRA + """</head><body>"""

def rh(kx,tt):
    return ('<div class="rh"><div><div class="kx">%s</div><div class="tt">%s</div></div>'
            '<div class="r"><b>VALVIC MARCENARIA</b><br>Vargas Decor Ltda<br>'
            'CNPJ 17.269.304/0001-51</div></div><div class="gold-rule"></div>'%(kx,tt))
def rf(e,d):
    return '<div class="rf"><span>%s</span><span>%s</span></div>'%(e,d)

P1 = """<section class="sheet">%(h)s<div class="body">
<p style="font-size:8.6pt;line-height:1.55">Este documento registra a decis&atilde;o da diretoria sobre o
<b>formato de pagamento das comiss&otilde;es de projeto</b>, tomada depois das conversas com o setor. Ele diz
em que momento a comiss&atilde;o passa a ser devida, em que datas ela &eacute; paga e o que acontece se um erro
de projeto gerar custo para a empresa. &Eacute; o combinado &mdash; escrito, para que nenhuma das partes precise
adivinhar.</p>

<div class="fichaL" style="margin-top:3.4mm">
  <div class="f"><div class="k">Setor</div><div class="v">Projeto e Programa&ccedil;&atilde;o</div></div>
  <div class="f"><div class="k">Aplica-se a</div><div class="v">Projetistas</div></div>
  <div class="f"><div class="k">Vig&ecirc;ncia</div><div class="v"><span class="falta">[[a partir de __/__/____]]</span></div></div>
  <div class="f"><div class="k">Decis&atilde;o</div><div class="v">Diretoria</div></div>
</div>

<div class="mini">O fluxo do setor &mdash; etapa a etapa</div>
<div class="flx">
  <div class="cx"><div class="lane">Projetista</div><div class="bx">Medi&ccedil;&atilde;o</div></div>
  <div class="ar">&rarr;</div>
  <div class="cx"><div class="lane">Projetista</div><div class="bx">Programa&ccedil;&atilde;o</div></div>
  <div class="ar">&rarr;</div>
  <div class="cx"><div class="lane">Desenhista / projetista</div><div class="bx">Detalhamento do cliente</div></div>
  <div class="ar">&rarr;</div>
  <div class="cx"><div class="lane">&nbsp;</div><div class="dia">Validou?</div></div>
  <div class="ar">&rarr;</div>
  <div class="cx"><div class="lane">Desenhista</div><div class="bx">Detalhamento produ&ccedil;&atilde;o</div></div>
  <div class="ar">&rarr;</div>
  <div class="cx"><div class="lane">Projetista</div><div class="bx">Libera&ccedil;&atilde;o para produ&ccedil;&atilde;o<br>arquivos gerais e lista de compras</div></div>
</div>

<div class="ramos">
  <div class="ramo s"><div class="q">Validou &middot; sim</div>
  Segue para o <b>detalhamento de produ&ccedil;&atilde;o</b> e, na mesma hora,
  <b>libera a comiss&atilde;o do projetista</b>.</div>
  <div class="ramo n"><div class="q">Validou &middot; n&atilde;o</div>
  Vai para o <b>Ajusta</b> e <b>volta para a Programa&ccedil;&atilde;o</b>. O ciclo se repete at&eacute;
  validar, e <b>n&atilde;o gera comiss&atilde;o nem penalidade</b> &mdash; ajuste antes da valida&ccedil;&atilde;o
  faz parte do trabalho.</div>
</div>

<div class="obs">
  <div><b>Na valida&ccedil;&atilde;o:</b> &eacute; necess&aacute;rio <b>documento assinado</b> pelo cliente.</div>
  <div><b>Na libera&ccedil;&atilde;o:</b> a <b>lista de compras</b> vai lan&ccedil;ada no <b>Calcme</b>.</div>
</div>

<div class="gatilho">
  <div class="h">Quando a comiss&atilde;o fica v&aacute;lida</div>
  <p>A comiss&atilde;o de projeto &eacute; considerada <b>v&aacute;lida mediante a aprova&ccedil;&atilde;o do
  detalhamento apresentado ao cliente, com o aceite dele</b> &mdash; e o aceite s&oacute; existe com
  <b>documento assinado</b>. Antes disso o projeto n&atilde;o gera comiss&atilde;o, ainda que j&aacute;
  esteja desenhado e reapresentado v&aacute;rias vezes.</p>
</div>

<div class="mini">Datas de corte e de pagamento</div>
<table class="compacta">
<tr><th style="width:52%%">Aprova&ccedil;&atilde;o do detalhamento pelo cliente</th><th>Pagamento</th></tr>
<tr><td>Do dia <b>26 do m&ecirc;s anterior</b> at&eacute; o dia <b>10</b></td><td><b>Dia 15</b> do mesmo m&ecirc;s</td></tr>
<tr><td>Do dia <b>11</b> at&eacute; o dia <b>25</b></td><td><b>Dia 30</b> do mesmo m&ecirc;s</td></tr>
<tr><td>Do dia <b>26</b> em diante</td><td>Dia 15 do m&ecirc;s seguinte</td></tr>
</table>
<p style="font-size:7.4pt;line-height:1.45;color:var(--muted);margin-top:1.6mm">Se o dia 15 ou o dia 30 ca&iacute;rem
em s&aacute;bado, domingo ou feriado, o pagamento ocorre no primeiro dia &uacute;til seguinte. Em fevereiro, e nos
meses de 31 dias, o &ldquo;dia 30&rdquo; &eacute; o <b>&uacute;ltimo dia do m&ecirc;s</b>. A data que vale &eacute;
a da <b>assinatura do documento de aceite</b> pelo cliente, n&atilde;o a do envio do detalhamento.</p>
</div>%(f)s</section>"""

P2 = """<section class="sheet">%(h)s<div class="body">
<div class="nota at"><div class="h">O pagamento n&atilde;o encerra a responsabilidade t&eacute;cnica</div>
Receber a comiss&atilde;o no aceite do cliente <b>n&atilde;o exime o profissional de responder pelas falhas
t&eacute;cnicas decorrentes do seu trabalho</b>. O motivo &eacute; simples: a efic&aacute;cia do projeto s&oacute;
se confirma depois, porque o servi&ccedil;o ainda percorre programa&ccedil;&atilde;o, corte, fabrica&ccedil;&atilde;o,
confer&ecirc;ncia de sa&iacute;da e montagem &mdash; e &eacute; nessas etapas que um erro de projeto aparece.
A comiss&atilde;o &eacute; paga antes porque a empresa confia no trabalho, n&atilde;o porque deixou de conferi-lo.</div>

<div class="mini">O que &eacute; e o que n&atilde;o &eacute; erro de projeto</div>
<div class="duas">
  <div class="nao"><div class="hh">Responde o projetista</div><ul>
    <li>Medida, cota ou folga erradas no detalhamento</li>
    <li>Ferragem especificada incompat&iacute;vel com a pe&ccedil;a ou com o v&atilde;o</li>
    <li>Material, cor ou espessura divergentes do que foi vendido e aceito</li>
    <li>Sentido de abertura, de veio ou usinagem indicados de forma incorreta</li>
    <li>Interfer&ecirc;ncia n&atilde;o prevista entre m&oacute;vel, parede, el&eacute;trica, hidr&aacute;ulica ou eletrodom&eacute;stico</li>
    <li>Arquivos gerais ou lista de compras liberados para a produ&ccedil;&atilde;o incompletos, ou divergentes do detalhamento que foi validado</li>
  </ul></div>
  <div class="sim"><div class="hh">N&atilde;o responde o projetista</div><ul>
    <li>Altera&ccedil;&atilde;o pedida pelo cliente ou pelo arquiteto <b>depois</b> do aceite</li>
    <li>Diverg&ecirc;ncia de obra em rela&ccedil;&atilde;o &agrave; medida informada por terceiro</li>
    <li>Falha de execu&ccedil;&atilde;o: corte, colagem, furo ou montagem fora do que o projeto manda</li>
    <li>Defeito de material ou de ferragem vindo do fornecedor</li>
    <li>Ponto que o projetista <b>sinalizou por escrito</b> como pend&ecirc;ncia e seguiu sem defini&ccedil;&atilde;o</li>
    <li>Decis&atilde;o t&eacute;cnica tomada pela coordena&ccedil;&atilde;o contra a recomenda&ccedil;&atilde;o registrada do projetista</li>
  </ul></div>
</div>

<div class="mini" style="margin-top:4mm">Como uma ocorr&ecirc;ncia &eacute; tratada</div>
<div class="passo"><div class="n">1</div><div class="t"><b>Identifica&ccedil;&atilde;o.</b> A ocorr&ecirc;ncia precisa ser
<b>evidente e clara</b>, com a origem no projeto demonstrada &mdash; a pe&ccedil;a, o detalhamento e o que
divergiu.</div></div>
<div class="passo"><div class="n">2</div><div class="t"><b>Apresenta&ccedil;&atilde;o.</b> O erro &eacute; apresentado ao
profissional de forma <b>&eacute;tica, correta e respeitosa</b>, em conversa reservada, com o material em
m&atilde;os. Nunca em grupo e nunca por terceiros.</div></div>
<div class="passo"><div class="n">3</div><div class="t"><b>Direito de resposta.</b> O profissional tem direito a
apresentar a sua leitura t&eacute;cnica. Se ela afastar a origem no projeto, a ocorr&ecirc;ncia &eacute;
encerrada sem desconto.</div></div>
<div class="passo"><div class="n">4</div><div class="t"><b>Apura&ccedil;&atilde;o do custo.</b> Confirmada a origem,
levanta-se <b>apenas o custo de mat&eacute;ria-prima</b> que a empresa precisou repor. M&atilde;o de obra, frete e
tempo de f&aacute;brica n&atilde;o entram nesta conta.</div></div>

<div class="mini" style="margin-top:3.4mm">O desconto</div>
<p style="font-size:8.2pt;line-height:1.5">Quando o erro exp&otilde;e a empresa a <b>custo de mat&eacute;ria-prima</b>,
esse valor &eacute; descontado das <b>comiss&otilde;es em aberto e, se necess&aacute;rio, das futuras</b>.</p>
<div class="local" style="margin-top:4mm">Belo Horizonte, <span class="l"></span> de
<span class="l"></span> de <span class="s"></span>.</div>
<div class="assin">
  <div class="a"><div class="ln"></div><div class="t">Valvic Marcenaria &middot; Diretoria</div></div>
  <div class="a"><div class="ln"></div><div class="t">Projetista &middot; ci&ecirc;ncia e de acordo</div></div>
</div>
</div>%(f)s</section>"""

doc = (HEAD
  + P1 % {'h': rh('Comunicado de Acordo','Comiss&otilde;es de Projeto'),
          'f': rf('Fluxo, gatilho e datas de pagamento','1 / 2')}
  + P2 % {'h': rh('Comunicado de Acordo','Responsabilidade t&eacute;cnica'),
          'f': rf('Responsabilidade, apura&ccedil;&atilde;o e desconto','2 / 2')}
  + '</body></html>')
io.open('comunicado-comissoes-projeto.html','w',encoding='utf-8').write(doc)
print('gerado: %d caracteres'%len(doc))
