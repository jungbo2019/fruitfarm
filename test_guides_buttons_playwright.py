from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})

    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))

    # Login
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(500)

    # 1. Guides Page
    page.goto('http://127.0.0.1:5000/admin/guides')
    page.wait_for_timeout(500)

    # Check button 1: New Guide
    btn1 = page.query_selector('button:has-text("+ 신규 파트너 가이드 등록")')
    print("Found btn1 (+ 신규 파트너 가이드 등록):", btn1 is not None)
    if btn1:
        btn1.click()
        page.wait_for_timeout(300)
        modal1 = page.query_selector('#newGuideModal')
        is_visible1 = modal1.is_visible()
        print("Is newGuideModal visible after click?:", is_visible1)

    # Close modal 1
    page.click('#newGuideModal button:has(.fa-xmark)')
    page.wait_for_timeout(300)

    # Check button 2: Guide QR Card
    btn2 = page.query_selector('button:has-text("가이드 QR 명함 발급")')
    print("Found btn2 (가이드 QR 명함 발급):", btn2 is not None)
    if btn2:
        btn2.click()
        page.wait_for_timeout(300)
        modal2 = page.query_selector('#guideQrModal')
        is_visible2 = modal2.is_visible()
        print("Is guideQrModal visible after click?:", is_visible2)

    print("Browser errors:", errors)
    browser.close()
