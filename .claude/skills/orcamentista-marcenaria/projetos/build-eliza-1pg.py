# -*- coding: utf-8 -*-
"""ELIZA E LUIZ GUSTAVO — proposta de UMA PÁGINA  [29/10/2026]

⭐ [Jonathan 29/10] "faça uma proposta sintetizando em uma pagina o projeto
   da brinquedoteca e esse banco considerando as corrediças ocultas da
   hettich e o estofado. considere um desconto de 10% para pagamento a
   vista."
⛔ A cozinha de brinquedo SAI: o cliente tirou do escopo.

⭐⭐ [Jonathan 30/10] "no orcamento da eliza que adicionamos o banco ·
   atualize para a versao com os valores de corrediças telescopicas."

Os números não são novos. A brinquedoteca vem de `orcamento-brinquedoteca-v2.py`
(preços DECLARADOS, não rateados) e o banco vem da proposta que já foi ao
cliente — canto alemão na coluna TELESCÓPICA, R$ 18.500, mais o estofado
R$ 6.500. As duas colunas estão no mesmo PDF `Proposta_eliza_e_luiz`: a troca
é de coluna, não de cálculo.

⛔⛔ E A TROCA ARRASTA A GARANTIA, que é o que ninguém vê ao mexer no preço.
   `closer-vendas/referencias/garantia.md` dá 2 ANOS para telescópica e 10
   para Hettich. A folha prometia "10 anos nos dois escopos", porque era a
   Hettich do canto alemão que sustentava o tier — e era a ÚNICA ferragem de
   10 anos em toda a proposta. ⭐ A brinquedoteca não tem corrediça nenhuma:
   é solda, estrutura e espuma, e os 10 anos dela já foram prometidos ao
   cliente em 30/09. Então a garantia passa a ser ESCALONADA POR ESCOPO
   [Jonathan, 30/10]: 10 anos na brinquedoteca, 2 anos no canto alemão — que
   é exatamente o que a coluna telescópica daquele PDF já oferecia a ele.
   ⛔ Nivelar os dois por baixo rebaixaria uma promessa que o cliente tem na
   mão; nivelar por cima prometeria 10 anos sobre uma ferragem de 2.
"""
import pathlib, base64, subprocess, os

P = pathlib.Path(__file__).resolve().parent
CSS = (P/'css-brinquedoteca.css').read_text()
br = lambda v: f'{v:,.0f}'.replace(',', '.')

def uri(p):
    return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()

HERO = uri(P/'img-brinquedoteca'/'capa.jpg')
# ⛔ A IMAGEM MORAVA EM /tmp, E /tmp NÃO SOBREVIVE AO CONTAINER [30/10/2026].
#   Na segunda vez que este script rodou, numa sessão nova, o render não
#   existia mais. ⭐ Entrada de build é arquivo do repositório, nunca de /tmp.
BANCO = uri(P/'img-brinquedoteca'/'estudio-canto-alemao.jpg')

# ⭐ os doze itens da v2 agrupados em cinco conjuntos legíveis — a soma é a
#   mesma, item a item, e nenhum preço foi recalculado
# ⭐ [Jonathan 29/10] "ultilize as mesmas descrições dos itens da
#   brinquedoteca, sem mudar as nomenclaturas, não precisa descrever cada
#   item · não precisa colocar o valor de cada item, apenas exclua o item
#   solicitado."
# ⛔ Os nomes são os da proposta-brinquedoteca.pdf, na ordem e na grafia dela.
#   O item 13, Cozinha de brinquedo, R$ 12.000, SAIU.
BRINQ = [
 'Passarela suspensa', 'Gradis de contenção', 'Plataformas acolchoadas',
 'Piscina de espuma', 'Banco extenso', 'Parede norte',
 'Casinha — paredes', 'Casinha — escada', 'Janelas e pórticos moldurados',
 'Escorregador com túnel curvo', 'Toldo personalizado',
 'Pintura ou papel de parede — aplicação',
]
T_BRINQ_PROPOSTA = 193_620     # investimento total da proposta original
COZINHA          = 12_000      # o item 13, retirado
ESTUDIO = ['Canto alemão em “C” · corrediças telescópicas',
           'Estofado capitonê']
