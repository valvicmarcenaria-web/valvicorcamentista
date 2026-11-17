# -*- coding: utf-8 -*-
"""Escopo de Marceneiro Junior em folha unica, com os dois formatos."""
import io, re
CSS = re.search(r'(?is)<style.*?</style>',
                io.open('escopo-marceneiro.html', encoding='utf-8').read()).group(0)

EXTRA = """<style>
.body{padding:4mm 13mm 2mm}
.duas{display:flex;gap:6mm}
.duas>div{flex:1;min-width:0}
.cmp{font-size:7.3pt;line-height:1.38}
.cmp li{font-size:7.3pt;line-height:1.38;margin-bottom:.9mm;padding-left:3.2mm}
.cmp li::before{top:1.35mm;width:1.4mm;height:1.4mm}
ul.cmp{padding-left:0}
.mini{font-size:6.2pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);
  font-weight:800;margin:0 0 1.4mm;display:flex;align-items:center;gap:2mm}
.mini::after{content:'';flex:1;height:.25mm;background:var(--line)}
.fichaL{display:flex;border:.3mm solid var(--navy2);margin:0 0 3mm}
.fichaL .f{flex:1;padding:1.6mm 2.6mm;border-right:.25mm solid var(--line);min-width:0}
.fichaL .f:last-child{border-right:0}
.fichaL .k{font-size:5.4pt;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);font-weight:700}
.fichaL .v{font-size:7.6pt;font-weight:700;color:var(--navy);margin-top:.5mm;line-height:1.2}
.deg3{display:flex;gap:2.4mm;margin:0 0 3mm}
.deg3>div{flex:1;border:.28mm solid var(--line);border-radius:1mm;padding:1.8mm 2.4mm;min-width:0}
.deg3 .t{font-size:7.8pt;font-weight:800;color:var(--navy);line-height:1.15}
.deg3 .d{font-size:6.8pt;line-height:1.35;color:var(--ink);margin-top:.8mm}
.deg3 .aq{background:var(--goldbg);border-color:var(--gold)}
.lim{background:#f7f9fb;border:.28mm solid var(--line);border-left:1.1mm solid var(--navy2);
  padding:2mm 3mm;font-size:7.2pt;line-height:1.45;margin:0 0 3mm}
.lim b{color:var(--navy)}
.pack{border:.3mm solid var(--line);border-top:1mm solid var(--gold);border-radius:1mm;
  padding:2.4mm 3mm;background:#fffdf8;height:100%}
.pack .hd{font-family:'Cormorant Garamond',serif;font-size:13pt;font-weight:700;color:var(--navy);line-height:1}
.pack .big{font-family:'Cormorant Garamond',serif;font-size:16pt;font-weight:700;color:var(--navy);
  line-height:1;margin:1.6mm 0 .6mm}
.pack .sm{font-size:6.9pt;line-height:1.4;color:var(--ink)}
.pack .sm b{color:var(--navy)}
.pack ul{padding-left:0;margin-top:1.6mm}
.pack li{font-size:6.9pt;line-height:1.35;margin-bottom:.7mm;padding-left:3mm}
.pack li::before{top:1.2mm;width:1.3mm;height:1.3mm}
.comum{background:var(--navy);color:#fff;padding:2mm 3mm;font-size:7pt;line-height:1.45;
  border-radius:1mm;margin-top:2.6mm}
.comum b{color:var(--goldsoft)}
.alerta{background:var(--redbg);border-left:1.1mm solid var(--red);padding:1.8mm 3mm;
  font-size:7.2pt;line-height:1.42;margin:0 0 3mm}
.alerta b{color:var(--red)}
</style>"""

DOC = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Valvic &middot; Marceneiro J&uacute;nior &mdash; folha &uacute;nica</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
""" + CSS + EXTRA + """</head><body>
<section class="sheet">
<div class="rh"><div><div class="kx">Escopo de Fun&ccedil;&atilde;o</div>
<div class="tt">Marceneiro J&uacute;nior</div></div>
<div class="r"><b>VALVIC MARCENARIA</b><br>Vargas Decor Ltda<br>CNPJ 17.269.304/0001-51</div></div>
<div class="gold-rule"></div>
<div class="body">

