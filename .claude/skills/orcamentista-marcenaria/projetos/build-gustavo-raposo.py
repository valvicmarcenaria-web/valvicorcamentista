# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO — proposta · casa completa  [30/10/2026]

⭐ MESMO LAYOUT DO `build-michelle-arlei.py`, que o Jonathan cravou em 19/10:
   > "NUNCA APRESENTE PREÇO SEM ANTES GERAR VALOR na proposta. Fale um pouco
   >  da empresa e dos processos antes de expor valores. Mostre as duas
   >  linhas antes, fale das diferenças. (...) Descreva os itens junto com a
   >  listagem dos ambientes, só listando item por item mesmo."

   ⛔ A primeira versão desta peça FUGIU do layout: espremi três cartões no
     espaço de dois e as descrições não nomeavam o material. O CSS é o do
     Michelle, sem uma vírgula de diferença — o que muda são só as variações
     de três colunas, e elas mantêm a mesma generosidade de respiro.

[Jonathan, 30/10, segunda rodada] dez correções, todas aqui dentro:
   1 · o layout volta a ser o do Michelle
   2 · o conteúdo das páginas 3 a 5 dele é mantido
   3 · só imagem que mostra MARCENARIA
   4 · preço de cada ambiente NAS TRÊS LINHAS
   5 · uma página sobre as três opções, antes de qualquer valor
   6 · ⛔ SAI o downgrade da cozinha e do muxarabi — não se apresenta
   7 · prazo de 120 dias corridos
   8 · o termo de garantia e como se aciona
   9 · forma de pagamento, a escada do Michelle
  10 · o puxador Zen da cozinha

⛔ Sem metragem e sem contagem em nenhuma descrição.
⛔⛔ Nenhum número é digitado: tudo sai de `gustavo-raposo/cenarios.py`.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cen', P/'gustavo-raposo'/'cenarios.py')
cen = importlib.util.module_from_spec(spec); sys.modules['cen'] = cen
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(cen)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA = 'Gustavo Raposo', 'Condomínio Vale dos Pinhais · Nova Lima'
ARQ, DATA = 'Luiza Pacheco Arquitetura', '30 de outubro de 2026'
PRAZO, VALIDADE = '120 dias corridos', '7 dias úteis'
NP = 17                      # páginas · o assert no fim confere
N0 = 14                      # ⛔ a primeira página com preço

def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-gustavo-raposo'/n).read_bytes()).decode())
IMG = {n.stem: uri(n.name) for n in sorted((P/'img-gustavo-raposo').iterdir())}

