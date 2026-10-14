/**
 * Valvic Marcenaria · botão "Abrir ficha do projeto"
 *
 * Onde mora: dentro da planilha CONTROLE DE PAGAMENTOS.
 *   Extensões → Apps Script → cole este arquivo inteiro → salve.
 *   Feche e abra a planilha: aparece o menu "Valvic" na barra de cima.
 *
 * O que faz, com a linha do projeto selecionada numa aba de ano:
 *   1. duplica a "Ficha Modelo" na Custo por Projeto
 *   2. nomeia a aba com o cliente
 *   3. preenche cliente, projeto e valor de venda
 *   4. registra a aba no Painel Geral, na primeira vaga livre
 *   5. estende a Base · Comissões com o bloco de 12 ambientes daquele projeto
 *
 * Por que botão e não automático: um gatilho onEdit criaria ficha a cada linha
 * digitada errada, a cada teste, a cada cliente que não fechou. Aqui a ficha
 * nasce quando alguém decide que o projeto existe.
 *
 * Se a Custo por Projeto for recriada noutro arquivo, troque o ID abaixo.
 */

const ID_CUSTO = '1tTJXG4w7lDvIcnd0dyr219-leOPwuURqrBk6lJIr18I';

// ── mapa da ficha. Se a estrutura mudar, é aqui que se acerta ────────────
const FICHA = {
  modelo: 'Ficha Modelo',
  painel: 'Painel Geral',
  base: 'Base · Comissões',
  cliente: 'A7',          // identificação
  dataEntrada: 'F7',
  projeto: 'A9',
  vendaRealizada: 'D28',  // bloco 1
  ambLinha0: 49,          // bloco 3 · primeiro ambiente
  ambQtd: 12,
  painelLinha0: 11,       // Painel Geral · primeira vaga de projeto
  painelLinhaF: 50,
  baseLinha0: 2,          // Base · primeira linha de dados
};

const COLS_AMB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'];


function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Valvic')
    .addItem('Abrir ficha do projeto selecionado', 'abrirFicha')
    .addSeparator()
    .addItem('Reconstruir a Base · Comissões', 'reconstruirBase')
    .addToUi();
}


function abrirFicha() {
  const ui = SpreadsheetApp.getUi();
  const aba = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const linha = aba.getActiveRange().getRow();

  if (!/^20\d\d$/.test(aba.getName())) {
    ui.alert('Selecione a linha do projeto numa aba de ano (2026, 2025...).');
    return;
  }

  const cliente = String(aba.getRange(linha, 1).getValue() || '').trim();
  const projeto = String(aba.getRange(linha, 2).getValue() || '').trim();
  const valor = aba.getRange(linha, 3).getValue();
  const data1 = aba.getRange(linha, 10).getValue();   // data do 1º pagamento

  if (!cliente || !valor) {
    ui.alert('Essa linha não tem cliente e investimento.\n\n' +
             'Selecione uma linha de projeto, não uma linha divisora de mês.');
    return;
  }

  const destino = SpreadsheetApp.openById(ID_CUSTO);
  if (destino.getSheetByName(cliente)) {
    ui.alert('Já existe uma aba chamada "' + cliente + '" na Custo por Projeto.\n\n' +
             'Se for outro projeto do mesmo cliente, mude o nome na coluna Cliente ' +
             'antes de abrir a ficha.');
    return;
  }

  const painel = destino.getSheetByName(FICHA.painel);
  const vaga = primeiraVaga_(painel);
  if (vaga < 0) {
    ui.alert('O Painel Geral está com as ' +
             (FICHA.painelLinhaF - FICHA.painelLinha0 + 1) +
             ' vagas de projeto ocupadas. Libere uma antes de abrir ficha nova.');
    return;
  }

  const r = ui.alert('Abrir ficha do projeto?',
    'Cliente: ' + cliente + '\n' +
    'Projeto: ' + (projeto || '(em branco)') + '\n' +
    'Valor: ' + valor + '\n\n' +
    'Vai criar a aba na Custo por Projeto, registrar no Painel Geral e estender a base.',
    ui.ButtonSet.OK_CANCEL);
  if (r !== ui.Button.OK) return;

  // 1 · duplica o modelo e nomeia
  const modelo = destino.getSheetByName(FICHA.modelo);
  const nova = modelo.copyTo(destino).setName(cliente);
  destino.setActiveSheet(nova);
  destino.moveActiveSheet(destino.getSheets().length - 1);

  // 2 · preenche o que já se sabe
  nova.getRange(FICHA.cliente).setValue(cliente);
  if (projeto) nova.getRange(FICHA.projeto).setValue(projeto);
  nova.getRange(FICHA.vendaRealizada).setValue(valor);
  let notaData = 'Data de entrada em branco — preencha na ficha.';
  if (data1 instanceof Date) {
    nova.getRange(FICHA.dataEntrada).setValue(data1);
    notaData = 'Data de entrada preenchida com a data do 1º pagamento — confira.';
  }

  // 3 · registra no Painel Geral
  painel.getRange(vaga, 2).setValue(cliente);

  // 4 · estende a base
  const i = vaga - FICHA.painelLinha0;
  escreverBlocoBase_(destino, i, cliente);

  SpreadsheetApp.flush();
  ui.alert('Ficha criada.',
    'A aba "' + cliente + '" existe na Custo por Projeto, registrada na linha ' +
    vaga + ' do Painel Geral.\n\n' + notaData + '\n\n' +
    'Falta preencher na ficha: vendedor, coordenador, entrega prevista e os ambientes.',
    ui.ButtonSet.OK);
}


