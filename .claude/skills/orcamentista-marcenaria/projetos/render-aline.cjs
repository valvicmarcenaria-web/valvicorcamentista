const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + __dirname + '/proposta-aline.html', { waitUntil: 'networkidle' });
  await page.pdf({ path: 'proposta-aline.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('PDF ok');
})();