# ⭐⭐ ESTE BLOCO É GERADO, NÃO DIGITADO. Os títulos e as descrições saíram
#   de um agente por ambiente lendo o LEVANTAMENTO (`gustavo-raposo/*.py`),
#   no estilo que o Jonathan aprovou no Michelle: duas frases curtas, sem
#   metragem, sem contagem, terminando no nome do material.
# ⛔ E as imagens passaram por triagem: um agente ABRIU cada render e cortou
#   as que não mostram marcenaria. Seis caíram, entre elas a que eu tinha
#   posto na capa — era mesa, cadeira e pedra, sem um móvel planejado.
#    (título, imagens, tags, acabamento, [(móvel, descrição)])
PG = [
 ('A varanda.',
  ['varanda-02'],
  ['Varanda', 'Lavabo'],
  'MDF Nogueira Caiena e Branco TX, Duratex, na varanda · Espelho prata colado no lavabo, sem MDF',
  [('Armário da parede', 'Portas de giro, gavetas e gavetão, com o nicho aberto da lava-louças e a estrutura que recebe a bancada de granito. MDF Nogueira Caiena, com interno em Branco TX.'),
   ('Gaveteiro da ilha', 'Embutido na ilha de alvenaria, com gavetas, gavetão e as gavetas verticais de temperos ao lado do forno. MDF Nogueira Caiena, com interno em Branco TX.'),
   ('Cristaleira de vidro temperado', 'Portas de vidro temperado incolor em cima e portas de giro embaixo, com prateleiras para a louça à mostra. MDF Nogueira Caiena, por dentro e por fora.'),
   ('Espelho da parede', 'Espelho fixo colado na parede, acima e abaixo da bancada, com corte, transporte e instalação por nossa conta. Espelho prata colado.')]),
 ('A cozinha<br>e a despensa.',
  ['cozinha-01', 'cozinha-02'],
  ['Cozinha', 'Despensa'],
  'Laca acetinada M048, Sayerlack, sobre MDF, com interno em MDF Branco TX, Duratex · MDF Branco Diamante, Linha Trama, Duratex',
  [('Armário superior', 'Portas de giro com moldura provençal e prateleira em cada vão. MDF laqueado acetinado M048, Sayerlack, com perfil de LED embutido correndo por baixo.'),
   ('Nicho sobre a geladeira', 'Nicho aberto que aproveita o vão acima da geladeira. Sem portas, ele é lacado por inteiro, até o fundo. MDF laqueado acetinado M048, Sayerlack.'),
   ('Armário inferior', 'Gavetões e básculas com moldura provençal, além do nicho da lava-louças, com a estrutura já preparada para receber a bancada de quartzito. MDF laqueado acetinado M048, Sayerlack, com interno em MDF branco.'),
   ('Armário da bancada do cooktop', 'Gaveteiro com gaveta de talheres, nicho de forno compatibilizado com o aparelho de vocês e armário de porta de giro com prateleira. MDF laqueado acetinado M048, Sayerlack, com interno em MDF branco.'),
   ('Prateleiras da parede menor', 'Prateleiras de parede com fixação invisível, sem suporte à vista, para as conservas e os mantimentos do dia a dia. MDF Branco Diamante, com estrutura de aço embutida entre as duas faces.'),
   ('Prateleiras da parede maior', 'Seguem a outra perna do L e vencem o vão livre sem apoio no meio, para o peso de verdade da despensa. MDF Branco Diamante.')]),
 ('A lavanderia<br>e a rouparia.',
  ['lavanderia-01', 'rouparia-01', 'lavanderia-02'],
  ['Lavanderia', 'Rouparia'],
  'MDF Branco Diamante, Linha Trama, e Branco TX, Duratex · MDF Off-White Suave e Nogueira Thar, Duratex, com interno em Branco',
  [('Armário superior', 'Básculas que abrem para cima, sobre a bancada, com puxador tipo cava usinado na própria frente. MDF Branco Diamante.'),
   ('Armário inferior', 'Gavetões em corrediça oculta, báscula e o painel fixo que fecha o vão do tanque. MDF Branco Diamante.'),
   ('Torre de vassouras', 'Porta de giro de piso a teto, com prateleiras no topo e o nicho alto para vassoura e rodo. MDF Branco Diamante.'),
   ('Armário da rouparia', 'Portas de giro com puxador em cava quadrada, maleiro no alto e prateleiras internas para a roupa de cama e as toalhas. Corpo em MDF Off-White Suave e frentes em MDF Nogueira Thar.')]),
 ('O office.',
  ['office-01'],
  ['Office'],
  'MDF Nogueira Caiena, Linha Design, Duratex',
  [('Painel muxarabi em réguas', 'Grade de réguas encaixadas uma a uma em meia-madeira, que filtra a vista e desenha a parede inteira do office. MDF Nogueira Caiena, com filetagem manual.')]),
 ('A suíte master.',
  ['suite-master-01', 'closet-master-01', 'banho-master-01'],
  ['Suíte master', 'Closet', 'Banho master'],
  'MDF Nogueira Caiena e Off-White Suave, Duratex · MDF Off-White Suave, Linha Sense, Duratex · MDF Nogueira Thar e Branco, Duratex',
  [('Painel da cabeceira', 'Reveste a parede da cabeceira inteira, com negativo vertical iluminado em LED e a porta do closet mimetizada dentro dele. MDF Nogueira Caiena.'),
   ('Porta pivotante mimetizada', 'Gira em pivô, sem batente nem marco: fechada, some no veio do painel. MDF Nogueira Caiena do lado da suíte e Off-White Suave do lado do closet.'),
   ('Armário da suíte', 'Portas de giro, maleiro, prateleiras internas e gavetões com puxador tipo cava. MDF Off-White Suave por dentro, com testeira, rodapé e frentes em Nogueira Caiena.'),
   ('Armário do closet', 'Armário aberto, com cabideiros, maleiro, prateleiras e, embaixo, as gavetas e sapateiras deslizantes com puxador tipo cava. MDF Off-White Suave.'),
   ('Armário da parede oposta', 'Cabideiro, maleiro e a coluna de prateleiras para roupa dobrada, com gavetas e sapateiras deslizantes embaixo. MDF Off-White Suave.'),
   ('Bandeira sobre a porta pivotante', 'Fecha o vão acima da porta pivotante da suíte, pela face voltada para o closet. MDF Off-White Suave.'),
   ('Armário superior com espelhos', 'Portas de espelho que correm sobre a bancada, com prateleiras internas para frascos e produtos do dia a dia. MDF Nogueira Thar, com perfil de LED embutido por baixo.'),
   ('Gabinete suspenso sob a bancada', 'Portas de giro nas pontas e gavetas no centro, todas com puxador em cava usinada, e suspenso do piso para a limpeza passar por baixo. MDF Nogueira Thar, com o interno em MDF Branco.')]),
 ('A suíte dos filhos.',
  ['suite01-01', 'suite01-02', 'banho01-01'],
  ['Suíte 01', 'Banho'],
  'MDF Nogueira Thar e Off-White Suave, Duratex, com internos em MDF Branco · MDF Azul Secreto, Linha Essencial, com interno em Branco, Duratex',
  [('Painel de cabeceira frisado', 'Painel frisado atrás das camas, com frisos verticais correndo de ponta a ponta. MDF Nogueira Thar, com perfil de LED embutido na peça.'),
   ('Armário de cabideiros e gavetas', 'Portas de correr flutuantes em MDF e espelho, abrindo para maleiro, cabideiros e gavetas com puxador cava. MDF Off-White Suave, com interno em Branco.'),
   ('Armário de prateleiras e sapateiras', 'Portas de correr flutuantes em MDF e espelho, com coluna de cabideiros de um lado e prateleiras, gavetas e sapateiras deslizantes do outro. MDF Off-White Suave, com interno em Branco.'),
   ('Módulo de canto do armário', 'Fecha a esquina do armário em L, com maleiro, prateleira e cabideiros contínuos que dobram o canto. MDF Off-White Suave, com interno em Branco.'),
   ('Mesa suspensa de estudo', 'Mesa de estudo suspensa, sem pés, fixada na parede e com saia frontal que dá a espessura aparente do tampo. MDF Nogueira Thar.'),
   ('Gaveteiro com rodízios', 'Gaveteiro solto sobre rodízios, que entra e sai de baixo da mesa, com gavetas de corrediça invisível e puxador cava. MDF Nogueira Thar.'),
   ('Bases de cama e gavetão', 'Bases de cama em caixa, com estrado em metalon, e gavetão que abre para a cama auxiliar. MDF Nogueira Thar.'),
   ('Gabinete suspenso sob a bancada', 'Gavetas e portas de giro com prateleira interna, abertas por cava usinada na própria frente, sem puxador aparente. Suspenso, flutua acima do piso e deixa o banheiro mais leve de limpar. MDF Azul Secreto, Linha Essencial.')]),
 ('A suíte das filhas.',
  ['suite02-01', 'suite02-02', 'banho02-01'],
  ['Suíte 02', 'Closet', 'Banho'],
  'MDF Nogueira Thar e Off-White Suave, Duratex · MDF Off-White Suave, Linha Sense, Duratex · MDF Pinole, com interno em MDF Branco, Duratex',
  [('Estante e armário de canto', 'Estante rasa com prateleiras iluminadas sobre um armário mais fundo, de gavetas em palhinha que abrem por fecho-toque. MDF Nogueira Thar, com perfil de LED embutido sob cada prateleira.'),
   ('Painéis de parede', 'Revestem a parede inteira das camas: os trechos atrás das cabeceiras são frisados e lavados por perfil de LED nas arestas, e o restante fica liso. MDF Nogueira Thar frisado e Off-White Suave.'),
   ('Porta pivotante mimetizada', 'Folha de acesso ao closet, mimetizada no painel liso da parede, com puxador tipo cava e tranca pelo lado de dentro. MDF Off-White Suave.'),
   ('Penteadeira suspensa', 'Tampo suspenso sobre pés cilíndricos metálicos, com gavetas rasas de frente em palhinha e abertura por fecho-toque. MDF Nogueira Thar com palhinha natural.'),
   ('Armários de canto arredondado', 'Ficam nas pontas da penteadeira, com gavetas de palhinha e fecho-toque e a faixa cheia que forma o canto arredondado. MDF Nogueira Thar com palhinha natural.'),
   ('Mesa de cabeceira', 'Fica entre as camas, apoiada na estrutura cilíndrica dourada, com gavetas de palhinha e puxador redondo dourado à vista. MDF Nogueira Thar com palhinha natural.'),
   ('Bases de cama com gavetão', 'Cada base recebe gavetão de cama auxiliar, com estrado em metalon sob os colchões. MDF Nogueira Thar.'),
   ('Armário de cabideiros', 'Armário aberto, sem portas, com cabideiro de roupa longa, cabideiro de roupa curta e o maleiro no alto para malas e roupa de cama. MDF Off-White Suave.'),
   ('Armário de prateleiras e gavetas', 'Coluna de prateleiras com gavetas e sapateiras que deslizam em corrediça oculta, abertas por puxador cava, e a coluna de cabideiros ao lado. MDF Off-White Suave.'),
   ('Módulo de canto em L', 'Resolve o encontro do armário em L e leva os cabideiros contínuos que viram a esquina, com o maleiro seguindo por cima. MDF Off-White Suave.'),
   ('Gabinete suspenso sob a bancada', 'Gavetas e portas de giro com puxador tipo cava usinado nas frentes, e prateleiras internas atrás das portas. O móvel é suspenso, flutuando acima do piso, em MDF Pinole com interno em MDF Branco.')]),
 ('Hóspedes e os<br>banhos sociais.',
  ['hospedes-02', 'banho-hospedes-01', 'banho-social-01'],
  ['Suíte hóspedes', 'Banho hóspedes', 'Banho social'],
  'MDF Off-White Suave e Branco, Duratex · MDF Nogueira Thar e Branco, Duratex',
  [('Armário da suíte', 'Folhas de correr flutuantes, maleiro, cabideiro e prateleiras, com gavetas e sapateiras deslizantes embaixo. MDF Off-White Suave, com interno em MDF Branco.'),
   ('Gabinete suspenso sob a bancada', 'Portas de giro com prateleira interna e puxador em cava usinada na própria frente. Fica suspenso do piso, sob a bancada. MDF Nogueira Thar, com interno em MDF Branco.'),
   ('Gabinete suspenso sob a bancada', 'Portas de giro com puxador tipo cava e prateleiras internas, suspenso para deixar o piso livre embaixo da bancada. MDF Nogueira Thar, com interno em MDF Branco.')]),
 ('O homeschooling.',
  ['homeschooling-01', 'homeschooling-02'],
  ['Homeschooling'],
  'MDF Cinza Fóssil, Linha Velluto, e Azul Secreto, Duratex',
  [('Nicho em Azul Secreto', 'Nicho aberto com prateleiras e perfil de LED embutido em cada vão, apoiado sobre o armário inferior. O fundo fica à vista e é ele que traz a cor para o ambiente. MDF Azul Secreto.'),
   ('Armário inferior', 'Portas de giro com prateleira interna e colunas de gavetas e gavetões, com puxador em cava usinada na própria frente. MDF Cinza Fóssil, Linha Velluto.'),
   ('Armário de estante', 'Portas de giro altas, com prateleiras internas em toda a largura, para livro e material de estudo. MDF Cinza Fóssil, Linha Velluto.')]),
]

