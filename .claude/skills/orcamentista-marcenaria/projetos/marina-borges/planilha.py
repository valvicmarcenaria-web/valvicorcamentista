# -*- coding: utf-8 -*-
"""CHARBEL CHELALA — monta o conteúdo das abas da planilha da casa.

⭐ A planilha é a entrega; este arquivo é o que a enche. Cada aba sai com
  as seis seções do modelo, na mesma ordem e com os mesmos rótulos:
  O AMBIENTE · OS ITENS · O QUE NÃO É MARCENARIA · AS PEÇAS · AS NOTAS ·
  AS DÚVIDAS.

⛔ VALOR, NÃO FÓRMULA, nas colunas de custo. O IMPORTRANGE da aba
  "Base (importada)" só liga depois que uma PESSOA clica em PERMITIR
  ACESSO, e nenhum script dá essa autorização. Fórmula escrita antes disso
  vira #REF! e some com a planilha inteira. ⭐ A coluna CHAVE DA BASE fica
  preenchida em toda peça, que é o que permite religar depois.
"""
import importlib.util, sys, pathlib, json

AQUI = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('lv', AQUI / 'levantamento.py')
lv = importlib.util.module_from_spec(_s); sys.modules['lv'] = lv
_s.loader.exec_module(lv)
b = lv.b

FOLHAS = {15: 'cozinha', 16: 'cozinha, hall e jantar', 17: 'estar e TV',
          18: 'acessos e corredor', 19: 'suíte', 20: 'suíte', 21: 'suíte',
          22: 'banho da suíte', 23: 'banheiro social', 24: 'quarto',
          25: 'quarto'}

FORA = {
 '01 Cozinha': [
   '⛔ Bancadas A (287 × 65), B (72 × 41) e C (126 × 52) e o nicho de 203 × 70 × 32, '
   'todos em Quartzito Verde Guatemala — MARMORARIA.',
   '⛔ Forno a gás de embutir e os bojos das cubas — do cliente.',
   '⛔ O módulo de 121 × 82 da vista 02: a própria folha escreve "Painel fixo em '
   'ALVENARIA" em cima dele. ⚠ Mas ele está DESENHADO EM MADEIRA — está nas dúvidas.',
   '⛔ O revestimento existente de 72 × 85 da vista 02 — obra.'],
 '02 Hall e Jantar': [
   '⛔ O painel de ônix retroiluminado de 103 × 175 da divisória e o mármore do hall '
   'de 93 × 178 — MARMORARIA. ⭐ A MOLDURA de madeira em volta dos dois é nossa.',
   '⛔ Forro em gesso.'],
 '03 Estar e TV': [
   '⛔ A pedra vertical da TV, 193 × 147 × 4 em quartzito, e os fixadores em estrutura '
   'metálica que a apoiam — a folha diz "estrutura metálica para apoio da pedra".',
   '⛔ O rack em quartzito, 367 × 47 — MARMORARIA.',
   '⛔ O tampo da mesa de jantar, 150 × 77 em quartzito. ⭐ OS DOIS PÉS SÃO NOSSOS.',
   '⛔ Frigobar 40 L e adega de 14 garrafas Elettromec Inox — do cliente.'],
 '04 Acessos e Corredor': [
   '⛔ A faixa de quartzito de 105,49 que atravessa o ARMÁRIO F e a faixa horizontal '
   'de pedra do painel de 105 — MARMORARIA.',
   '⛔ A porta existente de 210 × 17 à esquerda da vista 05 — já está no apartamento.'],
 '05 Suíte': [
   '⛔ O forro em pintura branco neve do mapa-chave. ⭐ O forro em MDF Cipres, ao lado '
   'dele, é nosso.',
   '⛔ Colchão, cama e roupa de cama — móvel solto.'],
 '06 Closet': [
   '⛔ Nada de terceiro neste ambiente. ⭐ As 9 folhas em perfil de alumínio com vidro '
   'SÃO NOSSAS: saem no mesmo caminhão e são instaladas pela mesma equipe.'],
 '07 Banho da Suíte': [
   '⛔ O nicho do box, 54 × 243, com moldura em mármore branco — MARMORARIA.',
   '⛔ A "bancada nova" de 80 da folha 22: a folha não diz o material, e bancada de '
   'banho neste projeto tem sido sempre pedra. ⚠ Está nas dúvidas.',
   '⛔ Louça, metal e box.'],
 '08 Banheiro Social': [
   '⛔ Bancada em granito Grigio Carnico polido, cuba esculpida sem fundo, rodaparede '
   'de 160 × 110 e as prateleiras em mármore de 250 — MARMORARIA, cinco peças.',
   '⛔ Louça, metal e box.'],
 '09 Quarto': [
   '⛔ Papel de parede da vista 17 e o aparelho de ar-condicionado.',
   '⛔ Cabeceira estofada, cama e colchão — móvel solto e tapeceiro.'],
}

