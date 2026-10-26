import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'fruitfarm.db')

def upgrade_guides_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Guides Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS guides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guide_code TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        agency TEXT NOT NULL,
        phone TEXT NOT NULL,
        kakao_id TEXT,
        commission_rate REAL DEFAULT 0.25,
        total_orders INTEGER DEFAULT 0,
        total_sales_usd REAL DEFAULT 0.0,
        total_commission_usd REAL DEFAULT 0.0,
        settled_commission_usd REAL DEFAULT 0.0,
        status TEXT DEFAULT 'active',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 2. Add guide columns to orders table if not exist
    cursor.execute("PRAGMA table_info(orders)")
    cols = [col[1] for col in cursor.fetchall()]
    if 'guide_code' not in cols:
        cursor.execute("ALTER TABLE orders ADD COLUMN guide_code TEXT")
        print("Added guide_code to orders")
    if 'guide_commission_usd' not in cols:
        cursor.execute("ALTER TABLE orders ADD COLUMN guide_commission_usd REAL DEFAULT 0.0")
        print("Added guide_commission_usd to orders")
    if 'guide_settled' not in cols:
        cursor.execute("ALTER TABLE orders ADD COLUMN guide_settled INTEGER DEFAULT 0")
        print("Added guide_settled to orders")

    # 3. Seed initial 3 verified guide partners if table is empty
    cursor.execute("SELECT COUNT(*) FROM guides")
    if cursor.fetchone()[0] == 0:
        guides_data = [
            ('GUIDE_KIM', '김철수 팀장', '하나투어 푸꾸옥 전담팀', '010-3344-5566', 'guide_kim_pqc', 0.25, 1, 100.0, 25.0, 0.0),
            ('GUIDE_LEE', '이영희 실장', '모두투어 동남아팀', '010-7788-9900', 'guide_lee_pqc', 0.25, 0, 0.0, 0.0, 0.0),
            ('GUIDE_PARK', '박민수 가이드', '푸꾸옥 자유여행 프리랜서', '010-1122-3344', 'guide_park_pqc', 0.25, 0, 0.0, 0.0, 0.0)
        ]
        cursor.executemany('''
        INSERT INTO guides (
            guide_code, name, agency, phone, kakao_id, commission_rate,
            total_orders, total_sales_usd, total_commission_usd, settled_commission_usd
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', guides_data)
        print("Seeded baseline guides")

    # Update existing baseline order with GUIDE_KIM
    cursor.execute("UPDATE orders SET guide_code = 'GUIDE_KIM', guide_commission_usd = 25.0 WHERE id = 1 AND (guide_code IS NULL OR guide_code = '')")

    conn.commit()
    conn.close()
    print("Guide schema upgrade completed successfully.")

if __name__ == '__main__':
    upgrade_guides_schema()
