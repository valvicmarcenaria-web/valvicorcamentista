/**
 * Valvic Marcenaria · atualização de estrutura, feita de dentro do Drive
 *
 * Onde colar: na planilha CUSTO POR PROJETO.
 *   Extensões → Apps Script → cole este arquivo → salve → Executar `atualizarTudo`.
 *   Na primeira vez o Google pede autorização: ele mexe em outras planilhas.
 *
 * O que faz, sem você subir arquivo nenhum:
 *
 *   1. amplia a Base · Comissões de 22 para 27 colunas, trazendo os percentuais
 *      de custo de venda do bloco 2 de cada ficha;
 *   2. reescreve a aba Comissões das catorze planilhas individuais, cada uma no
 *      formato da sua função.
 *
 * O que cada um passa a ver:
 *
 *   PROJETISTA      a conta inteira — venda, imposto, taxa, RT, comissão do
 *   Lorrane         vendedor, custos, líquido e a comissão. É sobre o líquido
 *   Lucas, Bruna    que o percentual dela incide, e ela precisa poder conferir.
 *
 *   COORDENAÇÃO     produção, montagem e coordenação. Sem valor de venda e sem
 *   Deivison        receita: a coordenação é dele, o faturamento do cliente não.
 *
 *   OPERAÇÃO        produção e montagem. Nada de venda, receita ou coordenação.
 *   os dez          O que ele fez e o que tem a receber.
 *
 * O que foi digitado à mão — data combinada, status, nota fiscal e observação —
 * é lido antes, casado pelo NOME DO PROJETO e devolvido depois. Casar por nome e
 * não por posição é o que permite as colunas mudarem de lugar sem embaralhar.
 */

const ID_CUSTO = '1tTJXG4w7lDvIcnd0dyr219-leOPwuURqrBk6lJIr18I';

// ── as catorze, com o perfil de cada uma ────────────────────────────────
// perfil: 'projetista' · 'coordenacao' · 'operacao'
const PESSOAS = [
  { nome: 'Lorrane',  perfil: 'projetista',  pj: true,  id: '1VamDp_gzbRMMuWYSSrJoxjhfUDfMbJDjyVnGOliO2x0' },
  { nome: 'Lucas',    perfil: 'projetista',  pj: false, id: '18O6qW0T0JrFtvyhcSM_QPrNoQgNQg1XVCtBn1WDLAzI' },
  { nome: 'Bruna',    perfil: 'projetista',  pj: true,  id: '1kIvZ5chhDav8t7R_xh1c03ctqGXs2ZDc17WD8BglFk0' },
  { nome: 'Deivison', perfil: 'coordenacao', pj: true,  id: '1QLcbZFBHPVtpJ7tlEZ-h9uA1JF5dWeRUspIWDw1LYRQ' },
  { nome: 'Ronald',   perfil: 'operacao',    pj: true,  id: '1ZQ_WSDSj1PYYIDLx6UxIQ2wZbqdkS9wNYjPnFNrHWw0' },
  { nome: 'Samuel',   perfil: 'operacao',    pj: true,  id: '1V5V3_yyABqnZKhvFRbR6XKBvZXLxQ9nFVnDqcgYeBM4' },
  { nome: 'Cesar',    perfil: 'operacao',    pj: true,  id: '1ZoFwZUoTvAeGvyg4qA5VSIRYHJW8v9e7wQPiymqCF5g' },
  { nome: 'Jhon',     perfil: 'operacao',    pj: true,  id: '1ls1NBCTWt6KbUovDEKmEqFohP78Od7IoZ559hIG-fHA' },
  { nome: 'Joelson',  perfil: 'operacao',    pj: true,  id: '1dTsPZLSbwF7LKC9vIRkIR3X4TQ7UT3JjIG4J7TBGtjY' },
  { nome: 'Davi',     perfil: 'operacao',    pj: false, id: '1bVIOGUkllLb-Gv09O7MPBFfSkfU2YMkHp2OC8AsGMxc' },
  { nome: 'Jomar',    perfil: 'operacao',    pj: false, id: '1zPnwSruRLICptaaWrSL3LSkFpCLCEhneiC4wobg9u6Q' },
  { nome: 'Bruno',    perfil: 'operacao',    pj: false, id: '1myxNnqgAxdKITzoEgG_Q337fABd0EI-If7XURff3bIc' },
  { nome: 'Wallace',  perfil: 'operacao',    pj: false, id: '1kzUbOo1ZpcPKtJruh4KBsFmAFa8lyKzvlc1fnqmzVz8' },
  { nome: 'Douglas',  perfil: 'operacao',    pj: false, id: '1igVyI7G-YJ6cZ7cX8yxr-8jfpd60YUQ8Jmyaw2mlsyA' },
];

