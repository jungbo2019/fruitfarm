from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1366, 'height': 850})
    
    page.goto('http://127.0.0.1:5000/')
    page.evaluate('localStorage.clear(); sessionStorage.clear();')
    page.reload()
    page.wait_for_timeout(1000)

    # 1. 10+2 Custom Builder Button & Prices (No .00)
    builder = page.query_selector('#custom-builder')
    if builder:
        builder.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_cents_builder.png')
        print('1. Builder prices screenshot saved!')

    # 2. Catalog Section (Real Photos, No 2호점, $10 / $20 No .00)
    prods = page.query_selector('#products')
    if prods:
        prods.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_catalog_photos.png')
        print('2. Catalog photos screenshot saved!')

    # 3. Flagship Store Section (Color check: bold dark text on clean white card)
    store = page.query_selector('#store-location')
    if store:
        store.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_flagship_store.png')
        print('3. Flagship store colors screenshot saved!')

    # 4. Footer Guarantee Block (No $150 customs, No FEFO, replaced with clean benefits)
    footer = page.query_selector('footer')
    if footer:
        footer.scroll_into_view_if_needed()
        page.wait_for_timeout(600)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_guarantee.png')
        print('4. Footer guarantee screenshot saved!')

    browser.close()
    print('All audit screenshots saved successfully!')
