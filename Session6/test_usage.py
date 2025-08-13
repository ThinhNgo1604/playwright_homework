

def test_visit_youtube(page):
    page.goto("https://youtube.com")

def test_visit_https(page):
    page.goto("https://self-signed.badssl.com/")

def test_viewport_size(page, playwright):
    iphone_11 = playwright.devices["iPhone 11"]
    assert page.viewport_size["width"] ==  iphone_11["viewport"]["width"]
    assert page.viewport_size["height"] == iphone_11["viewport"]["height"]
