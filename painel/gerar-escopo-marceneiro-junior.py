# -*- coding: utf-8 -*-
"""Gera os dois escopos de Marceneiro Junior (CLT e PJ).
Mesmo corpo de escopo; muda so a pagina de remuneracao."""
import io, re

CSS = re.search(r'(?is)<style.*?</style>',
                io.open('escopo-marceneiro.html', encoding='utf-8').read()).group(0)

HEAD = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Valvic &middot; Escopo de Fun&ccedil;&atilde;o &mdash; Marceneiro J&uacute;nior (%(reg)s)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
""" + CSS + """</head><body>"""

def rh(kx, tt, pag):
    return ('<div class="rh"><div><div class="kx">%s</div><div class="tt">%s</div></div>'
            '<div class="r"><b>VALVIC MARCENARIA</b><br>Vargas Decor Ltda<br>'
            'CNPJ 17.269.304/0001-51</div></div><div class="gold-rule"></div>' % (kx, tt)), \
           ('<div class="rf"><span>%s</span><span>%s</span></div>' % (pag[0], pag[1]))

# ---------------------------------------------------------------- 1 CAPA
def capa(reg, sub):
    return """<section class="sheet">
<div class="capa">
  <div class="mk">V</div>
  <div class="kx">Escopo de Fun&ccedil;&atilde;o</div>
  <h1>Marceneiro J&uacute;nior</h1>
  <div class="nv">Produ&ccedil;&atilde;o e montagem &middot; %(sub)s</div>
  <div class="ln"></div>
  <div class="lead">Este documento diz, sem rodeio, o que a Valvic espera do seu trabalho,
  o que voc&ecirc; recebe em troca, como funciona a contrata&ccedil;&atilde;o e por quais
  resultados voc&ecirc; responde. &Eacute; o combinado &mdash; escrito, para que nenhuma das
  duas partes precise adivinhar.</div>
  <div class="emp"><b>LEGADO &middot; SINERGIA &middot; EXCEL&Ecirc;NCIA</b><br>
  Marcenaria de alto padr&atilde;o &middot; Belo Horizonte / MG<br>
  Documento de escopo &middot; anexo ao %(anexo)s</div>
</div>
<div class="rf"><span>Valvic &middot; Marceneiro J&uacute;nior</span><span>1 / 5</span></div>
</section>""" % {'sub': sub, 'anexo': ('contrato de trabalho' if reg == 'CLT'
                                      else 'contrato de presta&ccedil;&atilde;o de servi&ccedil;os')}

# ---------------------------------------------------------------- 2 CONTEXTO
def contexto(reg):
    h, f = rh('Contexto', 'A empresa, o seu lugar nela e o n&iacute;vel do cargo',
              ('Contexto e n&iacute;vel do cargo', '2 / 5'))
    regime = 'CLT' if reg == 'CLT' else 'Presta&ccedil;&atilde;o de servi&ccedil;os'
    return """<section class="sheet">%(h)s<div class="body">
<div class="sec"><div class="bar"></div><div class="kx">Escopo &middot; Marceneiro J&uacute;nior</div></div>
<div class="sec2">Quem &eacute; a Valvic</div>
<p>A Valvic &eacute; uma marcenaria de alto padr&atilde;o de Belo Horizonte. Fabricamos m&oacute;veis
planejados sob medida para clientes exigentes, boa parte com projeto de arquiteto, com ferragens
de primeira linha e CNC pr&oacute;pria. Nossos valores s&atilde;o <b>Legado, Sinergia e
Excel&ecirc;ncia</b>: aqui n&atilde;o se busca vender muito, e sim vender bem e entregar melhor
ainda. Cada pe&ccedil;a leva o nome da casa.</p>