CSS = """
:root{
  --ink:#1E1B17; --soft:#5E574E; --mut:#9A9287; --line:#E0D8CB;
  --hair:#EFE9DF; --sand:#F6F1E8; --wood:#A8794A; --wood-lt:#D9BD96;
  --dk:#262220; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.5pt;line-height:1.55;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:15mm 17mm 14mm;height:100%;display:flex;flex-direction:column;}
.foot{margin-top:auto;padding-top:6mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:6.8pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.4px solid var(--ink);padding-bottom:3mm;flex:none;}
.hd .b{font-size:7.6pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:6.8pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--wood);font-weight:700;margin-top:5mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;
  line-height:1.03;font-weight:600;letter-spacing:-.02em;margin-top:1.5mm;flex:none;}
.lead{color:var(--soft);font-size:9.6pt;line-height:1.5;margin-top:3mm;
  max-width:132mm;flex:none;}
.lead b{color:var(--ink);font-weight:600;}

/* ── capa ───────────────────────────────────────────────────────────── */
.cv{height:297mm;display:flex;flex-direction:column;}
.cv .ph{flex:1;overflow:hidden;line-height:0;background:#000;}
.cv .ph img{width:100%;height:100%;object-fit:cover;}
.cv .bt{background:var(--dk);color:#F4EFE6;padding:13mm 17mm 12mm;flex:none;}
.cv .mark{font-size:8pt;letter-spacing:.42em;text-transform:uppercase;
  color:#EFE6D6;font-weight:700;}
.cv h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:42pt;
  line-height:1;font-weight:600;letter-spacing:-.02em;margin:5mm 0 0;}
.cv .sub{font-size:10.5pt;color:#C6BDB0;margin-top:4mm;font-weight:300;}
.cv .sub b{color:#EFE7DA;font-weight:500;}

/* ── mosaico: fotos MENORES, composição assimétrica que alterna ─────── */
.mos{margin:6mm -17mm 0;display:grid;gap:2mm;line-height:0;overflow:hidden;
  flex:1 1 auto;min-height:68mm;max-height:128mm;}
.mos img{width:100%;height:100%;object-fit:cover;display:block;}
.mos.a{grid-template-columns:118mm 1fr;}
.mos.b{grid-template-columns:1fr 118mm;}
.mos .st{display:grid;grid-template-rows:1fr 1fr;gap:2mm;}
.mos.solo{grid-template-columns:1fr;min-height:112mm;}
.mos.tall{max-height:none;min-height:150mm;}

/* ── lista item a item ──────────────────────────────────────────────── */
.lista{margin-top:7mm;columns:2;column-gap:10mm;flex:none;}
.li{break-inside:avoid;padding:3.6mm 0 3.6mm 5mm;border-left:2px solid var(--wood-lt);
  margin-bottom:3mm;}
.acab{margin-top:6mm;padding-top:4mm;border-top:1px solid var(--line);
  display:flex;align-items:baseline;gap:6mm;flex:none;}
.acab .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;flex:none;}
.acab .v{font-size:9pt;color:var(--soft);}
.acab .v b{color:var(--ink);font-weight:600;}
.li .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;
  font-weight:600;line-height:1.1;letter-spacing:-.01em;}
.li .d{color:var(--soft);font-size:8.2pt;line-height:1.42;margin-top:1.2mm;}
.tags{margin-top:5mm;display:flex;gap:3mm;flex-wrap:wrap;flex:none;}
.tags span{font-size:6.6pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--wood);font-weight:700;border:1px solid var(--line);
  border-radius:20px;padding:1.6mm 4mm;}

/* ── empresa e processo ─────────────────────────────────────────────── */
.duo{display:grid;grid-template-columns:1fr 1fr;gap:9mm;margin-top:7mm;flex:none;}
.step{display:grid;grid-template-columns:9mm 1fr;gap:4mm;padding:3.4mm 0;
  border-top:1px solid var(--line);}
.step:first-of-type{border-top:1.4px solid var(--ink);}
.step .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:700;color:var(--wood-lt);line-height:.9;}
.step .t{font-size:10.5pt;font-weight:600;}
.step .d{color:var(--soft);font-size:8.2pt;line-height:1.42;margin-top:.8mm;}
.sel{background:var(--sand);border-radius:3px;padding:8mm;flex:none;}
.sel .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.sel .d{color:var(--soft);font-size:8.6pt;line-height:1.5;margin-top:2mm;}
.sel .d b{color:var(--ink);font-weight:600;}

/* ── as duas linhas ─────────────────────────────────────────────────── */
.vs{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:6mm;flex:none;}
.vs .c{border:1px solid var(--line);border-radius:3px;padding:9mm 8mm 8mm;}
.vs .c.on{background:var(--dk);border-color:var(--dk);color:#F4EFE6;}
.vs .k{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.vs .c.on .k{color:var(--wood-lt);}
.vs .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:20pt;
  font-weight:600;margin-top:2mm;line-height:1.05;}
.vs .g{font-family:'Cormorant Garamond',Georgia,serif;font-size:36pt;
  font-weight:700;line-height:1;margin-top:4mm;letter-spacing:-.02em;}
.vs .gl{font-size:7.2pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;margin-top:1.5mm;}
.vs .c.on .gl{color:#9A9287;}
.vs .p{margin-top:5mm;padding-top:4mm;border-top:1px solid var(--line);
  font-size:9pt;color:var(--soft);}
.vs .c.on .p{border-top:1px solid rgba(255,255,255,.2);color:#BDB5A8;}
.vs .p b{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
  font-weight:700;color:var(--ink);display:block;margin-top:1mm;
  font-variant-numeric:tabular-nums;}
.vs .c.on .p b{color:#fff;}
.dif{margin-top:6mm;flex:none;}
.dif .r{display:grid;grid-template-columns:30mm 1fr 1fr;gap:6mm;
  padding:4.2mm 0;border-top:1px solid var(--line);align-items:baseline;}
.dif .r:first-child{border-top:1.4px solid var(--ink);}
.dif .k{font-size:6.8pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.dif .a{color:var(--soft);font-size:8.8pt;}
.dif .b2{font-size:8.8pt;font-weight:600;}

/* ── valores ────────────────────────────────────────────────────────── */
.rows{margin-top:6mm;flex:none;}
.row{display:flex;justify-content:space-between;align-items:baseline;
  padding:2.4mm 0;border-top:1px solid var(--line);font-size:10pt;}
.row:first-child{border-top:1.4px solid var(--ink);}
.row .v{font-variant-numeric:tabular-nums;font-weight:600;}
.vista{margin-top:7mm;background:var(--dk);color:#F4EFE6;border-radius:3px;
  padding:9mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.vista .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--wood-lt);font-weight:700;}
.vista .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:44pt;
  font-weight:700;color:#fff;line-height:.9;letter-spacing:-.03em;
  margin-top:3mm;font-variant-numeric:tabular-nums;}
.vista .s{font-size:9pt;color:#C2BAAD;margin-top:3mm;}
.vista .rt{text-align:right;flex:none;}
.vista .rt .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:#8E867A;font-weight:700;}
.vista .rt .v{font-size:15pt;color:#B6AEA1;margin-top:1.5mm;
  font-variant-numeric:tabular-nums;}
.pay{margin-top:6mm;flex:none;}
.pay .r{display:flex;justify-content:space-between;align-items:baseline;gap:6mm;
  padding:2.6mm 0;border-top:1px solid var(--line);font-size:9.2pt;color:var(--soft);}
.pay .r:first-child{border-top:1.4px solid var(--ink);}
.pay .r b{color:var(--ink);font-weight:600;}
.pay .r .x{flex:none;font-size:8.6pt;letter-spacing:.06em;color:var(--wood);
  font-weight:700;}
.pay .r.on{color:var(--ink);}
.pay .r.on .x{font-size:10pt;}

/* ── condições ──────────────────────────────────────────────────────── */
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:6mm;
  padding-top:4mm;border-top:1.4px solid var(--ink);flex:none;}
.four .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.four .v{font-size:11pt;font-weight:600;margin-top:1.2mm;}
.four .s{color:var(--soft);font-size:7.6pt;margin-top:.8mm;line-height:1.35;}
.notes{margin-top:6mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;
  flex:none;}
.notes .bx{background:var(--sand);border-radius:3px;padding:5.5mm 6mm;}
.notes .bx.w{background:#fff;border:1px solid var(--line);}
.notes .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.notes .d{color:var(--soft);font-size:8pt;line-height:1.45;margin-top:2mm;}
.notes .d b{color:var(--ink);font-weight:600;}
"""

