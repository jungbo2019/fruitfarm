with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove the disastrous rule:
disastrous_rule = '.text-white:not(.hero-keep-white):not(.btn-keep-white) { color: #0F172A !important; }'
if disastrous_rule in text:
    text = text.replace(disastrous_rule, '/* removed buggy text-white override */')
    print('Removed buggy text-white override!')
else:
    print('disastrous_rule not found')

# 2. Fix guideActiveBanner to be completely gone or commented out
if 'id="guideActiveBanner"' in text:
    # remove the entire guideActiveBanner div so it can NEVER display on public shopping site
    start = text.find('<!-- Active Guide Partner Mode Banner')
    if start == -1:
        start = text.find('<div id="guideActiveBanner"')
    end = text.find('</div>', text.find('id="guideActiveBanner"'))
    end = text.find('</div>', end + 1)
    end = text.find('</div>', end + 1)
    text = text[:start] + '<!-- Guide B2B Mode isolated to partner route -->' + text[end+6:]
    print('Removed guideActiveBanner from customer base.html!')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(text)
