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
  custoTotal: 'D22', margem: 'D23',   // bloco resumo · coluna D = realizado
  colsBase: 29,
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
const GOLDBG = '#f6edd6', MUTED = '#6c7785', OK = '#2f7d4f', ABERTO = '#c47d0e';
const AV0 = 4, AVF = 33;          // faixa de lançamentos da aba Avulsos
const MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
  'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
const MOEDA = 'R$ #,##0.00', PCT = '0.0%', DATA = 'dd/mm/yyyy';


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
  sh.setFrozenRows(1);
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
 * Completa a identificação e a venda de uma ficha que ficou pela metade.
 *
 * Escreve SÓ em célula vazia. Se já houver algo digitado, ela é pulada e o log
 * diz qual — preencher ficha não pode significar apagar o que alguém decidiu.
 *
 * Os dados vêm da Controle de Pagamentos. O que não está lá — vendedor,
 * coordenador, entrega prevista, quem produziu, quem montou, quem projetou e
 * os percentuais de comissão — continua em branco, porque é decisão sua e eu
 * não tenho de onde tirar.
 */
function completarFichas() {
  const PENDENTES = [
    { aba: 'Richard',
      cliente: 'Richard e Camila',
      projeto: 'Roupeiro',
      entrada: new Date(2026, 6, 27),      // 27/07/2026 · data do 1º pagamento
      venda: 19000,
      imposto: 0.05,                       // Simples, igual a todos os outros projetos
      ambientes: [['Roupeiro', 19000]] },
  ];

  const ss = SpreadsheetApp.openById(ID_CUSTO);
  PENDENTES.forEach(function (d) {
    const sh = ss.getSheetByName(d.aba);
    if (!sh) { console.log(d.aba + ': aba não encontrada.'); return; }
    console.log('── ' + d.aba + ' ──');

    const poe = function (ref, valor, rotulo) {
      const c = sh.getRange(ref);
      const atual = c.getValue();
      if (atual !== '' && atual !== null) {
        console.log('  pulei ' + ref + ' (' + rotulo + '): já tem "'
                    + c.getDisplayValue() + '"');
        return;
      }
      c.setValue(valor);
      console.log('  escrevi ' + ref + ' (' + rotulo + '): ' + c.getDisplayValue());
    };

    poe('A7', d.cliente, 'cliente');
    poe('A9', d.projeto, 'projeto');
    if (d.entrada) poe('F7', d.entrada, 'data de entrada');
    poe('D28', d.venda, 'valor de venda realizado');
    if (d.imposto != null) poe('B38', d.imposto, 'imposto sobre a nota');

    (d.ambientes || []).forEach(function (amb, i) {
      const r = FICHA.amb0 + i;
      poe('A' + r, amb[0], 'ambiente');
      poe('C' + r, amb[1], 'valor do ambiente');
    });
  });

  SpreadsheetApp.flush();
  console.log('\nFalta preencher à mão: vendedor, coordenador, entrega prevista, '
            + 'e no bloco de ambientes quem produziu, quem montou, quem projetou '
            + 'e os percentuais de cada um.');
  console.log('Depois disso, rode atualizarTudo para a Base e as individuais lerem.');
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
    diz('Painel Geral: ' + repararPainelGeral_() + ' projeto(s) registrado(s)');
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
    'Custos de venda',
    'Custo total do projeto', 'Margem de contribuição'];

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
      // custo total e margem: é daqui que sai a MC por projeto no painel
      L.push(cel_(ab, FICHA.custoTotal, r, false));
      L.push(cel_(ab, FICHA.margem, r, false));
    } else {
      L.push('', '', '', '', '', '', '', '', '', '', '');
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
    const nova = atual.replace(/!A1:[A-Z]+\d+/, '!A1:AC' + BASE_FIM);
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
