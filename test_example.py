def test_example_is_working(page):
    page.goto("https://playwright.dev")
    assert "Playwright" in page.title()