T_BRINQ = T_BRINQ_PROPOSTA - COZINHA     # 181.620
# ⭐⭐ A COLUNA TELESCÓPICA, R$ 18.500 [Jonathan, 30/10] — era 23.000 na
#   coluna oculta. R$ 4.500 a menos, do mesmo PDF, sem recalcular nada.
T_EST   = 18_500 + 6_500                 # canto alemão + estofado
TOTAL   = T_BRINQ + T_EST
# ⭐ [Jonathan 29/10] "arredonde para 190k · entrada em multiplos cheques
#   totalizando 157.988 · restante pos entrega" e "aplique os R$ 12 de
#   desconto e apresente o percentual de desconto tbm" — os R$ 12 que
#   faltavam para o saldo fechar em R$ 32.000 redondos. Sobre os 211.120
#   daquele dia, isso deu R$ 21.132 de desconto e R$ 189.988 de fechado.
# ⭐⭐ [Jonathan 30/10] O DESCONTO CONCEDIDO FICA EM REAIS, não em percentual:
#   os mesmos R$ 21.132 sobre um total R$ 4.500 menor. O percentual sobe de
#   10,01% para 10,23% sozinho, e é ele que a folha imprime.
# ⛔⛔ POR ISSO O DESCONTO É AGORA O DADO DE ENTRADA E O FECHADO O DERIVADO.
#   Invertido — fechado cravado, desconto calculado, como estava — mexer no
#   preço de um item mudava o desconto em silêncio, e o número que o cliente
#   lê como concessão passava a depender de um arredondamento.
# ⭐ E o saldo caiu redondo sozinho: 185.488 − 157.988 = 27.500. Não precisou
#   do ajuste de R$ 12 desta vez, e o assert abaixo é quem garante isso.
DESCONTO = 21_132          # concedido em 29/10, mantido em reais
AVISTA   = TOTAL - DESCONTO
ENTRADA  = 157_988         # os cheques, inalterados
SALDO    = AVISTA - ENTRADA
DESC     = DESCONTO / TOTAL
PCT      = f'{DESC*100:.2f}'.replace('.', ',') + '%'

# ⛔⛔ A DATA DO RODAPÉ ESTAVA CRAVADA EM 29/10 [30/10/2026]. Eu regerei a
#   folha hoje com o canto alemão R$ 4.500 mais barato e ela saiu com a data
#   de ontem: duas propostas na mão do cliente, mesma data, preços
#   diferentes, e nenhuma delas dizendo qual é a boa. ⭐ Data de documento é
#   a do dia em que ele foi gerado — nunca literal.
DATA = '30 de outubro de 2026'

assert T_BRINQ == 181_620, T_BRINQ      # v2 menos a cozinha de brinquedo
assert T_EST   == 25_000,  T_EST        # telescópica 18.500 + estofado 6.500
assert TOTAL   == 206_620, TOTAL
assert AVISTA  == 185_488, AVISTA
# ⛔ O SALDO PÓS-ENTREGA TEM DE SER REDONDO: é o número que o cliente guarda
#   na cabeça, e foi para arredondá-lo que o Jonathan deu os R$ 12 em 29/10.
assert SALDO == 27_500 and SALDO % 500 == 0, SALDO

def lista(ls, n0=1):
    """Só o nome, numerado como na proposta de origem. Sem descrição e sem
       valor — o preço aparece uma vez, no subtotal do conjunto."""
    return ''.join(f'<div class="it"><span class="n">{i:02d}</span>'
                   f'<span class="t">{t}</span></div>'
                   for i, t in enumerate(ls, n0))

HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}
/* ⭐ uma folha só: tudo encolhe para caber, e nada sai */
.in{{padding:11mm 20mm 7mm;}}
.ttl{{font-size:20pt;margin-top:3mm;}}
.cj{{padding:.6mm 0;}}
.cj .t{{font-size:9pt;}}
.cj .d{{font-size:6.9pt;line-height:1.32;}}
.cj .v{{font-size:10pt;}}
.cj.tot{{padding-top:3.4mm;}}
.cj.tot .t{{font-size:10.5pt;}}
.cj.tot .v{{font-size:19pt;}}
.gr{{grid-template-columns:repeat(4,1fr);gap:0 6mm;margin-top:4mm;}}
.gr .v{{font-size:7.9pt;line-height:1.48;margin-top:1.2mm;}}
.gr .k{{font-size:6.2pt;letter-spacing:.24em;}}
.obs{{margin-top:3.5mm;padding-top:3mm;font-size:6.7pt;line-height:1.46;}}
.pe2{{margin-top:4mm;padding-top:4mm;}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:0 10mm;}}
.cols.um{{grid-template-columns:1fr;}}
.it{{display:flex;gap:4mm;align-items:baseline;padding:1.05mm 0;
  border-bottom:1px solid var(--linha);}}
.it .n{{font-size:7.4pt;color:var(--verde-lt);letter-spacing:.06em;}}
.it .t{{font-size:9.2pt;letter-spacing:-.005em;}}
.sb{{display:flex;justify-content:space-between;align-items:baseline;
  margin-top:2.5mm;padding-top:2mm;border-top:1.2px solid var(--tinta);}}
.sb span{{font-size:6.6pt;letter-spacing:.28em;text-transform:uppercase;
  color:var(--mut);}}
.sb b{{font-size:12pt;font-weight:400;letter-spacing:-.015em;}}
.duo{{display:grid;grid-template-columns:1fr 1fr;gap:0;height:27mm;margin:0 -20mm 2.5mm;}}
.duo .ph{{height:100%;}}
.duo .ph span{{position:absolute;left:0;bottom:0;background:var(--verde);
  color:#DCE5DD;font-size:6.2pt;letter-spacing:.26em;text-transform:uppercase;
  padding:2mm 4mm;}}
.sub2{{font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;
  color:var(--verde-lt);font-weight:500;margin:4.5mm 0 2mm;}}
.av{{margin-top:3.5mm;background:var(--verde);color:#F4F2EC;padding:3.5mm 5mm;
  display:flex;align-items:baseline;justify-content:space-between;}}
