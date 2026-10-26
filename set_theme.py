import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
conn.execute("UPDATE settings SET value='proposal_D' WHERE key='active_proposal'")
conn.commit()
cur = conn.cursor()
cur.execute("SELECT value FROM settings WHERE key='active_proposal'")
print("Active Theme is now:", cur.fetchone()[0])
conn.close()
