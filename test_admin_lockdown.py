import urllib.request
import urllib.error
import http.cookiejar

# Create an opener that doesn't follow redirects to check 302 status, or follows them to check landing page
class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirectHandler)

admin_urls = [
    '/admin',
    '/admin/dashboard',
    '/admin/orders',
    '/admin/products',
    '/admin/guides',
    '/admin/marketing',
    '/admin/operations',
    '/admin/crm',
    '/admin/sales',
    '/admin/settings',
    '/admin/control-center',
    '/admin/inventory/scan'
]

print("=== TESTING STRICT UNLOGGED ACCESS BLOCK ===")
all_blocked = True
for path in admin_urls:
    url = f"http://127.0.0.1:5000{path}"
    req = urllib.request.Request(url)
    try:
        resp = opener.open(req)
        print(f"FAIL: {path} returned status {resp.getcode()} instead of redirect!")
        all_blocked = False
    except urllib.error.HTTPError as e:
        if e.code == 302:
            redirect_loc = e.headers.get('Location', '')
            if '/admin/login' in redirect_loc:
                print(f"[PASS - BLOCKED] {path} -> 302 Redirect to {redirect_loc}")
            else:
                print(f"FAIL: {path} redirected to unexpected {redirect_loc}")
                all_blocked = False
        else:
            print(f"HTTP code {e.code} for {path}")
    except Exception as e:
        print(f"Error {path}: {e}")

print("===========================================")
if all_blocked:
    print("ALL ADMIN PAGES ARE 100% STRICTLY BLOCKED FOR UNLOGGED USERS!")
else:
    print("SOME ADMIN PAGES ARE NOT BLOCKED!")
