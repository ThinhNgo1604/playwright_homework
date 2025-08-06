import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)


    page.get_by_role("link", name="Polski 1 664 000+ haseł").click()
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("searchbox", name="Search Wikipedia").click()
    page.get_by_role("searchbox", name="Search Wikipedia").fill("cat")
    page.get_by_role("link", name="Cat Small domesticated").click()
    page.get_by_text("The cat (Felis catus), also").click()

    # ---------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
