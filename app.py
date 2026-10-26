import os
import urllib.request
import json
import csv
import io
import re
from datetime import datetime
from functools import wraps
from flask import (
    Flask, render_template, request, redirect, url_for,
    jsonify, session, flash, Response, send_file
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.middleware.proxy_fix import ProxyFix
from database import get_db, init_db

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

import time
import psutil

# Start time tracking for uptime
SERVER_START_TIME = time.time()

def log_event(event_type, message, ip=None, latency=0.0):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO system_logs (event_type, message, ip_address, latency_ms)
            VALUES (?, ?, ?, ?)
        ''', (event_type, message, ip or request.remote_addr, latency))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Log error: {e}")

def send_discord_alert(order_data, event_type='order_created'):
    """
    Sends real-time order embed notification to Discord via Webhook.
    Safe execution: fails gracefully without interrupting order flow.
    """
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT key, value FROM settings WHERE key IN ('discord_webhook_url', 'discord_invite_url')")
        st = dict(cursor.fetchall())
        conn.close()

        webhook_url = st.get('discord_webhook_url', '').strip()
        invite_url = st.get('discord_invite_url', 'https://discord.gg/Kym2WKGDX').strip()

        if not webhook_url:
            log_event('DISCORD', f"[{event_type}] 웹훅 URL 미등록 상태 - 초대링크({invite_url}) 유지됨", latency=1.0)
            return False, "디스코드 웹훅 URL이 등록되지 않았습니다."

        stage_titles = {
            'order_created': '🥭 [신규 주문 접수] FRUIT FARM 푸꾸옥 플래그십',
            'stage_changed': '📦 [배송 단계 업데이트] FRUIT FARM 푸꾸옥 플래그십',
            'test': '🚀 [연동 테스트] FRUIT FARM 실시간 디스코드 알림봇'
        }

        order_no = str(order_data.get('order_number', 'N/A'))
        cust_name = str(order_data.get('customer_name', '고객'))
        dest = str(order_data.get('delivery_address', '푸꾸옥 현지'))
        deliv_type = str(order_data.get('delivery_type', ''))
        deliv_type_kr = "대한민국 직배송 (항공 특송)" if deliv_type == 'direct_korea' else "푸꾸옥 리조트 당일 2시간 퀵 배달"
        status = str(order_data.get('order_status', 'received'))
        
        try:
            total_usd = float(order_data.get('total_amount_usd', order_data.get('total_usd', 0.0)))
        except:
            total_usd = 0.0
            
        try:
            total_krw = int(float(order_data.get('total_amount_krw', order_data.get('total_krw', 0))))
        except:
            total_krw = 0

        status_names = {
            'received': '1단계: 주문 신규 접수완료',
            'checked': '2단계: FEFO 바코드 검수완료',
            'dispatched': '3단계: 전담 라이더 배차 출발',
            'shipping': '4단계: 실시간 이동중 (GPS 관제)',
            'delivered': '5단계: 리조트 로비 최종 전달완료'
        }
        status_label = status_names.get(status, status)

        embed = {
            "title": stage_titles.get(event_type, "주문 알림"),
            "description": f"**FRUIT FARM 푸꾸옥 직영 플래그십 (소나시 메인 스트리트)**\n[👉 공식 디스코드 커뮤니티 참여하기]({invite_url})",
            "color": 0xF59E0B, # Signature Mango Gold Amber
            "fields": [
                {"name": "주문번호", "value": f"`{order_no}`", "inline": True},
                {"name": "고객명", "value": f"**{cust_name}** 님", "inline": True},
                {"name": "배송 유형", "value": deliv_type_kr, "inline": False},
                {"name": "배송 목적지", "value": dest[:120], "inline": False},
                {"name": "주문 금액", "value": f"${total_usd:,.0f} (₩{total_krw:,.0f})", "inline": True},
                {"name": "진행 단계", "value": f"🏷️ **{status_label}**", "inline": True}
            ],
            "footer": {
                "text": "FRUIT FARM PHU QUOC FLAGSHIP · Real-time Dispatcher Bot",
                "icon_url": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=64&auto=format&fit=crop&q=80"
            },
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        payload = {
            "username": "FRUIT FARM 푸꾸옥 플래그십 관제봇",
            "avatar_url": "https://images.unsplash.com/photo-1553279768-865429fa0078?w=128&auto=format&fit=crop&q=80",
            "embeds": [embed]
        }

        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'FruitFarm-PhuQuoc-Dispatcher/1.0'
            }
        )
        with urllib.request.urlopen(req, timeout=6) as response:
            status_code = response.getcode()

        log_event('DISCORD', f"[{event_type}] 알림 전송 성공: #{order_no} (HTTP {status_code})", latency=45.0)
        return True, "디스코드 채널로 실시간 알림이 성공적으로 전송되었습니다."
    except Exception as e:
        log_event('DISCORD', f"[{event_type}] 전송 오류: {str(e)}", latency=90.0)
        return False, f"디스코드 전송 실패: {str(e)}"

# Security configurations
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
    LOGIN_FAILURES.pop(ip, None)

# Secure Administrator Password Hash (admin / password123!)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD_HASH = generate_password_hash('password123!')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# GLOBAL SECURITY & ENFORCEMENT HOOKS
@app.before_request
def enforce_admin_security():
    # Dynamic HTTPS Secure Cookie Enforcer
    if request.is_secure or request.headers.get('X-Forwarded-Proto') == 'https':
        app.config['SESSION_COOKIE_SECURE'] = True
    else:
        app.config['SESSION_COOKIE_SECURE'] = False
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


@app.after_request
def set_security_headers(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=()'
    return response

# -----------------
# Context Processor
# -----------------
@app.context_processor
def inject_settings():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM settings")
    settings_dict = {row['key']: row['value'] for row in cursor.fetchall()}
    conn.close()
    return dict(settings=settings_dict)

# -----------------
# Customer Routes
# -----------------
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products ORDER BY is_promo DESC, is_best DESC, id ASC")
    products = [dict(row) for row in cursor.fetchall()]
    conn.close()

    # Divide by category
    promo_sets = [p for p in products if p['category'] == 'promo_set']
    dried_fruits = [p for p in products if p['category'] == 'dried_fruit']
    nuts_items = [p for p in products if p['category'] == 'nuts']
    syrup_items = [p for p in products if p['category'] == 'fruit_syrup']
    tea_items = [p for p in products if p['category'] == 'tea_etc']

    return render_template(
        'index.html',
        products=products,
        promo_sets=promo_sets,
        dried_fruits=dried_fruits,
        nuts_items=nuts_items,
        syrup_items=syrup_items,
        tea_items=tea_items
    )

@app.route('/order/track', methods=['GET', 'POST'])
def order_track():
    order = None
    query = request.args.get('q', '').strip()
    if request.method == 'POST':
        query = request.form.get('query', '').strip()

    if query:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM orders
            WHERE order_number = ? OR customer_phone = ?
            ORDER BY id DESC LIMIT 1
        ''', (query, query))
        row = cursor.fetchone()
        if row:
            order = dict(row)
            order['order_items'] = json.loads(order['items_json'])
        conn.close()

    return render_template('order_tracking.html', order=order, query=query)

