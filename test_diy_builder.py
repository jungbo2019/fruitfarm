import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def test_diy_builder():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=True)
        page = browser.new_page(viewport={'width': 1440, 'height': 900})

        page.goto('http://127.0.0.1:5000/')
        page.wait_for_timeout(1000)

        # Check initial state
        btn = page.query_selector('#btnCompleteDIY')
        assert btn.is_disabled(), "Button should initially be disabled"
        print("Initial DIY button is disabled as expected.")

        # Click '+' 10 times on first regular item
        plus_btn_regular = page.query_selector('button[onclick*="updateBuilderRegular"]')
        if plus_btn_regular:
            for i in range(10):
                plus_btn_regular.click(force=True)
            print("Clicked 10 regular items.")

        page.wait_for_timeout(500)

        # Click '+' 2 times on first bonus item
        plus_btn_bonus = page.query_selector('button[onclick*="updateBuilderBonus"]')
        if plus_btn_bonus:
            for i in range(2):
                plus_btn_bonus.click(force=True)
            print("Clicked 2 bonus items.")

        # Check button status
        page.wait_for_timeout(500)
        btn_disabled = btn.is_disabled()
        print(f"DIY button disabled after 10+2 selection: {btn_disabled}")
        assert not btn_disabled, "Button should be enabled when 10 regular + 2 bonus items are selected!"

        # Handle alert
        page.on('dialog', lambda d: d.accept())
        btn.click(force=True)
        page.wait_for_timeout(600)

        # Check if cart modal opened
        cart_modal = page.query_selector('#cartModal')
        assert cart_modal.is_visible(), "Cart modal should open after DIY package added!"
        print("PASS: 10+2 DIY Builder works and opens cart modal successfully!")

        browser.close()

if __name__ == '__main__':
    test_diy_builder()
