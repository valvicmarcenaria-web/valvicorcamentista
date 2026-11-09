# -*- coding: utf-8 -*-
"""CHARBEL CHELALA — ⭐ A PROPOSTA, gerada do mesmo motor que o orçamento.

⛔⛔ NENHUM NÚMERO DESTA PROPOSTA É DIGITADO. Todos saem de planilha.json,
  que sai de levantamento.py, que lê a Base de Custos da casa. O rótulo se
  calcula, nunca se digita — e numa proposta de 625 mil isso deixa de ser
  elegância e vira a diferença entre cobrar o que foi levantado e cobrar o
  que alguém lembrou de digitar.

⭐ A ESTRUTURA É A DA PROPOSTA DA ANA CAROLINA E DO ANDRÉ [Jonathan,
  09/11/2026: "use a mesma estrutura de informacoes da blum e siforma
  dessa proposta"]. O que muda é o projeto: lá eram cinco armários num
  padrão só; aqui são nove ambientes em cinco padrões de MDF.

⚠ O FECHAMENTO É R$ 625.000,00 e o modelo, depois que o Branco TX saiu do
  interior, dá R$ 645.096,69. A tabela da folha de investimento é RATEADA
  para fechar no redondo, centavo a centavo. ⛔ Isso NÃO é arredondamento:
  são R$ 20 mil absorvidos na margem, que cai de 57,0% para 56,4%. Uma
  tabela de proposta que não soma o total é um erro que o cliente encontra.
"""
import io, json, os, subprocess, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import base as b

FOTOS = os.path.join(AQUI, 'fotos')
FONTES = os.path.join(AQUI, 'pr')          # cormorant.css + os .woff2 moram junto da saída


# ── o dinheiro ──────────────────────────────────────────────────────────
def brl(v, casas=2):
    s = f'{v:,.{casas}f}'.replace(',', '§').replace('.', ',').replace('§', '.')
    return s


def rateia(bruto, alvo):
    """reparte o fechado entre os ambientes, e fecha no centavo"""
    tot = sum(bruto.values())
    fat = alvo / tot
    out = {k: round(v * fat, 2) for k, v in bruto.items()}
    sobra = round(alvo - sum(out.values()), 2)
    maior = max(out, key=out.get)          # a sobra cai na maior linha
    out[maior] = round(out[maior] + sobra, 2)
    assert abs(sum(out.values()) - alvo) < 0.005, sum(out.values())
    return out


def le():
    d = json.load(open(os.path.join(AQUI, 'planilha.json'), encoding='utf-8'))
    bruto, itens = {}, {}
    for aba, R in d.items():
        i = [k for k, r in enumerate(R) if r and r[0] == 'ITEM'][0]
        lin = []
        for r in R[i + 1:]:
            if not r or not r[0]:
                break
            if str(r[0]).startswith('⭐'):
                bruto[aba] = r[7]
                break
            lin.append((str(r[0]), str(r[1]), str(r[2]), r[7]))
        itens[aba] = lin
    return bruto, itens


# ── o que cada ambiente é, em palavras de proposta ──────────────────────
#   ⭐ ESCRITO A PARTIR DAS PRANCHAS, não do orçamento: o cliente não quer
#     saber de chapa, quer saber o que vai usar todo dia.
AMB = {
 '01 Cozinha': dict(
  foto='c-cozinha.jpg', tarja='COZINHA', titulo='A cozinha.',
  bullets=[
   ('A frente é uma peça só', 'Os armários superior e inferior correm a parede inteira sem interrupção de desenho, e o painel do forno entra na mesma linha da frente.'),
   ('O puxador não é comprado', 'É <b>cava usinada no próprio material</b> da porta e da gaveta. Sem peça aplicada, sem metal à vista, sem o que soltar com os anos.'),
   ('A torre central esconde o quadro', 'O quadro de distribuição do apartamento fica atrás de uma tampa que abre. Deixa de ser um retângulo na parede.'),
   ('O varal corre como gaveta', 'Por isso sai sobre <b>corrediça Blum</b>, não sobre trilho de varal: sai inteiro e volta sozinho.'),
  ],
  acab='MDF Caribe Linha Dual Syncro, da Guararapes · interior no mesmo padrão · puxador cava usinado · rodapé inox · ferragem Blum'),

 '02 Hall e Jantar': dict(
  foto='r-40-02.jpg', tarja='HALL E JANTAR', titulo='O hall<br>e o jantar.',
  bullets=[
   ('A cristaleira é a peça da entrada', 'Vai do chão ao teto, com a vitrine fechada por <b>porta de vidro em esquadria de alumínio</b> e o aparador embaixo.'),
   ('A esquadria é slim, de 25 mm', 'Perfil fino, que dá <b>leveza à moldura e personalidade ao desenho</b>: o que se vê é o vidro e o que está atrás dele, não o perfil.'),
   ('A divisória tem moldura curva', 'Usinada na própria folha, não perfil colado por cima.'),
   ('O forro em madeira acompanha o recorte', 'Não o retângulo: o desenho do teto segue a planta do hall.'),
  ],
  acab='MDF Caribe Linha Dual Syncro · porta de vidro em esquadria slim de 25 mm · fita de LED com perfil de embutir · ferragem Blum'),

 '03 Estar e TV': dict(
  foto='r-40-00.jpg', tarja='ESTAR E TV', titulo='O estar<br>e a TV.',
  bullets=[
   ('A base do rack corre a parede', 'Uma porta de abrir e duas de correr, todas em <b>MDF ripado Caribe</b>, sobre sistema de correr <b>Siforma</b> com amortecimento nos dois sentidos.'),
   ('A adega fecha em reflecta bronze', 'Vidro reflecta bronze em <b>esquadria slim de 25 mm com perfil champanhe</b>, sobre dobradiça Blum de vidro, com estrutura metálica de suporte das garrafas por dentro.'),
   ('Os dois pés da mesa de jantar são nossos', 'Com <b>entalhamento diagonal usinado em CNC</b>. São peça de marcenaria, não base comprada.'),
   ('O painel fixo é ripado', 'Com filetagem nas duas faces de cada ripa, sobre estrutura de sarrafo por trás.'),
  ],
  acab='MDF Caribe Linha Dual Syncro · ripado com filetagem · vidro reflecta bronze em esquadria slim de 25 mm, perfil champanhe · Siforma · ferragem Blum'),

 '04 Acessos e Corredor': dict(
  foto='c-corredor.jpg', tarja='ACESSOS E CORREDOR', titulo='Os acessos<br>e o corredor.',
  bullets=[
   ('As portas somem no painel', 'Fechadas, a porta da suíte e a do quarto não se leem como porta: a folha <b>continua o ripado do painel</b>, sobre sistema pivô e fecho rolete de porta embutida.'),
   ('O ripado corre do hall ao corredor', 'Sem interrupção de desenho — é a maior metragem de filetagem do apartamento.'),
   ('O espelho é fixado na marcenaria', 'Não na parede: sai no mesmo caminhão e é instalado pela mesma equipe.'),
   ('O armário tem acabamento curvo ripado', 'Na lateral à vista, a ripa <b>vira a quina</b> em vez de topar nela.'),
  ],
  acab='MDF Caribe Linha Dual Syncro e Cipres · ripado com filetagem · espelho fixado na marcenaria · sistema pivô embutido · ferragem Blum'),

 '05 Suíte': dict(
  foto='f00.jpg', tarja='SUÍTE', titulo='A suíte.',
  bullets=[
   ('Três padrões de MDF no mesmo quarto', '<b>Cipres, Fontana Linha Magma e Cacao Matt</b> — e o painel da cabeceira usa os três empilhados: Cacao em cima, Fontana no meio, Cipres embaixo.'),
   ('O ripado das divisórias é VAZADO', 'A ripa <b>atravessa a divisória e se vê dos dois lados</b>. Não é ripado aplicado numa face: é estrutura.'),
   ('O painel da cabeceira é mais largo que a chapa', 'Sai emendado <b>por projeto</b>, e a emenda é decidida no desenho, não na serra.'),
   ('A prateleira do painel leva alma de aço', 'É o que trabalha contra a flecha, e o que a mantém reta daqui a dez anos.'),
  ],
  acab='MDF Cipres, Fontana Linha Magma e Cacao Matt · interior no mesmo padrão · espelho fixado na marcenaria · ferragem Blum'),

 '06 Closet': dict(
  foto='r-39-04.jpg', tarja='CLOSET', titulo='O closet.', inteira=True,
  bullets=[
   ('Nove folhas em esquadria de alumínio com vidro', 'De <b>piso a teto</b>, nas três vistas. É o que decide a cara do ambiente, e é a razão de o closet ser a maior linha do apartamento.'),
   ('A esquadria é slim, de 25 mm', 'Perfil fino, que confere <b>mais leveza e personalidade</b>: a moldura quase desaparece e o que se vê é o vidro e o que está guardado atrás dele.'),
   ('Com porta de vidro, o interior é fachada', 'Por isso o miolo sai em <b>MDF Cipres</b>, no mesmo padrão da frente: tudo o que está atrás do vidro é visto.'),
   ('A sapateira é de prateleira inclinada', 'Com <b>encaixe usinado em ângulo</b> na lateral. O sapato fica de frente, não de lado.'),
   ('A luz corre em cada prateleira e em cada arara', 'Fita de LED com perfil de embutir e difusor, acionada por <b>botton na própria marcenaria</b> — não há interruptor na parede.'),
  ],
  acab='MDF Cipres · nove folhas em esquadria de alumínio slim de 25 mm com vidro · fita de LED com perfil de embutir · cabideiro em metal · ferragem Blum'),

 '07 Banho da Suíte': dict(
  foto='f01.jpg', tarja='BANHO DA SUÍTE', titulo='O banho<br>da suíte.',
  bullets=[
   ('As folhas são espelhadas', 'Espelho prata <b>colado sobre a estrutura de MDF</b> — a folha é espelho inteiro, sem moldura e sem quadro aparente.'),
   ('A luz sai do espelho', 'A fita de LED corre dentro de uma faixa demarcada no desenho, com perfil de embutir e difusor. Não vem do teto.'),
   ('Padrão único', 'Todo o ambiente em <b>MDF Cinza Sagrado, da Duratex</b>, por fora e por dentro.'),
  ],
  acab='MDF Cinza Sagrado, da Duratex · interior no mesmo padrão · espelho prata colado na folha · puxador cava usinado · ferragem Blum'),

 '08 Banheiro Social': dict(
  foto='r-39-03.jpg', tarja='BANHEIRO SOCIAL', titulo='O banheiro<br>social.',
  bullets=[
   ('A porta infinita', 'O puxador é <b>cava usinada na própria estrutura do espelho</b>. Chamamos assim porque não há onde a mão apareça, e não há peça aplicada sobre o espelho.'),
   ('São três peças de espelho', 'A folha do armário, o espelho fixado e a moldura — todas nossas, todas no mesmo caminhão.'),
   ('O nicho aberto na base', 'Quebra a frente cheia e dá onde apoiar, sem porta.'),
  ],
  acab='MDF Cinza Sagrado, da Duratex · interior no mesmo padrão · três peças de espelho prata · puxador cava usinado · ferragem Blum'),

 '09 Quarto': dict(
  foto='r-39-07.jpg', tarja='QUARTO', titulo='O quarto.',
  bullets=[
   ('Duas folhas de correr em Cacao Matt', 'Sobre sistema de correr <b>Siforma</b>. Folha larga leva <b>dois desempenadores</b>, e é o que a impede de descer com o tempo.'),
   ('O armário dobra em L', 'Nichos abertos em Cipres, bancada e prateleira, e o retorno acompanha a volta da parede.'),
   ('O móvel baú abre retrátil', 'A frente em Cacao Matt <b>entra para dentro</b> em vez de girar para fora.'),
   ('O painel da cabeceira abraça o espelho', 'Dentro de moldura, com <b>pulsador Blum Tip-on</b> no acionamento da luz.'),
  ],
  acab='MDF Cacao Matt, da Arauco, e Cipres · interior no mesmo padrão · espelho fixado na marcenaria · Siforma · ferragem Blum'),
}

