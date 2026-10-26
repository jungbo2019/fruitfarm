import requests

s = requests.Session()
BASE = 'http://127.0.0.1:5000'

s.post(f'{BASE}/admin/login', data={'username': 'admin', 'password': 'password123!'})

# 1. Barcode Scan FEFO
r = s.post(f'{BASE}/api/admin/inventory/scan-action', json={'barcode': '8936001000041', 'mode': 'OUT_POS'})
assert r.status_code == 200
data = r.json()
assert data['success'] == True
assert data['lot']['lot_number'] == 'LOT-MG180-2610-A'
print("FEFO 출고 성공! 출고 로트:", data['lot']['lot_number'], "유통기한:", data['lot']['expiry_date'])

# 2. Check Lots
r = s.post(f'{BASE}/api/admin/inventory/scan-action', json={'barcode': '8936001000041', 'mode': 'CHECK'})
assert r.status_code == 200
d_check = r.json()
assert d_check['success'] == True
print("재고 실사 성공! 로트 수:", len(d_check['lots']))

# 3. Reports
r = s.get(f'{BASE}/admin/inventory/reports')
assert r.status_code == 200
print("일/월/년 수불부 리포트 Status 200 OK")

# 4. Scan page
r = s.get(f'{BASE}/admin/inventory/scan')
assert r.status_code == 200
print("바코드 스캔 터미널 Status 200 OK")

print("All inventory barcode tests passed!")
