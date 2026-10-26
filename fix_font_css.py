with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
replacement = '<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />'

text = text.replace(target, replacement)

with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Pretendard CSS fixed!")
