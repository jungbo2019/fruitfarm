import sys
import os
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def audit_facts_and_ui():
    console_errors = []
    page_logs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=True)
        page = browser.new_page(viewport={'width': 1440, 'height': 1200})

        # Capture console messages and errors
        page.on('console', lambda msg: page_logs.append(f"[{msg.type}] {msg.text}"))
        page.on('pageerror', lambda err: console_errors.append(str(err)))

        print("Navigating to http://127.0.0.1:5000/ ...")
        page.goto('http://127.0.0.1:5000/', wait_until='networkidle')

        # 1. Check title & text
        title = page.title()
        print(f"Page Title: {title}")

        # 2. Check for '2호점' anywhere in DOM
        content = page.content()
        has_2hojeom = '2호점' in content
        print(f"Contains '2호점': {has_2hojeom}")

        # 3. Check Cart Button & Badge
        cart_badge = page.inner_text('#cartBadge') if page.query_selector('#cartBadge') else 'None'
        print(f"Initial Cart Badge: {cart_badge}")

        # 4. Click '장바구니 담기' on first product
        add_btn = page.query_selector('button[onclick*="addToCart"]')
        if add_btn:
            print(f"Clicking Add To Cart button...")
            add_btn.click()
            page.wait_for_timeout(600)
            new_badge = page.inner_text('#cartBadge') if page.query_selector('#cartBadge') else 'None'
            print(f"Cart Badge after click: {new_badge}")
        else:
            print("WARNING: No Add To Cart button found!")

        # 5. Check Cart Modal
        cart_modal = page.query_selector('#cartModal')
        is_cart_visible = cart_modal.is_visible() if cart_modal else False
        print(f"Cart Modal visible: {is_cart_visible}")

        # 6. Check Checkout Button inside Cart Modal
        checkout_btn = page.query_selector('#cartModal button[onclick*="openCheckoutModal"]')
        if checkout_btn:
            print(f"Clicking Checkout button...")
            checkout_btn.click()
            page.wait_for_timeout(600)
            checkout_modal = page.query_selector('#checkoutModal')
            is_checkout_visible = checkout_modal.is_visible() if checkout_modal else False
            print(f"Checkout Modal visible: {is_checkout_visible}")

        # 7. Check AI Chatbot Button
        ai_btn = page.query_selector('button[onclick*="openAIChatbot"]')
        if ai_btn:
            print("Clicking AI Chatbot button...")
            ai_btn.click()
            page.wait_for_timeout(500)
            ai_modal = page.query_selector('#aiChatModal')
            print(f"AI Chat Modal visible: {ai_modal.is_visible() if ai_modal else False}")

        # 8. Check DIY Package Builder
        diy_btn = page.query_selector('#btnCompleteDIY')
        if diy_btn:
            print(f"DIY Button status: disabled={diy_btn.is_disabled()}, text='{diy_btn.inner_text()}'")

        # 9. Screenshot for visual review
        screenshot_path = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_full_flow_live.png'
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to: {screenshot_path}")

        browser.close()

    print("\n--- CONSOLE ERRORS ---")
    print(f"Total Errors: {len(console_errors)}")
    for err in console_errors:
        print(" [ERROR]:", err)

    print("\n--- RECENT PAGE LOGS ---")
    for log in page_logs[-10:]:
        print(" ", log)

if __name__ == '__main__':
    audit_facts_and_ui()