NOTAS = {
 '01 Cozinha': [
   '⭐ A FOLHA 15 QUASE FICOU DE FORA. O texto dela só nomeia Quartzito Verde '
   'Guatemala, e por isso ela estava arquivada como marmoraria. É a cozinha inteira. '
   'O que decide se a folha é nossa não é o material que ela nomeia, é o que ela desenha.',
   '⭐ Um padrão só de MDF: Caribe Linha Dual Syncro Guararapes, em 18 e em 15. '
   'O interior fecha em Branco TX, porque toda porta daqui é cheia.',
   '⭐ As 7 folhas da vista 02 saem das cotas de topo da própria prancha: '
   '31,5 · 31,5 · 27,5 · 27,5 · 23 · 35 · 35. Não foram divididas por conta.',
   '⭐ O QDC mora dentro da torre central e leva tampa de inspeção — é marcenaria, '
   'não elétrica.',
   '⛔ Puxador CAVA usinado no próprio material em toda a cozinha: 50 o metro de '
   'frente, não unidade. São 15 metros de frente.'],
 '02 Hall e Jantar': [
   '⭐ A cristaleira é a peça cara do ambiente, e não por causa da madeira: são duas '
   'folhas de perfil com vidro e quatro fitas de LED. O preço de folha vem de obra '
   'medida (Kenia e Fábio, 12/06/2026: porta de giro de cristaleira = R$ 475).',
   '⭐ A divisória do hall tem 7 cm de espessura e moldura curva r = 10 nas duas '
   'faces: a usinagem curva é manual, R$ 5,00 o metro, e são 7 metros.',
   '⭐ O forro do hall é de madeira e tem desenvolvimento de 141,37 — a cota está no '
   'DETALHE: FORRO HALL, não na planta.'],
 '03 Estar e TV': [
   '⭐ Três execuções de ripado diferentes no mesmo ambiente: porta de abrir, portas '
   'de correr e acabamento curvo. Ripa de 4 com vão de 2, substrato de 15 e duas '
   'camadas por causa dos 3 cm de espessura.',
   '⭐ OS PÉS DA MESA SÃO MARCENARIA E SÃO CAROS: miolo laminado de 10 chapas cada e '
   'entalhamento diagonal em CNC. O tampo em cima deles é da marmoraria.',
   '⚠ A porta é "vidro reflecta bronze". A Base tem reflecta bronze com perfil '
   'champanhe a R$ 450 a folha; o reflecta CHAMPAGNE segue sem cotação desde o '
   'projeto da Sandra.'],
 '04 Acessos e Corredor': [
   '⭐⭐ AS DUAS PORTAS DE PASSAGEM SOMEM DENTRO DO PAINEL. Não é porta encostada em '
   'painel: é folha de 208 cm embutida, com sistema pivô e fecho rolete, e o '
   'alinhamento do veio tem de atravessar a junta.',
   '⭐ O painel corre 346,53 contínuos. Chapa de 275 não atravessa isso: a peça sai '
   'declarada em partes e a emenda é projeto, não improviso.',
   '⭐ Perfil de proteção de piso em todo painel que toca o chão [Jonathan, 28/10].'],
 '05 Suíte': [
   '⭐⭐ QUATRO PADRÕES DE MDF NO MESMO AMBIENTE: Cipres, Fontana Linha Magma, Cacao '
   'Matt e o Branco TX do interior. Cada padrão arredonda a sua própria chapa, e é '
   'por isso que a suíte compra mais chapa do que a área dela sugere.',
   '⭐ As duas divisórias levam RIPADO VAZADO de 4 × 240 × 4,20 — vazado, não aplicado: '
   'a ripa atravessa e se vê dos dois lados.',
   '⭐ A prateleira do painel da vista 11 tem 225,5 de vão livre. Acima de 1,20 m a '
   'Base manda alma de aço, e é contra FLECHA, não contra empeno.',
   '⚠ O forro em MDF Cipres não tem UMA cota na folha 19. Os 9 m² são leitura do '
   'mapa-chave pela proporção com o painel da cabeceira. Tem de ser medido.'],
 '06 Closet': [
   '⭐⭐ O CLOSET É 27% DO PROJETO, e o motivo o desenho esconde e o render grita: '
   'AS NOVE FOLHAS NÃO SÃO DE MDF. São perfil de alumínio dourado com vidro, de piso '
   'a teto, nas três vistas.',
   '⭐ Por isso o interior sai em Cipres e não em Branco TX: com porta de vidro, o '
   'interior é fachada.',
   '⭐ A vista 9C é sapateira de PRATELEIRA INCLINADA: 8 × 22,50 = 180 por coluna, '
   'duas colunas, 16 prateleiras com encaixe usinado em ângulo.',
   '⚠ As folhas têm 2,57 m de altura. O R$ 1.400 da Base é de porta de espelho de '
   'cerca de 2,10 m. Esta é mais alta e leva vidro — ver as dúvidas.'],
 '07 Banho da Suíte': [
   '⭐ MDF Cinza Sagrado Duratex, padrão único do ambiente.',
   '⭐ As 4 folhas do superior são ESPELHADAS: espelho prata colado sobre a estrutura '
   'de MDF, 600 o m², mais a chapa por baixo. A fita de LED corre no eixo h = 90, '
   'dentro da faixa de espelho demarcada.'],
 '08 Banheiro Social': [
   '⭐ O ARMÁRIO G tem o puxador CAVA USINADO NA PRÓPRIA ESTRUTURA DO ESPELHO — a '
   'folha chama isso de "porta infinita". É usinagem, não puxador comprado.',
   '⭐ São três peças de espelho no ambiente: a folha do G, o espelho de 140 × 140 da '
   'vista 16, e a moldura.'],
 '09 Quarto': [
   '⭐ Duas folhas de correr de 97,5 × 251 em Cacao Matt. Toda porta deslizante leva '
   'desempenador, e folha de 70 cm ou mais leva DOIS: são 4.',
   '⭐ O móvel baú tem PORTA RETRÁTIL — a folha desenha a projeção de abertura. É '
   'sistema, não dobradiça.',
   '⭐ O painel da cabeceira da folha 25 tem 13 cm de profundidade e abraça um espelho '
   'de 75 × 220 dentro de moldura de 106 × 248.'],
}