# ⭐ O CSS acima é o do Michelle e Arlei, sem uma vírgula de diferença. O que
#   vem abaixo são só as variações de TRÊS colunas — e elas guardam a mesma
#   generosidade de respiro dos cartões dele, que foi o que fugiu na v1.
EXTRA = """
/* ── TRÊS linhas em vez de duas, com o mesmo fôlego ─────────────────── */
.vs.tri{grid-template-columns:repeat(3,1fr);gap:3.5mm;}
.vs.tri .c{padding:8mm 6.5mm 7mm;}
.vs.tri .n{font-size:16pt;line-height:1.08;}
.vs.tri .g{font-size:30pt;margin-top:4mm;}
.vs.tri .p{margin-top:4.5mm;padding-top:3.5mm;}
.vs.tri .p b{font-size:15pt;}
.dif.tri .r{grid-template-columns:23mm 1fr 1fr 1fr;gap:4.5mm;padding:3.8mm 0;}
.dif.tri .a,.dif.tri .b2,.dif.tri .c3{font-size:8.1pt;line-height:1.4;}
.dif.tri .c3{font-weight:600;}
.dif.tri .b2{font-weight:500;color:var(--soft);}

/* ── as três opções, por dentro ─────────────────────────────────────── */
.op{margin-top:6mm;flex:none;}
.op .b{display:grid;grid-template-columns:30mm 1fr;gap:7mm;padding:5mm 0;
  border-top:1px solid var(--line);align-items:start;}
.op .b:first-child{border-top:1.4px solid var(--ink);}
.op .k{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.op .nm{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
  font-weight:600;line-height:1.08;margin-top:1.5mm;}
.op .gg{font-size:7.4pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--mut);font-weight:700;margin-top:1.5mm;}
.op .d{color:var(--soft);font-size:8.7pt;line-height:1.5;}
.op .d b{color:var(--ink);font-weight:600;}
.op .d em{font-style:normal;color:var(--wood);font-weight:600;}

/* ── preço por ambiente nas TRÊS linhas ─────────────────────────────── */
.t3{margin-top:5mm;flex:none;width:100%;border-collapse:collapse;}
.t3 th{font-size:6.4pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--wood);font-weight:700;text-align:right;padding:0 0 2.2mm;
  border-bottom:1.4px solid var(--ink);}
.t3 th:first-child{text-align:left;}
.t3 td{font-size:8.6pt;padding:1.9mm 0;border-bottom:1px solid var(--hair);
  text-align:right;font-variant-numeric:tabular-nums;}
.t3 td:first-child{text-align:left;color:var(--soft);}
.t3 td.on{font-weight:600;}
.t3 tr.tot td{font-size:10.5pt;font-weight:600;padding-top:3mm;
  border-top:1.4px solid var(--ink);border-bottom:none;}
.t3 tr.tot td:first-child{color:var(--ink);}
.nota{margin-top:3.5mm;font-size:7.6pt;line-height:1.45;color:var(--mut);flex:none;}
.nota b{color:var(--soft);font-weight:600;}

/* ── garantia ───────────────────────────────────────────────────────── */
.gar{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-top:6mm;flex:none;}
.gar .c{border:1px solid var(--line);border-radius:3px;padding:7mm 6mm;}
.gar .c.on{background:var(--dk);border-color:var(--dk);color:#F4EFE6;}
.gar .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.gar .c.on .k{color:var(--wood-lt);}
.gar .g{font-family:'Cormorant Garamond',Georgia,serif;font-size:28pt;
  font-weight:700;line-height:1;margin-top:3mm;}
.gar .d{font-size:8pt;line-height:1.42;color:var(--soft);margin-top:2.5mm;}
.gar .c.on .d{color:#BDB5A8;}
.ac{margin-top:6mm;flex:none;}
.ac .r{display:grid;grid-template-columns:9mm 1fr;gap:4mm;padding:3.4mm 0;
  border-top:1px solid var(--line);}
.ac .r:first-child{border-top:1.4px solid var(--ink);}
.ac .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:700;color:var(--wood-lt);line-height:.9;}
.ac .t{font-size:10pt;font-weight:600;}
.ac .d{color:var(--soft);font-size:8.2pt;line-height:1.42;margin-top:.8mm;}
"""

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · {OBRA}</span><span>{n} / {NP}</span></div>')
def head():
    return (f'<div class="hd"><div class="b">Valvic Marcenaria</div>'
            f'<div class="m">{CLIENTE} · {DATA}</div></div>')

