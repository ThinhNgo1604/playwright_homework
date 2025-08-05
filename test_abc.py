from playwright.sync_api import Page

def test_navigate(page : Page):
    page.goto("https://google.com")