<div class="ficha">
  <div class="f" style="width:33.33%%"><div class="k">Cargo</div><div class="v">Marceneiro J&uacute;nior</div></div>
  <div class="f" style="width:33.33%%"><div class="k">&Aacute;rea</div><div class="v">Produ&ccedil;&atilde;o e Montagem</div></div>
  <div class="f" style="width:33.34%%"><div class="k">Regime</div><div class="v">%(regime)s</div></div>
  <div class="f" style="width:33.33%%"><div class="k">Supervis&atilde;o</div><div class="v">Coordena&ccedil;&atilde;o de Produ&ccedil;&atilde;o</div></div>
  <div class="f" style="width:33.33%%"><div class="k">Trabalha com</div><div class="v">Ajudante <span>sob a sua condu&ccedil;&atilde;o</span></div></div>
  <div class="f" style="width:33.34%%"><div class="k">Local</div><div class="v">F&aacute;brica <span>e obra do cliente</span></div></div>
  <div class="f" style="width:100%%;border-right:0"><div class="k">Forma&ccedil;&atilde;o e acompanhamento</div><div class="v">Deivson <span>na f&aacute;brica</span> &middot; Samuel <span>na obra</span></div></div>
</div>

<div class="sec2">Onde o J&uacute;nior entra</div>
<p>O n&iacute;vel do cargo n&atilde;o &eacute; definido por tempo de casa, e sim pela
<b>complexidade do ambiente</b> pelo qual voc&ecirc; responde &mdash; a mesma r&eacute;gua que a
casa usa para or&ccedil;ar.</p>
<div class="escada">
  <div class="deg">
    <div class="n">01</div><div class="t">Ajudante</div>
    <div class="d">Apoia a produ&ccedil;&atilde;o e aprende o of&iacute;cio. <b>N&atilde;o responde por ambiente.</b></div>
  </div>
  <div class="deg aqui">
    <div class="n">02</div><div class="t">Marceneiro J&uacute;nior<span class="tagaqui">voc&ecirc; est&aacute; aqui</span></div>
    <div class="d">Responde por <b>ambiente de complexidade m&eacute;dia</b>: arm&aacute;rio, gaveta, prateleira, frente lisa ou ripada. O que a f&aacute;brica faz todo dia.</div>
  </div>
  <div class="deg">
    <div class="n">03</div><div class="t">Marceneiro</div>
    <div class="d">Responde por ambiente <b>dif&iacute;cil e complexo</b>: usinagem de relevo, palhinha, moldura em pe&ccedil;a inteira, geometria fora de esquadro, estrutura met&aacute;lica aparente.</div>
  </div>
</div>

<div class="nota"><div class="h">A l&oacute;gica desta fun&ccedil;&atilde;o</div>
Voc&ecirc; recebe um ambiente e <b>responde por ele</b>: pelo prazo, pelo acabamento, pelo material
que consumiu, pela ferramenta que usou e pelo ajudante que trabalhou com voc&ecirc;. A
autonomia cresce na medida em que a entrega se confirma &mdash; e o caminho para o pr&oacute;ximo
degrau &eacute; o que voc&ecirc; demonstra saber fazer, avaliado a cada 90 dias.</div>
</div>%(f)s</section>""" % {'h': h, 'f': f, 'regime': regime}

# ---------------------------------------------------------------- 3 FABRICA
def fabrica():
    h, f = rh('Escopo &middot; Parte 1', 'Na f&aacute;brica', ('Escopo de f&aacute;brica', '3 / 5'))
    return """<section class="sheet">%(h)s<div class="body">
<div class="grupo"><div class="gh"><div class="gn">1</div><div class="gt">Ler o projeto antes de encostar na chapa</div></div>
<ul>
<li>Interpretar o projeto executivo e o plano de corte, e conferir se o que est&aacute; desenhado fecha com a medida real da obra</li>
<li>Levantar d&uacute;vida <b>antes de cortar</b> &mdash; pe&ccedil;a errada n&atilde;o volta a ser chapa</li>
<li>Conferir cor, espessura, veio e quantidade do material recebido</li>
</ul></div>

<div class="grupo"><div class="gh"><div class="gn">2</div><div class="gt">Fabricar no padr&atilde;o da casa</div></div>
<ul>
<li>Montagem de caixaria e de gaveta, com esquadro e folga corretos</li>
<li><b>Filetagem</b>, inclusive de puxador, e o acabamento que define o padr&atilde;o Valvic</li>
<li>Fura&ccedil;&atilde;o, ferragens e regulagem &mdash; dobradi&ccedil;a, corredi&ccedil;a, pist&atilde;o e puxador</li>
<li>Opera&ccedil;&atilde;o segura da serra e das m&aacute;quinas para as quais voc&ecirc; tem autoriza&ccedil;&atilde;o</li>
<li>Aproveitamento de chapa: o MDF &eacute; o maior custo do projeto, e sobra mal cortada &eacute; dinheiro no lixo</li>
</ul></div>

