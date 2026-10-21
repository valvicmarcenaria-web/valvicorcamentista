# -*- coding: utf-8 -*-
"""PROPOSTA — BRINQUEDOTECA · Eliza e Luiz Gustavo  [30/09/2026]

[Jonathan] "linda, única, minimalista, exclusiva, padrão único."

CSS próprio (`css-brinquedoteca.css`), não o das propostas de marcenaria:
verde do projeto, tipografia display leve, sem caixa e sem borda grossa.

⛔⛔ SEM METRAGEM NEM QUANTITATIVO (referencias/proposta-comercial.md).
⛔ Classes com sufixo próprio — .cj .esc2 .pe2 — para não colidir.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('v2', P/'orcamento-brinquedoteca-v2.py')
oq = importlib.util.module_from_spec(spec); sys.modules['v2'] = oq
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(oq)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, PROJETO = 'Eliza e Luiz Gustavo', 'Helena Antunes Arquitetura e Interiores'
DATA, PRAZO, VALIDADE, GARANTIA = '21 de outubro de 2026', '90 dias corridos', '10 dias', '10 anos'
NP = 5
img = lambda n: f'img-brinquedoteca/{n}.jpg'
CSS = open(P/'css-brinquedoteca.css', encoding='utf-8').read()

# nome e descrição de proposta — sem medida, sem contagem
CONJ = [
 ('Passarela suspensa',
  'Estrutura em aço com pintura automotiva.'),
 ('Gradis de contenção',
  'Corda de alma em aço e <b>malha de corda náutica com cabo de aço '
  'entrelaçado</b>, dupla na estrutura suspensa. Inclui a rede do mezanino.'),
 ('Plataformas acolchoadas',
  'Degraus estruturados, <b>espuma de alta densidade</b> e revestimento '
  'em tecido.'),
 ('Piscina de espuma',
  'Estrutura de contenção, fundo e paredes acolchoados, com o <b>painel de '
  'guarda-corpo</b> acolchoado.'),
 ('Banco extenso',
  'Estrutura em aço com assento acolchoado e fechamento aparente em '
  '<b>MDF Berneck, padrão Tabasco</b>.'),
 ('Parede norte',
  'Estrutura em aço e MDF ultra premium cru, pronto para o efeito tijolinho.'),
 ('Casinha — paredes',
  'Fachada e laterais em MDF ultra premium cru, dupla face.'),
 ('Casinha — escada',
  'MDF ultra premium, com os degraus em revestimento emborrachado.'),
 ('Janelas e pórticos moldurados',
  'Estilo veneziana em usinagem plana, com frisos, em laca branca.'),
 ('Escorregador com túnel curvo',
  'Teto em arco sobre gabarito, pista em laminado e gradil de proteção.'),
 ('Pintura ou papel de parede — aplicação',
  '<b>Mão de obra</b> da pintura acrílica dos painéis, por dentro e por '
  'fora, <b>ou</b> da aplicação de vinil adesivo e papel na torre. '
  '<b>O material é fornecido pela cliente.</b>'),
 ('Cozinha de brinquedo',
  'Módulo lúdico sob medida, em MDF ultra premium cru.'),
]
NOMES = [i['nome'] for i in oq.ITENS]
assert len(CONJ) == len(NOMES), (len(CONJ), len(NOMES))

def pe(n):
    return (f'<div class="pe2"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · Brinquedoteca</span><span>{n} / {NP}</span></div>')

# ── 1 · capa ─────────────────────────────────────────────────────────────
p1 = f"""<div class="pg cv"><div class="in">
  <div class="ph"><img src="{img('capa')}" alt=""></div>
  <div class="pe">
    <div class="sel">Proposta · Brinquedoteca</div>
    <div class="nm disp">Eliza<br>&amp; Luiz Gustavo</div>
    <div class="sub">Uma pequena rua construída dentro de casa — para subir,
    escalar, escorregar e se esconder. Projeto {PROJETO}.</div>
  </div>
