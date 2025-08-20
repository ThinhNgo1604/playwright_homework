from playwright.sync_api import sync_playwright

#C0rny-Mac: input in terminal:
    # python test_auto_wait.py
# This script demonstrates Playwright's auto-waiting feature for elements
# This test will automatically wait for the element to be ready before clicking
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("file:////Users/thinhngo/Documents/My Python/playwright/Session7/demo-auto-wait.html")  # nhớ đổi path tới file demo.html

    print("⏳ Trying to click Submit...")
    page.click("#submit")   # Playwright sẽ tự động CHỜ ~5s

    print("✅ Click successful!")
    browser.close()


# C0rny-Mac: input in terminal:
    # pytest -v -s test_auto_wait.py --browser chromium --headed -k test_auto_wait_animte
# This test will automatically wait for the element to be ready before clicking
def test_auto_wait_animte(page):
    page.goto("file:////Users/thinhngo/Documents/My Python/playwright/Session7/demo-animate.html") # nhớ đổi path tới file demo.html
    page.click("#moving") # Playwright sẽ tự động chờ cho đến khi phần tử sẵn sàng để click
    print("✅ Click on moving element successful!")

# C0rny-Mac: input in terminal:
    # pytest -v -s test_auto_wait.py --browser chromium --headed -k test_auto_wait_overlay
def test_auto_wait_overlay(page):
    page.goto("file:////Users/thinhngo/Documents/My Python/playwright/Session7/demo-overlay.html") # nhớ đổi path tới file demo.html
    page.click("#target") # Playwright sẽ tự động chờ cho đến khi phần tử sẵn sàng để click
    print("✅ Click on overlay button successful!")