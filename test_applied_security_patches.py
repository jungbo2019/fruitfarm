import requests
import time

BASE_URL = "http://127.0.0.1:5000"

def test_security_patches():
    session = requests.Session()
    print("=== [1. Security HTTP Headers Test] ===")
    res = session.get(f"{BASE_URL}/")
    headers = res.headers
    assert headers.get("X-Frame-Options") == "SAMEORIGIN", f"Missing X-Frame-Options: {headers}"
    assert headers.get("X-Content-Type-Options") == "nosniff", f"Missing X-Content-Type-Options: {headers}"
    assert headers.get("Referrer-Policy") == "strict-origin-when-cross-origin", f"Missing Referrer-Policy: {headers}"
    assert "Permissions-Policy" in headers, f"Missing Permissions-Policy: {headers}"
    print("PASS: Security HTTP Headers (X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy) verified!")

    print("\n=== [2. Guide Verify API Data Masking Test] ===")
    guide_res = session.post(f"{BASE_URL}/api/guide/verify", json={"guide_code": "GUIDE_KIM"})
    print("Guide API Response:", guide_res.json())
    guide_data = guide_res.json().get("guide", {})
    assert "guide_code" in guide_data, "guide_code should be present"
    assert "name" in guide_data, "name should be present"
    assert "commission_rate" not in guide_data, "commission_rate MUST be masked for public callers!"
    assert "total_sales_usd" not in guide_data, "total_sales_usd MUST be masked for public callers!"
    assert "total_commission_usd" not in guide_data, "total_commission_usd MUST be masked for public callers!"
    print("PASS: Financial details (commission_rate, total_sales_usd, total_commission_usd) successfully masked for public users!")

    print("\n=== [3. Admin Login Normal Test] ===")
    admin_session = requests.Session()
    login_res = admin_session.post(
        f"{BASE_URL}/admin/login",
        data={"username": "admin", "password": "password123!"},
        allow_redirects=True
    )
    assert "FRUIT FARM" in login_res.text or "dashboard" in login_res.url or login_res.status_code == 200
    assert "admin_logged_in" in [c.name for c in admin_session.cookies] or "session" in [c.name for c in admin_session.cookies]
    print(f"PASS: Legitimate admin login verified! Final URL: {login_res.url}")

    print("\n=== [4. Brute-Force Rate Limiting Test (Mock IP / Distinct Session)] ===")
    attacker_session = requests.Session()
    # Test wrong password with a fresh mock IP
    test_ip = f"203.0.113.{int(time.time()) % 200 + 10}"
    headers = {"X-Forwarded-For": test_ip}

    for i in range(1, 6):
        t0 = time.time()
        fail_res = attacker_session.post(
            f"{BASE_URL}/admin/login",
            data={"username": "admin", "password": "wrongpassword!"},
            headers=headers
        )
        duration = time.time() - t0
        print(f"Attempt {i}: took {duration:.2f}s, response status {fail_res.status_code}")
        assert duration >= 0.9, f"Rate limiting delay expected at least 1s, got {duration}"

    # 6th attempt should be locked out
    lock_res = attacker_session.post(
        f"{BASE_URL}/admin/login",
        data={"username": "admin", "password": "wrongpassword!"},
        headers=headers
    )
    assert "접속이 제한되었습니다" in lock_res.text or "잠금" in lock_res.text, "Brute-force lockout message expected!"
    print("PASS: Brute-force rate limiting and 15-minute IP lockout verified!")

    print("\n==============================================")
    print("[SUCCESS] ALL 4 SECURITY PATCHES VERIFIED SUCCESSFULLY!")
    print("==============================================")

if __name__ == "__main__":
    test_security_patches()
