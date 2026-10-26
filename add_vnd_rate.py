import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()
c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('usd_vnd_rate', '25400')")
conn.commit()

c.execute("SELECT key, value FROM settings WHERE key LIKE '%rate%'")
for r in c.fetchall():
    print(r)
conn.close()
