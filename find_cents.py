import glob
import re

for p in glob.glob('templates/**/*.html', recursive=True):
    with open(p, encoding='utf-8') as f:
        text = f.read()
    
    matches = re.findall(r'(\$\{\{\s*["\']%.2f["\']\|format\([^)]+\)\s*\}\}|\$[0-9]+\.00)', text)
    if matches:
        print(f"{p}: {len(matches)} matches -> {matches[:3]}")

with open('templates/index.html', encoding='utf-8') as f:
    text = f.read()
if '$100.00' in text:
    print("Found literal $100.00 in index.html")
if '%.2f' in text:
    print("Found %.2f in index.html")