<div class="grupo"><div class="gh"><div class="gn">3</div><div class="gt">Conferir antes de sair</div></div>
<ul>
<li>Preencher a <b>ficha de confer&ecirc;ncia de produ&ccedil;&atilde;o</b> do ambiente antes do carregamento</li>
<li>Separar e conferir ferragens, perfis e acess&oacute;rios &mdash; o que falta na obra vira viagem</li>
<li>Proteger a pe&ccedil;a para o transporte: risco feito na carga &eacute; retrabalho seu</li>
</ul></div>

<div class="grupo"><div class="gh"><div class="gn">4</div><div class="gt">Organiza&ccedil;&atilde;o e limpeza</div></div>
<ul>
<li>Bancada, ferramenta e corredor livres ao fim de cada dia &mdash; padr&atilde;o 5S</li>
<li>Retalho aproveit&aacute;vel guardado e identificado; o que n&atilde;o presta, descartado</li>
<li>Cada ferramenta devolvida ao seu lugar, para que a pr&oacute;xima pessoa a encontre</li>
<li>P&oacute;, serragem e res&iacute;duo recolhidos do posto de trabalho</li>
</ul></div>

<div class="nota at"><div class="h">O que a Valvic n&atilde;o aceita</div>
<b>Esconder erro.</b> Pe&ccedil;a que voltou, medida errada, risco no m&oacute;vel do cliente ou
material danificado t&ecirc;m de ser avisados <b>na hora</b>. Erro avisado cedo &eacute; problema
pequeno; erro descoberto pelo cliente &eacute; preju&iacute;zo e &eacute; confian&ccedil;a perdida.
Ningu&eacute;m aqui &eacute; cobrado por avisar &mdash; s&oacute; por esconder.</div>
</div>%(f)s</section>""" % {'h': h, 'f': f}

# ---------------------------------------------------------------- 4 OBRA
def obra():
    h, f = rh('Escopo &middot; Parte 2', 'Na obra e os limites do cargo', ('Escopo de obra e limites', '4 / 5'))
    return """<section class="sheet">%(h)s<div class="body">
<div class="grupo"><div class="gh"><div class="gn">5</div><div class="gt">Montar como quem assina a pe&ccedil;a</div></div>
<ul>
<li>Conferir medida e prumo antes de subir o m&oacute;vel; parede fora de esquadro se resolve na montagem, n&atilde;o na reclama&ccedil;&atilde;o</li>
<li>Fixa&ccedil;&atilde;o segura, nivelamento, regulagem de porta e de gaveta</li>
<li>Instala&ccedil;&atilde;o de bancada, prateleira, nicho e pe&ccedil;as de banheiro</li>
<li>Arremate e acabamento final &mdash; &eacute; o que o cliente v&ecirc; primeiro</li>
</ul></div>

<div class="grupo"><div class="gh"><div class="gn">6</div><div class="gt">Conduta na casa do cliente</div></div>
<ul>
<li>Proteger piso e ambiente, e devolver o espa&ccedil;o limpo ao fim do dia</li>
<li>Falar com o cliente com respeito e <b>nunca combinar mudan&ccedil;a de escopo direto com ele</b> &mdash; qualquer pedido novo passa pela coordena&ccedil;&atilde;o</li>
<li>Quando utilizar ve&iacute;culo da empresa, registrar a ficha de uso na sa&iacute;da e na volta</li>
</ul></div>

<div class="grupo"><div class="gh"><div class="gn">7</div><div class="gt">Conduzir o ajudante</div></div>
<ul>
<li>Mostrar como se faz, n&atilde;o s&oacute; mandar fazer</li>
<li>Responder pela seguran&ccedil;a de quem est&aacute; trabalhando com voc&ecirc;</li>
<li>Dizer &agrave; coordena&ccedil;&atilde;o, com honestidade, o que o ajudante j&aacute; domina e o que falta</li>
</ul></div>

