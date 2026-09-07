#!/usr/bin/env python3
"""
Abertura de produção — gera todos os checklists de um projeto, já preenchidos.

    python3 gerar-abertura.py projeto.json [saida.pdf]

O JSON descreve o projeto; o script devolve um HTML e um PDF com as sete folhas
(escopo de venda, ficha de medição, matriz do marceneiro, conferência de saída,
insumos e kit, kit da obra, kit do montador e conferência final da direção).

POR QUE ESTE SCRIPT EXISTE, se já há a ferramenta web:
o painel onde o artefato roda bloqueia impressão e download — é regra da plataforma,
não falha de código. A ferramenta web serve para ler o contrato e validar os dados;
o PDF sai daqui e chega como arquivo, sem popup e sem copiar nada.

O JSON (todos os campos são texto; ambientes é uma lista):

{
  "cliente": "Lucas e Ana",
  "op": "P-2026-058",
  "versao": "v2",
  "endereco": "Rua Ouro Preto, 1240 — Belvedere",
  "arquiteto": "Isabella Biancardine",
  "vendedor": "Jonathan",
  "prazo": "30/10/2026",
  "condominio": "Ed. Vista — 8º andar, elevador de serviço",
  "acesso": "Carga e descarga só até as 17h",
  "caixaria": "Branco Diamante",
  "dobradica": "Hettich Sensys ônix",
  "corredica": "Oculta soft-close",
  "puxador": "Passante e em cava",
  "iluminacao": "Fita de LED 240 leds com perfil e difusor",
  "ambientes": [
    {"nome": "Living jantar", "itens": ["Cristaleira"], "descricao": "..."},
    ...
  ]
}

As marcas de atenção de cada ambiente (led, vidro, serralheria, pedra, correr,
validar) são deduzidas da descrição — e podem ser forçadas no JSON, por exemplo
"led": true. É isso que faz a coluna de LED aparecer só onde há LED, e a tarja de
"a validar" só onde o contrato deixou algo em aberto.
"""
import html
import json
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(AQUI, 'folhas.css'), encoding='utf-8').read()
MAX_LINHAS = 22   # linhas de conferência por folha
MAX_COLS = 6      # ambientes por folha nas tabelas em matriz

PADRAO = [('caixaria', 'Cor da caixaria interna'), ('dobradica', 'Dobradiça'),
          ('corredica', 'Corrediça'), ('puxador', 'Puxador / perfil'), ('iluminacao', 'Iluminação')]

MARCAS = {
    'led': r'\bled\b|ilumina|sensor',
    'vidro': r'vidro|espelho|reflecta',
    'serralheria': r'serralheria|tubular|eletrost[áa]tic|a[çc]o',
    'pedra': r'tampo|bancada em|pedra|granito|m[áa]rmore|quartzo',
    'correr': r'deslizante|correr|coplanar|de passagem',
    'validar': r'a se validar|a validar|obs\.|verificar',
}


def e(x):
    return html.escape(str(x or ''))


def preparar(p):
    """Completa o que faltar e deduz as marcas de atenção de cada ambiente."""
    p.setdefault('ambientes', [])
    for a in p['ambientes']:
        a.setdefault('itens', [])
        a.setdefault('descricao', '')
        base = f"{a.get('nome','')} {' '.join(a['itens'])} {a['descricao']}".lower()
        for k, rx in MARCAS.items():
            if k not in a:
                a[k] = bool(re.search(rx, base))
    return p


# ── peças comuns a todas as folhas ────────────────────────────────────────────
def cab(tt, kx, sb):
    return (f'<div class="sh-h"><div class="co">Valvic Marcenaria</div>'
            f'<div class="sb">Vargas Decor Ltda · BH/MG · {e(sb)}</div>'
            f'<div class="tt">{e(tt)}</div><div class="kx">{e(kx)}</div></div>')


def ident(p, extra=None):
    if extra is None:
        extra = f'<div><b>Aberto em:</b> <span class="v">{e(p.get("aberto"))}</span></div>'
    return (f'<div class="sh-id">'
            f'<div><b>Cliente:</b> <span class="v">{e(p.get("cliente"))}</span></div>'
            f'<div><b>OP:</b> <span class="v">{e(p.get("op"))}</span></div>'
            f'<div><b>Prazo:</b> <span class="v">{e(p.get("prazo"))}</span></div>'
            f'{extra}</div>')


def rodape(p, dir_, pg=''):
    return (f'<div class="sh-f"><span>Valvic Marcenaria · OP {e(p.get("op"))} · {e(p.get("cliente"))}</span>'
            f'<span class="r">{e(dir_)}{" · " + e(pg) if pg else ""}</span></div>')