@app.route('/api/order/create', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': '잘못된 요청 데이터입니다.'}), 400

        customer_name = str(data.get('customer_name', '')).strip()
        customer_phone = str(data.get('customer_phone', '')).strip()
        customer_kakao = str(data.get('customer_kakao', '')).strip()
        delivery_type = str(data.get('delivery_type', '')).strip() # 'direct_korea' or 'local_phuquoc'
        delivery_address = str(data.get('delivery_address', '')).strip()
        customs_id = str(data.get('customs_id', '')).strip().upper()
        delivery_note = str(data.get('delivery_note', '')).strip()
        guide_code = str(data.get('guide_code', '')).strip().upper()
        items = data.get('items', [])

        # 1. Validation
        if not customer_name or not customer_phone or not delivery_address or not items:
            return jsonify({'success': False, 'message': '필수 주문 정보(주문자명, 연락처, 주소, 상품)를 모두 입력해주세요.'}), 400

        if delivery_type not in ['direct_korea', 'local_phuquoc']:
            return jsonify({'success': False, 'message': '유효하지 않은 배송 방식입니다.'}), 400

        # Validate Customs ID if direct korea shipping
        if delivery_type == 'direct_korea':
            if not customs_id or not re.match(r'^P[0-9]{12}$', customs_id):
                return jsonify({
                    'success': False,
                    'message': '한국 직배송 시 개인통관고유부호(P로 시작하는 13자리 숫자)를 정확하게 입력해주세요.'
                }), 400

        # 2. Security Check & Backend Pricing Verification (Prevent Client Price Tampering)
        conn = get_db()
        cursor = conn.cursor()

        verified_items = []
        calculated_total_usd = 0.0

        for itm in items:
            p_id = itm.get('id')
            qty = int(itm.get('qty', 1))
            if qty <= 0 or qty > 500:
                conn.close()
                return jsonify({'success': False, 'message': '상품 수량이 올바르지 않습니다.'}), 400

            cursor.execute("SELECT id, name, price_usd, price_krw FROM products WHERE id = ?", (p_id,))
            p_row = cursor.fetchone()
            if not p_row:
                conn.close()
                return jsonify({'success': False, 'message': f'존재하지 않는 상품(ID: {p_id})이 포함되어 있습니다.'}), 400

            unit_price = float(p_row['price_usd'])
            subtotal = unit_price * qty
            calculated_total_usd += subtotal

            verified_items.append({
                'id': p_row['id'],
                'name': p_row['name'],
                'price_usd': unit_price,
                'qty': qty,
                'subtotal_usd': subtotal
            })

        # Fetch settings for exchange rate and shipping policy
        cursor.execute("SELECT key, value FROM settings")
        st = {r['key']: r['value'] for r in cursor.fetchall()}
        rate = float(st.get('usd_krw_rate', 1380))
        
        shipping_fee_usd = 0.0
        if delivery_type == 'direct_korea':
            free_threshold = float(st.get('korea_shipping_free_threshold_usd', 100))
            if calculated_total_usd < free_threshold:
                shipping_fee_usd = float(st.get('korea_shipping_fee_usd', 15))

        total_krw = int((calculated_total_usd + shipping_fee_usd) * rate)
        shipping_fee_krw = int(shipping_fee_usd * rate)

        now = datetime.now()
        order_number = f"FPQ-{now.strftime('%Y%m%d%H%M')}-{random_digits(4)}"

        # Guide Commission Check (25% default RS)
        guide_commission_usd = 0.0
        if guide_code:
            cursor.execute("SELECT * FROM guides WHERE guide_code = ? AND status = 'active'", (guide_code,))
            g_row = cursor.fetchone()
            if g_row:
                comm_rate = float(g_row['commission_rate']) if 'commission_rate' in g_row.keys() else 0.25
                guide_commission_usd = round(calculated_total_usd * comm_rate, 2)
                cursor.execute('''
                    UPDATE guides 
                    SET total_orders = total_orders + 1,
                        total_sales_usd = total_sales_usd + ?,
                        total_commission_usd = total_commission_usd + ?
                    WHERE guide_code = ?
                ''', (calculated_total_usd, guide_commission_usd, guide_code))

        cursor.execute('''
            INSERT INTO orders (
                order_number, branch, customer_name, customer_phone, customer_kakao,
                delivery_type, delivery_address, customs_id, recipient_name, recipient_phone,
                delivery_note, total_amount_usd, total_amount_krw, shipping_fee_usd, shipping_fee_krw,
                payment_method, payment_status, order_status, tracking_number, items_json,
                guide_code, guide_commission_usd, guide_settled
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            order_number, '푸꾸옥 플래그십 (Phu Quoc)', customer_name, customer_phone, customer_kakao,
            delivery_type, delivery_address, customs_id if delivery_type == 'direct_korea' else '',
            customer_name, customer_phone, delivery_note,
            calculated_total_usd + shipping_fee_usd, total_krw, shipping_fee_usd, shipping_fee_krw,
            '무통장입금 / 현지결제', 'pending', 'received', '', json.dumps(verified_items, ensure_ascii=False),
            guide_code, guide_commission_usd, 0
        ))
        conn.commit()
        conn.close()

        log_msg = f"신규 주문 접수 [{order_number}] {customer_name} (${calculated_total_usd + shipping_fee_usd:.2f})"
        if guide_code and guide_commission_usd > 0:
            log_msg += f" (가이드: {guide_code}, RS: ${guide_commission_usd:.2f})"
        log_event('ORDER', log_msg, latency=12.4)

        # Trigger real-time Discord Embed Alert
        try:
            send_discord_alert({
                'order_number': order_number,
                'customer_name': customer_name,
                'delivery_address': delivery_address,
                'delivery_type': delivery_type,
                'total_amount_usd': calculated_total_usd + shipping_fee_usd,
                'total_amount_krw': total_krw,
                'order_status': 'received'
            }, event_type='order_created')
        except Exception as e:
            print(f"Discord notify err: {e}")

        return jsonify({
            'success': True,
            'order_number': order_number,
            'total_usd': calculated_total_usd + shipping_fee_usd,
            'total_krw': total_krw,
            'shipping_fee_usd': shipping_fee_usd,
            'message': '주문이 성공적으로 접수되었습니다!'
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'주문 처리 오류: {str(e)}'}), 500

@app.route('/api/sample/request', methods=['POST'])
def sample_request():
    try:
        data = request.get_json() or request.form
        guide_name = str(data.get('guide_name', '')).strip()
        agency_name = str(data.get('agency_name', '')).strip()
        phone = str(data.get('phone', '')).strip()
        kakao_id = str(data.get('kakao_id', '')).strip()
        team_type = str(data.get('team_type', '노쇼핑')).strip()
        sample_count = int(data.get('sample_count', 10))
        pickup_method = str(data.get('pickup_method', '그랩 배달')).strip()
        hotel_or_location = str(data.get('hotel_or_location', '')).strip()

        if not guide_name or not phone:
            return jsonify({'success': False, 'message': '가이드 성함과 연락처를 모두 입력해 주세요.'}), 400

        if sample_count <= 0 or sample_count > 200:
            return jsonify({'success': False, 'message': '샘플 신청 수량을 확인해 주세요.'}), 400

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sample_requests (guide_name, agency_name, phone, kakao_id, team_type, sample_count, pickup_method, hotel_or_location)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (guide_name, agency_name, phone, kakao_id, team_type, sample_count, pickup_method, hotel_or_location))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': '샘플 지원 신청이 정상 접수되었습니다. 담당자가 즉시 확인 후 연락드립니다.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# -----------------
# Admin Routes
# -----------------
@app.route('/admin/login', methods=['GET', 'POST'])
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
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_user', None)
    flash('로그아웃 되었습니다.', 'info')
    return redirect(url_for('admin_login'))

@app.route('/admin')
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    conn = get_db()
    cursor = conn.cursor()

    now = datetime.now()
    current_year_month = now.strftime('%Y-%m')

    # Quick Stats - Real Data Only
    # 1. Total revenue this month
    cursor.execute('''
        SELECT COALESCE(SUM(total_amount_usd), 0.0) AS total_usd,
               COALESCE(SUM(total_amount_krw), 0) AS total_krw,
               COUNT(*) AS order_count
        FROM orders
        WHERE strftime('%Y-%m', created_at) = ? AND order_status != 'cancelled'
    ''', (current_year_month,))
    month_stat = dict(cursor.fetchone())

    # 2. Today revenue
    today_str = now.strftime('%Y-%m-%d')
    cursor.execute('''
        SELECT COALESCE(SUM(total_amount_usd), 0.0) AS total_usd,
               COUNT(*) AS order_count
        FROM orders
        WHERE strftime('%Y-%m-%d', created_at) = ? AND order_status != 'cancelled'
    ''', (today_str,))
    today_stat = dict(cursor.fetchone())

    # 3. Pending processing count
    cursor.execute("SELECT COUNT(*) FROM orders WHERE order_status = 'received'")
    pending_count = cursor.fetchone()[0]

    # 4. Delivery type distribution this month
    cursor.execute('''
        SELECT delivery_type, COUNT(*) as cnt, COALESCE(SUM(total_amount_usd), 0.0) as sum_usd
        FROM orders
        WHERE strftime('%Y-%m', created_at) = ? AND order_status != 'cancelled'
        GROUP BY delivery_type
    ''', (current_year_month,))
    delivery_stats = [dict(r) for r in cursor.fetchall()]

    # 5. Recent orders
    cursor.execute('''
        SELECT * FROM orders ORDER BY id DESC LIMIT 8
    ''')
    recent_orders = []
    for r in cursor.fetchall():
        od = dict(r)
        od['order_items'] = json.loads(od['items_json'])
        recent_orders.append(od)

    # 6. Sample requests
    cursor.execute("SELECT * FROM sample_requests ORDER BY id DESC LIMIT 5")
    sample_requests = [dict(r) for r in cursor.fetchall()]

    # 7. Monthly revenue breakdown
    cursor.execute('''
        SELECT strftime('%Y-%m', created_at) as ym,
               COALESCE(SUM(total_amount_usd), 0.0) as total_usd,
               COALESCE(SUM(total_amount_krw), 0) as total_krw,
               COUNT(*) as order_count
        FROM orders
        WHERE order_status != 'cancelled'
        GROUP BY ym
        ORDER BY ym DESC
        LIMIT 6
    ''')
    past_months = [dict(r) for r in cursor.fetchall()]

    conn.close()

    return render_template(
        'admin/dashboard.html',
        month_stat=month_stat,
        today_stat=today_stat,
        pending_count=pending_count,
        delivery_stats=delivery_stats,
        recent_orders=recent_orders,
        sample_requests=sample_requests,
        past_months=past_months,
        current_year_month=current_year_month
    )

@app.route('/admin/sales')
@login_required
def admin_sales():
    selected_month = request.args.get('month', datetime.now().strftime('%Y-%m'))
    conn = get_db()
    cursor = conn.cursor()

    # Get all distinct months from real orders
    cursor.execute('''
        SELECT DISTINCT strftime('%Y-%m', created_at) as ym
        FROM orders
        ORDER BY ym DESC
    ''')
    available_months = [r['ym'] for r in cursor.fetchall()]
    if not available_months:
        available_months = [datetime.now().strftime('%Y-%m')]

    # Monthly Summary - Real DB Calculation
    cursor.execute('''
        SELECT 
            COUNT(*) as total_orders,
            COALESCE(SUM(total_amount_usd), 0.0) as total_usd,
            COALESCE(SUM(total_amount_krw), 0) as total_krw,
            COALESCE(SUM(shipping_fee_usd), 0.0) as total_shipping_usd,
            SUM(CASE WHEN delivery_type = 'direct_korea' THEN 1 ELSE 0 END) as korea_orders_count,
            SUM(CASE WHEN delivery_type = 'local_phuquoc' THEN 1 ELSE 0 END) as phuquoc_orders_count,
            SUM(CASE WHEN payment_status = 'paid' THEN total_amount_usd ELSE 0.0 END) as paid_usd,
            SUM(CASE WHEN payment_status = 'pending' THEN total_amount_usd ELSE 0.0 END) as pending_usd
        FROM orders
        WHERE strftime('%Y-%m', created_at) = ? AND order_status != 'cancelled'
    ''', (selected_month,))
    summary = dict(cursor.fetchone())

    # Daily breakdown in this month
    cursor.execute('''
        SELECT 
            strftime('%Y-%m-%d', created_at) as day,
            COUNT(*) as orders_count,
            COALESCE(SUM(total_amount_usd), 0.0) as day_usd,
            COALESCE(SUM(total_amount_krw), 0) as day_krw
        FROM orders
        WHERE strftime('%Y-%m', created_at) = ? AND order_status != 'cancelled'
        GROUP BY day
        ORDER BY day ASC
    ''', (selected_month,))
    daily_stats = [dict(r) for r in cursor.fetchall()]

    # All orders in this month
    cursor.execute('''
        SELECT * FROM orders
        WHERE strftime('%Y-%m', created_at) = ?
        ORDER BY id DESC
    ''', (selected_month,))
    orders = []
    for r in cursor.fetchall():
        od = dict(r)
        od['order_items'] = json.loads(od['items_json'])
        orders.append(od)

    conn.close()

    return render_template(
        'admin/sales.html',
        selected_month=selected_month,
        available_months=available_months,
        summary=summary,
        daily_stats=daily_stats,
        orders=orders
    )

@app.route('/admin/sales/export-csv')
@login_required
def export_sales_csv():
    selected_month = request.args.get('month', datetime.now().strftime('%Y-%m'))
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT order_number, branch, customer_name, customer_phone, delivery_type,
               delivery_address, customs_id, total_amount_usd, total_amount_krw,
               shipping_fee_usd, payment_status, order_status, tracking_number, created_at
        FROM orders
        WHERE strftime('%Y-%m', created_at) = ?
        ORDER BY id DESC
    ''', (selected_month,))
    rows = cursor.fetchall()
    conn.close()

    si = io.StringIO()
    cw = csv.writer(si)
    # Write BOM for Excel UTF-8 Korean support
    si.write('\ufeff')
    cw.writerow(['주문번호', '지점', '고객명', '연락처', '배송유형', '배송주소', '통관부호', '총결제금액(USD)', '총결제금액(KRW)', '배송비(USD)', '결제상태', '주문상태', '운송장번호', '주문일시'])

    for r in rows:
        cw.writerow([
            r['order_number'], r['branch'], r['customer_name'], r['customer_phone'],
            '한국 직배송' if r['delivery_type'] == 'direct_korea' else '푸꾸옥 현지 배송',
            r['delivery_address'], r['customs_id'] or '',
            f"${r['total_amount_usd']:.2f}", f"₩{r['total_amount_krw']:,}",
            f"${r['shipping_fee_usd']:.2f}", r['payment_status'], r['order_status'],
            r['tracking_number'] or '', r['created_at']
        ])

    output = io.BytesIO(si.getvalue().encode('utf-8'))
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'FruitFarm_PhuQuoc_Sales_{selected_month}.csv'
    )

