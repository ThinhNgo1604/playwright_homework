import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.wikipedia.org/")
    await page.get_by_role("searchbox", name="Search Wikipedia").click()
    await page.get_by_role("searchbox", name="Search Wikipedia").fill("cat")
    await page.get_by_role("link", name="Cat Small domesticated").click()
    await page.locator("div:nth-child(3) > div > div > span > .mw-file-description").first.click()
    await page.locator(".mw-mmv-final-image").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())