import os
import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def test_product_image_edit():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=True)
        page = browser.new_page(viewport={'width': 1440, 'height': 900})

        # 1. Login
        print("Logging in...")
        page.goto('http://127.0.0.1:5000/admin/login')
        page.fill('input[name="username"]', 'admin')
        page.fill('input[name="password"]', 'password123!')
        page.click('button[type="submit"]')
        page.wait_for_timeout(1000)

        # 2. Go to Products
        print("Navigating to /admin/products...")
        page.goto('http://127.0.0.1:5000/admin/products')
        page.wait_for_timeout(1000)

        # 3. Check elements
        camera_btn = page.query_selector('label:has-text("사진 교체")')
        url_input = page.query_selector('input[name="image_url"]')

        print("Camera '사진 교체' button found:", camera_btn is not None)
        print("Image URL input found:", url_input is not None)
        assert camera_btn is not None, "Camera button should exist!"
        assert url_input is not None, "Image URL input should exist!"

        # 4. Take Screenshot of upgraded UI
        screenshot_path = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_admin_products_image_edit.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

        browser.close()
        print("PASS: Admin product photo edit UI verified successfully!")

if __name__ == '__main__':
    test_product_image_edit()
