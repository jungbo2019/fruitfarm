import re

with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Ensure import urllib.request
if 'import urllib.request' not in code:
    code = code.replace('import os\n', 'import os\nimport urllib.request\n', 1)

# 2. Add send_discord_alert helper right after log_event
discord_helper_code = '''
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
            "description": f"**FRUIT FARM 푸꾸옥 직영 플래그십 (소나시 메인 스트리트)**\\n[👉 공식 디스코드 커뮤니티 참여하기]({invite_url})",
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
'''

if 'def send_discord_alert' not in code:
    code = code.replace("        print(f\"Log error: {e}\")\n", "        print(f\"Log error: {e}\")\n" + discord_helper_code)

# 3. Call send_discord_alert in create_order()
target_create_order = """        log_msg = f"신규 주문 접수 [{order_number}] {customer_name} (${calculated_total_usd + shipping_fee_usd:.2f})"
        if guide_code and guide_commission_usd > 0:
            log_msg += f" (가이드: {guide_code}, RS: ${guide_commission_usd:.2f})"
        log_event('ORDER', log_msg, latency=12.4)"""

replacement_create_order = """        log_msg = f"신규 주문 접수 [{order_number}] {customer_name} (${calculated_total_usd + shipping_fee_usd:.2f})"
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
            print(f"Discord notify err: {e}")"""

if target_create_order in code:
    code = code.replace(target_create_order, replacement_create_order)

# 4. In admin_advance_order_stage, call send_discord_alert
target_advance = """    cursor.execute(\"\"\"
        UPDATE orders 
        SET order_status = ?, updated_at = datetime('now')
        WHERE id = ?
    \"\"\", (next_stage, order_id))
    conn.commit()
    conn.close()"""

replacement_advance = """    cursor.execute(\"\"\"
        UPDATE orders 
        SET order_status = ?, updated_at = datetime('now')
        WHERE id = ?
    \"\"\", (next_stage, order_id))
    conn.commit()

    # Fetch updated order for Discord Stage Alert
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    o_row = cursor.fetchone()
    if o_row:
        order_dict = dict(o_row)
        order_dict['order_status'] = next_stage
        send_discord_alert(order_dict, event_type='stage_changed')
    conn.close()"""

if target_advance in code:
    code = code.replace(target_advance, replacement_advance)

# 5. In admin_settings, add discord keys to allowed_keys
target_keys = """        allowed_keys = [
            'usd_krw_rate', 'korea_shipping_fee_usd', 'korea_shipping_free_threshold_usd',
            'store_branch_name', 'store_address', 'kakao_channel_url', 'store_phone', 'business_hours'
        ]"""

replacement_keys = """        allowed_keys = [
            'usd_krw_rate', 'korea_shipping_fee_usd', 'korea_shipping_free_threshold_usd',
            'store_branch_name', 'store_address', 'kakao_channel_url', 'store_phone', 'business_hours',
            'discord_invite_url', 'discord_webhook_url'
        ]"""

if target_keys in code:
    code = code.replace(target_keys, replacement_keys)

# 6. Add API endpoints for Discord test and webhook save
discord_endpoints = '''
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
'''

if '/api/admin/discord/test' not in code:
    code = code.replace("if __name__ == '__main__':", discord_endpoints + "\nif __name__ == '__main__':")

with open(r'E:\fruitfarm\app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully injected Discord notification engine into app.py")
