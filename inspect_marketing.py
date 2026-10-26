with open('templates/admin/marketing.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('grid')
print(text[idx:idx+1200].encode('ascii', errors='replace').decode('ascii'))
