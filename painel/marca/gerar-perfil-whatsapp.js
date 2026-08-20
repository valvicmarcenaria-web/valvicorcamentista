const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                                    args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 1000, height: 1000 }, deviceScaleFactor: 1 });
  await p.goto('file://' + __dirname + '/perfil.html');
  await p.waitForTimeout(2500);
  for (const id of ['c1','c2','c3','c4']) {
    await p.locator('#' + id).screenshot({ path: `${__dirname}/perfil-${id}.png` });
  }
  await b.close();
})();