</div></div>"""

# ── 2 · o conceito ───────────────────────────────────────────────────────
p2 = f"""<div class="pg"><div class="in">
  <div class="sel">O que vamos construir</div>
  <h1 class="ttl disp">Não é um móvel.<br><em>É um lugar.</em></h1>
  <div class="hair"></div>
  <p class="txt">Uma brinquedoteca não se resolve com marcenaria. O que
  sustenta uma criança lá no alto é <b>aço</b>; o que a
  protege quando ela erra é <b>espuma na densidade certa</b>; e o que faz a
  casinha parecer uma casa de verdade é <b>usinagem peça a peça</b>.</p>
  <p class="txt">São <b>ofícios distintos no mesmo contrato</b> — serralheria,
  marcenaria, estofaria, pintura automotiva e instalação — e insumos que não
  se compram no mesmo lugar: perfil de aço, corda de alma de aço, espuma em
  densidades diferentes, MDF ultra premium, laca, tecido e revestimento
  emborrachado.</p>
  <p class="txt">Contratados em separado, <b>cada um responde pelo seu pedaço
  e ninguém responde pelo conjunto</b> — e é no encontro entre eles que a
  obra para. Aqui é um fornecedor só: <b>um cronograma, uma medição, uma
  garantia</b>.</p>
  <p class="txt"><b>É por isso que a Valvic não se apresenta como uma
  marcenaria.</b> Somos uma empresa que <b>articula soluções</b>: quem
  dimensiona o aço, quem escolhe a densidade da espuma, quem tece a malha
  de corda, quem usina a curva e quem instala <b>respondem ao mesmo
  projeto e ao mesmo contrato</b>. A marcenaria é uma das mãos — não é o
  limite do que entregamos.</p>

  <div class="ph sangra" style="margin-top:10mm;height:96mm;">
    <img src="{img('geral')}" alt=""></div>

  <div class="gr">
    <div><div class="k">Estrutura</div><div class="v">Perfil de aço
      dimensionado por peça, <b>pintura automotiva</b> em cabine — a mesma
      que se aplica em carroceria.</div></div>
    <div><div class="k">Amortecimento</div><div class="v">Cada uso pede uma
      espuma: a que <b>afunda</b> na piscina, a que <b>sustenta</b> no
      degrau, a que <b>absorve</b> na parede.</div></div>
    <div><div class="k">Superfície</div><div class="v"><b>MDF ultra premium
      cru</b>, plano e alinhado — entregue pronto para o acabamento que a
      cliente escolher.</div></div>
    <div><div class="k">Acabamento nosso</div><div class="v">Janelas e
      pórticos saem <b>em laca branca</b>, com friso e usinagem
      plana no estilo veneziana.</div></div>
  </div>
  {pe(2)}
</div></div>"""

# ── 3 · como isso se sustenta + a referencia de acabamento ──────────────
pENG = f"""<div class="pg"><div class="in">
  <div class="sel">Como isso se sustenta</div>
  <h1 class="ttl disp">O que segura<br><em>uma criança no alto.</em></h1>
  <div class="hair"></div>

  <div class="eng">
    <div class="r"><div class="k">Infraestrutura</div>
      <div class="d">As paredes sobem sobre <b>metalon 50 × 30 em chapa
      16</b>. É uma <b>chapa mais grossa</b> do que a de divisória
      comum — escolhida de propósito, por <b>resistência e
      segurança</b>, principalmente onde ficam a <b>ponte suspensa</b> e a
      <b>grade de cordas suspensa</b>. É o que não aparece e é
      o que sustenta.</div></div>
    <div class="r"><div class="k">Malha de corda</div>
      <div class="d">As telas de proteção são <b>malha de corda
      náutica</b> tecida nó a nó, com <b>fios de cabo de aço
      entrelaçados</b> para resistência. Na <b>estrutura suspensa a malha
      é dupla</b>, o que reduz o vão entre os nós pela metade.
      Presa à estrutura por <b>ganchos soldados</b>, não por
      amarração.</div></div>
    <div class="r"><div class="k">Amortecimento</div>
      <div class="d">Nas <b>plataformas de subida</b> e no <b>painel de
      guarda-corpo da piscina</b> entra <b>espuma de alta densidade</b>,
      revestida em <b>tecido a definir com vocês</b>. <b>Couro natural
      não está contemplado</b> neste valor.</div></div>
    <div class="r"><div class="k">Acabamento</div>
      <div class="d">Os painéis entregam <b>crus, planos e alinhados</b>.
      A pintura acrílica e o papel são <b>aplicados por nós</b>
      — e o material vem de vocês.</div></div>
  </div>

  <div class="ref">
    <div class="ph"><img src="{img('tabasco-berneck')}" alt=""></div>
    <div>
      <div class="k">Sugestão de acabamento · banco</div>
      <div class="t disp">Padrão <em>Tabasco</em>,<br>da Berneck.</div>
      <div class="d">Para o <b>fechamento aparente do banco</b>, sugerimos o
      padrão <b>Tabasco da Berneck</b> — a imagem ao lado é
      referência do padrão, não do nosso projeto. É uma cor
      que aguenta o uso de uma brinquedoteca e <b>conversa com o assento
      estofado</b> sem pedir manutenção.</div>
    </div>
  </div>
  {pe(3)}
