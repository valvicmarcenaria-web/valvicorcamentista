# -*- coding: utf-8 -*-
"""Gera a aba `Base (importada)` da PLANILHA BASE da Valvic.

⭐⭐ POR QUE ELA MUDOU EM RELAÇÃO À DO ICA. Na do ICA o preço vinha por
  POSIÇÃO: a célula escrevia `=I19` e torcia para que a linha 19 do bloco
  importado continuasse sendo o Melamínico Fosco de 18 mm. A própria aba
  avisava: "LINHA NOVA VAI NO FIM, NUNCA NO MEIO". ⛔ Isso é uma bomba-
  relógio: basta alguém inserir uma linha na Base de Custos e TODO orçamento
  que usar esta planilha passa a somar o preço errado, calado.

⭐ Aqui o preço vem por NOME. Cada chave declara o PRODUTO como ele se chama
  na Base, e a espessura quando for chapa; a fórmula busca por esses dois
  critérios dentro do bloco importado. Inserir, remover ou reordenar linha
  na Base deixa de quebrar nada. É a mesma lição que o Painel já tinha
  aprendido — buscar por rótulo, não por posição.

⛔ locale pt_BR: separador de argumento é ';'. Nome de função em INGLÊS, que
  a API normaliza.

Layout da aba:
    A  chave que o motor usa        E  produto, como se chama na Base
    B  R$ (fórmula ou digitado)     F  espessura, só para chapa
    C  unidade                      N1 bloco MDF importado        (N:R)
    D  de onde vem, em texto        T1 bloco Ferragens importado  (T:X)
"""
BASE_CUSTOS = '13cZGej-AUTTyWZblqtraTBnc1HUECjT6fy3zy6R5mv4'

