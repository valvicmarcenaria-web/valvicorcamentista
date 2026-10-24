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
  { nome: 'Bruna',    perfil: 'gestao',      pj: true,
    id: '1kIvZ5chhDav8t7R_xh1c03ctqGXs2ZDc17WD8BglFk0' },
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
  custoTotal: 'D22', margem: 'D23',   // bloco resumo · coluna D = realizado
  comGestao: 'D66',                   // gestão técnica · 0,5% do líquido
  gestorTecnico: 'H9',                // ao lado do coordenador, na identificação
  vendedorNome: 'D9', comVenda: 'D41',
  competencia: 'D10',                 // linha 10 · era espaçador
  entregaSituacao: 'L9',              // No prazo · Atrasado · Em produção
  faturado: 'D34',                    // total das notas emitidas
  rtValor: 'D43', rtStatus: 'H43',    // RT do parceiro e se já foi pago
  colsBase: 38,
};
const COLS_AMB = 'ABCDEFGHIJKLMNO'.split('');

// colunas da Base, por nome — usadas nas fórmulas das individuais
const B = {
  projeto: 'A', valor: 'E',
  prodQuem: 'F', prodCom: 'H', montQuem: 'J', montCom: 'L',
  projQuem: 'N', projCom: 'P', coordQuem: 'S', coordCom: 'T',
  liquido: 'U', venda: 'V',
  imposto: 'W', maquina: 'X', rt: 'Y', vendedor: 'Z', custoVenda: 'AA',
  gestQuem: 'AD', gestCom: 'AE', vendQuem: 'AF', vendCom: 'AG',
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
let CALIBRADO = false;

function calibrar_(ss) {
  // Se uma execução anterior morreu no meio, a aba de teste pode ter ficado.
  // insertSheet com nome repetido dá erro, então tira a velha antes.
  const velha = ss.getSheetByName('__teste_separador__');
  if (velha) ss.deleteSheet(velha);
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
  CALIBRADO = true;
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

/**
 * setFormula e setFormulas passando pelo tradutor.
 *
 * A trava do CALIBRADO existe porque esse erro já aconteceu duas vezes: uma
 * função nova escreve fórmula sem ter chamado calibrar_ antes, grava vírgula
 * numa planilha que quer ponto e vírgula, e a ficha inteira vira #ERROR! sem
 * nenhum aviso. Agora a execução para e diz o nome da função que esqueceu.
 */
function posF_(rg, f) {
  exigirCalibracao_();
  return rg.setFormula(fx_(f));
}
function posFs_(rg, m) {
  exigirCalibracao_();
  return rg.setFormulas(m.map(function (lin) { return lin.map(fx_); }));
}

function exigirCalibracao_() {
  if (CALIBRADO) return;
  throw new Error('fórmula escrita sem calibrar o separador. '
    + 'Chame calibrar_(ss) antes de escrever fórmula nesta planilha.');
}


const NAVY = '#0e2038', NAVY2 = '#16314f', GOLDS = '#d8bd80';
const CALC = '#eaf1f8', ZEBRA = '#f7f5ef', OKBG = '#e6f0e9', ABERTOBG = '#faefdc';
const GOLDBG = '#f6edd6', MUTED = '#6c7785', OK = '#2f7d4f', ABERTO = '#c47d0e';
const INK = '#1b2733';

// O cadastro da ficha, igual ao do bloco 5. Jackson saiu da equipe mas o nome
// continua nas fichas antigas, e a comissão que ele gerou continua somando.
const EQUIPE_FICHA = ['Deivison', 'Ronald', 'Samuel', 'Cesar', 'Jhon', 'Joelson',
  'Davi', 'Jomar', 'Bruno', 'Wallace', 'Douglas', 'Terceiro / avulso'];
// A Bruna saiu do menu de projetista: passou a Gestora Técnica e não desenha
// projeto. Continua no cadastro do bloco 5, porque recebe.
const PROJETISTAS_FICHA = ['Lorrane', 'Lucas', 'Externo / avulso'];
const GESTORES_FICHA = ['Bruna'];
const AV0 = 4, AVF = 33;          // faixa de lançamentos da aba Avulsos
const MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
  'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
const MOEDA = 'R$ #,##0.00', PCT = '0.0%', DATA = 'dd/mm/yyyy';


// ════════════════════════════════════════════════════════════════════════
//  PAINEL DE GESTÃO  ·  a planilha que o Walton abre
// ════════════════════════════════════════════════════════════════════════
//
// Por que planilha e não Looker: aqui o painel se constrói sozinho, por
// script, e atualiza no mesmo atualizarTudo. No Looker alguém teria de montar
// cada gráfico à mão e refazer quando a estrutura mudasse.
//
// Por que não tem filtro de mês: quem abre como LEITOR não consegue mexer em
// filtro nenhum — filtro exige permissão de edição, e investidor com edição na
// planilha não é opção. Então o ano inteiro aparece de uma vez, mês a mês.
//
// Tudo aqui é VALOR calculado pelo script. Nenhuma fórmula aponta para as
// planilhas de origem: o Walton não alcança arquivo nenhum, nem pelo texto de
// uma fórmula.

const ID_PAINEL = '1-7XUrVso9oVKccQjM2m5Tgd9_-QIk-r1LZ8XZbDnGL0';


function montarPainelGestao() {
  const ano = new Date().getFullYear();
  const d = lerTudoDoPainel_(ano);
  const ss = SpreadsheetApp.openById(ID_PAINEL);

  abaVisaoGeral_(ss, d, ano);
  abaMargem_(ss, d);
  abaComissoes_(ss, d, ano);
  abaEquipe_(ss, d, ano);
  abaComoLer_(ss, d, ano);

  // a aba padrão "Página1" só atrapalha
  const p1 = ss.getSheetByName('Página1') || ss.getSheetByName('Sheet1');
  if (p1 && ss.getSheets().length > 1) ss.deleteSheet(p1);

  SpreadsheetApp.flush();
  const r = d.projetos.length + ' projeto(s) · ' + d.ambientes.length + ' ambiente(s) · '
          + d.recebimentos.length + ' recebimento(s)';
  console.log('Painel de Gestão: ' + r);
  return r;
}


/** Lê as quatro bases e devolve tudo já somado. */
function lerTudoDoPainel_(ano) {
  const pg = SpreadsheetApp.openById(ID_PAG);
  const cp = SpreadsheetApp.openById(ID_CUSTO);

  const pega = function (ss, aba) {
    const sh = ss.getSheetByName(aba);
    if (!sh) throw new Error('aba "' + aba + '" não encontrada — rode montarBasesDoPainel antes.');
    const n = sh.getLastRow() - 1;
    if (n < 1) return [];
    return sh.getRange(2, 1, n, sh.getLastColumn()).getValues();
  };

  const projetos = pega(pg, 'Base · Projetos');
  const recebimentos = pega(pg, 'Base · Recebimentos');
  const custoFixo = pega(pg, 'Base · Custo Fixo');
  const aporte = lerAporte_(pg);
  const base = pega(cp, FICHA.base);

  // ── ambientes: só linha com ambiente preenchido ──
  const ambientes = base.filter(function (L) { return String(L[2] || '').trim() !== ''; });

  // ── um registro por projeto, com venda, custo e margem ──
  const porProjeto = {};
  base.forEach(function (L) {
    const nome = String(L[0] || '').trim();
    if (!nome) return;
    if (!porProjeto[nome]) {
      porProjeto[nome] = { projeto: nome, cliente: String(L[1] || '').trim(),
                           venda: 0, liquido: 0, custo: 0, margem: 0, ambientes: 0, valor: 0 };
    }
    const p = porProjeto[nome];
    p.venda += Number(L[21]) || 0;      // só a primeira linha do bloco tem valor
    p.liquido += Number(L[20]) || 0;
    p.custo += Number(L[27]) || 0;
    p.margem += Number(L[28]) || 0;
    if (String(L[2] || '').trim()) { p.ambientes++; p.valor += Number(L[4]) || 0; }
  });

  return {
    projetos: projetos, recebimentos: recebimentos, custoFixo: custoFixo,
    aporte: aporte,
    base: base, ambientes: ambientes,
    porProjeto: Object.keys(porProjeto).map(function (k) { return porProjeto[k]; }),
  };
}


// ── desenho ─────────────────────────────────────────────────────────────

/** Devolve a aba limpa, pronta para receber o desenho. */
function abaLimpa_(ss, nome, largura) {
  let sh = ss.getSheetByName(nome);
  if (!sh) sh = ss.insertSheet(nome);
  sh.getCharts().forEach(function (c) { sh.removeChart(c); });
  const tudo = sh.getRange(1, 1, sh.getMaxRows(), sh.getMaxColumns());
  tudo.breakApart();
  tudo.clear();
  sh.clearConditionalFormatRules();
  sh.setFrozenRows(0);
  if (sh.getMaxColumns() < largura) sh.insertColumnsAfter(sh.getMaxColumns(), largura - sh.getMaxColumns());
  sh.setHiddenGridlines(true);
  sh.setTabColor(NAVY2);
  sh.setColumnWidth(1, 16);
  return sh;
}

/** Cabeçalho de marca, igual em todas as abas. */
function cabecalhoPainel_(sh, titulo, sub, largura) {
  sh.getRange(1, 2, 1, largura - 2).merge().setValue('  VALVIC MARCENARIA        ' + titulo)
    .setBackground(NAVY).setFontColor('#ffffff').setFontSize(13).setFontWeight('bold')
    .setVerticalAlignment('middle');
  sh.setRowHeight(1, 34);
  sh.getRange(2, 2, 1, largura - 2).merge().setValue('  ' + sub)
    .setBackground(GOLDBG).setFontColor(NAVY2).setFontSize(9).setFontStyle('italic')
    .setVerticalAlignment('middle');
  sh.setRowHeight(2, 20);
  sh.setRowHeight(3, 8);
}

/** Faixa de seção. */
function secaoPainel_(sh, lin, texto, largura) {
  sh.getRange(lin, 2, 1, largura - 2).merge().setValue('  ' + texto)
    .setBackground(NAVY2).setFontColor(GOLDS).setFontSize(9.5).setFontWeight('bold')
    .setVerticalAlignment('middle');
  sh.setRowHeight(lin, 20);
}

/** Tabela com cabeçalho e linhas, devolvendo a linha seguinte. */
function tabelaPainel_(sh, lin, col, cab, linhas, formatos) {
  const n = cab.length;
  sh.getRange(lin, col, 1, n).setValues([cab])
    .setBackground(NAVY).setFontColor(GOLDS).setFontSize(8.5).setFontWeight('bold')
    .setHorizontalAlignment('center').setWrap(true);
  sh.setRowHeight(lin, 26);
  if (linhas.length) {
    const rg = sh.getRange(lin + 1, col, linhas.length, n);
    rg.setValues(linhas).setFontSize(10).setFontColor(INK)
      .setBorder(true, true, true, true, true, true, '#d6dbe2', SpreadsheetApp.BorderStyle.SOLID);
    formatos.forEach(function (f, i) {
      if (f) sh.getRange(lin + 1, col + i, linhas.length, 1).setNumberFormat(f);
    });
    for (let i = 0; i < linhas.length; i += 2) {
      sh.getRange(lin + 1 + i, col, 1, n).setBackground(ZEBRA);
    }
  }
  return lin + linhas.length + 2;
}

/** Cartão grande de número. */
function cartaoPainel_(sh, lin, col, rotulo, valor, cor, formato) {
  sh.getRange(lin, col, 1, 2).merge().setValue(rotulo)
    .setFontColor(MUTED).setFontSize(9).setFontWeight('bold').setHorizontalAlignment('center');
  sh.getRange(lin + 1, col, 1, 2).merge().setValue(valor)
    .setNumberFormat(formato || MOEDA).setFontColor(cor).setFontSize(16).setFontWeight('bold')
    .setHorizontalAlignment('center').setVerticalAlignment('middle')
    .setBackground('#ffffff')
    .setBorder(true, true, true, true, false, false, '#d6dbe2', SpreadsheetApp.BorderStyle.SOLID);
  sh.setRowHeight(lin + 1, 30);
}


// ── aba 1 · Visão geral ─────────────────────────────────────────────────
function abaVisaoGeral_(ss, d, ano) {
  const W = 9;
  const sh = abaLimpa_(ss, 'Visão geral', W);
  cabecalhoPainel_(sh, 'PAINEL DE GESTÃO', 'Ano ' + ano
    + '   ·   vendido é contrato assinado   ·   recebido é dinheiro que entrou   ·   os dois não batem, e não é erro', W);
  for (let c = 2; c <= W; c++) sh.setColumnWidth(c, 118);

  // ── do ano corrente ──
  const doAno = d.projetos.filter(function (L) { return String(L[0]) === String(ano); });
  const vendido = doAno.reduce(function (s, L) { return s + (Number(L[4]) || 0); }, 0);
  const aReceber = doAno.reduce(function (s, L) { return s + (Number(L[6]) || 0); }, 0);
  const recAno = d.recebimentos.filter(function (L) { return String(L[6]) === String(ano); });
  const recebido = recAno.reduce(function (s, L) { return s + (Number(L[4]) || 0); }, 0);

  let fixo = 0;
  d.custoFixo.forEach(function (L) {
    if (String(L[0] || '').indexOf('Custo operacional') === 0) fixo = Number(L[2]) || 0;
  });

  let lin = 5;
  secaoPainel_(sh, lin, 'O ANO EM QUATRO NÚMEROS', W); lin += 2;
  cartaoPainel_(sh, lin, 2, 'Vendido no ano', vendido, NAVY);
  cartaoPainel_(sh, lin, 4, 'Recebido no ano', recebido, '#2f7d4f');
  cartaoPainel_(sh, lin, 6, 'A receber', aReceber, '#c47d0e');
  cartaoPainel_(sh, lin, 8, 'Custo fixo por mês', fixo, '#b0413f');
  lin += 4;

  // ── mês a mês ──
  secaoPainel_(sh, lin, 'MÊS A MÊS   ·   ' + ano, W); lin += 2;
  const linhas = [];
  for (let m = 0; m < 12; m++) {
    const vendM = doAno.filter(function (L) { return String(L[1]) === MESES[m]; });
    const recM = recAno.filter(function (L) { return String(L[7]) === MESES[m]; });
    linhas.push([
      MESES[m],
      vendM.reduce(function (s, L) { return s + (Number(L[4]) || 0); }, 0),
      recM.reduce(function (s, L) { return s + (Number(L[4]) || 0); }, 0),
      vendM.length,
    ]);
  }
  linhas.push(['Total do ano',
    linhas.reduce(function (s, L) { return s + L[1]; }, 0),
    linhas.reduce(function (s, L) { return s + L[2]; }, 0),
    linhas.reduce(function (s, L) { return s + L[3]; }, 0)]);

  const linTab = lin;
  lin = tabelaPainel_(sh, lin, 2, ['Mês', 'Vendido', 'Recebido', 'Projetos vendidos'],
                      linhas, [null, MOEDA, MOEDA, '0']);
  sh.getRange(linTab + 13, 2, 1, 4).setBackground(NAVY).setFontColor(GOLDS).setFontWeight('bold');

  const g = sh.newChart().setChartType(Charts.ChartType.COLUMN)
    .addRange(sh.getRange(linTab, 2, 13, 3))
    .setPosition(linTab, 6, 0, 0)
    .setOption('title', 'Vendido e recebido, mês a mês')
    .setOption('colors', [NAVY, '#2f7d4f'])
    .setOption('legend', { position: 'top' })
    .setOption('width', 500).setOption('height', 300)
    .build();
  sh.insertChart(g);

  // ── ano a ano ──
  secaoPainel_(sh, lin, 'ANO A ANO', W); lin += 2;
  const anos = {};
  d.projetos.forEach(function (L) {
    const a = String(L[0]);
    if (!anos[a]) anos[a] = { n: 0, vend: 0, rec: 0, sal: 0 };
    anos[a].n++; anos[a].vend += Number(L[4]) || 0;
    anos[a].rec += Number(L[5]) || 0; anos[a].sal += Number(L[6]) || 0;
  });
  const lAnos = Object.keys(anos).sort().reverse().map(function (a) {
    const x = anos[a];
    return [a, x.n, x.vend, x.rec, x.sal, x.vend ? x.rec / x.vend : 0, x.n ? x.vend / x.n : 0];
  });
  lin = tabelaPainel_(sh, lin, 2,
    ['Ano', 'Projetos', 'Vendido', 'Recebido', 'A receber', '% recebido', 'Ticket médio'],
    lAnos, [null, '0', MOEDA, MOEDA, MOEDA, '0.0%', MOEDA]);

  // ── custo fixo ──
  secaoPainel_(sh, lin, 'CUSTO FIXO DA OPERAÇÃO   ·   por mês', W); lin += 2;
  lin = tabelaPainel_(sh, lin, 2, ['Indicador', 'Grupo', 'Valor'],
    d.custoFixo.map(function (L) { return [L[0], L[1], Number(L[2]) || 0]; }),
    [null, null, MOEDA]);

  // ── aporte do Walton · o dinheiro dele ──
  if (d.aporte.length) {
    secaoPainel_(sh, lin, 'APORTE DO WALTON', W); lin += 2;
    lin = tabelaPainel_(sh, lin, 2, ['Movimento', 'Valor'], d.aporte, [null, MOEDA]);
  }
}


// ── aba 2 · Margem por projeto ──────────────────────────────────────────
function abaMargem_(ss, d) {
  const W = 8;
  const sh = abaLimpa_(ss, 'Margem por projeto', W);
  cabecalhoPainel_(sh, 'MARGEM POR PROJETO',
    'Margem de contribuição = venda menos todo o custo do projeto   ·   o pior vem primeiro, '
    + 'porque é esse que precisa de conversa', W);
  sh.setColumnWidth(2, 190); sh.setColumnWidth(3, 170);
  for (let c = 4; c <= W; c++) sh.setColumnWidth(c, 125);

  const com = d.porProjeto.filter(function (p) { return p.venda > 0; })
    .map(function (p) {
      return [p.projeto, p.cliente, p.venda, p.custo, p.margem,
              p.venda ? p.margem / p.venda : 0, p.ambientes];
    })
    .sort(function (a, b) { return a[5] - b[5]; });

  let lin = 5;
  secaoPainel_(sh, lin, 'PROJETOS COM VENDA LANÇADA', W); lin += 2;
  const l0 = lin;
  lin = tabelaPainel_(sh, lin, 2,
    ['Projeto', 'Cliente', 'Valor de venda', 'Custo total', 'Margem', 'MC %', 'Ambientes'],
    com, [null, null, MOEDA, MOEDA, MOEDA, '0.0%', '0']);

  if (com.length) {
    const faixa = sh.getRange(l0 + 1, 7, com.length, 1);
    sh.setConditionalFormatRules([
      SpreadsheetApp.newConditionalFormatRule().whenNumberLessThan(0.25)
        .setBackground('#fbe7e6').setFontColor('#b0413f').setBold(true).setRanges([faixa]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenNumberBetween(0.25, 0.35)
        .setBackground('#fbf1dc').setFontColor('#c47d0e').setBold(true).setRanges([faixa]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenNumberGreaterThan(0.35)
        .setBackground('#e2f0e7').setFontColor('#2f7d4f').setBold(true).setRanges([faixa]).build(),
    ]);
  }

  sh.getRange(lin, 2, 1, W - 1).merge().setValue(
    'Leia junto com a ficha. Projeto com ambiente ainda não lançado mostra margem alta e falsa — '
    + 'faltam custos. MC acima de 60% quase sempre é ficha incompleta, não lucro.')
    .setFontColor(MUTED).setFontSize(9).setFontStyle('italic').setWrap(true);
  sh.setRowHeight(lin, 32);
}


// ── categorias profissionais, como o Walton enxerga a casa ──────────────
//
// Vendedores · Projetistas e coordenação · Operação. Quem não está nomeado
// aqui cai em Operação, que é onde está a maioria e onde entra o freelancer
// que aparece uma vez e some.
const CATEGORIA = {
  'Jonathan': 'Vendedores', 'Vitor': 'Vendedores',
  'Lorrane': 'Projetistas e coordenação', 'Lucas': 'Projetistas e coordenação',
  'Bruna': 'Projetistas e coordenação', 'Deivison': 'Projetistas e coordenação',
};
const ORDEM_CAT = ['Vendedores', 'Projetistas e coordenação', 'Operação'];
function categoriaDe_(nome) { return CATEGORIA[nome] || 'Operação'; }

// Cada frente de comissão: quem recebe, quanto, e qual data a situa no mês.
//
// Produção fecha pela data de FABRICAÇÃO e montagem pela data de MONTAGEM —
// é a diferença entre o que saiu da fábrica e o que chegou na casa do cliente.
// Projeto, coordenação, gestão e venda não têm etapa própria: nascem com o
// projeto, então seguem a data de entrada.
const FRENTES_COM = [
  { quem: 5,  val: 7,  data: 8,  nome: 'Produção' },
  { quem: 9,  val: 11, data: 12, nome: 'Montagem' },
  { quem: 13, val: 15, data: 17, nome: 'Projeto' },
  { quem: 18, val: 19, data: 17, nome: 'Coordenação' },
  { quem: 29, val: 30, data: 17, nome: 'Gestão técnica' },
  { quem: 31, val: 32, data: 17, nome: 'Venda' },
];

/**
 * Doze colunas de mês mais "sem data" e total.
 *
 * É assim que o painel entrega a visão mensal sem filtro: quem abre como
 * leitor não consegue mexer em filtro nenhum, então em vez de esconder onze
 * meses atrás de um controle que ele não pode tocar, os doze ficam à vista.
 */
function cabMeses_(primeira) {
  return [primeira].concat(MESES.map(function (m) { return m.substring(0, 3); }))
                   .concat(['Sem data', 'Total']);
}

/** Acumulador: chave → [12 meses, sem data, total]. */
function novaMatriz_() { return {}; }
function somaNaMatriz_(m, chave, data, valor, ano) {
  if (!valor) return;
  if (!m[chave]) m[chave] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0];
  const l = m[chave];
  if (data instanceof Date && data.getFullYear() === ano) l[data.getMonth()] += valor;
  else l[12] += valor;
  l[13] += valor;
}
function matrizEmLinhas_(m, rotulo) {
  return Object.keys(m).sort(function (a, b) { return m[b][13] - m[a][13]; })
    .map(function (k) { return [rotulo ? rotulo(k) : k].concat(m[k]); });
}
function linhaTotal_(linhas, rotulo) {
  const t = [rotulo];
  for (let c = 0; c < 14; c++) {
    t.push(linhas.reduce(function (s, L) { return s + (Number(L[c + 1]) || 0); }, 0));
  }
  return t;
}
function formatosMes_() {
  const f = [null];
  for (let i = 0; i < 14; i++) f.push(MOEDA);
  return f;
}


// ── aba 3 · Comissões ───────────────────────────────────────────────────
function abaComissoes_(ss, d, ano) {
  const W = 17;
  const sh = abaLimpa_(ss, 'Comissões', W);
  cabecalhoPainel_(sh, 'COMISSÕES   ·   ' + ano,
    'Produção fecha pela data de fabricação, montagem pela data de montagem   ·   '
    + 'o resto segue a data de entrada do projeto   ·   sem nome de ninguém', W);
  sh.setColumnWidth(2, 200);
  for (let c = 3; c <= W; c++) sh.setColumnWidth(c, 92);

  const porCat = novaMatriz_(), porFrente = novaMatriz_();
  d.base.forEach(function (L) {
    FRENTES_COM.forEach(function (f) {
      const v = Number(L[f.val]) || 0;
      if (!v) return;
      const quem = String(L[f.quem] || '').trim();
      somaNaMatriz_(porCat, quem ? categoriaDe_(quem) : 'Sem dono', L[f.data], v, ano);
      somaNaMatriz_(porFrente, f.nome, L[f.data], v, ano);
    });
  });

  let lin = 5;
  secaoPainel_(sh, lin, 'POR CATEGORIA PROFISSIONAL', W); lin += 2;
  const lCat = ORDEM_CAT.concat(['Sem dono'])
    .filter(function (c) { return porCat[c]; })
    .map(function (c) { return [c].concat(porCat[c]); });
  const l0 = lin;
  lin = tabelaPainel_(sh, lin, 2, cabMeses_('Categoria'),
                      lCat.concat([linhaTotal_(lCat, 'Total')]), formatosMes_());
  sh.getRange(l0 + lCat.length + 1, 2, 1, 15)
    .setBackground(NAVY).setFontColor(GOLDS).setFontWeight('bold');
  const iSemDono = lCat.map(function (r) { return r[0]; }).indexOf('Sem dono');
  if (iSemDono >= 0) {
    sh.getRange(l0 + 1 + iSemDono, 2, 1, 15)
      .setBackground(ABERTOBG).setFontColor('#c47d0e').setFontWeight('bold');
  }

  secaoPainel_(sh, lin, 'POR TIPO DE TRABALHO', W); lin += 2;
  const lFr = FRENTES_COM.map(function (f) { return f.nome; })
    .filter(function (n) { return porFrente[n]; })
    .map(function (n) { return [n].concat(porFrente[n]); });
  const l1 = lin;
  lin = tabelaPainel_(sh, lin, 2, cabMeses_('Tipo de trabalho'),
                      lFr.concat([linhaTotal_(lFr, 'Total')]), formatosMes_());
  sh.getRange(l1 + lFr.length + 1, 2, 1, 15)
    .setBackground(NAVY).setFontColor(GOLDS).setFontWeight('bold');

  let liquido = 0, comTotal = 0;
  d.base.forEach(function (L) { liquido += Number(L[20]) || 0; });
  lFr.forEach(function (r) { comTotal += r[14]; });

  secaoPainel_(sh, lin, 'PESO DA OPERAÇÃO', W); lin += 2;
  cartaoPainel_(sh, lin, 2, 'Comissão total', comTotal, NAVY);
  cartaoPainel_(sh, lin, 4, 'Receita líquida', liquido, '#2f5d8c');
  cartaoPainel_(sh, lin, 6, 'Comissão ÷ receita', liquido ? comTotal / liquido : 0,
                '#c47d0e', '0.0%');
  lin += 4;
  sh.getRange(lin, 2, 1, W - 2).merge().setValue(
    'Historicamente esse percentual fica entre 15% e 22%. A coluna "Sem data" é o trabalho '
    + 'sem data de etapa lançada, e a linha "Sem dono" é comissão calculada com o nome em '
    + 'branco — as duas somam no total e não aparecem em mês nenhum.')
    .setFontColor(MUTED).setFontSize(9).setFontStyle('italic').setWrap(true);
  sh.setRowHeight(lin, 32);
}


// ── aba 4 · Equipe ──────────────────────────────────────────────────────
function abaEquipe_(ss, d, ano) {
  const W = 17;
  const sh = abaLimpa_(ss, 'Equipe', W);
  cabecalhoPainel_(sh, 'VOLUME DE OBRA POR COLABORADOR   ·   ' + ano,
    'Quanto de obra, em reais, passou pelas mãos de cada um, mês a mês   ·   '
    + 'é produção, não é o que a pessoa recebe', W);
  sh.setColumnWidth(2, 165); sh.setColumnWidth(3, 150);
  for (let c = 4; c <= W; c++) sh.setColumnWidth(c, 88);

  const matriz = function (iQuem, iData, iValor) {
    const m = novaMatriz_();
    d.ambientes.forEach(function (L) {
      const quem = String(L[iQuem] || '').trim();
      if (!quem) return;
      somaNaMatriz_(m, quem, L[iData], Number(L[iValor]) || 0, ano);
    });
    return Object.keys(m).sort(function (a, b) { return m[b][13] - m[a][13]; })
      .map(function (k) { return [k, categoriaDe_(k)].concat(m[k]); });
  };

  const cab = ['Colaborador', 'Categoria'].concat(
    MESES.map(function (x) { return x.substring(0, 3); })).concat(['Sem data', 'Total']);
  const fmt = [null, null].concat(MESES.map(function () { return MOEDA; }))
                          .concat([MOEDA, MOEDA]);

  const bloco = function (lin, titulo, linhas) {
    secaoPainel_(sh, lin, titulo, W); lin += 2;
    const l0 = lin;
    const tot = ['Total', ''];
    for (let c = 0; c < 14; c++) {
      tot.push(linhas.reduce(function (s, L) { return s + (Number(L[c + 2]) || 0); }, 0));
    }
    lin = tabelaPainel_(sh, lin, 2, cab, linhas.concat([tot]), fmt);
    sh.getRange(l0 + linhas.length + 1, 2, 1, 16)
      .setBackground(NAVY).setFontColor(GOLDS).setFontWeight('bold');
    return lin;
  };

  let lin = 5;
  lin = bloco(lin, 'PRODUZIDO   ·   saiu da fábrica, pela data de fabricação',
              matriz(5, 8, 4));
  lin = bloco(lin, 'ENTREGUE   ·   montado na casa do cliente, pela data de montagem',
              matriz(9, 12, 4));
  lin = bloco(lin, 'PROJETADO   ·   desenhado, pela data de entrada do projeto',
              matriz(13, 17, 4));

  sh.getRange(lin, 2, 1, W - 2).merge().setValue(
    'Produzido e entregue não batem no mesmo mês, e não é erro: um ambiente sai da fábrica '
    + 'num mês e é montado noutro. A diferença entre os dois é o que está pronto e ainda não '
    + 'foi entregue. Ambiente sem nome preenchido não aparece aqui e mesmo assim gera comissão.')
    .setFontColor(MUTED).setFontSize(9).setFontStyle('italic').setWrap(true);
  sh.setRowHeight(lin, 32);
}


// ── aba 5 · Como ler ────────────────────────────────────────────────────
function abaComoLer_(ss, d, ano) {
  const W = 7;
  const sh = abaLimpa_(ss, 'Como ler', W);
  cabecalhoPainel_(sh, 'COMO LER ESTE PAINEL', 'Atualizado em '
    + Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "dd/MM/yyyy 'às' HH:mm"), W);
  sh.setColumnWidth(2, 200);
  for (let c = 3; c <= W; c++) sh.setColumnWidth(c, 110);

  const itens = [
    ['Vendido', 'Contrato assinado no período. Vira obra e vira custo, mas não vira caixa na hora.'],
    ['Recebido', 'Dinheiro que entrou no período, muitas vezes de contrato de meses atrás. É caixa.'],
    ['A receber', 'O que já foi vendido e ainda não entrou. É o saldo dos contratos em aberto.'],
    ['Margem de contribuição', 'Venda menos todo o custo do projeto: material, terceirizados, logística, '
      + 'comissões e custos de venda. Não desconta o custo fixo da empresa.'],
    ['Custo fixo', 'O que a operação custa por mês independentemente de vender: folha e estrutura. '
      + 'A soma das margens precisa cobrir isso antes de sobrar lucro.'],
    ['Volume de obra', 'Quanto de obra, em reais, passou pelas mãos de cada pessoa. '
      + 'É medida de produção e de dependência, não de remuneração.'],
    ['Produzido', 'O que saiu da fábrica, somado pela data de fabricação do ambiente.'],
    ['Entregue', 'O que foi montado na casa do cliente, pela data de montagem. Não bate com '
      + 'produzido no mesmo mês, e a diferença é o que está pronto e ainda não foi entregue.'],
    ['Sem data', 'Trabalho lançado sem data de etapa. Soma no total do ano e não aparece em '
      + 'mês nenhum — é o que falta datar.'],
    ['Sem dono', 'Comissão calculada com o nome em branco. Entra no custo do projeto e '
      + 'ninguém recebe.'],
    ['Categoria profissional', 'Vendedores · Projetistas e coordenação · Operação. '
      + 'As comissões aparecem por categoria, nunca com o nome de quem recebe.'],
  ];

  let lin = 5;
  secaoPainel_(sh, lin, 'O QUE CADA PALAVRA SIGNIFICA', W); lin += 2;
  lin = tabelaPainel_(sh, lin, 2, ['Termo', 'O que é'], itens, [null, null]);
  sh.getRange(lin - itens.length - 1, 3, itens.length + 1, 1).setWrap(true);
  sh.setColumnWidth(3, 560);

  secaoPainel_(sh, lin, 'O QUE ESTE PAINEL AINDA NÃO MOSTRA', W); lin += 2;
  const limites = [
    ['Ficha pela metade', 'Projeto com ambiente não lançado aparece com margem alta e comissão baixa. '
      + 'A tabela de margem é o lugar de encontrá-los.'],
    ['Trabalho sem dono', 'Ambiente com percentual preenchido e nome em branco gera comissão que ninguém '
      + 'recebe. Não aparece na aba Equipe e continua no custo.'],
    ['É uma foto', 'Os números são do momento em que o painel foi atualizado, e a data está no '
      + 'alto desta aba. A atualização roda sozinha de madrugada; fora disso, é manual.'],
  ];
  lin = tabelaPainel_(sh, lin, 2, ['Limite', 'Por quê'], limites, [null, null]);
  sh.getRange(lin - limites.length - 1, 3, limites.length + 1, 1).setWrap(true);
}


// ════════════════════════════════════════════════════════════════════════
//  BASES DO PAINEL  ·  as tabelas que o Looker Studio consegue ler
// ════════════════════════════════════════════════════════════════════════
//
// O Looker lê TABELA: uma linha de cabeçalho e, abaixo, linhas iguais entre si.
// As abas de ano da Controle de Pagamentos não são tabela — têm linha divisória
// de mês no meio, cabeçalho mesclado e até cinco pagamentos na mesma linha.
// A aba Custo Fixo é pior: cada pessoa com o salário dela, que é exatamente o
// que não pode chegar ao painel do Walton.
//
// Estas três abas são a tradução. São VALORES, não fórmulas: é uma foto, e por
// isso precisam ser refeitas quando os dados mudam. O atualizarTudo já faz isso.

const ID_PAG = '1zC1cjkDpMA7FPYSf4_CO7WrqhIjmJ7ciXR_QGQ4XA9A';
const ANOS = ['2026', '2025', '2024', '2023'];
const C_BLOCOS = [9, 12, 15, 18, 21];     // I, L, O, R, U · valor, data, descrição
const LIN_ITEM0 = 10;                      // primeira linha de projeto na aba de ano


function montarBasesDoPainel() {
  const ss = SpreadsheetApp.openById(ID_PAG);
  const p = basesProjetosERecebimentos_(ss);
  const cf = baseCustoFixo_(ss);
  SpreadsheetApp.flush();
  const r = p.projetos + ' projeto(s), ' + p.recebimentos + ' recebimento(s), '
          + cf + ' linha(s) de custo fixo';
  console.log('Bases do painel: ' + r);   // rodando sozinha, o log é o único retorno
  return r;
}


/** Escreve uma tabela limpa: cabeçalho fixo em cima, dados embaixo, nada mais. */
function escreverTabela_(ss, nome, cab, linhas) {
  let sh = ss.getSheetByName(nome);
  if (!sh) sh = ss.insertSheet(nome);
  sh.clear();
  // clearDataValidations existe em intervalo, não em aba.
  sh.getRange(1, 1, sh.getMaxRows(), sh.getMaxColumns()).clearDataValidations();
  if (sh.getMaxColumns() < cab.length) {
    sh.insertColumnsAfter(sh.getMaxColumns(), cab.length - sh.getMaxColumns());
  }
  const precisa = linhas.length + 2;
  if (sh.getMaxRows() < precisa) sh.insertRowsAfter(sh.getMaxRows(), precisa - sh.getMaxRows());

  sh.getRange(1, 1, 1, cab.length).setValues([cab])
    .setBackground(NAVY2).setFontColor('#ffffff').setFontWeight('bold').setFontSize(9);
  if (linhas.length) sh.getRange(2, 1, linhas.length, cab.length).setValues(linhas);
  const filtro = sh.getFilter();
  if (filtro) filtro.remove();
  if (linhas.length) sh.getRange(1, 1, linhas.length + 1, cab.length).createFilter();
  sh.setTabColor('#6c7785');
  return linhas.length;
}


/**
 * Varre as abas de ano e devolve duas tabelas:
 *   Base · Projetos      — uma linha por projeto
 *   Base · Recebimentos  — uma linha por pagamento, com data de verdade
 *
 * A linha divisória de mês é reconhecida pelo nome do mês na coluna A. Ela não
 * vira linha de dado: vira o mês de competência das linhas que vêm abaixo dela.
 */
function basesProjetosERecebimentos_(ss) {
  const projetos = [], recebimentos = [], puladas = [];

  ANOS.forEach(function (ano) {
    const sh = ss.getSheetByName(ano);
    if (!sh) return;
    const fim = sh.getLastRow();
    if (fim < LIN_ITEM0) return;

    const n = fim - LIN_ITEM0 + 1;
    const vals = sh.getRange(LIN_ITEM0, 1, n, 23).getValues();
    let mes = '';

    for (let i = 0; i < n; i++) {
      const L = vals[i];
      const a = String(L[0] || '').trim();
      if (!a) continue;

      const iMes = MESES.indexOf(a);
      if (iMes >= 0) { mes = a; continue; }        // divisória: só guarda o mês

      const investimento = Number(L[2]) || 0;
      const recebido = Number(L[4]) || 0;
      if (!investimento && !recebido) {
        // Linha com nome e sem dinheiro nenhum. Pode ser rascunho, pode ser
        // projeto digitado pela metade. Não entra na base, mas aparece no log:
        // linha que some calada é linha que ninguém conserta.
        puladas.push(ano + ' linha ' + (LIN_ITEM0 + i) + ': "' + a + '"');
        continue;
      }

      const cliente = a;
      const projeto = String(L[1] || '').trim();
      projetos.push([ano, mes, cliente, projeto, investimento,
                     recebido, Number(L[5]) || 0, Number(L[6]) || 0,
                     String(L[7] || '').trim(), String(L[3] || '').trim()]);

      C_BLOCOS.forEach(function (c0, k) {
        const valor = Number(L[c0 - 1]) || 0;
        if (!valor) return;
        const data = L[c0];                         // coluna seguinte
        const desc = String(L[c0 + 1] || '').trim();
        const ehData = data instanceof Date;
        recebimentos.push([
          ano, cliente, projeto, k + 1, valor,
          ehData ? data : '',
          ehData ? data.getFullYear() : '',
          ehData ? MESES[data.getMonth()] : '',
          ehData ? Utilities.formatDate(data, Session.getScriptTimeZone(), 'yyyy-MM') : '',
          desc || (ehData ? '' : String(data || '').trim()),
        ]);
      });
    }
  });

  escreverTabela_(ss, 'Base · Projetos',
    ['Ano', 'Mês da venda', 'Cliente', 'Projeto', 'Investimento', 'Recebido',
     'Saldo a receber', '% recebido', 'Situação', 'Forma de pagamento'], projetos);

  escreverTabela_(ss, 'Base · Recebimentos',
    ['Ano do contrato', 'Cliente', 'Projeto', 'Nº do pagamento', 'Valor', 'Data',
     'Ano', 'Mês', 'Competência', 'Descrição'], recebimentos);

  if (puladas.length) {
    console.log('  linhas com nome e sem valor, fora da base:');
    puladas.forEach(function (t) { console.log('    ' + t); });
  }
  return { projetos: projetos.length, recebimentos: recebimentos.length };
}


/**
 * Só os cinco totais da aba Custo Fixo. Nome e salário de ninguém.
 *
 * É de propósito: o Looker lê a aba inteira que a gente apontar para ele, e a
 * Custo Fixo tem uma linha por pessoa. Apontar o painel do Walton para lá
 * colocaria a folha inteira dentro da fonte de dados do relatório. Aqui só
 * atravessam os agregados.
 */
function baseCustoFixo_(ss) {
  const sh = ss.getSheetByName('Custo Fixo');
  if (!sh) { console.log('aviso: aba "Custo Fixo" não encontrada.'); return 0; }

  const ALVOS = [
    ['TOTAL DA FOLHA', 'Folha de pagamento', 'Custo fixo'],
    ['TOTAL DA ESTRUTURA', 'Estrutura', 'Custo fixo'],
    ['TOTAL DOS INVESTIMENTOS', 'Investimentos', 'Investimento'],
    ['CUSTO FIXO OPERACIONAL', 'Custo operacional · folha + estrutura', 'Total'],
    ['COM INVESTIMENTOS', 'Custo total · com investimentos', 'Total'],
  ];
  const fim = sh.getLastRow();
  const rot = sh.getRange(1, 1, fim, 1).getDisplayValues();
  const val = sh.getRange(1, 8, fim, 1).getValues();

  const linhas = [];
  ALVOS.forEach(function (alvo) {
    for (let r = 0; r < fim; r++) {
      if (String(rot[r][0] || '').trim().toUpperCase().indexOf(alvo[0]) === 0) {
        linhas.push([alvo[1], alvo[2], Number(val[r][0]) || 0, new Date()]);
        return;
      }
    }
    console.log('aviso: não achei "' + alvo[0] + '" na aba Custo Fixo.');
  });

  return escreverTabela_(ss, 'Base · Custo Fixo',
    ['Indicador', 'Grupo', 'Valor', 'Atualizado em'], linhas);
}


/**
 * Acrescenta a linha de GESTÃO TÉCNICA no bloco 4 de todas as fichas, e a
 * coluna correspondente no bloco 5.
 *
 * Gestão técnica é da mesma natureza da coordenação: uma pessoa por projeto,
 * percentual sobre a receita líquida. 0,5%. A diferença é onde mora o nome —
 * o da coordenação está na identificação, no topo da ficha, e o da gestão
 * técnica fica na própria linha da comissão, coluna H. A identificação não tem
 * campo livre, e nome colado na comissão que ele gera é mais difícil de
 * esquecer de preencher.
 *
 * RODE QUANTAS VEZES PRECISAR. A função confere ficha por ficha se a linha já
 * existe e pula as que já têm. Se o Google interromper no meio por tempo —
 * são dezoito fichas e muita mesclagem —, é só rodar de novo: ela continua
 * de onde parou.
 */
function adicionarGestaoTecnica() {
  const ROSTER = EQUIPE_FICHA.concat(PROJETISTAS_FICHA).concat(GESTORES_FICHA);
  const regra = SpreadsheetApp.newDataValidation()
    .requireValueInList(ROSTER, true).setAllowInvalid(true)
    .setHelpText('Quem faz a gestão técnica deste projeto.').build();

  const ss = SpreadsheetApp.openById(ID_CUSTO);
  // SEM ISTO AS FÓRMULAS NASCEM QUEBRADAS. A planilha é pt_BR e quer ponto e
  // vírgula; o Apps Script grava o texto cru. Toda função que escreve fórmula
  // tem de calibrar antes — esqueci numa e a ficha inteira virou #ERROR!.
  calibrar_(ss);
  const FIXAS = ['Instruções', FICHA.painel, 'Listas', FICHA.base];
  let feitas = 0, refeitas = 0;

  ss.getSheets().forEach(function (sh) {
    const nome = sh.getName();
    if (FIXAS.indexOf(nome) >= 0) return;

    // ── acha a linha da coordenação; é por ela que a ficha se reconhece ──
    let rc = 0;
    const rot = sh.getRange(50, 1, 40, 1).getDisplayValues();
    for (let i = 0; i < rot.length; i++) {
      if (String(rot[i][0] || '').indexOf('Coordenação de produção') === 0) { rc = 50 + i; break; }
    }
    if (!rc) { console.log('pulei "' + nome + '": não achei a linha de coordenação.'); return; }

    // Se a linha já existe, as fórmulas são reescritas assim mesmo. É de
    // propósito: a primeira versão desta função gravou fórmula com o separador
    // errado e deixou as fichas em #ERROR!. Função que só sabe criar não
    // conserta o que ela própria estragou.
    const jaTem = String(sh.getRange(rc + 1, 1).getDisplayValue() || '')
                    .indexOf('Gestão técnica') === 0;
    const g = rc + 1;

    if (!jaTem) {
      sh.insertRowAfter(rc);
      sh.getRange(g, 1, 1, 15).breakApart();
      sh.getRange(g, 5, 1, 2).merge();
      sh.getRange(g, 8, 1, 8).merge();
      sh.getRange(g, 1).setValue('Gestão técnica');
    }
    // O percentual NÃO é escrito por aqui. A célula nasce vazia, com o formato
    // de percentual e nada dentro: quem decide o número é quem gerencia, e
    // valor que o script inventa é valor que ninguém confere.
    sh.getRange(g, 2).setNumberFormat('0.0%');
    posF_(sh.getRange(g, 3), '=IF($B' + g + '="","",ROUND($B' + g + '*$C$45,2))');
    posF_(sh.getRange(g, 4), '=IF($B' + g + '="","",ROUND($B' + g + '*$D$45,2))');
    posF_(sh.getRange(g, 5), '=IF(OR($C' + g + '="",$D' + g + '=""),"",ROUND($D' + g + '-$C' + g + ',2))');
    posF_(sh.getRange(g, 7), '=IF(OR($D' + g + '="",$A$13="",$A$13=0),"",$D' + g + '/$A$13)');
    sh.getRange(g, 3, 1, 3).setNumberFormat(MOEDA);
    sh.getRange(g, 7).setNumberFormat('0.0%');
    sh.getRange(g, 8).setDataValidation(regra)
      .setHorizontalAlignment('left').setFontWeight('bold').setFontColor(NAVY2);

    // ── 2 · bloco 5 passa a somar a gestão junto da coordenação ──
    //
    // Uma coluna só, e não uma coluna nova: a ficha tem quinze colunas fixas e
    // abrir mais uma empurraria o bloco inteiro. Na mesma linha nunca há os
    // dois — quem coordena não é quem faz gestão técnica —, então somar na
    // mesma casa não mistura dinheiro de gente diferente.
    let rh = 0;
    const rot2 = sh.getRange(g, 1, 30, 1).getDisplayValues();
    for (let i = 0; i < rot2.length; i++) {
      if (String(rot2[i][0] || '').trim() === 'Colaborador') { rh = g + i; break; }
    }
    if (!rh) {
      console.log('aviso: "' + nome + '" tem a linha, mas não achei o bloco 5.');
      if (jaTem) { refeitas++; } else { feitas++; }
      return;
    }

    sh.getRange(rh, 8).setValue('Coordenação / Gestão técnica (R$)').setWrap(true);
    for (let r = rh + 1; r < rh + 30; r++) {
      const quem = String(sh.getRange(r, 1).getDisplayValue() || '').trim();
      if (quem === 'TOTAL') break;
      if (!quem) continue;
      posF_(sh.getRange(r, 8),
        '=IF($A' + r + '="","",IF($A' + r + '=$F$9,IF($D$' + rc + '="",0,$D$' + rc + '),0)'
        + '+IF($A' + r + '=$H$' + g + ',IF($D$' + g + '="",0,$D$' + g + '),0))');
    }
    if (jaTem) { refeitas++; } else { feitas++; }
  });

  SpreadsheetApp.flush();
  const r = feitas + ' ficha(s) com a linha nova, ' + refeitas + ' com as fórmulas refeitas';
  console.log('Gestão técnica: ' + r);
  return r;
}


/**
 * Põe o menu de vendedor na célula certa, em todas as fichas.
 *
 * O gerador pendurou a lista de vendedores em D7, que é "Nº do projeto", em
 * vez de D9, que é "Vendedor". Resultado: o campo errado tinha menu e o certo
 * não tinha nenhum. Esta função tira de lá e põe aqui, na Ficha Modelo e em
 * todas as abas de projeto.
 *
 * Não apaga conteúdo. Se alguém digitou alguma coisa em D7 ou D9, o texto
 * continua: só a regra de validação muda.
 */
function corrigirMenuVendedor() {
  const VENDEDORES = ['Jonathan', 'Vitor', 'Indicação', 'Arquiteto parceiro', 'Outro'];
  const FIXAS = ['Instruções', FICHA.painel, 'Listas', FICHA.base];

  const ss = SpreadsheetApp.openById(ID_CUSTO);
  const regra = SpreadsheetApp.newDataValidation()
    .requireValueInList(VENDEDORES, true)
    .setAllowInvalid(true)          // nome fora da lista avisa, não bloqueia
    .setHelpText('Quem vendeu este projeto.')
    .build();

  let n = 0;
  ss.getSheets().forEach(function (sh) {
    const nome = sh.getName();
    if (FIXAS.indexOf(nome) >= 0) return;
    if (sh.getMaxRows() < 9 || sh.getMaxColumns() < 5) return;

    // confere que é mesmo uma ficha antes de mexer
    const rotulo = String(sh.getRange('A8').getDisplayValue() || '').trim().toUpperCase();
    if (rotulo.indexOf('PROJETO') !== 0) {
      console.log('pulei "' + nome + '": A8 diz "' + rotulo + '", não parece ficha.');
      return;
    }

    sh.getRange('D7:E7').clearDataValidations();
    sh.getRange('D9:E9').setDataValidation(regra);
    n++;
  });

  SpreadsheetApp.flush();
  console.log('menu de vendedor corrigido em ' + n + ' ficha(s), incluindo a Ficha Modelo.');
  console.log('D7 voltou a ser campo livre (Nº do projeto). D9 agora tem a lista: '
              + VENDEDORES.join(', ') + '.');
}


/**
 * CONFERE TUDO. Não escreve nada, não cria aba, não apaga nada.
 *
 * Existe porque descobrir defeito por print de tela é caro: a planilha já está
 * errada quando alguém percebe. Esta função percorre a cadeia inteira — ficha,
 * Base, planilhas individuais, bases do painel, painel do Walton — e devolve
 * uma lista de ok e FALHA no Registro de execução.
 *
 * Rode ANTES e DEPOIS de qualquer atualizarTudo. Antes, para saber de onde se
 * está partindo; depois, para saber o que mudou.
 */
function validar() {
  const L = [];
  let n = 0, mau = 0;
  const diz = function (t) { L.push(t); console.log(t); };
  const ok = function (t, cond, det) {
    n++;
    if (!cond) mau++;
    diz((cond ? '  ok    ' : '  FALHA ') + t + (det ? '   ·   ' + det : ''));
  };
  const ERRO = /^#(ERROR|REF|VALUE|NAME|DIV|N\/A|NUM|NULL)/;
  const conta = function (vals) {
    let c = 0;
    vals.forEach(function (lin) {
      lin.forEach(function (v) { if (ERRO.test(String(v))) c++; });
    });
    return c;
  };

  diz('════ CUSTO POR PROJETO ════');
  const cp = SpreadsheetApp.openById(ID_CUSTO);
  const FIXAS = ['Instruções', FICHA.painel, 'Ficha Modelo', 'Listas', FICHA.base];
  const fichas = cp.getSheets().map(function (s) { return s.getName(); })
                   .filter(function (x) { return FIXAS.indexOf(x) < 0; });

  const pg = cp.getSheetByName(FICHA.painel);
  const reg = !pg ? [] : pg.getRange(FICHA.pg0, 2, FICHA.pgf - FICHA.pg0 + 1, 1).getDisplayValues()
                .map(function (r) { return String(r[0] || ''); })
                .filter(function (x) { return x !== ''; });
  // Registro que não casa com aba nenhuma. Costuma ser nome digitado com outra
  // caixa ou espaço — getSheetByName é literal, "luiz" não é "Luiz ". O script
  // nunca apaga registro, então sai pela mão de quem lê este log.
  const orfaos = reg.filter(function (x) { return fichas.indexOf(x) < 0; });
  ok(pg ? 'Painel Geral registra todas as fichas, e só elas'
        : 'Painel Geral saiu daqui, e a Base não depende dele',
     !pg || (reg.length === fichas.length && orfaos.length === 0),
     reg.length + ' registro(s) para ' + fichas.length + ' aba(s)'
     + (orfaos.length ? ' · sobrando: ' + orfaos.map(function (x) {
         return '"' + x + '"'; }).join(' | ') + ' — apague essas células do Painel Geral'
       : ''));
  const faltam = fichas.filter(function (f) { return reg.indexOf(f) < 0; });
  ok('nenhuma ficha fora do Painel Geral', faltam.length === 0, faltam.join(' | '));

  // ── Base · Comissões ──
  const base = cp.getSheetByName(FICHA.base);
  ok('Base · Comissões tem ' + FICHA.colsBase + ' colunas',
     base.getLastColumn() === FICHA.colsBase, 'achei ' + base.getLastColumn());
  const bv = base.getRange(2, 1, Math.max(1, base.getLastRow() - 1), base.getLastColumn())
                 .getDisplayValues();
  ok('Base sem célula de erro', conta(bv) === 0, conta(bv) + ' célula(s)');

  // ── dinheiro sem dono, lido da Base ──
  let semDono = 0, qtdSemDono = 0;
  const FRENTES = [[5, 7, 'produção'], [9, 11, 'montagem'], [13, 15, 'projeto'],
                   [18, 19, 'coordenação'], [29, 30, 'gestão técnica'],
                   [31, 32, 'venda']];
  const porFrente = {}, porProjeto = {};
  const bn = base.getRange(2, 1, Math.max(1, base.getLastRow() - 1), base.getLastColumn())
                 .getValues();
  bn.forEach(function (r) {
    FRENTES.forEach(function (f) {
      const quem = String(r[f[0]] || '').trim();
      const val = Number(r[f[1]]) || 0;
      if (val <= 0 || quem) return;
      semDono += val;
      qtdSemDono++;
      if (!porFrente[f[2]]) porFrente[f[2]] = { v: 0, n: 0 };
      porFrente[f[2]].v += val;
      porFrente[f[2]].n++;
      const proj = String(r[0] || '').trim() || '(sem projeto)';
      porProjeto[proj] = (porProjeto[proj] || 0) + val;
    });
  });
  ok('toda comissão tem dono', qtdSemDono === 0,
     qtdSemDono + ' lançamento(s), R$ ' + semDono.toFixed(2));

  // Saber que há dinheiro sem dono não resolve nada. Saber em qual frente e em
  // qual projeto é o que faz alguém levantar e ir preencher.
  if (qtdSemDono) {
    FRENTES.forEach(function (f) {
      const x = porFrente[f[2]];
      if (x) diz('          · ' + f[2] + ': R$ ' + x.v.toFixed(2)
                 + '  em ' + x.n + ' lançamento(s)');
    });
    const piores = Object.keys(porProjeto)
      .sort(function (a, b) { return porProjeto[b] - porProjeto[a]; }).slice(0, 5);
    diz('          · onde mais dói: '
        + piores.map(function (p) { return p + ' R$ ' + porProjeto[p].toFixed(2); }).join('  |  '));
  }

  // ── ficha por ficha ──
  let semGestao = [], comErro = [], ambDifere = [], semCampoComp = [], semMes = [];
  fichas.concat(['Ficha Modelo']).forEach(function (nome) {
    const sh = cp.getSheetByName(nome);
    if (!sh || sh.getLastRow() < 70) { comErro.push(nome + ' (curta demais)'); return; }
    const rot = String(sh.getRange('A66').getDisplayValue() || '');
    if (rot.indexOf('Gestão técnica') !== 0) semGestao.push(nome);
    if (String(sh.getRange('A10').getDisplayValue() || '').indexOf('MÊS DE COMPETÊNCIA') !== 0) {
      semCampoComp.push(nome.trim());
    } else if (!String(sh.getRange('D10').getDisplayValue() || '').trim()
               && nome !== 'Ficha Modelo') {
      semMes.push(nome.trim());
    }
    const chave = sh.getRange('A13:A13').getDisplayValues()
      .concat(sh.getRange('D22:D23').getDisplayValues())
      .concat(sh.getRange('D45:D45').getDisplayValues())
      .concat(sh.getRange('D65:D66').getDisplayValues())
      .concat(sh.getRange('D70:D70').getDisplayValues());
    if (conta(chave) > 0) comErro.push(nome);
    const venda = Number(sh.getRange('A13').getValue()) || 0;
    const soma = Number(sh.getRange('C61').getValue()) || 0;
    if (venda > 0 && soma > 0 && Math.abs(venda - soma) > 1) {
      const d = soma - venda;
      ambDifere.push(nome.trim() + ': ' + (d < 0 ? 'faltam R$ ' + (-d).toFixed(2)
                                                 : 'sobram R$ ' + d.toFixed(2)));
    }
  });
  ok('todas as fichas têm a linha de gestão técnica', semGestao.length === 0,
     semGestao.join(' | '));
  ok('todas as fichas têm o campo de competência', semCampoComp.length === 0,
     semCampoComp.join(' | '));
  ok('projeto entregue tem competência', semMes.length === 0,
     semMes.length + ' sem entrega real, logo sem competência: ' + semMes.join(' | '));
  ok('nenhuma ficha com erro nas células-chave', comErro.length === 0, comErro.join(' | '));
  ok('ambientes somam o valor de venda', ambDifere.length === 0, ambDifere.join(' | '));

  diz('');
  diz('════ CONTROLE DE PAGAMENTOS ════');
  const pgto = SpreadsheetApp.openById(ID_PAG);
  [['Base · Projetos', 10], ['Base · Recebimentos', 10], ['Base · Custo Fixo', 4]]
    .forEach(function (b) {
      const sh = pgto.getSheetByName(b[0]);
      ok(b[0] + ' existe e tem linha', !!sh && sh.getLastRow() > 1,
         sh ? (sh.getLastRow() - 1) + ' linha(s)' : 'aba ausente');
      if (sh) ok(b[0] + ' com ' + b[1] + ' colunas', sh.getLastColumn() === b[1],
                 'achei ' + sh.getLastColumn());
    });
  const cf = pgto.getSheetByName('Base · Custo Fixo');
  if (cf && cf.getLastRow() > 1) {
    const v = cf.getRange(2, 3, cf.getLastRow() - 1, 1).getValues();
    const zerados = v.filter(function (x) { return !Number(x[0]); }).length;
    ok('custo fixo sem total zerado', zerados === 0, zerados + ' zerado(s)');
  }

  diz('');
  diz('════ PLANILHAS INDIVIDUAIS ════');
  PESSOAS.forEach(function (p) {
    const ss = SpreadsheetApp.openById(p.id);
    const sh = ss.getSheetByName('Comissões');
    if (!sh) { ok(p.nome, false, 'aba Comissões não encontrada'); return; }

    const esperado = layout_(p).map(function (c) { return c.t; });
    const achado = sh.getRange(3, 1, 1, sh.getLastColumn()).getDisplayValues()[0]
                     .map(function (x) { return String(x).trim(); });
    const igual = esperado.length === achado.length
      && esperado.every(function (t, i) { return t === achado[i]; });

    const bs = ss.getSheetByName('_base');
    const imp = bs ? bs.getRange('A1').getFormula() : '';
    const faixaOk = imp.indexOf('A1:AL') > 0;
    const dado = bs ? conta(bs.getRange('A2:B3').getDisplayValues()) === 0 : false;
    const pa = ss.getSheetByName('Painel');
    const erroPainel = pa ? conta(pa.getRange(5, 2, 26, 6).getDisplayValues()) : 99;

    ok(p.nome + ' · colunas conferem com o perfil "' + p.perfil + '"', igual,
       igual ? '' : 'esperado ' + esperado.length + ', achei ' + achado.length);
    ok(p.nome + ' · IMPORTRANGE vai até AL', faixaOk, imp ? '' : 'sem _base');
    ok(p.nome + ' · a Base chega sem erro', dado);
    ok(p.nome + ' · Painel sem célula de erro', erroPainel === 0, erroPainel + ' célula(s)');
  });

  diz('');
  diz('════ ANÁLISE MENSAL ════');
  const pn = SpreadsheetApp.openById(ID_PAINEL);
  const pam = pgto.getSheetByName('Análise mensal');
  ok('Análise mensal existe', !!pam);
  if (pam) {
    const e = conta(pam.getRange(1, 1, Math.min(pam.getLastRow(), 200),
                                 Math.max(1, pam.getLastColumn())).getDisplayValues());
    ok('Análise mensal sem célula de erro', e === 0, e + ' célula(s)');
  }
  ok('as duas abas antigas foram embora',
     !pgto.getSheetByName('Painel de Competência') && !pgto.getSheetByName('Produção e Entrega'));

  diz('');
  diz('════ PAINEL DE GESTÃO ════');
  ['Visão geral', 'Margem por projeto', 'Comissões', 'Equipe', 'Como ler']
    .forEach(function (aba) {
      const sh = pn.getSheetByName(aba);
      if (!sh) { ok('aba ' + aba, false, 'não existe'); return; }
      const e = conta(sh.getRange(1, 1, Math.min(sh.getLastRow(), 60),
                                  Math.max(1, sh.getLastColumn())).getDisplayValues());
      ok('aba ' + aba + ' sem erro', e === 0, e + ' célula(s)');
    });

  diz('');
  diz('════ ' + n + ' verificações · ' + mau + ' falha(s) ════');
  if (!mau) diz('Pode apresentar.');
  return L.join('\n');
}


/**
 * SÓ LÊ. Não escreve nada, não apaga nada, não altera uma célula sequer.
 *
 * Mostra no Registro de execução o que está de fato dentro das células do
 * Samuel: a fórmula escrita e o que o Google devolveu. É assim que se acha a
 * origem de um #ERROR! — olhando a célula de origem, não a que exibe o erro.
 */
function diagnostico() {
  const NOME = 'Lorrane';          // troque aqui para olhar outra pessoa
  let p = null;
  PESSOAS.forEach(function (x) { if (x.nome === NOME) p = x; });
  if (!p) { console.log('Não existe ' + NOME + ' na lista.'); return; }

  const ss = SpreadsheetApp.openById(p.id);
  console.log('=== ' + NOME + ' · ' + p.perfil + ' · ' + (p.pj ? 'PJ' : 'CLT') + ' ===');
  console.log('abas: ' + ss.getSheets().map(function (s) { return s.getName(); }).join(' | '));

  // ── Comissões: cabeçalho e a primeira linha ──
  const sh = ss.getSheetByName('Comissões');
  const nc = sh.getLastColumn();
  const cab = sh.getRange(3, 1, 1, nc).getDisplayValues()[0];
  console.log('\nComissões · ' + nc + ' colunas:');
  cab.forEach(function (t, i) {
    console.log('   ' + colLetra_(i + 1) + ' = ' + t);
  });
  console.log('\nlinha 4, o que está digitado nas colunas manuais:');
  cab.forEach(function (t, i) {
    if (/^(Pagamento|Status|Repassado|Observa)/.test(String(t))) {
      const c = sh.getRange(4, i + 1);
      console.log('   ' + colLetra_(i + 1) + ' ' + t + ' = ' + JSON.stringify(c.getDisplayValue())
                  + '   (tipo: ' + (c.getValue() instanceof Date ? 'DATA' : typeof c.getValue()) + ')');
    }
  });

  // ── Painel: linha a linha, do 5 em diante ──
  const pa = ss.getSheetByName('Painel');
  console.log('\nPainel, linhas 5 a 30:');
  for (let r = 5; r <= 30; r++) {
    const vs = pa.getRange(r, 2, 1, 6).getDisplayValues()[0];
    if (vs.join('').trim() === '') continue;
    console.log('   ' + (r < 10 ? ' ' : '') + r + ' | ' + vs.join(' | '));
  }

  // ── a fórmula do primeiro mês, seja qual for a linha ──
  for (let r = 5; r <= 30; r++) {
    if (String(pa.getRange(r, 2).getDisplayValue()).trim() === 'Janeiro') {
      console.log('\nJaneiro está na linha ' + r + '. Fórmulas:');
      for (let c = 3; c <= 7; c++) {
        console.log('   ' + colLetra_(c) + r + '  ' + (pa.getRange(r, c).getFormula() || '(vazia)'));
      }
      break;
    }
  }
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
    diz('Estrutura: ' + garantirEstrutura_());
  } catch (e) {
    diz('Estrutura: FALHOU — ' + e.message);
  }
  try {
    diz('Painel Geral: ' + repararPainelGeral_() + ' projeto(s)');
    diz('Base · Comissões: ' + atualizarBase_() + ' projeto(s), '
      + FICHA.colsBase + ' colunas');
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

  try {
    diz('Bases do painel: ' + montarBasesDoPainel());
  } catch (e) {
    diz('Bases do painel: FALHOU — ' + e.message);
  }

  try {
    diz('Painel de Gestão: ' + montarPainelGestao());
  } catch (e) {
    diz('Painel de Gestão: FALHOU — ' + e.message);
  }

  try {
    diz('Gestão 2026 · ' + migrarParaGestao2026());
    diz('Gestão 2026 · Clientes: ' + abaClientes_());
    diz('Gestão 2026 · Painel Geral: ' + abaPainelGeralG26_());
    diz('Gestão 2026 · Análise mensal: ' + abaAnaliseMensal_());
  } catch (e) {
    diz('Gestão 2026: FALHOU — ' + e.message);
  }

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
  // A Base não depende mais deste registro. Se a aba foi embora para a
  // Gestão 2026, não há nada a reparar e nada quebra por isso.
  if (!pg) return 'aba não existe mais aqui — a Base não depende dela';
  const FIXAS = ['Instruções', FICHA.painel, 'Ficha Modelo', 'Listas', FICHA.base];
  const abas = ss.getSheets().map(function (sh) { return sh.getName(); })
                 .filter(function (n) { return FIXAS.indexOf(n) < 0; });

  const n = FICHA.pgf - FICHA.pg0 + 1;
  const atual = pg.getRange(FICHA.pg0, 2, n, 1).getValues()
                  .map(function (r) { return String(r[0] || ''); });

  // SÓ ACRESCENTA. Nunca apaga, nunca troca o que já está escrito — nem o que
  // parece sobra. O que estiver lá é de alguém, e a versão que apagava já
  // destruiu dez registros uma vez.
  const jaEstao = {};
  atual.forEach(function (v) { if (v) jaEstao[v] = true; });

  let escritas = 0;
  abas.forEach(function (aba) {
    if (jaEstao[aba]) return;
    for (let i = 0; i < n; i++) {
      if (atual[i] === '') {
        pg.getRange(FICHA.pg0 + i, 2).setValue(aba);
        atual[i] = aba;
        jaEstao[aba] = true;
        escritas++;
        return;
      }
    }
    console.log('  aviso: sem vaga livre no Painel Geral para "' + aba + '".');
  });

  const orfaos = atual.filter(function (v) {
    return v && abas.indexOf(v) < 0;
  });
  if (orfaos.length) {
    console.log('  aviso: registrado no Painel Geral sem aba correspondente, '
                + 'e deixado como está: ' + orfaos.join(' | '));
  }

  SpreadsheetApp.flush();
  return atual.filter(function (v) { return v !== ''; }).length
         + (escritas ? ' (' + escritas + ' acrescentado[s])' : '');
}


function atualizarBase_() {
  const ss = SpreadsheetApp.openById(ID_CUSTO);
  console.log('  separador desta planilha: "' + calibrar_(ss) + '"');
  const base = ss.getSheetByName(FICHA.base);

  const CAB = ['Projeto', 'Cliente', 'Ambiente', '% do total', 'Valor do ambiente',
    'Produção — quem', '% produção', 'Comissão produção', 'Fabricado em',
    'Montagem — quem', '% montagem', 'Comissão montagem', 'Montado em',
    'Projetista — quem', '% projeto', 'Comissão projetista', 'Total do ambiente',
    'Data de entrada', 'Coordenador', 'Comissão coordenação',
    'Receita líquida do projeto', 'Valor de venda',
    'Imposto %', 'Taxa de máquina %', 'RT %', 'Comissão do vendedor %',
    'Custos de venda',
    'Custo total do projeto', 'Margem de contribuição',
    'Gestor técnico', 'Comissão gestão técnica',
    // sem o nome do vendedor não existe categoria "vendedores" no painel
    'Vendedor', 'Comissão de venda',
    // o mês em que o projeto pesa, e como ele está de entrega
    'Competência', 'Situação da entrega',
    // nota emitida e o RT do parceiro, com o status do pagamento
    'Faturado', 'RT do parceiro', 'RT pago'];

  base.clear();
  base.getRange(1, 1, 1, CAB.length).setValues([CAB])
      .setBackground(NAVY2).setFontColor('#ffffff').setFontSize(8.5)
      .setFontWeight('bold').setWrap(true).setHorizontalAlignment('center');
  base.setFrozenRows(0);

  // SEM trim: dez abas têm espaço no fim do nome, e getSheetByName é literal.
  // E sem apagar nada do Painel Geral: se o nome não casar, apenas se registra
  // no log. Apagar registro foi o que destruiu a lista na primeira tentativa.
  // A Base é escrita a partir das ABAS que existem, não do que está escrito no
  // Painel Geral. Registro é coisa de quem lê; aba é coisa que existe.
  const FIXAS = ['Instruções', FICHA.painel, 'Ficha Modelo', 'Listas', FICHA.base];
  const abas = ss.getSheets().map(function (sh) { return sh.getName(); })
                 .filter(function (x) { return FIXAS.indexOf(x) < 0; });
  let n = 0;
  abas.forEach(function (nome, i) {
    if (i >= FICHA.pgf - FICHA.pg0 + 1) {
      console.log('  aviso: "' + nome + '" ficou de fora, a Base comporta '
                  + (FICHA.pgf - FICHA.pg0 + 1) + ' projetos.');
      return;
    }
    escreverBlocoBase_(base, i, nome);
    n++;
  });
  SpreadsheetApp.flush();
  return n;
}

function ref_(nome) { return "'" + String(nome).replace(/'/g, "''") + "'"; }

/**
 * Célula do projeto trazida para a base, com endereço absoluto.
 *
 * A guarda é o CLIENTE da ficha, não o ambiente da linha. Antes era o
 * ambiente, e por isso projeto com venda lançada e nenhum ambiente sumia dos
 * painéis inteiros — foi o caso da Carla Dresller, que tem entrega real, RT
 * de R$ 2.565 e não aparecia em lugar nenhum.
 */
function cel_(ab, end, r, texto) {
  const abs = '$' + end.charAt(0) + '$' + end.slice(1);
  return '=IF(' + ab + '!$A$7="","",IF(' + ab + '!' + abs + '="",' + (texto ? '""' : '0')
       + ',' + ab + '!' + abs + '))';
}

function escreverBlocoBase_(base, i, nomeAba) {
  const r0 = FICHA.base0 + i * FICHA.ambQtd;
  const pgL = FICHA.pg0 + i;
  const ab = ref_(nomeAba);
  const linhas = [];
  for (let j = 0; j < FICHA.ambQtd; j++) {
    const r = r0 + j, fr = FICHA.amb0 + j;
    // A primeira linha do bloco publica o projeto mesmo sem ambiente lançado:
    // basta haver cliente na ficha. As outras onze continuam presas ao ambiente.
    //
    // O nome do projeto é escrito como TEXTO, e o cliente vem da própria ficha.
    // Antes os dois vinham do Painel Geral, e essa dependência prendia o
    // Painel Geral dentro da Custo por Projeto: tirá-lo de lá quebrava a Base
    // inteira. Agora a Base se basta, e o Painel Geral pode morar onde for
    // mais útil de ler.
    const guarda = j === 0 ? ab + '!$A$7' : '$C' + r;
    const L = [
      '=IF(' + guarda + '="","","' + String(nomeAba).replace(/"/g, '""') + '")',
      '=IF(' + guarda + '="","",' + ab + '!$A$7)',
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
      // custo total e margem: é daqui que sai a MC por projeto no painel
      L.push(cel_(ab, FICHA.custoTotal, r, false));
      L.push(cel_(ab, FICHA.margem, r, false));
      L.push(cel_(ab, FICHA.gestorTecnico, r, true));
      L.push(cel_(ab, FICHA.comGestao, r, false));
      L.push(cel_(ab, FICHA.vendedorNome, r, true));
      L.push(cel_(ab, FICHA.comVenda, r, false));
      L.push(cel_(ab, FICHA.competencia, r, true));
      L.push(cel_(ab, FICHA.entregaSituacao, r, true));
      L.push(cel_(ab, FICHA.faturado, r, false));
      L.push(cel_(ab, FICHA.rtValor, r, false));
      L.push(cel_(ab, FICHA.rtStatus, r, true));
    } else {
      L.push('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '');
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

  // A fatia do projetista, medida do jeito que não mente.
  //
  // Valor de venda · sua parte é a SOMA DIRETA dos ambientes que levam o nome
  // dele. Nada de proporção para chegar nela: é o dinheiro dos ambientes dele.
  //
  // Participação é essa soma dividida pelo VALOR DE VENDA DO PROJETO — não
  // pela soma dos ambientes lançados. A primeira versão dividia pelos
  // ambientes lançados e, numa ficha com um ambiente de 20 mil num projeto de
  // 47 mil, esse único ambiente virava 100%: o projetista aparecia com o
  // projeto inteiro. A conta se protegia de ficha incompleta escondendo que a
  // ficha estava incompleta.
  //
  // Efeito colateral desejado: se a soma dos ambientes passar do valor de
  // venda, a Participação passa de 100% e fica à vista. Erro que aparece é
  // erro que se corrige.
  const COL_PART = 'C';   // Participação
  const COL_PARTE = 'D';  // Valor de venda · sua parte
  const COL_CUSTO = 'I';  // Custos de venda · sua parte

  const parteVenda = function (r) {
    return '=IF($A' + r + '="","",ROUND(SUMIFS('
      + '_base!$' + B.valor + '$2:$' + B.valor + '$' + BASE_FIM
      + ',_base!$' + B.projeto + '$2:$' + B.projeto + '$' + BASE_FIM + ',$A' + r
      + ',_base!$' + B.projQuem + '$2:$' + B.projQuem + '$' + BASE_FIM
      + ',"' + p.nome + '"),2))';
  };

  const participacao = function (r) {
    const lb = 2 + (r - LIN0) * FICHA.ambQtd;
    return '=IF($A' + r + '="","",IFERROR($' + COL_PARTE + r
      + '/_base!$' + B.venda + '$' + lb + ',0))';
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
      { t: 'Valor de venda · sua parte', w: 15, calc: true, nf: MOEDA, f: parteVenda },
      { t: 'Imposto %', w: 10, calc: true, nf: PCT, f: doProjeto('imposto') },
      { t: 'Taxa de máquina %', w: 11, calc: true, nf: PCT, f: doProjeto('maquina') },
      { t: 'RT %', w: 9, calc: true, nf: PCT, f: doProjeto('rt') },
      { t: 'Comissão do vendedor %', w: 11, calc: true, nf: PCT, f: doProjeto('vendedor') },
      { t: 'Custos de venda · sua parte', w: 15, calc: true, nf: MOEDA, f: fatia('custoVenda') },
      { t: 'Receita líquida · sua parte', w: 15, calc: true, nf: MOEDA, f: function (r) {
          // sua parte MENOS os custos da sua parte. A conta fecha na tela:
          // D − I = J. Antes era a líquida do projeto vezes a participação,
          // que dava o mesmo número mas obrigava a confiar na proporção em vez
          // de conferir subtraindo.
          return '=IF($A' + r + '="","",ROUND($' + COL_PARTE + r
            + '-$' + COL_CUSTO + r + ',2))'; } },
      { t: 'Comissão a receber', w: 15, calc: true, nf: MOEDA, total: true,
        f: soma('projCom', 'projQuem') },
    ]);
  } else if (p.perfil === 'gestao') {
    // Gestão técnica é por PROJETO, como a coordenação do Deivison: 0,5% da
    // receita líquida. Na Base ela vive na primeira linha do bloco de doze,
    // então o SUMIFS por projeto pega uma linha só e não multiplica por doze.
    //
    // A receita líquida aparece porque é a base do cálculo. Comissão que a
    // pessoa não consegue conferir sozinha é comissão que gera desconfiança.
    cols = cols.concat([
      { t: 'Receita líquida do projeto', w: 16, calc: true, nf: MOEDA, f: doProjeto('liquido') },
      { t: 'Gestão técnica · a receber', w: 16, calc: true, nf: MOEDA, total: true,
        f: soma('gestCom', 'gestQuem') },
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
    const nova = atual.replace(/!A1:[A-Z]+\d+/, '!A1:AL' + BASE_FIM);
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
  const tudo = sh.getRange(1, 1, sh.getMaxRows(), sh.getMaxColumns());
  tudo.breakApart();
  tudo.clear();
  // clear() leva conteúdo e formato, mas NÃO leva validação de dados. Sem esta
  // linha a lista "Em aberto / Pago" ficava grudada na coluna onde o Status
  // morava no layout anterior, enquanto o cabeçalho andava para o lado.
  tudo.clearDataValidations();
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
  // nada congelado, por decisão: congelamento quebra mesclagem e atrapalha no celular
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

  const C = "'Comissões'!";
  const A = "'Avulsos'!";
  const temAvulso = !!ss.getSheetByName('Avulsos');
  const p0 = LIN0, pf = LIN0 + N_PROJ - 1;

  const cCom = C + '$' + LT + '$' + p0 + ':$' + LT + '$' + pf;   // valor
  const cSt  = C + '$' + LS + '$' + p0 + ':$' + LS + '$' + pf;   // status
  const cDt  = C + '$' + LP + '$' + p0 + ':$' + LP + '$' + pf;   // data combinada
  const aVal = A + '$C$' + AV0 + ':$C$' + AVF;
  const aDt  = A + '$D$' + AV0 + ':$D$' + AVF;
  const aSt  = A + '$E$' + AV0 + ':$E$' + AVF;

  // Linhas 1 a 3 (título, subtítulo e o aviso de autorização) ficam como estão.
  // Daí para baixo é tudo fórmula e rótulo, nada digitado — pode ser refeito.
  if (pa.getMaxRows() < 40) pa.insertRowsAfter(pa.getMaxRows(), 40 - pa.getMaxRows());
  if (pa.getMaxColumns() < 8) pa.insertColumnsAfter(pa.getMaxColumns(), 8 - pa.getMaxColumns());
  pa.setFrozenRows(0);
  const corpo = pa.getRange(5, 1, pa.getMaxRows() - 4, pa.getMaxColumns());
  corpo.breakApart();
  corpo.clear();
  corpo.clearDataValidations();
  pa.clearConditionalFormatRules();

  const faixa = function (lin, texto) {
    pa.getRange(lin, 2, 1, 7).merge().setValue('  ' + texto)
      .setBackground(GOLDBG).setFontColor(NAVY2).setFontSize(10).setFontWeight('bold')
      .setVerticalAlignment('middle');
    pa.setRowHeight(lin, 20);
  };

  // três cartões lado a lado: C+D, E+F, G+H
  const cartoes = function (lin, itens) {
    itens.forEach(function (it, i) {
      const c0 = 3 + i * 2;
      pa.getRange(lin, c0, 1, 2).merge().setValue(it[0])
        .setFontColor(MUTED).setFontSize(9).setFontWeight('bold');
      pa.getRange(lin + 1, c0, 1, 2).merge();
      posF_(pa.getRange(lin + 1, c0), it[1]);
      pa.getRange(lin + 1, c0).setNumberFormat(MOEDA)
        .setFontColor(it[2]).setFontSize(16).setFontWeight('bold');
    });
    pa.setRowHeight(lin + 1, 26);
  };

  // ── comissões ──
  faixa(5, 'COMISSÕES   ·   pelo que está lançado na Custo por Projeto');
  cartoes(6, [
    ['No ano', '=ROUND(SUM(' + cCom + '),2)', NAVY],
    ['Já paga', '=ROUND(SUMIF(' + cSt + ',"Pago",' + cCom + '),2)', OK],
    ['A receber', '=ROUND($C$7-$E$7,2)', ABERTO],
  ]);

  // ── avulsos ──
  let L = 9;
  if (temAvulso) {
    faixa(9, 'AVULSOS   ·   o que você lançou na aba Avulsos');
    cartoes(10, [
      ['No ano', '=ROUND(SUM(' + aVal + '),2)', NAVY],
      ['Já pago', '=ROUND(SUMIF(' + aSt + ',"Pago",' + aVal + '),2)', OK],
      ['A receber', '=ROUND($C$11-$E$11,2)', ABERTO],
    ]);
    L = 13;
  }

  // ── total a receber ──
  pa.getRange(L, 2, 1, 2).merge().setValue('  A RECEBER   ·   TOTAL')
    .setBackground(NAVY).setFontColor(GOLDS).setFontSize(11).setFontWeight('bold')
    .setVerticalAlignment('middle');
  pa.getRange(L, 4, 1, 4).merge();
  posF_(pa.getRange(L, 4), temAvulso ? '=ROUND($G$7+$G$11,2)' : '=ROUND($G$7,2)');
  pa.getRange(L, 4).setNumberFormat(MOEDA).setBackground(NAVY).setFontColor(GOLDS)
    .setFontSize(18).setFontWeight('bold').setHorizontalAlignment('right')
    .setVerticalAlignment('middle');
  pa.setRowHeight(L, 34);

  // ── mês a mês ──
  const lm = L + 2;
  faixa(lm, 'MÊS A MÊS   ·   pela data combinada de pagamento');
  // Quem não tem aba de Avulsos não ganha a coluna de Avulsos: coluna que só
  // pode dar zero é ruído. Para esses, a de Comissões já é o total.
  const cab = temAvulso
    ? ['Mês', 'Comissões', 'Avulsos', 'Total', 'Já pago', 'A receber']
    : ['Mês', 'Comissões', 'Já pago', 'A receber'];
  const nc = cab.length;
  pa.getRange(lm + 1, 2, 1, nc).setValues([cab])
    .setBackground(NAVY).setFontColor(GOLDS).setFontSize(9).setFontWeight('bold')
    .setHorizontalAlignment('center');

  for (let m = 0; m < 12; m++) {
    const r = lm + 2 + m;
    const ini = 'DATE(YEAR(TODAY()),' + (m + 1) + ',1)';
    const fim = 'EOMONTH(DATE(YEAR(TODAY()),' + (m + 1) + ',1),0)';
    const noMes = function (val, dt) {
      return 'SUMIFS(' + val + ',' + dt + ',">="&' + ini + ',' + dt + ',"<="&' + fim + ')';
    };
    const pagoNoMes = function (val, dt, st) {
      return 'SUMIFS(' + val + ',' + dt + ',">="&' + ini + ',' + dt + ',"<="&' + fim
             + ',' + st + ',"Pago")';
    };
    pa.getRange(r, 2).setValue(MESES[m])
      .setFontColor(NAVY2).setFontSize(10).setFontWeight('bold');
    posF_(pa.getRange(r, 3), '=ROUND(' + noMes(cCom, cDt) + ',2)');
    if (temAvulso) {
      posF_(pa.getRange(r, 4), '=ROUND(' + noMes(aVal, aDt) + ',2)');
      posF_(pa.getRange(r, 5), '=ROUND($C' + r + '+$D' + r + ',2)');
      posF_(pa.getRange(r, 6), '=ROUND(' + pagoNoMes(cCom, cDt, cSt)
        + '+' + pagoNoMes(aVal, aDt, aSt) + ',2)');
      posF_(pa.getRange(r, 7), '=ROUND($E' + r + '-$F' + r + ',2)');
    } else {
      posF_(pa.getRange(r, 4), '=ROUND(' + pagoNoMes(cCom, cDt, cSt) + ',2)');
      posF_(pa.getRange(r, 5), '=ROUND($C' + r + '-$D' + r + ',2)');
    }
    pa.getRange(r, 3, 1, nc - 1).setNumberFormat(MOEDA).setFontColor(NAVY2).setFontSize(10);
    if (m % 2) pa.getRange(r, 2, 1, nc).setBackground(ZEBRA);
  }
  // ── o que ainda não tem data combinada ──
  //
  // Sem esta linha a tabela mostrava "Total do ano R$ 0,00" enquanto o cartão
  // de cima mostrava o total cheio: dois números com o mesmo nome discordando.
  // Agora o que não foi acordado tem lugar próprio, e a tabela fecha com o
  // cartão. É também o jeito de enxergar o que falta combinar.
  const rs = lm + 14;
  const somaMes = function (L) { return 'SUM(' + L + (lm + 2) + ':' + L + (lm + 13) + ')'; };
  pa.getRange(rs, 2).setValue('Sem data combinada')
    .setFontColor(ABERTO).setFontSize(10).setFontWeight('bold').setFontStyle('italic');
  const pago7 = temAvulso ? '($E$7+$E$11)' : '$E$7';
  if (temAvulso) {
    posF_(pa.getRange(rs, 3), '=ROUND($C$7-' + somaMes('C') + ',2)');
    posF_(pa.getRange(rs, 4), '=ROUND($C$11-' + somaMes('D') + ',2)');
    posF_(pa.getRange(rs, 5), '=ROUND($C' + rs + '+$D' + rs + ',2)');
    posF_(pa.getRange(rs, 6), '=ROUND(' + pago7 + '-' + somaMes('F') + ',2)');
    posF_(pa.getRange(rs, 7), '=ROUND($E' + rs + '-$F' + rs + ',2)');
  } else {
    posF_(pa.getRange(rs, 3), '=ROUND($C$7-' + somaMes('C') + ',2)');
    posF_(pa.getRange(rs, 4), '=ROUND(' + pago7 + '-' + somaMes('D') + ',2)');
    posF_(pa.getRange(rs, 5), '=ROUND($C' + rs + '-$D' + rs + ',2)');
  }
  pa.getRange(rs, 3, 1, nc - 1).setNumberFormat(MOEDA)
    .setFontColor(ABERTO).setFontSize(10).setFontWeight('bold');
  pa.getRange(rs, 2, 1, nc).setBackground(ABERTOBG);

  // ── total do ano: os doze meses MAIS o que não tem data ──
  const rt = lm + 15;
  pa.getRange(rt, 2, 1, nc).setBackground(NAVY);
  pa.getRange(rt, 2).setValue('Total do ano').setFontColor(GOLDS).setFontWeight('bold');
  for (let c = 3; c <= nc + 1; c++) {
    const Lc = colLetra_(c);
    posF_(pa.getRange(rt, c), '=ROUND(SUM(' + Lc + (lm + 2) + ':' + Lc + rs + '),2)');
    pa.getRange(rt, c).setNumberFormat(MOEDA).setFontColor(GOLDS).setFontWeight('bold');
  }
  pa.getRange(lm + 1, 2, 15, nc).setBorder(true, true, true, true, true, true,
    '#d6dbe2', SpreadsheetApp.BorderStyle.SOLID);

  pa.getRange(rt + 2, 2, 1, nc).merge().setValue(
    'O mês é o da DATA COMBINADA de pagamento, digitada à mão na aba Comissões. '
    + 'O que ainda não tem data cai na linha "Sem data combinada" — é o que falta '
    + 'acordar, e por isso a tabela fecha com o total lá de cima. '
    + 'Divergência se fala antes do pagamento.')
    .setFontColor(MUTED).setFontSize(9).setFontStyle('italic').setWrap(true);
  pa.setRowHeight(rt + 2, 34);
}


function colLetra_(n) {
  let s = '';
  while (n > 0) { const m = (n - 1) % 26; s = String.fromCharCode(65 + m) + s; n = (n - 1 - m) / 26; }
  return s;
}


/** Lê os totais da aba "Aporte Walton" — entradas, saídas, investimentos, saldo. */
function lerAporte_(ss) {
  const sh = ss.getSheetByName('Aporte Walton');
  if (!sh) return [];
  const fim = sh.getLastRow();
  const val = sh.getRange(1, 1, fim, 1).getValues();
  const rot = sh.getRange(1, 2, fim, 1).getDisplayValues();
  const ALVOS = [['Total · entradas', 'Entradas'], ['Total · saídas', 'Saídas'],
                 ['Total · investimentos', 'Investimentos'],
                 ['SALDO DO APORTE', 'Saldo do aporte']];
  const linhas = [];
  ALVOS.forEach(function (a) {
    for (let r = 0; r < fim; r++) {
      if (String(rot[r][0] || '').trim().indexOf(a[0]) === 0) {
        linhas.push([a[1], Number(val[r][0]) || 0]);
        return;
      }
    }
  });
  return linhas;
}


/**
 * Tira o controle de ORÇADO × REALIZADO de onde ele aparecia como indicador:
 * MC % orçada, Δ p.p. e Desvio de custo.
 *
 * Motivo: esse controle não acontecia no dia a dia. A coluna Orçado ficava
 * vazia em todos os projetos, e indicador que ninguém alimenta não fica
 * neutro — ele senta ao lado do indicador que importa e rouba a atenção com
 * um zero que parece informação.
 *
 * O QUE SAI são células de FÓRMULA e rótulos, não preenchimento de ninguém.
 * As colunas "Orçado (R$)" dos blocos continuam existindo: se um dia a prática
 * mudar, o número volta sem refazer nada.
 *
 * Idempotente: rode quantas vezes quiser.
 */
function removerControleOrcado() {
  const ss = SpreadsheetApp.openById(ID_CUSTO);
  calibrar_(ss);
  const FIXAS = ['Instruções', FICHA.painel, 'Listas', FICHA.base];
  let fichas = 0;

  // ── 1 · o topo de cada ficha ──
  ss.getSheets().forEach(function (sh) {
    const nome = sh.getName();
    if (FIXAS.indexOf(nome) >= 0) return;
    if (sh.getMaxRows() < 20 || sh.getMaxColumns() < 15) return;
    if (String(sh.getRange('A8').getDisplayValue() || '').trim().toUpperCase().indexOf('PROJETO') !== 0) return;

    // a faixa de KPI vai da coluna 7 à 15; desmancha e refaz só ela
    sh.getRange(12, 7, 2, 9).breakApart();
    sh.getRange(12, 8, 2, 8).clearContent();      // H e I em diante, rótulo e fórmula

    sh.getRange(12, 7, 1, 9).merge().setValue('MC %')
      .setFontSize(7.5).setFontWeight('bold').setFontColor(MUTED)
      .setHorizontalAlignment('center').setVerticalAlignment('middle')
      .setBackground('#ffffff');
    sh.getRange(13, 7, 1, 9).merge()
      .setNumberFormat('0.0%').setFontSize(13).setFontWeight('bold').setFontColor(NAVY)
      .setHorizontalAlignment('center').setVerticalAlignment('middle')
      .setBackground(GOLDBG);
    fichas++;
  });

  // ── 2 · a tabela do Painel Geral, se ela ainda mora aqui ──
  const pg = ss.getSheetByName(FICHA.painel);
  if (!pg) {
    SpreadsheetApp.flush();
    console.log('Controle de orçado: ' + fichas + ' ficha(s); Painel Geral não está aqui.');
    return fichas + ' ficha(s)';
  }
  const hd = FICHA.pg0 - 1;                      // linha de cabeçalho
  const n = FICHA.pgf - FICHA.pg0 + 1;

  pg.getRange(hd, 15, 1, 4).breakApart().clearContent();
  pg.getRange(hd, 15).setValue('Diagnóstico');

  const fs = [];
  for (let i = 0; i < n; i++) {
    const r = FICHA.pg0 + i;
    fs.push(['=IF($N' + r + '="","",IF($N' + r + '>=0.35,"Margem boa",'
             + 'IF($N' + r + '>=0.25,"Margem apertada","Margem crítica")))']);
  }
  pg.getRange(FICHA.pg0, 16, n, 3).clearContent();
  posFs_(pg.getRange(FICHA.pg0, 15, n, 1), fs);
  pg.getRange(FICHA.pg0, 15, n, 1).setHorizontalAlignment('center')
    .setFontSize(8.5).setFontWeight('bold').setFontColor(NAVY2);
  pg.getRange(FICHA.pgf + 1, 15, 1, 4).clearContent();

  // as cores do diagnóstico mudam de coluna; as outras regras ficam como estão
  const faixa = pg.getRange(FICHA.pg0, 15, n, 1);
  const regras = pg.getConditionalFormatRules().filter(function (r) {
    return r.getRanges().every(function (g) { return g.getColumn() !== 15; });
  });
  [['Margem boa', '#e2f0e7', '#2f7d4f'],
   ['Margem apertada', '#fbf1dc', '#b57a16'],
   ['Margem crítica', '#fbe7e6', '#b0413f']].forEach(function (x) {
    regras.push(SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo(x[0])
      .setBackground(x[1]).setFontColor(x[2]).setBold(true).setRanges([faixa]).build());
  });
  pg.setConditionalFormatRules(regras);

  SpreadsheetApp.flush();
  const r = fichas + ' ficha(s) sem MC % orçada e sem desvio de custo, '
          + 'Painel Geral sem as três colunas do orçado';
  console.log('Controle de orçado: ' + r);
  return r;
}


// ════════════════════════════════════════════════════════════════════════
//  COMPETÊNCIA MENSAL
// ════════════════════════════════════════════════════════════════════════
//
// Cada projeto escolhe um mês na ficha, e é nesse mês que a receita e o custo
// INTEIROS dele pesam — não importa em que mês cada compra aconteceu.
//
// É decisão de gestão, não de contabilidade. A vantagem é olhar o mês e ver
// projeto fechado em vez de pedaço: venda, custo e margem do mesmo projeto na
// mesma linha do tempo. O preço é que um projeto comprado em agosto e entregue
// em outubro aparece inteiro em outubro, se for esse o mês escolhido.

const MES3 = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
              'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
/** 'Out/2026' → 24315, para ordenar. Texto estranho vai para o fim. */
function ordemComp_(c) {
  const p = String(c || '').split('/');
  const i = MES3.indexOf(p[0]);
  if (i < 0 || !p[1]) return 999999;
  return Number(p[1]) * 12 + i;
}

function compDeHoje_() {
  const d = new Date();
  return MES3[d.getMonth()] + '/' + d.getFullYear();
}


/**
 * Põe o campo de competência na linha 10 de todas as fichas.
 *
 * A linha 10 era um espaçador de 8 pixels, vazia. Usar o que já existe em vez
 * de inserir linha nova foi escolha deliberada: inserir empurraria tudo abaixo
 * e obrigaria a mexer em dezenas de constantes, na Base e nas individuais.
 *
 * NÃO ESCREVE POR CIMA DE NADA. Se a linha 10 de alguma ficha tiver conteúdo
 * que não seja este campo, a ficha é pulada e o nome aparece no log. Rode
 * quantas vezes quiser: o mês já escolhido nunca é alterado.
 */
function adicionarCompetencia() {
  const ss = SpreadsheetApp.openById(ID_CUSTO);
  calibrar_(ss);
  const FIXAS = ['Instruções', FICHA.painel, 'Listas', FICHA.base];
  const ROTULO = 'MÊS DE COMPETÊNCIA';
  let feitas = 0, refeitas = 0;
  const ocupadas = [], trocados = [];

  ss.getSheets().forEach(function (sh) {
    const nome = sh.getName();
    if (FIXAS.indexOf(nome) >= 0) return;
    if (sh.getMaxRows() < 20 || sh.getMaxColumns() < 15) return;

    // é mesmo uma ficha?
    if (String(sh.getRange('A8').getDisplayValue() || '').trim().toUpperCase().indexOf('PROJETO') !== 0) {
      console.log('  pulei "' + nome + '": não parece ficha.');
      return;
    }

    const linha = sh.getRange(10, 1, 1, 15).getDisplayValues()[0]
                    .map(function (v) { return String(v || '').trim(); });
    const jaTem = linha[0].indexOf(ROTULO) === 0;
    const vazia = linha.join('') === '';

    if (!jaTem && !vazia) {
      ocupadas.push(nome + ' → "' + linha.filter(String).join(' | ') + '"');
      return;
    }

    sh.setRowHeight(10, 18);
    sh.getRange(10, 1, 1, 15).breakApart();
    sh.getRange(10, 1, 1, 3).merge().setValue(ROTULO)
      .setFontSize(8).setFontWeight('bold').setFontColor(MUTED)
      .setHorizontalAlignment('right').setVerticalAlignment('middle')
      .setBackground('#ffffff');
    // o que estiver digitado aqui vira fórmula. Nada se perde: o mês passa a
    // sair da entrega real, que é de onde ele deveria ter vindo desde o começo.
    const antes = String(sh.getRange(10, 4).getDisplayValue() || '').trim();
    if (antes && !sh.getRange(10, 4).getFormula()) {
      trocados.push(nome.trim() + ' tinha "' + antes + '"');
    }
    sh.getRange(10, 4, 1, 2).merge()
      .setFontSize(11).setFontWeight('bold').setFontColor(NAVY)
      .setHorizontalAlignment('center').setVerticalAlignment('middle')
      .setBackground(CALC)
      .clearDataValidations();
    posF_(sh.getRange(10, 4),
      '=IF($J$7="","",CHOOSE(MONTH($J$7),'
      + MES3.map(function (x) { return '"' + x + '"'; }).join(',')
      + ')&"/"&YEAR($J$7))');
    sh.getRange(10, 6, 1, 10).merge().setValue(
      'vem do mês da ENTREGA REAL — enquanto não for entregue, não tem competência')
      .setFontSize(8).setFontStyle('italic').setFontColor(MUTED)
      .setHorizontalAlignment('left').setVerticalAlignment('middle')
      .setBackground('#ffffff');

    if (jaTem) { refeitas++; } else { feitas++; }
  });

  if (trocados.length) {
    console.log('  o valor digitado virou fórmula da entrega real em:');
    trocados.forEach(function (t) { console.log('    ' + t); });
  }
  if (ocupadas.length) {
    console.log('  NÃO MEXI nestas, a linha 10 tinha conteúdo:');
    ocupadas.forEach(function (t) { console.log('    ' + t); });
  }
  SpreadsheetApp.flush();
  const r = feitas + ' ficha(s) com o campo novo, ' + refeitas + ' já tinha(m)'
          + (ocupadas.length ? ', ' + ocupadas.length + ' pulada(s)' : '');
  console.log('Competência: ' + r);
  return r;
}


// ════════════════════════════════════════════════════════════════════════
//  ANÁLISE MENSAL  ·  competência e produção na mesma tela
// ════════════════════════════════════════════════════════════════════════
//
// Substitui as abas "Painel de Competência" e "Produção e Entrega". Eram dois
// recortes do mesmo mês em dois lugares, e separados obrigavam a abrir duas
// telas para responder uma pergunta só.
//
// Seis medidas, no resumo e na tabela, nesta ordem — é a vida de um projeto:
//   Vendido    contrato assinado, pelo mês da venda
//   Faturado   nota emitida, pelo mês da entrega
//   Produzido  ambiente que saiu da fábrica, pela data de fabricação
//   Montado    ambiente entregue, pela data de montagem
//   Custo fixo o que a operação custa, exista venda ou não
//   Pago       comissão e RT que de fato saíram do caixa

/** Comissão com status Pago nas catorze individuais, por mês da data combinada. */
function comissoesPagasPorMes_(ano) {
  const m = [0,0,0,0,0,0,0,0,0,0,0,0,0,0];
  PESSOAS.forEach(function (p) {
    let sh;
    try { sh = SpreadsheetApp.openById(p.id).getSheetByName('Comissões'); } catch (e) { return; }
    if (!sh) return;
    const cols = layout_(p);
    const iT = cols.findIndex(function (c) { return c.total; }) + 1;
    const iP = cols.findIndex(function (c) { return c.manual === 'pagamento'; }) + 1;
    const iS = cols.findIndex(function (c) { return c.manual === 'status'; }) + 1;
    if (!iT || !iP || !iS) return;
    const v = sh.getRange(LIN0, 1, N_PROJ, Math.max(iT, iP, iS)).getValues();
    v.forEach(function (L) {
      if (String(L[iS - 1] || '').trim() !== 'Pago') return;
      const val = Number(L[iT - 1]) || 0;
      if (!val) return;
      const d = L[iP - 1];
      if (d instanceof Date && d.getFullYear() === ano) { m[d.getMonth()] += val; }
      else { m[12] += val; }
      m[13] += val;
    });
  });
  return m;
}


function abaAnaliseMensal_() {
  const ano = new Date().getFullYear();
  const cp = SpreadsheetApp.openById(ID_CUSTO);
  const pgto = SpreadsheetApp.openById(ID_PAG);

  const base = cp.getSheetByName(FICHA.base);
  const nb = base.getLastRow() - 1;
  const bv = nb > 0 ? base.getRange(2, 1, nb, base.getLastColumn()).getValues() : [];

  // ── um registro por projeto, e a lista de ambientes ──
  const vistos = {}, projetos = [], amb = [];
  bv.forEach(function (L) {
    const nome = String(L[0] || '').trim();
    if (String(L[2] || '').trim()) {
      amb.push({ projeto: nome, cliente: String(L[1] || '').trim(),
                 ambiente: String(L[2]).trim(), valor: Number(L[4]) || 0,
                 fab: L[8] instanceof Date ? L[8] : null,
                 mont: L[12] instanceof Date ? L[12] : null });
    }
    if (!nome || vistos[nome]) return;
    vistos[nome] = true;
    projetos.push({
      projeto: nome, cliente: String(L[1] || '').trim(),
      venda: Number(L[21]) || 0, custo: Number(L[27]) || 0, margem: Number(L[28]) || 0,
      comp: String(L[33] || '').trim(), situacao: String(L[34] || '').trim() || '—',
      faturado: Number(L[35]) || 0, rt: Number(L[36]) || 0,
      rtPago: String(L[37] || '').trim() === 'Pago',
    });
  });

  // ── as seis medidas, mês a mês ──
  const zero = function () { return [0,0,0,0,0,0,0,0,0,0,0,0,0,0]; };
  const vendido = zero(), faturado = zero(), produzido = zero(), montado = zero(),
        fixo = zero(), pago = zero();

  const bp = pgto.getSheetByName('Base · Projetos');
  if (bp && bp.getLastRow() > 1) {
    bp.getRange(2, 1, bp.getLastRow() - 1, 10).getValues().forEach(function (L) {
      if (String(L[0]) !== String(ano)) return;
      const i = MESES.indexOf(String(L[1] || '').trim());
      const v = Number(L[4]) || 0;
      if (i >= 0) vendido[i] += v; else vendido[12] += v;
      vendido[13] += v;
    });
  }

  const noMes = function (alvo, comp, valor) {
    if (!valor) return;
    const i = MES3.indexOf(String(comp).split('/')[0]);
    const a = Number(String(comp).split('/')[1]);
    if (i >= 0 && a === ano) alvo[i] += valor; else alvo[12] += valor;
    alvo[13] += valor;
  };
  projetos.forEach(function (p) {
    noMes(faturado, p.comp, p.faturado);
    if (p.rtPago) noMes(pago, p.comp, p.rt);
  });
  amb.forEach(function (a) {
    if (a.fab) { const i = a.fab.getFullYear() === ano ? a.fab.getMonth() : 12;
                 produzido[i] += a.valor; produzido[13] += a.valor; }
    if (a.mont) { const i = a.mont.getFullYear() === ano ? a.mont.getMonth() : 12;
                  montado[i] += a.valor; montado[13] += a.valor; }
  });

  let custoMes = 0;
  const cf = pgto.getSheetByName('Base · Custo Fixo');
  if (cf && cf.getLastRow() > 1) {
    cf.getRange(2, 1, cf.getLastRow() - 1, 3).getValues().forEach(function (L) {
      if (String(L[0] || '').indexOf('Custo operacional') === 0) custoMes = Number(L[2]) || 0;
    });
  }
  const mHoje = new Date().getMonth();
  for (let i = 0; i <= mHoje; i++) { fixo[i] = custoMes; fixo[13] += custoMes; }

  const comPagas = comissoesPagasPorMes_(ano);
  for (let i = 0; i < 14; i++) pago[i] += comPagas[i];

  // ── desenho ──
  const W = 17;
  const sh = abaLimpa_(SpreadsheetApp.openById(ID_G26), 'Análise mensal', W);
  cabecalhoPainel_(sh, 'ANÁLISE MENSAL   ·   ' + ano,
    'Vendido e faturado medem resultado   ·   produzido e montado medem atividade   ·   '
    + 'não batem entre si, e não devem bater', W);
  sh.setColumnWidth(2, 190);
  for (let c = 3; c <= W; c++) sh.setColumnWidth(c, 92);

  let lin = 5;
  secaoPainel_(sh, lin, 'RESUMO DE ' + MESES[mHoje].toUpperCase() + '   ·   '
    + 'o mês corrente em seis números', W);
  lin += 2;
  const medidas = [
    ['Vendido', vendido, NAVY], ['Faturado', faturado, NAVY2],
    ['Produzido', produzido, '#2f5d8c'], ['Montado', montado, '#2f7d4f'],
    ['Custo fixo total', fixo, '#b0413f'], ['Comissões e RTs pagas', pago, '#c47d0e'],
  ];
  medidas.forEach(function (m, i) {
    const col = 2 + (i % 3) * 2;
    const li = lin + Math.floor(i / 3) * 3;
    cartaoPainel_(sh, li, col, m[0], m[1][mHoje], m[2]);
  });
  lin += 6;

  secaoPainel_(sh, lin, 'MÊS A MÊS', W); lin += 2;
  const l0 = lin;
  const linhas = medidas.map(function (m) { return [m[0]].concat(m[1]); });
  lin = tabelaPainel_(sh, lin, 2, cabMeses_('Medida'), linhas, formatosMes_());
  sh.getRange(l0 + 5, 2, 1, 15).setBackground('#fcf2f1').setFontColor('#b0413f');
  sh.getRange(l0 + 6, 2, 1, 15).setBackground(ABERTOBG).setFontColor('#c47d0e');
  sh.getRange(l0 + 1, 2, 6, 1).setFontWeight('bold').setFontColor(NAVY);

  // ── competência: o projeto fechado, no mês em que foi entregue ──
  const meses = {}, semComp = [];
  projetos.forEach(function (p) {
    if (!p.venda && !p.custo) return;
    if (!p.comp) { semComp.push(p); return; }
    if (!meses[p.comp]) meses[p.comp] = [];
    meses[p.comp].push(p);
  });
  const ordem = Object.keys(meses).sort(function (a, b) { return ordemComp_(a) - ordemComp_(b); });
  const soma = function (l, c) { return l.reduce(function (s, p) { return s + p[c]; }, 0); };

  const CAB = ['Cliente', 'Projeto', 'Valor do projeto', 'Total de custos',
               'MC final', 'MC %', 'Condição de entrega'];
  const FMT = [null, null, MOEDA, MOEDA, MOEDA, '0.0%', null];
  const faixasMC = [], faixasCond = [];

  const blocoProjetos = function (titulo, lista, ambar) {
    secaoPainel_(sh, lin, titulo, W); lin += 2;
    const ls = lista.sort(function (a, b) { return b.venda - a.venda; })
      .map(function (p) {
        return [p.cliente || p.projeto, p.projeto, p.venda, p.custo, p.margem,
                p.venda ? p.margem / p.venda : 0, p.situacao];
      });
    const v = soma(lista, 'venda');
    ls.push(['Total', '', v, soma(lista, 'custo'), soma(lista, 'margem'),
             v ? soma(lista, 'margem') / v : 0, '']);
    const li = lin;
    lin = tabelaPainel_(sh, lin, 2, CAB, ls, FMT);
    sh.getRange(li + ls.length, 2, 1, 7)
      .setBackground(ambar ? ABERTOBG : NAVY)
      .setFontColor(ambar ? '#c47d0e' : GOLDS).setFontWeight('bold');
    faixasMC.push(sh.getRange(li + 1, 7, ls.length - 1, 1));
    faixasCond.push(sh.getRange(li + 1, 8, ls.length - 1, 1));
  };

  secaoPainel_(sh, lin, 'COMPETÊNCIA   ·   o projeto inteiro pesa no mês da entrega', W);
  lin += 2;
  ordem.forEach(function (c) { blocoProjetos('Entregues em ' + c, meses[c], false); });
  if (semComp.length) {
    blocoProjetos('Ainda sem entrega real — não entram em mês nenhum', semComp, true);
  }

  // ── produção: o ambiente, pela data de cada etapa ──
  const prontos = amb.filter(function (a) { return a.fab && !a.mont; });
  const emProd = amb.filter(function (a) { return !a.fab; });
  const somaA = function (l) { return l.reduce(function (s, a) { return s + a.valor; }, 0); };
  const CAB2 = ['Cliente', 'Projeto', 'Ambiente', 'Valor', 'Fabricado em', 'Montado em'];
  const FMT2 = [null, null, null, MOEDA, 'dd/mm/yyyy', 'dd/mm/yyyy'];

  const blocoAmb = function (titulo, lista, ambar) {
    secaoPainel_(sh, lin, titulo, W); lin += 2;
    if (!lista.length) {
      sh.getRange(lin, 2).setValue('Nada aqui.').setFontColor(MUTED).setFontStyle('italic');
      lin += 2;
      return;
    }
    const ls = lista.sort(function (a, b) { return b.valor - a.valor; })
      .map(function (a) { return [a.cliente, a.projeto, a.ambiente, a.valor,
                                  a.fab || '', a.mont || '']; });
    ls.push(['Total', '', '', somaA(lista), '', '']);
    const li = lin;
    lin = tabelaPainel_(sh, lin, 2, CAB2, ls, FMT2);
    sh.getRange(li + ls.length, 2, 1, 6)
      .setBackground(ambar ? ABERTOBG : NAVY)
      .setFontColor(ambar ? '#c47d0e' : GOLDS).setFontWeight('bold');
  };

  secaoPainel_(sh, lin, 'PRODUÇÃO   ·   o ambiente, pela data de cada etapa', W); lin += 2;
  blocoAmb('Pronto e não entregue — R$ ' + somaA(prontos).toFixed(2)
           + ' de obra feita esperando montagem', prontos, true);
  blocoAmb('Ainda em produção — sem data de fabricação lançada', emProd, false);

  // ── cores de estado: sempre com o rótulo escrito, nunca só a cor ──
  if (faixasMC.length) {
    sh.setConditionalFormatRules([
      SpreadsheetApp.newConditionalFormatRule().whenNumberLessThan(0.25)
        .setBackground('#fcf2f1').setFontColor('#b0413f').setBold(true)
        .setRanges(faixasMC).build(),
      SpreadsheetApp.newConditionalFormatRule().whenNumberBetween(0.25, 0.35)
        .setBackground('#fdf8ee').setFontColor('#c47d0e').setBold(true)
        .setRanges(faixasMC).build(),
      SpreadsheetApp.newConditionalFormatRule().whenNumberGreaterThan(0.35)
        .setBackground('#eff5f1').setFontColor('#2f7d4f').setBold(true)
        .setRanges(faixasMC).build(),
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Atrasado')
        .setBackground('#fcf2f1').setFontColor('#b0413f').setBold(true)
        .setRanges(faixasCond).build(),
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Em produção')
        .setBackground('#f0f4f9').setFontColor('#2f5d8c').setBold(true)
        .setRanges(faixasCond).build(),
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('No prazo')
        .setBackground('#eff5f1').setFontColor('#2f7d4f').setBold(true)
        .setRanges(faixasCond).build(),
    ]);
  }

  sh.getRange(lin, 2, 1, W - 2).merge().setValue(
    'Vendido é contrato assinado, pelo mês da venda. Faturado é nota emitida, alocada no mês '
    + 'da entrega. Produzido e montado medem ambiente, não projeto, pela data de cada etapa — '
    + 'por isso nunca batem com os dois primeiros. Custo fixo é o vigente hoje, repetido nos '
    + 'meses já corridos. Pago é o que saiu do caixa: comissão com status Pago nas planilhas '
    + 'individuais, mais RT com status Pago na ficha.')
    .setFontColor(MUTED).setFontSize(9).setFontStyle('italic').setWrap(true);
  sh.setRowHeight(lin, 44);

  SpreadsheetApp.flush();
  const r = projetos.length + ' projeto(s) · ' + amb.length + ' ambiente(s) · '
          + ordem.length + ' mês(es) com entrega';
  console.log('Análise mensal: ' + r);
  return r;
}


/**
 * Garante a estrutura das fichas antes de qualquer leitura.
 *
 * Roda dentro do atualizarTudo, e não como migração avulsa: migração que
 * depende de alguém lembrar de rodar é migração que uma ficha nova nasce sem.
 *
 * Tudo é idempotente e NADA apaga preenchimento. Onde há risco de apagar —
 * as linhas de retrabalho que sobram — a função confere se estão vazias e,
 * se não estiverem, deixa como está e avisa no log.
 */
function garantirEstrutura_() {
  const ss = SpreadsheetApp.openById(ID_CUSTO);
  calibrar_(ss);
  const FIXAS = ['Instruções', FICHA.painel, 'Listas', FICHA.base];
  const ROSTER = EQUIPE_FICHA.concat(PROJETISTAS_FICHA).concat(GESTORES_FICHA);
  const regraGestor = SpreadsheetApp.newDataValidation()
    .requireValueInList(ROSTER, true).setAllowInvalid(true)
    .setHelpText('Quem faz a gestão técnica deste projeto.').build();
  let ident = 0, rt = 0, retrab = 0;
  const retrabCheio = [];

  ss.getSheets().forEach(function (sh) {
    const nome = sh.getName();
    if (FIXAS.indexOf(nome) >= 0) return;
    if (sh.getMaxRows() < 50 || sh.getMaxColumns() < 15) return;
    if (String(sh.getRange('A8').getDisplayValue() || '').trim().toUpperCase().indexOf('PROJETO') !== 0) return;

    sh.setFrozenRows(0);
    sh.setFrozenColumns(0);

    // ── 1 · GESTÃO TÉCNICA entra na identificação, ao lado do coordenador ──
    if (String(sh.getRange(8, 8).getDisplayValue() || '').trim() !== 'GESTÃO TÉCNICA') {
      // o nome que estava na linha da comissão vem junto; nada se perde
      const antigo = String(sh.getRange(66, 8).getDisplayValue() || '').trim();

      sh.getRange(8, 8, 2, 8).breakApart();
      [[8, 'GESTÃO TÉCNICA'], [10, 'DIAS DE ATRASO'], [12, 'SITUAÇÃO DA ENTREGA']]
        .forEach(function (x, k) {
          const larg = k === 2 ? 4 : 2;
          sh.getRange(8, x[0], 1, larg).merge().setValue(x[1])
            .setFontSize(7.5).setFontWeight('bold').setFontColor(MUTED)
            .setHorizontalAlignment('center').setVerticalAlignment('middle')
            .setBackground('#ffffff');
          sh.getRange(9, x[0], 1, larg).merge()
            .setFontSize(10.5).setFontWeight('bold').setFontColor(NAVY)
            .setHorizontalAlignment('center').setVerticalAlignment('middle')
            .setBackground(k === 0 ? '#fff9e3' : CALC);
        });
      sh.getRange(9, 8).setDataValidation(regraGestor);
      if (antigo && ROSTER.indexOf(antigo) >= 0) sh.getRange(9, 8).setValue(antigo);

      posF_(sh.getRange(9, 10), '=IF(OR($H$7="",$J$7=""),"",$J$7-$H$7)');
      sh.getRange(9, 10).setNumberFormat('0 "dias"');
      posF_(sh.getRange(9, 12), '=IF($H$7="","",IF($J$7="",'
        + 'IF(TODAY()>$H$7,"Atrasado","Em produção"),'
        + 'IF($J$9<=0,"No prazo","Atrasado")))');

      // a linha da comissão de gestão devolve a coluna de observação
      sh.getRange(66, 8, 1, 8).breakApart();
      sh.getRange(66, 8, 1, 8).merge().clearDataValidations()
        .setValue('quem faz a gestão técnica está na identificação, no topo da ficha')
        .setFontSize(8.5).setFontColor(INK).setHorizontalAlignment('left')
        .setBackground('#fff9e3');
      ident++;
    }

    // ── 2 · bloco 5 passa a olhar o nome novo ──
    for (let r = 74; r < 100; r++) {
      const quem = String(sh.getRange(r, 1).getDisplayValue() || '').trim();
      if (quem === 'TOTAL') break;
      if (!quem) continue;
      posF_(sh.getRange(r, 8),
        '=IF($A' + r + '="","",IF($A' + r + '=$F$9,IF($D$65="",0,$D$65),0)'
        + '+IF($A' + r + '=$H$9,IF($D$66="",0,$D$66),0))');
    }

    // ── 3 · RT ganha status de pagamento ──
    if (String(sh.getRange(43, 10).getDisplayValue() || '').indexOf('status do pagamento') !== 0) {
      sh.getRange(43, 8, 1, 8).breakApart();
      sh.getRange(43, 8, 1, 2).merge().setFontSize(9).setFontWeight('bold')
        .setFontColor(NAVY2).setHorizontalAlignment('center').setBackground('#fff9e3')
        .setDataValidation(SpreadsheetApp.newDataValidation()
          .requireValueInList(['Em aberto', 'Pago'], true).setAllowInvalid(true)
          .setHelpText('O RT já foi pago ao parceiro?').build());
      sh.getRange(43, 10, 1, 6).merge().setValue('status do pagamento do RT ao parceiro')
        .setFontSize(8.5).setFontColor(INK).setHorizontalAlignment('left')
        .setBackground('#fff9e3');
      rt++;
    }

    // ── 4 · retrabalho: quatro linhas bastam, se as outras estiverem vazias ──
    const rb0 = acharLinha_(sh, 'O que aconteceu', 110, 140);
    if (rb0) {
      const prim = rb0 + 1;
      const sobra = sh.getRange(prim + 4, 1, 8, 5).getDisplayValues();
      if (sobra.join('').trim() === '') {
        sh.deleteRows(prim + 4, 8);
        retrab++;
      } else {
        retrabCheio.push(nome.trim());
      }
    }
  });

  // o Painel Geral perde a coluna de diagnóstico e o congelamento
  const pg = ss.getSheetByName(FICHA.painel);
  if (pg) {
  pg.setFrozenRows(0);
  pg.setFrozenColumns(0);
  const hd = FICHA.pg0 - 1;
  const n = FICHA.pgf - FICHA.pg0 + 1;
  if (String(pg.getRange(hd, 15).getDisplayValue() || '').trim() === 'Diagnóstico') {
    pg.getRange(hd, 15).clearContent();
    pg.getRange(FICHA.pg0, 15, n, 1).clearContent();
    pg.setConditionalFormatRules(pg.getConditionalFormatRules().filter(function (r) {
      return r.getRanges().every(function (g) { return g.getColumn() !== 15; });
    }));
  }
  }
  const bs = ss.getSheetByName(FICHA.base);
  if (bs) { bs.setFrozenRows(0); bs.setFrozenColumns(0); }

  if (retrabCheio.length) {
    console.log('  retrabalho NÃO encurtado, tem lançamento nas linhas que sobrariam: '
                + retrabCheio.join(' | '));
  }
  SpreadsheetApp.flush();
  return ident + ' ficha(s) com gestão técnica na identificação, ' + rt
       + ' com status do RT, ' + retrab + ' com retrabalho em 4 linhas';
}

/** Primeira linha entre ini e fim cuja coluna A começa com o texto. */
function acharLinha_(sh, texto, ini, fim) {
  const n = Math.min(fim, sh.getMaxRows()) - ini + 1;
  if (n < 1) return 0;
  const v = sh.getRange(ini, 1, n, 1).getDisplayValues();
  for (let i = 0; i < n; i++) {
    if (String(v[i][0] || '').trim().indexOf(texto) === 0) return ini + i;
  }
  return 0;
}


// ════════════════════════════════════════════════════════════════════════
//  GESTÃO 2026  ·  o ano inteiro numa planilha só
// ════════════════════════════════════════════════════════════════════════
//
// Reúne o que estava espalhado: a relação de clientes e o histórico de
// pagamentos (que vivia na Controle de Pagamentos), a Análise mensal e o
// Painel Geral dos projetos (que vivia na Custo por Projeto).
//
// A migração é por CÓPIA. Nada é apagado da origem por este script — conferir
// primeiro, limpar depois, e a limpeza é decisão de quem confere.

const ID_G26 = '16VkH3jaTp6O1wahE3zXFwUiQQSXm1bGFuLaaQMg3pjs';
const ANO_G26 = '2026';


/**
 * Copia para a Gestão 2026 as abas que vêm prontas: o ano de pagamentos e as
 * Listas que alimentam os menus dela.
 *
 * copyTo leva fórmula, formato, validação e dado — é a única forma de trazer
 * a aba de ano "na íntegra", porque ela tem divisória de mês, cabeçalho
 * mesclado e cinco blocos de pagamento por linha. Reconstruir seria reescrever.
 *
 * Idempotente: se a aba já existe no destino, não copia de novo.
 */
function migrarParaGestao2026() {
  const org = SpreadsheetApp.openById(ID_PAG);
  const dst = SpreadsheetApp.openById(ID_G26);
  const feitas = [], puladas = [];

  [[ANO_G26, 'Pagamentos ' + ANO_G26], ['Listas', 'Listas']].forEach(function (par) {
    if (dst.getSheetByName(par[1])) { puladas.push(par[1]); return; }
    const o = org.getSheetByName(par[0]);
    if (!o) { console.log('  aviso: aba "' + par[0] + '" não existe na origem.'); return; }
    const nova = o.copyTo(dst).setName(par[1]);
    nova.setFrozenRows(0);
    nova.setFrozenColumns(0);
    feitas.push(par[1]);
  });

  const p1 = dst.getSheetByName('Página1') || dst.getSheetByName('Sheet1');
  if (p1 && dst.getSheets().length > 1) dst.deleteSheet(p1);

  SpreadsheetApp.flush();
  const r = (feitas.length ? 'copiada(s): ' + feitas.join(', ') : 'nada novo a copiar')
          + (puladas.length ? ' · já existia(m): ' + puladas.join(', ') : '');
  console.log('Gestão 2026: ' + r);
  return r;
}


/**
 * Aba "Clientes": o cadastro, uma linha por cliente.
 *
 * Uma linha e não uma sublinha. Sublinha por cliente obriga a inserir e apagar
 * linha o tempo todo, quebra fórmula e não se ordena nem se filtra. Uma linha
 * com as colunas do cadastro faz tudo isso de graça.
 *
 * O que já existe não é tocado: telefone, endereço, e-mail e observações são
 * lidos antes e devolvidos depois, casados pelo nome do cliente.
 */
function abaClientes_() {
  const dst = SpreadsheetApp.openById(ID_G26);
  const CAB = ['Cliente', 'Projeto', 'Telefone', 'E-mail', 'Endereço',
               'Observações', 'Ficha aberta?', 'Investimento', 'Recebido',
               'Saldo a receber', 'Situação'];
  const MANUAIS = [3, 4, 5, 6];                 // telefone, e-mail, endereço, obs

  let sh = dst.getSheetByName('Clientes');
  const guardado = {};
  if (sh && sh.getLastRow() > 1) {
    const v = sh.getRange(2, 1, sh.getLastRow() - 1, Math.max(6, sh.getLastColumn())).getValues();
    v.forEach(function (L) {
      const c = String(L[0] || '').trim();
      if (!c) return;
      guardado[c] = MANUAIS.map(function (i) { return L[i - 1]; });
    });
  }

  // quem são os clientes: a aba de pagamentos do ano é a fonte
  const pg = dst.getSheetByName('Pagamentos ' + ANO_G26);
  const linhas = [];
  if (pg) {
    const fim = pg.getLastRow();
    const v = pg.getRange(10, 1, Math.max(1, fim - 9), 8).getValues();
    v.forEach(function (L) {
      const nome = String(L[0] || '').trim();
      if (!nome || MESES.indexOf(nome) >= 0) return;
      const inv = Number(L[2]) || 0;
      if (!inv) return;
      const g = guardado[nome] || ['', '', '', ''];
      linhas.push([nome, String(L[1] || '').trim(), g[0], g[1], g[2], g[3], '',
                   inv, Number(L[4]) || 0, Number(L[5]) || 0, String(L[7] || '').trim()]);
    });
  }

  // quem já tem ficha aberta na Custo por Projeto
  const cp = SpreadsheetApp.openById(ID_CUSTO);
  const FIXAS = ['Instruções', FICHA.painel, 'Ficha Modelo', 'Listas', FICHA.base];
  const fichas = {};
  cp.getSheets().forEach(function (s) {
    const n = s.getName();
    if (FIXAS.indexOf(n) < 0) fichas[n.trim()] = true;
  });
  linhas.forEach(function (L) { L[6] = fichas[L[0].trim()] ? 'Sim' : '—'; });

  const W = CAB.length;
  sh = abaLimpa_(dst, 'Clientes', W + 1);
  sh.setColumnWidth(1, 190); sh.setColumnWidth(2, 170); sh.setColumnWidth(3, 130);
  sh.setColumnWidth(4, 190); sh.setColumnWidth(5, 240); sh.setColumnWidth(6, 260);
  for (let c = 7; c <= W; c++) sh.setColumnWidth(c, 115);

  sh.getRange(1, 1, 1, W).setValues([CAB])
    .setBackground(NAVY).setFontColor(GOLDS).setFontSize(9).setFontWeight('bold')
    .setHorizontalAlignment('center').setWrap(true);
  sh.setRowHeight(1, 26);
  if (linhas.length) {
    const rg = sh.getRange(2, 1, linhas.length, W);
    rg.setValues(linhas).setFontSize(10).setFontColor(INK)
      .setBorder(true, true, true, true, true, true, '#d6dbe2', SpreadsheetApp.BorderStyle.SOLID);
    sh.getRange(2, 8, linhas.length, 3).setNumberFormat(MOEDA);
    MANUAIS.forEach(function (c) {
      sh.getRange(2, c, linhas.length, 1).setBackground('#fff9e3');
    });
    sh.getRange(2, 6, linhas.length, 1).setWrap(true);
    for (let i = 1; i < linhas.length; i += 2) {
      sh.getRange(1 + i + 1, 1, 1, W).setBackground(ZEBRA);
    }
    sh.setConditionalFormatRules([
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('—')
        .setFontColor('#c47d0e').setBold(true)
        .setRanges([sh.getRange(2, 7, linhas.length, 1)]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Sim')
        .setFontColor('#2f7d4f').setBold(true)
        .setRanges([sh.getRange(2, 7, linhas.length, 1)]).build(),
    ]);
  }
  sh.getRange(linhas.length + 3, 1, 1, W).merge().setValue(
    'As colunas creme são suas: telefone, e-mail, endereço e observações. O resto vem da aba '
    + 'de pagamentos e se refaz a cada atualização — o que você digitar nas creme é lido antes '
    + 'e devolvido depois, casado pelo nome do cliente. "Ficha aberta?" diz se já existe a aba '
    + 'do cliente na Custo por Projeto.')
    .setFontColor(MUTED).setFontSize(9).setFontStyle('italic').setWrap(true);
  sh.setRowHeight(linhas.length + 3, 34);

  SpreadsheetApp.flush();
  return linhas.length + ' cliente(s)';
}


/**
 * Painel Geral dos projetos, agora na Gestão 2026 e feito de VALORES.
 *
 * Sem "A comprar" e sem "Diagnóstico", como pedido. Na Custo por Projeto ele
 * era fórmula com INDIRECT, que é volátil e recalcula a planilha inteira a
 * cada toque; aqui é foto, escrita pelo script.
 */
function abaPainelGeralG26_() {
  const cp = SpreadsheetApp.openById(ID_CUSTO);
  const base = cp.getSheetByName(FICHA.base);
  const nb = base.getLastRow() - 1;
  const bv = nb > 0 ? base.getRange(2, 1, nb, base.getLastColumn()).getValues() : [];

  const vistos = {}, linhas = [];
  bv.forEach(function (L) {
    const nome = String(L[0] || '').trim();
    if (!nome || vistos[nome]) return;
    vistos[nome] = true;
    const venda = Number(L[21]) || 0, custo = Number(L[27]) || 0, margem = Number(L[28]) || 0;
    linhas.push([nome, String(L[1] || '').trim(),
                 L[17] instanceof Date ? L[17] : '',
                 String(L[34] || '').trim() || '—',
                 String(L[33] || '').trim() || '—',
                 venda, custo, margem, venda ? margem / venda : 0]);
  });
  linhas.sort(function (a, b) { return b[5] - a[5]; });

  const CAB = ['Projeto', 'Cliente', 'Data de entrada', 'Entrega', 'Competência',
               'Venda', 'Custo total', 'MC (R$)', 'MC %'];
  const FMT = [null, null, 'dd/mm/yyyy', null, null, MOEDA, MOEDA, MOEDA, '0.0%'];

  const W = CAB.length + 1;
  const dst = SpreadsheetApp.openById(ID_G26);
  const sh = abaLimpa_(dst, 'Painel Geral', W);
  cabecalhoPainel_(sh, 'PAINEL GERAL DOS PROJETOS',
    'Um projeto por linha, do maior para o menor   ·   vem da Custo por Projeto   ·   '
    + 'atualizado em ' + Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'dd/MM/yyyy HH:mm'), W);
  sh.setColumnWidth(2, 185); sh.setColumnWidth(3, 185);
  for (let c = 4; c <= W; c++) sh.setColumnWidth(c, 120);

  let lin = 5;
  const venda = linhas.reduce(function (s, L) { return s + L[5]; }, 0);
  const custo = linhas.reduce(function (s, L) { return s + L[6]; }, 0);
  const margem = linhas.reduce(function (s, L) { return s + L[7]; }, 0);
  secaoPainel_(sh, lin, 'O CONJUNTO', W); lin += 2;
  cartaoPainel_(sh, lin, 2, 'Projetos', linhas.length, NAVY, '0');
  cartaoPainel_(sh, lin, 4, 'Vendido', venda, NAVY2);
  cartaoPainel_(sh, lin, 6, 'Custo total', custo, '#b0413f');
  cartaoPainel_(sh, lin, 8, 'MC média', venda ? margem / venda : 0, '#2f7d4f', '0.0%');
  lin += 4;

  secaoPainel_(sh, lin, 'PROJETO A PROJETO', W); lin += 2;
  const l0 = lin;
  const tot = ['Total', '', '', '', '', venda, custo, margem, venda ? margem / venda : 0];
  lin = tabelaPainel_(sh, lin, 2, CAB, linhas.concat([tot]), FMT);
  sh.getRange(l0 + linhas.length + 1, 2, 1, CAB.length)
    .setBackground(NAVY).setFontColor(GOLDS).setFontWeight('bold');
  if (linhas.length) {
    const mc = sh.getRange(l0 + 1, 10, linhas.length, 1);
    const ent = sh.getRange(l0 + 1, 5, linhas.length, 1);
    sh.setConditionalFormatRules([
      SpreadsheetApp.newConditionalFormatRule().whenNumberLessThan(0.25)
        .setBackground('#fcf2f1').setFontColor('#b0413f').setBold(true).setRanges([mc]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenNumberBetween(0.25, 0.35)
        .setBackground('#fdf8ee').setFontColor('#c47d0e').setBold(true).setRanges([mc]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenNumberGreaterThan(0.35)
        .setBackground('#eff5f1').setFontColor('#2f7d4f').setBold(true).setRanges([mc]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Atrasado')
        .setBackground('#fcf2f1').setFontColor('#b0413f').setBold(true).setRanges([ent]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Em produção')
        .setBackground('#f0f4f9').setFontColor('#2f5d8c').setBold(true).setRanges([ent]).build(),
      SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('No prazo')
        .setBackground('#eff5f1').setFontColor('#2f7d4f').setBold(true).setRanges([ent]).build(),
    ]);
  }

  SpreadsheetApp.flush();
  return linhas.length + ' projeto(s)';
}


// ════════════════════════════════════════════════════════════════════════
//  ATUALIZAÇÃO AUTOMÁTICA
// ════════════════════════════════════════════════════════════════════════
//
// O painel é feito de valores, não de fórmulas — de propósito, para o Walton
// não alcançar as planilhas de origem nem pelo texto de uma fórmula. O preço
// é que ele não se atualiza sozinho: alguém tem de mandar.
//
// Estas duas funções resolvem isso. Instale uma vez e o Google passa a rodar
// o atualizarTudo todo dia de madrugada, sem ninguém abrir nada.

function instalarAtualizacaoAutomatica() {
  // tira o que já houver, para não acumular gatilho repetido a cada instalação
  let removidos = 0;
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'atualizarTudo') {
      ScriptApp.deleteTrigger(t);
      removidos++;
    }
  });
  ScriptApp.newTrigger('atualizarTudo').timeBased().atHour(5).everyDays(1).create();
  const r = 'atualizarTudo passa a rodar todo dia por volta das 5h'
          + (removidos ? ' (' + removidos + ' agendamento[s] antigo[s] removido[s])' : '');
  console.log(r);
  return r;
}

function removerAtualizacaoAutomatica() {
  let n = 0;
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'atualizarTudo') { ScriptApp.deleteTrigger(t); n++; }
  });
  console.log(n + ' agendamento(s) removido(s). O painel volta a depender de execução manual.');
  return n;
}
