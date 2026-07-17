# -*- coding: utf-8 -*-
# Proposta ALINE SANCHES no LAYOUT PREMIUM DA KÊNIA. Reusa o CSS da Kenia (le do arquivo),
# gera corpo estatico (sem JS) com os dados do Aline. Imagens em base64. Render weasyprint.
import re, base64, pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')
kenia = (P/'propostakeniafabiopremium.html').read_text(encoding='utf-8')
CSS = re.search(r'<style>.*?</style>', kenia, re.S).group(0)   # reaproveita o visual da Kenia

def b64(name):
    return 'data:image/png;base64,' + base64.b64encode((P/name).read_bytes()).decode()
HERO=b64('img-aline-hero.png'); SALA=b64('img-aline-sala.png')

# ---------------- DADOS ALINE ----------------
AMB = [
 ("Cozinha & Gourmet","R$ 28.000",[
   ("M01","Aéreos da cozinha","316 cm — 2 + 4 portas de giro + módulo Cumaru com nicho de microondas, escorredor de louças e depurador; LED inferior em cava.","Nude · Cumaru"),
   ("M02","Armários baixos","Torre de forno com gavetão de vassoura, módulo cooktop (2 portas), porta-temperos e baixo de apoio; vãos livres p/ geladeira e lava-e-seca.","Nude"),
   ("M03","Báscula + nicho","Báscula (prof. 45) e nicho de microondas na faixa média.","Cumaru"),
   ("M04","Torre de despensa","179 × 248 — 4 + 3 portas de giro, nicho revestido em Cumaru com LED e 2 gavetas-fruteira com frente de vidro.","Nude · Cumaru"),
   ("M05","Armário estreito","Sob a bancada alta — 3 gavetas com corrediças telescópicas.","Nude"),
   ("M06","Cristaleira","50 × 145 — porta e 5 prateleiras em vidro incolor 8 mm, LED embutido.","Cumaru"),
   ("M07","Pórtico decorativo","Moldura em Cumaru com perfil de LED 3000K, acionamento por interruptor bolinha.","Cumaru"),
 ]),
 ("Área Social","R$ 9.000",[
   ("M08","Painel de TV","Painel em Nude com detalhe ripado em Cumaru (ripas de 3 cm / vãos de 3 cm).","Nude · Cumaru"),
   ("M09","Prateleira suspensa","Cumaru, com fita de LED 3000K embutida em cava na face inferior.","Cumaru"),
   ("M10","Rack / hack suspenso","Corpo em Cumaru, 2 gavetas em Nude com corrediças telescópicas (prof. 40).","Cumaru · Nude"),
   ("M11","Ripado sob a bancada em L","Cumaru, ripas de 3 cm com espaçamento de 3 cm.","Cumaru"),
 ]),
 ("Quarto 02 & Escritório","R$ 14.500",[
   ("M12","Roupeiro de correr","156 cm — 2 portas de correr, nichos laterais revestidos em Cumaru com LED; interno com maleiro, cabideiros, gavetas e sapateiras.","Nude · Cumaru"),
   ("M13","Coluna de nichos","Lateral do roupeiro — 5 nichos em Cumaru com LED em cava.","Cumaru"),
   ("M14","Aéreo do escritório","2 portas — corpo Cumaru com frentes em Nude, LED inferior.","Cumaru · Nude"),
   ("M15","Bancada de trabalho","130 cm — 2 gavetas estreitas, com previsão de caixa de tomadas embutida.","Nude"),
   ("M16","Penteadeira","Cumaru — gaveta com repartições internas e tampo em vidro incolor.","Cumaru"),
   ("M17","Cabeceira em L","Nude, com fita de LED 3000K embutida em cava na face superior.","Nude"),
 ]),
 ("Banheiro","R$ 5.300",[
   ("M18","Espelheira / aéreo","123,5 × 126 — 1 porta de correr com espelho prata e nichos com LED.","Cumaru"),
   ("M19","Gabinete","Báscula + gaveta (corrediça telescópica) + porta de papel-higiênico na lateral.","Cumaru"),
 ]),
 ("Quarto Casal / Suíte","R$ 21.000",[
   ("M20","Painel de TV","Painel em Nude com prateleira em Cumaru (prof. 25), LED inferior.","Nude · Cumaru"),
   ("M21","Roupeiro de correr","200 cm + módulo lateral 100 cm — 2 portas de correr (1 com espelho prata); interno completo com prateleiras, cabideiros, 4 gavetas e sapateiras.","Nude · Cumaru"),
   ("M22","Painel ripado da cabeceira","254 cm em Cumaru, ripas de 3 cm com espaçamento de 3 cm.","Cumaru"),
   ("M23","Mesa lateral","Nude, 2 gavetas; pés em metalon com pintura dourado fosco.","Nude"),
 ]),
]