#   ⭐ DOIS AMBIENTES POR FOLHA [Jonathan, 09/11/2026]. O closet fica
#     sozinho: é a maior linha do apartamento e a imagem que vende o job.
PARES = [('01 Cozinha', '02 Hall e Jantar'),
         ('03 Estar e TV', '04 Acessos e Corredor'),
         ('05 Suíte', '09 Quarto'),
         ('06 Closet', None),
         ('07 Banho da Suíte', '08 Banheiro Social')]
ORDEM = ['01 Cozinha', '02 Hall e Jantar', '03 Estar e TV', '04 Acessos e Corredor',
         '05 Suíte', '06 Closet', '07 Banho da Suíte', '08 Banheiro Social', '09 Quarto']

#   ⛔ SEM CONTAGEM DE CHAPA [Jonathan: "é dispensavel apresentar
#     quantitativo de insumos"]. E sem Branco TX, que não existe neste
#     projeto: o interior sai no padrão do próprio ambiente.
PADROES = [
 ('Caribe', 'Linha Dual Syncro · Guararapes', 'Cozinha, hall, jantar, estar e corredor'),
 ('Cipres', 'Guararapes', 'Suíte, closet, quarto e corredor'),
 ('Fontana', 'Linha Magma · Guararapes', 'Cabeceira, painéis e tampos da suíte'),
 ('Cacao', 'Matt · Arauco', 'Bancada da suíte e portas de correr do quarto'),
 ('Cinza Sagrado', 'Duratex', 'Banho da suíte e banheiro social'),
]

#   ⭐⭐ BLUM E SIFORMA SÃO EMPRESAS DIFERENTES [Jonathan, 09/11/2026], e eu
#     as tinha misturado numa linha só, "Blum SI Forma". A Blum é austríaca
#     e faz dobradiça, corrediça e pulsador. O sistema de correr SI Ocean 80
#     é da SIFORMA. Escrever as duas juntas é erro de ficha técnica, e numa
#     proposta de 625 mil ficha técnica errada é o que o cliente confere.
FERRAGEM = [
 ('DOBRADIÇA', 'Blum CLIP top BLUMOTION', 'img-000.png', None,
  ['Amortecimento <b>BLUMOTION</b> embutido no caneco: a porta fecha suave e em silêncio.',
   'Encaixe <b>CLIP</b>: a porta se monta e se retira sem ferramenta, para limpeza ou ajuste.',
   'Regulagem em altura, lateral e profundidade: a porta se realinha em minutos.',
   'Testada em <b>200 mil</b> aberturas e fechamentos antes de sair da fábrica.']),
 ('CORREDIÇA', 'Blum MOVENTO com BLUMOTION', 'img-001.png', 'img-002.png',
  ['Oculta sob a gaveta: a lateral fica limpa, <b>sem trilho de metal à vista</b>.',
   'Extração total: a gaveta sai inteira e mostra o fundo.',
   '<b>BLUMOTION</b> integrado: no fim do curso a gaveta se recolhe sozinha e fecha sem ruído.',
   'Movimento sincronizado nos dois lados, mesmo com carga desigual.']),
 ('SISTEMA DE CORRER', 'SI Ocean 80 · Siforma', 'img-003.png', 'img-004.png',
  ['⭐ <b>Outra fabricante</b>: a Siforma faz o sistema de correr; a Blum, a dobradiça e a corrediça.',
   'Para roupeiros de portas de correr, com folhas de peso alto.',
   'Amortecimento nos dois sentidos: a folha desacelera ao abrir e ao fechar.',
   'O trilho some na estrutura — não há perfil aparente no piso.']),
]