LIN = ('Telescópica', 'Hettich', 'Blum')     # ⭐ sempre da entrada ao topo

# ⭐ o puxador ganha linha própria onde ele foi especificado
PUX = {'A cozinha<br>e a despensa.': cen.PUXADOR_COZINHA + ', em todas as frentes'}
pg = []
# ── 1 · capa ────────────────────────────────────────────────────────────
pg.append(f"""<div class="page"><div class="cv">
  <div class="ph"><img src="{IMG['cozinha-03']}" alt=""></div>
  <div class="bt">
    <div class="mark">Valvic Marcenaria</div>
    <h1>A casa<br>inteira.</h1>
    <div class="sub"><b>{CLIENTE}</b> · {OBRA}<br>Projeto <b>{ARQ}</b></div>
  </div>
</div></div>""")

# ── 2 · a empresa e o processo ──────────────────────────────────────────
ETAPAS = [
 ('Medição', 'Vamos ao local antes de cortar e conferimos cada medida do '
  'projeto executivo. É aí que fecham as alturas do piso ao forro.'),
 ('Detalhamento', 'Compatibilizamos a marcenaria com a elétrica, com os '
  'eletrodomésticos de vocês e com a marmoraria, peça por peça.'),
 ('Corte', 'CNC próprio, com furação oculta — a cavilha só aparece onde '
  'ninguém vê. É o que deixa a face limpa e o móvel no esquadro.'),
 ('Montagem', 'Equipe nossa, não terceirizada. Quem monta responde pelo que '
  'cortou.'),
 ('Entrega', 'Regulagem de cada porta e cada gaveta, e a iluminação já '
  'instalada e acesa.'),
]
steps = ''.join(f'<div class="step"><div class="n serif">{i:02d}</div>'
                f'<div><div class="t">{t}</div><div class="d">{d}</div></div>'
                f'</div>' for i, (t, d) in enumerate(ETAPAS, 1))
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Quem faz</div>
  <div class="h1 serif">Marcenaria própria,<br>do desenho à regulagem.</div>
  <div class="lead">A Valvic é marcenaria de <b>fábrica própria em Belo
  Horizonte</b>. Projeto, corte, montagem e instalação saem da mesma casa —
  entre o desenho da arquiteta e a última porta regulada <b>não entra
  terceiro nenhum</b>. É por isso que conseguimos responder por prazo e por
  garantia sem repassar a conversa para outro.</div>

  <div class="mos a" style="flex:none;height:84mm;min-height:0;max-height:84mm;">
    <img src="{IMG['suite-master-01']}" alt="">
    <div class="st"><img src="{IMG['closet-master-01']}" alt="">
      <img src="{IMG['rouparia-01']}" alt=""></div>
  </div>

  <div class="eye">Como fazemos</div>
  <div style="margin-top:3mm;flex:none;">{steps}</div>
  {foot(2)}