def etiquetas(a):
    t = [n for k, n in [('led', 'LED'), ('vidro', 'vidro'), ('serralheria', 'serralheria'),
                        ('pedra', 'pedra'), ('correr', 'correr')] if a.get(k)]
    if a.get('validar'):
        t.append('A VALIDAR')
    return e(' · '.join(t)) or '—'


def linhas_do(a):
    """Os itens do contrato mais duas linhas em branco, para a fábrica quebrar em mais módulos."""
    return list(a['itens']) + ['', '']


def paginar(grupos, maximo):
    """Empacota grupos em folhas sem partir um ambiente à toa."""
    pgs, cur, n = [], [], 0
    for g in grupos:
        resto, primeiro = list(g['linhas']), True
        while resto:
            if maximo - n <= 2 and cur:
                pgs.append(cur); cur, n = [], 0; continue
            corte = min(maximo - n, len(resto))
            cur.append({'amb': g['amb'], 'linhas': resto[:corte], 'cont': not primeiro})
            resto = resto[corte:]
            n += corte; primeiro = False
            if n >= maximo:
                pgs.append(cur); cur, n = [], 0
    if cur:
        pgs.append(cur)
    return pgs or [[]]


def corpo_grupos(grupos, celulas):
    """A célula do ambiente ocupa todas as linhas dele; a linha dourada separa um do outro."""
    out = []
    for g in grupos:
        for k, linha in enumerate(g['linhas']):
            cont = '<br><span style="font-weight:400;font-size:8px">(continua)</span>' if g['cont'] else ''
            amb = (f'<td class="amb" rowspan="{len(g["linhas"])}">{e(g["amb"]["nome"])}{cont}</td>'
                   if k == 0 else '')
            out.append(f'<tr class="{"grp" if k == 0 else ""}">{amb}<td>{e(linha)}</td>{celulas(g["amb"])}</tr>')
    return ''.join(out)


def caixa(n=1):
    return '<td class="c"><span class="bx"></span></td>' * n


def vazias(n):
    return '<td></td>' * n


# ── 1 · escopo de venda ───────────────────────────────────────────────────────
def folha_escopo(p):
    linhas_padrao = ''.join(
        f'<td style="width:15%"><b>{e(r)}</b></td><td>{e(p.get(k)) or "—"}</td>'
        for k, r in PADRAO[:3])
    linhas_padrao2 = ''.join(
        f'<td><b>{e(r)}</b></td><td>{e(p.get(k)) or "—"}</td>' for k, r in PADRAO[3:]) + '<td></td><td></td>'
    corpo = ''.join(
        f'<tr class="{"hot" if a.get("validar") else ""}"><td class="c">{i+1}</td>'
        f'<td><b>{e(a["nome"])}</b></td><td>{e(" · ".join(a["itens"]))}</td>'
        f'<td class="sub">{e(a["descricao"][:220])}</td><td>{etiquetas(a)}</td></tr>'
        for i, a in enumerate(p['ambientes']))
    return f'''<section class="sheet">
    {cab('Escopo de Venda', 'O que foi vendido — para a produção não adivinhar', 'Abertura de produção')}
    {ident(p)}
    <div class="sh-id" style="grid-template-columns:repeat(3,1fr)">
      <div><b>Obra:</b> {e(p.get('endereco'))}</div>
      <div><b>Arquiteto / RT:</b> {e(p.get('arquiteto'))}</div>
      <div><b>Vendedor:</b> {e(p.get('vendedor'))}</div>
      <div><b>Versão do projeto:</b> {e(p.get('versao'))}</div>
      <div><b>Condomínio / acesso:</b> {e(p.get('condominio'))}</div>
      <div><b>Restrições:</b> {e(p.get('acesso'))}</div>
    </div>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Padrão geral
      <small>· vale para tudo, salvo o que a descrição do item disser em contrário</small></span></div>
    <table><tbody><tr>{linhas_padrao}</tr><tr>{linhas_padrao2}</tr></tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Ambientes e itens</span></div>
    <table><thead><tr><th class="c" style="width:5%">Nº</th><th style="width:20%">Ambiente</th>
      <th style="width:24%">Itens</th><th>Descrição do contrato</th>
      <th style="width:13%">Atenção</th></tr></thead><tbody>{corpo}</tbody></table>
    <div class="sh-note"><b>A trava:</b> ambiente marcado como <b>item a validar</b> não entra em
    programação. O que estiver aberto — cor, medida, puxador, ferragem, embutido — volta ao comercial
    e se resolve <b>antes</b> de cortar chapa. Chapa cortada errada não tem conserto: compra-se outra.</div>
    <div class="sh-sign"><div>Aberto por · data</div><div>Coordenação de produção · ciente</div></div>
    {rodape(p, 'ESCOPO DE VENDA')}</section>'''


