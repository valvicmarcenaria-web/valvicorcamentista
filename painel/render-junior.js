const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  for (const [src, out] of [
    ['escopo-marceneiro-junior-clt.html', 'Valvic_Escopo_Marceneiro_Junior_CLT.pdf'],
    ['escopo-marceneiro-junior-pj.html',  'Valvic_Escopo_Marceneiro_Junior_PJ.pdf'],
  ]) {
    const p = await b.newPage();
    await p.goto('file://' + __dirname + '/' + src, { waitUntil: 'networkidle', timeout: 60000 });
    try { await p.evaluate(() => document.fonts.ready); } catch (e) {}
    await p.pdf({ path: __dirname + '/' + out, format: 'A4', printBackground: true,
                  margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    await p.close();
    console.log('gerado: ' + out);
  }
  await b.close();
})();
