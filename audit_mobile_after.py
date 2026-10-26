import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

def audit_mobile_after():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome', headless=True)
        page = browser.new_page(
            viewport={'width': 390, 'height': 844},
            user_agent='Mozilla/5.0 (Linux; Android 13; SM-S918N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            device_scale_factor=2
        )

        page.goto('http://127.0.0.1:5000/', wait_until='networkidle')
        page.wait_for_timeout(1000)

        # 1. Capture Hero Section on Mobile
        hero_shot = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_mobile_hero_fixed.png'
        page.screenshot(path=hero_shot)
        print(f"Hero shot saved to: {hero_shot}")

        # 2. Scroll to Competitor Matrix and capture
        matrix = page.query_selector('#competitor-matrix')
        if matrix:
            matrix.scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            matrix_shot = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_mobile_matrix_fixed.png'
            page.screenshot(path=matrix_shot)
            print(f"Matrix shot saved to: {matrix_shot}")

        # 3. Scroll to Promo Cards and capture
        promo = page.query_selector('#promo')
        if promo:
            promo.scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            promo_shot = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_mobile_promo_fixed.png'
            page.screenshot(path=promo_shot)
            print(f"Promo shot saved to: {promo_shot}")

        # 4. Full page screenshot
        full_shot = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842\audit_mobile_full_fixed.png'
        page.screenshot(path=full_shot, full_page=True)
        print(f"Full mobile shot saved to: {full_shot}")

        browser.close()

if __name__ == '__main__':
    audit_mobile_after()
