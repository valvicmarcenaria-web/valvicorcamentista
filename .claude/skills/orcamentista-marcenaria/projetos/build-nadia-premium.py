# -*- coding: utf-8 -*-
"""NÁDIA E MAURÍLIO — folder PREMIUM, 8 páginas. Proposta comercialmente agressiva.

[Jonathan 11/08/2026]
  · layout do folder do Apto CJ (`build-apto-cj-folder.py`), 8 páginas
  · escopo: as DUAS lavanderias · armário do corredor (hall dos dormitórios) ·
    cozinha SEM o painel de TV · closet do casal
  · ferragens BLUM · garantia 20 anos · entrega 90 a 120 dias
  · pagamento 20 · 20 · 20 · 40 (fechamento · 60 dias · início da montagem ·
    ENTREGA FINAL) — some a parcela pós-obra
  · 12% de desconto
  · validade: sexta-feira, 14 de agosto de 2026 (hoje é terça, 11 — janela de 3 dias)
  · deixar claro que é um momento estratégico e uma grande oportunidade

VALORES — coluna COM FERRAGENS do `nadia_v3.pdf`, menos o painel de TV:
  130.100 − 2.250 = 127.850 de tabela → −12% = 112.508,00
  3 × 22.501,60 (20%) + 1 × 45.003,20 (40%)

[Jonathan 11/08, 2ª rodada] desconto 15% → 12% · corrediça MOVENTO → TANDEM ·
  última parcela leva os 40% restantes · e o ARMÁRIO DO CORREDOR NÃO TEM BLUM
  (as portas de espelho correm no sistema da própria esquadria de alumínio).
  ⚠️ "última parcela com os 40% restantes" não disse em qual marco. Adotei
     ENTREGA FINAL — a parcela pós-obra some. Se for para manter o marco
     pós-obra, é trocar uma linha em PARCELAS.

⚠️ NÃO HÁ LEVANTAMENTO PARA ESTE JOB. Os valores vieram prontos do documento de
   origem — não existe `corte-nadia.py`, não há plano de corte nem MC conferida.
   Três compressões estão empilhadas sobre um número que não consigo auditar:
   o desconto de 12%, o upgrade para Blum e o alongamento do recebimento.
   Está tudo escrito no dossiê `2026-nadia-maurilio.md`.

⚠️ GARANTIA — `referencias/ferragens.md` proíbe vender ferragem POR GARANTIA
   ("garantia vitalícia da ferragem nunca fez parte do escopo da Valvic").
   Aqui os 20 anos são emitidos como **garantia VALVIC**, não da Blum — é termo
   nosso, não do fabricante. A ferragem, na página 3, é argumentada por CICLOS
   TESTADOS, amortecimento e regulagem, como manda a referência.

⚠️ Lavanderia superior: no documento de origem a célula de valor está EM BRANCO
   e a descrição diz "Idem lavanderia". Mantidos os 5.850 do térreo. Segue aberto.
"""
import pathlib, base64
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
CSS = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""', 1)[0]

def uri(n):
    return 'data:image/jpeg;base64,' + base64.b64encode((P/'img'/n).read_bytes()).decode()

CLO1, CLO2, CLO3 = (uri(f'nadia-closet-{i}.jpg') for i in (1, 2, 3))
COZ1, COZ2, COZ3 = (uri(f'nadia-cozinha-{i}.jpg') for i in (1, 2, 3))
LAV1, LAV2 = uri('nadia-lavanderia-1.jpg'), uri('nadia-lavanderia-2.jpg')

