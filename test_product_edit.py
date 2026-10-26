import urllib.request
import urllib.parse
import http.cookiejar

# Create session with cookies
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 1. Login
login_data = urllib.parse.urlencode({'username': 'admin', 'password': 'password123!'}).encode('utf-8')
resp = opener.open('http://127.0.0.1:5000/admin/login', data=login_data)
print("Login status:", resp.getcode())

# 2. Try POST edit to product 1
edit_data = urllib.parse.urlencode({
    'action': 'edit',
    'product_id': '1',
    'price_usd': '100.0',
    'price_krw': '138000',
    'stock': '999',
    'badge': 'BEST PROMO (10+2)'
}).encode('utf-8')

try:
    resp2 = opener.open('http://127.0.0.1:5000/admin/products', data=edit_data)
    print("Edit status:", resp2.getcode())
    print("Final URL:", resp2.geturl())
except urllib.error.HTTPError as e:
    print("HTTPError:", e.code, e.read().decode('utf-8', errors='ignore')[:300])
except Exception as e:
    print("Error:", e)
