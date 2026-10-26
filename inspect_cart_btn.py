with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('nav-cart-badge')
print(text[idx-200:idx+200].encode('ascii', errors='replace').decode('ascii'))
