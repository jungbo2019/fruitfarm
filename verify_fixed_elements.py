import os
from playwright.sync_api import sync_playwright

BRAIN_DIR = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842'

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})

    # 1. Main Page Benefit Card & Icon Verification
    print("[1] Verifying Main Page Benefit Badge Icon...")
    page.goto('http://127.0.0.1:5000/')
    page.wait_for_timeout(500)

    # Scroll to benefit badge or card
    benefit_box = page.query_selector('.fa-shield-halved')
    if benefit_box:
        print("  -> [PASS] fa-shield-halved icon found and mounted!")
    else:
        print("  -> [FAIL] fa-shield-halved icon not found!")

    # Take screenshot of the exact benefit section
    benefit_card = page.query_selector('.border-b:has-text("안심 보증 & 특급 혜택")')
    if not benefit_card:
        # parent container
        benefit_card = page.query_selector('div:has-text("대한민국 100% 무사통관 보증제")')

    shot_benefit = os.path.join(BRAIN_DIR, 'audit_benefit_icon_fixed.png')
    page.screenshot(path=shot_benefit, full_page=False)
    print(f"  -> Saved benefit screenshot: {shot_benefit}")

    # 2. Marketing Viral Studio Verification
    print("\n[2] Verifying Marketing Viral Studio Textarea...")
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(500)

    page.goto('http://127.0.0.1:5000/admin/marketing')
    page.wait_for_timeout(500)

    viral_text = page.input_value('#viralOutput')
    print(f"  -> Viral Textarea length: {len(viral_text)} chars")
    if len(viral_text) > 50:
        print(f"  -> [PASS] Textarea is filled with content: {viral_text[:60]}...")
    else:
        print("  -> [FAIL] Textarea is still empty!")

    shot_marketing = os.path.join(BRAIN_DIR, 'audit_marketing_text_fixed.png')
    page.screenshot(path=shot_marketing, full_page=False)
    print(f"  -> Saved marketing studio screenshot: {shot_marketing}")

    browser.close()

print("\nALL VERIFICATIONS COMPLETE.")
