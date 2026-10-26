import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
cursor = conn.cursor()

cursor.execute("SELECT id, name, category, price_usd, price_krw, stock, badge, image_url, description FROM products")
products = cursor.fetchall()
print(f"Total products in DB: {len(products)}")
for p in products:
    print(f"ID {p[0]}: [{p[2]}] {p[1]} | ${p[3]} (₩{p[4]:,}) | 재고: {p[5]} | 뱃지: {p[6]} | 이미지: {p[7]}")
    print(f"   설명: {p[8][:80]}...")

print("\n--- SETTINGS ---")
cursor.execute("SELECT key, value FROM settings")
for k, v in cursor.fetchall():
    print(f"{k}: {v}")

conn.close()
