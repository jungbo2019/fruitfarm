import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()

cols_to_add = [
    ("rider_name", "TEXT DEFAULT '응우옌 라이더 (Nguyen Grab)'"),
    ("rider_phone", "TEXT DEFAULT '+84 90 123 4567'"),
    ("rider_plate", "TEXT DEFAULT '68-P1 888.88'"),
    ("eta_minutes", "INTEGER DEFAULT 14"),
    ("cogs_usd", "REAL DEFAULT 45.0"),
    ("expense_delivery_usd", "REAL DEFAULT 3.0"),
    ("expense_packaging_usd", "REAL DEFAULT 1.5")
]

c.execute("PRAGMA table_info(orders)")
existing_cols = [row[1] for row in c.fetchall()]

for col_name, col_def in cols_to_add:
    if col_name not in existing_cols:
        c.execute(f"ALTER TABLE orders ADD COLUMN {col_name} {col_def}")
        print(f"Added column {col_name} to orders table.")

conn.commit()
conn.close()
print("Database schema upgraded successfully!")
