import re

with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find all sections and comments
matches = re.findall(r'(?:<!--\s*([0-9\.\s\w\(\)-]+)\s*-->|<section\s+[^>]*?id=["\']([^"\']+)["\'])', text)
for m in matches:
    print(m)