</div></div>""")

# ── 3 · as TRÊS linhas, ANTES de qualquer preço ─────────────────────────
#    ⭐ é a página 3 do Michelle, item por item, com uma coluna a mais
DIF = [
 ('Corrediça',
  'Telescópica, com o trilho aparente na lateral da gaveta e sem amortecedor '
  'de fechamento.',
  'Oculta alemã: o trilho some por baixo, a gaveta abre inteira e não mostra '
  'ferragem na lateral.',
  'Oculta Blum: a mesma discrição da alemã, com o curso mais macio e a maior '
  'capacidade de carga das três.'),
 ('Dobradiça',
  'Nacional, com abertura de noventa graus.',
  'Alemã, com amortecedor e regulagem nos três sentidos.',
  'Blum, com amortecedor e regulagem nos três sentidos.'),
 ('Básculas',
  'Articulador premium de molas: a porta sobe sozinha e para onde você '
  'soltar. O mesmo nas três linhas.',
  'O mesmo articulador premium.', 'O mesmo articulador premium.'),
 ('Iluminação',
  'Perfil de LED embutido na própria peça, com difusor sem pontos e cor '
  'estável no tempo. O mesmo nas três linhas.',
  'O mesmo perfil, entregue instalado.', 'O mesmo perfil, entregue instalado.'),
 ('Garantia', cen.CEN['Telescópica']['gar'], cen.CEN['Hettich']['gar'],
  cen.CEN['Blum']['gar']),
]
difs = ''.join(f'<div class="r"><div class="k">{k}</div><div class="a">{a}</div>'
               f'<div class="b2">{b}</div><div class="c3">{c}</div></div>'
               for k, a, b, c in DIF)
cards = ''.join(
  f'<div class="c{" on" if n == "Blum" else ""}"><div class="k">{n}</div>'
  f'<div class="n serif">{cen.CEN[n]["chamada"]}</div>'
  f'<div class="g serif">{cen.CEN[n]["gar"]}</div>'
  f'<div class="gl">de garantia</div></div>' for n in LIN)
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Uma escolha</div>
  <div class="h1 serif">Três linhas. A diferença<br>está na ferragem.</div>
  <div class="lead">O desenho, os padrões de MDF, a laca da cozinha, a
  furação oculta e o acabamento são <b>os mesmos nas três</b>. O que muda é
  a peça que vocês tocam todo dia — e é ela que decide <b>quanto tempo o
  móvel continua fechando bem</b>.</div>

  <div class="vs tri">{cards}</div>
  <div class="dif tri">{difs}</div>

  <div class="sel" style="margin-top:5mm;">
    <div class="k">O que não muda</div>
    <div class="d">Os <b>padrões de MDF especificados pela arquiteta</b>, a
    <b>laca acetinada da cozinha</b>, a <b>furação oculta</b>, o <b>puxador
    cava usinado na própria peça</b>, as <b>almas de aço</b> nas prateleiras
    de vão longo, a <b>iluminação entregue instalada</b> e a <b>equipe
    própria</b> do corte à montagem.</div>
  </div>
  {foot(3)}
</div></div>""")

# ── 4 · as três opções, por dentro — ainda SEM preço ────────────────────
OPC = [
 ('Telescópica', 'A linha de entrada',
  'A corrediça telescópica corre sobre esferas e <b>mostra o trilho na '
  'lateral da gaveta</b> quando ela abre. Não tem amortecedor: a gaveta '
  'fecha no impulso que você der. É a ferragem que a maior parte do mercado '
  'entrega como padrão, e ela cumpre o que promete — <em>o que muda é por '
  'quanto tempo</em>.'),
 ('Hettich', 'O padrão da casa',
  'A corrediça oculta alemã corre <b>por baixo da caixa da gaveta</b>: você '
  'abre e não vê ferragem nenhuma, só a madeira. A gaveta sai inteira, o '
  'fechamento é amortecido e a regulagem é fina nos três sentidos. '
  '<em>É a linha que especificamos nesta casa</em> e a que o projeto da '
  'arquiteta pressupõe.'),
 ('Blum', 'O topo',
  'A mesma discrição da alemã, com o <b>curso mais macio e a maior '
  'capacidade de carga</b> das três — é o que se sente num gavetão cheio, '
  'que é onde ferragem fraca aparece primeiro. A Blum é a referência do '
  'mercado, e é por isso que respondemos por ela <em>por trinta anos</em>.'),
]
ops = ''.join(
  f'<div class="b"><div><div class="k">{k}</div>'
  f'<div class="nm serif">{cen.CEN[k]["chamada"]}</div>'
  f'<div class="gg">{cen.CEN[k]["gar"]} de garantia</div></div>'
  f'<div class="d">{d}</div></div>' for k, _, d in OPC)
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">As três opções</div>
  <div class="h1 serif">O que vocês<br>vão sentir na mão.</div>
  <div class="lead">A ferragem é a única peça da marcenaria que <b>se usa
  todo dia e se desgasta</b>. O MDF não cansa, a pintura não cansa, a
  furação não cansa. A corrediça e a dobradiça, sim — e é por isso que a
  escolha entre as três linhas <b>vale para a casa toda</b>: a garantia do
  conjunto segue sempre a ferragem de menor linha presente.</div>

  <div class="op">{ops}</div>

  <div class="sel" style="margin-top:6mm;">
    <div class="k">Como escolher</div>
    <div class="d">Abra uma gaveta de cada linha antes de decidir — <b>em
    trinta segundos a mão resolve o que a tabela não resolve</b>. Levamos as
    três amostras à obra na medição, sem compromisso.</div>
  </div>
  {foot(4)}