def _esp(it, q):
    """a abertura de material de um item, para a seção O AMBIENTE"""
    pass


def linhas_ambiente(nome, d, T):
    """⭐ Seção ① · uma linha por material, por ferragem e por terceirizado."""
    rend = b.CHAPA_M2 * b.APROV
    L, custo_mat = [], 0.0
    #   chapa · ⛔ a chapa é do PROJETO: o ambiente leva a fração dele, com o
    #     rateio do arredondamento. Por isso sai com casa decimal.
    for k in sorted(d['area']):
        preco = T['preco'][k]
        sobra = T['chapas'][k] * preco - T['area'][k] / rend * preco
        parte = d['area'][k] / T['area'][k]
        c = d['area'][k] / rend * preco + sobra * parte
        custo_mat += c
        L.append([f'{k[0]} {k[1]} mm', f'{dec(d["area"][k])} m² deste ambiente · '
                  f'{dec(T["area"][k])} m² e {T["chapas"][k]} chapa(s) no projeto '
                  f'inteiro · {lv.brl(preco)} a chapa',
                  round(d['area'][k] / rend, 2), 'chapa', round(c, 2), 0])
    for rot, m, p in (('Fita de borda de cor', d['fita_cor'], b.FITA_COR),
                      ('Fita de borda Branco TX', d['fita_br'], b.FITA_BRANCA)):
        if m:
            c = m * p * b.FITA_PERDA
            custo_mat += c
            L.append([rot, f'{lv.brl(p)} o metro · perda de serra de '
                      f'{b.FITA_PERDA - 1:.0%}',
                      round(m, 1), 'm', round(c, 2), 0])
    #   ferragem e terceirizado, agrupados pelo rótulo
    for campo, un_pad in (('fer', 'un'), ('terc', None)):
        agr = {}
        for it, _dir in d['itens']:
            for linha in getattr(it, campo):
                if campo == 'fer':
                    n, q, u = linha; un = un_pad
                else:
                    n, q, u, un = linha
                a = agr.setdefault((n, u, un), [0.0, 0.0])
                a[0] += q; a[1] += q * u
        for (n, u, un), (q, c) in sorted(agr.items()):
            custo_mat += c
            L.append([n, f'{lv.brl(u)} o {un}',
                      round(q, 2), un, round(c, 2), 0])
    #   corte, frete, consumíveis e embalagem
    corte = (T['n_chapas'] * b.CORTE_CHAPA * (d['pecas'] / T['pecas'])
             + d['pecas'] * b.CORTE_PECA)
    L.append(['Corte', f'{d["pecas"]} peça(s) × R$ 2,50 · mais o rateio das '
              f'{T["n_chapas"]} chapas do projeto', d['pecas'], 'peça',
              round(corte, 2), 0])
    fr = lv.VIAGENS[nome] * b.FRETE_VIAGEM
    L.append(['Frete · R$ 200 a viagem', '⭐ A QUANTIDADE É DIGITADA: quantas '
              'viagens este ambiente leva.', lv.VIAGENS[nome], 'viagem',
              round(fr, 2), 0])
    chapa_fita = sum(r[4] for r in L if r[0].startswith(('MDF', 'Fita')))
    cons = chapa_fita * b.CONSUMIVEIS
    L.append(['Consumíveis', '6% sobre chapa e fita', b.CONSUMIVEIS, '%',
              round(cons, 2), 0])
    emb = (custo_mat + corte) * b.EMBALAGEM
    L.append(['Embalagem', '2% sobre o custo direto', b.EMBALAGEM, '%',
              round(emb, 2), 0])
    tot = d['direto']
    L.append(['CUSTO DIRETO DO AMBIENTE', '', '', '', round(tot, 2), 1.0])
    for r in L[:-1]:
        r[5] = round(r[4] / tot, 4) if tot else 0
    return L


