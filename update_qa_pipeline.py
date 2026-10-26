with open(r'E:\fruitfarm\gemini_qa_pipeline.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    # Check 2: Discord Community Link in Footer
    discord_footer_link = page.query_selector('footer a[href*="discord.gg/Kym2WKGDX"]')
    if discord_footer_link:
        print("  -> [PASS] Footer contains active Discord link (https://discord.gg/Kym2WKGDX).")
    else:
        print("  [FAIL] Discord footer link missing or broken.")"""

replacement = """    # Check 2: Verify Retail Footer is Clean (Zero Internal Discord Link)
    discord_footer_link = page.query_selector('footer a[href*="discord"]')
    if not discord_footer_link:
        print("  -> [PASS] Retail footer is 100% clean. Internal Discord link eliminated from customer view.")
    else:
        print("  [FAIL] Discord link still visible in retail footer!")"""

if target in text:
    text = text.replace(target, replacement)
    with open(r'E:\fruitfarm\gemini_qa_pipeline.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated gemini_qa_pipeline.py successfully.")
else:
    print("Target not found in gemini_qa_pipeline.py")
