import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in c.fetchall()]
print("Tables:", tables)

for t in tables:
    c.execute(f"PRAGMA table_info({t})")
    cols = [r[1] for r in c.fetchall()]
    print(f"Table '{t}': {cols}")

conn.close()
