import json, html
docs=json.load(open('docs.json'))

CSS = """
:root{
  --ink:#0E2038; --ink-2:#20303f; --gold:#C2A05A; --gold-dk:#8d6a2c;
  --paper:#FBFAF7; --surface:#ffffff; --rule:#e4ded1; --rail:#ddd5c4;
  --mute:#64707F; --ok:#2f7d4f; --restr:#b0413f;
  --shadow:0 1px 2px rgba(14,32,56,.06), 0 8px 24px -12px rgba(14,32,56,.18);
}
@media (prefers-color-scheme: dark){
  :root{
    --ink:#EDE9E0; --ink-2:#c3ccd6; --gold:#D8B978; --gold-dk:#E3C994;
    --paper:#0B1420; --surface:#131E2C; --rule:#243244; --rail:#2c3c50;
    --mute:#8e9cad; --ok:#6fc08f; --restr:#e08b88;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -14px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --ink:#EDE9E0; --ink-2:#c3ccd6; --gold:#D8B978; --gold-dk:#E3C994;
  --paper:#0B1420; --surface:#131E2C; --rule:#243244; --rail:#2c3c50;
  --mute:#8e9cad; --ok:#6fc08f; --restr:#e08b88;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -14px rgba(0,0,0,.7);
}
:root[data-theme="light"]{
  --ink:#0E2038; --ink-2:#20303f; --gold:#C2A05A; --gold-dk:#8d6a2c;
  --paper:#FBFAF7; --surface:#ffffff; --rule:#e4ded1; --rail:#ddd5c4;
  --mute:#64707F; --ok:#2f7d4f; --restr:#b0413f;
  --shadow:0 1px 2px rgba(14,32,56,.06), 0 8px 24px -12px rgba(14,32,56,.18);
}
*,*::before,*::after{ box-sizing:border-box; }
body{ margin:0; background:var(--paper); color:var(--ink);
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
  font-size:16px; line-height:1.55; -webkit-font-smoothing:antialiased; }
.serif{ font-family:Georgia,"Iowan Old Style","Times New Roman",serif; }
.mono{ font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace; font-variant-numeric:tabular-nums; }
.wrap{ max-width:60rem; margin:0 auto; padding:clamp(1.5rem,4vw,3.5rem) clamp(1rem,4vw,2rem) 4rem; }

/* ---------- cabeçalho ---------- */
header{ border-bottom:1px solid var(--rule); padding-bottom:1.75rem; }
.eyebrow{ font-size:.7rem; letter-spacing:.22em; text-transform:uppercase; color:var(--gold-dk); font-weight:700; }
h1{ font-family:Georgia,"Iowan Old Style",serif; font-weight:600; font-size:clamp(1.9rem,5vw,2.9rem);
  line-height:1.1; margin:.5rem 0 0; text-wrap:balance; letter-spacing:-.01em; }
.sub{ color:var(--mute); max-width:44ch; margin:.7rem 0 0; font-size:1rem; }
.stats{ display:flex; flex-wrap:wrap; gap:0; margin-top:1.6rem; }
.stat{ padding-right:1.6rem; margin-right:1.6rem; border-right:1px solid var(--rule); }
.stat:last-child{ border-right:none; margin-right:0; padding-right:0; }
.stat .n{ font-family:Georgia,serif; font-size:1.5rem; font-weight:700; line-height:1; }
.stat .l{ font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; color:var(--mute); margin-top:.3rem; font-weight:600; }

/* ---------- trilho cronológico ---------- */
ol.tl{ list-style:none; margin:2.25rem 0 0; padding:0; display:flex; flex-direction:column; gap:1.1rem; }
li.item{ display:grid; grid-template-columns:5.5rem 1fr; gap:0 1.4rem; position:relative; }
li.item::before{ content:""; position:absolute; left:5.5rem; top:.55rem; bottom:-1.1rem;
  width:1px; background:var(--rail); }
li.item:last-child::before{ display:none; }
.when{ text-align:right; padding-top:.15rem; padding-right:.9rem; }
.when .d{ font-size:.86rem; font-weight:700; letter-spacing:.02em; }
.when .y{ font-size:.7rem; color:var(--mute); margin-top:.1rem; }
.node{ position:absolute; left:calc(5.5rem - 4px); top:.55rem; width:9px; height:9px; border-radius:50%;
  background:var(--paper); border:2px solid var(--rail); }
li.item.fresh .node{ border-color:var(--gold); background:var(--gold); }

.card{ background:var(--surface); border:1px solid var(--rule); border-radius:6px;
  padding:1.15rem 1.3rem 1.2rem; box-shadow:var(--shadow); }
.card h2{ font-family:Georgia,serif; font-weight:600; font-size:1.22rem; line-height:1.25;
  margin:0; letter-spacing:-.005em; }
.card h2 .s{ color:var(--mute); font-weight:400; font-style:italic; }
.q{ margin:.5rem 0 0; color:var(--ink-2); font-size:.94rem; max-width:62ch; }
.tags{ display:flex; flex-wrap:wrap; gap:.4rem; margin-top:.85rem; }
.tag{ font-size:.72rem; padding:.2rem .55rem; border:1px solid var(--rule); border-radius:3px;
  color:var(--mute); background:transparent; }
.foot{ display:flex; flex-wrap:wrap; align-items:center; gap:.75rem; margin-top:1rem;
  padding-top:.85rem; border-top:1px solid var(--rule); }
.meta{ font-size:.76rem; color:var(--mute); letter-spacing:.01em; }
.chip{ font-size:.68rem; font-weight:700; letter-spacing:.06em; text-transform:uppercase;
  padding:.18rem .5rem; border-radius:3px; }
.chip.rev{ color:var(--ok); border:1px solid color-mix(in srgb, var(--ok) 40%, transparent); }
.chip.restr{ color:var(--restr); border:1px solid color-mix(in srgb, var(--restr) 40%, transparent); }
.chip.w{ color:var(--gold-dk); border:1px solid color-mix(in srgb, var(--gold) 55%, transparent); }
a.open{ margin-left:auto; display:inline-flex; align-items:center; gap:.45rem;
  background:var(--ink); color:var(--paper); text-decoration:none; font-size:.82rem; font-weight:600;
  padding:.5rem .95rem; border-radius:4px; border:1px solid transparent; transition:opacity .15s ease; }
a.open:hover{ opacity:.85; }
a.open:focus-visible{ outline:2px solid var(--gold); outline-offset:2px; }
a.open svg{ width:.85em; height:.85em; }

footer{ margin-top:3rem; padding-top:1.25rem; border-top:1px solid var(--rule);
  font-size:.78rem; color:var(--mute); display:flex; flex-wrap:wrap; gap:.75rem 1.5rem; }
footer b{ color:var(--ink); font-weight:600; }
@media (max-width:34rem){
  li.item{ grid-template-columns:1fr; gap:.4rem; }
  li.item::before, .node{ display:none; }
  .when{ text-align:left; }
  .when .d{ font-size:.75rem; letter-spacing:.08em; text-transform:uppercase; color:var(--gold-dk); }
  .when .y{ display:inline; margin-left:.4rem; }
  a.open{ margin-left:0; }
}
@media (prefers-reduced-motion:reduce){ *{ transition:none !important; } }
"""