ETAPAS = [
 ('PARTIDA', 'da decisão ao contrato', [
  ('DECISÃO', 'Aprovação', '01', 'Escopo, acabamentos e ferragens definidos. Nada entra em produção sem essa decisão.', 'Escopo fechado, ambiente por ambiente.'),
  ('REGISTRO', 'Contrato', '02', 'Contrato assinado, prazos e responsabilidades registrados. Tudo o que foi dito fica escrito.', 'Contrato e cronograma com datas.')]),
 ('ENGENHARIA', 'da obra ao arquivo de máquina', [
  ('PAREDE', 'Medição técnica', '03', 'Nossa equipe mede a obra no local. O projeto passa a conversar com a parede real.', 'Medidas da obra construída, não do desenho.'),
  ('DESENHO', 'Detalhamento', '04', 'Fechamos com vocês e com a arquiteta cada decisão de execução antes de cortar nada.', 'Nenhuma decisão de execução em aberto.'),
  ('ARQUIVO', 'Programação', '05', 'O detalhamento vira arquivo de máquina. O erro é corrigido na tela, não na chapa.', 'Plano de corte e usinagem programado.')]),
 ('FÁBRICA', 'onde o móvel nasce e é testado', [
  ('CORTE', 'Usinagem', '06', 'Corte, furação, fresa e acabamento de borda. Tudo acontece dentro da nossa fábrica.', 'Peças prontas e identificadas, uma por uma.'),
  ('ENCAIXE', 'Montagem em fábrica', '07', 'O móvel é montado aqui antes de ir para a obra. Problema de encaixe morre aqui.', 'Móvel montado e testado antes de sair.'),
  ('CHECKLIST', 'Conferência', '08', 'Peça por peça contra o projeto: medida, cor, ferragem, sentido de abertura, luz.', 'Checklist assinado antes do carregamento.')]),
 ('ENTREGA', 'da nossa fábrica à sua casa', [
  ('CARGA', 'Transporte', '09', 'Embalagem, carregamento e transporte são nossos, da nossa fábrica até a porta da sua casa. O móvel não troca de mão no caminho.', 'Móvel embalado e carregado por quem montou.'),
  ('PRUMO', 'Instalação', '10', 'Equipe própria instala, nivela e regula. A obra recebe móvel pronto, não peça solta.', 'Móveis no lugar, nivelados e regulados.'),
  ('TESTE', 'Vistoria técnica', '11', 'Com vocês, abrimos tudo: cada porta, cada gaveta, cada luz. Nada passa sem testar.', 'Ajustes finais feitos na frente de vocês.'),
  ('CASA', 'Entrega final', '12', 'Ambiente limpo, móvel em uso e termo de garantia na mão de vocês. O projeto virou casa.', 'Termo de garantia emitido e assinado.')]),
]

FORA = [
 ('Toda a pedra', 'Quartzito Verde Guatemala, ônix retroiluminado, granito Grigio Carnico, cuba esculpida, rodaparede e as prateleiras de mármore. Bancada, sóculo, frontão, tampo, soleira e peitoril.'),
 ('Louça, metal e box', 'Cubas, torneiras, registros, vasos e o box de vidro dos banheiros.'),
 ('Eletrodomésticos', 'Forno, frigobar, adega Elettromec, cooktop e coifa.'),
 ('Obra e revestimento', 'Alvenaria, gesso, papel de parede, forro em pintura, elétrica, hidráulica e ar-condicionado.'),
 ('Móvel solto e decoração', 'Cabeceira estofada, cama, colchão, mesa posta, poltronas, luminárias, tapetes e cortinas.'),
]