def peca_custo(p, T):
    """⭐ O custo de MATERIAL de uma peça: chapa com o rateio do projeto,
    mais a fita dela. Corte, consumível, ferragem e frete são do ambiente e
    estão na seção ①, nunca duplicados aqui."""
    rend = b.CHAPA_M2 * b.APROV
    k = (p['mat'], p['esp'])
    a = p['L'] * p['A'] / 10000 * p['qtd']
    preco = T['preco'][k]
    sobra = T['chapas'][k] * preco - T['area'][k] / rend * preco
    c = a / rend * preco + sobra * (a / T['area'][k])
    fita = p['fita'] * p['qtd'] * (b.FITA_BRANCA if p['mat'] == 'MDF Branco TX'
                                   else b.FITA_COR) * b.FITA_PERDA
    return a, c + fita


def monta(nome, d, T):
    """o bloco inteiro de uma aba, a partir da coluna B"""
    folhas = ' e '.join(str(f) for f in sorted(d['folhas']))
    R = [[f'  VALVIC MARCENARIA        {nome[3:].upper()}'],
         [f'  {b.CLIENTE} · {b.ARQUITETA} · {b.EXECUTIVO}, folha(s) {folhas} · '
          f'ferragem Blum · {len(d["itens"])} itens · {d["pecas"]} peças'],
         [],
         ['  O AMBIENTE   ·   o que ele consome, por linha de material'],
         [],
         ['MATERIAL', 'ESPECIFICAÇÃO', 'QUANTIDADE', 'UN', 'CUSTO', '% DO CUSTO']]
    R += linhas_ambiente(nome, d, T)
    R += [[], ['  OS ITENS   ·   cada item é um móvel, e é assim que ele vai '
               'para a proposta'], [],
          ['ITEM', 'MÓVEL', 'MEDIDA E CADEIA DE COTAS', '', '', '', '',
           'PREÇO', 'CUSTO']]
    soma = 0.0
    for i, (it, dire) in enumerate(d['itens'], 1):
        soma += dire
        R.append([f'{i:02d}', it.nome, it.obs, '', '', '', '',
                  round(lv.preco_item(dire), 2), round(dire, 2)])
    R.append(['⭐ CONFERÊNCIA', 'a soma dos itens contra o custo direto da '
              'seção ①', f'diferença de {lv.brl(soma - d["direto"])}', '', '',
              '', '', round(lv.preco_item(d['direto']), 2), round(soma, 2)])
    R += [[], ['  O QUE NÃO É MARCENARIA   ·   está na prancha, não está '
               'nesta conta'], []]
    R += [['', x] for x in FORA[nome]]
    R += [[], ['  AS PEÇAS, ITEM POR ITEM   ·   cada linha é uma peça que vai '
               'para o plano de corte'], [],
          ['PEÇA', 'OBSERVAÇÃO', 'C', 'L', 'QTD', 'UN', 'CHAVE DA BASE',
           'ÁREA m²', 'CUSTO DE MATERIAL']]
    for it, _dir in d['itens']:
        R.append([f'■ {it.nome}', it.obs])
        for p in it.pecas:
            a, c = peca_custo(p, T)
            obs = p['obs']
            if max(p['L'], p['A']) > b.ALT_MAX:
                obs = (obs + ' · ' if obs else '') + (
                    f'⛔ {max(p["L"], p["A"]):.0f} cm NÃO CABE na chapa de 275: '
                    f'sai emendada, e a emenda é projeto')
            R.append([p['nome'], obs, round(p['L'], 2), round(p['A'], 2),
                      p['qtd'], 'peça', f'{p["mat"]} {p["esp"]}',
                      round(a, 3), round(c, 2)])
    R += [[], ['  AS NOTAS   ·   o que a leitura da prancha ensinou, e que a '
               'próxima pessoa precisa saber'], []]
    R += [['', x] for x in NOTAS[nome]]
    R += [[], ['  AS DÚVIDAS   ·   ⛔ cada uma é dinheiro parado, e estão em '
               'ordem de quanto valem'], []]
    R += [['', x] for x in DUVIDAS.get(nome, ['⭐ Nenhuma dúvida aberta '
                                              'específica deste ambiente.'])]
    return R


