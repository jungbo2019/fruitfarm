with open('templates/base.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find("document.getElementById('guideActiveBanner').classList.remove('hidden');")
print(text[idx-300:idx+300].encode('ascii', errors='replace').decode('ascii'))
