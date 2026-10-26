from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1366, 'height': 820})
    
    page.goto('http://127.0.0.1:5000/')
    page.evaluate('localStorage.clear(); sessionStorage.clear();')
    page.reload()
    page.wait_for_timeout(1000)

    # 1. Hero
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_polished_hero.png')
    print('1. Polished Hero saved!')

    # 2. Gallery
    page.evaluate('window.scrollTo(0, 650)')
    page.wait_for_timeout(600)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_polished_gallery.png')
    print('2. Polished Gallery saved!')

    # 3. 10+2 Builder (Fruit Photos)
    builder = page.query_selector('#custom-builder')
    if builder:
        builder.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_polished_builder_fruits.png')
        print('3. Polished Builder Fruit Photos saved!')

    # 4. Products Section
    prods = page.query_selector('#products')
    if prods:
        prods.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_polished_products.png')
        print('4. Polished Products saved!')

    browser.close()
    print('All visual checks done!')
