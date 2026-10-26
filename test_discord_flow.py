import urllib.request
import json
import sqlite3

# 1. Place test order via API
order_data = {
    "customer_name": "디스코드 연동 테스트",
    "customer_phone": "010-9999-8888",
    "customer_kakao": "test_discord",
    "delivery_type": "local_phuquoc",
    "delivery_address": "베트남 푸꾸옥 노보텔 풀빌라 201호",
    "delivery_note": "로비 도착 시 디스코드/카톡 연락 부탁드립니다.",
    "items": [
        {"id": 1, "qty": 2}
    ]
}

req = urllib.request.Request(
    'http://127.0.0.1:5000/api/order/create',
    data=json.dumps(order_data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("Order creation response:", res)
except Exception as e:
    print("Order creation error:", e)

# 2. Check system logs for DISCORD and ORDER events
conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()
c.execute("SELECT id, event_type, message, created_at FROM system_logs ORDER BY id DESC LIMIT 5")
for row in c.fetchall():
    print("Log row:", row)
conn.close()
