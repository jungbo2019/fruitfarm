from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1366, 'height': 850})
    
    page.goto('http://127.0.0.1:5000/')
    page.evaluate('localStorage.clear(); sessionStorage.clear();')
    page.reload()
    page.wait_for_timeout(1000)

    # 1. 10+2 Custom Builder
    builder = page.query_selector('#custom-builder')
    if builder:
        builder.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_builder_fixed.png')
        print('1. Builder fixed screenshot saved!')

    # 2. Products Grid
    prods = page.query_selector('#products')
    if prods:
        prods.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_products_fixed.png')
        print('2. Products fixed screenshot saved!')

    # 3. Promo Sets
    promo = page.query_selector('#promo')
    if promo:
        promo.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_promo_fixed.png')
        print('3. Promo fixed screenshot saved!')

    browser.close()
    print('Audit capture complete!')