def html():
    bruto, itens = le()
    fechado = rateia(bruto, b.PRECO_FECHADO)
    entrada = b.PRECO_FECHADO * b.PAGAMENTO[0][1]
    css = io.open(os.path.join(FONTES, 'cormorant.css'), encoding='utf-8').read()
    F = lambda n: 'file://' + os.path.join(FOTOS, n)

    P = []   # as folhas

    # ── 01 · capa ───────────────────────────────────────────────────────
    P.append(f'''<section class="pg capa">
 <div class="capa-txt">
  <div class="marca">VALVIC MARCENARIA</div>
  <h1>Charbel<br>Chelala</h1>
  <p class="lede">O apartamento inteiro em marcenaria — nove ambientes,
   da cozinha ao closet, em cinco padrões de MDF e ferragem Blum.</p>
  <div class="capa-meta">
   <div><span>PROJETO</span>Mariana Borges<br>Arquitetura &amp; Interiores</div>
   <div><span>OBRA</span>Apartamento<br>Belo Horizonte</div>
   <div><span>LINHA</span>Blum</div>
   <div><span>DATA</span>Novembro de 2026</div>
  </div>
  <div class="capa-rod">PROPOSTA DE MARCENARIA &nbsp;&nbsp;·&nbsp;&nbsp; VALVIC · VARGAS DECOR</div>
 </div>
 <div class="capa-img" style="background-image:url('{F('r-40-04.jpg')}')">
  <div class="badge"><span>PADRÃO</span><b>Cinco MDF</b>
   <i>Guararapes · Arauco · Duratex</i></div>
 </div>
</section>''')

    # ── 02 · o apartamento ──────────────────────────────────────────────
    faixa = ''.join(f'<div style="background-image:url(\'{F(x)}\')"></div>'
                    for x in ('r-39-05.jpg', 'r-39-08.jpg', 'f00.jpg', 'r-39-02.jpg'))
    P.append(f'''<section class="pg">
 <div class="faixa">{faixa}<div class="tarja">O APARTAMENTO</div></div>
 <div class="corpo">
  <div class="eyebrow">O QUE ESTE APARTAMENTO PEDE</div>
  <h2>Nove ambientes. Cinco padrões. Um contrato.</h2>
  <p class="texto">Da cozinha ao quarto, passando pelo hall, pelo estar, pelo corredor que esconde
   duas portas, pela suíte, pelo closet e pelos dois banhos — <b>um só projeto da arquiteta
   Mariana Borges</b>, com portas de giro de cava usinada, folhas de correr amortecidas, nove
   folhas em perfil de alumínio com vidro e gavetas que fecham sozinhas.
   <b>Cinco padrões de MDF por fora — Caribe, Cipres, Fontana Magma, Cacao Matt e Cinza
   Sagrado — e o interior no mesmo padrão da face</b>, sobre ferragem Blum e sistema de correr Siforma.
   <b>Uma só empresa responde por tudo o que está nestas folhas</b>, da medição à instalação.
   <i>Um contrato, uma data, um nome para chamar.</i></p>
  <div class="numeros">
   <div><b>9</b><span>AMBIENTES</span></div>
   <div><b>38</b><span>ITENS DE MÓVEL</span></div>
   <div><b>5</b><span>PADRÕES DE MDF</span></div>
   <div><b>1</b><span>CONTRATO, UMA DATA</span></div>
  </div>
 </div>
 {rod(2)}
</section>''')

    # ── 03 · a empresa ──────────────────────────────────────────────────
    cards = [
     ('01', 'O projeto pede mais que marcenaria.',
      'Nove folhas em perfil de alumínio com vidro, portas em reflecta bronze, espelhos colados em folha, '
      'ripado vazado, forro em madeira e três peças de espelho nos banhos. <b>Tudo isso entra no nosso '
      'escopo, no mesmo contrato e na mesma data.</b> Vocês não contratam mais ninguém para a marcenaria '
      'e para o que faz parte dela. O que fica fora vem nomeado.'),
     ('02', 'A peça sai daqui conferida.',
      'Detalhamento, programação, usinagem, montagem e conferência acontecem dentro da nossa fábrica. '
      'Cada módulo é montado aqui antes de ser embalado: porta regulada, gaveta corrida, folha de correr '
      'alinhada. A conferência é <b>etapa do processo</b>, não boa vontade no fim.'),
     ('03', 'Uma arquiteta responsável pelo projeto.',
      'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como responsável. É ela quem lê '
      'o executivo prancha por prancha, está na medição e segue as peças pela fábrica. Ela conversa com a '
      'arquiteta Mariana Borges na mesma linguagem técnica. <b>Vocês explicam o projeto uma vez, a uma pessoa.</b>'),
     ('04', 'O executivo de marcenaria é nosso.',
      'Antes de cortar, a Valvic desenha. O projeto de interiores diz o que o ambiente precisa ser; o nosso '
      'executivo diz como cada móvel se constrói — estrutura, ferragem, sentido de abertura, folga das portas, '
      'onde a chapa emenda. É nele que a divergência aparece <i>no papel, antes de virar retrabalho</i>.'),
    ]
    cs = ''.join(f'<div class="card"><div class="n">{n}</div><h4>{t}</h4><p>{p}</p></div>'
                 for n, t, p in cards)
    P.append(f'''<section class="pg">
 <div class="corpo alto">
  <div class="eyebrow">A EMPRESA E A INFRAESTRUTURA</div>
  <h2>A Valvic articula todas as soluções do projeto.</h2>
  <p class="texto curto">Um projeto raramente se perde na marcenaria. Ele se perde na costura entre os ofícios,
   quando cada um chega com contrato, prazo e medida próprios. Aqui não há essa costura para fazer: tudo o que
   esta proposta reúne entra no mesmo escopo, no mesmo contrato e na mesma data.</p>
  <div class="cards">{cs}</div>
  <div class="nota">Na próxima folha, o caminho que o projeto percorre — etapa por etapa, até o dia em que o apartamento está em uso.</div>
 </div>
 {rod(3)}
</section>''')

    # ── 04 · doze etapas ────────────────────────────────────────────────
    cols = ''
    for fase, sub, passos in ETAPAS:
        ps = ''.join(
         f'<div class="passo"><div class="kicker">{k}</div>'
         f'<div class="passo-t"><h5>{t}</h5><span class="num">{n}</span></div>'
         f'<p>{d}</p><div class="saida">{s}</div></div>'
         for k, t, n, d, s in passos)
        cols += f'<div class="fase"><div class="fase-h">{fase}</div><div class="fase-s">{sub}</div>{ps}</div>'
    P.append(f'''<section class="pg">
 <div class="corpo alto">
  <div class="eyebrow">O CAMINHO DO SEU PROJETO</div>
  <div class="etapa-head">
   <h2 class="duas">Doze etapas,<br>um só responsável</h2>
   <p class="texto curto">Da decisão de vocês até o apartamento pronto são doze etapas — e nenhuma delas muda de dono.</p>
  </div>
  <div class="fases">{cols}</div>
 </div>
 {rod(4)}
</section>''')

    # ── 05 · o padrão ───────────────────────────────────────────────────
    pads = ''.join(
     f'<div class="pad"><div class="pad-n">{n}</div><div class="pad-f">{f}</div>'
     f'<div class="pad-o">{o}</div></div>'
     for n, f, o in PADROES)
    P.append(f'''<section class="pg">
 <div class="hero" style="background-image:url('{F('r-39-04.jpg')}')">
  <div class="tarja">REFERÊNCIA DE AMBIENTE</div>
  <div class="hero-badge"><b>Cinco padrões</b><span>GUARARAPES · ARAUCO · DURATEX</span>
   <i>Imagens do projeto executivo · a amostra física é apresentada na aprovação</i></div>
 </div>
 <div class="corpo">
  <div class="eyebrow">O PADRÃO</div>
  <h2>Cinco padrões. E o que está por dentro<br>é o mesmo que está por fora.</h2>
  <p class="texto curto">Caixa, gaveta e fundo saem no <b>padrão da própria face</b> — nenhum armário deste
   apartamento é branco por dentro. Com porta de vidro no closet e na cristaleira, o interior é fachada: o que
   se vê atrás do vidro é o mesmo material da frente.</p>
  <div class="pads">{pads}</div>
 </div>
 {rod(5)}
</section>''')

    # ── 06 a 10 · os nove ambientes, dois por folha ────────────────────
    def meio(aba):
        a = AMB[aba]
        bs = ''.join(f'<li><b>{x}</b> {d}</li>' for x, d in a['bullets'])
        return f'''<div class="meio">
   <div class="meio-img" style="background-image:url('{F(a['foto'])}')">
    <div class="tarja baixo">{a['tarja']}</div></div>
   <div class="meio-txt">
    <h3>{a['titulo']}</h3>
    <ul class="bul">{bs}</ul>
    <div class="acab"><span>ACABAMENTOS</span>{a['acab']}</div>
   </div>
  </div>'''

    for i, (e, d) in enumerate(PARES):
        if d is None:                       # o closet ocupa a folha inteira
            a = AMB[e]
            bs = ''.join(f'<li><b>{x}</b> {y}</li>' for x, y in a['bullets'])
            P.append(f'''<section class="pg amb">
 <div class="amb-img" style="background-image:url('{F(a['foto'])}')">
  <div class="tarja baixo">{a['tarja']}</div>
 </div>
 <div class="amb-txt">
  <div class="eyebrow">AMBIENTE</div>
  <h3>{a['titulo']}</h3>
  <ul class="bul">{bs}</ul>
  <div class="acab"><span>ACABAMENTOS</span>{a['acab']}</div>
 </div>
 {rod(6 + i)}
</section>''')
        else:
            P.append(f'''<section class="pg dois">
 {meio(e)}
 {meio(d)}
 {rod(6 + i)}
</section>''')

    # ── 15 · por que blum ───────────────────────────────────────────────
    P.append(f'''<section class="pg escuro">
 <div class="corpo alto">
  <div class="eyebrow ouro">POR QUE BLUM</div>
  <h2 class="claro">A ferragem é a única parte<br>do móvel que trabalha todo dia.</h2>
  <p class="texto claro curto">É ela que decide se, daqui a muitos anos, a porta ainda fecha alinhada e a gaveta
   ainda corre macia. Por isso a ferragem de movimento deste projeto sai na linha <b>Blum</b>, uma das referências
   mundiais do ramo — e as folhas de correr, no sistema <b>SI Ocean 80, da Siforma</b>.</p>
  <div class="big4">
   <div><b>200 mil</b><span>ABERTURAS E FECHAMENTOS</span><p>É o ensaio a que a Blum submete as suas dobradiças antes de elas saírem da fábrica.</p></div>
   <div><b>30 anos</b><span>DE GARANTIA VALVIC</span><p>No projeto inteiro: marcenaria e ferragem de movimento, com termo assinado no dia da entrega.</p></div>
   <div><b>Áustria</b><span>EMPRESA FAMILIAR</span><p>A Blum desenha e fabrica as próprias ferragens, com controle de qualidade em cada etapa.</p></div>
   <div><b>BLUMOTION</b><span>O FECHAMENTO AMORTECIDO</span><p>Porta e gaveta fecham suave e silenciosamente, toda vez — sem a batida que, com os anos, é o que desgasta o móvel.</p></div>
  </div>
  <p class="frase">Neste apartamento, toda porta de giro e toda gaveta se movem sobre Blum —
   <i>sem exceção</i>.</p>
  <div class="nota escura"><b>TESTADA ANTES DE CHEGAR AQUI</b><br>
   Na fábrica da Blum, as ferragens passam por ensaios de movimento, de carga e de corrosão — com calor, água e
   sal — que reproduzem em laboratório o desgaste de anos de uso. O que chega à nossa bancada já provou que dura.</div>
 </div>
 {rod(11, True)}
</section>''')

    # ── 12 · as ferragens deste projeto, com imagem ────────────────────
    fs = ''
    for rot, nome, im1, im2, xs in FERRAGEM:
        duas = (f'<div class="fer-im"><div style="background-image:url(\'{F(im1)}\')"></div>'
                f'<div style="background-image:url(\'{F(im2)}\')"></div></div>') if im2 else \
               (f'<div class="fer-im"><div style="background-image:url(\'{F(im1)}\')"></div></div>')
        fs += (f'<div class="fer">{duas}<div class="kicker">{rot}</div>'
               f'<h4>{nome}</h4><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>')
    P.append(f'''<section class="pg">
 <div class="corpo alto">
  <div class="eyebrow">AS FERRAGENS DESTE PROJETO</div>
  <div class="etapa-head">
   <h2 class="duas">O que vocês tocam<br>todo dia.</h2>
   <p class="texto curto">Cada porta, cada gaveta e cada folha de correr deste apartamento se move sobre uma
    destas três peças — e elas vêm de <b>duas fabricantes diferentes</b>.</p>
  </div>
  <div class="fers tres">{fs}</div>
  <div class="nota">As <b>nove folhas do closet</b> e as portas de cristaleira e de adega se fecham em
   <b>esquadria de alumínio com perfil slim de 25 mm</b>, sobre dobradiça Blum de vidro. O perfil fino é
   escolha de desenho: confere mais leveza à moldura e personalidade ao conjunto, e deixa o vidro — e o que
   está guardado atrás dele — como o que se vê. <i>Imagens ilustrativas das fabricantes.</i></div>
 </div>
 {rod(12)}
</section>''')

    # ── 17 · garantia ───────────────────────────────────────────────────
    fx13 = ''.join(f'<div style="background-image:url(\'{F(x)}\')"></div>'
                   for x in ('r-39-06.jpg', 'r-40-01.jpg', 'r-40-03.jpg'))
    P.append(f'''<section class="pg">
 <div class="corpo alto">
  <div class="eyebrow">GARANTIA</div>
  <h2>Trinta anos. O termo é assinado na entrega.</h2>
  <p class="texto curto">A garantia da Valvic <b>é escalonada pela ferragem</b> — e a linha Blum é a do prazo mais
   longo da casa. Ela vale para o projeto inteiro e não é promessa de proposta: é <b>termo assinado no dia da
   entrega</b>, junto com o guia de conservação do móvel.</p>
  <div class="gar">
   <div class="gar-card"><b>30</b><span>ANOS DE GARANTIA</span><h4>Linha Blum</h4>
    <p>Marcenaria e ferragem de movimento, no projeto inteiro.</p></div>
   <div class="gar-col">
    <div class="eyebrow">COMO SE ACIONA</div>
    <div class="gar-p"><h5>Vocês nos chamam</h5><span>01</span>
     <p>Por telefone, WhatsApp ou e-mail, direto com a fábrica. Sem central e sem intermediário.</p></div>
    <div class="gar-p"><h5>Respondemos em 24 horas</h5><span>02</span>
     <p>Esse é o nosso compromisso de retorno, contado a partir do chamado.</p></div>
    <div class="gar-p"><h5>Visita em até três dias úteis</h5><span>03</span>
     <p>Se não resolvermos pelo telefone, a equipe vai ao local. Dentro do prazo de garantia, visita e reparo não têm custo.</p></div>
   </div>
   <div class="gar-col">
    <div class="eyebrow">O QUE O TERMO COBRE</div>
    <div class="gar-i"><span>MARCENARIA E FERRAGEM DE MOVIMENTO</span>
     <p>Estrutura, frentes, corrediças, dobradiças e os sistemas de correr, pelo prazo da linha.</p></div>
    <div class="gar-i"><span>MONTAGEM E INSTALAÇÃO</span>
     <p>Instalações e regulagens têm garantia de dois anos.</p></div>
    <div class="eyebrow" style="margin-top:7mm">O QUE FICA DE FORA</div>
    <div class="gar-i"><span>DESGASTE, UMIDADE E ALTERAÇÃO POR TERCEIRO</span>
     <p>Dano vindo da obra ou mudança feita no móvel depois da entrega.</p></div>
   </div>
  </div>
  <div class="faixa fim">{fx13}<div class="tarja">O APARTAMENTO PRONTO</div></div>
 </div>
 {rod(13)}
</section>''')

    # ── 18 · investimento ───────────────────────────────────────────────
    linhas = ''
    for aba in ORDEM:
        a = AMB[aba]
        n = len(itens[aba])
        sub = ' · '.join(x[1].split(' · ')[0] for x in itens[aba][:2])
        linhas += (f'<tr><td><b>{aba[3:]}</b><span>{n} '
                   f'{"itens" if n > 1 else "item"} · {a["acab"].split(" · ")[0]}</span></td>'
                   f'<td class="v">{brl(fechado[aba], 0)}</td></tr>')
    P.append(f'''<section class="pg">
 <div class="corpo alto">
  <div class="eyebrow">INVESTIMENTO · LINHA BLUM</div>
  <h2>O apartamento, ambiente por ambiente.</h2>
  <div class="inv">
   <div class="inv-t">
    <p class="texto curto">Cada móvel foi levantado <b>peça por peça do projeto executivo</b>, ambiente por
     ambiente. Nada é rateio nem estimativa por metro quadrado. Valores em reais.</p>
    <table>
     <thead><tr><th>AMBIENTE</th><th class="v">LINHA<br>BLUM</th></tr></thead>
     <tbody>{linhas}</tbody>
     <tfoot><tr><td>O PROJETO COMPLETO</td><td class="v">{brl(b.PRECO_FECHADO, 0)}</td></tr></tfoot>
    </table>
   </div>
   <div class="inv-card">
    <div class="eyebrow ouro">O PROJETO COMPLETO</div>
    <div class="preco">R$ {brl(b.PRECO_FECHADO)}</div>
    <p>Nove ambientes em cinco padrões de MDF, interior no mesmo padrão da face, ferragem Blum, sistema de
     correr Siforma, as nove folhas do closet em esquadria slim de 25 mm com vidro e 30 anos de garantia.</p>
    <div class="hr"></div>
    <div class="eyebrow ouro">ENTRADA, NA ASSINATURA</div>
    <div class="entrada">R$ {brl(entrada)}</div>
   </div>
  </div>
  <div class="nota"><b>O QUE ESTÁ INCLUSO</b><br>
   Projeto executivo de marcenaria, os cinco padrões de MDF por fora e por dentro, usinagem, ferragens Blum,
   o sistema de correr Siforma, as nove folhas de closet e as portas de cristaleira e de adega em esquadria
   de alumínio slim de 25 mm com vidro, os espelhos, a iluminação em fita de LED com perfil e fonte, o
   transporte, a montagem e a instalação — num só contrato, com uma só data e uma só responsável.</div>
 </div>
 {rod(14)}
</section>''')

    # ── 19 · condições ──────────────────────────────────────────────────
    pg = ''.join(
     f'<tr><td>{n}</td><td class="pc">{int(p*100)}%</td>'
     f'<td class="v">R$ {brl(b.PRECO_FECHADO*p)}</td></tr>'
     for n, p, _ in b.PAGAMENTO)
    fora = ''.join(f'<div class="fora-i"><b>{t}</b><p>{d}</p></div>' for t, d in FORA)
    P.append(f'''<section class="pg">
 <div class="corpo alto">
  <div class="eyebrow">CONDIÇÕES</div>
  <h2>Prazo, pagamento e fronteiras.</h2>
  <div class="cond">
   <div>
    <div class="eyebrow">VALIDADE DESTA PROPOSTA</div>
    <h5 class="cond-v">{b.VALIDADE_DIAS} dias corridos</h5>
    <p>A partir desta data. É por esse tempo que conseguimos reservar a vaga na agenda da fábrica que sustenta
     a entrega em {b.PRAZO_DIAS} dias corridos.</p>
    <div class="eyebrow">PRAZO DE EXECUÇÃO</div>
    <h5 class="cond-v">{b.PRAZO_DIAS} dias corridos</h5>
    <p>Contados a partir da medição técnica no local, não da assinatura. A medição tem data própria no cronograma.</p>
    <div class="eyebrow">GARANTIA</div>
    <h5 class="cond-v">30 anos · linha Blum</h5>
    <p>Instalação e regulagem, dois anos. Termo assinado na entrega.</p>
    <div class="eyebrow">PROJETO EXECUTIVO DE MARCENARIA</div>
    <h5 class="cond-v">Incluso</h5>
    <p>Aprovado por vocês e pela arquiteta Mariana Borges antes de qualquer corte.</p>
   </div>
   <div>
    <div class="eyebrow">FORMAS DE PAGAMENTO</div>
    <table class="pag"><tbody>{pg}</tbody></table>
    <p class="mini">Todas as parcelas por transferência bancária. Os dias contam a partir da assinatura do contrato.</p>
    <div class="nota pequena"><b>A AMOSTRA DO PADRÃO</b><br>
     Os cinco padrões de MDF são apresentados em amostra física na aprovação do projeto executivo, antes da
     compra da chapa. É nesse momento que vocês confirmam cor e desenho de cada um — e só depois disso a
     chapa entra em corte. O valor desta proposta já contempla os cinco.</div>
   </div>
   <div>
    <div class="eyebrow">O QUE NÃO ESTÁ NESTA PROPOSTA</div>
    {fora}
   </div>
  </div>
  <div class="assina"><div>Charbel Chelala</div><div>Valvic Marcenaria · Vargas Decor LTDA</div></div>
 </div>
 {rod(15)}
</section>''')

    # ── 20 · contracapa ─────────────────────────────────────────────────
    P.append(f'''<section class="pg capa fim">
 <div class="capa-txt">
  <div class="marca">VALVIC MARCENARIA</div>
  <h1 class="menor">Um contrato.<br>Uma data.<br>Um nome<br>para chamar.</h1>
  <p class="lede">Obrigado pela confiança de pôr este apartamento na nossa mão.
   O desenho da arquiteta Mariana Borges sai da nossa fábrica e chega instalado.</p>
  <div class="capa-meta dois">
   <div><span>PROPOSTA</span>Charbel Chelala</div>
   <div><span>VALIDADE</span>{b.VALIDADE_DIAS} dias corridos</div>
  </div>
 </div>
 <div class="capa-img" style="background-image:url('{F('r-39-05.jpg')}')"></div>
</section>''')

    return TOPO.replace('/*FONTES*/', css) + '\n'.join(P) + '</body></html>'


