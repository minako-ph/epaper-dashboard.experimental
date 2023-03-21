const puppeteer = require('puppeteer');     //Puppeteerの定義
const urlList = require('./urlList.json');   //URL一覧の読み込み
(async () => {
  //ブラウザ起動
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--user-data-dir=/home/pi/.config/chromium/Profile 3'
    ],
    executablePath: '/usr/bin/chromium-browser',
  });
  //タブ展開
  const page = await browser.newPage();
  //Viewportの設定
  await page.setViewport({ width: 1080, height: 768 });
  for (key in urlList) {
    //ページ遷移
    await page.goto(urlList[key].url, { waitUntil: 'networkidle2' });
    //スクリーンショットの取得と保存
    await page.screenshot({ path: `../../pic/${urlList[key].saveFileName}.png`, fullPage: true });
  }
  await browser.close();
})();
