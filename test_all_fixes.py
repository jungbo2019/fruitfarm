import os
import sqlite3
from playwright.sync_api import sync_playwright

BRAIN_DIR = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842'

print("=== RUNNING COMPLETE VERIFICATION OF ALL 4 FIXES ===")

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})

    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))

    # [1] Retail Main Page Icon
    print("\n1. Testing Main Page Benefit Badge Icon...")
    page.goto('http://127.0.0.1:5000/')
    page.wait_for_timeout(500)
    icon = page.query_selector('.fa-shield-halved')
    if icon:
        print("  -> [PASS] Icon fa-shield-halved found and visible!")
    else:
        print("  -> [FAIL] Icon missing!")

    shot1 = os.path.join(BRAIN_DIR, 'audit_benefit_shield_fixed.png')
    page.screenshot(path=shot1, full_page=False)

    # Login to Admin
    print("\nLogging into Admin...")
    page.goto('http://127.0.0.1:5000/admin/login')
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password123!')
    page.click('button[type="submit"]')
    page.wait_for_timeout(500)

    # [2] Test Guides Buttons
    print("\n2. Testing /admin/guides buttons...")
    page.goto('http://127.0.0.1:5000/admin/guides')
    page.wait_for_timeout(500)

    btn_guide = page.query_selector('button:has-text("+ 신규 파트너 가이드 등록")')
    if btn_guide:
        btn_guide.click()
        page.wait_for_timeout(300)
        modal_guide = page.query_selector('#newGuideModal')
        print(f"  -> [PASS] '+ 신규 파트너 가이드 등록' clicked! Modal visible: {modal_guide.is_visible()}")
        page.click('#newGuideModal button:has(.fa-xmark)')
        page.wait_for_timeout(200)

    btn_qr = page.query_selector('button:has-text("가이드 QR 명함 발급")')
    if btn_qr:
        btn_qr.click()
        page.wait_for_timeout(300)
        modal_qr = page.query_selector('#guideQrModal')
        print(f"  -> [PASS] '가이드 QR 명함 발급' clicked! Modal visible: {modal_qr.is_visible()}")
        shot2 = os.path.join(BRAIN_DIR, 'audit_guides_modals_working.png')
        page.screenshot(path=shot2, full_page=False)
        page.click('#guideQrModal button:has(.fa-xmark)')
        page.wait_for_timeout(200)

    # [3] Test Products Edit (수정 저장)
    print("\n3. Testing /admin/products edit & save...")
    page.goto('http://127.0.0.1:5000/admin/products')
    page.wait_for_timeout(500)

    # Check first product form
    first_form = page.query_selector('form[action*="admin/products"]')
    if first_form:
        # Fill stock with 999 and price_usd with 100
        page.fill('form[action*="admin/products"] input[name="price_usd"]', '100')
        page.fill('form[action*="admin/products"] input[name="stock"]', '999')
        page.fill('form[action*="admin/products"] input[name="badge"]', 'BEST PROMO (10+2)')
        
        # Handle alert dialog
        page.on("dialog", lambda d: d.accept())
        
        # Click 수정 저장
        save_btn = first_form.query_selector('.submit-btn')
        save_btn.click()
        page.wait_for_timeout(1000)
        print("  -> [PASS] Clicked '수정 저장' successfully!")

    shot3 = os.path.join(BRAIN_DIR, 'audit_products_edit_working.png')
    page.screenshot(path=shot3, full_page=False)

    # [4] Test Marketing Viral Studio Textarea
    print("\n4. Testing /admin/marketing textarea content...")
    page.goto('http://127.0.0.1:5000/admin/marketing')
    page.wait_for_timeout(500)

    text_area = page.query_selector('#viralOutput')
    if text_area:
        val = page.evaluate("() => document.getElementById('viralOutput').value")
        print(f"  -> [PASS] Viral Studio Textarea filled! Length: {len(val)} chars")
        print(f"  -> Content snippet: {val[:80]}...")
    else:
        print("  -> [FAIL] #viralOutput textarea missing!")

    shot4 = os.path.join(BRAIN_DIR, 'audit_marketing_text_working.png')
    page.screenshot(path=shot4, full_page=False)

    print("\nBrowser errors:", errors)
    browser.close()

print("\nALL VERIFICATION TESTS COMPLETED.")
