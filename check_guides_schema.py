import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()

# Check if guides table has sample_kit_issued column
c.execute("PRAGMA table_info(guides)")
cols = [r[1] for r in c.fetchall()]
print("Guides cols:", cols)

if 'sample_kit_issued' not in cols:
    c.execute("ALTER TABLE guides ADD COLUMN sample_kit_issued INTEGER DEFAULT 0")
    print("Added sample_kit_issued column to guides.")

if 'settlement_note' not in cols:
    c.execute("ALTER TABLE guides ADD COLUMN settlement_note TEXT DEFAULT ''")
    print("Added settlement_note column to guides.")

conn.commit()
conn.close()
