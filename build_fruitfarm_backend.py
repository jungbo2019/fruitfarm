import re

with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Endpoints for Guide & CRM
new_endpoints = '''
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
'''

if '/api/admin/guide/add' not in code:
    code = code.replace("if __name__ == '__main__':", new_endpoints + "\nif __name__ == '__main__':")
    with open(r'E:\fruitfarm\app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Injected guide APIs and CRM route into app.py")
else:
    print("APIs already present in app.py")
