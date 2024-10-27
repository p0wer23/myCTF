const puppeteer = require('puppeteer');

async function visit(url, cookie_url) {
  try {
    const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
    const page = await browser.newPage({ headless: true });
    const secret = '0SMnNKmEmLb6A8XDRqTNd0MWmC6u5937dAdL9rqXMTnP7MJMkmEBefAJgqfavZaZqt9mbgpSWYJwhZUkfgf3UAw7RVpGxRHHWFQ6U128cJ2KnaREbjqGLDMM2E4A0nKE';
    cookie_url = cookie_url + 'get_cookie?secret=' + secret;
    const res = await set_cookie(page, cookie_url);
    page.setDefaultNavigationTimeout(20000);

    await page.goto(url);
    console.log(`Opened ${url} successfully.`);
    await browser.close();
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

async function set_cookie(page, cookie_url) {
    const res = await page.goto(cookie_url);
    return res;
}


module.exports = {visit}