# ── 2 · ficha de medição ──────────────────────────────────────────────────────
COMBINADOS = [
    'Unidade sempre em <b>milímetros</b>. Sem cm e sem "mais ou menos".',
    '<b>Canto de referência</b> por ambiente: escolha um canto (0,0) e cote tudo a partir dele.',
    'Parede fora de esquadro: meça em <b>3 alturas</b>, use a menor e anote a diferença.',
    'Confira as <b>diagonais</b> do ambiente. Diferentes = ambiente torto, precisa de folga.',
    'Pé-direito e rebaixo: meça a <b>altura livre real</b> — a sanca de LED come altura.',
    '<b>Foto limpa e foto cotada</b> de cada parede, nomeadas Ambiente-Parede.',
    'Cote <b>toda interferência</b> em X,Y do canto: tomada, água, esgoto, gás, viga, ar.',
    'Revestimento pronto? Se não, registre <b>"medida sobre contrapiso / reboco"</b>.',
    'Nicho de embutido = <b>medida do aparelho</b>, batendo marca e modelo do escopo.',
    'Acesso: confirme que o <b>maior módulo passa</b> pela porta, corredor, curva e elevador.',
]


def folha_medicao(p):
    metodo = ''.join(f'<tr><td class="c" style="width:5%"><b>{i+1}</b></td><td>{c}</td></tr>'
                     for i, c in enumerate(COMBINADOS))
    corpo = ''.join(f'<tr><td><b>{e(a["nome"])}</b></td><td></td><td></td>{caixa(3)}<td></td></tr>'
                    for a in p['ambientes'])
    corpo += (f'<tr><td></td><td></td><td></td>{caixa(3)}<td></td></tr>') * 3
    return f'''<section class="sheet">
    {cab('Ficha de Medição', 'Medidas em mm · anexar as fotos cotadas', 'Conferência técnica')}
    {ident(p)}
    <div class="sh-sec"><span class="bar"></span><span class="tx">Os dez combinados
      <small>· não é sobre como medir, é sobre não deixar buraco de informação</small></span></div>
    <table><tbody>{metodo}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Levantamento por ambiente</span></div>
    <table><thead><tr><th style="width:17%">Ambiente</th><th style="width:15%">Canto de referência</th>
      <th style="width:13%">Pé-direito livre</th><th class="c" style="width:11%">Revest. pronto</th>
      <th class="c" style="width:11%">Diagonais iguais</th><th class="c" style="width:10%">Fotos</th>
      <th>Interferências cotadas (X,Y)</th></tr></thead><tbody>{corpo}</tbody></table>
    <div class="sh-note"><b>Regra de ouro:</b> medida não é opinião. Na dúvida, meça de novo e
    fotografe. É mais barato voltar à obra hoje do que refazer um móvel amanhã.</div>
    <div class="sh-sign"><div>Quem mediu · data</div><div>Conferido por · data</div></div>
    {rodape(p, 'FICHA DE MEDIÇÃO')}</section>'''


# ── 3 · matriz do marceneiro ──────────────────────────────────────────────────
def folhas_matriz(p):
    tem_led = any(a.get('led') for a in p['ambientes'])
    cols = ['Medida', 'Acabam.', 'Ferragem', 'Folgas'] + (['LED'] if tem_led else []) + ['Limpeza', 'Embal.']

    def cel(a):
        out = ''
        for c in cols:
            out += ('<td class="c" style="color:#b3aa96">—</td>'
                    if c == 'LED' and not a.get('led') else caixa())
        return out + '<td class="c"><span class="bx" style="border-radius:50%;width:14px;height:14px"></span></td><td></td>'

    pgs = paginar([{'amb': a, 'linhas': linhas_do(a)} for a in p['ambientes']], MAX_LINHAS)
    a_validar = [a['nome'] for a in p['ambientes'] if a.get('validar')]
    alerta = (f'<div class="sh-navy alerta"><div class="nh">Atenção — não programe ainda</div>'
              f'Com item a validar no contrato: <b>{e(" · ".join(a_validar))}</b>. O comercial fecha o '
              f'que está em aberto antes de qualquer corte.</div>') if a_validar else ''
    ths = ''.join(f'<th class="c">{c}</th>' for c in cols)
    out = []
    for i, pg in enumerate(pgs):
        pgtxt = f'folha {i+1}/{len(pgs)}' if len(pgs) > 1 else ''
        out.append(f'''<section class="sheet">
        {cab('Matriz de Conferência do Marceneiro', 'Uma linha por módulo · marque ao conferir', 'Conferência técnica na fábrica')}
        {ident(p)}{alerta}
        <div class="sh-sec"><span class="bar"></span><span class="tx">Módulos por ambiente
          <small>· as duas linhas em branco de cada ambiente são para a fábrica quebrar em mais módulos</small></span></div>
        <table><thead><tr><th style="width:15%">Ambiente</th>
          <th style="width:{28 - (3 if tem_led else 0)}%">Módulo / item</th>{ths}
          <th class="c" style="width:7%">Adesivo</th><th style="width:12%">Obs.</th></tr></thead>
          <tbody>{corpo_grupos(pg, cel)}</tbody></table>
        <div class="sh-sec"><span class="bar"></span><span class="tx">Liberação</span></div>
        <table><tbody><tr>
          <td style="width:34%"><span class="bx"></span> <b style="color:#2f7d4f">LIBERADO</b> — todos os módulos conferidos</td>
          <td style="width:34%"><span class="bx r"></span> <b style="color:#b0413f">RETIDO</b> — há módulo pendente</td>
          <td>Ambiente(s) liberado(s):</td></tr></tbody></table>
        <div class="sh-sign"><div>Marceneiro responsável · data</div><div>Conferido por · data</div></div>
        {rodape(p, 'MATRIZ DO MARCENEIRO', pgtxt)}</section>''')
    return ''.join(out)


