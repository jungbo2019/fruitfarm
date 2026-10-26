import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
cur = conn.cursor()
cur.execute("SELECT key, value FROM settings")
rows = cur.fetchall()
for r in rows:
    print(r)
conn.close()