# chave, unidade, de-onde-vem, produto na Base, esp, valor digitado
#   produto preenchido  → busca no bloco (esp preenchida = MDF, vazia = ferragem)
#   produto vazio       → o valor de B é digitado, e D diz por quê
K = [
 ('§', 'OS PARÂMETROS DA CASA — não vêm da Base, são regra'),
 ('Área da chapa',  'm²', 'Chapa de 275 × 185 cm', '', '', 5.0875),
 ('Aproveitamento', '',   '⭐ 0,80 · a chapa principal rende de 85 a 92%, o '
                          'projeto inteiro rende menos', '', '', 0.80),
 ('Consumíveis',    '',   '6% sobre chapa e fita', '', '', 0.06),
 ('Embalagem',      '',   '2% sobre o custo direto', '', '', 0.02),

 ('§', 'CHAPA — o preço vem da Base pelo PRODUTO e pela ESPESSURA'),
 ('MDF cor 18',  'chapa', 'Melamínico Fosco · ⭐ a chapa de cor padrão da casa',
  'MDF Melamínico Fosco', 18, None),
 ('MDF cor 15',  'chapa', 'Melamínico Fosco', 'MDF Melamínico Fosco', 15, None),
 ('MDF cor 6',   'chapa', 'Melamínico Fosco', 'MDF Melamínico Fosco', 6, None),
 ('MDF branco 18', 'chapa', 'Branco TX', 'MDF Branco TX', 18, None),
 ('MDF branco 15', 'chapa', 'Branco TX', 'MDF Branco TX', 15, None),
 ('MDF branco 6',  'chapa', 'Branco TX', 'MDF Branco TX', 6, None),
 ('MDF Branco TX 18', 'chapa', 'Branco TX · o nome do produto na Base',
  'MDF Branco TX', 18, None),
 ('MDF Branco TX 15', 'chapa', 'Branco TX', 'MDF Branco TX', 15, None),
 ('MDF Branco TX 6',  'chapa', 'Branco TX', 'MDF Branco TX', 6, None),
 ('MDF Cru 18', 'chapa', '⛔ NÃO EXISTE NA BASE. Laca é MDF cru mais pintura '
  'em cabine, e a Base não tem linha de cru. Valor DERIVADO da razão '
  'cru/fosco de 0,76 da base antiga — confirmar com o fornecedor', '', '', 530),
 ('MDF Cru 15', 'chapa', '⛔ derivado, ver acima', '', '', 410),
 ('MDF Cru 6',  'chapa', '⛔ derivado, ver acima', '', '', 255),

 ('§', 'FITA E FILETAGEM — ⭐ são DUAS coisas, e a Base as traz num preço só'),
 ('Fita cor', 'm', '⭐ Os R$ 5,50 da "fita de cor com filetagem" da Base são '
  'R$ 3,00 de FITA mais R$ 2,50 de FILETAGEM. Juntos num número, nunca se vê '
  'que a fita branca custa R$ 2,00 e que a filetagem de ripa custa o dobro',
  '', '', 3.00),
 ('Fita Branco TX', 'm', 'Caixaria · R$ 2,00 contra R$ 3,00 da fita de cor',
  '', '', 2.00),
 ('Filetagem automática', 'm', 'Coladeira · 15 e 18 mm · serviço, sem '
  'desperdício', '', '', 2.50),
 ('Filetagem manual', 'm', '⛔ Ripa e chapa de 6 mm não entram na coladeira',
  '', '', 5.00),

 ('§', 'FERRAGEM — o preço vem da Base pelo nome do PRODUTO'),
 ('Dobradiça', 'un', 'A dobradiça que vale hoje', 'Dobradiça Blum', '', None),
 ('Corrediça', 'por gaveta', 'A corrediça que vale hoje', 'Corrediça Blum', '', None),
 ('Dobradiça Hettich', 'un', 'Linha Gold · 100 mil ciclos · ajuste 3D',
  'Hettich Sensys', '', None),
 ('Corrediça Hettich', 'par', 'Linha Gold · oculta · 30 kg · 100 mil ciclos',
  'Hettich Quadro V6 500 mm', '', None),
 ('Corrediça Hardt', 'par', '⭐ o Padrão da casa · 5 anos de garantia',
  'Hardt Invisível P-10', '', None),
 ('Dobradiça vidro', 'un', '⚠ A COTAR · faixa observada de 30 a 85',
  'Dobradiça para porta de vidro', '', None),
 ('Báscula HK-XS', 'un', '⭐ A báscula da casa · ⛔ é DE MOLAS, não a gás',
  'Blum AVENTOS HK-XS', '', None),
 ('Pulsador', 'un', '⚠ Pulsador e puxador slim NÃO se somam na mesma frente',
  'Pulsador Blum Tip-on ou Servo', '', None),
 ('Puxador slim', 'un', 'É o que abre a báscula quando não há cava',
  'Puxador slim para báscula', '', None),
 ('Cava usinada', 'm', 'Por metro de frente · ⚠ faixa observada de 25 a 50',
  'Cava usinada, por metro de frente', '', None),
 ('Puxador Alças Traso 128', 'un', 'Zen Design · 128 mm',
  'Puxador Alças Traso 128 mm', '', None),
 ('Puxador passante', 'm', 'Perfil SP7000, por metro de frente',
  'Perfil puxador passante SP7000', '', None),
 ('Alma de aço', 'barra', '⭐ Prateleira de vão acima de 1,20 m · contra '
  'FLECHA, não contra empeno',
  'Alma de aço · barra chata 5 mm, barra de 3 m', '', None),
 ('Suporte oculto', 'un', '⭐ De 40 em 40 cm · ⛔ é o de prateleira de PAREDE, '
  'não o jogo de quatro de armário', 'Suporte oculto de prateleira', '', None),
 ('Cabideiro', 'un', '', 'Cabideiro em metal preto ou grafite', '', None),
 ('LED conjunto', 'm', 'Fita, perfil, usinagem e instalação',
  'LED COB, conjunto completo', '', None),
 ('Perfil de LED', 'm', 'Só o perfil, com difusor', 'Perfil de LED com difusor',
  '', None),
 ('Fonte de LED', 'un', 'Uma a cada 8 a 10 m de perfil', 'Fonte de LED', '', None),
 ('Sistema de correr SS-150', 'conjunto', '⭐ Duas portas · o sistema que a '
  'arquiteta costuma especificar em porta flutuante', 'SS150, 2 portas', '', None),
 ('Sistema de correr Dominus', 'conjunto', '⭐ O sistema de correr da casa · '
  'flutuante, trilho oculto, duplo amortecimento', 'Dominus Rometal, 2 portas',
  '', None),
 ('Desempenador de porta', 'un', '⭐⭐ PADRÃO EM TODA PORTA DESLIZANTE, e '
  'folha de 70 cm ou mais leva DOIS · anti-empeno', 'Desempenador de portas',
  '', None),
 ('Corrediça de carga', 'par', '⛔ leito de bicama · A COTAR',
  'Corrediça de carga para leito de cama', '', None),
 ('Pistão de tampo de baú', 'un', '⛔ dois por tampo · A COTAR',
  'Pistão de tampo de baú', '', None),

 ('§', 'AS REGRAS QUE O JONATHAN CRAVOU — não existem na Base com este nome'),
 ('Suporte de prateleira', 'jogo', '⭐ [Jonathan, 28/10/2026] Toda prateleira '
  'INTERNA de armário leva composição de 4 suportes · ⛔ não é o suporte '
  'oculto de R$ 30', '', '', 6.50),
 ('Corrediça touch', 'por gaveta', '⭐ [Jonathan, 28/10/2026] SUBSTITUI o par '
  'de corrediça E o pulsador — os dois', '', '', 500.00),
 ('Perfil de proteção de piso', 'm', '⭐ [Jonathan, 28/10/2026] Em todo painel '
  'que toca o chão', '', '', 15.00),
 ('Estrado em metalon', 'quadro', '⭐ [Jonathan, 28/10/2026] Um por leito · '
  '⛔ some o painel de MDF', '', '', 250.00),
 ('Malha de cordas náuticas', 'm²', '⭐ [Jonathan, 28/10/2026] Quando '
  'substitui o estrado', '', '', 250.00),
 ('Palhinha natural', 'm²', '⭐ [Jonathan, 28/10/2026] É TAPECEIRO · ⛔ não é '
  'a chapa melamínica que imita o desenho', '', '', 650.00),
 ('Estofamento em linho', 'm²', '⭐ [Jonathan, 28/10/2026]', '', '', 600.00),
 ('Corte por chapa', 'chapa', '⭐ [Jonathan, 28/10/2026] Por ambiente',
  '', '', 2.00),
 ('Corte por peça', 'peça', '⭐ [Jonathan, 28/10/2026] Por ambiente',
  '', '', 2.50),
 ('Frete', 'viagem', '⭐ [Jonathan, 29/10/2026] A quantidade é digitada na '
  'célula amarela de cada aba de ambiente', '', '', 200.00),
 ('Laca, por m² de peça', 'm²', '⭐ Peça LISA · ⚠ frente com relevo de router '
  'pinta mais devagar: perguntar o acréscimo ao pintor', '', '', 650.00),
 ('Espelho prata colado', 'm²', '⭐ Espelho FIXO, colado sobre MDF · mais a '
  'chapa por baixo', '', '', 600.00),
 ('Porta de espelho em alumínio', 'm²', '⭐ Folha que ABRE ou CORRE: perfil de '
  'alumínio mais espelho com película · ⛔ NÃO entra no plano de corte',
  '', '', 700.00),

 ('§', '⛔ OS BURACOS CONHECIDOS — vazios DE PROPÓSITO, para gritar'),
 ('Moldura provençal', 'frente', '⛔ A usinagem do relevo na router não tem '
  'preço. Cronometrar uma frente na fábrica resolve', '', '', ''),
 ('Usinagem de muxarabi vazado', 'm', '⛔ Corte de router por metro, em painel '
  'vazado, ripado ou perfurado. Cronometrar uma peça resolve', '', '', ''),
 ('Vidro temperado incolor', 'm²', '⛔ A cotar com o vidraceiro', '', '', ''),
 ('Vidro reflecta', 'm²', '⛔ Sem preço desde o projeto da Sandra', '', '', ''),
 ('Serralheria estrutural', 'conjunto', '⛔⛔ NÃO TEM PREÇO UNITÁRIO: cada peça '
  'é um orçamento fechado do serralheiro, e o valor vem da aba do ambiente, '
  'linha por linha', '', '', ''),
 ('Carreto', 'viagem', '⛔ A preencher', '', '', ''),
 ('Rodízio de gaveteiro', 'un', '⛔ A cotar', '', '', ''),
 ('Puxador NEO32 Bronze', 'un', '⛔ A cotar', '', '', ''),
]

