import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
conn.execute("UPDATE settings SET value='sunset_amber' WHERE key='theme_preset'")
conn.execute("UPDATE settings SET value='#F97316' WHERE key='theme_primary_color'")
conn.execute("UPDATE settings SET value='proposal_D' WHERE key='active_proposal'")
conn.commit()

cur = conn.cursor()
cur.execute("SELECT key, value FROM settings WHERE key IN ('theme_preset', 'theme_primary_color', 'active_proposal')")
print(cur.fetchall())
conn.close()
