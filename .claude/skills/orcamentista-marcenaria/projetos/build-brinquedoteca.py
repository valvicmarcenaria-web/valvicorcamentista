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
DATA, PRAZO, VALIDADE, GARANTIA = '30 de setembro de 2026', '90 dias corridos', '10 dias', '10 anos'
NP = 4
img = lambda n: f'img-brinquedoteca/{n}.jpg'
CSS = open(P/'css-brinquedoteca.css', encoding='utf-8').read()

# nome e descrição de proposta — sem medida, sem contagem
CONJ = [
 ('Passarela suspensa', 'Estrutura em aço, piso em compensado naval e pintura automotiva.'),
 ('Gradis de contenção', 'Quadro metálico com corda combinada de alma em aço, com a rede do mezanino e as telas de proteção.'),
 ('Plataformas acolchoadas', 'Degraus estruturados, espuma de alta densidade e courvin náutico.'),
 ('Piscina de espuma', 'Estrutura de contenção, fundo e paredes acolchoados.'),
 ('Banco extenso', 'Estrutura em aço com assento acolchoado em courvin náutico.'),
 ('Parede de desenho', 'Painel em laminado branco, para escrever e apagar.'),
 ('Parede estrutural principal', 'Estrutura em aço e MDF ultra premium cru, pronto para o acabamento.'),
 ('Casinha — paredes', 'Fachada e laterais em MDF ultra premium cru, dupla face.'),
 ('Casinha — escada', 'Estrutura em aço com degraus forrados e pintura automotiva.'),
 ('Janelas e pórticos moldurados', 'Estilo veneziana em usinagem plana, com frisos, em laca branca.'),
 ('Escorregador com túnel curvo', 'Teto em arco sobre gabarito, pista em laminado e gradil de proteção.'),
 ('Cozinha de brinquedo', 'Módulo lúdico sob medida, em MDF ultra premium cru.'),
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
  <p class="txt">São ofícios distintos no mesmo contrato — serralheria, marcenaria,
  estofaria e pintura automotiva — sob um único responsável. A
  Valvic desenha, fabrica, pinta, estofa e instala com equipe própria.</p>

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

# ── 3 · os conjuntos e o investimento ────────────────────────────────────
linhas = ''
for k, ((nome, desc), chave) in enumerate(zip(CONJ, NOMES), 1):
    linhas += (f'<div class="cj"><div class="n">{k:02d}</div>'
               f'<div><div class="t">{nome}</div><div class="d">{desc}</div></div>'
               f'<div class="v">R$ {br(oq.PV[chave])}</div></div>')

p3 = f"""<div class="pg"><div class="in">
  <div class="sel">Os conjuntos</div>
  <h1 class="ttl disp">Peça a peça,<br><em>uma só obra.</em></h1>
  <div class="hair"></div>
  {linhas}
  <div class="cj tot"><div class="n"></div>
    <div><div class="t">Investimento total</div></div>
    <div class="v disp">R$ {br(oq.TOT)}</div></div>
  {pe(3)}
</div></div>"""

# ── 4 · condições ────────────────────────────────────────────────────────
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

  <div class="ph sangra" style="margin-top:12mm;height:78mm;">
    <img src="{img('mezanino')}" alt=""></div>

  <div class="obs">Tudo é fabricado, pintado, estofado e instalado por <b>equipe
  própria</b>. Acompanham o fornecimento: projeto executivo, estrutura
  metálica, chapas, espumas, courvin, cordas, <b>a rede do mezanino</b>,
  <b>as telas de proteção</b>, laca das janelas, pintura automotiva,
  transporte e montagem. <b>Não acompanham:</b> o acabamento das paredes e o
  efeito de tijolinho, os blocos da piscina, obra civil, elétrica, piso e
  revestimentos. Medidas
  conferidas no local antes da fabricação.</div>
  {pe(4)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;'
        '9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'
        '<style>' + CSS + '</style></head><body>' + p1 + p2 + p3 + p4 + '</body></html>')

(P/'proposta-brinquedoteca.html').write_text(HTML, encoding='utf-8')
tmp = HTML.replace('src="img-brinquedoteca/', f'src="file://{P}/img-brinquedoteca/')
open('/tmp/in.html', 'w', encoding='utf-8').write(tmp)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-brinquedoteca.pdf')], check=True, env=env)
print(f'proposta-brinquedoteca.pdf · {NP} páginas · R$ {br(oq.TOT)}')