# ── escopo e valores ───────────────────────────────────────────────────────
ITENS = [
 ('Lavanderia do térreo', 'Pavimento inferior',
  'Estrutura interna e acabamento externo em <b>MDF Areia Guararapes</b> · puxadores '
  'inferiores em cava e superiores passantes · fundo em MDF com <b>duplo revestimento</b> · '
  'dobradiças <b>Blum CLIP top BLUMOTION</b>.', 5850),
 ('Lavanderia superior', 'Pavimento superior',
  'Mesma especificação da lavanderia do térreo, ponto a ponto — mesma chapa, mesmo fundo '
  'com duplo revestimento, mesma linha de ferragem.', 5850),
 ('Armário do corredor', 'Hall dos dormitórios',
  'Estrutura interna e acabamento externo em <b>MDF Areia Guararapes</b> · portas de '
  '<b>espelho prata</b> em esquadria de <b>alumínio</b> — o perfil acompanha o tom do '
  'espelho, não o contraria. <i>Único conjunto sem ferragem Blum: as portas correm no '
  'próprio sistema da esquadria de alumínio.</i>', 6300),
 ('Cozinha · ilha e geladeiras', '',
  'Estrutura interna e externa em <b>MDF Areia</b> · puxadores em cava com perfil · '
  '<b>ilha de 2,80 m</b> · gavetas em <b>Blum TANDEM com BLUMOTION</b>.', 15100),
 ('Cozinha · cristaleira', '',
  'Cores conforme projeto · <b>3 portas de vidro reflecta bronze</b> em esquadria de '
  'alumínio bronze · prateleiras de vidro incolor temperado de 8 mm · puxadores em cava '
  'com perfil · iluminação de LED instalada · <b>80 cm</b> de largura.', 5650),
 ('Cozinha · bancada', 'Aéreos e inferiores',
  'Armários aéreos e inferiores com estrutura em <b>MDF Areia</b> · cores externas conforme '
  'projeto · básculas em <b>MDF amadeirado</b> interno e externo · puxadores inferiores em '
  'cava com <b>perfil Rometal RM280</b> e superiores passantes · básculas em '
  '<b>Blum AVENTOS HK-S</b> · gavetas em <b>Blum TANDEM</b>.', 52400),
 ('Closet do casal', 'Suíte master · versão 2',
  'Estrutura completa em <b>MDF Areia</b> · gavetas com puxadores espaçados e '
  '<b>Blum TANDEM com BLUMOTION</b> · <b>cabideiros metálicos</b> · sem a cômoda.', 36700),
]
TABELA   = sum(i[3] for i in ITENS)
DESC_PCT = 0.12
DESCONTO = round(TABELA*DESC_PCT, 2)
TOTAL    = round(TABELA - DESCONTO, 2)
P20      = round(TOTAL*0.20, 2)
P40      = round(TOTAL*0.40, 2)
assert TABELA == 127850, TABELA
assert DESCONTO == 15342.00 and TOTAL == 112508.00
assert P20 == 22501.60 and P40 == 45003.20
assert round(3*P20 + P40, 2) == TOTAL

def br(v):  return f'{v:,.0f}'.replace(',', '.')
def br2(v): return f'{v:,.2f}'.replace(',', '·').replace('.', ',').replace('·', '.')

PARCELAS = [
 ('1ª — no fechamento',             'Assinatura do contrato',            20, P20),
 ('2ª — 60 dias após o fechamento', 'Sem vínculo com etapa de obra',     20, P20),
 ('3ª — no início das montagens',   'Equipe Valvic no local',            20, P20),
 ('4ª — na entrega final',          'Marcenaria concluída e conferida',  40, P40),
]
def _lin_pag(i, n, d, pc, vl):
    cls = ' class="best"' if i == len(PARCELAS)-1 else ''
    sub = ('<span style="font-size:7.8pt;color:var(--mut);font-weight:400"> · '
           + d + '</span>')
    return (f'<tr{cls}><td>{n}{sub}</td>'
            f'<td class="r">{pc}%</td><td class="r">R$ {br2(vl)}</td></tr>')

linhas_pag = ''.join(_lin_pag(i, *r) for i, r in enumerate(PARCELAS))

linhas_item = ''.join(
  f'<tr><td class="nm">{a}</td><td class="r">R$ {br(v)}</td></tr>'
  for a, _, _, v in ITENS)

def bloco(a, b, d):
    sub = f'<div class="s">{b}</div>' if b else ''
    return f'<div class="amb"><div class="n">{a}</div>{sub}<div class="dd">{d}</div></div>'

ESC_LAV = ''.join(bloco(a, b, d) for a, b, d, _ in ITENS[:3])
ESC_COZ = ''.join(bloco(a, b, d) for a, b, d, _ in ITENS[3:6])
ESC_CLO = ''.join(bloco(a, b, d) for a, b, d, _ in ITENS[6:])

# ── SVG das ferragens: MECANISMO, não foto de catálogo ─────────────────────
SVG_TANDEM = """<svg viewBox="0 0 200 112" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="14" y="20" width="172" height="62" rx="2" stroke="#C9A96A" stroke-width="1.5"/>
 <rect x="26" y="30" width="128" height="42" rx="1.5" fill="#EFE7D8" stroke="#3A322A" stroke-width="1.5"/>
 <rect x="26" y="74" width="128" height="5" rx="1" fill="#C9A96A"/>
 <path d="M26 79 H154" stroke="#3A322A" stroke-width="1.2"/>
 <path d="M154 51 h26" stroke="#3A322A" stroke-width="1.2" stroke-dasharray="3 3"/>
 <path d="M172 45 l8 6 -8 6" stroke="#3A322A" stroke-width="1.2"/>
 <text x="26" y="98" font-size="8" fill="#8C7B5E" font-family="system-ui">a corrediça corre POR BAIXO — a gaveta não mostra trilho</text>
</svg>"""

