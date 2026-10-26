import os
from playwright.sync_api import sync_playwright

BRAIN_DIR = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842'

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})

    # Login
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(500)

    # Marketing page
    page.goto('http://127.0.0.1:5000/admin/marketing')
    page.wait_for_timeout(500)
    shot_path = os.path.join(BRAIN_DIR, 'audit_marketing_no_discord.png')
    page.screenshot(path=shot_path, full_page=False)
    print(f"Captured clean marketing screenshot: {shot_path}")

    browser.close()
