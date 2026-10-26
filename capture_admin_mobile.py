import sys
import os
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

artifact_dir = r"C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842"

with sync_playwright() as p:
    browser = p.chromium.launch(
        channel='msedge',
        headless=True,
        args=['--disable-blink-features=AutomationControlled', '--no-sandbox']
    )
    context = browser.new_context(
        viewport={'width': 390, 'height': 844},
        user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
    )
    page = context.new_page()

    # 1. Login
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(1000)

    # 2. Go to /admin/products
    page.goto('http://127.0.0.1:5000/admin/products')
    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(artifact_dir, 'audit_admin_mobile_products_fixed.png'))

    # 3. Test Mobile Drawer
    page.click('button[aria-label="메뉴 열기"]')
    page.wait_for_timeout(500)
    page.screenshot(path=os.path.join(artifact_dir, 'audit_admin_mobile_drawer.png'))

    print("Mobile admin screenshots captured successfully.")
    browser.close()