<div class="sec2">Os limites do cargo</div>
<p>O que ainda <b>n&atilde;o</b> &eacute; responsabilidade do J&uacute;nior. Estes limites
protegem voc&ecirc; e protegem a obra &mdash; e deixam de valer conforme os degraus se confirmam.</p>
<ul>
<li>N&atilde;o decide altera&ccedil;&atilde;o de projeto</li>
<li>N&atilde;o combina escopo novo com o cliente</li>
<li>N&atilde;o libera ambiente para carregamento sem a confer&ecirc;ncia da coordena&ccedil;&atilde;o</li>
<li>N&atilde;o opera m&aacute;quina para a qual n&atilde;o tem autoriza&ccedil;&atilde;o</li>
<li>N&atilde;o responde sozinho por ambiente <b>dif&iacute;cil ou complexo</b></li>
</ul>

<div class="sec2">Pelo que voc&ecirc; responde</div>
<table class="compacta">
<tr><th style="width:42%%">Resultado</th><th>Como se mede</th></tr>
<tr><td><b>Prazo</b></td><td>Ambiente entregue na data combinada com a coordena&ccedil;&atilde;o</td></tr>
<tr><td><b>Qualidade</b></td><td>Ambiente aceito na Confer&ecirc;ncia de Sa&iacute;da sem retrabalho</td></tr>
<tr><td><b>Material</b></td><td>Aproveitamento de chapa e consumo dentro do previsto para o ambiente</td></tr>
<tr><td><b>Registro</b></td><td>Ficha de confer&ecirc;ncia de produ&ccedil;&atilde;o preenchida antes do carregamento</td></tr>
<tr><td><b>Transpar&ecirc;ncia</b></td><td>Zero retrabalho causado por erro que n&atilde;o foi avisado</td></tr>
</table>
</div>%(f)s</section>""" % {'h': h, 'f': f}

# ------------------------------------------------- 5 REMUNERACAO (difere)
FERR = """<div class="sec2">Ferramentas e EPI</div>
<p>As ferramentas, equipamentos e EPIs necess&aacute;rios ao trabalho s&atilde;o
<b>cedidos pela Valvic, sem custo</b>. A cess&atilde;o &eacute; feita por meio do
<b>Termo de Responsabilidade de Ferramentas</b>, assinado na entrega, com a rela&ccedil;&atilde;o
do que foi recebido.</p>
<ul>
<li>Perda, extravio ou dano por mau uso s&atilde;o de responsabilidade de quem estava com a ferramenta, nos termos do documento assinado</li>
<li>Desgaste natural &eacute; da empresa &mdash; ferramenta que quebrou trabalhando n&atilde;o &eacute; problema seu, desde que comunicada</li>
<li>Ao fim do contrato, tudo &eacute; conferido e devolvido contra a mesma rela&ccedil;&atilde;o</li>
</ul>"""

AVAL = """<div class="sec2">Avalia&ccedil;&atilde;o e pr&oacute;ximo degrau</div>
<p>A cada <b>90 dias</b> h&aacute; uma conversa de avalia&ccedil;&atilde;o com quem te acompanha
&mdash; Deivson na f&aacute;brica, Samuel na obra. A r&eacute;gua &eacute; o que voc&ecirc; j&aacute;
domina, n&atilde;o o tempo de casa. Se a evolu&ccedil;&atilde;o veio, ela vira avan&ccedil;o; se
n&atilde;o veio, o ciclo repete por mais 90 dias, com o ponto a desenvolver dito de forma
clara e espec&iacute;fica. Ningu&eacute;m avan&ccedil;a sem estar pronto, e ningu&eacute;m fica
parado sem saber por qu&ecirc;.</p>"""

ASSIN = """<div class="local">Belo Horizonte, <span class="l"></span> de
<span class="l"></span> de <span class="s"></span>.</div>
<div class="assin">
  <div class="a"><div class="ln"></div><div class="t">Valvic Marcenaria &middot; Vargas Decor Ltda</div></div>
  <div class="a"><div class="ln"></div><div class="t">%(quem)s</div></div>
</div>"""

def remun_clt():
    h, f = rh('Remunera&ccedil;&atilde;o e condi&ccedil;&otilde;es', 'Regime CLT',
              ('Remunera&ccedil;&atilde;o &middot; CLT', '5 / 5'))
    return """<section class="sheet">%(h)s<div class="body">
