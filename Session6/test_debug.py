# COrny-Mac: input in terminal:
# pytest -v test_debug.py --browser chromium  --headed -k test_bing
    #(Pdb) page.locator("textarea[name=\"q\"]").click()
    #(Pdb) page.fill("textarea[name=\"q\"]", "dog")
    #(Pdb) page.press("textarea[name=\"q\"]", "Enter")
def test_bing(page):
    page.goto("https://www.bing.com")
    breakpoint()



# C0rny-Mac: input in terminal:
    # pytest -v test_debug.py --browser chromium  --headed -k test_youtube
def test_youtube(page):
    page.goto("https://www.youtube.com")
    page.pause() # This will pause the test execution, allowing you to inspect the page
    page.locator("input[name=\"search_query\"]").fill("dog")
    page.locator("input[name=\"search_query\"]").press("Enter")

# COrny-Mac: input in terminal:
    # pytest -v test_debug.py --browser chromium  --headed -k test_fail
    # This test is designed to fail and take a screenshot
import time
timestamp = int(time.time()) # to create a unique filename for the screenshot
def test_fail(page):
    page.goto("https://example.com")
    page.screenshot(path=f"screenshot_{timestamp}.png")
    assert False  # ép fail để test