</div></div>""")

# ── 5…13 · os ambientes, SEM preço ──────────────────────────────────────
for n, (titulo, imgs, ambs, acab, itens) in enumerate(PG, start=5):
    lado = 'a' if n % 2 == 0 else 'b'          # ⭐ alterna a cada página
    if len(imgs) == 1:
        mos, cls = f'<img src="{IMG[imgs[0]]}" alt="">', 'solo'
        if len(itens) <= 2:         # ⭐ ambiente de peça única
            cls = 'solo tall'
    elif len(imgs) == 3:
        st = (f'<div class="st"><img src="{IMG[imgs[1]]}" alt="">'
              f'<img src="{IMG[imgs[2]]}" alt=""></div>')
        mos = (f'<img src="{IMG[imgs[0]]}" alt="">{st}' if lado == 'a'
               else f'{st}<img src="{IMG[imgs[0]]}" alt="">')
        cls = lado
    else:
        mos = ''.join(f'<img src="{IMG[i]}" alt="">'
                      for i in (imgs if lado == 'a' else imgs[::-1]))
        cls = lado
    lis = ''.join(f'<div class="li"><div class="t">{t}</div>'
                  f'<div class="d">{d}</div></div>' for t, d in itens)
    tags = ''.join(f'<span>{a}</span>' for a in ambs)
    pux = (f'<div class="acab" style="margin-top:3mm;padding-top:3mm;">'
           f'<div class="k">Puxador</div><div class="v">{PUX[titulo]}</div>'
           f'</div>' if titulo in PUX else '')
    pg.append(f"""<div class="page"><div class="pad">
      {head()}
      <div class="eye">Ambiente</div>
      <div class="h1 serif">{titulo}</div>
      <div class="tags">{tags}</div>
      <div class="mos {cls}">{mos}</div>
      <div class="lista">{lis}</div>
      <div class="acab"><div class="k">Acabamentos</div>
        <div class="v">{acab}</div></div>
      {pux}
      {foot(n)}
    </div></div>""")

# ── 14 · o investimento, ambiente por ambiente, NAS TRÊS LINHAS ─────────
#    ⛔ [Jonathan 30/10] "a apresentação de preços de cada ambiente precisa
#      ser nas tres linhas (obs, a despensa e o office nao muda de valor nas
#      3)".
#    ⛔⛔ A OBSERVAÇÃO VIROU QUANDO AS MCs MUDARAM, e eu quase imprimi a
#      versão velha dela. O que não muda nesses ambientes é o CUSTO: nenhum
#      leva gaveta nem porta de giro, então não há corrediça nem dobradiça
#      para trocar — e o LAVABO entra no grupo junto com os outros dois. Mas
#      o PREÇO muda, porque a MC da linha telescópica é 35% e a das outras
#      duas é 42%. Com as MCs antigas (42/35/35) eles batiam entre Hettich e
#      telescópica; com as de agora (42/42/35) eles batem entre Hettich e
#      Blum. ⭐ A lição: AFIRME O QUE A PEÇA IMPRIME. Eu tinha travado a
#      igualdade de CUSTO e escrito igualdade de PREÇO — o assert passava e
#      a frase mentia.
IGUAIS = [i for i, (nome, _, pares, dobr) in enumerate(cen.AMB)
          if pares == 0 and dobr == 0]
assert {cen.AMB[i][0] for i in IGUAIS} == {'02 Lavabo', '04 Despensa', '07 Office'}, \
    [cen.AMB[i][0] for i in IGUAIS]
# ⛔ e agora a trava da AFIRMAÇÃO: o preço desses três tem de bater entre
#   Hettich e Blum, e tem de DIFERIR da telescópica.
for _i in IGUAIS:
    assert abs(cen.CEN['Hettich']['pv'][_i]
               - cen.CEN['Blum']['pv'][_i]) < 0.01, cen.AMB[_i][0]
    assert abs(cen.CEN['Hettich']['pv'][_i]
               - cen.CEN['Telescópica']['pv'][_i]) > 1.0, cen.AMB[_i][0]
# ⭐ a coluna da Hettich vai em negrito: é a linha especificada no projeto
_cls = {n: ' class="on"' if n == 'Hettich' else '' for n in LIN}
linhas = ''.join(
  f'<tr><td>{nome[3:]}</td>'
  + ''.join(f'<td{_cls[n]}>{br(cen.CEN[n]["pv"][i])}</td>' for n in LIN)
  + '</tr>' for i, (nome, *_) in enumerate(cen.AMB))
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento · ambiente por ambiente</div>
  <div class="h1 serif">Dezenove ambientes,<br>nas três linhas.</div>
  <div class="lead">Cada ambiente foi levantado <b>peça por peça do projeto
  executivo</b> — nada é rateio nem estimativa por metro quadrado. A
  <b>forma de pagamento está na página seguinte</b>.</div>
  <table class="t3">
    <tr><th>Ambiente</th>{''.join(f'<th>{n}</th>' for n in LIN)}</tr>
    {linhas}
    <tr class="tot"><td>A casa inteira</td>
      {''.join(f'<td>{br(cen.CEN[n]["preco"])}</td>' for n in LIN)}</tr>
  </table>
  <div class="nota"><b>Lavabo, Despensa e Office têm o mesmo valor nas
  linhas Hettich e Blum.</b> Nenhum dos três leva gaveta ou porta de giro —
  o lavabo é espelho, a despensa é prateleira e o office é painel —, então
  não existe corrediça nem dobradiça neles para trocar de uma linha para a
  outra.</div>
  {foot(N0)}
</div></div>""")

# ── 15 · o total e a FORMA DE PAGAMENTO ─────────────────────────────────
_on2 = {n: ' on' if n == 'Hettich' else '' for n in LIN}
cards2 = ''.join(
  f'<div class="c{_on2[n]}"><div class="k">{n}</div>'
  f'<div class="n serif">{cen.CEN[n]["chamada"]}</div>'
  f'<div class="g serif">{cen.CEN[n]["gar"]}</div>'
  f'<div class="gl">de garantia</div>'
  f'<div class="p">A casa inteira<b>R$ {br(cen.CEN[n]["preco"])}</b></div></div>'
  for n in LIN)
REF = 'Hettich'
# ⛔ SEM PERCENTUAL E SEM SEGUNDO VALOR: só a forma, como o Jonathan mandou.
FORMAS = [rot for rot, _, _ in cen.ESCADA]
pays = ''.join(f'<div class="r{" on" if i == 0 else ""}"><div>{rot}</div>'
               f'</div>' for i, rot in enumerate(FORMAS))
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento · as três linhas</div>
  <div class="h1 serif">Dois anos, dez, ou trinta.</div>
  <div class="lead">A mesma casa, o mesmo desenho e os mesmos padrões. A
  diferença é a <b>ferragem</b> — e o tempo pelo qual respondemos por ela.</div>

  <div class="vs tri">{cards2}</div>

  <div class="vista" style="margin-top:6mm;padding:8mm 9mm;">
    <div><div class="lab">A casa inteira · linha Hettich</div>
      <div class="big">R$ {br(cen.CEN[REF]['preco'])}</div>
      <div class="s">Dezenove ambientes, da varanda ao homeschooling, com
      projeto, corte, montagem e instalação por equipe própria.</div></div>
    <div class="rt"><div class="k">Garantia</div>
      <div class="v" style="font-size:19pt;color:#fff;">{cen.CEN[REF]['gar']}</div></div>
  </div>

  <div class="eye" style="margin-top:6mm;">Forma de pagamento</div>
  <div class="pay" style="margin-top:3mm;">{pays}</div>
  <div class="nota"><b>A entrada abre a produção</b> e o saldo vence na
  entrega, depois da montagem e da regulagem de cada porta e cada gaveta.</div>
  {foot(N0+1)}
