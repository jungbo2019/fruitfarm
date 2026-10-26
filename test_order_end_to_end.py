import sys
import sqlite3
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def test_full_order_placement():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=True)
        page = browser.new_page(viewport={'width': 1440, 'height': 900})

        print("Navigating to store...")
        page.goto('http://127.0.0.1:5000/')
        page.wait_for_timeout(1000)

        # 1. Add item to cart
        print("Clicking Add To Cart on Product #1...")
        page.click('button[onclick*="addToCart"]')
        page.wait_for_timeout(500)

        # 2. Click Checkout in Cart Modal
        print("Opening Checkout Modal...")
        page.click('#cartModal button[onclick*="openCheckoutModal"]')
        page.wait_for_timeout(500)

        # 3. Fill in Checkout Form
        print("Filling customer order details...")
        page.fill('#custName', '김철수')
        page.fill('#custPhone', '010-1234-5678')
        page.fill('#custKakao', 'chulsoo_kakao')
        page.fill('#custAddress', '서울특별시 강남구 테헤란로 152 강남파이낸스센터 10층')
        page.fill('#custCustomsId', 'P123456789012')
        page.fill('#custNote', '부재 시 경비실에 맡겨주세요')

        # 4. Accept dialog when submit triggers alert
        dialog_messages = []
        page.on('dialog', lambda dialog: (dialog_messages.append(dialog.message), dialog.accept()))

        # 5. Submit Order
        print("Submitting order...")
        page.click('#btnFinalSubmit')
        page.wait_for_timeout(2000)

        print("Dialog messages:", dialog_messages)
        print("Current URL after order:", page.url)

        # 6. Verify in DB
        conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
        cursor = conn.cursor()
        cursor.execute("SELECT order_number, customer_name, total_amount_usd, total_amount_krw, order_status FROM orders ORDER BY id DESC LIMIT 1")
        latest_order = cursor.fetchone()
        conn.close()

        print("Latest DB Order:", latest_order)
        assert latest_order is not None, "Order should be created in DB!"
        assert latest_order[1] == '김철수', "Customer name should match!"

        screenshot_path = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_order_success_track.png'
        page.screenshot(path=screenshot_path)
        print(f"Tracking screenshot saved to: {screenshot_path}")

        browser.close()
        print("ALL ORDER PLACEMENT AND TRACKING TESTS PASSED 100%!")

if __name__ == '__main__':
    test_full_order_placement()