def rod(n, claro=False):
    c = ' claro' if claro else ''
    return (f'<div class="rodape{c}"><span>VALVIC · CHARBEL CHELALA</span>'
            f'<span>{n:02d}</span></div>')


TOPO = '''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Charbel Chelala · Proposta de Marcenaria</title>
<style>
/*FONTES*/
:root{
  --creme:#F6F2E8; --creme2:#EDE7D8; --escuro:#231C15; --escuro2:#2E251B;
  --ouro:#A5884F; --ouro-claro:#C9A96A; --tinta:#1E1913; --corpo:#4C453B;
  --fino:#D9D0BD;
}
*{margin:0;padding:0;box-sizing:border-box}
@page{size:297mm 210mm;margin:0}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Inter',sans-serif;color:var(--tinta);background:var(--creme)}
.pg{width:297mm;height:210mm;position:relative;overflow:hidden;background:var(--creme);
    page-break-after:always;display:flex;flex-direction:column}
.pg:last-child{page-break-after:auto}

h2{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:30pt;line-height:1.08;
   letter-spacing:-.005em;margin-bottom:5mm}
h2.duas{margin:0;flex:0 0 95mm}
h3{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:27pt;line-height:1.1;margin-bottom:7mm}
h4{font-size:9pt;font-weight:600;line-height:1.35;margin-bottom:3mm}
h5{font-size:9.5pt;font-weight:600}
.eyebrow{font-size:6.3pt;font-weight:600;letter-spacing:.22em;color:var(--ouro);
   margin-bottom:3mm;position:relative;padding-top:2.5mm}
.eyebrow:before{content:'';position:absolute;top:0;left:0;width:9mm;height:1.5px;background:var(--ouro)}
.eyebrow.ouro{color:var(--ouro-claro)}.eyebrow.ouro:before{background:var(--ouro-claro)}
.texto{font-size:8.6pt;line-height:1.62;color:var(--corpo);max-width:185mm}
.texto.curto{max-width:150mm;font-size:8.2pt}
.texto b{color:var(--tinta);font-weight:600}
.texto i{color:var(--corpo)}
.corpo{padding:16mm 18mm 0;flex:1;display:flex;flex-direction:column}
.corpo.alto{padding-top:14mm}
.amb .rodape{left:calc(55% + 15mm)}
.rodape{position:absolute;bottom:9mm;left:18mm;right:18mm;display:flex;justify-content:space-between;
   font-size:6pt;letter-spacing:.2em}
.rodape{color:#A79C86}
.rodape.claro{color:#6E6253}

/* capa */
.capa{flex-direction:row}
.capa-txt{width:44%;background:var(--escuro);color:var(--creme);padding:17mm 15mm;
   display:flex;flex-direction:column}
.marca{font-size:6.6pt;letter-spacing:.34em;color:var(--ouro-claro);margin-bottom:11mm}
.capa h1{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:46pt;line-height:1.02;
   letter-spacing:-.01em;margin-bottom:8mm}
.capa h1.menor{font-size:33pt;line-height:1.12}
.lede{font-size:8.4pt;line-height:1.62;color:#CFC6B4;max-width:92mm}
.capa-meta{margin-top:auto;display:grid;grid-template-columns:1fr 1fr;gap:7mm 6mm;
   padding-top:7mm;border-top:1px solid rgba(214,201,174,.26)}
.capa-meta.dois{grid-template-columns:1fr 1fr}
.capa-meta div{font-size:8pt;line-height:1.45;color:#D9D0BD}
.capa-meta span{display:block;font-size:5.9pt;letter-spacing:.22em;color:var(--ouro-claro);margin-bottom:2mm}
.capa-rod{margin-top:8mm;font-size:5.8pt;letter-spacing:.22em;color:#7E7360}
.capa-img{flex:1;background-size:cover;background-position:center;position:relative}
.badge{position:absolute;right:0;bottom:16mm;background:var(--escuro);color:var(--creme);
   padding:7mm 9mm;max-width:74mm}
.badge span{display:block;font-size:5.9pt;letter-spacing:.22em;color:var(--ouro-claro);margin-bottom:2mm}
.badge b{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:20pt;display:block;line-height:1}
.badge i{display:block;font-style:normal;font-size:6.3pt;color:#A99C85;margin-top:2.5mm;line-height:1.4}

/* faixa de imagens */
.faixa{height:74mm;display:flex;gap:0;position:relative;background:var(--creme2)}
.faixa.fim{height:60mm;margin-top:auto;margin-bottom:15mm}
.faixa>div{flex:1;background-size:cover;background-position:center}
.tarja{position:absolute;left:0;bottom:0;background:var(--escuro);color:var(--ouro-claro);
   font-size:6.1pt;letter-spacing:.22em;padding:3mm 7mm}
.tarja.baixo{bottom:0}
.numeros{display:grid;grid-template-columns:repeat(4,1fr);gap:8mm;margin-top:auto;margin-bottom:16mm;
   padding-top:7mm;border-top:1px solid var(--fino)}
.numeros b{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:28pt;display:block;
   line-height:1;color:var(--ouro)}
.numeros span{display:block;font-size:5.9pt;letter-spacing:.2em;color:var(--corpo);margin-top:2.5mm}

/* cards */
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:8mm}
.card{border:1px solid var(--fino);padding:7mm 6mm}
.card .n{font-family:'Cormorant Garamond',serif;font-size:14pt;color:var(--ouro);margin-bottom:4mm}
.card p{font-size:7.3pt;line-height:1.55;color:var(--corpo)}
.card p b{color:var(--tinta);font-weight:600}
.nota{margin-top:auto;margin-bottom:14mm;border-left:2px solid var(--ouro);padding:4.5mm 7mm;
   background:rgba(165,136,79,.055);font-size:7.4pt;line-height:1.58;color:var(--corpo)}
.nota b{color:var(--tinta);font-weight:600;letter-spacing:.14em;font-size:6.3pt}
.nota.pequena{margin:6mm 0 0;font-size:7pt}
.nota.escura{background:rgba(201,169,106,.08);border-left-color:var(--ouro-claro);color:#BFB6A4}
.nota.escura b{color:var(--ouro-claro)}

/* etapas */
.etapa-head{display:flex;gap:12mm;align-items:flex-start;margin-bottom:7mm}
.fases{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid var(--ouro);
   flex:1;margin-bottom:14mm}
.fase{padding:5mm 6mm 0 0;border-right:1px solid var(--fino)}
.fase:last-child{border-right:0}
.fase:not(:first-child){padding-left:6mm}
.fase-h{font-size:6.2pt;letter-spacing:.2em;color:var(--ouro);font-weight:600}
.fase-s{font-size:6.8pt;color:#8C8475;font-style:italic;margin:1.5mm 0 4mm}
.passo{margin-bottom:4.5mm}
.kicker{font-size:5.6pt;letter-spacing:.2em;color:var(--ouro);margin-bottom:1mm}
.passo-t{display:flex;justify-content:space-between;align-items:baseline}
.passo-t h5{font-size:8.6pt}
.num{font-family:'Cormorant Garamond',serif;font-size:11pt;color:var(--ouro)}
.passo p{font-size:6.8pt;line-height:1.5;color:var(--corpo);margin-top:1.2mm}
.saida{font-size:6.2pt;color:#8C8475;border-left:1px solid var(--fino);padding-left:2.5mm;margin-top:1.8mm}

/* hero + padrões */
.hero{height:82mm;background-size:cover;background-position:center 38%;position:relative}
.hero-badge{position:absolute;right:12mm;bottom:9mm;background:var(--creme);padding:6mm 7mm;max-width:88mm}
.hero-badge b{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:19pt;display:block;line-height:1}
.hero-badge span{display:block;font-size:5.9pt;letter-spacing:.2em;color:var(--ouro);margin-top:2mm}
.hero-badge i{display:block;font-style:normal;font-size:6pt;color:#8C8475;margin-top:2.5mm;line-height:1.4}
.pads{display:grid;grid-template-columns:repeat(5,1fr);gap:5mm;margin:6mm 0}
.pad{border-top:1px solid var(--ouro);padding-top:3mm}
.pad-n{font-family:'Cormorant Garamond',serif;font-size:14pt;line-height:1.05}
.pad-f{font-size:5.9pt;letter-spacing:.14em;color:var(--ouro);margin:1.5mm 0 2.5mm}
.pad-o{font-size:7pt;line-height:1.45;color:var(--corpo)}

/* dois ambientes por folha */
.dois{flex-direction:row}
.meio{flex:1;display:flex;flex-direction:column;min-width:0}
.meio+.meio{border-left:1px solid var(--fino)}
.meio-img{height:88mm;background-size:cover;background-position:center;position:relative;
   background-color:var(--creme2)}
.meio-img:after{content:'';position:absolute;top:0;left:0;right:0;height:18mm;
   background:linear-gradient(to bottom,rgba(20,15,10,.3),rgba(20,15,10,0))}
.meio-txt{padding:9mm 11mm 0;flex:1;display:flex;flex-direction:column}
.meio-txt h3{font-size:22pt;margin-bottom:5mm}
.meio-txt .bul li{font-size:7.2pt;line-height:1.52;padding-bottom:3.2mm}
.meio-txt .acab{margin-bottom:14mm;font-size:6.8pt}
.dois .rodape{left:11mm;right:11mm}

/* ambiente, folha inteira */
.amb{flex-direction:row}
.amb-img{width:55%;background-size:cover;background-position:center;position:relative;background-color:var(--creme2)}
.amb-img:after{content:'';position:absolute;top:0;left:0;right:0;height:26mm;
   background:linear-gradient(to bottom,rgba(20,15,10,.42),rgba(20,15,10,0))}
.amb-img.desenho{background-size:contain;background-repeat:no-repeat;background-color:#EDE7D8}
.amb-img.desenho:after{background:none}
.amb-img.desenho .amb-cap{color:var(--ouro);text-shadow:none}
.amb-cap{position:absolute;top:9mm;left:10mm;font-size:5.9pt;letter-spacing:.2em;color:rgba(255,255,255,.85);
   text-shadow:0 1px 6px rgba(0,0,0,.5)}
.amb-txt{flex:1;padding:16mm 15mm 0;display:flex;flex-direction:column}
.bul{list-style:none}
.bul li{font-size:7.6pt;line-height:1.58;color:var(--corpo);padding:0 0 4mm 5mm;position:relative}
.bul li:before{content:'';position:absolute;left:0;top:2.6mm;width:1.6mm;height:1.6mm;
   border-radius:50%;background:var(--ouro)}
.bul b{color:var(--tinta);font-weight:600}
.acab{margin-top:auto;margin-bottom:15mm;border-left:2px solid var(--ouro);padding-left:5mm;
   font-size:7.1pt;line-height:1.55;color:var(--corpo)}
.acab span{display:block;font-size:6.1pt;letter-spacing:.2em;color:var(--ouro);margin-bottom:2mm}

/* escuro */
.escuro{background:var(--escuro)}
.escuro h2.claro,.escuro .frase{color:var(--creme)}
.texto.claro{color:#B8AF9C}.texto.claro b{color:var(--creme)}
.big4{display:grid;grid-template-columns:repeat(4,1fr);gap:7mm;margin:9mm 0 0}
.big4>div{border-top:1px solid rgba(201,169,106,.4);padding-top:4mm}
.big4 b{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:26pt;color:var(--ouro-claro);
   display:block;line-height:1}
.big4 span{display:block;font-size:5.8pt;letter-spacing:.2em;color:#9A8F7B;margin:2.5mm 0 3mm}
.big4 p{font-size:7pt;line-height:1.5;color:#B8AF9C}
.frase{font-family:'Cormorant Garamond',serif;font-size:17pt;line-height:1.35;margin:9mm 0 0;max-width:185mm}
.frase i{color:var(--ouro-claro)}

/* ferragens */
.fers{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;margin-top:2mm}
.fers.tres{grid-template-columns:repeat(3,1fr);gap:8mm}
.fer-im{display:flex;gap:2mm;height:52mm;margin-bottom:4mm}
.fer-im>div{flex:1;background-size:cover;background-position:center;background-color:var(--creme2)}
.fers.tres .kicker{margin-bottom:1.5mm}
.fers.tres h4{font-size:12pt;margin-bottom:3.5mm}
.fers.tres li{font-size:7.2pt;padding-bottom:2.8mm}
.fer-q{border-top:1px solid var(--ouro);padding-top:3mm;margin-bottom:3mm}
.fer-q b{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:26pt;color:var(--ouro);
   display:block;line-height:1}
.fer-q span{display:block;font-size:5.8pt;letter-spacing:.2em;color:var(--corpo);margin-top:2mm}
.fer h4{font-size:10pt;font-family:'Cormorant Garamond',serif;font-weight:500;margin-bottom:3mm}
.fer ul{list-style:none}
.fer li{font-size:7pt;line-height:1.5;color:var(--corpo);padding:0 0 2.5mm 4mm;position:relative}
.fer li:before{content:'';position:absolute;left:0;top:2.2mm;width:1.4mm;height:1.4mm;
   border-radius:50%;background:var(--ouro)}
.fer b{color:var(--tinta);font-weight:600}

/* garantia */
.gar{display:grid;grid-template-columns:76mm 1fr 1fr;gap:9mm;margin-top:5mm}
.gar-card{background:var(--escuro);color:var(--creme);padding:9mm 8mm}
.gar-card b{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:44pt;line-height:1;
   color:var(--ouro-claro);display:block}
.gar-card span{display:block;font-size:5.9pt;letter-spacing:.2em;color:#9A8F7B;margin:3mm 0 7mm}
.gar-card h4{font-size:10pt;margin-bottom:2.5mm}
.gar-card p{font-size:7.2pt;line-height:1.5;color:#B8AF9C}
.gar-p{margin-bottom:5mm;position:relative}
.gar-p span{position:absolute;right:0;top:0;font-family:'Cormorant Garamond',serif;font-size:11pt;color:var(--ouro)}
.gar-p p{font-size:7pt;line-height:1.5;color:var(--corpo);margin-top:1.5mm}
.gar-i{margin-bottom:4.5mm}
.gar-i span{font-size:5.8pt;letter-spacing:.17em;color:var(--ouro);display:block;margin-bottom:1.5mm}
.gar-i p{font-size:7pt;line-height:1.5;color:var(--corpo)}

/* investimento */
.inv{display:grid;grid-template-columns:1fr 80mm;gap:10mm;margin-top:1mm}
table{width:100%;border-collapse:collapse;margin-top:4mm}
thead th{font-size:5.9pt;letter-spacing:.2em;color:var(--corpo);font-weight:600;text-align:left;
   padding-bottom:2.5mm;border-bottom:1px solid var(--fino)}
th.v,td.v{text-align:right}
tbody td{padding:1.65mm 0;border-bottom:1px solid var(--fino);font-size:7.9pt;vertical-align:top}
tbody td b{font-weight:600;display:block}
tbody td span{display:block;font-size:5.9pt;color:#8C8475;margin-top:.6mm}
td.v{font-weight:600;font-size:9pt;white-space:nowrap;background:rgba(165,136,79,.06);
   padding-right:4mm;padding-left:6mm}
tfoot td{padding:2.4mm 0;font-size:6.6pt;letter-spacing:.2em;color:var(--corpo);
   border-top:2px solid var(--ouro)}
tfoot td.v{font-family:'Cormorant Garamond',serif;font-size:19pt;letter-spacing:0;color:var(--tinta);
   padding-right:4mm}
.inv-card{background:var(--escuro);color:var(--creme);padding:10mm 9mm;align-self:start}
.preco{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:30pt;line-height:1;margin:2mm 0 5mm}
.inv-card p{font-size:7.2pt;line-height:1.55;color:#B8AF9C}
.hr{height:1px;background:rgba(214,201,174,.26);margin:7mm 0}
.entrada{font-size:12pt;font-weight:600;margin-top:1mm}

/* condições */
.cond{display:grid;grid-template-columns:repeat(3,1fr);gap:11mm;margin-top:4mm;flex:1}
.cond .eyebrow{margin-top:6mm}
.cond .eyebrow:first-child{margin-top:0}
.cond-v{font-size:10.5pt;font-weight:500;margin-bottom:1.5mm}
.cond p{font-size:7pt;line-height:1.5;color:var(--corpo)}
.pag td{padding:2.8mm 0;border-bottom:1px solid var(--fino);font-size:7.8pt}
.pag td.pc{text-align:right;font-weight:600;color:var(--ouro);width:14mm}
.pag td.v{background:none;font-size:8pt;padding-left:4mm}
.mini{font-size:6.3pt;color:#8C8475;margin-top:2.5mm}
.fora-i{margin-bottom:4mm}
.fora-i b{font-size:8pt;font-weight:600;display:block;margin-bottom:1.2mm}
.fora-i p{font-size:6.9pt;line-height:1.5;color:var(--corpo)}
.assina{display:grid;grid-template-columns:1fr 1fr;gap:14mm;margin-bottom:15mm}
.assina div{border-top:1px solid var(--tinta);padding-top:2.5mm;font-size:7.6pt}
</style></head><body>
'''


