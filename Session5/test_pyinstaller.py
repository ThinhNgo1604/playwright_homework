import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

def resource_path(relative_path):
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).parent
    return str(base_path / relative_path)

if __name__ == "__main__":
    chromium_path = resource_path("playwright/chromium")

    # ✅ Gán full quyền thực thi (khắc phục EACCES)
    os.chmod(chromium_path, 0o755)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000,
            executable_path=chromium_path
        )
        page = browser.new_page()
        page.goto("https://playwright.dev")
        page.screenshot(path="playwright_screenshot.png")
        browser.close()