</div></div>"""

# ── 4 · os conjuntos e o investimento ────────────────────────────────────
linhas = ''
for k, ((nome, desc), chave) in enumerate(zip(CONJ, NOMES), 1):
    linhas += (f'<div class="cj"><div class="n">{k:02d}</div>'
               f'<div><div class="t">{nome}</div><div class="d">{desc}</div></div>'
               f'<div class="v">R$ {br(oq.PV[chave])}</div></div>')

p3 = f"""<div class="pg"><div class="in" style="padding-top:15mm;">
  <div class="sel">Os conjuntos</div>
  <h1 class="ttl disp">Peça a peça,<br><em>uma só obra.</em></h1>
  <div class="hair"></div>
  {linhas}
  <div class="cj tot"><div class="n"></div>
    <div><div class="t">Investimento total</div></div>
    <div class="v disp">R$ {br(oq.TOT)}</div></div>
  {pe(4)}
</div></div>"""

# ── 5 · condições ────────────────────────────────────────────────────────
p4 = f"""<div class="pg"><div class="in">
  <div class="sel">Condições</div>
  <h1 class="ttl disp">Como acontece.</h1>
  <div class="hair"></div>

  <div class="esc2">
    <div class="l"><span class="p disp">40%</span><span class="q">na assinatura — libera a compra do aço, da espuma e das chapas</span></div>
    <div class="l"><span class="p disp">30%</span><span class="q">no início da montagem no local</span></div>
    <div class="l"><span class="p disp">30%</span><span class="q">na entrega, com tudo montado e conferido</span></div>
  </div>

  <div class="gr" style="margin-top:11mm;grid-template-columns:1fr 1fr 1fr;">
    <div><div class="k">Prazo</div><div class="v"><b>{PRAZO}</b>, contados da
      assinatura, do pagamento da entrada e da conferência de medidas no
      local.</div></div>
    <div><div class="k">Garantia</div><div class="v"><b>{GARANTIA}</b> sobre
      estrutura, solda e ferragens — termo da Valvic sobre o conjunto que
      fabricamos e instalamos.</div></div>
    <div><div class="k">Validade</div><div class="v"><b>{VALIDADE}</b> a
      partir desta data.</div></div>
  </div>

  <div class="obs">Tudo é fabricado, pintado, estofado e instalado por
  <b>equipe própria</b>. Acompanham o fornecimento: projeto executivo,
  estrutura metálica em <b>chapa 16</b>, chapas, espumas, tecidos,
  cordas, <b>a malha de corda náutica</b>, <b>a rede do mezanino</b>, laca
  das janelas, pintura automotiva, transporte e montagem.
  <b>É mão de obra nossa e material de vocês:</b> a
  <b>pintura acrílica</b> dos painéis e o <b>papel de parede</b> da torre
  — aplicamos, e a tinta, a massa e o papel são fornecidos pela
  cliente. <b>Não acompanham:</b> o efeito de tijolinho, os blocos da
  piscina, <b>couro natural</b> no revestimento, obra civil, elétrica, piso
  e revestimentos. O <b>tecido dos acolchoados</b> ainda será definido com
  vocês. Medidas conferidas no local antes da fabricação.</div>
  {pe(5)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;'
        '9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'
        '<style>' + CSS + '</style></head><body>' + p1 + p2 + pENG + p3 + p4 + '</body></html>')

(P/'proposta-brinquedoteca.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-brinquedoteca/', f'src="file://{P}/img-brinquedoteca/')
open('/tmp/in.html', 'w', encoding='utf-8').write(tmp)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-brinquedoteca.pdf')], check=True, env=env)
print(f'proposta-brinquedoteca.pdf · {NP} páginas · R$ {br(oq.TOT)}')