</div></div>""")

# ── 16 · a GARANTIA: o termo e como se aciona ───────────────────────────
#    ⭐ [Jonathan 30/10] "fale do nosso termo de garantia e formato de
#      acionamento". Os prazos e o atendimento saem de
#      `closer-vendas/referencias/garantia.md`, que é a política oficial.
gars = ''.join(
  f'<div class="c{" on" if n == "Hettich" else ""}"><div class="k">{n}</div>'
  f'<div class="g serif">{cen.CEN[n]["gar"]}</div>'
  f'<div class="d">{d}</div></div>'
  for n, d in zip(LIN, (
    'Sobre a marcenaria, a ferragem e a montagem.',
    'Sobre a marcenaria, a ferragem e a montagem. É a linha especificada '
    'neste projeto.',
    'Sobre a marcenaria, a ferragem e a montagem — o maior prazo que a casa '
    'oferece.')))
PASSOS = [
 ('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a '
  'fábrica. Não há central, não há protocolo e não há intermediário.'),
 ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, '
  'contado em dias úteis a partir do chamado.'),
 ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a '
  'equipe vai ao local. Dentro do prazo de garantia, a visita e o reparo '
  'não têm custo.'),
]
passos = ''.join(f'<div class="r"><div class="n serif">{i:02d}</div>'
                 f'<div><div class="t">{t}</div><div class="d">{d}</div></div>'
                 f'</div>' for i, (t, d) in enumerate(PASSOS, 1))
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Garantia</div>
  <div class="h1 serif">O termo é assinado<br>na entrega.</div>
  <div class="lead">A garantia da Valvic <b>é escalonada pela ferragem</b>,
  e vale para a casa inteira pelo prazo da <b>linha de menor tempo presente
  no projeto</b>. Não é promessa de proposta: é <b>termo assinado no dia da
  entrega</b>, junto com o guia de conservação do móvel.</div>

  <div class="gar">{gars}</div>

  <div class="eye" style="margin-top:7mm;">Como se aciona</div>
  <div class="ac">{passos}</div>

  <div class="notes" style="margin-top:6mm;">
    <div class="bx"><div class="k">O que o termo cobre</div>
      <div class="d">A <b>marcenaria</b> — estrutura, painéis, frentes e
      acabamento. A <b>ferragem de movimento</b>, pelo prazo da linha
      escolhida. A <b>montagem e a instalação</b>. As <b>instalações e
      regulagens</b> têm garantia de <b>dois anos</b> em qualquer
      linha.</div></div>
    <div class="bx w"><div class="k">O que fica de fora</div>
      <div class="d">A <b>iluminação em LED</b>, que é componente eletrônico
      e segue a garantia do fabricante. O <b>desgaste de uso</b>, o dano por
      <b>umidade ou infiltração</b> vinda da obra, e a alteração feita por
      terceiro no móvel depois da entrega. O termo traz também as
      <b>obrigações de conservação</b> do contratante.</div></div>
  </div>
  {foot(N0+2)}
</div></div>""")

# ── 17 · condições ──────────────────────────────────────────────────────
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Condições</div>
  <div class="h1 serif">Como fechamos.</div>

  <div class="mos a" style="max-height:72mm;">
    <img src="{IMG['suite02-01']}" alt="">
    <div class="st"><img src="{IMG['homeschooling-01']}" alt="">
      <img src="{IMG['lavanderia-01']}" alt=""></div>
  </div>

  <div class="four">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div>
      <div class="s">Do aceite, da entrada e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">2 · 10 · 30 anos</div>
      <div class="s">Conforme a linha escolhida.</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div>
      <div class="s">Do corte à instalação.</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div>
      <div class="s">A partir desta data.</div></div>
  </div>

  <div class="notes">
    <div class="bx"><div class="k">O que não está incluso</div>
      <div class="d">Toda a <b>pedra</b> — bancadas, rodobancas, sóculos,
      soleiras e a cuba esculpida do lavabo, que são marmoraria. Os
      <b>eletrodomésticos</b>, as <b>cubas, torneiras e louças</b>. A
      <b>elétrica</b> — pontos, circuitos, drivers e interruptores. As
      <b>esquadrias</b>, o <b>forro</b>, o <b>piso</b>, a <b>pintura de
      parede</b> e o <b>corpo de alvenaria</b> da ilha da varanda.</div></div>
    <div class="bx w"><div class="k">A confirmar antes da produção</div>
      <div class="d">A <b>medição no local</b> antes do corte, que é ela que
      fecha a altura dos móveis do piso ao forro. A <b>cristaleira da
      varanda</b>, que a planta desenha curva e a elevação desenha reta — e
      as duas não podem estar certas ao mesmo tempo. O <b>forno e o
      micro-ondas</b>, para a torre da cozinha. E <b>amostra</b> dos padrões
      de MDF e da cor da laca, aprovadas por vocês e pela
      arquiteta.</div></div>
  </div>
  {foot(NP)}
</div></div>""")

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + EXTRA + '</style></head><body>'
        + ''.join(pg) + '</body></html>')

assert len(pg) == NP, f'⛔ {len(pg)} páginas, o rodapé diz {NP}'
# ⛔⛔ "NUNCA APRESENTE PREÇO SEM ANTES GERAR VALOR" — a trava, não a boa fé.
_antes = ''.join(pg[:N0-1])
assert 'R$' not in _antes, '⛔⛔ TEM PREÇO ANTES DA PÁGINA DE VALOR'
# ⛔⛔ MARCAÇÃO INTERNA NÃO VAI PARA O CLIENTE. ⭐/⛔/⚠ são a minha linguagem
#   de orçamento; impressas, viram emoji vermelho no meio da frase. Aconteceu
#   na folha da Eliza, eu apontei, e repeti aqui na v1. Vai de assert.
_marca = [c for c in '⭐⛔⚠' if c in ''.join(pg)]
assert not _marca, f'⛔⛔ MARCAÇÃO INTERNA NA PEÇA DO CLIENTE: {_marca}'
# ⛔ E nenhuma imagem reprovada na triagem pode ter entrado.
_CORTADAS = {'varanda-01', 'office-02', 'office-muxarabi', 'banho-master-02',
             'banho02-02', 'hospedes-01'}
for _c in _CORTADAS:
    assert IMG[_c] not in HTML, f'⛔⛔ IMAGEM REPROVADA NA PEÇA: {_c}'

(P/'proposta-gustavo-raposo.html').write_text(HTML, encoding='utf-8')
subprocess.run(['node', str(P/'render-pdf.js'), str(P/'proposta-gustavo-raposo.html'),
                str(P/'proposta-gustavo-raposo.pdf')], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'proposta-gustavo-raposo.pdf · {NP} páginas · '
      f'{(P/"proposta-gustavo-raposo.pdf").stat().st_size//1024} kB · '
      f'primeiro preço na {N0}')
for n in LIN:
    c = cen.CEN[n]
    print(f'  {n:13s} tabela R$ {br(c["tabela"]):>9s} · à vista R$ {br(c["vista"]):>9s}'
          f' · {c["gar"]}')
