import sqlite3
import glob

# 1. Update database settings
conn = sqlite3.connect('fruitfarm.db')
c = conn.cursor()

updates = {
    'store_branch_name': 'FRUIT FARM 푸꾸옥 직영 플래그십 (소나시)',
    'text_gallery_title': '푸꾸옥 플래그십 실제 쇼룸 & 무료 시식 현장',
    'text_catalog_title': 'FRUIT FARM 푸꾸옥 직영 플래그십 전 상품',
    'text_location_title': 'FRUIT FARM 푸꾸옥 플래그십 스토어',
    'meta_title': 'FRUIT FARM 푸꾸옥 플래그십 | 프리미엄 무설탕 골드망고'
}

for k, v in updates.items():
    c.execute("UPDATE settings SET value = ? WHERE key = ?", (v, k))
conn.commit()
print("Updated database settings!")

# 2. Update templates and app.py
targets = glob.glob('templates/**/*.html', recursive=True) + ['app.py']

for p in targets:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '2호점' in content:
        new_content = content.replace('푸꾸옥 2호점', '푸꾸옥 플래그십')
        new_content = new_content.replace('2호점', '푸꾸옥 플래그십')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {p}")

print("Replaced all '2호점' across templates and database!")