<div class="fichaL">
  <div class="f"><div class="k">&Aacute;rea</div><div class="v">Produ&ccedil;&atilde;o e Montagem</div></div>
  <div class="f"><div class="k">Supervis&atilde;o</div><div class="v">Coordena&ccedil;&atilde;o de Produ&ccedil;&atilde;o</div></div>
  <div class="f"><div class="k">Local</div><div class="v">F&aacute;brica e obra do cliente</div></div>
  <div class="f"><div class="k">Trabalha com</div><div class="v">Ajudante sob sua condu&ccedil;&atilde;o</div></div>
  <div class="f"><div class="k">Forma&ccedil;&atilde;o</div><div class="v">Deivson e Samuel</div></div>
</div>

<div class="mini">O n&iacute;vel do cargo &mdash; definido pela complexidade do ambiente, n&atilde;o pelo tempo de casa</div>
<div class="deg3">
  <div><div class="t">Ajudante</div><div class="d">Apoia e aprende. N&atilde;o responde por ambiente.</div></div>
  <div class="aq"><div class="t">Marceneiro J&uacute;nior<span class="tagaqui">este cargo</span></div>
    <div class="d">Responde por <b>ambiente m&eacute;dio</b>: arm&aacute;rio, gaveta, prateleira, frente lisa ou ripada.</div></div>
  <div><div class="t">Marceneiro</div><div class="d">Responde por ambiente <b>dif&iacute;cil e complexo</b>: relevo, palhinha, geometria fora de esquadro.</div></div>
</div>

<div class="duas">
  <div>
    <div class="mini">Na f&aacute;brica</div>
    <ul class="cmp">
      <li><b>Ler o projeto antes de cortar.</b> Projeto executivo e plano de corte conferidos contra a medida real da obra; cor, espessura, veio e quantidade do material; d&uacute;vida se levanta antes &mdash; pe&ccedil;a errada n&atilde;o volta a ser chapa.</li>
      <li><b>Fabricar no padr&atilde;o da casa.</b> Caixaria e gaveta com esquadro e folga corretos; filetagem, inclusive de puxador; fura&ccedil;&atilde;o, ferragens e regulagem de dobradi&ccedil;a, corredi&ccedil;a, pist&atilde;o e puxador.</li>
      <li><b>Chapa e m&aacute;quina.</b> Aproveitamento de chapa &mdash; o MDF &eacute; o maior custo do projeto; opera&ccedil;&atilde;o segura apenas das m&aacute;quinas para as quais h&aacute; autoriza&ccedil;&atilde;o, sempre com EPI.</li>
      <li><b>Conferir antes de sair.</b> Ficha de confer&ecirc;ncia de produ&ccedil;&atilde;o preenchida antes do carregamento; ferragens, perfis e acess&oacute;rios separados; pe&ccedil;a protegida para o transporte.</li>
      <li><b>Organiza&ccedil;&atilde;o e limpeza.</b> Bancada, ferramenta e corredor livres ao fim do dia, padr&atilde;o 5S; cada ferramenta de volta ao seu lugar; retalho aproveit&aacute;vel guardado e identificado; p&oacute; e serragem recolhidos do posto.</li>
    </ul>
  </div>
  <div>
    <div class="mini">Na obra</div>
    <ul class="cmp">
      <li><b>Montar como quem assina a pe&ccedil;a.</b> Medida e prumo conferidos antes de subir o m&oacute;vel; parede fora de esquadro se resolve na montagem, n&atilde;o na reclama&ccedil;&atilde;o; fixa&ccedil;&atilde;o segura, nivelamento e regulagem de porta e gaveta.</li>
      <li><b>Acabamento.</b> Instala&ccedil;&atilde;o de bancada, prateleira, nicho e pe&ccedil;as de banheiro; arremate final &mdash; &eacute; o que o cliente v&ecirc; primeiro.</li>
      <li><b>Conduta na casa do cliente.</b> Piso e ambiente protegidos, espa&ccedil;o devolvido limpo; <b>nunca combinar mudan&ccedil;a de escopo direto com o cliente</b> &mdash; pedido novo passa pela coordena&ccedil;&atilde;o.</li>
      <li><b>Conduzir o ajudante.</b> Mostrar como se faz, n&atilde;o s&oacute; mandar fazer; responder pela seguran&ccedil;a de quem trabalha com voc&ecirc;; dizer &agrave; coordena&ccedil;&atilde;o o que ele j&aacute; domina e o que falta.</li>
      <li><b>Ve&iacute;culo.</b> Quando utilizar ve&iacute;culo da empresa, registrar a ficha de uso na sa&iacute;da e na volta.</li>
    </ul>
  </div>
</div>

