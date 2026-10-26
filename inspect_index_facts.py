import re

with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Total HTML length: {len(html)} chars")

# Check for '2호점'
twos = re.findall(r'.{0,30}2호점.{0,30}', html)
print(f"Found '2호점': {len(twos)}")
for t in twos[:5]:
    print(" -", t.strip())

# Check for placeholders like lorem, 010-, test, etc.
placeholders = re.findall(r'.{0,20}(?:lorem|010-0000|test|임시|테스트|홍길동).{0,20}', html, re.IGNORECASE)
print(f"Found placeholders: {len(placeholders)}")
for p in placeholders[:10]:
    print(" -", p.strip())