DIF = [
 ("M12 2l3.5 6.5L22 9.3l-5 4.8 1.2 6.9L12 17.8 5.8 21 7 14.1 2 9.3l6.5-.8Z","Ferragem que abre macio a vida toda","CORREDIÇAS TELESCÓPICAS · DOBRADIÇAS HARDT · SOFT-CLOSE","Gaveta que corre no ponto e porta que fecha sem batida. Ferragem escolhida para o uso diário — não a mais barata da prateleira."),
 ("M3 3h18v18H3zM9 9h6M9 12h6M9 15h4","Engenharia digital antes do corte","PLANO DE CORTE PEÇA A PEÇA · APROVAÇÃO PRÉVIA","Cada módulo é decomposto e conferido em plano de corte antes de qualquer chapa entrar na serra. Zero improviso na obra."),
 ("M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z","Equipe própria do início ao fim","SEM TERCEIRIZAÇÃO · RESPONSABILIDADE TOTAL","Quem projeta é quem produz é quem instala. A responsabilidade não muda de mão no meio do caminho."),
 ("M12 2l2.4 7.4H22l-6 4.3 2.3 7.3-6.3-4.6-6.3 4.6 2.3-7.3-6-4.3h7.6z","Acabamento amadeirado texturizado","MDF NUDE BERNECK + CUMARU ARAUCO · BORDAS COLADAS","O amadeirado que você toca todo dia — Nude nas frentes, Cumaru nos detalhes e ripados, com fita de borda no tom, sem emenda aparente."),
 ("M22 16.92V19a2 2 0 01-2.18 2A19.79 19.79 0 013.07 5.18 2 2 0 015 3h2.09a2 2 0 012 1.72c.13.96.36 1.9.7 2.81a2 2 0 01-.45 2.11L8.09 10.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0122 18z","Suporte real pós-entrega","GARANTIA EM CONTRATO · VISITA DE ACOMPANHAMENTO","Garantia formal assinada. Não sumimos após o pagamento — estamos aqui quando você precisar."),
]

def dif_html():
    out=[]
    for path,t,spec,desc in DIF:
        out.append(f'''<div class="dif"><div class="dif-ico"><svg viewBox="0 0 24 24"><path d="{path}"/></svg></div>
        <div><div class="dif-title">{t}</div><div class="dif-spec">{spec}</div><div class="dif-desc">{desc}</div></div></div>''')
    return "\n".join(out)

def amb_html(groups):
    out=[]
    for nome,val,itens in groups:
        rows="".join(f'''<div class="d-item"><div class="d-code">{c}</div>
          <div class="d-body"><span class="d-name">{n}</span> — <span class="d-desc">{d}</span></div>
          <div class="d-cor">{cor}</div></div>''' for c,n,d,cor in itens)
        out.append(f'''<div class="amb-group"><div class="amb-head"><div class="amb-title">{nome}</div>
        <div class="amb-count">{len(itens)} itens</div><div class="amb-val">{val}</div></div>{rows}</div>''')
    return "\n".join(out)

TL=[("1","Alinhamento","Entendemos o escopo e o ambiente antes de qualquer número. A visita define o que será executado."),
("2","Detalhamento Técnico","O projeto da Galeria 42 vira instrução de fábrica. Cada medida conferida no local."),
("3","Programação","Data de produção definida antes de iniciar, com prazo comunicado."),
("4","Produção","Corte, montagem e furação com os processos acumulados em anos de fábrica."),
("5","Acabamento","Borda, superfície e detalhe revisados antes do módulo entrar em embalagem."),
("6","Conferência","Cada peça testada, cada ferragem montada e verificada antes de sair da fábrica."),
("7","Entrega & Montagem","Equipe própria. Do caminhão ao parafuso final — sem terceirização de montagem."),
("8","Compromisso Contínuo","Ferragem tem garantia. Dúvida tem resposta. A relação não encerra na entrega.")]
def tl_html():
    out=[]
    for i,(n,nm,arg) in enumerate(TL):
        conn='' if i in (3,7) else '<div class="tl-conn"></div>'
        out.append(f'<div class="tl-step"><div class="tl-circle"><span class="tl-num">{n}</span></div><div class="tl-name">{nm}</div><div class="tl-arg">{arg}</div>{conn}</div>')
    return "\n".join(out)

HTML=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">{CSS}</head><body>

<section class="page" id="p1">
  <div class="topbar"><div class="logo"><svg viewBox="0 0 12 12"><path d="M6 0L7 5.2L12 6L7 6.8L6 12L5 6.8L0 6L5 5.2Z"/></svg><span class="logo-name">Valvic</span></div><span class="badge">Premium · Hardt</span></div>
  <div class="hero"><img id="hero-img" src="{HERO}" alt="Projeto" style="display:block"/></div>
  <div class="identity"><div>
    <div class="prep">Proposta preparada para</div>
    <div class="client-name">Aline Sanches</div>
    <div class="proj-label">Projeto de marcenaria sob medida</div>
    <div class="proj-desc">Apartamento completo · Design de Interiores Galeria 42 / Natally Duarte</div>
  </div><div class="meta"><div class="meta-date">24/07/2026</div><div class="meta-ref">Ref. Premium · Hardt</div></div></div>
  <div class="gold-bar"></div>
</section>