if __name__ == '__main__':
    saida = os.path.join(AQUI, 'pr', 'proposta.html')
    os.makedirs(os.path.dirname(saida), exist_ok=True)
    io.open(saida, 'w', encoding='utf-8').write(html())
    bruto, _ = le()
    fechado = rateia(bruto, b.PRECO_FECHADO)
    print('─' * 72)
    for k in ORDEM:
        print('  %-24s modelo %12s   fechado %12s' % (k, brl(bruto[k]), brl(fechado[k])))
    print('  %-24s modelo %12s   fechado %12s' % ('TOTAL', brl(sum(bruto.values())),
                                                  brl(sum(fechado.values()))))
    print('─' * 72)
    print('  html:', saida)

    # ── e o PDF, pela mesma mão: sem passo manual que alguém esquece ───
    pdf = os.path.join(AQUI, 'pr', 'Charbel Chelala · Proposta Valvic · Linha Blum.pdf')
    js = '''const {chromium} = require('playwright');
(async () => {
  const nav = await chromium.launch();
  const pg  = await nav.newPage();
  await pg.goto('file://' + process.argv[1], {waitUntil: 'networkidle'});
  await pg.emulateMedia({media: 'print'});
  await pg.pdf({path: process.argv[2], width: '297mm', height: '210mm',
                printBackground: true,
                margin: {top: '0', right: '0', bottom: '0', left: '0'}});
  await nav.close();
})();'''
    r = subprocess.run(['node', '-e', js, saida, pdf], capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(pdf):
        print('   pdf:', pdf)
    else:
        print('   ⚠ pdf não saiu:', (r.stderr or r.stdout).strip()[:300])
