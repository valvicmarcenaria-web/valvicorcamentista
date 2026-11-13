# -*- coding: utf-8 -*-
"""ATTOS · COSTA LAGUNA — CRONOGRAMA DO ESCRITÓRIO, EM UMA PÁGINA  [10/11/2026]

⭐ [Jonathan, 10/11/2026] "vamos criar a o mesmo projeção de cronograma para o
   escritório do projeto do attos que precisa ser entregue até dia 10/12".
⭐ É a mesma folha do escopo de venda do Orlando e Ivone, com o mesmo visual
   (o CSS é lido de `build-orlando-ivone-escopo.py`).
⭐ A fonte é o `Valvic_Escopo_Venda_Attos.pdf` do Drive (06/11/2026):
   · "O escritório é contratual para 10/12/2026, instalado. Não entra na fila
     dos 70 dias — produção, carga e instalação precisam de janela própria";
   · a divergência entre o render e o executivo neste ambiente;
   · a bancada que avança em mesa com apoio metálico (a pedra é de terceiro, o
     apoio é nosso);
   · medição até 7 dias corridos após a assinatura de 06/11/2026.
   E `attos-costa-laguna/_HALL-ESCRITORIO.md`, a leitura do executivo Rev. 03.
⭐ Documento INTERNO, para a gestão e a produção: não leva preço.
⛔ [Jonathan, 10/11/2026] "não trabalhamos mais com a hettich sensys, no projeto do
   Attos será a novisys" — a dobradiça é a Hettich NOVISYS.
"""
import pathlib, subprocess, os, re, html

P = pathlib.Path(__file__).resolve().parent
E = lambda t: html.escape(str(t))
CSS = re.search(r'CSS = """(.*?)"""', (P / 'build-orlando-ivone-escopo.py').read_text(encoding='utf-8'),
                re.S).group(1)

CLIENTE = 'Attos Henrique Salles'
OBRA = 'Costa Laguna · Alphaville, Nova Lima'
PROJETO = 'Executivo Costa Laguna ATTOS · Rev. 03'
LOCAL = 'Attos Henrique Salles · Costa Laguna · escritório'
RODAPE = 'CRONOGRAMA · ESCRITÓRIO · COSTA LAGUNA · ATTOS'
ENTREGA = '10/12/2026'

CARDS = [
 ('Medição técnica', 'Até 13/11/2026'),
 ('Linha contratada', 'Hettich · corrediça oculta com Silent System · dobradiça Novisys'),
 ('Garantia', '10 anos marcenaria e ferragem · 2 anos instalação · LED pelo fabricante'),
]
ITENS = [
 ('ESCRITÓRIO', 'Painel ripado de fundo',
  'Parede inteira do fundo, na mesma cadência da casa · base contínua onde os armários se fixam'),
 ('ESCRITÓRIO', 'Armário superior, bancada e armário inferior',
  'Armário superior suspenso, de portas de giro · bancada corre sobre o armário e avança em mesa, '
  'com apoio metálico na ponta · armário inferior com portas e gaveteiro'),
]
# ⭐ o cronograma: a previsão de cada etapa é preenchida à mão pela gestão
ETAPAS = [
 ('Definições informacionais', 'Cores e render × executivo resolvido'),
 ('Programação', 'Executivo de marcenaria aprovado e plano de corte'),
 ('Usinagem', 'Corte, fita de borda, ripas e usinagem'),
 ('Pré-montagem', 'Armários montados e regulados, ripado em painéis'),
 ('Conferência', 'Conferência contra o escopo · embalagem e carga'),
 ('Início de montagem', 'Equipe na obra, com pontos elétricos prontos'),
]
FERRAGENS = [('Corrediças', 'Hettich'), ('Dobradiças', 'Hettich Novisys')]
ESTRUTURA = ('Caixaria 15 mm, fundos 6 mm, frentes em 18 mm · <b>o apoio metálico da mesa é nosso</b>')
ATENCAO = ('<b>Fora da fila dos 70 dias</b> da casa: produção, carga e instalação com <b>janela '
           'própria</b>. O render e o executivo <b>não batem</b> aqui: resolver antes de detalhar.')
DEFINIR = [
 ('Cores e padrões de MDF', '<b>Definir as cores com o cliente</b> antes de comprar chapa.'),
 ('Render × executivo', 'Resolver a divergência entre o 3D e o projeto técnico <b>antes de detalhar</b>.'),
 # ⭐ [Jonathan, 13/11/2026] marmoraria eliminada
 ('Apoio metálico da mesa', 'Desenhar o <b>apoio metálico estrutural</b> da ponta da mesa.'),
]

