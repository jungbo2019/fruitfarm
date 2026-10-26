from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge')
    page = browser.new_page(viewport={'width': 1280, 'height': 800})

    # 1. Hero
    page.goto('http://127.0.0.1:5000/')
    time.sleep(1)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_hero_contrast_fixed.png')

    # 2. Login
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    time.sleep(1)

    # 3. Operations
    page.goto('http://127.0.0.1:5000/admin/operations')
    time.sleep(1)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_admin_operations_fixed.png')

    # 4. Products
    page.goto('http://127.0.0.1:5000/admin/products')
    time.sleep(1)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_admin_products_fixed.png')

    browser.close()
    print("Recapture complete!")
