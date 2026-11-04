# -*- coding: utf-8 -*-
"""SPE NOVA LIMA 1 — proposta COMPLETA (stand + apartamento decorado).

[Jonathan 10/09/2026] REVISÃO DE FECHAMENTO:
  · investimento FECHADO em R$ 168.000 (era R$ 204.000)
  · ferragem especificada e REBAIXADA: dobradiças Hettich Novisys, corrediças
    telescópicas SEM amortecimento, articuladores simples e sistema de correr
    de roupeiro RO65 Rometal (saía Dominus)
  · "não fale sobre quantitativo de material nem metragem de nada"
  · "não precisa desmembrar os ambientes, apenas cite todos"

[Jonathan 10/09, 2º ajuste]
  · o INTERNO dos armários é MDF Branco TX — dito com todas as letras
  · os LEDs são FORNECIDOS PELO CLIENTE — saem do escopo Valvic

⚠ O LED sai do custo: 16,7 m no decorado a R$ 130/m (fita + perfil com
  difusor) = R$ 2.171. O custo direto cai de R$ 83.193 para R$ 81.022 e a MC
  em R$ 168.000 sobe de 30,5% para 31,8%. A sanca do pilar do stand também
  perde o LED, mas o stand está com preço travado desde 17/07 e não tenho a
  linha dele separada.

⛔ Onde o descritivo dizia "iluminado" / "iluminada", passa a dizer
  "preparado para iluminação". Móvel que promete luz e não entrega a fita é a
  mesma falha de 02/09 na direção da imagem.

→ Some a tabela de dez frentes com valor por linha. Fica UM número.
→ Saem TODAS as cotas, m² e contagens do descritivo. O escopo continua
  completo — o que sai é a régua, não o móvel.

⚠ A GARANTIA CAI DE 5 PARA 2 ANOS. `ferragens.md`: "a Linha Silver troca
  corrediças ocultas por telescópicas (garantia 2 anos nas corrediças)". Não dá
  para vender telescópica sem amortecimento com os 5 anos que a versão anterior
  oferecia — os 5 anos estavam ancorados justamente na corrediça oculta.

⚠ MARGEM. O rebaixamento de ferragem vale ~R$ 4.210 de custo direto; nos
  R$ 204.000 anteriores a MC combinada era 37,2%. Em R$ 168.000 com a ferragem
  nova a MC cai para ~30,5%. Mantendo os 37,2% o número seria R$ 194.300.
  O corte é decisão de preço do Jonathan, não consequência da ferragem.

Histórico: proposta de 07/08 (R$ 189.400), revisão de 21/08 com a copa e a ilha
(R$ 204.000). Motor do decorado: `corte-spe-decorado.py`.
"""

import pathlib, re
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

# CSS idêntico ao da primeira versão — lido do próprio build original
CSS = re.search(r'<style>\n(.*?)\n</style>',
                (P/'build-lm.py').read_text(encoding='utf-8'), re.S).group(1)

AMBIENTES = [
 ('Stand de vendas', [
   'Gourmet e lounge — painéis das paredes, armário gourmet, móvel do lounge, '
   'porta ripada e forro',
   'Corretores e pilar central — painel de backdrop com nicho recuado e painel '
   'do pilar com moldura de hidrante e sanca preparada para iluminação',
   'Pérgola em perfil metálico revestido em MDF madeirado',
   'Portas — copa, armário gourmet e acesso ao QG',
 ]),
 ('Apartamento decorado', [
   'Cozinha — bancada em “L”, torre do forno, aéreos em dois planos e painel '
   'alto com nichos',
   'Sala — painelaria com nichos de espelho, espelho emoldurado e porta '
   'embutida',
   'Quarto — roupeiro espelhado, módulo de nichos em laca brilhante preparado '
   'para iluminação, cabeceira estofada, painel de TV, bancada e criado suspenso',
   'Suíte — torre de nichos preparada para iluminação, roupeiro espelhado, '
   'painel ripado, cabeceira estofada e cortineiro',
   'Copa — armário com portas de giro, gaveteiro central e prateleiras',
   'Ilha gourmet — corpo com os quatro lados em acabamento, nicho ventilado '
   'para a adega e armário',
 ]),
]
# [Jonathan 10/09] investimento FECHADO — sem desmembrar por ambiente
TOT = 168000
PRAZO, GARANTIA = '60 a 75 dias úteis', '2 anos'
def br(v): return f'{v:,.0f}'.replace(',', '.')

