# -*- coding: utf-8 -*-
"""NÁDIA E MAURÍLIO — MEMORIAL DESCRITIVO PARA VALIDAÇÃO.

Documento técnico, simples, para a cliente conferir item a item e dar o aceite
final. NÃO é o folder comercial — aquele é `build-nadia-premium.py`.

[Jonathan 11/08/2026, 3ª rodada]
  · ACRÉSCIMO: cristaleira ao lado da torre da geladeira, 2 portas em vidro
    REFLECTA BRONZE (o Jonathan escreveu "fumê" e corrigiu em seguida)
  · RETORNA o painel de TV ao projeto
  · CLOSET 100% em MDF GIANDUIA TRAMA
  · detalhes amadeirados da COZINHA em MDF ITAPUÃ
  · LED da marcenaria é fornecimento NOSSO
  · valor R$ 112.500 · pagamento conforme a proposta (20 · 20 · 20 · 40)

⚠️ O ESCOPO CRESCEU E O PREÇO NÃO. Ver `2026-nadia-maurilio.md`:
   tabela dos 7 conjuntos ............ 127.850
   + painel de TV (volta) ............   2.250  →  130.100
   + cristaleira nova ................  não orçada
   + closet Areia → Gianduia Trama ...  delta não orçado
   preço .............................  112.500
   O desconto efetivo sai de 12% para 13,5% só com o painel de TV.

[Jonathan 11/08, 4ª rodada] O MDF AREIA SAI DO PROJETO INTEIRO:
  · lavanderia inferior — Gianduia Trama interno e externo · SAI um módulo aéreo,
    ENTRA um gaveteiro com 3 gavetas internas, puxadores espaçados
  · lavanderia superior — idem
  · hall dos dormitórios — Gianduia Trama
  · cozinha — no lugar do Areia, Gianduia Trama
  Resultado: acabamento ÚNICO em Gianduia Trama, com Itapuã só nos amadeirados.
  ⚠️ Preço mantido em R$ 112.500. É a terceira rodada de acréscimo com o preço
     congelado, e a maior delas: a troca de chapa agora vale para os ~R$ 93.400
     de tabela que ainda estavam em Areia. NÃO TENHO O PREÇO DE COMPRA DA
     GIANDUIA TRAMA na base — precisa cotar antes de assinar.

[Jonathan 11/08, 5ª rodada] prateleiras da Cristaleira 2 em MDF (não vidro) ·
  TODOS os fundos com duplo revestimento (era só lavanderia) · confirma que não há
  MDF Areia no projeto · REMOVIDO o bloco de aceite com assinatura.

⚠️ A largura da cristaleira nova não foi informada. O memorial declara
   "largura a confirmar na medição" — que é justamente o papel deste documento.
"""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

TOTAL = 112500
PARC  = [('1ª — no fechamento',              20, 22500),
         ('2ª — 60 dias após o fechamento',  20, 22500),
         ('3ª — no início das montagens',    20, 22500),
         ('4ª — na entrega final',           40, 45000)]
assert sum(v for _, _, v in PARC) == TOTAL

def br(v): return f'{v:,.0f}'.replace(',', '.')