<div class="remun">
  <div class="c"><div class="k">Sal&aacute;rio mensal</div><div class="v">R$ 2.500</div>
    <div class="s">Registrado em carteira</div></div>
  <div class="c"><div class="k">Vale-refei&ccedil;&atilde;o</div><div class="v">R$ 400</div>
    <div class="s">Por m&ecirc;s, desde a admiss&atilde;o</div></div>
  <div class="c"><div class="k">Vale-transporte</div><div class="v">Conforme regi&atilde;o</div>
    <div class="s">Calculado pelo seu trajeto</div></div>
</div>

<table class="compacta">
<tr><th style="width:34%%">Item</th><th>Como funciona</th></tr>
<tr><td><b>Regime</b></td><td>CLT, com registro em carteira desde o primeiro dia</td></tr>
<tr><td><b>Experi&ecirc;ncia</b></td><td>Contrato de experi&ecirc;ncia de <b>90 dias</b>, prorrog&aacute;vel uma vez, nos termos da lei</td></tr>
<tr><td><b>Direitos</b></td><td>13&ordm; sal&aacute;rio, f&eacute;rias com 1/3, FGTS e os demais previstos em lei</td></tr>
<tr><td><b>Vale-refei&ccedil;&atilde;o</b></td><td>R$ 400 por m&ecirc;s, mantidos em todas as etapas da trilha</td></tr>
<tr><td><b>Vale-transporte</b></td><td>Conforme a regi&atilde;o de moradia e o trajeto at&eacute; a f&aacute;brica</td></tr>
<tr><td><b>Ferramental</b></td><td>Cedido pela Valvic, sob termo assinado</td></tr>
<tr><td><b>Ajudante</b></td><td>Disponibilizado pela empresa, sob a sua condu&ccedil;&atilde;o</td></tr>
</table>

<div class="nota"><div class="h">Sobre o vale-transporte</div>
O valor do VT &eacute; calculado hoje para a f&aacute;brica no <b>Horto</b>. Na mudan&ccedil;a
para o <b>Jardim Canad&aacute;</b>, o benef&iacute;cio ser&aacute; <b>reajustado</b> para o novo
trajeto. Isso n&atilde;o depende de pedido seu: a empresa recalcula quando a mudan&ccedil;a
acontecer.</div>

%(ferr)s
%(aval)s
%(assin)s
</div>%(f)s</section>""" % {'h': h, 'f': f, 'ferr': FERR, 'aval': AVAL,
                            'assin': ASSIN % {'quem': 'Colaborador &middot; Marceneiro J&uacute;nior'}}

def remun_pj():
    h, f = rh('Remunera&ccedil;&atilde;o e condi&ccedil;&otilde;es', 'Presta&ccedil;&atilde;o de servi&ccedil;os',
              ('Remunera&ccedil;&atilde;o &middot; PJ', '5 / 5'))
    return """<section class="sheet">%(h)s<div class="body">
<div class="remun">
  <div class="c"><div class="k">Ajuda de custo mensal</div><div class="v">R$ 3.500</div>
    <div class="s">Valor inicial, podendo chegar a <b>R$ 4.500</b></div></div>
  <div class="c"><div class="k">Comiss&atilde;o de fabrica&ccedil;&atilde;o</div><div class="v">2,5%%</div>
    <div class="s">Do ambiente que voc&ecirc; fabricar</div></div>
  <div class="c"><div class="k">Comiss&atilde;o de montagem</div><div class="v">2,5%%</div>
    <div class="s">Do ambiente que voc&ecirc; montar</div></div>
</div>

<div class="nota ok"><div class="h">A ajuda de custo &eacute; piso, n&atilde;o adiantamento</div>
A ajuda de custo &eacute; paga <b>independentemente da comiss&atilde;o</b>. Ela n&atilde;o &eacute;
descontada do que voc&ecirc; produzir: a comiss&atilde;o vem <b>por cima</b> dela. Em um m&ecirc;s
de pouca produ&ccedil;&atilde;o voc&ecirc; recebe a ajuda de custo integral; em um m&ecirc;s forte,
recebe a ajuda de custo <b>mais</b> a comiss&atilde;o.</div>