// ── mapa da ficha ───────────────────────────────────────────────────────
const FICHA = {
  painel: 'Painel Geral', base: 'Base · Comissões',
  pg0: 11, pgf: 50,
  amb0: 49, ambQtd: 12, base0: 2,
  entrada: 'F7', coordenador: 'F9', venda: 'A13',
  imposto: 'B38', maquina: 'B39', vendedor: 'B41', rt: 'B43',
  custoVenda: 'D44', liquido: 'D45', comCoord: 'D65',
  colsBase: 27,
};
const COLS_AMB = 'ABCDEFGHIJKLMNO'.split('');

// colunas da Base, por nome — usadas nas fórmulas das individuais
const B = {
  projeto: 'A', valor: 'E',
  prodQuem: 'F', prodCom: 'H', montQuem: 'J', montCom: 'L',
  projQuem: 'N', projCom: 'P', coordQuem: 'S', coordCom: 'T',
  liquido: 'U', venda: 'V',
  imposto: 'W', maquina: 'X', rt: 'Y', vendedor: 'Z', custoVenda: 'AA',
};
const BASE_FIM = 482;
const N_PROJ = 40, LIN0 = 4;

/**
 * O separador de argumentos das fórmulas.
 *
 * Numa planilha em português o Google espera ponto e vírgula — SOMA(A1;B1) —
 * e em inglês espera vírgula. O Apps Script grava o texto que a gente manda,
 * sem traduzir. Foi por isso que a Base inteira virou #ERROR!: escrevemos
 * vírgula numa planilha pt_BR.
 *
 * Em vez de chutar, calibrar_() faz um teste: escreve =SUM(1,2) numa aba
 * temporária e vê se o resultado é 3. Se não for, a planilha usa ponto e
 * vírgula. A aba temporária é apagada em seguida, dê certo ou dê errado.
 */
let SEP = ',';

function calibrar_(ss) {
  const tmp = ss.insertSheet('__teste_separador__');
  try {
    tmp.getRange(1, 1).setFormula('=SUM(1,2)');
    SpreadsheetApp.flush();
    SEP = (tmp.getRange(1, 1).getValue() === 3) ? ',' : ';';
  } catch (e) {
    SEP = ';';
  } finally {
    ss.deleteSheet(tmp);
  }
  return SEP;
}

/** Troca as vírgulas separadoras pelo que a planilha entende, poupando o que
 *  estiver dentro de aspas — "Pago" não pode virar "Pago;". */
function fx_(f) {
  if (SEP === ',' || typeof f !== 'string' || f.charAt(0) !== '=') return f;
  let fora = true, out = '';
  for (let i = 0; i < f.length; i++) {
    const c = f.charAt(i);
    if (c === '"') fora = !fora;
    out += (c === ',' && fora) ? SEP : c;
  }
  return out;
}

/** setFormula e setFormulas passando pelo tradutor. */
function posF_(rg, f) { return rg.setFormula(fx_(f)); }
function posFs_(rg, m) {
  return rg.setFormulas(m.map(function (lin) { return lin.map(fx_); }));
}


const NAVY = '#0e2038', NAVY2 = '#16314f', GOLDS = '#d8bd80';
const CALC = '#eaf1f8', ZEBRA = '#f7f5ef', OKBG = '#e6f0e9', ABERTOBG = '#faefdc';
const MOEDA = 'R$ #,##0.00', PCT = '0.0%', DATA = 'dd/mm/yyyy';


/**
 * SÓ LÊ. Não escreve nada, não apaga nada, não altera uma célula sequer.
 *
 * Mostra no Registro de execução o que está de fato dentro das células do
 * Samuel: a fórmula escrita e o que o Google devolveu. É assim que se acha a
 * origem de um #ERROR! — olhando a célula de origem, não a que exibe o erro.
 */
