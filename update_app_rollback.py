# -*- coding: utf-8 -*-
with open('E:/fruitfarm/app.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')

old_advance_code = '''# -------------------------------------------------------------
# QUICK 1-CLICK SEQUENTIAL PIPELINE ADVANCE
# -------------------------------------------------------------
@app.route('/admin/order/advance-stage', methods=['POST'])
def admin_advance_order_stage():
    order_id = request.form.get('order_id')
    next_stage = request.form.get('next_stage')
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE orders 
        SET order_status = ?, updated_at = datetime('now')
        WHERE id = ?
    """, (next_stage, order_id))
    conn.commit()
    conn.close()

    log_event('ORDER', f"주문 #{order_id} 상태 순차 전진 완료 -> {next_stage}")
    flash(f"주문 단계가 성공적으로 [{next_stage}] 상태로 전진되었습니다.", 'success')
    return redirect(request.referrer or url_for('admin_orders'))'''

new_advance_code = '''# -------------------------------------------------------------
# 1-CLICK PIPELINE ADVANCE & ROLLBACK (상태 전진 및 되돌아가기 상호작용)
# -------------------------------------------------------------
@app.route('/admin/order/advance-stage', methods=['POST'])
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
    conn.close()

    stage_label = stage_names.get(next_stage, next_stage)
    if action_type == 'rollback':
        log_event('ORDER', f"주문 #{order_id} 상태를 이전 단계로 되돌림 -> {stage_label}")
        flash(f"주문이 성공적으로 이전 단계 [{stage_label}] 상태로 안전하게 되돌려졌습니다.", 'warning')
    else:
        log_event('ORDER', f"주문 #{order_id} 상태 순차 전진 완료 -> {stage_label}")
        flash(f"주문 단계가 성공적으로 [{stage_label}] 상태로 전진되었습니다.", 'success')
        
    return redirect(request.referrer or url_for('admin_orders'))'''

if old_advance_code in text:
    text = text.replace(old_advance_code, new_advance_code)
    print("Updated app.py with rollback support!")
else:
    print("Warning: old_advance_code not found directly")

with open('E:/fruitfarm/app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("app.py successfully written!")
