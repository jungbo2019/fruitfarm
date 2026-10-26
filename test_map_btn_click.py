import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()

    page.goto('http://127.0.0.1:5000/')
    page.wait_for_timeout(1000)

    # Find the link containing '구글 지도에서 매장 찾기'
    btn = page.query_selector('text="구글 지도에서 매장 찾기"')
    if btn:
        print("Found element:", btn)
        tag = btn.evaluate("el => el.tagName")
        parent = btn.evaluate("el => el.parentElement.outerHTML")
        href = btn.evaluate("el => el.getAttribute('href') || el.parentElement.getAttribute('href')")
        print(f"Tag: {tag}, Href: {href}")
        print("Parent HTML:", parent[:200])

        # Test clicking it and seeing what page/event triggers
        with page.expect_popup() as popup_info:
            btn.click()
        popup = popup_info.value
        print("Popup opened URL:", popup.url)
    else:
        print("NOT FOUND!")

    browser.close()
