import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()
webhook_url = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

c.execute("INSERT OR REPLACE INTO settings (key, value) VALUES ('discord_webhook_url', ?)", (webhook_url,))
conn.commit()
conn.close()
print("Saved webhook URL to fruitfarm.db settings table.")
