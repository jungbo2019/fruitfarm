import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()
c.execute("SELECT key, value FROM settings WHERE key LIKE '%competitor%' OR key LIKE '%title%' OR key LIKE '%hero%'")
for row in c.fetchall():
    print(f"{row[0]}: {row[1]}")
conn.close()
