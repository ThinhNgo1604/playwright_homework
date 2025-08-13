import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=500)
        page = await browser.new_page()
        await page.goto("http://google.com")
        print(await page.title())
        await browser.close()
asyncio.run(main())