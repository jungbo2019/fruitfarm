import sqlite3
conn = sqlite3.connect('fruitfarm.db')
c = conn.cursor()
c.execute("SELECT key, value FROM settings WHERE key LIKE '%theme%'")
for row in c.fetchall():
    print(row)