<div class="sec2">Como a comiss&atilde;o &eacute; calculada</div>
<p>Os 2,5%% incidem sobre a <b>receita l&iacute;quida do ambiente</b> &mdash; o valor de venda
menos a nota fiscal, a taxa do meio de pagamento, a RT do arquiteto e a comiss&atilde;o de venda.
&Eacute; o mesmo crit&eacute;rio que vale para toda a equipe de produ&ccedil;&atilde;o da casa.</p>

<table class="compacta">
<tr><th colspan="2">Exemplo &mdash; ambiente de R$ 18.000, pago por transfer&ecirc;ncia, projeto com RT de arquiteto</th></tr>
<tr><td>Valor de venda do ambiente</td><td class="n">R$ 18.000,00</td></tr>
<tr><td>(&minus;) Nota fiscal, 5%%</td><td class="n">&minus; R$ 900,00</td></tr>
<tr><td>(&minus;) RT do arquiteto, 10%% do l&iacute;quido</td><td class="n">&minus; R$ 1.710,00</td></tr>
<tr><td><b>= Receita l&iacute;quida do ambiente</b></td><td class="n"><b>R$ 15.390,00</b></td></tr>
<tr><td>Comiss&atilde;o de fabrica&ccedil;&atilde;o &middot; 2,5%%</td><td class="n">R$ 384,75</td></tr>
<tr><td>Comiss&atilde;o de montagem &middot; 2,5%%</td><td class="n">R$ 384,75</td></tr>
<tr><td><b>Total, se voc&ecirc; fizer as duas etapas</b></td><td class="n"><b>R$ 769,50</b></td></tr>
</table>

<div class="nota at"><div class="h">Leia com aten&ccedil;&atilde;o</div>
As duas comiss&otilde;es <b>n&atilde;o s&atilde;o autom&aacute;ticas no mesmo ambiente</b>. Na
casa, fabrica&ccedil;&atilde;o e montagem muitas vezes ficam com pessoas diferentes. Voc&ecirc;
recebe a comiss&atilde;o <b>da etapa que executou</b> &mdash; se executar as duas, recebe as duas;
se executar uma, recebe uma. A distribui&ccedil;&atilde;o &eacute; da coordena&ccedil;&atilde;o
de produ&ccedil;&atilde;o e fica registrada na ficha do projeto.</div>

<table class="compacta">
<tr><th style="width:34%%">Item</th><th>Como funciona</th></tr>
<tr><td><b>Regime</b></td><td>Presta&ccedil;&atilde;o de servi&ccedil;os, com CNPJ pr&oacute;prio e nota fiscal mensal</td></tr>
<tr><td><b>Pagamento</b></td><td>Ajuda de custo no m&ecirc;s de refer&ecirc;ncia; comiss&atilde;o conforme a ficha do projeto</td></tr>
<tr><td><b>Ferramental</b></td><td>Cedido pela Valvic, sob termo assinado</td></tr>
<tr><td><b>Ajudante</b></td><td>Disponibilizado pela empresa, sob a sua condu&ccedil;&atilde;o</td></tr>
<tr><td><b>Avalia&ccedil;&atilde;o</b></td><td>A cada 90 dias, com a coordena&ccedil;&atilde;o</td></tr>
</table>

%(ferr)s
%(aval)s
%(assin)s
</div>%(f)s</section>""" % {'h': h, 'f': f, 'ferr': FERR, 'aval': AVAL,
                            'assin': ASSIN % {'quem': 'Prestador &middot; Marceneiro J&uacute;nior'}}

# ---------------------------------------------------------------- EMIT
for reg, sub, remun, nome in [
    ('CLT', 'regime CLT', remun_clt(), 'escopo-marceneiro-junior-clt.html'),
    ('PJ', 'presta&ccedil;&atilde;o de servi&ccedil;os', remun_pj(), 'escopo-marceneiro-junior-pj.html'),
]:
    doc = (HEAD.replace('%(reg)s', reg) + capa(reg, sub) + contexto(reg) + fabrica()
           + obra() + remun + '</body></html>')
    io.open(nome, 'w', encoding='utf-8').write(doc)
    print('%s  ->  %d caracteres' % (nome, len(doc)))
