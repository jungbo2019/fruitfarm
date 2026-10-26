with open('templates/index.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="products"')
print(text[idx+2400:idx+3500].encode('ascii', errors='replace').decode('ascii'))
