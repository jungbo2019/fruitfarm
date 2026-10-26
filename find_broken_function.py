import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with open(r'E:\fruitfarm\broken_script_2.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()

    # Find the earliest line that causes the syntax error
    for count in range(1, len(lines) + 1):
        test_code = "".join(lines[:count])
        # try parsing by adding dummy closing braces or checking
        # Better: let's test each function individually or check line by line
        pass

    # Let's inspect functions by splitting on 'function '
    funcs = "".join(lines).split('function ')
    print(f"Total function definitions: {len(funcs)}")
    for i, func in enumerate(funcs[1:], 1):
        func_name = func.split('(')[0].strip()
        code_to_eval = "function " + func
        try:
            page.evaluate(f"(function() {{ {code_to_eval} }})")
        except Exception as e:
            print(f"ERROR in function: '{func_name}'")
            print(str(e)[:150])
            print("--- FUNCTION SNIPPET ---")
            print(code_to_eval[:300])

    browser.close()
