with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("settings.get('store_phone'")
if idx != -1:
    line_start = text.rfind('<li>', 0, idx)
    line_end = text.find('</li>', idx)
    text = text[:line_start] + '<li>• 실시간 상담: 카카오톡 채널 @fruitfarm</li>' + text[line_end+5:]
    print("Replaced store_phone in footer with Kakao channel!")

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(text)
