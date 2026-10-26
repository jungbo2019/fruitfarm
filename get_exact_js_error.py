import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()

    failed_requests = []
    page_errors = []

    page.on('requestfailed', lambda req: failed_requests.append(f"{req.url} - {req.failure}"))
    page.on('response', lambda res: failed_requests.append(f"{res.url} - {res.status}") if res.status >= 400 else None)
    page.on('pageerror', lambda err: page_errors.append(err))

    page.goto('http://127.0.0.1:5000/')
    page.wait_for_timeout(1000)

    print("=== FAILED REQUESTS (404/ERR) ===")
    for req in failed_requests:
        print(req)

    print("\n=== PAGE ERRORS (EXACT STACK) ===")
    for err in page_errors:
        print(err)

    browser.close()
