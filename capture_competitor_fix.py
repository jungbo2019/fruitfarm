from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge')
    page = browser.new_page(viewport={'width': 1280, 'height': 800})

    page.goto('http://127.0.0.1:5000/')
    time.sleep(1)

    # Scroll to competitor matrix
    page.locator('#competitor-matrix').scroll_into_view_if_needed()
    time.sleep(0.5)

    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/audit_competitor_matrix_fixed.png')

    browser.close()
    print("Competitor matrix & calculator screenshot captured successfully!")
