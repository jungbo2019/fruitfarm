with open('templates/base.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find("applyGuideModeUI")
while idx != -1:
    print('Called at', idx)
    print(text[idx-100:idx+150].encode('ascii', errors='replace').decode('ascii'))
    idx = text.find('applyGuideModeUI', idx+1)
