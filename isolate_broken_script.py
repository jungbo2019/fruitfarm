import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()

    scripts = []
    # Evaluate script tags
    page.goto('http://127.0.0.1:5000/')
    content = page.content()
    
    with open(r'E:\fruitfarm\rendered_index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Rendered HTML saved to rendered_index.html")

    # Let's inspect script elements
    script_texts = page.eval_on_selector_all('script:not([src])', 'elements => elements.map(e => e.innerHTML)')
    for idx, s in enumerate(script_texts):
        print(f"--- SCRIPT TAG #{idx} (length {len(s)}) ---")
        lines = s.split('\n')
        print(f"Total lines: {len(lines)}")
        # let's try running eval on each script in the page context to see which one throws!
        try:
            page.evaluate(f"(function() {{ {s} }})")
            print(" -> Syntax VALID!")
        except Exception as e:
            print(" -> SYNTAX ERROR IN THIS SCRIPT TAG:")
            print(str(e)[:300])
            with open(f'E:\\fruitfarm\\broken_script_{idx}.js', 'w', encoding='utf-8') as bf:
                bf.write(s)

    browser.close()
