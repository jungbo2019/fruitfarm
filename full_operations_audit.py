import os
from playwright.sync_api import sync_playwright

artifact_dir = r"C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842"
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 1050})
    page.on("pageerror", lambda err: errors.append(f"PageError: {err}"))
    page.on("console", lambda msg: errors.append(f"ConsoleError: {msg.text}") if msg.type == "error" else None)

    # 1. Check Customer Live GPS Tracking Map
    page.goto("http://127.0.0.1:5000/order/track?query=FPQ-20261025-001")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "audit_live_tracking_map.png"))
    print("1. [AUDIT] Captured audit_live_tracking_map.png")

    # 2. Check 1~10 Operations Cockpit & Financial/Shortage Control
    page.goto("http://127.0.0.1:5000/admin/operations")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "audit_admin_operations.png"))
    print("2. [AUDIT] Captured audit_admin_operations.png")

    # 3. Check Orders 5-Stage Sequential Pipeline
    page.goto("http://127.0.0.1:5000/admin/orders")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "audit_admin_orders_pipeline.png"))
    print("3. [AUDIT] Captured audit_admin_orders_pipeline.png")

    # 4. Check SNS Viral Marketing Center
    page.goto("http://127.0.0.1:5000/admin/marketing")
    page.wait_for_timeout(600)
    page.screenshot(path=os.path.join(artifact_dir, "audit_admin_marketing.png"))
    print("4. [AUDIT] Captured audit_admin_marketing.png")

    browser.close()

if errors:
    print("Browser errors observed:", errors)
else:
    print("-> ZERO BROWSER ERRORS DETECTED! ALL 4 AUDIT CHECKS PASSED!")