# ── escopo: ambiente → conjuntos ───────────────────────────────────────────
AMBIENTES = [
 ('Lavanderia do térreo', 'Pavimento inferior', [
   ('Armário da lavanderia <span class="alt">alterado</span>',
    '<b>MDF Gianduia Trama, interno e externo.</b>',
    '<b>Sai um módulo aéreo</b> e entra um <b>gaveteiro com 3 gavetas internas</b>, '
    'com puxadores espaçados. Demais puxadores inferiores em cava e superiores '
    'passantes.'),
 ]),
 ('Lavanderia superior', 'Pavimento superior', [
   ('Armário da lavanderia <span class="alt">alterado</span>',
    '<b>MDF Gianduia Trama, interno e externo.</b>',
    'Mesma especificação da lavanderia do térreo, ponto a ponto — inclusive a troca '
    'do módulo aéreo pelo <b>gaveteiro de 3 gavetas internas</b> com puxadores '
    'espaçados e a linha de ferragem.'),
 ]),
 ('Hall dos dormitórios', 'Corredor', [
   ('Armário do corredor',
    '<b>MDF Gianduia Trama</b>, interno e externo.',
    'Portas de <b>espelho prata</b> em esquadria de <b>alumínio</b>. As portas correm '
    'no sistema da própria esquadria — <b>é o único conjunto sem ferragem Blum</b>, '
    'por construção.'),
 ]),
 ('Cozinha', 'Cinco conjuntos', [
   ('Ilha e torre das geladeiras',
    'Estrutura interna e externa em <b>MDF Gianduia Trama</b>.',
    '<b>Ilha de 2,80 m.</b> Puxadores em cava com perfil. Gavetas em '
    '<b>Blum TANDEM com BLUMOTION</b>.'),
   ('Cristaleira 1 — 80 cm',
    'Cores conforme projeto.',
    '<b>3 portas em vidro reflecta bronze</b> com esquadria de alumínio bronze. '
    'Prateleiras em vidro incolor temperado de 8 mm. Puxadores em cava com perfil. '
    'Iluminação de LED.'),
   ('Cristaleira 2 — ao lado da torre da geladeira <span class="novo">acréscimo</span>',
    'Cores conforme projeto, no mesmo padrão da Cristaleira 1.',
    '<b>2 portas em vidro reflecta bronze</b> com esquadria de alumínio bronze. '
    '<b>Prateleiras em MDF</b>, no mesmo acabamento do móvel. Iluminação de LED. '
    '<b class="conf">Largura a confirmar na medição.</b>'),
   ('Bancada — aéreos e inferiores',
    'Estrutura e externos em <b>MDF Gianduia Trama</b>. Básculas com '
    '<b>detalhe amadeirado em MDF Itapuã</b>, interno e externo.',
    'Puxadores inferiores em cava com <b>perfil Rometal RM280</b> e superiores '
    'passantes. Básculas em <b>Blum AVENTOS HK-S</b>. Gavetas em <b>Blum TANDEM</b>.'),
   ('Painel de TV <span class="novo">retorna ao projeto</span>',
    'Painel em <b>MDF Itapuã</b>.',
    'Iluminação de LED instalada. Sem ferragem móvel.'),
 ]),
 ('Suíte master', 'Closet do casal · versão 2', [
   ('Closet do casal',
    '<b>100% em MDF Gianduia Trama</b> — estrutura, frentes e internos, sem mistura '
    'de acabamento.',
    'Gavetas com puxadores espaçados e <b>Blum TANDEM com BLUMOTION</b>. '
    '<b>Cabideiros metálicos</b> em todos os vãos de pendurar. Sem a cômoda.'),
 ]),
]

def _amb(nome, sub, itens):
    linhas = ''.join(
      f'<tr><td class="it">{a}</td><td class="ac">{b}</td><td class="de">{c}</td></tr>'
      for a, b, c in itens)
    return (f'<div class="amb"><div class="hd"><span class="n">{nome}</span>'
            f'<span class="s">{sub}</span></div>'
            f'<table class="esc"><tr><th>Conjunto</th><th>Acabamento</th>'
            f'<th>Especificação</th></tr>{linhas}</table></div>')

ESCOPO_A = ''.join(_amb(*a) for a in AMBIENTES[:3])   # lavanderias + hall
ESCOPO_B = ''.join(_amb(*a) for a in AMBIENTES[3:])   # cozinha + suíte

ACAB = [
 ('MDF Gianduia Trama',   '<b>Acabamento único de toda a marcenaria</b> — as duas '
                          'lavanderias, o armário do corredor, a cozinha inteira e o '
                          'closet do casal, interno e externo.'),
 ('MDF Itapuã',           'Único contraponto: os <b>detalhes amadeirados</b> — básculas '
                          'da cozinha e painel de TV.'),
 ('Espelho prata',        'Portas do armário do corredor, em esquadria de alumínio.'),
 ('Vidro reflecta bronze','Portas das duas cristaleiras, em esquadria de alumínio bronze.'),
 ('Vidro temperado 8 mm', 'Prateleiras da Cristaleira 1, incolor. A Cristaleira 2 '
                          'leva <b>prateleiras em MDF</b>.'),
]
ESPESS = [
 ('15 mm', 'Caixaria — estrutura interna de todos os conjuntos.'),
 ('18 mm', 'Prateleiras, portas e frentes.'),
 ('6 mm',  'Fundos de <b>todo</b> o mobiliário, <b>todos com duplo revestimento</b> — '
           'as duas faces seladas, e não só a que aparece.'),
 ('0,4 mm','Fita de borda extra fina, em todas as bordas aparentes.'),
]
FERR = [
 ('Blum CLIP top BLUMOTION', 'Portas de giro. Amortecimento no corpo da dobradiça e '
                             'regulagem em três eixos com a porta montada.'),
 ('Blum TANDEM com BLUMOTION', 'Gavetas. Corrediça oculta sob a gaveta, extração total.'),
 ('Blum AVENTOS HK-S',       'Básculas dos aéreos da cozinha. A porta para onde a mão soltar.'),
 ('Esquadria de alumínio',   'Armário do corredor — sistema próprio do perfil, sem Blum.'),
]