BOX = '<span class="box"></span>'
DATA_V = '___/___/______'
cards = ''.join(f'<div><div class="k">{E(k)}</div><div class="v">{E(v)}</div></div>' for k, v in CARDS)
itens = ''.join(f'<tr><td class="amb">{E(a)}</td><td class="it">{E(i)}</td><td class="sp">{E(s)}</td>'
                f'<td class="ok">{BOX}</td></tr>' for a, i, s in ITENS)
crono = ''.join(f'<tr><td class="n">{n:02d}</td><td class="it">{E(k)}</td><td class="sp">{E(d)}</td>'
                f'<td class="dt">{DATA_V}</td><td class="dt">{DATA_V}</td><td class="ok">{BOX}</td></tr>'
                for n, (k, d) in enumerate(ETAPAS, 1))
crono += (f'<tr class="fim"><td class="n">{len(ETAPAS) + 1:02d}</td><td class="it">Entrega no cliente</td>'
          f'<td class="sp">Escritório instalado e conferido</td>'
          f'<td class="dt dd">{ENTREGA}</td><td class="dt">{DATA_V}</td><td class="ok">{BOX}</td></tr>')
fer = ''.join(f'<div><div class="k">{E(k)}</div><div class="v">{E(v)}</div></div>' for k, v in FERRAGENS)
defs = ''.join(f'<tr><td class="ok">{BOX}</td><td class="it">{E(k)}</td><td class="sp">{d}</td>'
               f'<td class="def">……………………</td></tr>' for k, d in DEFINIR)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Cronograma · Escritório · {E(CLIENTE)}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="page">
 <div class="hd"><div class="lg">valvic<small>MARCENARIA</small></div>
  <div class="r"><div class="t">Cronograma · Escritório</div><div class="s">{E(LOCAL)} · folha 1 de 1</div></div></div>

 <div class="cards">
  <div><div class="k">Cliente</div><div class="v">{E(CLIENTE)}</div></div>
  <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
  <div><div class="k">Projeto</div><div class="v">{E(PROJETO)}</div></div>
  <div><div class="k">Escopo</div><div class="v">Escritório · {len(ITENS)} itens · sai à frente da casa</div></div>
 </div>

 <div class="prazo"><div><div class="k">Escritório instalado · contratual</div>
   <div class="d">{ENTREGA}</div></div>
  <div class="t">É a data do <b>escritório instalado e conferido</b>, independente do prazo da casa.
   A previsão de cada etapa abaixo tem de caber antes dela.</div></div>

 <div class="info">{cards}</div>

 <div class="sec">1 · <b>Os {len(ITENS)} itens do escritório</b>, como contratados</div>
 <table><tr><th>Ambiente</th><th>Item</th><th>Especificação</th><th class="ok">OK</th></tr>{itens}</table>

 <div class="sec">2 · <b>Cronograma de etapas</b> · previsão de entrega de cada etapa</div>
 <table class="cr"><colgroup><col style="width:8mm"><col style="width:38mm"><col><col style="width:23mm">
  <col style="width:23mm"><col style="width:8mm"></colgroup><tr><th>Nº</th><th>Etapa</th>
  <th>O que fecha a etapa</th><th class="dt">Previsão</th><th class="dt">Realizado</th><th class="ok">✓</th></tr>{crono}</table>

 <div class="sec">3 · Ferragens que serão utilizadas e estrutura</div>
 <div class="fer">{fer}</div>
 <div class="bl"><span class="h">Estrutura e chapas.</span> {ESTRUTURA}</div>
 <div class="at"><div class="e">Ponto de atenção</div><div>{ATENCAO}</div></div>

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
for _c in ('Orlando', 'Ivone', 'Haverson', 'Ana Carolina', 'Alexandre', 'Gisele', 'Gustavo', 'Phillip'):
    assert _c not in _t, f'⛔ vestígio de outro cliente: {_c}'
assert 'R$' not in _t, '⛔ o cronograma não leva preço'
assert 'pedra' not in _t.lower() and 'marmoraria' not in _t.lower(), '⛔ marmoraria eliminada [Jonathan, 13/11/2026]'
assert 'nada corta' not in _t, '⛔ "nunca precisa dizer isso: nada corta antes" [Jonathan, 11/11/2026]'
assert 'Sensys' not in _t and 'Novisys' in _t, '⛔ a dobradiça do Attos é a Novisys [Jonathan, 10/11/2026]'
assert not [c for c in '⭐⛔⚠' if c in _t], '⛔ marcação interna'
assert all(e in _t for e, _d in ETAPAS) and ENTREGA in _t

R = P / 'attos-costa-laguna'
OUT = R / 'cronograma-escritorio-attos.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'Valvic_Cronograma_Escritorio_Attos.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDF)], capture_output=True,
                                                       text=True).stdout).group(1))
assert npg == 1, f'⛔ o cronograma tem de caber em uma página: saiu com {npg}'
print(f'{PDF.name} · 1 folha · {len(ITENS)} itens · {len(ETAPAS) + 1} etapas · entrega {ENTREGA}')