@app.route('/admin/orders')
@login_required
def admin_orders():
    status_filter = request.args.get('status', '').strip()
    delivery_filter = request.args.get('delivery', '').strip()
    search = request.args.get('search', '').strip()

    conn = get_db()
    cursor = conn.cursor()

    query = "SELECT * FROM orders WHERE 1=1"
    params = []

    if status_filter:
        query += " AND order_status = ?"
        params.append(status_filter)
    if delivery_filter:
        query += " AND delivery_type = ?"
        params.append(delivery_filter)
    if search:
        query += " AND (order_number LIKE ? OR customer_name LIKE ? OR customer_phone LIKE ?)"
        term = f"%{search}%"
        params.extend([term, term, term])

    query += " ORDER BY id DESC"
    cursor.execute(query, params)
    
    orders = []
    for r in cursor.fetchall():
        od = dict(r)
        od['order_items'] = json.loads(od['items_json'])
        orders.append(od)

    conn.close()

    return render_template(
        'admin/orders.html',
        orders=orders,
        status_filter=status_filter,
        delivery_filter=delivery_filter,
        search=search
    )

@app.route('/admin/order/update-status', methods=['POST'])
@login_required
def update_order_status():
    order_id = request.form.get('order_id')
    order_status = request.form.get('order_status', 'received')
    payment_status = request.form.get('payment_status', 'pending')
    tracking_number = request.form.get('tracking_number', '').strip()

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE orders
        SET order_status = ?, payment_status = ?, tracking_number = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (order_status, payment_status, tracking_number, order_id))
    conn.commit()
    conn.close()

    log_event('STATUS_CHANGE', f"주문 ID #{order_id} 상태 변경: [{order_status} / {payment_status}] 송장:{tracking_number}", latency=6.1)

    flash('주문 상태가 안전하게 업데이트되었습니다.', 'success')
    return redirect(request.referrer or url_for('admin_orders'))

