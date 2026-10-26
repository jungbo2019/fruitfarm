from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()

    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("console", lambda msg: print(f"CONSOLE [{msg.type}]: {msg.text}"))

    # Login
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(500)

    # Go to /admin/guides
    page.goto('http://127.0.0.1:5000/admin/guides')
    page.wait_for_timeout(500)

    print("Page errors on /admin/guides:", errors)

    # Try clicking the new guide button
    btn = page.query_selector('button:has-text("신규 파트너 가이드 등록")')
    print("Found button:", btn is not None)
    if btn:
        btn.click()
        page.wait_for_timeout(300)
        modal = page.query_selector('#newGuideModal')
        print("Modal class after click:", modal.get_attribute('class'))

    browser.close()
