import sqlite3
import os

DB_PATH = os.path.join(r"E:\fruitfarm", "fruitfarm.db")
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("UPDATE settings SET value = 'SV2A - V07 Khu Sonasea Bãi Trường, Phú Quốc (소나시 12가)' WHERE key = 'store_address'")
c.execute("UPDATE settings SET value = '+84 386 074 755' WHERE key = 'store_phone'")
c.execute("UPDATE settings SET value = 'FRUIT FARM 푸꾸옥 2호점 (VƯỜN HOA QUẢ)' WHERE key = 'store_branch_name'")
c.execute("UPDATE settings SET value = '매일 09:00 ~ 22:00 (연중무휴 / 전 품목 무료 시식 상시 운영)' WHERE key = 'business_hours'")

conn.commit()
conn.close()
print("Settings successfully updated with real store photos & information!")
