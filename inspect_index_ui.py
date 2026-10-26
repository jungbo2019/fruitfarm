import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- BUTTONS WITH ONCLICK OR ID ---")
for m in re.finditer(r'<button\s+([^>]*?)>(.*?)</button>', html, re.DOTALL):
    attrs = m.group(1)
    content = re.sub(r'<[^>]+>', '', m.group(2)).strip()[:30]
    if 'onclick' in attrs or 'id=' in attrs:
        print(f"Button: text='{content}' | attrs={attrs.strip()[:80]}")

print("\n--- FORMS ---")
for m in re.finditer(r'<form\s+([^>]*?)>', html):
    print("Form:", m.group(1))

print("\n--- MODALS / DRAWERS ---")
for m in re.finditer(r'<div\s+[^>]*?id=[\'"]([^\'"]*(?:modal|drawer|popup)[^\'"]*)[\'"]', html, re.IGNORECASE):
    print("Modal/Drawer ID:", m.group(1))

print("\n--- JAVASCRIPT FUNCTIONS DEFINED ---")
for m in re.finditer(r'function\s+([a-zA-Z0-9_]+)\s*\(', html):
    print("JS Function:", m.group(1))