SVG_AVENTOS = """<svg viewBox="0 0 200 112" fill="none" xmlns="http://www.w3.org/2000/svg">
 <path d="M20 88 H186" stroke="#C9A96A" stroke-width="1.5"/>
 <rect x="20" y="62" width="80" height="20" rx="1.5" fill="#EFE7D8" stroke="#3A322A" stroke-width="1.5"/>
 <g opacity=".38">
  <rect x="20" y="62" width="80" height="20" rx="1.5" fill="none" stroke="#3A322A"
        stroke-width="1.2" transform="rotate(-32 22 72)"/>
  <rect x="20" y="62" width="80" height="20" rx="1.5" fill="none" stroke="#3A322A"
        stroke-width="1.2" transform="rotate(-62 22 72)"/>
 </g>
 <path d="M100 72 A 52 52 0 0 0 62 22" stroke="#C9A96A" stroke-width="1.4" stroke-dasharray="4 3"/>
 <circle cx="22" cy="72" r="3.2" fill="#C9A96A"/>
 <text x="112" y="38" font-size="8" fill="#8C7B5E" font-family="system-ui">para onde a mão</text>
 <text x="112" y="49" font-size="8" fill="#8C7B5E" font-family="system-ui">soltar</text>
</svg>"""

SVG_CLIPTOP = """<svg viewBox="0 0 200 112" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="18" y="14" width="16" height="84" fill="#3A322A"/>
 <rect x="120" y="14" width="13" height="84" fill="#EFE7D8" stroke="#3A322A" stroke-width="1.5"/>
 <g opacity=".34">
  <rect x="120" y="14" width="13" height="84" fill="none" stroke="#3A322A" stroke-width="1.2"
        transform="rotate(-26 126 56)"/>
  <rect x="120" y="14" width="13" height="84" fill="none" stroke="#3A322A" stroke-width="1.2"
        transform="rotate(-52 126 56)"/>
 </g>
 <path d="M34 56 H120" stroke="#C9A96A" stroke-width="1.5"/>
 <circle cx="34" cy="56" r="3.4" fill="#C9A96A"/><circle cx="120" cy="56" r="3.4" fill="#C9A96A"/>
 <path d="M60 42 h34" stroke="#8C7B5E" stroke-width="1" stroke-dasharray="2 2"/>
 <path d="M60 70 h34" stroke="#8C7B5E" stroke-width="1" stroke-dasharray="2 2"/>
 <text x="40" y="108" font-size="8" fill="#8C7B5E" font-family="system-ui">regulagem em 3 eixos, com a porta montada</text>
</svg>"""

SVG_ESTR = """<svg viewBox="0 0 260 138" fill="none" xmlns="http://www.w3.org/2000/svg">
 <rect x="30" y="14" width="9" height="104" fill="#3A322A"/>
 <rect x="196" y="14" width="9" height="104" fill="#3A322A"/>
 <rect x="39" y="14" width="157" height="9" fill="#3A322A"/>
 <rect x="39" y="109" width="157" height="9" fill="#3A322A"/>
 <rect x="39" y="60" width="157" height="11" fill="#C9A96A"/>
 <rect x="205" y="14" width="4" height="104" fill="#B9AC93"/>
 <rect x="213" y="10" width="11" height="112" fill="#6E6250"/>
 <text x="46" y="36" font-size="9" fill="#241E18" font-family="system-ui" font-weight="700">15 mm</text>
 <text x="46" y="48" font-size="8" fill="#8C7B5E" font-family="system-ui">caixaria interna</text>
 <text x="82" y="69" font-size="8" fill="#241E18" font-family="system-ui" font-weight="700">18 mm · prateleira</text>
 <text x="46" y="103" font-size="8" fill="#8C7B5E" font-family="system-ui">base 15 mm</text>
 <path d="M209 130 H205" stroke="#8C7B5E"/>
 <text x="146" y="133" font-size="7.5" fill="#8C7B5E" font-family="system-ui">fundo 6 mm →</text>
 <text x="228" y="66" font-size="8" fill="#241E18" font-family="system-ui" font-weight="700">18 mm</text>
 <text x="228" y="77" font-size="7.5" fill="#8C7B5E" font-family="system-ui">porta</text>
</svg>"""

