import sqlite3
import json
import os
from datetime import datetime, timedelta
import random

DB_PATH = os.path.join(os.path.dirname(__file__), 'fruitfarm.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # 1. Products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL, -- 'dried_fruit', 'nuts', 'fruit_syrup', 'promo_set', 'tea_etc'
        sub_title TEXT,
        description TEXT,
        price_usd REAL NOT NULL,
        price_krw INTEGER NOT NULL,
        weight_g INTEGER DEFAULT 180,
        image_url TEXT,
        is_best BOOLEAN DEFAULT 0,
        is_promo BOOLEAN DEFAULT 0,
        stock INTEGER DEFAULT 999,
        badge TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 2. Orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_number TEXT UNIQUE NOT NULL,
        branch TEXT DEFAULT '푸꾸옥 2호점 (Phu Quoc)',
        customer_name TEXT NOT NULL,
        customer_phone TEXT NOT NULL,
        customer_kakao TEXT,
        delivery_type TEXT NOT NULL, -- 'direct_korea' (한국 직배송) or 'local_phuquoc' (푸꾸옥 현지 배달/픽업)
        delivery_address TEXT NOT NULL, -- 한국 주소 or 리조트/호텔명 & 객실
        customs_id TEXT, -- 개인통관고유부호 (한국 직배송용)
        recipient_name TEXT,
        recipient_phone TEXT,
        delivery_note TEXT,
        total_amount_usd REAL NOT NULL,
        total_amount_krw INTEGER NOT NULL,
        shipping_fee_usd REAL DEFAULT 0,
        shipping_fee_krw INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '계좌이체 (KRW/USD)',
        payment_status TEXT DEFAULT 'pending', -- 'pending', 'paid', 'refunded'
        order_status TEXT DEFAULT 'received', -- 'received', 'preparing', 'shipping', 'delivered', 'cancelled'
        tracking_number TEXT,
        items_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 3. Sample requests table (노쇼핑/쇼핑1회 팀 가이드용)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sample_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guide_name TEXT NOT NULL,
        agency_name TEXT,
        phone TEXT NOT NULL,
        kakao_id TEXT,
        team_type TEXT, -- '노쇼핑', '쇼핑 1회', '자유여행/기타'
        sample_count INTEGER DEFAULT 10,
        pickup_method TEXT, -- '그랩 배달', '푸꾸옥 2호점 직접 방문'
        hotel_or_location TEXT,
        status TEXT DEFAULT '접수완료', -- '접수완료', '발송준비', '전달완료'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 4. Settings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')

    # 5. System Audit & Operation Logs Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type TEXT NOT NULL, -- 'ORDER', 'LOGIN', 'STATUS_CHANGE', 'CONFIG', 'SECURITY'
        message TEXT NOT NULL,
        ip_address TEXT,
        latency_ms REAL DEFAULT 0.0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()

    # Seed default settings
    default_settings = {
        'usd_krw_rate': '1380',
        'korea_shipping_fee_usd': '15',
        'korea_shipping_free_threshold_usd': '100',
        'phuquoc_shipping_fee_usd': '0',
        'store_branch_name': 'FRUIT FARM 푸꾸옥 2호점',
        'store_address': '베트남 푸꾸옥 즈엉동 야시장 인근 FRUIT FARM 2호점 (Phu Quoc)',
        'kakao_channel_url': 'https://pf.kakao.com',
        'store_phone': '+84 90 123 4567',
        'business_hours': '매일 09:00 ~ 22:00 (연중무휴, 무료 시식 상시 운영)'
    }

    for k, v in default_settings.items():
        cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (k, v))

    # Check if products exist, otherwise seed
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        seed_products(conn)

    # Check if sample orders exist, otherwise seed some historical orders for monthly revenue demo
    cursor.execute("SELECT COUNT(*) FROM orders")
    if cursor.fetchone()[0] == 0:
        seed_sample_orders(conn)

    conn.commit()
    conn.close()

