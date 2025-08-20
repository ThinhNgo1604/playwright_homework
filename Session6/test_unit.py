import unittest
import pytest
from playwright.sync_api import Page

class PlaywrightTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
    
    def test_foobar(self):
        self.page.goto("https://example.com")
        # assert self.page.title() == "Example Domain"
        assert self.page.evaluate("document.title") == "Example Domain"
        print("Page title is:", self.page.evaluate("document.title"))
        assert self.page.evaluate("window.location.href") == "https://example.com/"
        print("Page URL is:", self.page.evaluate("window.location.href"))
        assert self.page.evaluate("window.location.hostname") == "example.com"
        print("Page hostname is:", self.page.evaluate("window.location.hostname"))

# C0rny-Mac: input in terminal:
    # pytest -v -s test_unit.py --browser chromium --headed -k test_foobar

def test_youtube_title(page):
    page.goto("https://www.youtube.com")
    page.locator("input[name='search_query']").fill("cat videos")
    page.locator("input[name='search_query']").press("Enter")
    page.wait_for_timeout(3000)  # đợi kết quả hiện ra

    # Lấy tiêu đề trang bằng evaluate
    title = page.evaluate("document.title")
    print("Page title is:", title)
    assert "you" in title