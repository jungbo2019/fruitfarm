from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge')
    page = browser.new_page(viewport={'width': 1280, 'height': 800})

    # 1. Main Page with clean header & AI concierge in Hero card
    page.goto('http://127.0.0.1:5000/')
    time.sleep(1)
    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_clean_customer_hero.png')

    # 2. Click the AI Concierge button to open chatbot
    page.click('button:has-text("AI 24시 즉시상담")')
    time.sleep(0.5)

    # Click first FAQ chip: "한국 배송 소요기간"
    page.click('button:has-text("한국 배송 소요기간")')
    time.sleep(1.2) # wait for bot to respond

    page.screenshot(path='C:/Users/user/.gemini/antigravity/brain/49c79cbc-1a5d-43a3-9fb0-17db051e3842/screen_ai_chatbot_active.png')

    browser.close()
    print("AI Concierge screenshots captured successfully!")