.av .k{{font-size:6.8pt;letter-spacing:.3em;text-transform:uppercase;color:#A9BFAF;}}
.av .t{{font-size:9pt;color:#C3CFC5;margin-top:1.5mm;}}
.av .v{{font-size:18pt;letter-spacing:-.025em;white-space:nowrap;
  padding-left:6mm;}}
</style></head><body>

<div class="pg"><div class="in">
  <div class="sel">Proposta · Eliza e Luiz Gustavo</div>
  <h1 class="ttl disp">A brinquedoteca e o<br><em>canto alemão do estúdio.</em></h1>

  <div class="duo">
    <div class="ph"><img src="{HERO}" alt=""><span>Brinquedoteca</span></div>
    <div class="ph"><img src="{BANCO}" alt=""><span>Estúdio · canto alemão</span></div>
  </div>

  <div class="sub2">Brinquedoteca · projeto Helena Antunes</div>
  <div class="cols">{lista(BRINQ)}</div>
  <div class="sb"><span>Brinquedoteca</span><b>R$ {br(T_BRINQ)}</b></div>

  <div class="sub2">Estúdio de música · salinha</div>
  <div class="cols um">{lista(ESTUDIO)}</div>
  <div class="sb"><span>Estúdio</span><b>R$ {br(T_EST)}</b></div>

  <div class="cj tot"><div class="n"></div>
    <div><div class="t">Investimento</div>
      <div class="d">Os dois escopos, num só contrato e numa só data</div></div>
    <div class="v">R$ {br(TOTAL)}</div></div>
  <div class="cj" style="border-top:none;border-bottom:none;padding-top:2mm">
    <div class="n"></div>
    <div><div class="t" style="color:var(--verde)">Desconto concedido</div>
      <div class="d">{PCT} sobre o investimento</div></div>
    <div class="v" style="font-size:12pt;color:var(--verde)">− R$ {br(DESCONTO)}</div></div>

  <div class="av">
    <div><div class="k">Condição fechada · {PCT} de desconto</div>
      <div class="t">Entrada de <b>R$ {br(ENTRADA)}</b> em múltiplos cheques ·
        saldo de <b>R$ {br(SALDO)}</b> após a entrega.</div></div>
    <div class="v">R$ {br(AVISTA)}</div>
  </div>

  <div class="gr">
    <div><div class="k">Corrediças</div><div class="v">
      <b>Telescópicas de extensão total</b> — a gaveta abre por inteiro.
      Trilho aparente na lateral, sem amortecedor de fechamento.</div></div>
    <div><div class="k">Estofado</div><div class="v">
      Capitonê conforme projeto, em <b>espuma D33</b> — a densidade de assento
      de uso intenso, que não achata com o tempo.</div></div>
    <div><div class="k">Entrega</div><div class="v">
      <b>90 dias corridos</b>, contados da assinatura, da entrada e da
      conferência de medidas no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">
      <b>10 anos</b> na brinquedoteca e <b>2 anos</b> no canto alemão, sobre
      estrutura, solda, ferragens e marcenaria.</div></div>
  </div>

  <div class="obs"><b>Fora desta proposta:</b> a <b>cozinha de brinquedo</b>,
  retirada a pedido do cliente · tinta, massa e papel de parede, que são
  fornecimento da contratante — nossa é a mão de obra de aplicação.
  As paredes saem em <b>MDF ultra premium cru</b>, seladas e lixadas, prontas
  para pintura; ⛔ a garantia não cobre patologia causada por pintura de
  terceiro. O <b>projeto estrutural com ART</b> da passarela, do gradil e das
  plataformas está incluso.</div>

  <div class="pe2"><span>Valvic Marcenaria</span>
    <span>Eliza e Luiz Gustavo · {DATA}</span></div>
</div></div>
</body></html>'''

(P/'proposta-eliza-1pg.html').write_text(HTML, encoding='utf-8')
# ⛔ O renderer também morava em /tmp [30/10/2026]. Está no repositório
#   agora, e recebe os caminhos por argumento em vez de cravá-los dentro.
subprocess.run(['node', str(P/'render-pdf.js'), str(P/'proposta-eliza-1pg.html'),
                str(P/'proposta-eliza-1pg.pdf')], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'  {"BRINQUEDOTECA · " + str(len(BRINQ)) + " itens":<38}{br(T_BRINQ):>10}')
print(f'    {"(proposta " + br(T_BRINQ_PROPOSTA) + " menos a cozinha " + br(COZINHA) + ")":<36}')
print(f'  {"ESTÚDIO · " + str(len(ESTUDIO)) + " itens":<38}{br(T_EST):>10}')
print(f'  {"TOTAL":<38}{br(TOTAL):>10}')
print(f'  {"DESCONTO (" + PCT + ")":<38}{"-"+br(DESCONTO):>10}')
print(f'  {"FECHADO":<38}{br(AVISTA):>10}')
print(f'    {"entrada em cheques":<36}{br(ENTRADA):>10}')
print(f'    {"saldo pós-entrega":<36}{br(SALDO):>10}')
