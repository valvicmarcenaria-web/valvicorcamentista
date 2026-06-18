# -*- coding: utf-8 -*-
import re, weasyprint
SRC=".claude/skills/closer-vendas/ferramentas/proposta-signature.html"
s=open(SRC,encoding="utf-8").read()

# ---- alocação por ambiente (cara -> barata) ----
comp=[("Suíte Master","3 closets vidro reflecta bronze, painel ondulado, TV e penteadeira","90.400"),
 ("Cozinha","Superiores, inferiores, ilha, torre de eletros, cristaleira e adega (vidro bronze)","62.900"),
 ("Suíte 2","Closet vidro reflecta bronze, painel ripado e cabeceira","59.000"),
 ("Suíte 3","Closet vidro reflecta bronze, painéis ripados e cabeceira","42.600"),
 ("Louçaria + Lavabo","Louçarias reforçadas (30mm) e gabinete do lavabo","33.800"),
 ("Suíte 1","Closet vidro reflecta bronze, painéis, cabeceira e espelho","32.700"),
 ("Sala de TV","Painel de TV, armários inferiores e painel pivotante; espelho bronze","30.600"),
 ("Despensa","Armários com prateleiras e gavetas","26.000"),
 ("Quarto de serviço","Armários inferiores e painéis ripados","17.000")]
ess=[("Suíte Master","3 closets vidro reflecta bronze, painel ondulado, TV e penteadeira","84.700"),
 ("Cozinha","Superiores, inferiores, ilha, torre de eletros, cristaleira e adega (vidro bronze)","58.900"),
 ("Suíte 2","Closet vidro reflecta bronze, painel ripado e cabeceira","55.300"),
 ("Suíte 3","Closet vidro reflecta bronze, painéis ripados e cabeceira","39.900"),
 ("Louçaria + Lavabo","Louçarias reforçadas (30mm) e gabinete do lavabo","31.700"),
 ("Suíte 1","Closet vidro reflecta bronze, painéis, cabeceira e espelho","30.600"),
 ("Sala de TV","Painel de TV, armários inferiores e painel pivotante; espelho bronze","28.700"),
 ("Despensa","Armários com prateleiras e gavetas","24.400"),
 ("Quarto de serviço","Armários inferiores e painéis ripados","15.800")]

def rows(data,tbl):
    out=[]
    for amb,desc,val in data:
        out.append(f'''          <tr data-table="{tbl}">
            <td><span class="token editable-cell" contenteditable="false" data-placeholder="Ambiente">{amb}</span></td>
            <td><span class="token editable-cell" contenteditable="false" data-placeholder="Descrição">{desc}</span></td>
            <td class="val-cell"><span class="token editable-cell" contenteditable="false" data-placeholder="R$ 0,00">R$ {val}</span></td>
            <td class="rm-cell"><button class="btn-rm" onclick="removeRow(this)">×</button></td>
          </tr>''')
    return "\n".join(out)

# substitui tbodies
s=re.sub(r'(<tbody id="tbody-completa">).*?(</tbody>)', lambda m: m.group(1)+"\n"+rows(comp,"completa")+"\n        "+m.group(2), s, flags=re.S)
s=re.sub(r'(<tbody id="tbody-essencial">).*?(</tbody>)', lambda m: m.group(1)+"\n"+rows(ess,"essencial")+"\n        "+m.group(2), s, flags=re.S)

# p4 ambientes (nomes + descs) — agora únicos no doc
amap={">Quarto Casal<":">Cozinha<", ">Sala de Estar<":">Suíte Master<",
      ">Cozinha<":">Suítes 1 · 2 · 3<", ">Home Office<":">Serviço · Louçaria · Despensa<",
      "Roupeiro 6 portas · Painel TV · 2 criados-mudos":"Ilha · torre de eletros · cristaleira e adega (vidro bronze)",
      "Painel TV · Rack integrado · Nicho decorativo":"3 closets vidro reflecta bronze · painel ondulado · penteadeira",
      "Armários aéreos · Balcão baixo · Ilha central":"Closets em vidro bronze · painéis ripados · cabeceiras",
      "Bancada · Estante modular · Painel organizador":"Louçaria reforçada 30mm · armários · prateleiras"}
