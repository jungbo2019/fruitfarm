import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()

# Set theme_preset to fresh_cream_mango
c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('theme_preset', 'fresh_cream_mango')")
c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('theme_primary_color', '#F59E0B')")
c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('active_proposal', 'proposal_cream_mango')")

conn.commit()

c.execute("SELECT key, value FROM settings WHERE key IN ('theme_preset', 'theme_primary_color', 'active_proposal')")
print("Updated settings:", c.fetchall())
conn.close()