/**
 * Reescreve a Base · Comissões inteira a partir do que está no Painel Geral.
 * Use quando a base e os projetos saírem de sincronia — por exemplo depois de
 * renomear uma aba à mão, ou de apagar um projeto.
 */
function reconstruirBase() {
  const ui = SpreadsheetApp.getUi();
  const r = ui.alert('Reconstruir a Base · Comissões?',
    'Reescreve as fórmulas da base a partir dos projetos registrados no Painel ' +
    'Geral. Não apaga nada das fichas nem das planilhas individuais.',
    ui.ButtonSet.OK_CANCEL);
  if (r !== ui.Button.OK) return;

  const destino = SpreadsheetApp.openById(ID_CUSTO);
  const painel = destino.getSheetByName(FICHA.painel);
  const nomes = painel.getRange(FICHA.painelLinha0, 2,
                                FICHA.painelLinhaF - FICHA.painelLinha0 + 1, 1).getValues();
  let n = 0;
  for (let i = 0; i < nomes.length; i++) {
    const nome = String(nomes[i][0] || '').trim();
    if (nome && destino.getSheetByName(nome)) {
      escreverBlocoBase_(destino, i, nome);
      n++;
    } else {
      limparBlocoBase_(destino, i);
    }
  }
  SpreadsheetApp.flush();
  ui.alert('Base reconstruída com ' + n + ' projeto(s).');
}


// ── auxiliares ──────────────────────────────────────────────────────────

/** Primeira linha livre do Painel Geral, ou -1 se não houver. */
function primeiraVaga_(painel) {
  const n = FICHA.painelLinhaF - FICHA.painelLinha0 + 1;
  const v = painel.getRange(FICHA.painelLinha0, 2, n, 1).getValues();
  for (let i = 0; i < n; i++) {
    if (!String(v[i][0] || '').trim()) return FICHA.painelLinha0 + i;
  }
  return -1;
}

/** Nome de aba dentro de fórmula: aspas simples dobradas. */
function ref_(nome) {
  return "'" + String(nome).replace(/'/g, "''") + "'";
}

/** Escreve as 12 linhas da base do projeto que ocupa o índice i. */
function escreverBlocoBase_(destino, i, nomeAba) {
  const base = destino.getSheetByName(FICHA.base);
  const r0 = FICHA.baseLinha0 + i * FICHA.ambQtd;
  const pgLinha = FICHA.painelLinha0 + i;
  const ab = ref_(nomeAba);
  const linhas = [];

  for (let j = 0; j < FICHA.ambQtd; j++) {
    const r = r0 + j;
    const fr = FICHA.ambLinha0 + j;
    const linha = [
      '=IF($C' + r + '="","",\'' + FICHA.painel + '\'!$B$' + pgLinha + ')',
      '=IF($C' + r + '="","",\'' + FICHA.painel + '\'!$C$' + pgLinha + ')',
    ];
    COLS_AMB.forEach(function (c) {
      linha.push('=IF(' + ab + '!$' + c + '$' + fr + '="","",' + ab + '!$' + c + '$' + fr + ')');
    });
    linha.push('=IF($C' + r + '="","",IF(' + ab + '!$F$7="","",' + ab + '!$F$7))');
    linhas.push(linha);
  }
  base.getRange(r0, 1, FICHA.ambQtd, linhas[0].length).setFormulas(linhas);
}

/** Limpa o bloco de um índice que não tem projeto. */
function limparBlocoBase_(destino, i) {
  const base = destino.getSheetByName(FICHA.base);
  const r0 = FICHA.baseLinha0 + i * FICHA.ambQtd;
  base.getRange(r0, 1, FICHA.ambQtd, 18).clearContent();
}