# ── 4 · conferência de saída + insumos ────────────────────────────────────────
def folhas_saida(p):
    cols = ['Borda', 'Superf.', 'Tampa', 'Folgas', 'Limpeza', 'Embal.']
    ths = ''.join(f'<th class="c">{c}</th>' for c in cols)
    pgs = paginar([{'amb': a, 'linhas': linhas_do(a)} for a in p['ambientes']], MAX_LINHAS)
    out = []
    for i, pg in enumerate(pgs):
        pgtxt = f'folha {i+1}/{len(pgs)}' if len(pgs) > 1 else ''
        out.append(f'''<section class="sheet">
        {cab('Conferência de Saída', 'A última olhada antes de o móvel sair da fábrica', 'Acabamento e limpeza')}
        {ident(p)}
        <div class="sh-navy"><div class="nh">O que se confere aqui — e o que não</div>
          O técnico já foi conferido e corrigido na matriz do marceneiro. Aqui se olha
          <b>o que o cliente vai ver ao abrir a embalagem</b>. Não se discute execução — o que estiver
          errado volta para a coordenação com a pendência escrita.</div>
        <div class="sh-sec"><span class="bar"></span><span class="tx">Acabamento e limpeza, módulo a módulo</span></div>
        <table><thead><tr><th style="width:15%">Ambiente</th><th style="width:24%">Módulo / item</th>
          {ths}<th style="width:15%">Onde está o problema</th></tr></thead>
          <tbody>{corpo_grupos(pg, lambda a: caixa(len(cols)) + '<td></td>')}</tbody></table>
        <div class="sh-note"><b>O que cada coluna quer dizer:</b> borda colada em toda a volta, sem
        descolar nem queimado · superfície sem risco, mancha, cola ou marca de caneta · tampa em todas
        as dobradiças · folgas iguais dos dois lados e frentes no mesmo plano · sem pó, cola, fita crepe
        ou etiqueta esquecida · embalagem íntegra com cliente, ambiente e módulo escritos.</div>
        <div class="sh-sign"><div>Conferido por · data</div><div>Devolvido em · hora</div><div>Reconferido em</div></div>
        {rodape(p, 'CONFERÊNCIA DE SAÍDA', pgtxt)}</section>''')
    return ''.join(out) + folha_insumos(p)


BASE_INSUMOS = ['Dobradiças', 'Corrediças', 'Puxadores', 'Articulador / báscula', 'Suportes de prateleira',
                'Tapa-furo (cartela)', 'Parafusos e buchas', 'Pés / niveladores', 'Calafetador / silicone']
COND_INSUMOS = [('Perfil de LED', 'led'), ('Fita de LED + fonte', 'led'),
                ('Trilho e roldana do correr', 'correr'), ('Vidro / espelho embalado', 'vidro'),
                ('Peça de serralheria', 'serralheria')]