<div class="lim" style="margin-top:3mm"><b>Os limites do cargo.</b> O J&uacute;nior n&atilde;o decide
altera&ccedil;&atilde;o de projeto &middot; n&atilde;o combina escopo novo com o cliente &middot;
n&atilde;o libera ambiente para carregamento sem a confer&ecirc;ncia da coordena&ccedil;&atilde;o &middot;
n&atilde;o opera m&aacute;quina sem autoriza&ccedil;&atilde;o &middot; n&atilde;o responde sozinho
por ambiente dif&iacute;cil ou complexo. Estes limites protegem voc&ecirc; e protegem a obra, e
deixam de valer conforme os degraus se confirmam.</div>

<div class="alerta"><b>O que a Valvic n&atilde;o aceita: esconder erro.</b> Pe&ccedil;a que voltou,
medida errada, risco no m&oacute;vel do cliente ou material danificado t&ecirc;m de ser avisados
na hora. Erro avisado cedo &eacute; problema pequeno; erro descoberto pelo cliente &eacute;
preju&iacute;zo e &eacute; confian&ccedil;a perdida. Ningu&eacute;m aqui &eacute; cobrado por
avisar &mdash; s&oacute; por esconder.</div>

<div class="mini">Os dois formatos de remunera&ccedil;&atilde;o &mdash; mesmo escopo, mesma avalia&ccedil;&atilde;o</div>
<div class="duas">
  <div><div class="pack">
    <div class="hd">CLT</div>
    <div class="big">R$ 2.500 <span style="font-size:8pt;font-weight:400;color:var(--muted)">/ m&ecirc;s</span></div>
    <div class="sm">Sal&aacute;rio com registro em carteira</div>
    <ul>
      <li><b>VR R$ 400</b> por m&ecirc;s, desde a admiss&atilde;o</li>
      <li><b>VT conforme a regi&atilde;o</b> de moradia. Calculado hoje para a f&aacute;brica no <b>Horto</b>; na mudan&ccedil;a para o <b>Jardim Canad&aacute;</b> a empresa reajusta, sem precisar de pedido seu</li>
      <li>Contrato de experi&ecirc;ncia de <b>90 dias</b></li>
      <li>13&ordm; sal&aacute;rio, f&eacute;rias com 1/3, FGTS e os demais direitos de lei</li>
    </ul>
  </div></div>
  <div><div class="pack">
    <div class="hd">Presta&ccedil;&atilde;o de servi&ccedil;os</div>
    <div class="big">R$ 3.500 <span style="font-size:8pt;font-weight:400;color:var(--muted)">a R$ 4.500 / m&ecirc;s</span></div>
    <div class="sm">Ajuda de custo &mdash; <b>piso pago independentemente da comiss&atilde;o</b>, que vem por cima e n&atilde;o &eacute; descontada dela</div>
    <ul>
      <li><b>+ 2,5% sobre fabrica&ccedil;&atilde;o</b> e <b>2,5% sobre montagem</b>, calculados sobre a <b>receita l&iacute;quida do ambiente</b></li>
      <li>Ambiente de R$ 18.000 com RT de arquiteto: receita l&iacute;quida de R$ 15.390 &rarr; <b>R$ 384,75</b> por etapa</li>
      <li>Recebe-se a comiss&atilde;o <b>da etapa executada</b>. Fabrica&ccedil;&atilde;o e montagem muitas vezes ficam com pessoas diferentes</li>
      <li>CNPJ pr&oacute;prio e nota fiscal mensal</li>
    </ul>
  </div></div>
</div>

<div class="comum">Igual nos dois regimes: <b>ferramental, equipamentos e EPI cedidos pela Valvic</b>,
sem custo, sob Termo de Responsabilidade &middot; <b>ajudante disponibilizado pela empresa</b>,
sob a sua condu&ccedil;&atilde;o &middot; <b>avalia&ccedil;&atilde;o a cada 90 dias</b> com quem te
acompanha &mdash; Deivson na f&aacute;brica, Samuel na obra. A r&eacute;gua &eacute; o que voc&ecirc;
j&aacute; domina; se a evolu&ccedil;&atilde;o n&atilde;o veio, o ciclo repete com o ponto a
desenvolver dito de forma clara.</div>

</div>
<div class="rf"><span>Valvic Marcenaria &middot; Escopo de Fun&ccedil;&atilde;o &middot; Marceneiro J&uacute;nior</span><span>Legado &middot; Sinergia &middot; Excel&ecirc;ncia</span></div>
</section></body></html>"""

io.open('escopo-marceneiro-junior-folha-unica.html', 'w', encoding='utf-8').write(DOC)
print('folha unica gerada: %d caracteres' % len(DOC))
