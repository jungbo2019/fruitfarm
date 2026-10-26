with open('templates/index.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('COMPETITOR BENCHMARK')
if idx == -1:
    idx = text.find('competitor')
print(text[idx-50:idx+2000].encode('ascii', errors='replace').decode('ascii'))
