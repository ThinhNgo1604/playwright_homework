import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def custom_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_with_custom_page(custom_page):
    custom_page.goto("https://example.com")
    print(custom_page.title())
    assert custom_page.title() == "Example Domai"
