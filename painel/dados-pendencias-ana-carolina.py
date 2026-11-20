# -*- coding: utf-8 -*-
"""Dados do documento de pendências da obra Ana Carolina.

Editar aqui; o layout está em gerar-pendencias-ana-carolina.py.

Fonte: relato do Jonathan em 20/11/2026 (apontamentos da cliente em 19 e 20/11).
Ambientes vindos do bloco 3 da ficha de custo (N.GESTAO 2, aba 'Ana Carolina ').
"""

CLIENTE   = 'Ana Carolina Abreu'
OBRA      = 'Apto Funcionários · 10 ambientes'
VISTORIA  = '19/11/2026 — sem checklist'
PRAZO     = 'Sinteco entra 25/11 (quarta)'
EMISSAO   = '20/11/2026'
GESTOR    = 'Deivison Gonçalves'

CONTEXTO = [
    'sofreu <b>atraso longo na entrega</b>, em boa parte por problemas internos nossos;',
    'pagou o serviço <b>antecipadamente</b> para ajudar a empresa no caixa — e foi quem mais perdeu com o atraso;',
    'aceitou <b>sucessivos reacordos e reagendamentos</b> sem romper a relação.',
]
CONTEXTO_FECHO = (
    'Ela já nos deu crédito três vezes. Por isso cada pendência que aparece <b>agora</b>, '
    'depois de a obra ter sido declarada concluída e vistoriada, não é lida por ela como '
    'detalhe técnico — é lida como falta de cuidado. É aqui que a conta fica alta, e não '
    'em dinheiro: em confiança e em indicação.'
)

# (nº, pendência, por que não deveria ter chegado até a cliente, ação imediata)
APONTAMENTOS = [
    ('01', 'Espelho do lavabo — não entregue',
     'Não é detalhe: é peça de ambiente, prevista em projeto. Faltou conferir o projeto '
     'item a item antes de declarar a obra concluída.',
     'Medir o vão, confirmar LED e necessidade de painel, solicitar ao fornecedor'),
    ('02', 'Furo da porta do lavabo — mal executado',
     'Palavras da cliente: <i>“parece que a porta está estragada”.</i> O furo é recurso de '
     'segurança (acesso externo à fechadura, que fica pelo lado de dentro) — era previsto e '
     'deveria ter acabamento. Saiu da fábrica assim <b>e</b> passou pela vistoria na obra.',
     'Definir a solução de acabamento e executar na terça'),
    ('03', 'Prateleira da lavanderia — armário inferior',
     'Peça simples de marcenaria; ausência visível a olho na conferência de ambiente.',
     'Conferir medida no projeto, produzir e instalar'),
]

CAUSAS = [
    ('Não houve conferência do projeto contra o executado',
     'ninguém comparou a lista de itens do projeto com o que estava instalado — por isso um '
     'espelho inteiro passou.'),
    ('A vistoria de 19/11 foi feita sem documento',
     'sem checklist, sem lista de itens, sem assinatura. Vistoria sem papel é visita.'),
    ('Peça com defeito saiu da fábrica',
     'o furo da porta não foi barrado na saída — logo, não existe conferência de saída de peça.'),
]

# (quando, o que, quem, entregável)
PLANO = [
    ('Sáb 21/11<br><span class="h">manhã</span>',
     'Ir à obra: medir o vão do espelho do lavabo (largura × altura), fotografar o furo da '
     'porta, confirmar a prateleira faltante no armário inferior da lavanderia e varrer os '
     '8 ambientes com o checklist da folha 2',
     'Deivison', 'Checklist preenchido + medidas + fotos'),
    ('Sáb 21/11',
     'Conferir no projeto executivo (<span class="mono">Ana Carolina.pdf</span>, pasta de '
     'produção) se o espelho tem LED, qual o perfil e se exige painel de fundo; confirmar se '
     'há ponto de alimentação no lavabo',
     'Deivison', 'Definição escrita: com ou sem LED'),
    ('Sáb 21/11<br><span class="h">até o fim do dia</span>',
     'Solicitar o espelho ao fornecedor com a medida final, <b>exigindo entrega até terça '
     '24/11</b>. Se o fornecedor não atender no sábado, deixar o pedido pronto e disparar na '
     'primeira hora de segunda, com entrega comprometida para terça de manhã',
     'Deivison + Karla', 'Pedido emitido com data de entrega confirmada'),
    ('Seg 23/11',
     'Produzir na fábrica: painel de fundo do espelho (se houver LED), prateleira da '
     'lavanderia e a solução de acabamento do furo da porta',
     'Deivison', 'Peças prontas e separadas para a obra'),
    ('Ter 24/11',
     'Equipe na obra: instalar o painel, colar o espelho, instalar a prateleira, corrigir o '
     'furo da porta e resolver tudo o que a varredura de sábado apontar',
     'Equipe designada', 'Obra sem pendência de marcenaria'),
    ('Ter 24/11<br><span class="h">fim do dia</span>',
     'Vistoria final completa, com o checklist em mãos, assinada por você e pela cliente',
     'Deivison + cliente', 'Checklist assinado = entrega aceita'),
    ('Qua 25/11',
     'Sinteco entra. Nada nosso pode estar pendente nem ocupando a obra',
     '—', 'Obra entregue'),
]

RISCOS = [
    ('O prazo do fornecedor é o único ponto fora do nosso controle.',
     'Por isso a medida tem de sair no sábado e o pedido no mesmo dia. Um dia perdido aqui '
     'queima o prazo do Sinteco e a obra volta a atrasar por nossa causa.'),
    ('Se o espelho tiver LED e não houver ponto de alimentação no lavabo,',
     'isso tem de ser comunicado à cliente e à arquiteta <b>no sábado</b> — não na terça, com '
     'a equipe na obra.'),
    ('Toda pendência nova que a varredura de sábado apontar entra no mesmo pacote de terça.',
     'Nada fica para depois do Sinteco: com o piso tratado, voltar à obra passa a depender '
     'da autorização da cliente.'),
]

AMBIENTES = [
    'Sala · painéis', 'Sala · louçaria', 'Cozinha', 'Rouparia',
    'Banho social', 'Banho casal', 'Lavabo', 'Lavanderia',
]

CRITERIOS = [
    'Itens do<br>projeto<br>conferidos<br>um a um',
    'Portas e<br>gavetas:<br>alinhamento<br>e abertura',
    'Ferragens<br>e<br>puxadores',
    'Acabamento:<br>fita, vedação<br>e retoque',
    'Iluminação<br>e LED<br>funcionando',
]

PENDENCIAS_CONFIRMADAS = [
    ('Espelho do lavabo', 'medida: ____________ × ____________ mm   ·   LED: ( ) sim  ( ) não'),
    ('Furo da porta do lavabo', 'solução definida: ______________________________________'),
    ('Prateleira do armário inferior da lavanderia', 'medida: ____________ × ____________ mm'),
]

LINHAS_NOVAS = 15
