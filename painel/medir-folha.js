const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.goto('file://' + __dirname + '/escopo-marceneiro-junior-folha-unica.html',
               { waitUntil: 'networkidle', timeout: 60000 });
  try { await p.evaluate(() => document.fonts.ready); } catch (e) {}
  const m = await p.evaluate(() => {
    const sh = document.querySelector('.sheet'), bd = document.querySelector('.body');
    return { sheetH: sh.clientHeight, sheetScroll: sh.scrollHeight,
             bodyH: bd.clientHeight, bodyScroll: bd.scrollHeight };
  });
  console.log('folha: ' + m.sheetH + 'px de altura, conteudo ' + m.sheetScroll + 'px');
  console.log('corpo: ' + m.bodyH + 'px de altura, conteudo ' + m.bodyScroll + 'px');
  const over = m.bodyScroll - m.bodyH;
  console.log(over > 1 ? ('>>> TRANSBORDA ' + over + 'px — vai cortar') : '>>> CABE na folha');
  await p.pdf({ path: __dirname + '/Valvic_Escopo_Marceneiro_Junior_Folha_Unica.pdf',
                format: 'A4', printBackground: true, margin: {top:0,right:0,bottom:0,left:0} });
  await b.close();
})();
