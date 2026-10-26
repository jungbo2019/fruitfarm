import os
import sqlite3

def check_images():
    conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, image_url FROM products")
    missing_prods = []
    for pid, name, img in cursor.fetchall():
        if img.startswith('/static/'):
            local_path = os.path.join(r'E:\fruitfarm', img.lstrip('/'))
            if not os.path.exists(local_path):
                missing_prods.append((pid, name, img))
    print(f"Missing product images: {len(missing_prods)}")
    for m in missing_prods:
        print(" - Missing:", m)
        
    cursor.execute("SELECT key, value FROM settings WHERE key LIKE '%image%'")
    missing_settings = []
    for k, v in cursor.fetchall():
        if v.startswith('/static/'):
            local_path = os.path.join(r'E:\fruitfarm', v.lstrip('/'))
            if not os.path.exists(local_path):
                missing_settings.append((k, v))
    print(f"Missing settings images: {len(missing_settings)}")
    for m in missing_settings:
        print(" - Missing:", m)
    conn.close()

if __name__ == '__main__':
    check_images()
