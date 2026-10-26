import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'E:\fruitfarm\templates\base.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- BASE.HTML BUTTONS / MODALS / DRAWERS ---")
for m in re.finditer(r'<div\s+[^>]*?id=[\'"]([^\'"]*(?:modal|drawer|popup|cart|order)[^\'"]*)[\'"]', html, re.IGNORECASE):
    print("Element ID:", m.group(1))

print("\n--- BASE.HTML JAVASCRIPT FUNCTIONS ---")
for m in re.finditer(r'function\s+([a-zA-Z0-9_]+)\s*\(', html):
    print("JS Function in base.html:", m.group(1))
