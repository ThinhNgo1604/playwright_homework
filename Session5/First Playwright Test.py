import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo= 500 )
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()
asyncio.run(main())