FOOT = ('<div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span>'
        '<span>Nádia &amp; Maurílio · proposta válida até sexta, 14 de agosto de 2026</span></div>')

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}

  .cover-t{{background:var(--deep); position:relative; overflow:hidden;}}
  .cover-t::before{{content:""; position:absolute; inset:0;
     background:radial-gradient(120% 80% at 16% 10%, rgba(201,169,106,.17) 0%, transparent 58%),
                radial-gradient(90% 70% at 90% 96%, rgba(201,169,106,.11) 0%, transparent 60%);}}
  .cover-t .rules{{position:absolute; inset:0;
     background:repeating-linear-gradient(90deg, rgba(255,255,255,.030) 0 1px, transparent 1px 34mm);}}
  .mos{{position:absolute; inset:0; pointer-events:none; z-index:1;}}
  .mos figure{{position:absolute; margin:0; overflow:hidden; border-radius:3px;
      box-shadow:0 8px 30px rgba(0,0,0,.5);}}
  .mos figure img{{width:100%; height:100%; object-fit:cover; display:block;}}
  .mos .a img{{object-position:center 26%;}}
  .mos .a{{top:2mm; right:-16mm; width:112mm; height:84mm;}}
  .mos .b{{top:64mm; right:52mm; width:70mm; height:80mm;}}
  .mos .c{{top:102mm; right:-10mm; width:86mm; height:62mm;}}
  .mos .ln{{position:absolute; background:var(--gold-lt); opacity:.9;}}
  .mos .l1{{top:72mm; right:126mm; width:40mm; height:1.4px;}}
  .mos .l2{{top:100mm; right:139mm; width:1.4px; height:46mm;}}
  .cover-t .scrim{{position:absolute; left:0; right:0; bottom:0; height:60%;
     background:linear-gradient(to bottom, rgba(26,21,16,0) 0%, rgba(26,21,16,.86) 34%,
                var(--deep) 62%); z-index:2;}}
  .cover-t .inner{{position:relative; z-index:3; justify-content:flex-start;}}
  .cover-t .mid{{max-width:122mm; margin-top:auto; margin-bottom:15mm; flex:none;}}
  .cover-t .strip{{flex:none;}}
  .selo{{display:inline-block; margin-bottom:5mm; background:var(--gold-lt); color:#241E18;
     font-size:7.4pt; letter-spacing:.2em; text-transform:uppercase; font-weight:700;
     padding:2mm 4.5mm; border-radius:2px;}}

  /* página escura conceitual */
  .dark{{background:var(--deep); color:#EFE9DC;}}
  .dark .pad{{padding:17mm 19mm 15mm; display:flex; flex-direction:column;}}
  .dark .quatro{{flex:none;}}
  .dark .eyebrow{{color:var(--gold-lt);}}
  .dark .h-sec{{color:#fff;}} .dark .h-sec em{{color:var(--gold-lt);}}
  .dark .body-t{{color:#C9C2B4;}} .dark .body-t b{{color:#F0E7D6;}}
  .dark .pfoot{{color:#8E877A; border-color:rgba(201,169,106,.25);}}
  .dark .bl .d{{color:var(--gold-lt);}}
  .quatro{{margin-top:7mm; border-top:1px solid rgba(201,169,106,.30);}}
  .quatro > div{{display:flex; gap:6mm; padding:5.2mm 0;
      border-bottom:1px solid rgba(201,169,106,.16);}}
  .quatro .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:21pt; font-weight:700;
      color:var(--gold-lt); line-height:1; width:13mm; flex:none;}}
  .quatro .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:14.5pt; font-weight:700;
      color:#fff; line-height:1.2;}}
  .quatro .d{{font-size:9.1pt; color:#B9B1A2; line-height:1.62; margin-top:1.6mm;}}
  .quatro .d b{{color:#F0E7D6;}}
  .fecho{{margin-top:6mm; font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt;
      font-style:italic; color:var(--gold-lt); line-height:1.4;}}

  /* ambientes */
  .amb .dd{{font-size:9.4pt; color:var(--soft); line-height:1.66; margin-top:2mm;}}
  .amb .dd b{{color:var(--ink);}}

  .rend2{{display:flex; gap:5mm; margin-top:6mm;}}
  .rend2 > div{{flex:1;}}
  .rend2 img{{width:100%; height:68mm; object-fit:cover; display:block; border-radius:4px;
      box-shadow:0 1px 6px rgba(0,0,0,.12);}}
  .rend2 .cp{{font-size:6.2pt; letter-spacing:.13em; text-transform:uppercase; color:var(--gold);
      font-weight:700; margin-top:1.8mm;}}

  /* ferragens */
  .fer{{display:flex; gap:8mm; margin-top:6mm; border-top:1px solid var(--line);
      padding-top:6mm; align-items:center;}}
  .fer:first-of-type{{border-top:2px solid var(--ink);}}
  .fer .art{{width:70mm; flex:none; background:var(--sand); border-radius:6px; padding:4.5mm 5mm;}}
  .fer .art svg{{width:100%; height:auto; display:block;}}
  .fer .tx{{flex:1;}}
  .fer .k{{font-size:6.4pt; letter-spacing:.17em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .fer .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:17.5pt; font-weight:700;
      color:var(--ink); line-height:1.14; margin-top:1mm;}}
  .fer .d{{font-size:9.2pt; color:var(--soft); line-height:1.64; margin-top:2.2mm;}}
  .fer .d b{{color:var(--ink);}}

  .estr{{display:flex; gap:8mm; margin-top:4mm; align-items:center;}}
  .estr .dw{{width:96mm; flex:none; background:var(--sand); border-radius:6px; padding:8mm 6mm 5mm;}}
  .estr .dw svg{{width:100%; height:auto; display:block;}}
  .estr .tx{{flex:1;}}

  .desc-row td{{color:var(--gold) !important; font-weight:700;}}

  /* faixa de oferta — ancora o número já na página 2 */
  .oferta{{margin-top:auto; margin-bottom:9mm; border:1px solid rgba(201,169,106,.42);
      border-radius:6px; padding:6mm 7mm; background:rgba(201,169,106,.07);}}
  .oferta .ln{{display:flex; align-items:baseline; gap:6mm;}}
  .oferta .de{{font-size:11pt; color:#9C9384; text-decoration:line-through;
      font-family:'Cormorant Garamond',Georgia,serif;}}
  .oferta .por{{font-family:'Cormorant Garamond',Georgia,serif; font-size:30pt;
      font-weight:700; color:var(--gold-lt); line-height:1;}}
  .oferta .pc{{font-size:9.2pt; color:#B9B1A2; margin-top:2.6mm;}}
  .oferta .pc b{{color:#F0E7D6;}}

  .rend3{{display:flex; gap:4mm; margin-top:6mm;}}
  .rend3 > div{{flex:1;}}
  .rend3 img{{width:100%; height:46mm; object-fit:cover; display:block; border-radius:4px;
      box-shadow:0 1px 6px rgba(0,0,0,.12);}}
  .rend3 .cp{{font-size:6.2pt; letter-spacing:.13em; text-transform:uppercase; color:var(--gold);
      font-weight:700; margin-top:1.8mm;}}
  .p-inv .inv-hero{{padding:4.5mm 6mm;}}
  .p-inv .inv-hero .v{{font-size:30pt;}}
  .p-inv .item-tb{{margin-top:3.5mm;}}
  .p-inv .item-tb td{{padding:1.5mm 0;}}
  .p-inv .pay-tb{{margin-top:4mm;}}
  .p-inv .pay-tb td{{padding:1.6mm 0;}}
  .p-inv .terms{{margin-top:4mm;}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover cover-t">
  <div class="rules"></div>
  <div class="mos">
    <figure class="a"><img src="{COZ2}" alt=""></figure>
    <figure class="b"><img src="{CLO1}" alt=""></figure>
    <figure class="c"><img src="{LAV1}" alt=""></figure>
    <span class="ln l1"></span><span class="ln l2"></span>
  </div>
  <div class="scrim"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="selo">Condição especial · até sexta, 14 de agosto</div>
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Nádia<br>&amp; Maurílio.</div>
      <div class="sub">Cozinha · closet do casal · lavanderias · corredor</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">7 conjuntos · 5 ambientes</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Blum</div></div>
      <div class="c"><div class="k">Garantia</div><div class="v">20 anos</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. A OPORTUNIDADE ══════ -->
<div class="page dark"><div class="pad">
  <div class="eyebrow">Por que agora</div>
  <hr class="rule">
  <div class="h-sec">Uma janela de <em>três dias</em>.</div>
  <div class="body-t" style="margin-top:5mm; max-width:150mm;">
    Esta não é a proposta anterior com um desconto carimbado por cima. <b>Quatro coisas
    mudaram ao mesmo tempo</b>, e cada uma delas tem custo do nosso lado. Elas só se
    sustentam juntas, e só até sexta-feira.
  </div>

  <div class="quatro">
    <div>
      <div class="n">01</div>
      <div><div class="t">12% abaixo da tabela</div>
      <div class="d"><b>R$ {br2(DESCONTO)}</b> a menos, sem tirar uma linha do escopo.
      A especificação é a mesma — o que mudou foi o preço, não o móvel.</div></div>
    </div>
    <div>
      <div class="n">02</div>
      <div><div class="t">Toda a ferragem em Blum</div>
      <div class="d">A linha inteira subiu: <b>CLIP top BLUMOTION</b> nas portas,
      <b>TANDEM com BLUMOTION</b> nas gavetas, <b>AVENTOS</b> nas básculas. Dentro do
      preço já reduzido — <b>não é upgrade cobrado à parte</b>.</div></div>
    </div>
    <div>
      <div class="n">03</div>
      <div><div class="t">20 anos de garantia Valvic</div>
      <div class="d">Termo nosso, emitido por nós, sobre o conjunto que nós fornecemos
      e instalamos.</div></div>
    </div>
    <div>
      <div class="n">04</div>
      <div><div class="t">Quatro parcelas, a maior no fim</div>
      <div class="d">Entrada de apenas <b>20%</b>. Os outros 80% acompanham a execução, e a
      maior parcela — <b>40%, R$ {br2(P40)}</b> — só na <b>entrega final</b>, com a
      marcenaria concluída e conferida no local.</div></div>
    </div>
  </div>

  <div class="fecho">É o conjunto que faz a conta fechar — nenhuma das quatro<br>
  sobrevive isolada. Vale até <b>sexta-feira, 14 de agosto</b>.</div>

  <div class="oferta">
    <div class="ln"><span class="de">De R$ {br(TABELA)}</span>
      <span class="por">R$ {br2(TOTAL)}</span></div>
    <div class="pc">Sete conjuntos em <b>quatro parcelas</b> — três de
    R$ {br2(P20)} e a última de <b>R$ {br2(P40)}</b>, só na entrega final.</div>
  </div>
  {FOOT}
</div></div>

<!-- ══════ 3. FERRAGENS 100% BLUM ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">O que você não vê, e usa todo dia</div>
  <hr class="rule">
  <div class="h-sec">A ferragem é o <em>móvel</em> em movimento.</div>
  <div class="body-t" style="margin-top:4mm; max-width:152mm;">
    A chapa você escolhe pela cor. A ferragem você só percebe quando falha — e ela falha
    depois, não na entrega. Por isso ela está aqui, desenhada e nomeada: <b>toda a
    ferragem móvel desta proposta é Blum</b>, sem linha mista. A única exceção é o
    armário do corredor, cujas portas de espelho correm no <b>sistema da própria esquadria
    de alumínio</b> — ali não existe ferragem Blum a aplicar.
  </div>

  <div class="fer">
    <div class="art">{SVG_CLIPTOP}</div>
    <div class="tx">
      <div class="k">Portas</div>
      <div class="t">CLIP top BLUMOTION</div>
      <div class="d">Amortecimento <b>dentro do corpo da dobradiça</b> — sem peça extra
      pendurada na lateral. Regulagem em <b>três eixos com a porta já montada</b>: se a
      casa trabalhar, o alinhamento se corrige em minutos, sem desmontar nada.</div>
    </div>
  </div>

  <div class="fer">
    <div class="art">{SVG_TANDEM}</div>
    <div class="tx">
      <div class="k">Gavetas</div>
      <div class="t">TANDEM com BLUMOTION</div>
      <div class="d">Corrediça <b>oculta sob a gaveta</b>: a lateral fica limpa, sem trilho
      à vista. Extração total — o fundo da gaveta vem até a mão. Testada em <b>ciclos de
      abre-e-fecha</b> muito além do uso doméstico, com carga nominal.</div>
    </div>
  </div>

  <div class="fer">
    <div class="art">{SVG_AVENTOS}</div>
    <div class="tx">
      <div class="k">Básculas</div>
      <div class="t">AVENTOS HK-S</div>
      <div class="d">A porta <b>sobe e para onde a mão soltar</b> — não cai, não bate, não
      precisa de apoio. É o que torna aéreo de báscula utilizável de verdade numa cozinha
      que se usa todo dia.</div>
    </div>
  </div>

  <div class="pull" style="margin-top:7mm;">
    <div class="t">Uma linha só, do começo ao fim.</div>
    <div class="d">Ferragem misturada envelhece em ritmos diferentes: em três anos um lado
    do armário fecha macio e o outro bate. Especificar <b>uma linha única</b> é o que faz o
    conjunto envelhecer parelho — e é a razão de estar escrito na proposta, para poder ser
    cobrado.</div>
  </div>
  {FOOT}
</div></div>

<!-- ══════ 4. LAVANDERIAS E CORREDOR ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Escopo · parte 1</div>
  <hr class="rule">
  <div class="h-sec">As duas lavanderias e o <em>corredor</em>.</div>
  <div class="lead" style="margin-top:3mm;">Os três conjuntos que ninguém mostra em foto e
  que a casa usa todos os dias.</div>
  <div style="margin-top:6mm;">{ESC_LAV}</div>
  <div class="rend2">
    <div><img src="{LAV1}" alt=""><div class="cp">Lavanderia · projeto</div></div>
    <div><img src="{LAV2}" alt=""><div class="cp">Lavanderia · projeto</div></div>
  </div>
  {FOOT}
</div></div>

<!-- ══════ 5. COZINHA ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Escopo · parte 2</div>
  <hr class="rule">
  <div class="h-sec">A cozinha, em <em>três frentes</em>.</div>
  <div class="lead" style="margin-top:3mm;">Ilha e geladeiras, cristaleira e a bancada
  inteira — aéreos e inferiores.</div>
  <div style="margin-top:6mm;">{ESC_COZ}</div>
  <div class="rend2">
    <div><img src="{COZ1}" alt=""><div class="cp">Bancada · projeto</div></div>
    <div><img src="{COZ3}" alt=""><div class="cp">Ilha · projeto</div></div>
  </div>
  {FOOT}
</div></div>

<!-- ══════ 6. CLOSET ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Escopo · parte 3</div>
  <hr class="rule">
  <div class="h-sec">O closet do <em>casal</em>.</div>
  <div class="lead" style="margin-top:3mm;">Versão 2 — a que abre o piso, tira a cômoda e
  devolve circulação ao quarto.</div>
  <div style="margin-top:6mm;">{ESC_CLO}</div>
  <div class="rend3">
    <div><img src="{CLO2}" alt=""><div class="cp">Closet · projeto</div></div>
    <div><img src="{CLO1}" alt=""><div class="cp">Cabideiros e gavetas</div></div>
    <div><img src="{CLO3}" alt=""><div class="cp">Circulação central</div></div>
  </div>

  <table class="spec-tb" style="margin-top:7mm;">
    <th style="width:44mm;">O que muda na versão 2</th><th>Efeito</th>
    <tr><td>Sai a cômoda</td><td>O volume solto no meio do quarto deixa de existir — a
        guarda migra para dentro do closet, em gaveta com corrediça Blum.</td></tr>
    <tr><td>Gavetas espaçadas</td><td>Puxador espaçado em vez de contínuo: a frente respira
        e a peça não vira um bloco de linhas paralelas.</td></tr>
    <tr><td>Cabideiro metálico</td><td>Tubo em metal em todos os vãos de pendurar, e não
        travessa de MDF.</td></tr>
    <tr><td>Estrutura contínua</td><td>Um só conjunto em <b>MDF Areia</b>, sem emendas
        aparentes entre módulos.</td></tr>
  </table>

  <div class="pull" style="margin-top:6mm;">
    <div class="t">Cabideiro metálico, não de MDF.</div>
    <div class="d">O tubo metálico não flexiona com o peso da roupa ao longo do vão. Num
    closet inteiro, é a diferença entre a linha reta que se entrega e a barriga que aparece
    no segundo ano.</div>
  </div>
  {FOOT}
</div></div>

<!-- ══════ 7. CONSTRUÇÃO ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Como é feito</div>
  <hr class="rule">
  <div class="h-sec">Cada espessura tem um <em>porquê</em>.</div>
  <div class="body-t" style="margin-top:4mm; max-width:152mm;">
    A diferença entre 15 e 18 mm numa prateleira não aparece na entrega. Aparece três anos
    depois, quando ela cede no meio do vão. Por isso está escrita aqui — <b>para poder ser
    cobrada</b>.
  </div>

  <div class="estr">
    <div class="dw">{SVG_ESTR}</div>
    <div class="tx">
      <table class="spec-tb">
        <tr><td>Caixaria</td><td><b>15 mm</b> — estrutura interna de todos os conjuntos.</td></tr>
        <tr><td>Prateleiras</td><td><b>18 mm</b> — anti-flexão, em todo vão livre acima de 70 cm.</td></tr>
        <tr><td>Portas e frentes</td><td><b>18 mm</b> — planas e estáveis, com fita de borda extra fina.</td></tr>
        <tr><td>Fundos</td><td><b>6 mm em todo o mobiliário</b>. Nas lavanderias, com
            <b>duplo revestimento</b> — as duas faces seladas contra a umidade.</td></tr>
      </table>
    </div>
  </div>

  <table class="spec-tb" style="margin-top:7mm;">
    <th style="width:44mm;">Acabamento</th><th>Especificação</th>
    <tr><td>Chapa</td><td>MDF <b>Areia Guararapes</b> na estrutura e nos externos; cores
        externas da cozinha e da cristaleira conforme projeto; básculas em <b>MDF amadeirado</b>,
        interno e externo; painel do corredor com <b>espelho prata</b>.</td></tr>
    <tr><td>Fita de borda</td><td>Extra fina <b>0,4 mm</b> — a junta some na peça em vez de
        virar um filete.</td></tr>
    <tr><td>Puxadores</td><td>Cava com <b>perfil Rometal RM280</b> nos inferiores; passantes
        nos superiores; gavetas do closet com puxadores espaçados.</td></tr>
    <tr><td>Vidros</td><td>Cristaleira com <b>reflecta bronze</b> em esquadria de alumínio
        bronze e prateleiras em <b>temperado incolor de 8 mm</b>. Corredor com espelho prata
        em esquadria de alumínio.</td></tr>
    <tr><td>Iluminação</td><td>LED instalado na cristaleira, entregue funcionando.</td></tr>
  </table>
  {FOOT}
</div></div>

<!-- ══════ 8. INVESTIMENTO ══════ -->
<div class="page p-inv"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <hr class="rule">
  <div class="h-sec">O número, e como ele <em>se paga</em>.</div>

  <div class="inv-hero" style="margin-top:4.5mm;">
    <div class="k">Investimento total · condição especial</div>
    <div class="v serif">R$ {br2(TOTAL)}</div>
    <div class="c">De <b style="text-decoration:line-through">R$ {br(TABELA)}</b> por
    R$ {br2(TOTAL)} — <b>12% de desconto</b>, R$ {br2(DESCONTO)} a menos.</div>
    <div class="alt">Sete conjuntos · ferragem <b>Blum</b> · garantia <b>20 anos</b> ·
    fornecimento, montagem e instalação por equipe própria Valvic.</div>
  </div>

  <table class="item-tb">
    <tr><th>Conjunto</th><th class="r">Tabela</th></tr>
    {linhas_item}
    <tr class="desc-row"><td class="nm" style="color:var(--gold)">Desconto especial · 12%</td>
        <td class="r">− R$ {br2(DESCONTO)}</td></tr>
    <tr class="tot"><td>Total</td><td class="r">R$ {br2(TOTAL)}</td></tr>
  </table>

  <table class="pay-tb">
    <tr><th>Pagamento · quatro parcelas</th><th class="r">%</th><th class="r">Valor</th></tr>
    {linhas_pag}
  </table>

  <div class="terms">
    <div class="term"><div class="k">Entrega</div><div class="v">90 a 120<br>dias</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">20 anos</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">sexta<br>14 · agosto</div></div>
  </div>

  <div class="note">
    <b>Incluso:</b> projeto executivo, chapas, vidros, espelhos, LED e a <b>ferragem
    Blum</b> de todos os conjuntos — o armário do corredor não leva Blum porque as portas
    correm no sistema da própria esquadria de alumínio —, montagem e instalação por equipe
    própria Valvic. <b>Não incluso:</b> bancadas
    de pedra, cubas, metais, eletrodomésticos, pontos elétricos e hidráulicos, gesso, pintura
    e obra civil. Medidas a conferir no local antes da produção. <b>A lavanderia superior</b>
    está orçada com a mesma especificação e o mesmo valor da do térreo; havendo diferença de
    medida, o valor é revisto antes do contrato.
  </div>
  {FOOT}
</div></div>

</body></html>"""

(P/'proposta-nadia-premium.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-nadia-premium.html', len(HTML))
print(f'  tabela   R$ {br2(TABELA)}')
print(f'  desconto R$ {br2(DESCONTO)}  ({DESC_PCT*100:.0f}%)')
print(f'  total    R$ {br2(TOTAL)}')
print(f'  parcelas 3 × R$ {br2(P20)} + 1 × R$ {br2(P40)}')