def lista(t):
    its = ''.join(f'<li>{x}</li>' for x in dict(AMBIENTES)[t])
    return f'<ul>{its}</ul>'

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<style>
{CSS}
</style></head>
<body>

<!-- CAPA -->
<div class="page cover">
  <div class="frame"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="dot">.</span></div><div class="brand-sub">MARCENARIA</div></div>
    <div class="kicker">Proposta comercial</div>
    <div class="client">SPE Nova Lima 1</div>
    <div class="proj">Stand de vendas e apartamento decorado — projeto arq. Lodi Motta</div>
    <div class="meta">
      <div class="m"><div class="t">Escopo</div><div class="v">Stand completo e seis ambientes do decorado</div></div>
      <div class="m"><div class="t">Acabamentos</div><div class="v">Cravo Trend · Moscada · Anis · Frapé · Ciliegio</div></div>
    </div>
    <div class="foot">
      <div><span class="sparkles">&#10022; &#10022; &#10022;</span><br>Do executivo ao encaixe, medido no milímetro.</div>
      <div style="text-align:right">10 de setembro de 2026<br>validade 15 dias</div>
    </div>
  </div>
</div>

<!-- ESCOPO -->
<div class="page">
  <div class="eyebrow">O que será executado</div>
  <div class="section-h serif">O escopo completo</div>
  <hr class="rule">
  <p class="lead">Leitura fiel do seu executivo — parede a parede, das pranchas
  MOB 01 e MOB 02 do stand e MO 03, DET 02, DET 05, DET 06 e DET 07 do decorado.
  Fornecimento, terceiros coordenados e instalação por equipe própria Valvic.
  Medidas conferidas no local antes do corte.</p>

  <div class="block">
    <div class="nm">Stand de vendas</div>
    <div class="sub">Gourmet e lounge · corretores e pilar · pérgola · portas</div>
    {lista('Stand de vendas')}
  </div>

  <div class="block" style="margin-top:6mm;">
    <div class="nm">Apartamento decorado</div>
    <div class="sub">Cozinha · sala · quarto · suíte · copa · ilha gourmet</div>
    {lista('Apartamento decorado')}
  </div>

  <div class="note" style="margin-top:5mm;">
    <div class="h">Acabamentos</div>
    <b>Stand:</b> MDF Arauco Realce Cravo Trend nos painéis aparentes e Moscada
    Matt nas caixas e móveis; pérgola em perfil metálico revestido em MDF
    madeirado. <b>Decorado:</b> Anis Matt e Frapé Matt na cozinha, sala, suíte,
    copa e ilha; Ciliegio Poro e laca brilhante Sayerlack M072 no quarto.
    <b>O interno de todos os armários é MDF Branco TX</b> — caixaria,
    prateleiras, fundos e caixas de gaveta. Rodapé em perfil de inox escovado,
    item de serralheria fornecido por parceiro e coordenado pela Valvic.
    Espelhos, laca e estofados coordenados pela Valvic e entregues instalados.
  </div>

  <div class="note" style="margin-top:4mm;">
    <div class="h">Não inclusos</div>
    <b>Iluminação em LED — fita, perfil e drivers, fornecidos pelo cliente.</b>
    Forro e caixas em gypsum, porta veneziana e vidro temperado do pilar
    (terceiros), pintura, cortinas, tapetes, eletrodomésticos, bancadas e
    rodabancas de pedra, cubas e metais, pontos elétricos e hidráulicos e obra
    civil.
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>SPE Nova Lima 1 · Projeto Lodi Motta</span></div>
</div>

