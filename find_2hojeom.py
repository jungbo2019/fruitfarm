import sqlite3
import glob

conn = sqlite3.connect('fruitfarm.db')
c = conn.cursor()
c.execute("SELECT key, value FROM settings WHERE value LIKE '%2호점%'")
db_rows = c.fetchall()
print("DB settings with 2호점:")
for k, v in db_rows:
    print(f"  {k}: {v.encode('ascii', errors='replace').decode('ascii')}")

print("\nFiles with 2호점:")
for p in glob.glob('templates/**/*.html', recursive=True) + ['app.py']:
    with open(p, encoding='utf-8') as f:
        text = f.read()
    count = text.count('2호점')
    if count > 0:
        print(f"  {p}: {count} occurrences")
