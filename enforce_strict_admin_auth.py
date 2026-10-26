import re

with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add strict global before_request hook right after login_required
hook_code = '''
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# GLOBAL ADMIN SECURITY ENFORCER
@app.before_request
def enforce_admin_security():
    path = request.path
    # Protect all /admin and /api/admin paths
    if path.startswith('/admin') or path.startswith('/api/admin'):
        if path == '/admin/login':
            return None
        if not session.get('admin_logged_in'):
            if path.startswith('/api/admin'):
                return jsonify({'success': False, 'message': '관리자 인증이 필요합니다.'}), 401
            flash('보안 안내: 관리자 권한으로 로그인 후 이용하실 수 있습니다.', 'warning')
            return redirect(url_for('admin_login', next=request.url))
'''

code = re.sub(
    r'def login_required\(f\):[\s\S]*?return decorated_function',
    hook_code.strip(),
    code,
    count=1
)

# 2. Ensure admin_operations, admin_marketing, admin_advance_order_stage have @login_required
code = code.replace(
    "@app.route('/admin/operations')\ndef admin_operations():",
    "@app.route('/admin/operations')\n@login_required\ndef admin_operations():"
)
code = code.replace(
    "@app.route('/admin/marketing')\ndef admin_marketing():",
    "@app.route('/admin/marketing')\n@login_required\ndef admin_marketing():"
)
code = code.replace(
    "@app.route('/admin/order/advance-stage', methods=['POST'])\ndef admin_advance_order_stage():",
    "@app.route('/admin/order/advance-stage', methods=['POST'])\n@login_required\ndef admin_advance_order_stage():"
)

with open(r'E:\fruitfarm\app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Strict admin security enforcer applied successfully.")
