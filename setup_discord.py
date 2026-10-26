import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()

# Check settings table
c.execute("SELECT key, value FROM settings")
existing = dict(c.fetchall())
print("Existing settings keys:", list(existing.keys()))

# Insert or update discord_invite_url
invite_url = "https://discord.gg/Kym2WKGDX"
c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('discord_invite_url', ?)", (invite_url,))
if 'discord_webhook_url' not in existing:
    c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('discord_webhook_url', '')", ())

conn.commit()
print("Updated discord settings.")
c.execute("SELECT key, value FROM settings WHERE key LIKE '%discord%'")
print(c.fetchall())
conn.close()