def folha_insumos(p):
    """Linha é o insumo, coluna é o ambiente. Só há caixa onde o insumo se aplica àquele ambiente."""
    linhas = [(n, lambda a: True) for n in BASE_INSUMOS]
    linhas += [(n, (lambda k: (lambda a: bool(a.get(k))))(k))
               for n, k in COND_INSUMOS if any(a.get(k) for a in p['ambientes'])]
    blocos = [p['ambientes'][i:i + MAX_COLS] for i in range(0, len(p['ambientes']), MAX_COLS)] or [[]]
    out = []
    for b, ambs in enumerate(blocos):
        ths = ''.join(f'<th class="c">{e(a["nome"])}</th>' for a in ambs)
        corpo = ''.join(
            f'<tr><td><b>{e(n)}</b></td>' +
            ''.join(caixa() if f(a) else '<td class="c" style="color:#b3aa96">—</td>' for a in ambs) + '</tr>'
            for n, f in linhas)
        corpo += (f'<tr><td class="sub">Outro:</td>{caixa(len(ambs))}</tr>') * 2
        pgtxt = f'folha {b+1}/{len(blocos)}' if len(blocos) > 1 else ''
        out.append(f'''<section class="sheet">
        {cab('Insumos e Kit por Ambiente', 'O que falta aqui vira obra parada lá', 'Separação da carga')}
        {ident(p)}
        <div class="sh-sec"><span class="bar"></span><span class="tx">Previsto e separado
          <small>· escreva a quantidade prevista e marque ao separar · traço = não se aplica</small></span></div>
        <table><thead><tr><th style="width:26%">Insumo</th>{ths}</tr></thead><tbody>{corpo}</tbody></table>
        <div class="sh-note"><b>A regra do kit:</b> cada item vai em saco etiquetado com o módulo a que
        pertence — não tudo num saco só. <b>Previsto</b> sai do projeto ou da lista de materiais.</div>
        <div class="sh-sec"><span class="bar"></span><span class="tx">Resultado</span></div>
        <table><tbody><tr>
          <td style="width:30%"><span class="bx"></span> <b style="color:#2f7d4f">LIBERADO</b> — pode carregar</td>
          <td style="width:30%"><span class="bx r"></span> <b style="color:#b0413f">RETIDO</b> — volta à coordenação</td>
          <td>Pendência:</td></tr></tbody></table>
        <div class="sh-sign"><div>Separado por · data</div><div>Conferido por · data</div></div>
        {rodape(p, 'INSUMOS E KIT', pgtxt)}</section>''')
    return ''.join(out)


# ── 5 · kit da obra ───────────────────────────────────────────────────────────
CATEGORIAS = [
    ('1 · Ferramentas manuais e de desgaste',
     ['Furadeira e parafusadeira (+ baterias e carregador)', 'Martelete', 'Tico-tico',
      'Lâminas de tico-tico novas', 'Plaina', 'Pinador', 'Serra copo', 'Brocas vídea',
      'Brocas aço rápido', 'Jogo de bits', 'Jogo de chaves', 'Jogo de chave allen',
      'Sargentos e grampos de aperto', 'Serrinha', 'Diversos (alicate, martelo, formão)',
      'Material de laminação (lima, espátula, estilete)', 'Metro (trena)', 'Nível a laser',
      'Nível de mão', 'Pilhas para o nível', 'Aspirador de pó', 'Escada']),
    ('2 · Material de limpeza',
     ['Thinner', 'Querosene', 'Limpa-vidro', 'Estopa', 'Pano', 'Pincel', 'Vassoura e pá', 'Saco de lixo']),
    ('3 · Material de acabamento',
     ['Cola branca / instantânea / contato', 'Silicone na cor + aplicador', 'Calafetador',
      'Caneta ou massa de retoque na cor', 'Fita de borda de reposição + ferro',
      'Tapa-furo na cor', 'Verniz / spray']),
    ('4 · Proteções', ['Cantoneira', 'Plástico bolha', 'Stretch / filme', 'Papelão', 'Fita crepe', 'EPI da equipe']),
]


