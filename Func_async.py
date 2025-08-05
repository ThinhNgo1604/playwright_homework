
import asyncio
from playwright.async_api import async_playwright

async def open_page(url, delay):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=delay)
        page = await browser.new_page()
        await page.goto(url)
        print(f"Title of {url}: {await page.title()}")
        await browser.close()

async def main():
    # Dùng asyncio.gather để chạy 2 tác vụ song song
    await asyncio.gather(
        open_page("https://playwright.dev", 500),
        open_page("https://www.python.org", 500)
    )

asyncio.run(main())