<!-- FERRAGENS -->
<div class="page">
  <div class="eyebrow">Especificação técnica</div>
  <div class="section-h serif">A ferragem deste contrato</div>
  <hr class="rule">
  <p class="lead">A ferragem é o que se aciona todos os dias e é onde o móvel
  envelhece. Fica escrita aqui, item por item, para não haver dúvida do que está
  sendo contratado.</p>

  <div class="highlights" style="display:grid;grid-template-columns:1fr 1fr;gap:5mm">
    <div class="hl perg">
      <div class="t">Dobradiças — Hettich Novisys</div>
      <ul>
        <li>Dobradiça <b>Hettich</b>, linha <b>Novisys</b>, em todas as portas de giro e básculas do contrato.</li>
        <li>Tecnologia alemã, norma EN 15570, <b>100.000 ciclos</b> de abertura.</li>
        <li>Regulagem que mantém a fresta entre portas alinhada depois da instalação.</li>
      </ul>
    </div>
    <div class="hl port">
      <div class="t">Corrediças — telescópicas</div>
      <ul>
        <li><b>Corrediça telescópica, sem amortecimento</b>, em todas as gavetas e gavetões.</li>
        <li>Abertura total, deslizamento sobre esferas.</li>
        <li>É a linha que define a <b>garantia de 2 anos</b> desta proposta.</li>
      </ul>
    </div>
    <div class="hl port">
      <div class="t">Básculas — articulador simples</div>
      <ul>
        <li><b>Articulador simples</b> nas portas basculantes dos aéreos.</li>
        <li>Mantém a folha aberta na posição, liberando as duas mãos.</li>
      </ul>
    </div>
    <div class="hl perg">
      <div class="t">Roupeiros — RO65 Rometal</div>
      <ul>
        <li>Portas de correr espelhadas em <b>sistema RO65 da Rometal</b>, nos roupeiros do quarto e da suíte.</li>
        <li>Folha em esquadria de alumínio com espelho, sobre trilho Rometal.</li>
      </ul>
    </div>
  </div>

  <div class="note" style="margin-top:4mm;">
    <div class="h">Puxadores e iluminação</div>
    Puxador em <b>cava usinada</b> no próprio material, com fita de bordo,
    conforme o detalhe das pranchas. <b>A iluminação em LED é fornecida pelo
    cliente</b> — fita, perfil e drivers. A Valvic entrega os nichos, a sanca do
    pilar e o cortineiro da suíte com o <b>rasgo e o embutimento usinados,
    prontos para receber a fita</b>.
  </div>

  <div class="hero" style="margin-top:1mm;">
    <div class="t">Investimento total</div>
    <div class="big serif">R$ {br(TOT)}</div>
    <div class="cap">Stand de vendas e apartamento decorado, escopo completo —
    projeto executivo, fornecimento, terceiros coordenados e instalação por
    equipe própria Valvic. Uma execução, do desenho ao encaixe.</div>
  </div>

  <div class="split" style="margin-top:3mm;">
    <div>
      <h3 class="blk">Condições de pagamento</h3>
      <div class="hrule"></div>
      <ul class="pay">
        <li><b>40%</b> de entrada (assinatura)</li>
        <li><b>40%</b> no início da montagem</li>
        <li><b>20%</b> na entrega final</li>
      </ul>
    </div>
    <div>
      <h3 class="blk">Prazo &amp; garantia</h3>
      <div class="hrule"></div>
      <div class="terms">
        <div class="term"><div class="t">Entrega</div><div class="b">{PRAZO.replace(' dias', '<br>dias')}</div></div>
        <div class="term"><div class="t">Garantia</div><div class="b">{GARANTIA}</div></div>
      </div>
    </div>
  </div>


  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>SPE Nova Lima 1 · Projeto Lodi Motta · 10/09/2026</span></div>
</div>

</body></html>"""

(P/'proposta-spe-nova-lima.html').write_text(HTML, encoding='utf-8')
import subprocess
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-spe-nova-lima.pdf')], check=True)
print(f'proposta-spe-nova-lima.html · .pdf   ·   total R$ {br(TOT)}')