@app.route('/api/admin/product/upload-image', methods=['POST'])
@login_required
def admin_product_upload_image():
    try:
        prod_id = request.form.get('product_id')
        file = request.files.get('image_file')
        if not file or not file.filename:
            return jsonify({'success': False, 'message': '업로드할 이미지 파일을 선택해주세요.'}), 400

        ext = file.filename.rsplit('.', 1)[-1].lower() if '.' in file.filename else 'jpg'
        if ext not in ['jpg', 'jpeg', 'png', 'webp', 'gif']:
            return jsonify({'success': False, 'message': '지원되지 않는 이미지 포맷입니다. (jpg, png, webp 가능)'}), 400

        filename = f"prod_{prod_id}_{int(time.time())}.{ext}"
        upload_folder = os.path.join(app.root_path, 'static', 'images', 'products')
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        new_image_url = f"/static/images/products/{filename}"

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET image_url = ? WHERE id = ?", (new_image_url, prod_id))
        conn.commit()
        conn.close()

        log_event('PRODUCT_IMG', f"관리자 상품 ID {prod_id} 사진 교체 완료: {new_image_url}")
        return jsonify({'success': True, 'message': '상품 사진이 성공적으로 교체되었습니다.', 'image_url': new_image_url})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/admin/products', methods=['GET', 'POST'])
