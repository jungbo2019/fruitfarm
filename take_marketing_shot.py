import os
from playwright.sync_api import sync_playwright

BRAIN_DIR = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842'

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})

    # Login to Admin
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(500)

    # Marketing page
    page.goto('http://127.0.0.1:5000/admin/marketing')
    page.wait_for_timeout(500)

    shot = os.path.join(BRAIN_DIR, 'audit_marketing_text_working.png')
    page.screenshot(path=shot, full_page=False)
    print("Marketing screenshot saved.")
    browser.close()
