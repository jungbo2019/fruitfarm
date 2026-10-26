with open('templates/index.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="products"')
print(text[idx:idx+1500].encode('ascii', errors='replace').decode('ascii'))
