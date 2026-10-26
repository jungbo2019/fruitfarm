from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()

    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(600)

    page.goto('http://127.0.0.1:5000/admin/marketing')
    page.wait_for_timeout(600)

    print("Current URL:", page.url)
    el = page.query_selector('#viralOutput')
    print("Found #viralOutput?:", el is not None)
    if el:
        val = page.evaluate("() => document.getElementById('viralOutput').value")
        print("Value length:", len(val))
        print("Value preview:", repr(val[:100]))
    browser.close()
