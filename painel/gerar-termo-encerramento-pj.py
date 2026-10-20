# -*- coding: utf-8 -*-
"""Termo de encerramento de prestação de serviços — PJ. Uma folha A4.

Modelo reaproveitável: trocar o bloco DADOS e gerar de novo. O documento é
editado AQUI, nunca no HTML final.

    python3 painel/gerar-termo-encerramento-pj.py > painel/termo-encerramento-pj.html
"""

DADOS = dict(
    nome      = 'Luiz Eustáquio Barbosa Junior',
    cpf       = '136.576.126-61',
    cnpj      = '69.124.960/0001-60',
    funcao    = '',                       # em branco: preencher à mão
    inicio    = '14/09/2026',
    fim       = '09/10/2026',
    cidade    = 'Belo Horizonte',
    uf        = 'MG',
    emissao   = '20 de outubro de 2026',
)

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:14mm 15mm 12mm; display:flex; flex-direction:column;
  page-break-after:always; overflow:hidden }
.sheet:last-child{ page-break-after:auto }
@media print{ body{ background:#fff } .sheet{ margin:0 } }

.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:6px; margin-bottom:12px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:26px; font-weight:700;
  color:var(--navy); letter-spacing:.5px; line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7.5px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-top:3px }
.doc{ text-align:right }
.doc .m{ font-size:8px; color:var(--muted); letter-spacing:.4px }

h1{ font-family:'Cormorant Garamond',serif; font-size:24px; font-weight:600; color:var(--navy);
  text-align:center; margin:4px 0 2px; letter-spacing:.3px }
.sub{ text-align:center; font-size:8.5px; color:var(--muted); letter-spacing:1.6px;
  text-transform:uppercase; margin-bottom:13px }

.faixa{ background:var(--navy); color:var(--goldsoft); font-size:8.5px; font-weight:600;
  letter-spacing:2px; text-transform:uppercase; padding:5px 10px; margin:12px 0 7px; border-radius:2px }

.parte{ border:1px solid var(--linha); border-left:3px solid var(--gold); border-radius:2px;
  padding:9px 12px; margin-bottom:7px; font-size:10px; line-height:1.55 }
.parte .rot{ font-size:7px; letter-spacing:1.6px; text-transform:uppercase; color:var(--gold);
  font-weight:700; display:block; margin-bottom:2px }
.parte b{ color:var(--navy) }
.mono{ font-family:'JetBrains Mono',monospace; font-size:9.5px }
.vazio{ display:inline-block; min-width:150px; border-bottom:1px dotted #b6bfc9 }

.cl{ font-size:10px; line-height:1.6; margin-bottom:9px; text-align:justify }
.cl .t{ font-weight:700; color:var(--navy) }

.destaque{ background:var(--goldbg); border-left:3px solid var(--gold); border-radius:2px;
  padding:9px 12px; font-size:10px; line-height:1.6; text-align:justify; margin-bottom:9px }

.local{ font-size:10px; margin:14px 0 0; text-align:center; color:var(--ink) }

.assina{ display:grid; grid-template-columns:1fr 1fr; gap:26px; margin-top:auto; padding-top:6px }
.assina > div{ border-top:1px solid var(--ink); padding-top:4px; text-align:center }
.assina .n{ font-size:9px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:8px; color:var(--muted); margin-top:1px }
.test{ display:grid; grid-template-columns:1fr 1fr; gap:26px; margin-top:16px }
.test > div{ border-top:1px solid var(--linha); padding-top:4px; font-size:8px; color:var(--muted) }

.rodape{ margin-top:14px; border-top:1px solid var(--linha); padding-top:5px;
  display:flex; justify-content:space-between; font-size:7px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

D = DADOS
FUNCAO = D['funcao'] if D['funcao'] else '<span class="vazio">&nbsp;</span>'

print('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Termo de encerramento de prestação de serviços — __NOME__</title>
__FONTES__
<style>__CSS__</style>
</head>
<body>

<div class="sheet">
  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><div class="m">Vargas Decor Ltda · CNPJ 17.269.304/0001-51<br>
      Rua Silva Freire, 322 · Belo Horizonte / MG</div></div>
  </div>

  <h1>Termo de Encerramento de Prestação de Serviços</h1>
  <div class="sub">Contrato entre pessoas jurídicas · distrato amigável</div>

  <div class="faixa">Das partes</div>

  <div class="parte"><span class="rot">Contratante</span>
    <b>VARGAS DECOR LTDA</b>, nome fantasia <b>Valvic Marcenaria</b>, pessoa jurídica de direito
    privado inscrita no CNPJ sob o nº <span class="mono">17.269.304/0001-51</span>, com sede na
    Rua Silva Freire, 322, Belo Horizonte / MG, neste ato representada na forma de seus atos
    constitutivos.</div>

  <div class="parte"><span class="rot">Prestador</span>
    <b>__NOME__</b>, inscrito no CPF sob o nº <span class="mono">__CPF__</span>, responsável pela
    pessoa jurídica inscrita no CNPJ sob o nº <span class="mono">__CNPJ__</span>, que prestou
    serviços de __FUNCAO__ à CONTRATANTE.</div>

  <div class="faixa">Do objeto</div>

  <div class="destaque">As partes, de comum acordo e sem qualquer litígio entre si, firmam o
  presente termo para dar por <b>encerrada a prestação de serviços</b> havida no período de
  <b>__INICIO__ a __FIM__</b>, nos termos e condições abaixo.</div>

  <div class="cl"><span class="t">Cláusula 1ª — Do encerramento.</span> Fica encerrada, em
  <b>__FIM__</b>, por mútuo acordo, a prestação de serviços iniciada em <b>__INICIO__</b>, sem ônus,
  multa ou penalidade de qualquer natureza para qualquer das partes.</div>

  <div class="cl"><span class="t">Cláusula 2ª — Da quitação.</span> O PRESTADOR declara haver
  <b>recebido integralmente</b> a remuneração ajustada por todos os serviços prestados no período
  de __INICIO__ a __FIM__, nada mais tendo a receber ou a reclamar da CONTRATANTE a qualquer
  título, momento ou fundamento, outorgando-lhe, neste ato, <b>plena, geral, rasa e irrevogável
  quitação</b> quanto ao objeto deste termo.</div>

  <div class="cl"><span class="t">Cláusula 3ª — Da natureza da relação.</span> As partes declaram
  que a relação mantida foi de <b>prestação de serviços entre pessoas jurídicas</b>, executada com
  autonomia técnica e sem subordinação, pessoalidade ou habitualidade, não se estabelecendo entre
  elas qualquer vínculo empregatício, societário ou de representação, razão pela qual <b>não são
  devidas verbas de natureza trabalhista</b> de espécie alguma.</div>

  <div class="cl"><span class="t">Cláusula 4ª — Da devolução.</span> O PRESTADOR declara haver
  devolvido à CONTRATANTE todos os bens, ferramentas, equipamentos, materiais, chaves, documentos
  e acessos a sistemas que estiveram sob sua guarda em razão da prestação, nada retendo em seu
  poder.</div>

  <div class="cl"><span class="t">Cláusula 5ª — Do sigilo e da propriedade intelectual.</span>
  Permanecem em vigor, por prazo indeterminado, as obrigações de <b>sigilo</b> sobre informações de
  clientes, projetos, processos produtivos, preços, custos e fornecedores da CONTRATANTE. Projetos,
  desenhos, medidas e soluções técnicas desenvolvidos durante a prestação pertencem
  <b>exclusivamente à CONTRATANTE</b>.</div>

  <div class="cl"><span class="t">Cláusula 6ª — Do foro.</span> Fica eleito o foro da Comarca de
  __CIDADE__ / __UF__ para dirimir quaisquer questões oriundas deste termo, com renúncia a
  qualquer outro, por mais privilegiado que seja.</div>

  <div class="cl">E, por estarem assim justas e acordadas, as partes firmam o presente termo em
  duas vias de igual teor e forma, na presença das testemunhas abaixo.</div>

  <div class="local">__CIDADE__ / __UF__, __EMISSAO__.</div>

  <div class="assina">
    <div><div class="n">__NOME__</div>
      <div class="s">Prestador · CPF __CPF__ · CNPJ __CNPJ__</div></div>
    <div><div class="n">Vargas Decor Ltda — Valvic Marcenaria</div>
      <div class="s">Contratante · CNPJ 17.269.304/0001-51</div></div>
  </div>

  <div class="test">
    <div>Testemunha 1 · nome ______________________________ CPF ______________________</div>
    <div>Testemunha 2 · nome ______________________________ CPF ______________________</div>
  </div>

  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Termo de encerramento · PJ · __FIM__</span></div>
</div>

</body>
</html>'''
  .replace('__CSS__', CSS).replace('__NOME__', D['nome']).replace('__CPF__', D['cpf'])
  .replace('__CNPJ__', D['cnpj']).replace('__FUNCAO__', FUNCAO)
  .replace('__INICIO__', D['inicio']).replace('__FIM__', D['fim'])
  .replace('__CIDADE__', D['cidade']).replace('__UF__', D['uf'])
  .replace('__EMISSAO__', D['emissao']))
