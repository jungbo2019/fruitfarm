with open('templates/base.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('guideActiveBanner')
while idx != -1:
    print('Found at', idx)
    print(text[idx:idx+200].encode('ascii', errors='replace').decode('ascii'))
    idx = text.find('guideActiveBanner', idx+1)
