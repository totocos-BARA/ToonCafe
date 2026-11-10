// 앱 아이콘 PNG를 만들어요. 사용법: node tools/make-icons.js
const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const b = await chromium.launch();
  for (const [name, size] of [["icon-512", 512], ["icon-maskable-512", 512], ["icon-192", 192], ["apple-touch-icon", 180]]) {
    const p = await b.newPage({ viewport: { width: 512, height: 512 }, deviceScaleFactor: size / 512 });
    await p.goto("file://" + path.join(__dirname, "icon.html"));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.locator("#i").screenshot({ path: path.join(__dirname, "..", "icons", name + ".png") });
    await p.close();
  }
  await b.close();
})();
