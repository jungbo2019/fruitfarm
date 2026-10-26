import os
from playwright.sync_api import sync_playwright

artifact_dir = r"C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842"
os.makedirs(artifact_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 950})

    # 1. Admin Login
    page.goto("http://127.0.0.1:5000/admin/login")
    page.fill('input[name="username"]', "admin")
    page.fill('input[name="password"]', "password123!")
    page.click('button[type="submit"]')
    page.wait_for_timeout(800)

    # 2. Go to Design Customizer Page
    page.goto("http://127.0.0.1:5000/admin/design")
    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(artifact_dir, "screen_admin_design.png"))
    print("Captured screen_admin_design.png")

    # 3. Desktop Main Page
    page.goto("http://127.0.0.1:5000")
    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(artifact_dir, "screen_desktop_main.png"))
    print("Captured screen_desktop_main.png")

    browser.close()

print("Captures completed successfully!")
