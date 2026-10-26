with open(r'E:\fruitfarm\templates\base.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=Pretendard[^"]+" rel="stylesheet">',
              '<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />',
              text)

with open(r'E:\fruitfarm\templates\base.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Pretendard link fixed in base.html!")
