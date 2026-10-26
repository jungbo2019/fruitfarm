with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('매장 연락처: +84 386 074 755', '실시간 상담: 카카오톡 채널 @fruitfarm')
text = text.replace('PHU QUOC BRANCH 2', 'PHU QUOC FLAGSHIP STORE')
text = text.replace('푸꾸옥 2호점', '푸꾸옥 플래그십')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Cleaned footer phone and branch 2 text!')
