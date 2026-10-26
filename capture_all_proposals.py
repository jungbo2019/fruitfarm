import os
import sqlite3
from playwright.sync_api import sync_playwright

artifact_dir = r"C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842"
os.makedirs(artifact_dir, exist_ok=True)

db_path = r"E:\fruitfarm\fruitfarm.db"

def set_theme(preset, color):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("UPDATE settings SET value = ? WHERE key = 'theme_preset'", (preset,))
    c.execute("UPDATE settings SET value = ? WHERE key = 'theme_primary_color'", (color,))
    conn.commit()
    conn.close()

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 950})

    # --- 1. PROPOSAL A: Dark Luxury Gold ---
    set_theme('luxury_dark', '#E6A23C')
    page.goto("http://127.0.0.1:5000")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "proposal_A_dark_luxury.png"))
    print("Captured proposal_A_dark_luxury.png")

    # --- 2. PROPOSAL B: Clean Modern White ---
    set_theme('modern_light', '#2563EB')
    page.goto("http://127.0.0.1:5000")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "proposal_B_clean_white.png"))
    print("Captured proposal_B_clean_white.png")

    # --- 3. PROPOSAL C: Tropical Emerald ---
    set_theme('tropical_emerald', '#10B981')
    page.goto("http://127.0.0.1:5000")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "proposal_C_tropical_emerald.png"))
    print("Captured proposal_C_tropical_emerald.png")

    # --- 4. PROPOSAL D: Sunset Amber Terracotta ---
    set_theme('sunset_amber', '#F97316')
    page.goto("http://127.0.0.1:5000")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "proposal_D_sunset_amber.png"))
    print("Captured proposal_D_sunset_amber.png")

    # Reset to Default Flagship: luxury_dark
    set_theme('luxury_dark', '#E6A23C')

    # --- 5. ADMIN LAYOUT & TEXT CMS SCREENS ---
    page.goto("http://127.0.0.1:5000/admin/login")
    page.fill('input[name="username"]', "admin")
    page.fill('input[name="password"]', "password123!")
    page.click('button[type="submit"]')
    page.wait_for_timeout(600)

    page.goto("http://127.0.0.1:5000/admin/design")
    page.wait_for_timeout(600)

    # Tab 2: Layout Reordering
    page.click("#btn-tab-layout")
    page.wait_for_timeout(400)
    page.screenshot(path=os.path.join(artifact_dir, "proposal_admin_layout_reorder.png"))
    print("Captured proposal_admin_layout_reorder.png")

    # Tab 3: Text CMS
    page.click("#btn-tab-texts")
    page.wait_for_timeout(400)
    page.screenshot(path=os.path.join(artifact_dir, "proposal_admin_texts_cms.png"))
    print("Captured proposal_admin_texts_cms.png")

    browser.close()

print("All proposals and CMS screenshots captured successfully!")
