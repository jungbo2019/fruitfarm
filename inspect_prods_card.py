with open('templates/index.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="products"')
print(text[idx+1100:idx+2500].encode('ascii', errors='replace').decode('ascii'))