<section class="page" id="p2">
  <div class="p2-head"><div class="eyebrow">Por que Valvic</div>
  <div class="p2-headline">O detalhe<br><em>que você não vê</em><br>é o que faz a diferença.</div>
  <div class="p2-sub">Marcenaria é precisão milimétrica. Esta proposta existe porque você merece entender exatamente o que está comprando — e por que vale o que vale.</div></div>
  <div class="p2-body">
    <div class="photo-col"><img id="p2-img" src="{SALA}" alt="Detalhe" style="display:block"/></div>
    <div class="dif-col"><div class="dif-col-label">5 razões que definem a entrega</div>
    {dif_html()}
    </div>
  </div>
</section>

<section class="page descr">
  <div class="descr-head"><div class="eyebrow">O Projeto · Descritivo Técnico</div>
  <div class="descr-title">O que vamos<br>executar para você.</div>
  <div class="descr-sub">Aline Sanches &nbsp;—&nbsp; Apartamento completo · Galeria 42 / Natally Duarte</div>
  <div class="descr-specs">Ferragens Telescópica + Hardt · MDF Nude Berneck + Cumaru Arauco · Interior Branco TX · LED 3000K · Garantia 5 anos</div></div>
  <div class="descr-body">
  {amb_html(AMB[:2])}
  </div>
</section>

<section class="page descr">
  <div class="descr-cont"><span>Descritivo técnico</span><span class="descr-cont-pg">continuação</span></div>
  <div class="descr-body">
  {amb_html(AMB[2:])}
  </div>
</section>

<section class="page" id="p4">
  <div class="p4-head"><div class="p4-eyebrow">Daqui em diante</div>
  <div class="p4-title">Quem faz, responde —<br><em>do aceite à montagem.</em></div>
  <div class="p4-sub">Anos de fábrica, equipe própria, compromisso com cada detalhe — do primeiro contato ao pós-entrega.</div></div>
  <div class="tl-grid">{tl_html()}</div>
  <div class="p4-foot"><div class="foot-brand">Valvic Marcenaria</div></div>
</section>

<section class="page" id="p6">
  <div class="inv-dark-head"><div class="inv-eyebrow">Transparência Total</div><div class="inv-title">Seu Investimento.</div>
  <div class="inv-sub">Duas versões. Mesma marcenaria, mesma ferragem. Você escolhe o acabamento interno.</div></div>
  <div class="inv-body">
    <div class="ver-grid">
      <div class="ver-card hi"><div class="ver-tag">Recomendada</div><div class="ver-name">Tudo na cor</div>
      <div class="ver-desc">Interior dos armários acompanha o amadeirado das frentes — sensação de peça maciça e contínua ao abrir.</div>
      <div class="ver-price">R$ 88.700</div></div>
      <div class="ver-card"><div class="ver-tag">Mais enxuta</div><div class="ver-name">Branco interno</div>
      <div class="ver-desc">Interior em Branco TX — uso mais claro e funcional, amadeirado nas frentes. Mesma marcenaria e mesma ferragem.</div>
      <div class="ver-price">R$ 77.800</div></div>
    </div>
    <div class="pay-block"><div class="pay-label">Condições de pagamento</div>
    <table class="pay-tbl"><tbody>
      <tr class="hi"><td>Entrada — 30% na assinatura</td><td>30%</td></tr>
      <tr><td>1º boleto — 30 dias</td><td>17,5%</td></tr>
      <tr><td>2º boleto — 60 dias</td><td>17,5%</td></tr>
      <tr><td>3º boleto — 90 dias</td><td>17,5%</td></tr>
      <tr><td>4º boleto — 120 dias</td><td>17,5%</td></tr>
    </tbody></table></div>
    <div class="meta-row">
      <div class="meta-card mc-navy"><div class="mc-label">Prazo de entrega</div><div class="mc-val">90–120</div><div class="mc-sub">dias · a partir da aprovação</div></div>
      <div class="meta-card mc-gold"><div class="mc-label">Garantia</div><div class="mc-val">5 anos</div><div class="mc-sub">ferragens Hardt</div></div>
      <div class="meta-card mc-cream"><div class="mc-label">Validade dos valores</div><div class="mc-val">10</div><div class="mc-sub">dias corridos</div></div>
    </div>
    <p class="inv-foot"><b>Escopo Valvic:</b> marcenaria sob medida (Nude Berneck + Cumaru Arauco) · ferragens (Telescópica + Hardt) · vidros e espelhos dos móveis · iluminação LED embutida. <b>Não incluso:</b> pedra/marmoraria (bancadas e cubas), eletrodomésticos, box do banheiro, estofados e pés em metalon.</p>
    <div class="cta-row"><div><h3>Qual o próximo passo?</h3><p>Podemos apresentar a proposta pessoalmente e tirar todas as dúvidas. Estamos à disposição para tornar o projeto da Aline realidade.</p></div></div>
  </div>
</section>

</body></html>'''
(P/'proposta-aline.html').write_text(HTML,encoding='utf-8')
print('wrote proposta-aline.html', len(HTML))