def topo(n):
    extra = ('Documento 1 de 1 · páginas 1–4' if n == 1 else f'Página {n}')
    return ('<div class="top">'
            '<div><div class="bl">valvic<i>.</i></div><div class="bs">MARCENARIA</div></div>'
            '<div class="rt"><b>Memorial descritivo para validação</b><br>'
            'Nádia &amp; Maurílio · 11 de agosto de 2026<br>' + extra + '</div></div>')

def rodape(n):
    return ('<div class="foot"><span><b>VALVIC MARCENARIA</b></span>'
            '<span>Memorial para validação · Nádia &amp; Maurílio · 11/08/2026 · '
            f'pág. {n} de 4</span></div>')

def _tb(rows, c1='k'):
    return ''.join(f'<tr><td class="{c1}">{a}</td><td>{b}</td></tr>' for a, b in rows)

linhas_pag = ''.join(
  f'<tr><td>{n}</td><td class="r">{p}%</td><td class="r">R$ {br(v)}</td></tr>'
  for n, p, v in PARC)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@page{{size:A4; margin:0;}}
*{{box-sizing:border-box;}}
html,body{{margin:0; padding:0;}}
body{{font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
      color:#1F1B16; font-size:9.3pt; line-height:1.5; -webkit-print-color-adjust:exact;}}
.page{{width:210mm; height:297mm; padding:15mm 16mm 13mm; position:relative;
       page-break-after:always; overflow:hidden; background:#fff;}}
.page:last-of-type{{page-break-after:avoid;}}

.top{{display:flex; justify-content:space-between; align-items:flex-start;
      border-bottom:2px solid #1F1B16; padding-bottom:3.5mm;}}
.top .bl{{font-family:Georgia,serif; font-weight:700; font-size:15pt; letter-spacing:.13em;}}
.top .bl i{{color:#9C7A3C; font-style:normal;}}
.top .bs{{font-size:6.2pt; letter-spacing:.32em; color:#9C7A3C; font-weight:700; margin-top:1px;}}
.top .rt{{text-align:right; font-size:7.6pt; color:#6B6357; line-height:1.55;}}
.top .rt b{{color:#1F1B16;}}

h1{{font-family:Georgia,serif; font-size:17pt; font-weight:700; margin:6mm 0 1mm;
    letter-spacing:-.01em;}}
.sub{{font-size:9.4pt; color:#6B6357; margin-bottom:5mm;}}
h2{{font-size:7.4pt; letter-spacing:.2em; text-transform:uppercase; color:#9C7A3C;
    font-weight:700; margin:6mm 0 2mm; border-bottom:1px solid #E4DED2; padding-bottom:1.5mm;}}

.amb{{margin-bottom:4.5mm; break-inside:avoid;}}
.amb .hd{{display:flex; align-items:baseline; gap:3mm; border-bottom:1.5px solid #1F1B16;
          padding-bottom:1.4mm; margin-bottom:0;}}
.amb .hd .n{{font-family:Georgia,serif; font-size:12pt; font-weight:700;}}
.amb .hd .s{{font-size:6.6pt; letter-spacing:.16em; text-transform:uppercase;
             color:#9C7A3C; font-weight:700;}}
table{{width:100%; border-collapse:collapse;}}
.esc th{{text-align:left; font-size:6.2pt; letter-spacing:.14em; text-transform:uppercase;
         color:#948C7E; font-weight:700; padding:1.6mm 2.5mm 1.2mm 0; border-bottom:1px solid #E4DED2;}}
.esc td{{padding:2mm 2.5mm 2mm 0; border-bottom:1px solid #EFEAE0; vertical-align:top;
         font-size:8.5pt; line-height:1.48;}}
.esc td:last-child{{padding-right:0;}}
.esc .it{{width:46mm; font-weight:700; color:#1F1B16;}}
.esc .ac{{width:46mm; color:#5C5548;}}
.esc .de{{color:#5C5548;}}
.esc b{{color:#1F1B16;}}
.novo{{display:inline-block; background:#9C7A3C; color:#fff; font-size:5.8pt;
       letter-spacing:.12em; text-transform:uppercase; font-weight:700;
       padding:.7mm 1.6mm; border-radius:2px; vertical-align:middle; margin-left:1.5mm;}}
.alt{{display:inline-block; background:#EDE5D5; color:#7A6134; font-size:5.8pt;
      letter-spacing:.12em; text-transform:uppercase; font-weight:700;
      padding:.7mm 1.6mm; border-radius:2px; vertical-align:middle; margin-left:1.5mm;}}
.conf{{color:#A6443A !important;}}

.gen td{{padding:1.9mm 3mm 1.9mm 0; border-bottom:1px solid #EFEAE0; vertical-align:top;
         font-size:8.6pt; line-height:1.5; color:#5C5548;}}
.gen td.k{{width:44mm; font-weight:700; color:#1F1B16;}}
.gen b{{color:#1F1B16;}}

.box{{border:1px solid #DED7C9; border-radius:4px; padding:4mm 5mm; margin-top:3mm;
      background:#FBF8F2;}}
.box .t{{font-family:Georgia,serif; font-size:11pt; font-weight:700; margin-bottom:1.5mm;}}
.box p{{margin:0; font-size:8.6pt; color:#5C5548; line-height:1.55;}}
.box b{{color:#1F1B16;}}

.tot{{display:flex; align-items:baseline; justify-content:space-between;
      border:2px solid #1F1B16; border-radius:4px; padding:4.5mm 6mm; margin-top:3mm;}}
.tot .k{{font-size:7pt; letter-spacing:.2em; text-transform:uppercase; color:#6B6357;
         font-weight:700;}}
.tot .v{{font-family:Georgia,serif; font-size:26pt; font-weight:700; line-height:1;}}

.pag td{{padding:2mm 0; border-bottom:1px solid #EFEAE0; font-size:9pt;}}
.pag th{{text-align:left; font-size:6.2pt; letter-spacing:.14em; text-transform:uppercase;
         color:#948C7E; font-weight:700; padding:0 0 1.5mm; border-bottom:1.5px solid #1F1B16;}}
.pag .r{{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap;}}
.pag tr:last-child td{{font-weight:700;}}

.term{{display:flex; gap:4mm; margin-top:3mm;}}
.term > div{{flex:1; border:1px solid #DED7C9; border-radius:4px; padding:2.8mm 3mm;
             text-align:center;}}
.term .k{{font-size:6.2pt; letter-spacing:.14em; text-transform:uppercase; color:#948C7E;
          font-weight:700;}}
.term .v{{font-family:Georgia,serif; font-size:11.5pt; font-weight:700; margin-top:.8mm;
          line-height:1.15;}}

.aceite{{border:2px solid #1F1B16; border-radius:4px; padding:5mm 6mm; margin-top:5mm;}}
.aceite .t{{font-family:Georgia,serif; font-size:12.5pt; font-weight:700;}}
.aceite p{{font-size:8.4pt; color:#5C5548; line-height:1.55; margin:1.5mm 0 0;}}
.sig{{display:flex; gap:8mm; margin-top:9mm;}}
.sig > div{{flex:1; border-top:1px solid #1F1B16; padding-top:1.6mm; font-size:7.6pt;
            color:#6B6357;}}

.foot{{position:absolute; left:16mm; right:16mm; bottom:9mm; display:flex;
       justify-content:space-between; font-size:6.8pt; color:#948C7E;
       border-top:1px solid #E4DED2; padding-top:2mm;}}
.foot b{{color:#6B6357; font-weight:700; letter-spacing:.1em;}}
</style></head><body>

<!-- ═══════════ 1 ═══════════ -->
<div class="page">
  {topo(1)}

  <h1>Memorial descritivo</h1>
  <div class="sub">Conferência de escopo e especificação. <b>9 conjuntos em 5 ambientes.</b></div>

  <div class="box">
    <div class="t">Como usar este documento</div>
    <p>Cada conjunto está descrito com <b>acabamento</b> e <b>especificação técnica</b>.
    Confira item a item: o que estiver de acordo, segue para produção exatamente assim.
    O que precisar mudar, aponte antes da aprovação — depois dela, alteração de
    acabamento ou de ferragem implica revisão de prazo e de valor. Os pontos marcados
    em <b class="conf">vermelho</b> dependem da medição no local.</p>
  </div>

  <h2>Escopo · parte 1 — lavanderias e hall</h2>
  {ESCOPO_A}

  {rodape(1)}
</div>

<!-- ═══════════ 2 ═══════════ -->
<div class="page">
  {topo(2)}

  <h1>Escopo · parte 2</h1>
  <div class="sub">Cozinha e suíte master — os seis conjuntos de maior porte.</div>

  {ESCOPO_B}

  {rodape(2)}
</div>

<!-- ═══════════ 4 ═══════════ -->
<div class="page">
  {topo(3)}

  <h1>Padrões construtivos</h1>
  <div class="sub">O que vale para todos os conjuntos, salvo indicação em contrário.</div>

  <h2>Acabamentos</h2>
  <div class="box" style="margin-top:0; margin-bottom:3mm;">
    <div class="t">Um acabamento só, na casa inteira</div>
    <p>Toda a marcenaria é em <b>MDF Gianduia Trama</b>: da lavanderia do térreo ao
    closet do casal, a mesma chapa, interno e externo. O <b>MDF Itapuã</b> entra como
    contraponto amadeirado, só nas básculas da cozinha e no painel de TV.</p>
  </div>
  <table class="gen">{_tb(ACAB)}</table>

  <h2>Espessuras e bordas</h2>
  <table class="gen">{_tb(ESPESS)}</table>

  <h2>Ferragens</h2>
  <table class="gen">{_tb(FERR)}</table>

  <h2>Não incluso no escopo</h2>
  <div class="box" style="margin-top:0;">
    <p>Bancadas de pedra, cubas e metais · eletrodomésticos · pontos elétricos e
    hidráulicos · gesso, pintura e obra civil · cortinas, tapetes e decoração.</p>
  </div>

  {rodape(3)}
</div>

<!-- ═══════════ 4 ═══════════ -->
<div class="page">
  {topo(4)}

  <h1>Investimento e condições</h1>
  <div class="sub">Valores e prazos que acompanham o escopo das páginas 1 a 3.</div>

  <h2>Iluminação</h2>
  <table class="gen">
    <tr><td class="k">Fornecimento Valvic</td><td><b>Todo o LED da marcenaria é fornecido
    e instalado por nós</b> — fita, perfil, fonte e acionamento. Entregue funcionando,
    dentro da garantia da peça.</td></tr>
    <tr><td class="k">Onde</td><td>Cristaleira 1, Cristaleira 2 e painel de TV.</td></tr>
    <tr><td class="k">Alimentação</td><td>O <b>ponto elétrico</b> até o móvel é obra civil.
    Indicamos a posição exata na medição.</td></tr>
  </table>

  <h2>Investimento</h2>

  <div class="tot">
    <span class="k">Investimento total</span>
    <span class="v">R$ {br(TOTAL)}</span>
  </div>

  <h2>Pagamento — quatro parcelas</h2>
  <table class="pag">
    <tr><th>Parcela</th><th class="r">%</th><th class="r">Valor</th></tr>
    {linhas_pag}
    <tr><td>Total</td><td class="r">100%</td><td class="r">R$ {br(TOTAL)}</td></tr>
  </table>

  <h2>Prazo, garantia e validade</h2>
  <div class="term">
    <div><div class="k">Entrega</div><div class="v">90 a 120<br>dias</div></div>
    <div><div class="k">Garantia Valvic</div><div class="v">20 anos</div></div>
    <div><div class="k">Validade</div><div class="v">sexta<br>14 · agosto</div></div>
  </div>

  <div class="box" style="margin-top:5mm;">
    <div class="t">Próximos passos</div>
    <p>Com a aprovação deste memorial, entramos na <b>medição no local</b> e emitimos o
    projeto executivo de produção. O prazo de <b>90 a 120 dias</b> conta a partir da
    aprovação e da liberação da frente de trabalho. A <b>garantia Valvic de 20 anos</b>
    cobre o conjunto que fornecemos e instalamos, incluindo a ferragem Blum e o LED.</p>
  </div>

  {rodape(4)}
</div>

</body></html>"""

(P/'memorial-nadia.html').write_text(HTML, encoding='utf-8')
print('wrote memorial-nadia.html', len(HTML))
print(f'  total   R$ {br(TOTAL)}')
print('  parcelas', ' + '.join(f'{p}% {br(v)}' for _, p, v in PARC))
print(f'  conjuntos: {sum(len(a[2]) for a in AMBIENTES)} em {len(AMBIENTES)} ambientes')
