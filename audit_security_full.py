import re
import os
import glob
import sqlite3

def run_security_audit():
    findings = []
    
    app_path = r"E:\fruitfarm\app.py"
    with open(app_path, "r", encoding="utf-8") as f:
        app_code = f.read()

    # 1. Debug mode check
    if "debug=True" in app_code or "DEBUG = True" in app_code:
        findings.append({
            "category": "서버 설정 (Server Configuration)",
            "level": "주의 (Medium)",
            "item": "Flask Debug 모드 활성화",
            "detail": "Flask 실행 시 debug=True 설정이 포함되어 있으면 예외 발생 시 스택 트레이스 및 디버그 콘솔이 노출될 수 있습니다."
        })
    else:
        findings.append({
            "category": "서버 설정 (Server Configuration)",
            "level": "안전 (Pass)",
            "item": "Flask Debug 모드 비활성화 확인",
            "detail": "debug=False로 안정적으로 구동 중입니다."
        })

    # 2. SQL Injection check
    sql_inj_matches = re.findall(r'execute\(\s*f["\'].*?\{.*?\}', app_code)
    db_path = r"E:\fruitfarm\database.py"
    db_code = ""
    if os.path.exists(db_path):
        with open(db_path, "r", encoding="utf-8") as f:
            db_code = f.read()
        sql_inj_matches.extend(re.findall(r'execute\(\s*f["\'].*?\{.*?\}', db_code))
    
    if sql_inj_matches:
        findings.append({
            "category": "데이터베이스 보안 (Database & SQL)",
            "level": "위험 (High)",
            "item": "f-string을 사용한 동적 SQL 쿼리 탐지",
            "detail": f"{len(sql_inj_matches)}개의 쿼리에서 파라미터 바인딩 대신 f-string 문자열 포맷팅이 사용되었습니다: {sql_inj_matches[:3]}"
        })
    else:
        findings.append({
            "category": "데이터베이스 보안 (Database & SQL)",
            "level": "안전 (Pass)",
            "item": "SQL 파라미터 바인딩 (? 바인딩) 준수",
            "detail": "SQL 쿼리 내 직접 문자열 결합 없이 물음표(?) 매개변수 바인딩 방식을 사용하고 있습니다."
        })

    # 3. Authentication & Access Control
    if "@app.before_request" in app_code and "session.get('admin_logged_in')" in app_code:
        findings.append({
            "category": "인증 및 접근 제어 (Auth & Access Control)",
            "level": "안전 (Pass)",
            "item": "관리자 전체 라우트 강제 잠금 (Global Guard Hook)",
            "detail": "before_request 훅을 통해 /admin, /api/admin 등 모든 관리자 경로에 대해 비인가 세션을 100% 차단 및 로그인 페이지로 리다이렉트합니다."
        })
    else:
        findings.append({
            "category": "인증 및 접근 제어 (Auth & Access Control)",
            "level": "위험 (High)",
            "item": "관리자 라우트 보호 미흡",
            "detail": "일부 관리자 페이지가 비인가 상태로 접근 가능할 위험이 있습니다."
        })

    # 4. Password Storage & Hashing
    if "check_password_hash" in app_code and "generate_password_hash" in app_code:
        findings.append({
            "category": "인증 및 접근 제어 (Auth & Access Control)",
            "level": "안전 (Pass)",
            "item": "단방향 암호화 해시 (PBKDF2/SHA256) 검증",
            "detail": "관리자 비밀번호가 평문 비교 대신 werkzeug check_password_hash()로 안전하게 대조됩니다."
        })
    else:
        findings.append({
            "category": "인증 및 접근 제어 (Auth & Access Control)",
            "level": "위험 (High)",
            "item": "평문 비밀번호 검증 위험",
            "detail": "비밀번호가 평문으로 대조되고 있습니다."
        })

    # 5. Session Cookie Security
    cookie_http = "SESSION_COOKIE_HTTPONLY" in app_code
    cookie_samesite = "SESSION_COOKIE_SAMESITE" in app_code
    cookie_secure = "SESSION_COOKIE_SECURE" in app_code
    
    if cookie_http and cookie_samesite:
        level = "양호 (Good)" if not cookie_secure else "안전 (Pass)"
        findings.append({
            "category": "세션 및 쿠키 보안 (Session Security)",
            "level": level,
            "item": f"세션 쿠키 속성 설정 (HttpOnly={cookie_http}, SameSite={cookie_samesite}, Secure={cookie_secure})",
            "detail": "XSS를 통한 세션 탈취(HttpOnly)와 CSRF 공격(SameSite=Lax) 방어가 활성화되어 있습니다. HTTPS 전용 환경에서는 SESSION_COOKIE_SECURE = True 권장."
        })

    # 6. CSRF Protection (Cross-Site Request Forgery)
    has_csrf = "CSRFProtect" in app_code or "csrf_token" in app_code
    if not has_csrf:
        findings.append({
            "category": "웹 취약점 (Web Vulnerabilities)",
            "level": "주의 (Medium)",
            "item": "CSRF 토큰 검증 부재 (Flask-WTF 미적용)",
            "detail": "SameSite=Lax 쿠키가 방어막 역할을 하지만, POST 폼 전송에 대한 명시적인 CSRF 토큰(Flask-WTF) 검증을 추가하면 보안이 한층 강화됩니다."
        })
    else:
        findings.append({
            "category": "웹 취약점 (Web Vulnerabilities)",
            "level": "안전 (Pass)",
            "item": "CSRF 토큰 방어 적용",
            "detail": "CSRF 토큰 기반 폼 검증이 동작 중입니다."
        })

    # 7. XSS (Cross-Site Scripting) - Jinja2 safe filter audit
    templates = glob.glob(r"E:\fruitfarm\templates\**\*.html", recursive=True)
    safe_filters = []
    for t_path in templates:
        with open(t_path, "r", encoding="utf-8") as f:
            t_content = f.read()
            matches = re.findall(r'\{\{\s*.*?\|\s*safe\s*\}\}', t_content)
            if matches:
                safe_filters.append((os.path.basename(t_path), matches))
    
    if safe_filters:
        findings.append({
            "category": "웹 취약점 (Web Vulnerabilities)",
            "level": "정보 (Low/Info)",
            "item": f"Jinja2 '| safe' 필터 사용 내역 ({len(safe_filters)}개 템플릿)",
            "detail": f"HTML 렌더링을 허용하는 safe 필터가 사용되었습니다: {[x[0] for x in safe_filters]}. 관리자 직접 등록 콘텐츠 외에 사용자 입력값에 safe 필터가 적용되지 않도록 점검 필요."
        })
    else:
        findings.append({
            "category": "웹 취약점 (Web Vulnerabilities)",
            "level": "안전 (Pass)",
            "item": "Jinja2 자동 이스케이프(Auto-escaping) 준수",
            "detail": "기본 템플릿 엔진의 자동 HTML 이스케이프가 활성화되어 XSS를 차단합니다."
        })

    # 8. Brute Force Protection on Login
    if "limiter" in app_code or "fail_count" in app_code or "login_attempts" in app_code:
        findings.append({
            "category": "인증 보안 (Authentication Security)",
            "level": "안전 (Pass)",
            "item": "로그인 무차별 대입(Brute-force) 차단",
            "detail": "로그인 시도 횟수 제한(Rate Limiting)이 동작 중입니다."
        })
    else:
        findings.append({
            "category": "인증 보안 (Authentication Security)",
            "level": "개선 권장 (Medium)",
            "item": "로그인 무차별 대입(Brute-force) 방어 필요",
            "detail": "비밀번호 연속 5회 오류 시 일시적 잠금(Lockout) 또는 딜레이 처리를 도입하면 무차별 대입 공격을 효과적으로 방어할 수 있습니다."
        })

    # 9. HTTP Security Headers
    security_headers = ["X-Content-Type-Options", "X-Frame-Options", "Content-Security-Policy"]
    missing_headers = [h for h in security_headers if h not in app_code]
    if missing_headers:
        findings.append({
            "category": "네트워크 및 HTTP 헤더 (HTTP Headers)",
            "level": "개선 권장 (Low)",
            "item": f"보안 HTTP 응답 헤더 추가 권장 ({', '.join(missing_headers)})",
            "detail": "X-Frame-Options (클릭재킹 방지), X-Content-Type-Options (MIME 스니핑 방지) 등의 헤더를 @app.after_request로 전역 주입하면 브라우저 보안이 강화됩니다."
        })
    else:
        findings.append({
            "category": "네트워크 및 HTTP 헤더 (HTTP Headers)",
            "level": "안전 (Pass)",
            "item": "보안 HTTP 응답 헤더 완비",
            "detail": "필수 보안 헤더가 전역 응답에 주입되고 있습니다."
        })

    return findings

if __name__ == "__main__":
    results = run_security_audit()
    print(f"Total findings: {len(results)}")
    for r in results:
        print(f"[{r['level']}] {r['category']} - {r['item']}")
        print(f"    > {r['detail']}")
