with open('templates/index.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('FLAGSHIP STORE')
print(text[idx-50:idx+1500].encode('ascii', errors='replace').decode('ascii'))
