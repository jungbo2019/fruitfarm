with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'def (admin_orders[^\(]*)\(', text)
print("Orders functions:", matches)

# Find admin order status update route
lines = text.splitlines()
for i, l in enumerate(lines):
    if '/admin/order' in l or 'order_status' in l:
        print(f"Line {i}: {l.strip()[:70]}")
