import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()

    page.on('response', lambda res: print(f"HTTP {res.status} on: {res.url}") if res.status >= 400 else None)

    page.goto('http://127.0.0.1:5000/')
    page.wait_for_timeout(1000)
    browser.close()