function diagnostico() {
  const NOME = 'Samuel';
  let p = null;
  PESSOAS.forEach(function (x) { if (x.nome === NOME) p = x; });
  if (!p) { console.log('Não existe ' + NOME + ' na lista.'); return; }

  const ss = SpreadsheetApp.openById(p.id);
  console.log('abas: ' + ss.getSheets().map(function (s) { return s.getName(); }).join(' | '));
  console.log('locale: ' + ss.getSpreadsheetLocale());

  const mostra = function (aba, refs) {
    const sh = ss.getSheetByName(aba);
    if (!sh) { console.log(aba + ': NÃO EXISTE'); return; }
    refs.forEach(function (ref) {
      const c = sh.getRange(ref);
      console.log(aba + '!' + ref
        + '\n     fórmula: ' + (c.getFormula() || '(sem fórmula)')
        + '\n     mostra : ' + c.getDisplayValue());
    });
  };

  mostra('_base', ['A1', 'A2', 'B2', 'F2', 'H2']);
  mostra('Comissões', ['A3', 'C3', 'D3', 'E3', 'A4', 'C4', 'D4', 'E4']);
  mostra('Painel', ['C7', 'C14']);
}


/**
 * UMA SÓ, para testar antes de mexer nas catorze.
 *
 * Rode esta primeiro: escolha "testarUma" no seletor de função, ao lado do
 * botão Executar. Ela mexe só na planilha do Samuel e não toca na Base nem
 * no Painel Geral. Se o log disser "ok", aí sim rode atualizarTudo.
 */
function testarUma() {
  const NOME = 'Samuel';          // troque aqui para testar com outra pessoa
  let achou = null;
  PESSOAS.forEach(function (p) { if (p.nome === NOME) achou = p; });
  if (!achou) { console.log('Não existe ' + NOME + ' na lista PESSOAS.'); return; }
  try {
    const n = atualizarIndividual_(achou);
    console.log(NOME + ': ok' + (n ? '  ·  ' + n + ' linha(s) preservada(s)' : ''));
  } catch (e) {
    console.log(NOME + ': FALHOU — ' + e.message);
  }
}


/**
 * O relatório sai no "Registro de execução", embaixo do editor — não numa
 * janela. Janela de confirmação só existe em script preso a uma planilha, e
 * este precisa rodar preso ou solto, tanto faz.
 */
function atualizarTudo() {
  const log = [];
  const diz = function (t) { log.push(t); console.log(t); };

  diz('── começando ──');
  try {
    diz('Painel Geral: ' + repararPainelGeral_() + ' projeto(s) registrado(s)');
    diz('Base · Comissões: ' + atualizarBase_() + ' projeto(s), 27 colunas');
  } catch (e) {
    diz('Base · Comissões: FALHOU — ' + e.message);
    diz('As individuais não foram tocadas: sem a Base nova elas não teriam de onde ler.');
    return log.join('\n');
  }

  let ok = 0, erro = 0;
  PESSOAS.forEach(function (p) {
    try {
      const n = atualizarIndividual_(p);
      ok++;
      diz(p.nome + ': ok' + (n ? '  ·  ' + n + ' linha(s) preenchida(s) preservada(s)' : ''));
    } catch (e) {
      erro++;
      diz(p.nome + ': FALHOU — ' + e.message);
    }
  });

  diz('── fim: ' + ok + ' atualizada(s)' + (erro ? ', ' + erro + ' com erro' : '') + ' ──');
  return log.join('\n');
}


// ════════════════════════════════════════════════════════════════════════
//  Base · Comissões
// ════════════════════════════════════════════════════════════════════════

/**
 * Reescreve a lista de projetos do Painel Geral a partir das abas que existem
 * de verdade, na ordem em que estão na planilha.
 *
 * Existe porque uma versão anterior deste script apagava o registro quando não
 * achava a aba — e não achava porque dez abas têm espaço no fim do nome
 * ('Ana Carolina ') e o código aplicava trim antes de procurar. Dez registros
 * foram perdidos. Reconstruir a partir das abas é mais seguro do que confiar no
 * que sobrou: a verdade é a aba existir, não o nome estar escrito ali.
 */
function repararPainelGeral_() {
  const ss = SpreadsheetApp.openById(ID_CUSTO);
  const pg = ss.getSheetByName(FICHA.painel);
  const FIXAS = ['Instruções', FICHA.painel, 'Ficha Modelo', 'Listas', FICHA.base];
  const abas = ss.getSheets().map(function (sh) { return sh.getName(); })
                 .filter(function (n) { return FIXAS.indexOf(n) < 0; });

  const n = FICHA.pgf - FICHA.pg0 + 1;
  const vals = [];
  for (let i = 0; i < n; i++) vals.push([i < abas.length ? abas[i] : '']);
  pg.getRange(FICHA.pg0, 2, n, 1).setValues(vals);
  SpreadsheetApp.flush();
  return abas.length;
}


