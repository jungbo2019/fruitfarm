import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), 'fruitfarm.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def upgrade_inventory_schema():
    conn = get_db()
    cursor = conn.cursor()

    # 1. Product Barcode Column in products table
    cursor.execute("PRAGMA table_info(products)")
    columns = [col['name'] for col in cursor.fetchall()]
    if 'barcode' not in columns:
        cursor.execute("ALTER TABLE products ADD COLUMN barcode TEXT")
        print("Added barcode column to products table.")

    # 2. Inventory Lots Table (FEFO: 유통기한 기반 선입선출고 로트 관리)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory_lots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        lot_number TEXT UNIQUE NOT NULL,
        barcode TEXT NOT NULL,
        received_date DATE NOT NULL,
        expiry_date DATE NOT NULL,
        initial_qty INTEGER NOT NULL,
        current_qty INTEGER NOT NULL,
        unit_cost_usd REAL DEFAULT 0.0,
        status TEXT DEFAULT 'active', -- 'active', 'exhausted', 'expired'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    ''')

    # 3. Inventory Transactions Table (입출고 수불 원장)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory_transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lot_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        trans_type TEXT NOT NULL, -- 'IN_STOCK' (입고), 'OUT_ORDER' (택배출고), 'OUT_POS' (현장PC판매), 'DISCARD' (폐기)
        qty INTEGER NOT NULL,
        unit_price_usd REAL DEFAULT 0.0,
        reference_no TEXT, -- Order Number or Barcode Scan ID
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (lot_id) REFERENCES inventory_lots(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    ''')

    # Assign default standardized 880/893 (VN/KR) barcodes to existing 16 products
    barcode_mapping = {
        1: '8936001000010', # 10+2 기획 세트
        2: '8936001000027', # 5+1 기획 세트
        3: '8936001000034', # 청 5+1 세트
        4: '8936001000041', # 골드망고 180g
        5: '8936001000058', # 골드망고 400g
        6: '8936001000065', # 건용안
        7: '8936001000072', # 건용과
        8: '8936001000089', # 건파파야
        9: '8936001000096', # 건패션푸룻
        10: '8936001000102', # 캐슈넛
        11: '8936001000119', # 마카다미아
        12: '8936001000126', # 코코넛칩
        13: '8936001000133', # 히비스커스
        14: '8936001000140', # 편생강
        15: '8936001000157', # 수제 망고청
        16: '8936001000164'  # 수제 패션청
    }

    for pid, bcode in barcode_mapping.items():
        cursor.execute("UPDATE products SET barcode = ? WHERE id = ?", (bcode, pid))

    # Seed baseline inventory lots with realistic expiry dates for FEFO demo
    cursor.execute("SELECT COUNT(*) FROM inventory_lots")
    if cursor.fetchone()[0] == 0:
        today = datetime.now().date()
        # Create 2 lots for Gold Mango (180g) with different expiries to prove FEFO
        cursor.execute('''
        INSERT INTO inventory_lots (product_id, lot_number, barcode, received_date, expiry_date, initial_qty, current_qty, unit_cost_usd)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (4, 'LOT-MG180-2610-A', '8936001000041', today - timedelta(days=20), today + timedelta(days=160), 100, 85, 4.5))

        cursor.execute('''
        INSERT INTO inventory_lots (product_id, lot_number, barcode, received_date, expiry_date, initial_qty, current_qty, unit_cost_usd)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (4, 'LOT-MG180-2610-B', '8936001000041', today - timedelta(days=5), today + timedelta(days=240), 150, 150, 4.5))

        # Mango Syrup lot
        cursor.execute('''
        INSERT INTO inventory_lots (product_id, lot_number, barcode, received_date, expiry_date, initial_qty, current_qty, unit_cost_usd)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (15, 'LOT-SYR-2610-A', '8936001000157', today - timedelta(days=10), today + timedelta(days=90), 80, 72, 8.0))

        # Cashew lot
        cursor.execute('''
        INSERT INTO inventory_lots (product_id, lot_number, barcode, received_date, expiry_date, initial_qty, current_qty, unit_cost_usd)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (10, 'LOT-CSH-2610-A', '8936001000102', today - timedelta(days=15), today + timedelta(days=300), 120, 114, 5.0))

    conn.commit()
    conn.close()
    print("Inventory schema upgraded and baseline lots created!")

if __name__ == '__main__':
    upgrade_inventory_schema()
