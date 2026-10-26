import os
import re

app_path = r"E:\fruitfarm\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add ProxyFix import if missing
if "from werkzeug.middleware.proxy_fix import ProxyFix" not in code:
    code = code.replace(
        "from werkzeug.security import generate_password_hash, check_password_hash",
        "from werkzeug.security import generate_password_hash, check_password_hash\nfrom werkzeug.middleware.proxy_fix import ProxyFix"
    )

# 2. Add ProxyFix setup after app = Flask(__name__)
if "app.wsgi_app = ProxyFix" not in code:
    code = code.replace(
        "app = Flask(__name__)",
        "app = Flask(__name__)\napp.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)"
    )

# 3. Add brute-force tracking & dynamic secure cookie in security configs
security_config_target = """# Security configurations
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fruitfarm-pq2-secure-key-982341908234')
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['TEMPLATES_AUTO_RELOAD'] = True"""

security_config_replacement = """# Security configurations
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fruitfarm-pq2-secure-key-982341908234')
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# -----------------
# Brute-Force Defense Storage
# -----------------
LOGIN_FAILURES = {}

def is_ip_locked(ip):
    rec = LOGIN_FAILURES.get(ip)
    if not rec:
        return False, 0
    now = time.time()
    if rec.get('locked_until', 0) > now:
        remaining = int((rec['locked_until'] - now) // 60) + 1
        return True, remaining
    return False, 0

def record_login_failure(ip):
    now = time.time()
    rec = LOGIN_FAILURES.setdefault(ip, {'count': 0, 'locked_until': 0, 'last_attempt': now})
    if now - rec['last_attempt'] > 1800:
        rec['count'] = 0
    rec['count'] += 1
    rec['last_attempt'] = now
    if rec['count'] >= 5:
        rec['locked_until'] = now + 900  # 15 minutes lockout
    return rec['count']

def reset_login_failure(ip):
    LOGIN_FAILURES.pop(ip, None)"""

if security_config_target in code:
    code = code.replace(security_config_target, security_config_replacement)
else:
    print("WARNING: security_config_target not found verbatim")

# 4. Add dynamic secure cookie check and HTTP headers in before_request / after_request
before_target = """# GLOBAL ADMIN SECURITY ENFORCER
@app.before_request
def enforce_admin_security():"""

before_replacement = """# GLOBAL SECURITY & ENFORCEMENT HOOKS
@app.before_request
def enforce_admin_security():
    # Dynamic HTTPS Secure Cookie Enforcer
    if request.is_secure or request.headers.get('X-Forwarded-Proto') == 'https':
        app.config['SESSION_COOKIE_SECURE'] = True
    else:
        app.config['SESSION_COOKIE_SECURE'] = False"""

if before_target in code:
    code = code.replace(before_target, before_replacement)
else:
    print("WARNING: before_target not found verbatim")

# Add after_request for Security Headers
after_request_code = """
@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
    return response
"""
if "@app.after_request" not in code:
    # insert before context processor
    code = code.replace(
        "# -----------------\n# Context Processor",
        after_request_code + "\n# -----------------\n# Context Processor"
    )

# 5. Patch admin_login with Brute-Force lockout and delay
admin_login_pattern = r"@app\.route\('/admin/login', methods=\['GET', 'POST'\]\)\ndef admin_login\(\):[\s\S]*?return render_template\('admin/login\.html'\)"

admin_login_replacement = """@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    client_ip = request.headers.get('CF-Connecting-IP') or request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    locked, remain_min = is_ip_locked(client_ip)
    if locked:
        flash(f'보안 경고: 비밀번호 5회 연속 오류로 접속이 제한되었습니다. ({remain_min}분 후 재시도)', 'danger')
        return render_template('admin/login.html')

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            reset_login_failure(client_ip)
            session['admin_logged_in'] = True
            session['admin_user'] = username
            log_event('LOGIN', f"관리자 [{username}] 정상 로그인 승인 (IP: {client_ip})", latency=4.2)
            flash('푸꾸옥 플래그십 관리자 시스템에 정상 로그인되었습니다.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin_dashboard'))
        else:
            fail_count = record_login_failure(client_ip)
            time.sleep(1.0)  # Rate limiting delay against dictionary attacks
            if fail_count >= 5:
                flash('보안 경고: 비밀번호 5회 연속 오류로 계정이 15분간 잠금 처리되었습니다.', 'danger')
            else:
                flash(f'아이디 또는 비밀번호가 올바르지 않습니다. (실패: {fail_count}/5회)', 'danger')
    return render_template('admin/login.html')"""

code = re.sub(admin_login_pattern, admin_login_replacement, code)

# 6. Patch /api/guide/verify to mask financial data for non-admins
guide_verify_pattern = r"@app\.route\('/api/guide/verify', methods=\['POST'\]\)\ndef guide_verify\(\):[\s\S]*?return jsonify\(\{'success': False, 'message': str\(e\)\}\), 500"

guide_verify_replacement = """@app.route('/api/guide/verify', methods=['POST'])
def guide_verify():
    try:
        data = request.get_json() or {}
        guide_code = str(data.get('guide_code', '')).strip().upper()
        if not guide_code:
            return jsonify({'success': False, 'message': '가이드 코드를 입력해주세요.'}), 400

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM guides WHERE guide_code = ? AND status = 'active'", (guide_code,))
        row = cursor.fetchone()
        conn.close()

        if not row:
            return jsonify({'success': False, 'message': '유효하지 않거나 등록되지 않은 가이드 코드입니다.'}), 404

        guide = dict(row)
        is_admin = session.get('admin_logged_in', False)

        guide_payload = {
            'guide_code': guide['guide_code'],
            'name': guide['name'],
            'agency': guide['agency'],
            'status': guide['status']
        }

        # Financial breakdown strictly restricted to authenticated administrators
        if is_admin:
            guide_payload.update({
                'commission_rate': guide['commission_rate'],
                'total_orders': guide['total_orders'],
                'total_sales_usd': guide['total_sales_usd'],
                'total_commission_usd': guide['total_commission_usd'],
                'settled_commission_usd': guide['settled_commission_usd'],
                'pending_commission_usd': round(guide['total_commission_usd'] - guide['settled_commission_usd'], 2)
            })

        return jsonify({
            'success': True,
            'guide': guide_payload
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500"""

code = re.sub(guide_verify_pattern, guide_verify_replacement, code)

# Write back
with open(app_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Security patches successfully applied to E:\\fruitfarm\\app.py!")
