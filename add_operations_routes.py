import re

routes_code = """
# -------------------------------------------------------------
# 1~10 MASTER OPERATIONS COCKPIT & FINANCIAL/SHORTAGE CONTROL
# -------------------------------------------------------------
@app.route('/admin/operations')
def admin_operations():
    conn = get_db()
    cursor = conn.cursor()

    # 1. Total Orders & Revenue
    cursor.execute(\"\"\"
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
    \"\"\")
    finance = dict(cursor.fetchone())

    # Calculate Net Profit
    total_expenses = (finance['total_cogs_usd'] + 
                      finance['total_delivery_expense_usd'] + 
                      finance['total_packaging_expense_usd'] + 
                      finance['total_guide_commission_usd'])
    net_profit_usd = finance['total_revenue_usd'] - total_expenses
    rate = float(get_settings().get('usd_krw_rate', 1380))
    net_profit_krw = int(net_profit_usd * rate)
    profit_margin = round((net_profit_usd / finance['total_revenue_usd'] * 100), 1) if finance['total_revenue_usd'] > 0 else 0

    # 2. Stock Shortage Alert (< 20 units)
    cursor.execute(\"\"\"
        SELECT id, name, category, stock_quantity, weight_g, barcode
        FROM products
        WHERE stock_quantity < 25
        ORDER BY stock_quantity ASC
    \"\"\")
    shortage_items = [dict(row) for row in cursor.fetchall()]

    # 3. Pipeline Order Counts
    cursor.execute(\"\"\"
        SELECT 
            SUM(CASE WHEN order_status = 'received' THEN 1 ELSE 0 END) as count_received,
            SUM(CASE WHEN order_status = 'checked' OR order_status = 'preparing' THEN 1 ELSE 0 END) as count_checked,
            SUM(CASE WHEN order_status = 'dispatched' THEN 1 ELSE 0 END) as count_dispatched,
            SUM(CASE WHEN order_status = 'shipping' THEN 1 ELSE 0 END) as count_shipping,
            SUM(CASE WHEN order_status = 'delivered' THEN 1 ELSE 0 END) as count_delivered
        FROM orders
    \"\"\")
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
def admin_marketing():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(\"\"\"
        SELECT id, order_number, customer_name, customer_phone, delivery_address, delivery_type, order_status
        FROM orders
        ORDER BY id DESC LIMIT 10
    \"\"\")
    recent_orders = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return render_template('admin/marketing.html', recent_orders=recent_orders)

# -------------------------------------------------------------
# QUICK 1-CLICK SEQUENTIAL PIPELINE ADVANCE
# -------------------------------------------------------------
@app.route('/admin/order/advance-stage', methods=['POST'])
def admin_advance_order_stage():
    order_id = request.form.get('order_id')
    next_stage = request.form.get('next_stage')
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(\"\"\"
        UPDATE orders 
        SET order_status = ?, updated_at = datetime('now')
        WHERE id = ?
    \"\"\", (next_stage, order_id))
    conn.commit()
    conn.close()

    log_event('ORDER', f"주문 #{order_id} 상태 순차 전진 완료 -> {next_stage}")
    flash(f"주문 단계가 성공적으로 [{next_stage}] 상태로 전진되었습니다.", 'success')
    return redirect(request.referrer or url_for('admin_orders'))
"""

with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Insert before if __name__ == '__main__':
marker = "if __name__ == '__main__':"
if marker in code and "def admin_operations():" not in code:
    code = code.replace(marker, routes_code + "\n" + marker)
    with open(r'E:\fruitfarm\app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Routes added to app.py successfully!")
else:
    print("Routes already exist or marker not found.")