function atualizarBase_() {
  const ss = SpreadsheetApp.openById(ID_CUSTO);
  console.log('  separador desta planilha: "' + calibrar_(ss) + '"');
  const pg = ss.getSheetByName(FICHA.painel);
  const base = ss.getSheetByName(FICHA.base);

  const CAB = ['Projeto', 'Cliente', 'Ambiente', '% do total', 'Valor do ambiente',
    'Produção — quem', '% produção', 'Comissão produção', 'Fabricado em',
    'Montagem — quem', '% montagem', 'Comissão montagem', 'Montado em',
    'Projetista — quem', '% projeto', 'Comissão projetista', 'Total do ambiente',
    'Data de entrada', 'Coordenador', 'Comissão coordenação',
    'Receita líquida do projeto', 'Valor de venda',
    'Imposto %', 'Taxa de máquina %', 'RT %', 'Comissão do vendedor %',
    'Custos de venda'];

  base.clear();
  base.getRange(1, 1, 1, CAB.length).setValues([CAB])
      .setBackground(NAVY2).setFontColor('#ffffff').setFontSize(8.5)
      .setFontWeight('bold').setWrap(true).setHorizontalAlignment('center');
  base.setFrozenRows(1);

  // SEM trim: dez abas têm espaço no fim do nome, e getSheetByName é literal.
  // E sem apagar nada do Painel Geral: se o nome não casar, apenas se registra
  // no log. Apagar registro foi o que destruiu a lista na primeira tentativa.
  const nomes = pg.getRange(FICHA.pg0, 2, FICHA.pgf - FICHA.pg0 + 1, 1).getValues();
  let n = 0;
  for (let i = 0; i < nomes.length; i++) {
    const nome = String(nomes[i][0] || '');
    if (!nome) continue;
    if (!ss.getSheetByName(nome)) {
      console.log('  aviso: linha ' + (FICHA.pg0 + i) + ' do Painel Geral diz "'
                  + nome + '" e não há aba com esse nome. Nada foi apagado.');
      continue;
    }
    escreverBlocoBase_(base, i, nome);
    n++;
  }
  SpreadsheetApp.flush();
  return n;
}