def seed_products(conn):
    cursor = conn.cursor()
    products_data = [
        # 프로모션 세트
        (
            "[대박 프로모션] 180G 말린과일&견과류 10+2 기획 세트",
            "promo_set",
            "180g 총 12봉 (종류 자유선택 / 골드망고 등)",
            "시중 마트 대비 압도적 품질! 10봉 구매 시 인기 2봉 추가 증정 (총 12봉). 무설탕 저온건조 프리미엄 골드망고 포함 선택 가능",
            100.0, 138000, 2160,
            "/static/images/products/promo_10_2.jpg",
            1, 1, 999, "BEST PROMO (10+2)"
        ),
        (
            "[대용량 세트] 400G 말린과일&견과류 5+1 기획 세트",
            "promo_set",
            "400g 대용량 총 6봉 (종류 자유선택)",
            "선물용으로 가장 인기있는 400g 패키지! 5봉 구매 시 1봉 추가 증정. 푸꾸옥 직송 신선 포장",
            100.0, 138000, 2400,
            "/static/images/products/promo_400_5_1.jpg",
            1, 1, 999, "BEST PROMO (5+1)"
        ),
        (
            "[프리미엄 신제품] 수제 과일청 5병+1병 기획 세트",
            "promo_set",
            "망고청 / 패션푸룻청 5병 구매시 + 1병 무료 (총 6병)",
            "과일원액 90% + 사탕수수당 10%! 설탕 시럽 마트 제품과 비교 불가. 한 병당 약 20잔 음료/요거트 활용 가능!",
            100.0, 138000, 3000,
            "/static/images/products/promo_syrup_set.jpg",
            1, 1, 999, "NEW (5+1병)"
        ),
        # 단품 - 말린과일
        (
            "프리미엄 저온건조 골드망고 (180g)",
            "dried_fruit",
            "베트남 최상위 품종 골드망고 100% 저온건조",
            "애플망고보다 윗품종인 골드망고만을 엄선하여 저온건조! 무설탕, 무방부제, HACCP 호치민 자체공장 생산으로 쫀득하고 깊은 천연 단맛.",
            10.0, 13800, 180,
            "/static/images/products/gold_mango_180.jpg",
            1, 0, 450, "인기 1위"
        ),
        (
            "프리미엄 저온건조 골드망고 대용량 (400g)",
            "dried_fruit",
            "가족용/선물용 최상급 골드망고 400g",
            "무설탕, 무색소, HACCP 인증. 입안 가득 퍼지는 달콤함과 쫀득한 식감.",
            20.0, 27600, 400,
            "/static/images/products/gold_mango_400.jpg",
            1, 0, 320, "대용량 추천"
        ),
        (
            "달콤 쫀득 건용안 (Longan 180g)",
            "dried_fruit",
            "자연의 은은한 달콤함 베트남 특산 용안",
            "영양 가득, 피로 회복에 탁월한 베트남 천연 특산 과일 용안을 정성껏 말렸습니다.",
            10.0, 13800, 180,
            "/static/images/products/longan.jpg",
            0, 0, 200, "시식 강추"
        ),
        (
            "청정 레드 건용과 (Dragon Fruit 180g)",
            "dried_fruit",
            "항산화 성분이 풍부한 프리미엄 레드 용과",
            "식이섬유와 항산화 물질이 듬뿍 담긴 레드 용과를 부드럽게 건조하여 과육 본연의 맛을 살렸습니다.",
            10.0, 13800, 180,
            "/static/images/products/dragonfruit.jpg",
            0, 0, 180, "건강 간식"
        ),
        (
            "달콤 부드러운 건파파야 (Papaya 180g)",
            "dried_fruit",
            "소화에 좋은 천연 파파야 저온건조",
            "소화 효소가 풍부한 잘 익은 파파야만을 엄선하여 저온에서 위생적으로 말렸습니다.",
            10.0, 13800, 180,
            "/static/images/products/papaya.jpg",
            0, 0, 150, None
        ),
        (
            "새콤달콤 건패션푸룻 (Passion Fruit 180g)",
            "dried_fruit",
            "상큼함의 끝판왕! 비타민 폭탄 패션푸룻",
            "톡톡 씹히는 씨앗과 상큼달콤한 과육이 조화로운 인기 간식.",
            10.0, 13800, 180,
            "/static/images/products/passionfruit.jpg",
            1, 0, 210, "여성 선호 1위"
        ),
        # 견과류 & 유기농 특산품
        (
            "프리미엄 껍질 통 캐슈넛 (Cashew Nuts 180g)",
            "nuts",
            "베트남 빈푹성 최고등급 고소한 구운 캐슈넛",
            "짜지 않고 담백하게 볶아내어 견과류 본연의 고소함이 살아있습니다.",
            10.0, 13800, 180,
            "/static/images/products/cashew.jpg",
            1, 0, 300, "안주/간식 강추"
        ),
        (
            "고소한 통 마카다미아 (Macadamia 180g / 오프너 포함)",
            "nuts",
            "껍질째 로스팅하여 신선함과 고소함이 2배",
            "크래커(오프너)로 톡 까먹는 재미와 신선한 버터 풍미의 천연 마카다미아.",
            10.0, 13800, 180,
            "/static/images/products/macadamia.jpg",
            1, 0, 280, "인기 선물"
        ),
        (
            "바삭한 리얼 코코넛칩 (Coconut Chips 150g)",
            "nuts",
            "첨가물 없는 순수 코코넛 바삭 구이",
            "기름에 튀기지 않고 오븐에 구워 바삭하고 담백한 코코넛의 풍미.",
            9.0, 12400, 150,
            "/static/images/products/coconut_chips.jpg",
            0, 0, 190, None
        ),
        (
            "유기농 히비스커스 꽃차 (Organic Hibiscus 150g)",
            "tea_etc",
            "붉은 루비빛의 유기농 디톡스 히비스커스",
            "붓기 완화와 피부 미용에 뛰어난 유기농 인증 히비스커스 꽃잎 100%.",
            10.0, 13800, 150,
            "/static/images/products/hibiscus.jpg",
            0, 0, 140, "유기농 인증"
        ),
        (
            "유기농 편생강 (Organic Ginger 180g)",
            "tea_etc",
            "은은한 알싸함과 천연 감미의 유기농 편생강",
            "환절기 목 건강과 면역력에 탁월한 프리미엄 편생강.",
            10.0, 13800, 180,
            "/static/images/products/ginger.jpg",
            0, 0, 160, "어르신 인기"
        ),
        # 수제 과일청
        (
            "수제 리얼 골드망고청 (500ml)",
            "fruit_syrup",
            "과일원액 90% + 사탕수수당 10% (한 병당 20잔 활용)",
            "물 한 방울 안 섞인 진한 망고 과육 원액! 요거트 토핑, 탄산수에 타서 망고에이드로 최고입니다.",
            20.0, 27600, 500,
            "/static/images/products/mango_syrup.jpg",
            1, 0, 250, "강력 추천"
        ),
        (
            "수제 리얼 패션푸룻청 (500ml)",
            "fruit_syrup",
            "톡톡 씹히는 백향과 과육 90% 수제청",
            "카페에서 마시는 상큼한 백향과 에이드를 집에서 그대로! 선물용 최고 인기 아이템.",
            20.0, 27600, 500,
            "/static/images/products/passion_syrup.jpg",
            1, 0, 230, "카페 레시피"
        )
    ]

    cursor.executemany('''
    INSERT INTO products (name, category, sub_title, description, price_usd, price_krw, weight_g, image_url, is_best, is_promo, stock, badge)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', products_data)

def seed_sample_orders(conn):
    cursor = conn.cursor()
    # 기준 초기 주문 데이터 1건만 생성 (거짓 더미 없이 단 1건의 정상 주문)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_num = f"FPQ-{datetime.now().strftime('%Y%m%d')}-1001"
    items = [{
        "id": 1,
        "name": "[대박 프로모션] 180G 말린과일&견과류 10+2 기획 세트",
        "price_usd": 100.0,
        "qty": 1,
        "subtotal_usd": 100.0
    }]
    cursor.execute('''
    INSERT INTO orders (
        order_number, branch, customer_name, customer_phone, customer_kakao,
        delivery_type, delivery_address, customs_id, recipient_name, recipient_phone,
        delivery_note, total_amount_usd, total_amount_krw, shipping_fee_usd, shipping_fee_krw,
        payment_method, payment_status, order_status, tracking_number, items_json, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        order_num, '푸꾸옥 2호점 (Phu Quoc)', '홍길동', '010-1234-5678', 'hong_kakao',
        'direct_korea', '서울특별시 서초구 서초대로 301 101동 101호', 'P123456789012',
        '홍길동', '010-1234-5678', '문 앞에 안전하게 배송 부탁드립니다.',
        100.0, 138000, 0, 0,
        '무통장입금', 'pending', 'received', '',
        json.dumps(items, ensure_ascii=False), now_str, now_str
    ))

    # 가이드 샘플 신청 기준 1건만 등록
    cursor.execute('''
    INSERT INTO sample_requests (guide_name, agency_name, phone, kakao_id, team_type, sample_count, pickup_method, hotel_or_location, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', ('김가이드', '모두투어 푸꾸옥팀', '010-3344-5566', 'guide_kim', '노쇼핑', 10, '그랩 배달', '푸꾸옥 빈펄 리조트 로비', '접수완료'))

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")