def linhas():
    """Devolve (valores A:F, fórmulas de B) prontos para a API."""
    vals, fmls, r = [], [], 6
    for item in K:
        if item[0] == '§':
            vals.append([item[1], '', '', '', '', '']); fmls.append(None)
            r += 1; continue
        ch, un, de, prod, esp, lit = item
        if prod:
            if esp:   # chapa: produto MAIS espessura
                f = (f'=IFERROR(INDEX($Q$1:$Q$80;MATCH(1;($N$1:$N$80=$E{r})'
                     f'*($P$1:$P$80=$F{r});0));"")')
            else:     # ferragem: o nome do produto já é único
                f = f'=IFERROR(VLOOKUP($E{r};$T$1:$X$150;4;FALSE);"")'
            vals.append([ch, '', un, de, prod, esp]); fmls.append(f)
        else:
            vals.append([ch, lit, un, de, '', '']); fmls.append(None)
        r += 1
    return vals, fmls

if __name__ == '__main__':
    import json
    v, f = linhas()
    print(f'{len(v)} linhas · de A6 a F{5+len(v)}')
    print(f'{sum(1 for x in f if x)} com fórmula de busca · '
          f'{sum(1 for x in f if not x)} digitadas ou de seção')
    json.dump({'vals': v, 'fmls': f}, open('_base-importada.json', 'w'),
              ensure_ascii=False)
