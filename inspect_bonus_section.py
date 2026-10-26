import re

with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="bonusSection"')
if idx != -1:
    print(text[idx-200:idx+800])
else:
    print("bonusSection not found!")