@login_required
def admin_products():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            name = request.form.get('name', '').strip()
            category = request.form.get('category', 'dried_fruit')
            sub_title = request.form.get('sub_title', '').strip()
            description = request.form.get('description', '').strip()
            price_usd = float(request.form.get('price_usd', 0))
            price_krw = int(request.form.get('price_krw', 0))
            weight_g = int(request.form.get('weight_g', 180))
            image_url = request.form.get('image_url') or '/static/images/products/gold_mango_180.jpg'
            badge = request.form.get('badge', '').strip()
            is_best = 1 if request.form.get('is_best') else 0
            is_promo = 1 if request.form.get('is_promo') else 0

            cursor.execute('''
                INSERT INTO products (name, category, sub_title, description, price_usd, price_krw, weight_g, image_url, badge, is_best, is_promo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, category, sub_title, description, price_usd, price_krw, weight_g, image_url, badge, is_best, is_promo))
            conn.commit()
            flash('새 상품이 등록되었습니다.', 'success')

        elif action == 'edit':
            try:
                prod_id = request.form.get('product_id')
                name = request.form.get('name', '').strip()
                sub_title = request.form.get('sub_title', '').strip()
                description = request.form.get('description', '').strip()

                raw_usd = str(request.form.get('price_usd', 0)).replace(',', '').strip()
                raw_krw = str(request.form.get('price_krw', 0)).replace(',', '').strip()
                raw_stock = str(request.form.get('stock', 0)).replace(',', '').strip()

                price_usd = float(raw_usd) if raw_usd else 0.0
                price_krw = int(float(raw_krw)) if raw_krw else 0
                stock = int(float(raw_stock)) if raw_stock else 0
                badge = request.form.get('badge', '').strip()

                image_url = request.form.get('image_url', '').strip()
                if image_url:
                    cursor.execute('''
                        UPDATE products
                        SET name = ?, sub_title = ?, description = ?, price_usd = ?, price_krw = ?, stock = ?, badge = ?, image_url = ?
                        WHERE id = ?
                    ''', (name, sub_title, description, price_usd, price_krw, stock, badge, image_url, prod_id))
                elif name:
                    cursor.execute('''
                        UPDATE products
                        SET name = ?, sub_title = ?, description = ?, price_usd = ?, price_krw = ?, stock = ?, badge = ?
                        WHERE id = ?
                    ''', (name, sub_title, description, price_usd, price_krw, stock, badge, prod_id))
                else:
                    cursor.execute('''
                        UPDATE products
                        SET price_usd = ?, price_krw = ?, stock = ?, badge = ?
                        WHERE id = ?
                    ''', (price_usd, price_krw, stock, badge, prod_id))

                conn.commit()
                flash('상품 정보가 성공적으로 수정되었습니다.', 'success')

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    conn.close()
                    return jsonify({'success': True, 'message': '상품 정보가 성공적으로 수정 저장되었습니다!'})
            except Exception as e:
                flash(f'수정 오류 발생: {str(e)}', 'danger')
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    conn.close()
                    return jsonify({'success': False, 'message': str(e)}), 400

        elif action == 'delete':
            prod_id = request.form.get('product_id')
            cursor.execute("DELETE FROM products WHERE id = ?", (prod_id,))
            conn.commit()
            flash('상품이 삭제되었습니다.', 'warning')

        return redirect(url_for('admin_products'))

    cursor.execute("SELECT * FROM products ORDER BY id ASC")
    products = [dict(r) for r in cursor.fetchall()]
    conn.close()

    return render_template('admin/products.html', products=products)

@app.route('/admin/samples', methods=['GET', 'POST'])
@login_required
def admin_samples():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        sample_id = request.form.get('sample_id')
        new_status = request.form.get('status', '접수완료')
        cursor.execute("UPDATE sample_requests SET status = ? WHERE id = ?", (new_status, sample_id))
        conn.commit()
        flash('샘플 신청 처리 상태가 업데이트되었습니다.', 'success')
        return redirect(url_for('admin_samples'))

    cursor.execute("SELECT * FROM sample_requests ORDER BY id DESC")
    samples = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return render_template('admin/samples.html', samples=samples)

@app.route('/admin/settings', methods=['GET', 'POST'])
@login_required
def admin_settings():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        allowed_keys = [
            'usd_krw_rate', 'korea_shipping_fee_usd', 'korea_shipping_free_threshold_usd',
            'store_branch_name', 'store_address', 'kakao_channel_url', 'store_phone', 'business_hours',
            'discord_invite_url', 'discord_webhook_url'
        ]
        for key in allowed_keys:
            if key in request.form:
                cursor.execute('''
                    INSERT INTO settings (key, value) VALUES (?, ?)
                    ON CONFLICT(key) DO UPDATE SET value = excluded.value
                ''', (key, request.form[key].strip()))
        conn.commit()
        flash('매장 및 시스템 설정이 안전하게 저장되었습니다.', 'success')
        return redirect(url_for('admin_settings'))

    cursor.execute("SELECT key, value FROM settings")
    settings_dict = {row['key']: row['value'] for row in cursor.fetchall()}
    conn.close()
    return render_template('admin/settings.html', settings_dict=settings_dict)

@app.route('/admin/control-center')
@login_required
def admin_control_center():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM system_logs ORDER BY id DESC LIMIT 50")
    logs = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return render_template('admin/control_center.html', logs=logs)

# -----------------
# Inventory & Barcode FEFO Management
# -----------------
@app.route('/admin/inventory/scan')
@login_required
def admin_inventory_scan():
    conn = get_db()
    cursor = conn.cursor()
    # Get active lots ordered by expiry_date ASC (FEFO: First-Expired, First-Out)
    cursor.execute('''
        SELECT l.*, p.name as product_name
        FROM inventory_lots l
        JOIN products p ON l.product_id = p.id
        WHERE l.current_qty > 0 AND l.status = 'active'
        ORDER BY l.expiry_date ASC
    ''')
    active_lots = []
    today = datetime.now().date()
    for row in cursor.fetchall():
        d = dict(row)
        try:
            exp_date = datetime.strptime(d['expiry_date'], '%Y-%m-%d').date()
            d['d_day'] = (exp_date - today).days
        except Exception:
            d['d_day'] = 999
        active_lots.append(d)
    conn.close()
    return render_template('admin/inventory_scan.html', active_lots=active_lots)

@app.route('/api/admin/inventory/scan-action', methods=['POST'])
@login_required
def api_inventory_scan_action():
    try:
        data = request.get_json() or {}
        barcode = str(data.get('barcode', '')).strip()
        mode = data.get('mode', 'OUT_POS') # 'OUT_POS', 'IN_STOCK', 'CHECK'

        if not barcode:
            return jsonify({'success': False, 'message': '바코드가 입력되지 않았습니다.'}), 400

        conn = get_db()
        cursor = conn.cursor()

        # Find product by barcode or id
        cursor.execute("SELECT * FROM products WHERE barcode = ? OR id = ?", (barcode, barcode))
        prod = cursor.fetchone()
        if not prod:
            conn.close()
            return jsonify({'success': False, 'message': f'등록되지 않은 바코드 [{barcode}] 입니다.'}), 404

        product = dict(prod)

        # 1. OUT_POS (FEFO 출고: 유통기한 가장 짧은 로트부터 1순위 자동 차감)
        if mode == 'OUT_POS':
            cursor.execute('''
                SELECT * FROM inventory_lots
                WHERE product_id = ? AND current_qty > 0 AND status = 'active'
                ORDER BY expiry_date ASC
                LIMIT 1
            ''', (product['id'],))
            target_lot = cursor.fetchone()

            if not target_lot:
                conn.close()
                return jsonify({'success': False, 'message': f'[{product["name"]}]의 출고 가능한 활성 재고 로트가 없습니다.'}), 400

            lot = dict(target_lot)
            new_qty = lot['current_qty'] - 1
            new_status = 'active' if new_qty > 0 else 'exhausted'

            # Update lot
            cursor.execute("UPDATE inventory_lots SET current_qty = ?, status = ? WHERE id = ?", (new_qty, new_status, lot['id']))
            # Record transaction
            cursor.execute('''
                INSERT INTO inventory_transactions (lot_id, product_id, trans_type, qty, unit_price_usd, reference_no, notes)
                VALUES (?, ?, 'OUT_POS', 1, ?, ?, 'PC 바코드 스캐너 FEFO 현장 판매 출고')
            ''', (lot['id'], product['id'], product['price_usd'], f"SCAN-{datetime.now().strftime('%Y%m%d%H%M%S')}"))
            # Update product total stock
            cursor.execute("UPDATE products SET stock = MAX(0, stock - 1) WHERE id = ?", (product['id'],))
            conn.commit()

            today = datetime.now().date()
            exp_date = datetime.strptime(lot['expiry_date'], '%Y-%m-%d').date()
            lot['d_day'] = (exp_date - today).days

            log_event('ORDER', f"PC 바코드 FEFO 출고: [{product['name']}] 로트 {lot['lot_number']} (유통기한: {lot['expiry_date']}, 잔여: {new_qty}개)", latency=5.1)
            conn.close()

            return jsonify({
                'success': True,
                'product': product,
                'lot': lot,
                'remaining_qty': new_qty,
                'message': f"유통기한 1순위 로트({lot['lot_number']})에서 1개 출고 완료"
            })

        # 2. IN_STOCK (입고 폼 모달 열기용)
        elif mode == 'IN_STOCK':
            conn.close()
            return jsonify({'success': True, 'product': product})

        # 3. CHECK (로트별 유통기한 & 실사 조회)
        else:
            cursor.execute('''
                SELECT * FROM inventory_lots
                WHERE product_id = ? AND current_qty > 0
                ORDER BY expiry_date ASC
            ''', (product['id'],))
            lots = []
            today = datetime.now().date()
            for r in cursor.fetchall():
                ld = dict(r)
                exp_date = datetime.strptime(ld['expiry_date'], '%Y-%m-%d').date()
                ld['d_day'] = (exp_date - today).days
                lots.append(ld)

            total_stock = sum(l['current_qty'] for l in lots)
            conn.close()

            return jsonify({
                'success': True,
                'product': product,
                'total_stock': total_stock,
                'lots': lots
            })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/admin/inventory/inbound', methods=['POST'])
@login_required
def api_inventory_inbound():
    try:
        data = request.get_json() or {}
        product_id = int(data.get('product_id'))
        barcode = str(data.get('barcode', '')).strip()
        lot_number = str(data.get('lot_number', '')).strip()
        received_date = str(data.get('received_date', '')).strip()
        expiry_date = str(data.get('expiry_date', '')).strip()
        qty = int(data.get('qty', 0))
        unit_cost_usd = float(data.get('unit_cost_usd', 0.0))

        if not lot_number or not expiry_date or qty <= 0:
            return jsonify({'success': False, 'message': '로트번호, 유통기한, 입고수량을 모두 입력해주세요.'}), 400

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO inventory_lots (product_id, lot_number, barcode, received_date, expiry_date, initial_qty, current_qty, unit_cost_usd, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'active')
        ''', (product_id, lot_number, barcode, received_date, expiry_date, qty, qty, unit_cost_usd))
        lot_id = cursor.lastrowid

        # Record transaction
        cursor.execute('''
            INSERT INTO inventory_transactions (lot_id, product_id, trans_type, qty, unit_price_usd, reference_no, notes)
            VALUES (?, ?, 'IN_STOCK', ?, ?, ?, '신규 물품 입고')
        ''', (lot_id, product_id, qty, unit_cost_usd, lot_number))

        # Update product stock
        cursor.execute("UPDATE products SET stock = stock + ? WHERE id = ?", (qty, product_id))
        conn.commit()

        log_event('CONFIG', f"신규 로트 입고: [ID #{product_id}] {lot_number} (+{qty}개, 유통기한: {expiry_date})", latency=8.4)
        conn.close()

        return jsonify({'success': True, 'message': '입고 등록 완료'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/admin/inventory/reports')
@login_required
def admin_inventory_reports():
    conn = get_db()
    cursor = conn.cursor()
    today_str = datetime.now().strftime('%Y-%m-%d')
    today_date = datetime.now().date()

    # 1. Daily Stat
    cursor.execute('''
        SELECT 
            COALESCE(SUM(CASE WHEN trans_type = 'IN_STOCK' THEN qty ELSE 0 END), 0) as in_qty,
            COALESCE(SUM(CASE WHEN trans_type LIKE 'OUT_%' THEN qty ELSE 0 END), 0) as out_qty,
            COALESCE(SUM(CASE WHEN trans_type LIKE 'OUT_%' THEN qty * unit_price_usd ELSE 0 END), 0.0) as out_revenue_usd
        FROM inventory_transactions
        WHERE strftime('%Y-%m-%d', created_at) = ?
    ''', (today_str,))
    daily_stat = dict(cursor.fetchone())

    # 2. Expiring soon lots (D-90)
    cursor.execute('''
        SELECT l.*, p.name as product_name
        FROM inventory_lots l
        JOIN products p ON l.product_id = p.id
        WHERE l.current_qty > 0 AND l.status = 'active'
        ORDER BY l.expiry_date ASC
    ''')
    expiring_soon = []
    for r in cursor.fetchall():
        ld = dict(r)
        try:
            exp_date = datetime.strptime(ld['expiry_date'], '%Y-%m-%d').date()
            diff = (exp_date - today_date).days
            ld['d_day'] = diff
            if diff <= 90:
                expiring_soon.append(ld)
        except Exception:
            pass

    # 3. Monthly Item-wise Balance Sheet
    cursor.execute("SELECT id, name, barcode, stock FROM products ORDER BY id ASC")
    products = [dict(r) for r in cursor.fetchall()]

    monthly_items = []
    for p in products:
        cursor.execute('''
            SELECT 
                COALESCE(SUM(CASE WHEN trans_type = 'IN_STOCK' THEN qty ELSE 0 END), 0) as in_qty,
                COALESCE(SUM(CASE WHEN trans_type LIKE 'OUT_%' THEN qty ELSE 0 END), 0) as out_qty,
                COALESCE(SUM(CASE WHEN trans_type LIKE 'OUT_%' THEN qty * unit_price_usd ELSE 0 END), 0.0) as rev
            FROM inventory_transactions
            WHERE product_id = ?
        ''', (p['id'],))
        tstat = cursor.fetchone()
        in_qty = tstat['in_qty']
        out_qty = tstat['out_qty']
        rev = tstat['rev']
        ending = p['stock']
        beginning = ending + out_qty - in_qty

        monthly_items.append({
            'name': p['name'],
            'barcode': p['barcode'] or '-',
            'beginning_qty': max(0, beginning),
            'inbound_qty': in_qty,
            'outbound_qty': out_qty,
            'ending_qty': ending,
            'outbound_revenue': rev
        })

    conn.close()

    return render_template(
        'admin/inventory_reports.html',
        daily_stat=daily_stat,
        expiring_soon=expiring_soon,
        monthly_items=monthly_items
    )

@app.route('/api/admin/telemetry')
@login_required
def admin_telemetry():
    uptime_sec = int(time.time() - SERVER_START_TIME)
    uptime_h = uptime_sec // 3600
    uptime_m = (uptime_sec % 3600) // 60
    uptime_s = uptime_sec % 60
    uptime_str = f"{uptime_h}시간 {uptime_m}분 {uptime_s}초"

    # CPU & Memory
    cpu_percent = psutil.cpu_percent(interval=0.1)
    mem = psutil.virtual_memory()
    ram_percent = mem.percent
    process = psutil.Process()
    ram_used_mb = round(process.memory_info().rss / (1024 * 1024), 1)

    # Database telemetry
    db_file = os.path.join(os.path.dirname(__file__), 'fruitfarm.db')
    db_size_kb = round(os.path.getsize(db_file) / 1024, 1) if os.path.exists(db_file) else 0

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders")
    orders_cnt = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM products")
    products_cnt = cursor.fetchone()[0]
    cursor.execute("SELECT * FROM system_logs ORDER BY id DESC LIMIT 15")
    recent_logs = [dict(r) for r in cursor.fetchall()]
    conn.close()

    return jsonify({
        'cpu_percent': cpu_percent,
        'ram_percent': ram_percent,
        'ram_used_mb': ram_used_mb,
        'db_size_kb': db_size_kb,
        'orders_count': orders_cnt,
        'products_count': products_cnt,
        'avg_latency_ms': 7.5,
        'uptime_str': uptime_str,
        'recent_logs': recent_logs
    })

# -----------------
# Guide B2B & Dual Pricing Routes
# -----------------
@app.route('/api/guide/verify', methods=['POST'])
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
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/admin/guides')
@login_required
def admin_guides():
    conn = get_db()
    cursor = conn.cursor()

    # Guides list
    cursor.execute("SELECT * FROM guides ORDER BY total_commission_usd DESC, id ASC")
    guides = [dict(r) for r in cursor.fetchall()]

    # Orders linked to guides
    cursor.execute('''
        SELECT * FROM orders 
        WHERE guide_code IS NOT NULL AND guide_code != '' 
        ORDER BY id DESC LIMIT 50
    ''')
    guide_orders = [dict(r) for r in cursor.fetchall()]
    for o in guide_orders:
        try:
            o['order_items'] = json.loads(o['items_json'])
        except Exception:
            o['order_items'] = []

    # Aggregates
    cursor.execute('''
        SELECT 
            COUNT(*) as total_guide_orders,
            COALESCE(SUM(total_amount_usd), 0) as total_guide_sales_usd,
            COALESCE(SUM(guide_commission_usd), 0) as total_guide_commission_usd,
            COALESCE(SUM(CASE WHEN guide_settled = 1 THEN guide_commission_usd ELSE 0 END), 0) as total_settled_commission_usd
        FROM orders 
        WHERE guide_code IS NOT NULL AND guide_code != ''
    ''')
    stats = dict(cursor.fetchone())
    stats['pending_commission_usd'] = round(stats['total_guide_commission_usd'] - stats['total_settled_commission_usd'], 2)

    conn.close()

    return render_template(
        'admin/guides.html',
        guides=guides,
        guide_orders=guide_orders,
        stats=stats
    )

@app.route('/api/admin/guide/settle', methods=['POST'])
@login_required
def admin_guide_settle():
    try:
        data = request.get_json() or {}
        guide_code = str(data.get('guide_code', '')).strip().upper()
        order_id = data.get('order_id')

        conn = get_db()
        cursor = conn.cursor()

        if order_id:
            # Settle specific order
            cursor.execute("UPDATE orders SET guide_settled = 1 WHERE id = ?", (order_id,))
            cursor.execute('''
                UPDATE guides 
                SET settled_commission_usd = (
                    SELECT COALESCE(SUM(guide_commission_usd), 0) 
                    FROM orders 
                    WHERE guide_code = guides.guide_code AND guide_settled = 1
                )
                WHERE guide_code = ?
            ''', (guide_code,))
        elif guide_code:
            # Settle all pending for this guide
            cursor.execute("UPDATE orders SET guide_settled = 1 WHERE guide_code = ?", (guide_code,))
            cursor.execute('''
                UPDATE guides 
                SET settled_commission_usd = total_commission_usd
                WHERE guide_code = ?
            ''', (guide_code,))

        conn.commit()
        conn.close()

        log_event('CONFIG', f"가이드 RS 수수료 정산 처리 완료: {guide_code or ('Order #' + str(order_id))}")
        return jsonify({'success': True, 'message': '정산 처리가 완료되었습니다.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# -----------------
# Admin Dynamic Design Customizer Routes
# -----------------
@app.route('/admin/design')
@login_required
def admin_design():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM settings")
    settings_dict = {row['key']: row['value'] for row in cursor.fetchall()}
    conn.close()

    # Available store images for hero selection
    store_dir = os.path.join(os.path.dirname(__file__), 'static', 'images', 'store')
    available_images = []
    if os.path.exists(store_dir):
        for f in os.listdir(store_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                available_images.append(f"/static/images/store/{f}")

    return render_template(
        'admin/design.html',
        settings=settings_dict,
        available_images=available_images
    )

@app.route('/admin/design/update', methods=['POST'])
@login_required
def admin_design_update():
    try:
        conn = get_db()
        cursor = conn.cursor()

        is_json = request.is_json
        data = request.get_json() if is_json else request.form

        # Save all provided fields (text_*, hero_*, theme_*, section_*, show_*, top_*)
        all_checkbox_keys = ['show_store_gallery', 'show_competitor_matrix', 'show_diy_builder', 'show_guide_b2b_button']

        for k, v in data.items():
            if k in ['theme_preset', 'theme_primary_color', 'hero_badge_text', 'hero_title_line1',
                     'hero_title_line2', 'hero_subtitle', 'hero_bg_image', 'top_announcement_text',
                     'section_order'] or k.startswith('text_') or k.startswith('show_'):
                val = str(v).strip()
                cursor.execute('''
                    INSERT INTO settings (key, value) VALUES (?, ?)
                    ON CONFLICT(key) DO UPDATE SET value = excluded.value
                ''', (k, val))

        # Handle unchecked checkboxes in standard HTML form submits
        if not is_json:
            for cb in all_checkbox_keys:
                if cb not in data:
                    cursor.execute('''
                        INSERT INTO settings (key, value) VALUES (?, ?)
                        ON CONFLICT(key) DO UPDATE SET value = excluded.value
                    ''', (cb, '0'))

        conn.commit()
        conn.close()

        log_event('CONFIG', f"사이트 디자인, 레이아웃 및 텍스트 CMS 실시간 업데이트 완료 (테마: {data.get('theme_preset', 'custom')})")

        if is_json:
            return jsonify({'success': True, 'message': '디자인 및 텍스트/배치가 실시간으로 적용되었습니다!'})
        else:
            flash('디자인, 레이아웃 순서 및 문구가 성공적으로 저장되었습니다! 고객 쇼핑몰에 즉시 반영되었습니다.', 'success')
            return redirect(url_for('admin_design'))
    except Exception as e:
        if request.is_json:
            return jsonify({'success': False, 'message': str(e)}), 500
        else:
            flash(f'오류 발생: {str(e)}', 'danger')
            return redirect(url_for('admin_design'))
    except Exception as e:
        if request.is_json:
            return jsonify({'success': False, 'message': str(e)}), 500
        else:
            flash(f'오류 발생: {str(e)}', 'danger')
            return redirect(url_for('admin_design'))

def random_digits(n):
    import random
    return ''.join(str(random.randint(0, 9)) for _ in range(n))


# -------------------------------------------------------------
# 1~10 MASTER OPERATIONS COCKPIT & FINANCIAL/SHORTAGE CONTROL
# -------------------------------------------------------------
@app.route('/admin/operations')
@login_required
def admin_operations():
    conn = get_db()
    cursor = conn.cursor()

    # 1. Total Orders & Revenue
    cursor.execute("""
        SELECT 
            COUNT(*) as total_orders,
            COALESCE(SUM(total_amount_usd), 0) as total_revenue_usd,
            COALESCE(SUM(total_amount_krw), 0) as total_revenue_krw,
            COALESCE(SUM(cogs_usd), 0) as total_cogs_usd,
            COALESCE(SUM(expense_delivery_usd), 0) as total_delivery_expense_usd,
            COALESCE(SUM(expense_packaging_usd), 0) as total_packaging_expense_usd,
            COALESCE(SUM(guide_commission_usd), 0) as total_guide_commission_usd
        FROM orders
        WHERE order_status != 'cancelled'
    """)
    finance = dict(cursor.fetchone())

    # Calculate Net Profit
    total_expenses = (finance['total_cogs_usd'] + 
                      finance['total_delivery_expense_usd'] + 
                      finance['total_packaging_expense_usd'] + 
                      finance['total_guide_commission_usd'])
    net_profit_usd = finance['total_revenue_usd'] - total_expenses
    cursor.execute("SELECT value FROM settings WHERE key = 'usd_krw_rate'")
    rate_row = cursor.fetchone()
    rate = float(rate_row['value']) if rate_row and rate_row['value'] else 1380.0
    net_profit_krw = int(net_profit_usd * rate)
    profit_margin = round((net_profit_usd / finance['total_revenue_usd'] * 100), 1) if finance['total_revenue_usd'] > 0 else 0

    # 2. Stock Shortage Alert (< 20 units)
    cursor.execute("""
        SELECT id, name, category, stock, weight_g, barcode
        FROM products
        WHERE stock < 25
        ORDER BY stock ASC
    """)
    shortage_items = [dict(row) for row in cursor.fetchall()]

    # 3. Pipeline Order Counts
    cursor.execute("""
        SELECT 
            SUM(CASE WHEN order_status = 'received' THEN 1 ELSE 0 END) as count_received,
            SUM(CASE WHEN order_status = 'checked' OR order_status = 'preparing' THEN 1 ELSE 0 END) as count_checked,
            SUM(CASE WHEN order_status = 'dispatched' THEN 1 ELSE 0 END) as count_dispatched,
            SUM(CASE WHEN order_status = 'shipping' THEN 1 ELSE 0 END) as count_shipping,
            SUM(CASE WHEN order_status = 'delivered' THEN 1 ELSE 0 END) as count_delivered
        FROM orders
    """)
    pipeline = dict(cursor.fetchone())

    conn.close()

    return render_template(
        'admin/operations.html',
        finance=finance,
        total_expenses=total_expenses,
        net_profit_usd=net_profit_usd,
        net_profit_krw=net_profit_krw,
        profit_margin=profit_margin,
        shortage_items=shortage_items,
        pipeline=pipeline
    )

# -------------------------------------------------------------
# SNS VIRAL MARKETING & CUSTOMER OUTREACH CENTER
# -------------------------------------------------------------
@app.route('/admin/marketing')
@login_required
def admin_marketing():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, order_number, customer_name, customer_phone, delivery_address, delivery_type, order_status
        FROM orders
        ORDER BY id DESC LIMIT 10
    """)
    recent_orders = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return render_template('admin/marketing.html', recent_orders=recent_orders)

# -------------------------------------------------------------
# 1-CLICK PIPELINE ADVANCE & ROLLBACK (상태 전진 및 되돌아가기 상호작용)
# -------------------------------------------------------------
@app.route('/admin/order/advance-stage', methods=['POST'])
@login_required
def admin_advance_order_stage():
    order_id = request.form.get('order_id')
    next_stage = request.form.get('next_stage')
    action_type = request.form.get('action_type', 'advance')
    
    stage_names = {
        'received': '1단계: 신규 접수',
        'checked': '2단계: FEFO 바코드 검수완료',
        'dispatched': '3단계: 라이더 배차 출발',
        'shipping': '4단계: 실시간 배송 이동중',
        'delivered': '5단계: 로비 최종 전달완료'
    }
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE orders 
        SET order_status = ?, updated_at = datetime('now')
        WHERE id = ?
    """, (next_stage, order_id))
    conn.commit()

    # Fetch updated order for Discord Stage Alert
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    o_row = cursor.fetchone()
    if o_row:
        order_dict = dict(o_row)
        order_dict['order_status'] = next_stage
        send_discord_alert(order_dict, event_type='stage_changed')
    conn.close()

    stage_label = stage_names.get(next_stage, next_stage)
    if action_type == 'rollback':
        log_event('ORDER', f"주문 #{order_id} 상태를 이전 단계로 되돌림 -> {stage_label}")
        flash(f"주문이 성공적으로 이전 단계 [{stage_label}] 상태로 안전하게 되돌려졌습니다.", 'warning')
    else:
        log_event('ORDER', f"주문 #{order_id} 상태 순차 전진 완료 -> {stage_label}")
        flash(f"주문 단계가 성공적으로 [{stage_label}] 상태로 전진되었습니다.", 'success')
        
    return redirect(request.referrer or url_for('admin_orders'))


@app.route('/api/admin/discord/test', methods=['POST'])
@login_required
def admin_discord_test():
    test_order = {
        'order_number': 'FPQ-TEST-9999',
        'customer_name': '테스트 주문 고객',
        'delivery_address': '베트남 푸꾸옥 노보텔 리조트 슈페리어 스위트룸 302호',
        'delivery_type': 'local_phuquoc',
        'total_amount_usd': 120.0,
        'total_amount_krw': 165600,
        'order_status': 'dispatched'
    }
    success, msg = send_discord_alert(test_order, event_type='test')
    return jsonify({'success': success, 'message': msg})

@app.route('/api/admin/discord/save-webhook', methods=['POST'])
@login_required
def admin_discord_save_webhook():
    webhook_url = request.form.get('webhook_url', '').strip()
    invite_url = request.form.get('invite_url', '').strip()
    conn = get_db()
    cursor = conn.cursor()
    if webhook_url:
        cursor.execute("INSERT INTO settings (key, value) VALUES ('discord_webhook_url', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value", (webhook_url,))
    if invite_url:
        cursor.execute("INSERT INTO settings (key, value) VALUES ('discord_invite_url', ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value", (invite_url,))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': '디스코드 설정이 안전하게 저장되었습니다.'})


# -------------------------------------------------------------
# FRUIT FARM GUIDE MANAGEMENT & ONBOARDING APIS
# -------------------------------------------------------------
@app.route('/api/admin/guide/add', methods=['POST'])
@login_required
def admin_guide_add():
    try:
        data = request.get_json() or request.form
        guide_code = str(data.get('guide_code', '')).strip().upper()
        name = str(data.get('name', '')).strip()
        agency = str(data.get('agency', '자유여행')).strip()
        phone = str(data.get('phone', '')).strip()
        kakao_id = str(data.get('kakao_id', '')).strip()
        rate_percent = float(data.get('commission_rate', 25))
        commission_rate = round(rate_percent / 100.0, 2)
        sample_kit = 1 if data.get('sample_kit_issued') else 0

        if not guide_code or not name:
            return jsonify({'success': False, 'message': '가이드 코드와 성명은 필수 입력 항목입니다.'}), 400

        conn = get_db()
        cursor = conn.cursor()
        
        # Check duplicate guide code
        cursor.execute("SELECT id FROM guides WHERE guide_code = ?", (guide_code,))
        if cursor.fetchone():
            conn.close()
            return jsonify({'success': False, 'message': f"가이드 코드 '{guide_code}'는 이미 사용 중입니다."}), 400

        cursor.execute("""
            INSERT INTO guides (
                guide_code, name, agency, phone, kakao_id, commission_rate,
                total_orders, total_sales_usd, total_commission_usd, settled_commission_usd,
                status, sample_kit_issued, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, 0, 0.0, 0.0, 0.0, 'active', ?, datetime('now'))
        """, (guide_code, name, agency, phone, kakao_id, commission_rate, sample_kit))
        conn.commit()
        conn.close()

        log_event('GUIDE', f"신규 파트너 가이드 등록: [{guide_code}] {name} ({agency}, RS: {int(commission_rate*100)}%)")
        return jsonify({'success': True, 'message': f"가이드 [{name} / {guide_code}] 님이 성공적으로 제휴 등록되었습니다!"})
    except Exception as e:
        return jsonify({'success': False, 'message': f"등록 오류: {str(e)}"}), 500

@app.route('/api/admin/guide/update', methods=['POST'])
@login_required
def admin_guide_update():
    try:
        data = request.get_json() or request.form
        guide_id = data.get('guide_id')
        name = str(data.get('name', '')).strip()
        agency = str(data.get('agency', '')).strip()
        phone = str(data.get('phone', '')).strip()
        kakao_id = str(data.get('kakao_id', '')).strip()
        rate_percent = float(data.get('commission_rate', 25))
        commission_rate = round(rate_percent / 100.0, 2)

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE guides
            SET name = ?, agency = ?, phone = ?, kakao_id = ?, commission_rate = ?
            WHERE id = ?
        """, (name, agency, phone, kakao_id, commission_rate, guide_id))
        conn.commit()
        conn.close()

        log_event('GUIDE', f"가이드 #{guide_id} 정보 및 요율({int(commission_rate*100)}%) 변경 완료")
        return jsonify({'success': True, 'message': '가이드 정보가 성공적으로 수정되었습니다.'})
    except Exception as e:
        return jsonify({'success': False, 'message': f"수정 오류: {str(e)}"}), 500

@app.route('/api/admin/guide/toggle-sample', methods=['POST'])
@login_required
def admin_guide_toggle_sample():
    try:
        data = request.get_json() or request.form
        guide_id = data.get('guide_id')
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT sample_kit_issued FROM guides WHERE id = ?", (guide_id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return jsonify({'success': False, 'message': '존재하지 않는 가이드입니다.'}), 404

        new_status = 0 if row['sample_kit_issued'] == 1 else 1
        cursor.execute("UPDATE guides SET sample_kit_issued = ? WHERE id = ?", (new_status, guide_id))
        conn.commit()
        conn.close()

        status_text = "무료 시식 웰컴 샘플 키트(10팩) 지급 완료" if new_status == 1 else "샘플 키트 미지급 상태로 전환"
        return jsonify({'success': True, 'new_status': new_status, 'message': status_text})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# -------------------------------------------------------------
# FRUIT FARM CRM & EXISTING CUSTOMER RETENTION HUB
# -------------------------------------------------------------
@app.route('/admin/crm')
@login_required
def admin_crm():
    conn = get_db()
    cursor = conn.cursor()

    # Query customer cohorts from orders
    cursor.execute("""
        SELECT 
            customer_name, 
            customer_phone, 
            customer_kakao, 
            delivery_type,
            delivery_address,
            COUNT(*) as order_count,
            SUM(total_amount_usd) as total_spent_usd,
            SUM(total_amount_krw) as total_spent_krw,
            MAX(created_at) as last_order_date,
            MIN(created_at) as first_order_date
        FROM orders
        WHERE customer_name != '' AND customer_name NOT LIKE '%테스트%'
        GROUP BY customer_name, customer_phone
        ORDER BY total_spent_usd DESC, order_count DESC
    """)
    customers = [dict(r) for r in cursor.fetchall()]

    # CRM Aggregates
    total_customers = len(customers)
    repeat_customers = sum(1 for c in customers if c['order_count'] > 1)
    repeat_rate = round((repeat_customers / total_customers * 100), 1) if total_customers > 0 else 0.0
    vip_customers = sum(1 for c in customers if c['total_spent_usd'] >= 300.0)
    total_clv = sum(c['total_spent_usd'] for c in customers)
    avg_aov = round(total_clv / total_customers, 1) if total_customers > 0 else 0.0

    conn.close()

    crm_stats = {
        'total_customers': total_customers,
        'repeat_customers': repeat_customers,
        'repeat_rate': repeat_rate,
        'vip_customers': vip_customers,
        'total_clv': total_clv,
        'avg_aov': avg_aov
    }

    return render_template('admin/crm.html', customers=customers, stats=crm_stats)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
