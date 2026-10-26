import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def audit_mobile():
    with sync_playwright() as p:
        # Emulate mobile Galaxy/iPhone viewport (width 390px, height 844px)
        browser = p.chromium.launch(channel='chrome', headless=True)
        page = browser.new_page(
            viewport={'width': 390, 'height': 844},
            user_agent='Mozilla/5.0 (Linux; Android 13; SM-S918N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            device_scale_factor=2
        )

        page.goto('http://127.0.0.1:5000/', wait_until='networkidle')
        page.wait_for_timeout(1000)

        # Full page screenshot
        full_shot = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_mobile_before.png'
        page.screenshot(path=full_shot, full_page=True)
        print(f"Mobile screenshot saved to: {full_shot}")

        browser.close()

if __name__ == '__main__':
    audit_mobile()