DUVIDAS = {
 '01 Cozinha': [
   '⛔ R$ 23.177 no projeto · O MDF CARIBE LINHA DUAL SYNCRO custa quanto? A Base só '
   'tem "MDF cor" a R$ 700 e tem uma linha separada, "CHAPA — COR E ACABAMENTO '
   'ESPECIAL · R$ 1.000, confirmado em plano de corte". Dual Syncro é sincronizado, '
   'que é exatamente isso. Vale uma ligação ao fornecedor.',
   '⚠ O módulo de 121 × 82 da vista 02 está escrito "painel fixo em ALVENARIA" e '
   'desenhado em MADEIRA. Se for nosso, entra ~1 m² de Caribe mais a frente. '
   'PERGUNTA PARA A ARQUITETA.'],
 '02 Hall e Jantar': [
   '⚠ As prateleiras da vitrine: madeira ou vidro? Orcei em MDF Caribe, como a folha '
   'desenha. O render mostra madeira com LED por baixo, o que confirma.'],
 '03 Estar e TV': [
   '⛔ SEM PREÇO NA BASE · "Reflecta champagne" segue sem cotação fechada desde o '
   'projeto da Sandra. Usei reflecta BRONZE com perfil champanhe, R$ 450 a folha, '
   'que é o que a folha 17 pede.',
   '⚠ O entalhamento diagonal dos dois pés da mesa foi orçado em R$ 1.500 o par de '
   'usinagem CNC. É a única linha deste ambiente sem referência na Base.'],
 '04 Acessos e Corredor': [
   '⚠ A porta embutida de 208 cm saiu com sistema pivô (R$ 120) e fecho rolete '
   '(R$ 75). Porta embutida em painel costuma pedir batente oculto, que a Base não '
   'tem. Confirmar com quem monta.'],
 '05 Suíte': [
   '⛔ R$ 2.423 por 3 m² · O FORRO EM MDF CIPRES NÃO TEM COTA NA FOLHA 19. Os 9 m² '
   'são leitura do mapa-chave. Medir resolve, e é a medição mais barata do projeto.',
   '⚠ R$ 4.083 · DUAS MESAS DE CABECEIRA OU UMA? A folha 20 desenha uma e a chama no '
   'singular (vistas 12C e 12D são duas vistas da MESMA peça). A cama tem dois lados. '
   'Orcei duas.',
   '⚠ A fita metálica em latão dourado da mesa de cabeceira saiu como "friso em perfil '
   'laqueado", R$ 160 o metro — o mais perto que a Base tem. Latão de verdade é outro '
   'fornecedor.'],
 '06 Closet': [
   '⛔ R$ 16.647 · QUANTO CUSTA UMA FOLHA DE 2,57 M EM PERFIL DE ALUMÍNIO COM VIDRO? '
   'Usei R$ 1.400, que é a linha "Porta de espelho · R$ 1.200 + R$ 200 de frete, cerca '
   'de 1.400 posto na obra" da Base. Mas aquela é de ~2,10 m e leva espelho; estas são '
   'nove folhas de 2,57 m com vidro e perfil dourado. A R$ 2.000 a folha, o projeto '
   'sobe R$ 16.647.',
   '⚠ A metragem de LED do closet (24 m nas três vistas) saiu do render, que mostra '
   'fita em cada prateleira e em cada arara. A folha 21 não desenha a iluminação.'],
 '07 Banho da Suíte': [
   '⚠ A "bancada nova" de 80 da folha 22 não tem material declarado. Deixei FORA, '
   'porque bancada de banho neste projeto tem sido sempre pedra. Se for marcenaria, '
   'entra.'],
 '08 Banheiro Social': [
   '⚠ O espelho de 140 × 140 da vista 16 está escrito "fixado na PAREDE", não na '
   'marcenaria. Incluí, porque é espelho de banheiro e sai no mesmo caminhão — mas a '
   'regra dos dois estados manda deixar isso escrito.'],
 '09 Quarto': [
   '⚠ O "sistema de porta retrátil" do baú saiu a R$ 900, o mesmo do sistema de correr '
   'Blum. Porta retrátil de verdade (que entra na lateral) é outro ferragem e é mais '
   'cara. Confirmar o que a arquiteta quer.',
   '⚠ R$ 2.720 no projeto · O RODAPÉ. A prancha pede RODAPÉ INOX h = 2 em cinco '
   'folhas, e orcei inox a R$ 85 o metro, que a Base tem. ⛔ Mas a regra da casa '
   '[Jonathan, 26/10/2026] diz: "a prancha pede base metálica; nós fazemos em MDF '
   'melamínico". Se valer a regra, devolve R$ 2.720.'],
}


