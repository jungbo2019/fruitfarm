import os
import sys
from playwright.sync_api import sync_playwright

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

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

    # 1. Guides Page
    page.goto('http://127.0.0.1:5000/admin/guides')
    page.wait_for_timeout(500)
    shot_guides = os.path.join(BRAIN_DIR, 'audit_admin_guides_hub.png')
    page.screenshot(path=shot_guides, full_page=False)
    print(f"[PASS] Guides screenshot: {shot_guides}")

    # 2. Products Page with Merchandising Matrix
    page.goto('http://127.0.0.1:5000/admin/products')
    page.wait_for_timeout(500)
    shot_products = os.path.join(BRAIN_DIR, 'audit_admin_products_matrix.png')
    page.screenshot(path=shot_products, full_page=False)
    print(f"[PASS] Products matrix screenshot: {shot_products}")

    # 3. Marketing Page with Viral Studio Program
    page.goto('http://127.0.0.1:5000/admin/marketing')
    page.wait_for_timeout(500)
    shot_marketing = os.path.join(BRAIN_DIR, 'audit_admin_marketing_studio.png')
    page.screenshot(path=shot_marketing, full_page=False)
    print(f"[PASS] Marketing Viral Studio screenshot: {shot_marketing}")

    # 4. CRM & Customer Retention Page
    page.goto('http://127.0.0.1:5000/admin/crm')
    page.wait_for_timeout(500)
    shot_crm = os.path.join(BRAIN_DIR, 'audit_admin_crm_retention.png')
    page.screenshot(path=shot_crm, full_page=False)
    print(f"[PASS] CRM retention screenshot: {shot_crm}")

    # 5. Dashboard Value Chain
    page.goto('http://127.0.0.1:5000/admin/dashboard')
    page.wait_for_timeout(500)
    shot_dash = os.path.join(BRAIN_DIR, 'audit_admin_dashboard_valuechain.png')
    page.screenshot(path=shot_dash, full_page=False)
    print(f"[PASS] Dashboard value chain screenshot: {shot_dash}")

    browser.close()

print("ALL SCREENSHOTS CAPTURED SUCCESSFULLY.")
