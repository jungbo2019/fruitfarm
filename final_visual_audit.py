from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    # Test at typical laptop resolution 1366x768
    page = browser.new_page(viewport={'width': 1366, 'height': 820})
    
    # Clear localStorage so no stale guide keys remain
    page.goto('http://127.0.0.1:5000/')
    page.evaluate('localStorage.clear(); sessionStorage.clear();')
    page.reload()
    page.wait_for_timeout(1000)

    # 1. Hero & Header Screenshot
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_final_retail_hero.png')
    print('1. Hero & Header screenshot saved!')

    # 2. Scroll to Showroom Gallery
    page.evaluate('window.scrollTo(0, 750)')
    page.wait_for_timeout(600)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_final_retail_gallery.png')
    print('2. Showroom Gallery screenshot saved!')

    # 3. Scroll to 10+2 Builder (Check Fruit Photos)
    page.evaluate('window.scrollTo(0, 1600)')
    page.wait_for_timeout(600)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_final_retail_builder.png')
    print('3. 10+2 Builder fruit photos screenshot saved!')

    browser.close()
    print('Playwright visual audit finished!')