#   ⛔⛔ O pasteData FALA A LÍNGUA DA PLANILHA, NÃO A MINHA.
#     Esta planilha é pt_BR. Mandei "0.0651" e o Google leu o ponto como
#     separador de MILHAR: virou 651, e o percentual apareceu como
#     65100,0%. Mandei "759.2" e ele desistiu de converter: virou TEXTO
#     alinhado à esquerda, que nenhuma soma enxerga.
#   ⭐ E O QUE DENUNCIOU FOI O FORMATO, não a conta: o Painel continuou
#     certo porque lá eu escrevi com `updateCells` e numberValue, que não
#     passa por parser nenhum. A mesma informação, por dois caminhos, com
#     dois resultados — e só um dos dois reclamava.
def dec(v, casas=2):
    """⭐ número DENTRO DE FRASE, com vírgula — a planilha é brasileira e a
    prosa dela também. "12.21 m²" numa célula de texto não quebra conta
    nenhuma, e é exatamente o tipo de detalhe que ele vê antes de mim."""
    return ('%%.%df' % casas) % v if False else ('{:.%df}' % casas).format(v).replace('.', ',')


def ptbr(x):
    """número com vírgula decimal, que é como esta planilha lê"""
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        return '' if x is None else str(x)
    if isinstance(x, int):
        return str(x)
    return repr(x).replace('.', ',')


def tsv(linhas):
    return '\n'.join('\t'.join(ptbr(c) for c in r) for r in linhas)


if __name__ == '__main__':
    T, R = lv.por_ambiente()
    saida = {a: monta(a, R[a], T) for a in sorted(R)}
    (AQUI / 'planilha.json').write_text(
        json.dumps(saida, ensure_ascii=False), encoding='utf-8')
    for a in sorted(saida):
        print('%-24s %4d linhas  ·  custo %12s  ·  preço %14s'
              % (a, len(saida[a]), lv.brl(R[a]['direto']),
                 lv.brl(lv.preco_item(R[a]['direto']))))
    print('%-24s %4d linhas  ·  custo %12s  ·  preço %14s'
          % ('TOTAL', sum(len(v) for v in saida.values()), lv.brl(T['direto']),
             lv.brl(lv.preco_item(T['direto']))))
