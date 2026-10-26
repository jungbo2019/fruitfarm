from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge')
    page = browser.new_page(viewport={'width': 1280, 'height': 800})

    page.goto('http://127.0.0.1:5000/')
    time.sleep(1)

    # 1. Full Hero Section
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_hero_full.png')

    # 2. Scroll to Promo Section
    page.locator('#promo').scroll_into_view_if_needed()
    time.sleep(0.5)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_fixed_promo_section.png')

    browser.close()
    print("Feedback verification screenshots captured successfully!")