def folha_ferramentas(p):
    def bloco(tit, itens):
        meio = -(-len(itens) // 2)
        linhas = []
        for i in range(meio):
            def cel(n):
                return (f'<td>{e(n)}</td>' if n else '<td></td>') + caixa(2)
            linhas.append('<tr>' + cel(itens[i]) + cel(itens[i + meio] if i + meio < len(itens) else '') + '</tr>')
        return (f'<div class="sh-sec"><span class="bar"></span><span class="tx">{e(tit)}</span></div>'
                f'<table><thead><tr><th>Item</th><th class="c" style="width:9%">Precisa</th>'
                f'<th class="c" style="width:9%">Separado</th><th>Item</th>'
                f'<th class="c" style="width:9%">Precisa</th><th class="c" style="width:9%">Separado</th>'
                f'</tr></thead><tbody>{"".join(linhas)}</tbody></table>')
    return f'''<section class="sheet">
    {cab('Checklist de Insumos e Ferramentas — Kit da Obra', 'Nada sai sem conferir · nada volta esquecido', 'Expedição e montagem')}
    {ident(p)}
    <div class="sh-note"><b>Precisa</b> se marca na preparação, na fábrica. <b>Separado</b> se marca na
    carga, com o item na mão. Os dois têm de estar marcados antes de o caminhão sair.</div>
    {''.join(bloco(t, i) for t, i in CATEGORIAS)}
    <div class="sh-sign"><div>Separado por · data</div><div>Conferido na carga · data</div><div>Devolvido completo em</div></div>
    {rodape(p, 'KIT DA OBRA')}</section>'''


# ── 6 · kit do montador ───────────────────────────────────────────────────────
def folhas_montador(p):
    def duas(pares):
        return ''.join(f'<tr>{caixa()}<td style="width:45%">{a}</td>{caixa()}<td>{b}</td></tr>'
                       for a, b in pares)
    linha = '<div class="sh-ln"></div>'

    entrada = f'''<section class="sheet">
    {cab('Relatório de Entrada e POP Pré-montagem', 'O que fazer antes de descarregar', 'Montagem em obra · 1 de 3')}
    {ident(p)}
    <div class="sh-sec"><span class="bar"></span><span class="tx">Antes de descarregar qualquer peça</span></div>
    <table><tbody>{"".join(f'<tr>{caixa()}<td>{t}</td></tr>' for t in [
        'Registrar <b>fotos e vídeos</b> do ambiente no estado inicial, antes de tudo',
        'Conferir <b>recebimento × romaneio</b> — nada faltou nem quebrou no transporte',
        'Alocar volumes com estratégia: ordem de montagem, sem obstruir passagem',
        '<b>Proteger</b> piso, paredes e móveis do cliente antes de trabalhar',
        'Conferir energia, ponto de luz e água disponíveis',
        'Registrar <b>danos prévios</b> — do ambiente e do transporte — com foto',
        'Confirmar acesso: o <b>maior módulo passa</b> até o ambiente'])}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Estado do ambiente encontrado
      <small>· marque tudo o que se aplica</small></span></div>
    <table><tbody>{duas([
        ('Ambiente pronto e limpo, apto a montar', 'Obra ainda em execução'),
        ('Sem energia ou sem água', 'Piso não nivelado ou não acabado'),
        ('Parede fora de esquadro ou prumo', 'Revestimento não concluído'),
        ('Medida divergente do projeto', 'Interferência não prevista'),
        ('Acesso bloqueado — módulo não passa', 'Sujeira ou entulho no ambiente'),
        ('Item de terceiros não chegou', 'Conflito de agenda com terceiros'),
        ('Ambiente ocupado — cliente morando', 'Clima afetando o içamento')])}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Registro de danos e ocorrências de entrada</span></div>
    <table><thead><tr><th style="width:22%">Item / local</th><th>Descrição</th>
      <th class="c" style="width:9%">Foto</th><th style="width:24%">Origem provável</th></tr></thead>
      <tbody>{('<tr><td></td><td></td>' + caixa() + '<td>transporte / fábrica / obra</td></tr>') * 8}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Autorização para iniciar</span></div>
    <table><tbody><tr><td style="width:28%"><span class="bx"></span> <b style="color:#2f7d4f">APTO</b> — iniciar</td>
      <td style="width:34%"><span class="bx"></span> <b>INICIAR COM RESSALVA</b> registrada acima</td>
      <td><span class="bx r"></span> <b style="color:#b0413f">NÃO INICIAR</b> — acionar a coordenação</td></tr></tbody></table>
    <div class="sh-sign"><div>Montador · data e hora</div><div>Coordenação · ciente</div></div>
    {rodape(p, 'ENTRADA E PRÉ-MONTAGEM')}</section>'''

    feito = ''.join(f'<tr><td><b>{e(a["nome"])}</b></td><td></td>'
                    f'<td>concluído / parcial / pendente</td><td></td></tr>' for a in p['ambientes'][:4])
    feito += '<tr><td></td><td></td><td>concluído / parcial / pendente</td><td></td></tr>' * 6
    diario = f'''<section class="sheet">
    {cab('Relatório Diário de Montagem', 'O que foi feito · o que deu errado · o que sugere', 'Montagem em obra · 2 de 3 · imprimir 1 por dia')}
    {ident(p, '<div><b>Dia nº:</b> <span class="v">____</span> &nbsp; <b>Data:</b> ___/___</div>')}
    <div class="sh-sec"><span class="bar"></span><span class="tx">O que foi feito hoje</span></div>
    <table><thead><tr><th style="width:22%">Ambiente</th><th style="width:26%">Módulo</th>
      <th style="width:26%">Situação</th><th>Observação</th></tr></thead><tbody>{feito}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Erros de fabricação encontrados</span></div>
    <table><thead><tr><th style="width:28%">Peça / módulo</th><th>Erro</th>
      <th style="width:18%">Ação</th><th class="c" style="width:14%">Fábrica avisada</th></tr></thead>
      <tbody>{('<tr><td></td><td></td><td>ajusta / refaz</td>' + caixa() + '</tr>') * 5}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Avarias, ocorrências de cliente e de terceiros</span></div>
    <table><thead><tr><th style="width:22%">Tipo</th><th>Descrição</th><th style="width:24%">Providência</th>
      <th class="c" style="width:9%">Foto</th></tr></thead>
      <tbody>{('<tr><td>transporte / fábrica / cliente / terceiro</td><td></td><td></td>' + caixa() + '</tr>') * 5}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Sugestões de melhoria</span></div>
    <div>{linha * 3}</div>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Pendências e material que falta para amanhã</span></div>
    <div>{linha * 3}</div>
    <div class="sh-sign"><div>Montador responsável</div><div>Recebido pela coordenação · data</div></div>
    {rodape(p, 'RELATÓRIO DIÁRIO')}</section>'''

    vistoria = f'''<section class="sheet">
    {cab('Relatório Final — Vistoria Minuciosa', 'Confira tudo antes de dar a montagem por concluída', 'Montagem em obra · 3 de 3')}
    {ident(p)}
    <div class="sh-sec"><span class="bar"></span><span class="tx">Estrutura e funcionamento</span></div>
    <table><tbody>{duas([
        ('<b>Fixação e resistência</b>: móvel firme, bucha e parafuso corretos', '<b>Nivelamento e prumo</b>: pé regulável ajustado'),
        ('<b>Alinhamento</b> de portas e gavetas, folgas uniformes', 'Regulagem de dobradiça, corrediça e soft-close'),
        ('Tudo <b>funciona</b>: abre, fecha, gaveta corre, correr desliza', 'Iluminação testada — LED e sensor'),
        ('Tampo e bancada instalados, vedados e sem folga', 'Recortes de tomada, cuba e cooktop corretos')])}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Acabamento e finalização</span></div>
    <table><tbody>{duas([
        ('Superfície sem risco, mancha ou cola; borda íntegra', '<b>Marcas de caneta e lápis</b> removidas'),
        ('<b>Tampinhas de parafuso e de minifix</b> colocadas', '<b>Acabamento das dobradiças</b>: tampa colocada e alinhada'),
        ('Arremates de perfil, rodapé e acabamento concluídos', 'Silicone e vedação onde previsto, sem excesso'),
        ('Puxadores e ferragens finais instalados', '<b>Limpeza interna</b> — dentro de armários e gavetas'),
        ('Limpeza externa do móvel', 'Ambiente limpo; embalagem e entulho recolhidos'),
        ('<b>Foto final</b> de cada ambiente registrada', 'Cliente orientado sobre uso e conservação')])}</tbody></table>
    <div class="sh-sec"><span class="bar"></span><span class="tx">Pendências que ficaram</span></div>
    <table><thead><tr><th>Pendência</th><th style="width:20%">Resolver quando</th>
      <th style="width:18%">Responsável</th></tr></thead>
      <tbody>{'<tr><td></td><td></td><td></td></tr>' * 6}</tbody></table>
    <div class="sh-sign"><div>Montador responsável · data</div><div>Coordenação · ciente</div></div>
    {rodape(p, 'VISTORIA FINAL')}</section>'''
    return entrada + diario + vistoria


# ── 7 · conferência final da direção ──────────────────────────────────────────
ITENS_FINAL = [
    ('<b>Impressão de conjunto</b> — parece caro? é isto que vendemos?', 1),
    ('Alinhamento geral e <b>folgas uniformes</b> vistas de frente', 0),
    ('Frentes no mesmo plano; sem barriga e sem desnível', 0),
    ('<b>Acabamento e arremate</b> — friso, canto, encontro com parede', 1),
    ('Borda íntegra; superfície sem risco, mancha ou marca', 0),
    ('Tapa-furo e tampa de dobradiça colocados, na cor certa', 0),
    ('Portas, gavetas e correr: funcionam macios e sem ruído', 0),
    ('Puxadores e ferragens finais — alinhados e firmes', 0),
    ('<b>Iluminação</b> — LED aceso, perfil reto, emenda e cor uniformes', 1),
    ('Tampo, cuba e recortes: alinhados, vedados, sem folga', 0),
    ('Silicone e vedação limpos, sem excesso', 0),
    ('Encontro com a obra — piso, parede, teto, rodapé', 0),
    ('Interior limpo; gavetas e prateleiras sem pó ou cola', 0),
    ('Ambiente do cliente entregue limpo, sem entulho', 0),
    ('<b>Detalhe que o cliente vai notar</b> antes de nós', 1),
]


def folhas_final(p):
    blocos = [p['ambientes'][i:i + MAX_COLS] for i in range(0, max(len(p['ambientes']), 1), MAX_COLS)] or [[]]
    out = []
    for b, ambs in enumerate(blocos):
        larg = 69 // max(len(ambs), 1)
        ths = ''.join(f'<th class="c" style="width:{larg}%">{e(a["nome"])}</th>' for a in ambs)
        corpo = ''.join(f'<tr class="{"hot" if hot else ""}"><td>{t}</td>{vazias(len(ambs))}</tr>'
                        for t, hot in ITENS_FINAL)
        pend = ''.join(f'<tr><td class="c">{i+1}</td><td></td><td></td><td></td><td></td>{caixa()}</tr>'
                       for i in range(8))
        pgtxt = f'folha {b+1}/{len(blocos)}' if len(blocos) > 1 else ''
        out.append(f'''<section class="sheet">
        {cab('Conferência Final de Obra — Direção', 'Os móveis, ambiente por ambiente', 'Conferência da direção')}
        {ident(p, '<div><b>Conferida em:</b> <span class="v">___/___/____</span></div>')}
        <div class="sh-navy"><div class="nh">O que esta conferência é</div>
          A vistoria técnica já foi feita pelo montador e a conferência de saída pela fábrica.
          <b>Esta não repete nenhuma das duas</b> — se repetir, quem faz antes para de fazer. Aqui se
          valida o <b>padrão que a Valvic promete</b>: percorra o ambiente como o cliente percorreria.</div>
        <div class="sh-sec"><span class="bar"></span><span class="tx">Itens × ambientes
          <small>· ✓ conforme · nº da pendência quando não</small></span></div>
        <table><thead><tr><th style="width:31%">Item a validar</th>{ths}</tr></thead>
          <tbody>{corpo}</tbody></table>
        <div class="sh-sec"><span class="bar"></span><span class="tx">Pendências</span></div>
        <table><thead><tr><th class="c" style="width:6%">Nº</th><th style="width:17%">Ambiente</th>
          <th>O que está fora do padrão</th><th style="width:16%">Quem resolve</th>
          <th style="width:12%">Até quando</th><th class="c" style="width:11%">Resolvido</th></tr></thead>
          <tbody>{pend}</tbody></table>
        <div class="sh-sign"><div>Direção · data</div><div>Coordenação de produção · ciente</div></div>
        {rodape(p, 'CONFERÊNCIA FINAL', pgtxt)}</section>''')
    return ''.join(out)


CHECKLISTS = [
    ('escopo', folha_escopo), ('medicao', folha_medicao), ('matriz', folhas_matriz),
    ('saida', folhas_saida), ('ferramentas', folha_ferramentas),
    ('montador', folhas_montador), ('final', folhas_final),
]


def montar(p, quais=None):
    quais = quais or [k for k, _ in CHECKLISTS]
    corpo = ''.join(fn(p) for k, fn in CHECKLISTS if k in quais)
    fontes = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700"
              "&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap")
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            f'<title>Abertura de produção — {e(p.get("cliente"))} · OP {e(p.get("op"))}</title>'
            f'<link rel="preconnect" href="https://fonts.googleapis.com">'
            f'<link href="{fontes}" rel="stylesheet"><style>@page{{size:A4 portrait;margin:0}}'
            f'body{{margin:0;background:#8a8f96;font-family:\'Inter\',system-ui,sans-serif}}'
            f'@media print{{body{{background:#fff}}.sheet{{box-shadow:none;margin:0}}}}'
            f'{CSS}</style></head><body>{corpo}</body></html>')


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    p = preparar(json.load(open(sys.argv[1], encoding='utf-8')))
    if not p.get('cliente') or not p.get('op'):
        raise SystemExit('faltam "cliente" e/ou "op" no JSON — sem eles as folhas saem sem cabeçalho')
    destino = sys.argv[2] if len(sys.argv) > 2 else None
    base = destino[:-4] if destino and destino.endswith('.pdf') else \
        os.path.join(os.getcwd(), 'Valvic_Abertura_' + re.sub(r'[^A-Za-z0-9]', '_', p['op']))
    html_path, pdf_path = base + '.html', base + '.pdf'
    open(html_path, 'w', encoding='utf-8').write(montar(p, p.get('checklists')))

    gerar = os.path.join(AQUI, '..', '..', '.claude', 'skills',
                         'alice-assistente-operacional', 'ferramentas', 'gerar-pdf.py')
    r = subprocess.run([sys.executable, os.path.abspath(gerar), html_path, pdf_path],
                       capture_output=True, text=True)
    print(r.stdout or r.stderr)
    print(f'HTML: {html_path}')


if __name__ == '__main__':
    main()
