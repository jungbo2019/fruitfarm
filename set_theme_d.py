import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
cur = conn.cursor()
cur.execute("SELECT key FROM settings")
keys = [r[0] for r in cur.fetchall()]
print("Keys in settings:", keys)

# insert or replace active_proposal
conn.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('active_proposal', 'proposal_D')")
conn.commit()

cur.execute("SELECT value FROM settings WHERE key='active_proposal'")
print("active_proposal set to:", cur.fetchone()[0])
conn.close()