function ref_(nome) { return "'" + String(nome).replace(/'/g, "''") + "'"; }

/** Célula do projeto trazida para a base, com endereço absoluto. */
function cel_(ab, end, r, texto) {
  const abs = '$' + end.charAt(0) + '$' + end.slice(1);
  return '=IF($C' + r + '="","",IF(' + ab + '!' + abs + '="",' + (texto ? '""' : '0')
       + ',' + ab + '!' + abs + '))';
}

function escreverBlocoBase_(base, i, nomeAba) {
  const r0 = FICHA.base0 + i * FICHA.ambQtd;
  const pgL = FICHA.pg0 + i;
  const ab = ref_(nomeAba);
  const linhas = [];
  for (let j = 0; j < FICHA.ambQtd; j++) {
    const r = r0 + j, fr = FICHA.amb0 + j;
    const L = [
      '=IF($C' + r + '="","",\'' + FICHA.painel + '\'!$B$' + pgL + ')',
      '=IF($C' + r + '="","",\'' + FICHA.painel + '\'!$C$' + pgL + ')',
    ];
    COLS_AMB.forEach(function (c) {
      L.push('=IF(' + ab + '!$' + c + '$' + fr + '="","",' + ab + '!$' + c + '$' + fr + ')');
    });
    L.push(cel_(ab, FICHA.entrada, r, true));
    // projeto inteiro: só na primeira linha, senão o SUMIFS multiplica por doze
    if (j === 0) {
      L.push(cel_(ab, FICHA.coordenador, r, true));
      L.push(cel_(ab, FICHA.comCoord, r, false));
      L.push(cel_(ab, FICHA.liquido, r, false));
      L.push(cel_(ab, FICHA.venda, r, false));
      L.push(cel_(ab, FICHA.imposto, r, false));
      L.push(cel_(ab, FICHA.maquina, r, false));
      L.push(cel_(ab, FICHA.rt, r, false));
      L.push(cel_(ab, FICHA.vendedor, r, false));
      L.push(cel_(ab, FICHA.custoVenda, r, false));
    } else {
      L.push('', '', '', '', '', '', '', '', '');
    }
    linhas.push(L);
  }
  posFs_(base.getRange(r0, 1, FICHA.ambQtd, FICHA.colsBase), linhas);
}


// ════════════════════════════════════════════════════════════════════════
//  planilhas individuais
// ════════════════════════════════════════════════════════════════════════

/** As colunas da aba Comissões, conforme o perfil. */
function layout_(p) {
  const soma = function (vcol, qcol) {
    return function (r) {
      return '=IF($A' + r + '="","",ROUND(SUMIFS(_base!$' + B[vcol] + '$2:$' + B[vcol] + '$'
        + BASE_FIM + ',_base!$' + B.projeto + '$2:$' + B.projeto + '$' + BASE_FIM
        + ',$A' + r + ',_base!$' + B[qcol] + '$2:$' + B[qcol] + '$' + BASE_FIM
        + ',"' + p.nome + '"),2))';
    };
  };
  const doProjeto = function (col, moeda) {
    return function (r) {
      const lb = 2 + (r - LIN0) * FICHA.ambQtd;
      return '=IF($A' + r + '="","",IFERROR(_base!$' + B[col] + '$' + lb + ',""))';
    };
  };

  // Participação do projetista no projeto: quanto dos ambientes, em R$, leva o
  // nome dele, dividido pelo valor de todos os ambientes daquele projeto.
  //
  // Por que medir por valor e não por quantidade de ambientes: uma cozinha de
  // 30 mil e um lavabo de 4 mil contam igual se a gente contar peças. Em
  // dinheiro, cada um pesa o que pesa.
  //
  // A conta se normaliza sozinha — se os ambientes não somarem exatamente o
  // valor de venda, a proporção continua correta, porque o denominador é a
  // soma dos ambientes lançados, não o valor de venda.
  const COL_PART = 'C';   // a coluna Participação é a terceira no layout abaixo
  const participacao = function (r) {
    const fx = '_base!$' + B.projeto + '$2:$' + B.projeto + '$' + BASE_FIM;
    const fv = '_base!$' + B.valor + '$2:$' + B.valor + '$' + BASE_FIM;
    const fq = '_base!$' + B.projQuem + '$2:$' + B.projQuem + '$' + BASE_FIM;
    return '=IF($A' + r + '="","",IFERROR('
      + 'SUMIFS(' + fv + ',' + fx + ',$A' + r + ',' + fq + ',"' + p.nome + '")'
      + '/SUMIFS(' + fv + ',' + fx + ',$A' + r + '),0))';
  };

  // Valor do projeto reduzido à fatia dele.
  const fatia = function (col) {
    return function (r) {
      const lb = 2 + (r - LIN0) * FICHA.ambQtd;
      return '=IF($A' + r + '="","",ROUND(IFERROR(_base!$' + B[col] + '$' + lb
        + ',0)*$' + COL_PART + r + ',2))';
    };
  };

  let cols = [
    { t: 'Projeto', w: 24, calc: true, f: function (r) {
        const lb = 2 + (r - LIN0) * FICHA.ambQtd;
        return '=IFERROR(IF(_base!$A$' + lb + '="","",_base!$A$' + lb + '),"")'; } },
    { t: 'Cliente', w: 22, calc: true, f: function (r) {
        const lb = 2 + (r - LIN0) * FICHA.ambQtd;
        return '=IFERROR(IF(_base!$B$' + lb + '="","",_base!$B$' + lb + '),"")'; } },
  ];

  if (p.perfil === 'projetista') {
    cols = cols.concat([
      { t: 'Participação', w: 11, calc: true, nf: PCT, f: participacao },
      { t: 'Valor de venda · sua parte', w: 15, calc: true, nf: MOEDA, f: fatia('venda') },
      { t: 'Imposto %', w: 10, calc: true, nf: PCT, f: doProjeto('imposto') },
      { t: 'Taxa de máquina %', w: 11, calc: true, nf: PCT, f: doProjeto('maquina') },
      { t: 'RT %', w: 9, calc: true, nf: PCT, f: doProjeto('rt') },
      { t: 'Comissão do vendedor %', w: 11, calc: true, nf: PCT, f: doProjeto('vendedor') },
      { t: 'Custos de venda · sua parte', w: 15, calc: true, nf: MOEDA, f: fatia('custoVenda') },
      { t: 'Receita líquida · sua parte', w: 15, calc: true, nf: MOEDA, f: fatia('liquido') },
      { t: 'Comissão a receber', w: 15, calc: true, nf: MOEDA, total: true,
        f: soma('projCom', 'projQuem') },
    ]);
  } else if (p.perfil === 'coordenacao') {
    cols = cols.concat([
      { t: 'Produção', w: 13, calc: true, nf: MOEDA, f: soma('prodCom', 'prodQuem') },
      { t: 'Montagem', w: 13, calc: true, nf: MOEDA, f: soma('montCom', 'montQuem') },
      { t: 'Coordenação', w: 13, calc: true, nf: MOEDA, f: soma('coordCom', 'coordQuem') },
      { t: 'Total a receber', w: 15, calc: true, nf: MOEDA, total: true, f: function (r) {
          return '=IF($A' + r + '="","",ROUND(SUM($C' + r + ':$E' + r + '),2))'; } },
    ]);
  } else {
    cols = cols.concat([
      { t: 'Produção', w: 14, calc: true, nf: MOEDA, f: soma('prodCom', 'prodQuem') },
      { t: 'Montagem', w: 14, calc: true, nf: MOEDA, f: soma('montCom', 'montQuem') },
      { t: 'Total a receber', w: 15, calc: true, nf: MOEDA, total: true, f: function (r) {
          return '=IF($A' + r + '="","",ROUND(SUM($C' + r + ':$D' + r + '),2))'; } },
    ]);
  }

  cols.push({ t: 'Pagamento combinado', w: 15, manual: 'pagamento', nf: DATA });
  cols.push({ t: 'Status', w: 12, manual: 'status' });
  if (p.pj) cols.push({ t: 'Repassado em NF', w: 14, manual: 'nf' });
  cols.push({ t: 'Observação', w: 26, manual: 'obs' });
  return cols;
}


function atualizarIndividual_(p) {
  const ss = SpreadsheetApp.openById(p.id);
  calibrar_(ss);
  const sh = ss.getSheetByName('Comissões');
  if (!sh) throw new Error('aba Comissões não encontrada');

  // O _base foi criado quando a Base tinha 22 colunas (até V). Agora tem 27
  // (até AA), e sem alargar o IMPORTRANGE as colunas de imposto, máquina, RT,
  // vendedor e custos de venda chegam vazias nas planilhas dos projetistas.
  // Só o trecho do intervalo é trocado: o resto da fórmula fica como está,
  // inclusive o separador que ela já usa e a autorização já concedida.
  const bs = ss.getSheetByName('_base');
  if (bs) {
    const atual = bs.getRange('A1').getFormula();
    const nova = atual.replace(/!A1:[A-Z]+\d+/, '!A1:AA' + BASE_FIM);
    if (nova && nova !== atual) bs.getRange('A1').setFormula(nova);
  }

  // 1 · guarda o que foi digitado, casado pelo nome do projeto
  // A aba pode estar VAZIA: uma versão anterior deste script dava clear() e só
  // depois quebrava na mesclagem, deixando as catorze abas em branco. Numa aba
  // vazia getLastColumn() devolve 0 e o getRange abaixo estoura. Então se não
  // há cabeçalho, não há o que guardar — segue direto para a reconstrução.
  const guardado = {};
  let nGuardado = 0;
  const nCab = sh.getLastColumn();
  const cab = nCab >= 1 ? sh.getRange(3, 1, 1, nCab).getValues()[0] : [];
  const idx = {};
  cab.forEach(function (t, i) {
    const s = String(t || '');
    if (s.indexOf('Pagamento') === 0) idx.pagamento = i + 1;
    else if (s === 'Status') idx.status = i + 1;
    else if (s.indexOf('Repassado') === 0) idx.nf = i + 1;
    else if (s.indexOf('Observa') === 0) idx.obs = i + 1;
  });
  for (let r = LIN0; nCab >= 1 && r < LIN0 + N_PROJ; r++) {
    const proj = String(sh.getRange(r, 1).getDisplayValue() || '').trim();
    if (!proj) continue;
    const g = {};
    let tem = false;
    ['pagamento', 'status', 'nf', 'obs'].forEach(function (k) {
      if (!idx[k]) return;
      const v = sh.getRange(r, idx[k]).getValue();
      if (v !== '' && v !== null) { g[k] = v; tem = true; }
    });
    if (tem) { guardado[proj] = g; nGuardado++; }
  }

  // 2 · reescreve a aba
  const cols = layout_(p);
  // Descongelar ANTES de mesclar: o Google recusa mesclar células que cruzam a
  // fronteira do congelamento, e a aba vem congelada do formato anterior.
  sh.setFrozenRows(0);
  sh.setFrozenColumns(0);
  sh.getRange(1, 1, sh.getMaxRows(), sh.getMaxColumns()).breakApart();
  sh.clear();
  sh.clearConditionalFormatRules();
  const nc = cols.length;

  // a aba precisa ter colunas e linhas bastantes antes de escrever
  if (sh.getMaxColumns() < nc) sh.insertColumnsAfter(sh.getMaxColumns(), nc - sh.getMaxColumns());
  const precisa = LIN0 + N_PROJ + 2;
  if (sh.getMaxRows() < precisa) sh.insertRowsAfter(sh.getMaxRows(), precisa - sh.getMaxRows());

  sh.getRange(1, 1, 1, nc).merge().setValue('COMISSÕES   ·   ' + p.nome.toUpperCase())
    .setBackground(NAVY).setFontColor(GOLDS).setFontSize(14).setFontWeight('bold')
    .setVerticalAlignment('middle');
  sh.setRowHeight(1, 28);
  sh.getRange(2, 1, 1, nc).merge()
    .setValue('As colunas azuis vêm sozinhas da Custo por Projeto. Preencha a data '
      + 'combinada, o status' + (p.pj ? ', a nota fiscal' : '') + ' e a observação.'
      + (p.perfil === 'projetista'
         ? '   ·   Venda, custos e receita líquida aparecem na sua parte: o valor '
           + 'do projeto multiplicado pela Participação, que é quanto dos ambientes, '
           + 'em R$, está no seu nome.'
         : ''))
    .setBackground('#f6edd6').setFontColor(NAVY2).setFontSize(9).setFontStyle('italic');
  sh.setRowHeight(2, 18);

  sh.getRange(3, 1, 1, nc).setValues([cols.map(function (c) { return c.t; })])
    .setBackground(NAVY2).setFontColor(GOLDS).setFontSize(9).setFontWeight('bold')
    .setWrap(true).setHorizontalAlignment('center');
  sh.setRowHeight(3, 30);
  cols.forEach(function (c, i) { sh.setColumnWidth(i + 1, c.w * 7); });
  sh.setFrozenRows(3);
  // Sem congelar colunas: as linhas 1 e 2 sao mescladas de ponta a ponta, e o
  // Google recusa congelar duas colunas quando isso partiria a celula mesclada
  // ao meio. A aba tem no maximo doze colunas — cabe na tela sem congelamento.

  for (let i = 0; i < nc; i++) {
    const c = cols[i];
    if (!c.calc) continue;
    const fs = [];
    for (let r = LIN0; r < LIN0 + N_PROJ; r++) fs.push([c.f(r)]);
    const rg = sh.getRange(LIN0, i + 1, N_PROJ, 1);
    posFs_(rg, fs).setBackground(CALC).setFontColor(NAVY2).setFontSize(10);
    if (c.nf) rg.setNumberFormat(c.nf);
    if (c.total) rg.setFontWeight('bold'); else rg.setFontStyle('italic');
  }
  for (let i = 0; i < nc; i++) {
    const c = cols[i];
    if (!c.manual) continue;
    const rg = sh.getRange(LIN0, i + 1, N_PROJ, 1);
    rg.setBackground('#ffffff').setFontColor('#1b2733').setFontSize(10);
    if (c.nf) rg.setNumberFormat(c.nf);
    if (c.manual !== 'obs') rg.setHorizontalAlignment('center');
    if (c.manual === 'status') {
      rg.setDataValidation(SpreadsheetApp.newDataValidation()
        .requireValueInList(['Em aberto', 'Pago'], true).build());
    }
    if (c.manual === 'nf') {
      rg.setDataValidation(SpreadsheetApp.newDataValidation()
        .requireValueInList(['Sim', 'Não'], true).build());
    }
  }
  sh.getRange(LIN0, 1, N_PROJ, nc).setBorder(true, true, true, true, true, true,
    '#d6dbe2', SpreadsheetApp.BorderStyle.SOLID);

  // total e o apagamento de quem não entrou no projeto
  const iTot = cols.findIndex(function (c) { return c.total; }) + 1;
  const LT = colLetra_(iTot);
  const rTot = LIN0 + N_PROJ;
  sh.getRange(rTot, 1, 1, nc).setBackground(NAVY);
  sh.getRange(rTot, 1).setValue('TOTAL').setFontColor(GOLDS).setFontWeight('bold');
  posF_(sh.getRange(rTot, iTot),
        '=ROUND(SUM(' + LT + LIN0 + ':' + LT + (rTot - 1) + '),2)')
    .setNumberFormat(MOEDA).setFontColor(GOLDS).setFontWeight('bold');

  const faixa = sh.getRange(LIN0, 1, N_PROJ, nc);
  const LS = colLetra_(cols.findIndex(function (c) { return c.manual === 'status'; }) + 1);
  sh.setConditionalFormatRules([
    SpreadsheetApp.newConditionalFormatRule().whenFormulaSatisfied(
      fx_('=AND($A' + LIN0 + '<>"",$' + LT + LIN0 + '=0)'))
      .setFontColor('#dde0e4').setRanges([faixa]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenFormulaSatisfied(
      '=$' + LS + LIN0 + '="Pago"')
      .setBackground(OKBG).setFontColor('#2f7d4f').setBold(true)
      .setRanges([sh.getRange(LIN0, cols.findIndex(function (c) {
        return c.manual === 'status'; }) + 1, N_PROJ, 1)]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenFormulaSatisfied(
      '=$' + LS + LIN0 + '="Em aberto"')
      .setBackground(ABERTOBG).setFontColor('#a8700f').setBold(true)
      .setRanges([sh.getRange(LIN0, cols.findIndex(function (c) {
        return c.manual === 'status'; }) + 1, N_PROJ, 1)]).build(),
  ]);

  SpreadsheetApp.flush();

  // 3 · devolve o que estava digitado, pelo nome do projeto
  const novoIdx = {};
  cols.forEach(function (c, i) { if (c.manual) novoIdx[c.manual] = i + 1; });
  for (let r = LIN0; r < LIN0 + N_PROJ; r++) {
    const proj = String(sh.getRange(r, 1).getDisplayValue() || '').trim();
    const g = guardado[proj];
    if (!proj || !g) continue;
    Object.keys(g).forEach(function (k) {
      if (novoIdx[k]) sh.getRange(r, novoIdx[k]).setValue(g[k]);
    });
  }

  // 4 · o Painel aponta para as colunas novas
  atualizarPainel_(ss, LT, colLetra_(novoIdx.pagamento), LS);
  return nGuardado;
}


function atualizarPainel_(ss, LT, LP, LS) {
  const pa = ss.getSheetByName('Painel');
  if (!pa) return;
  const p0 = LIN0, pf = LIN0 + N_PROJ - 1;
  const C = "'Comissões'!";
  posF_(pa.getRange('C7'), '=ROUND(SUM(' + C + '$' + LT + '$' + p0 + ':$' + LT + '$' + pf + '),2)');
  posF_(pa.getRange('E7'), '=ROUND(SUMIF(' + C + '$' + LS + '$' + p0 + ':$' + LS + '$' + pf
    + ',"Pago",' + C + '$' + LT + '$' + p0 + ':$' + LT + '$' + pf + '),2)');
  posF_(pa.getRange('G7'), '=ROUND($C$7-$E$7,2)');

  // a tabela mês a mês começa onde estiver o rótulo "Janeiro"
  let lj = 0;
  for (let r = 10; r <= 20; r++) {
    if (String(pa.getRange(r, 2).getDisplayValue()).trim() === 'Janeiro') { lj = r; break; }
  }
  if (!lj) return;
  for (let m = 0; m < 12; m++) {
    const r = lj + m;
    const ini = 'DATE(YEAR(TODAY()),' + (m + 1) + ',1)';
    const fim = 'EOMONTH(DATE(YEAR(TODAY()),' + (m + 1) + ',1),0)';
    posF_(pa.getRange(r, 3), '=ROUND(SUMIFS(' + C + '$' + LT + '$' + p0 + ':$' + LT + '$' + pf
      + ',' + C + '$' + LP + '$' + p0 + ':$' + LP + '$' + pf + ',">="&' + ini
      + ',' + C + '$' + LP + '$' + p0 + ':$' + LP + '$' + pf + ',"<="&' + fim + '),2)');
    posF_(pa.getRange(r, 4), '=ROUND(SUMIFS(' + C + '$' + LT + '$' + p0 + ':$' + LT + '$' + pf
      + ',' + C + '$' + LP + '$' + p0 + ':$' + LP + '$' + pf + ',">="&' + ini
      + ',' + C + '$' + LP + '$' + p0 + ':$' + LP + '$' + pf + ',"<="&' + fim
      + ',' + C + '$' + LS + '$' + p0 + ':$' + LS + '$' + pf + ',"Pago"),2)');
    posF_(pa.getRange(r, 5), '=ROUND($C' + r + '-$D' + r + ',2)');
  }
  posF_(pa.getRange(lj + 12, 3), '=ROUND(SUM(C' + lj + ':C' + (lj + 11) + '),2)');
  posF_(pa.getRange(lj + 12, 4), '=ROUND(SUM(D' + lj + ':D' + (lj + 11) + '),2)');
  posF_(pa.getRange(lj + 12, 5), '=ROUND(SUM(E' + lj + ':E' + (lj + 11) + '),2)');
}


function colLetra_(n) {
  let s = '';
  while (n > 0) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = (n - 1 - m) / 26; }
  return s;
}