ICON='<svg viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 8.5V13h10V8.5M8 2v8m0 0L5 7m3 3l3-3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

items=[]
for i,d in enumerate(docs):
    rev = d['atu']!=d['cri']
    chips=''
    if rev: chips+=f'<span class="chip rev">revisado {html.escape(d["atu"])}</span>'
    if d['walton']: chips+='<span class="chip w">preparado p/ Walton</span>'
    if d['restrito']: chips+='<span class="chip restr">restrito</span>'
    tags=''.join(f'<span class="tag">{html.escape(t)}</span>' for t in d['tags'])
    dia,mes=d['cri'].split()
    items.append(f'''    <li class="item{' fresh' if i==0 else ''}">
      <span class="node" aria-hidden="true"></span>
      <div class="when"><div class="d mono">{dia} {mes}</div><div class="y mono">2026</div></div>
      <article class="card">
        <h2>{html.escape(d['t'])} <span class="s">· {html.escape(d['s'])}</span></h2>
        <p class="q">{html.escape(d['q'])}</p>
        <div class="tags">{tags}</div>
        <div class="foot">
          <span class="meta mono">{html.escape(d['fmt'])} · {d['kb']} KB</span>
          {chips}
          <a class="open" href="data:application/pdf;base64,{d['b64']}" download="{d['f']}" target="_blank" rel="noopener">{ICON} Abrir PDF</a>
        </div>
      </article>
    </li>''')

rev_n=sum(1 for d in docs if d['atu']!=d['cri'])
HTML=f'''<style>{CSS}</style>
<div class="wrap">
  <header>
    <div class="eyebrow">Valvic Marcenaria · Conversa com o investidor</div>
    <h1>Dossiê Walton</h1>
    <p class="sub">Tudo que foi produzido para a conversa com o Walton, do mais recente ao mais antigo. Cada entrada abre a versão mais atual do documento.</p>
    <div class="stats">
      <div class="stat"><div class="n mono">{len(docs)}</div><div class="l">documentos</div></div>
      <div class="stat"><div class="n mono">26 jun → 25 jul</div><div class="l">período</div></div>
      <div class="stat"><div class="n mono">{rev_n}</div><div class="l">revisado depois de criado</div></div>
    </div>
  </header>

  <ol class="tl">
{chr(10).join(items)}
  </ol>

  <footer>
    <span><b>Uso restrito.</b> Documentos com dado de remuneração e posição financeira — não circular fora dos sócios e do destinatário.</span>
    <span>Fonte: pasta <span class="mono">painel/</span> do repositório · atualizado em 25 de julho de 2026.</span>
  </footer>
</div>
'''
open('dossie-walton.html','w',encoding='utf-8').write(HTML)
print('escrito · MB:', round(len(HTML.encode())/1024/1024,2))
