import asyncio
from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page

async def main():
    browser: Browser = await launch(headless=False)
    page: Page = await browser.newPage()
    await page.goto("https://google.com")
    await page.screenshot({"path": "../../pic/pyppeteer.png"})
    await browser.close()

if __name__ == "__main__":
    asyncio.new_event_loop().run_until_complete(main())
