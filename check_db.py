import sqlite3
conn = sqlite3.connect('fruitfarm.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", c.fetchall())

try:
    c.execute("SELECT * FROM settings")
    print("Settings:", c.fetchall())
except Exception as e:
    print("Error:", e)
