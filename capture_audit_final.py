from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge')
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        # 1. Capture Hero Section
        print("Capturing Hero Section...")
        page.goto('http://127.0.0.1:5000/')
        time.sleep(1)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_hero_contrast_fixed.png')

        # 2. Login to Admin
        print("Logging into Admin...")
        page.goto('http://127.0.0.1:5000/admin/login')
        page.fill('input[name="username"]', 'admin')
        page.fill('input[name="password"]', 'password123!')
        page.click('button[type="submit"]')
        time.sleep(1)

        # 3. Capture Admin Operations & Virtual Tour
        print("Capturing Admin Operations...")
        page.goto('http://127.0.0.1:5000/admin/operations')
        time.sleep(1)
        # Click tour button to trigger mouse simulation
        try:
            page.click('#runTourBtn')
            time.sleep(1.2) # wait for virtual cursor to glide to step 1
        except Exception as e:
            print("Tour click note:", e)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_admin_operations_fixed.png')

        # 4. Capture Admin Orders Pipeline
        print("Capturing Admin Orders...")
        page.goto('http://127.0.0.1:5000/admin/orders')
        time.sleep(1)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_admin_orders_fixed.png')

        # 5. Capture Admin Products (Verify all 16 photos & no duplicates)
        print("Capturing Admin Products...")
        page.goto('http://127.0.0.1:5000/admin/products')
        time.sleep(1)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_admin_products_fixed.png')

        # 6. Capture Admin Marketing
        print("Capturing Admin Marketing...")
        page.goto('http://127.0.0.1:5000/admin/marketing')
        time.sleep(1)
        page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_admin_marketing_fixed.png')

        browser.close()
        print("All audit screenshots captured successfully!")

if __name__ == '__main__':
    run()
