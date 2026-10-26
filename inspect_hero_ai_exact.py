with open('templates/index.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('AI 24시 즉시상담')
print(text[idx-300:idx+400].encode('ascii', errors='replace').decode('ascii'))
