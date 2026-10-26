import sqlite3
import re
from collections import Counter

print("=== CHECK 1: DB PRODUCTS ===")
conn = sqlite3.connect('E:/fruitfarm/fruitfarm.db')
c = conn.cursor()
products = c.execute("SELECT id, name, category, price_usd, image_url, barcode FROM products").fetchall()
names = [p[1] for p in products]
barcodes = [p[5] for p in products]
images = [p[4] for p in products]

print("Total products:", len(products))
print("Duplicate names:", [k for k, v in Counter(names).items() if v > 1])
print("Duplicate barcodes:", [k for k, v in Counter(barcodes).items() if v > 1])
print("Duplicate images:", [k for k, v in Counter(images).items() if v > 1])

print("\n=== CHECK 2: DB ORDERS ===")
orders = c.execute("SELECT id, order_number, customer_name FROM orders").fetchall()
print("Total orders:", len(orders))
print("Duplicate order numbers:", [k for k, v in Counter([o[1] for o in orders]).items() if v > 1])

print("\n=== CHECK 3: DB GUIDES ===")
guides = c.execute("SELECT id, guide_code, name FROM guides").fetchall()
print("Total guides:", len(guides))
print("Duplicate guide codes:", [k for k, v in Counter([g[1] for g in guides]).items() if v > 1])

print("\n=== CHECK 4: INDEX.HTML DUPLICATES ===")
with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Check section IDs
section_ids = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', idx_content)
print("Section IDs:", section_ids)
print("Duplicate Section IDs:", [k for k, v in Counter(section_ids).items() if v > 1])

# Check duplicate headers or text blocks
h2_texts = [re.sub('<[^<]+?>', '', h).strip() for h in re.findall(r'<h2[^>]*>(.*?)</h2>', idx_content, re.DOTALL)]
print("Duplicate H2:", [k for k, v in Counter(h2_texts).items() if v > 1])

# Check duplicate buttons / ids
all_ids = re.findall(r'id=["\']([^"\']+)["\']', idx_content)
print("Duplicate DOM IDs in index.html:", [k for k, v in Counter(all_ids).items() if v > 1])

print("\n=== CHECK 5: ADMIN NAVIGATION & PAGES DUPLICATES ===")
with open('E:/fruitfarm/templates/admin/base_admin.html', 'r', encoding='utf-8') as f:
    admin_nav = f.read()

nav_links = re.findall(r'href=["\']([^"\']+)["\']', admin_nav)
print("Admin nav links:", [l for l in nav_links if '/admin' in l])
print("Duplicate admin nav links:", [k for k, v in Counter([l for l in nav_links if '/admin' in l]).items() if v > 1])
