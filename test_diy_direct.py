import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})

    page.goto('http://127.0.0.1:5000/')
    page.wait_for_timeout(1000)

    # Directly evaluate selecting 10 regular and 2 bonus
    page.evaluate("""() => {
        // Find first regular item id
        const firstReg = document.querySelector('button[onclick*="updateBuilderRegular"]');
        const onclick = firstReg.getAttribute('onclick');
        const idMatch = onclick.match(/updateBuilderRegular\((\d+)/);
        const id = idMatch ? parseInt(idMatch[1]) : 4;
        builderRegular[id] = 10;

        // Find first bonus item id
        const firstBonus = document.querySelector('button[onclick*="updateBuilderBonus"]');
        const bOnclick = firstBonus.getAttribute('onclick');
        const bIdMatch = bOnclick.match(/updateBuilderBonus\((\d+)/);
        const bId = bIdMatch ? parseInt(bIdMatch[1]) : 4;
        builderBonus[bId] = 2;

        refreshBuilderState();
    }""")

    btn = page.query_selector('#btnCompleteDIY')
    print("Direct state evaluation - DIY button disabled:", btn.is_disabled())
    print("DIY button text:", btn.inner_text())

    # Now click it
    page.on('dialog', lambda d: d.accept())
    btn.click()
    page.wait_for_timeout(500)

    cart_modal = page.query_selector('#cartModal')
    print("Cart modal visible:", cart_modal.is_visible())

    browser.close()