# ordem importa p/ nao cascatear nomes: faz numa passada
keys=sorted(amap, key=len, reverse=True)
pat=re.compile("|".join(re.escape(k) for k in keys))
s=pat.sub(lambda m: amap[m.group(0)], s)

# specs + garantia + JS defaults
for a,b in [("Blum Movento","Hettich"),("MDF 18mm","MDF na cor (15/18mm)"),
            ("Laca PU fosca","Metallic Suede / Cacao"),("cobertura Blum vitalícia","ferragens Hettich"),
            ("[especificar o ambiente ou item]","interior dos armários fechados (Branco TX)")]:
    s=s.replace(a,b)
for a,b in [("Signature · Blum","Signature · Hettich"),
            ("Blum não fabrica o segundo melhor","Hettich não fabrica o segundo melhor"),
            ("Ferragem Blum — austríaca, vitalícia","Ferragem Hettich — alemã, 10 anos"),
            ("MOVENTO BLUMOTION · FEATHER-TOUCH · GARANTIA VITALÍCIA","QUADRO · SENSYS · SILENT SYSTEM · GARANTIA 10 ANOS"),
            ("Blum desenvolve cada sistema há décadas","Hettich desenvolve cada sistema há décadas"),
            ("Blum: garantia vitalícia","Hettich: garantia de 10 anos")]:
    s=s.replace(a,b)
s=s.replace("Blum","Hettich")

# pagamento (Júnior: 30% + 4 boletos)
pay_old=re.search(r'(<table class="pay-tbl">).*?(</table>)', s, flags=re.S).group(0)
pay_new='''<table class="pay-tbl">
        <thead><tr><th>Condição</th><th>Observação</th></tr></thead>
        <tbody>
          <tr><td>Entrada 30% + 4 boletos (60 / 90 / 120 / 150 dias)</td><td>Condição padrão</td></tr>
          <tr class="hi"><td>À vista (transferência) na assinatura</td><td>Consultar</td></tr>
        </tbody>
      </table>'''
s=s.replace(pay_old,pay_new)

# placeholders
ph={"{{NOME_CLIENTE}}":"Júnior","{{PROJETO}}":"Residência Bouganville · Lagoa Santa",
 "{{DATA_PROPOSTA}}":"18 / 06 / 2026","{{TOTAL_COMPLETA}}":"395.000","{{TOTAL_ESSENCIAL}}":"370.000",
 "{{PRAZO}}":"30","{{GARANTIA_ANOS}}":"10 anos","{{VALIDADE}}":"22 / 06"}
for k,v in ph.items(): s=s.replace(k,v)

# print: esconder controles de edição
s=s.replace("</style>","  @media print{.rm-cell,.btn-add-row,#controls{display:none!important}}\n  </style>",1)

# ---- HTML para navegador (fontes do Google mantidas) ----
out_html=".claude/skills/closer-vendas/ferramentas/proposta-junior-signature.html"
open(out_html,"w",encoding="utf-8").write(s)
print("HTML:",out_html)

# ---- cópia para WeasyPrint (sem rede + patches A4) ----
r=re.sub(r'<link[^>]*fonts\.g[^>]*>','',s); r=re.sub(r'<link[^>]*gstatic[^>]*>','',r)
r=r.replace('page-break-inside: avoid;','')
r=r.replace('@page { size: A4; margin: 0; }','@page { size: 794px 1123px; margin: 0; } *,*::before,*::after{box-sizing:border-box;} .page{overflow:hidden !important;} .rm-cell,.btn-add-row,#controls{display:none!important;}')
open("/tmp/junior_render.html","w",encoding="utf-8").write(r)
weasyprint.HTML("/tmp/junior_render.html").write_pdf("/home/user/valvicorcamentista/proposta-junior-signature.pdf")
print("PDF: proposta-junior-signature.pdf")
