import os
from playwright.sync_api import sync_playwright

BRAIN_DIR = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842'

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 800, 'height': 800})
    page.goto('http://127.0.0.1:5000/admin/login')
    page.wait_for_timeout(500)
    shot_path = os.path.join(BRAIN_DIR, 'audit_login_clean_verified.png')
    page.screenshot(path=shot_path)
    print(f"[SUCCESS] Login screenshot saved: {shot_path}")
    browser.close()
