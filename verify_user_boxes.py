from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1366, 'height': 850})
    
    page.goto('http://127.0.0.1:5000/')
    page.evaluate('localStorage.clear(); sessionStorage.clear();')
    page.reload()
    page.wait_for_timeout(1000)

    # 1. Header & Cart Badge
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_cart_badge.png', clip={'x': 0, 'y': 0, 'width': 1366, 'height': 150})
    print('1. Cart badge screenshot saved!')

    # 2. Competitor Benchmark Table
    comp = page.query_selector('#competitor')
    if comp:
        comp.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_competitor_table.png')
        print('2. Competitor table screenshot saved!')

    browser.close()
    print('Visual audit completed!')
