import urllib.request
import json
import sqlite3

# Test 1: Check DB Settings directly
conn = sqlite3.connect(r"E:\fruitfarm\fruitfarm.db")
c = conn.cursor()
c.execute("SELECT key, value FROM settings WHERE key LIKE 'theme_%' OR key LIKE 'hero_%'")
print("Design settings in DB:")
for r in c.fetchall():
    print(f"  {r[0]}: {r[1]}")
conn.close()

# Test 2: Request index page and check dynamic injection
req = urllib.request.urlopen("http://127.0.0.1:5000")
html = req.read().decode('utf-8')
assert "Phu Quoc Sonasea 12" in html
assert "베트남 최상위 1% 골드망고" in html
print("Index page dynamic design injection test PASSED!")
