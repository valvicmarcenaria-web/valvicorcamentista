# -*- coding: utf-8 -*-
"""Lista TODA peça que o motor conta como prateleira, e por quê.

⭐ Existe porque o motor conta pelo NOME, e o nome mente: um painel
   chamado "painel das prateleiras" não é prateleira, uma horizontal fixa
   cavilhada não se apoia em suporte, e a segunda camada de uma prateleira
   duplada é a MESMA prateleira. Cada linha aqui é uma peça para olhar no
   olho antes de deixar o suporte e a alma entrarem na conta.
"""
import sys, json, importlib.util, pathlib, io, contextlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import base as B

ABAS = ['living', 'cozinha', 'lavanderia', 'quarto', 'areagourmet',
        'banhogourmet', 'homeoffice', 'suitehospedes', 'banhohospedes',
        'salacinema', 'suitemaster', 'closetmaster', 'banhomaster',
        'suitemariana', 'closetmariana', 'banhomariana', 'suite03',
        'closet03', 'banho03']

for nome in ABAS:
    spec = importlib.util.spec_from_file_location(nome, f'{nome}.py')
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    print(f'═══ {nome}')
    for p in getattr(mod, nome.upper()):
        n = p['nome'].lower()
        if not any(w in n for w in ('prateleira', 'sapateira', 'maleiro')):
            continue
        if 'moldura' in n:
            continue
        o = p['obs'].lower()
        sup = 'sem suporte' not in o
        alma = ('sem alma' not in o and 'prateleira' in n
                and max(p['c'], p['l']) > B.ALMA_VAO)
        marca = ('SUP' if sup else '   ') + ' ' + ('ALMA' if alma else '    ')
        if not sup and not alma:
            marca = 'isenta   '
        print(f'  {marca} {p["qtd"]}× {p["c"]:>6}×{p["l"]:<5} {p["nome"][:58]}')
