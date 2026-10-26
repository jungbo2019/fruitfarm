import sqlite3
import os

conn = sqlite3.connect(r"E:\fruitfarm\fruitfarm.db")
c = conn.cursor()
c.execute("UPDATE orders SET guide_code = 'GUIDE_KIM', guide_commission_usd = 25.0, guide_settled = 0 WHERE id = 48")
conn.commit()
conn.close()
print("Updated order 48 successfully")
