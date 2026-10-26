import sqlite3
import os

DB_PATH = 'E:/fruitfarm/fruitfarm.db'

# Correct data
clean_products = [
    (
        1,
        "[대박 프로모션] 180G 말린과일&견과류 10+2 기획 세트",
        "promo_set",
        "180g 총 12봉 (종류 자유선택 / 골드망고 등)",
        "시중 마트 대비 압도적 품질! 10봉 구매 시 인기 2봉 추가 증정 (총 12봉). 무설탕 저온건조 프리미엄 골드망고 포함 선택 가능",
        100.0, 138000, 2160,
        "/static/images/products/promo_10_2.jpg",
        1, 1, 999, "BEST PROMO (10+2)", "8936001000010"
    ),
    (
        2,
        "[대용량 세트] 400G 말린과일&견과류 5+1 기획 세트",
        "promo_set",
        "400g 대용량 총 6봉 (종류 자유선택)",
        "선물용으로 가장 인기있는 400g 패키지! 5봉 구매 시 1봉 추가 증정. 푸꾸옥 직송 신선 포장",
        100.0, 138000, 2400,
        "/static/images/products/promo_400_5_1.jpg",
        1, 1, 999, "BEST PROMO (5+1)", "8936001000027"
    ),
    (
        3,
        "[프리미엄 신제품] 수제 과일청 5병+1병 기획 세트",
        "promo_set",
        "망고청 / 패션푸룻청 5병 구매시 + 1병 무료 (총 6병)",
        "과일원액 90% + 사탕수수당 10%! 설탕 시럽 마트 제품과 비교 불가. 한 병당 약 20잔 음료/요거트 활용 가능!",
        100.0, 138000, 3000,
        "/static/images/products/promo_syrup_set.jpg",
        1, 1, 999, "NEW (5+1병)", "8936001000034"
    ),
    (
        4,
        "프리미엄 저온건조 골드망고 (180g)",
        "dried_fruit",
        "베트남 최상위 품종 골드망고 100% 저온건조",
        "애플망고보다 윗품종인 골드망고만을 엄선하여 저온건조! 무설탕, 무방부제, HACCP 호치민 자체공장 생산으로 쫀득하고 깊은 천연 단맛.",
        10.0, 13800, 180,
        "/static/images/products/gold_mango_180.jpg",
        1, 0, 450, "인기 1위", "8936001000041"
    ),
    (
        5,
        "프리미엄 저온건조 골드망고 대용량 (400g)",
        "dried_fruit",
        "가족용/선물용 최상급 골드망고 400g",
        "무설탕, 무색소, HACCP 인증. 입안 가득 퍼지는 달콤함과 쫀득한 식감.",
        20.0, 27600, 400,
        "/static/images/products/gold_mango_400.jpg",
        1, 0, 320, "대용량 추천", "8936001000058"
    ),
    (
        6,
        "달콤 쫀득 건용안 (Longan 180g)",
        "dried_fruit",
        "자연의 은은한 달콤함 베트남 특산 용안",
        "영양 가득, 피로 회복에 탁월한 베트남 천연 특산 과일 용안을 정성껏 말렸습니다.",
        10.0, 13800, 180,
        "/static/images/products/longan.jpg",
        0, 0, 200, "시식 강추", "8936001000065"
    ),
    (
        7,
        "청정 레드 건용과 (Dragon Fruit 180g)",
        "dried_fruit",
        "항산화 성분이 풍부한 프리미엄 레드 용과",
        "식이섬유와 항산화 물질이 듬뿍 담긴 레드 용과를 부드럽게 건조하여 과육 본연의 맛을 살렸습니다.",
        10.0, 13800, 180,
        "/static/images/products/dragonfruit.jpg",
        0, 0, 180, "건강 간식", "8936001000072"
    ),
    (
        8,
        "달콤 부드러운 건파파야 (Papaya 180g)",
        "dried_fruit",
        "소화에 좋은 천연 파파야 저온건조",
        "소화 효소가 풍부한 잘 익은 파파야만을 엄선하여 저온에서 위생적으로 말렸습니다.",
        10.0, 13800, 180,
        "/static/images/products/papaya.jpg",
        0, 0, 150, "소화/영양", "8936001000089"
    ),
    (
        9,
        "새콤달콤 건패션푸룻 (Passion Fruit 180g)",
        "dried_fruit",
        "상큼함의 끝판왕! 비타민 폭탄 패션푸룻",
        "톡톡 씹히는 씨앗과 상큼달콤한 과육이 조화로운 인기 간식.",
        10.0, 13800, 180,
        "/static/images/products/passionfruit.jpg",
        1, 0, 210, "여성 선호 1위", "8936001000096"
    ),
    (
        10,
        "프리미엄 껍질 통 캐슈넛 (Cashew Nuts 180g)",
        "nuts",
        "베트남 빈푹성 최고등급 고소한 구운 캐슈넛",
        "짜지 않고 담백하게 볶아내어 견과류 본연의 고소함이 살아있습니다.",
        10.0, 13800, 180,
        "/static/images/products/cashew.jpg",
        1, 0, 300, "안주/간식 강추", "8936001000102"
    ),
    (
        11,
        "고소한 통 마카다미아 (Macadamia 180g / 오프너 포함)",
        "nuts",
        "껍질째 로스팅하여 신선함과 고소함이 2배",
        "크래커(오프너)로 톡 까먹는 재미와 신선한 버터 풍미의 천연 마카다미아.",
        10.0, 13800, 180,
        "/static/images/products/macadamia.jpg",
        1, 0, 280, "인기 선물", "8936001000119"
    ),
    (
        12,
        "바삭한 리얼 코코넛칩 (Coconut Chips 150g)",
        "nuts",
        "첨가물 없는 순수 코코넛 바삭 구이",
        "기름에 튀기지 않고 오븐에 구워 바삭하고 담백한 코코넛의 풍미.",
        9.0, 12400, 150,
        "/static/images/products/coconut_chips.jpg",
        0, 0, 190, "바삭 간식", "8936001000126"
    ),
    (
        13,
        "유기농 히비스커스 꽃차 (Organic Hibiscus 150g)",
        "tea_etc",
        "루비빛 맑은 수색과 은은한 산미의 힐링 티",
        "피부 미용과 피로 회복에 도움을 주는 유기농 히비스커스를 정성껏 말렸습니다.",
        10.0, 13800, 150,
        "/static/images/products/hibiscus.jpg",
        0, 0, 140, "힐링 티", "8936001000133"
    ),
    (
        14,
        "유기농 생강차 (Organic Ginger 180g)",
        "tea_etc",
        "깊고 진한 풍미의 고산지대 천연 생강",
        "몸을 따뜻하게 해주는 베트남 고산지대 천연 생강을 위생적으로 가공했습니다.",
        10.0, 13800, 180,
        "/static/images/products/ginger.jpg",
        0, 0, 120, "건강차", "8936001000140"
    ),
    (
        15,
        "리얼 골드망고청 (500ml)",
        "fruit_syrup",
        "골드망고 생과육 90% 함유 리얼 과일청",
        "설탕 시럽이 아닌 생망고 과육이 그대로! 에이드, 요거트, 빙수 토핑으로 완벽.",
        20.0, 27600, 850,
        "/static/images/products/mango_syrup.jpg",
        1, 0, 160, "카페 인기", "8936001000157"
    ),
    (
        16,
        "리얼 패션푸룻청 (500ml)",
        "fruit_syrup",
        "새콤달콤 패션푸룻 생과육 90% 리얼 과일청",
        "비타민 C 가득! 탄산수에 타면 즉석에서 카페급 패션푸룻 에이드 완성.",
        20.0, 27600, 850,
        "/static/images/products/passion_syrup.jpg",
        1, 0, 150, "에이드 추천", "8936001000164"
    )
]

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

for p in clean_products:
    c.execute("""
        UPDATE products 
        SET name = ?, category = ?, sub_title = ?, description = ?,
            price_usd = ?, price_krw = ?, weight_g = ?, image_url = ?,
            is_best = ?, is_promo = ?, stock = ?, badge = ?, barcode = ?
        WHERE id = ?
    """, (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[0]))

conn.commit()

# Also clean guides names if needed
clean_guides = [
    (1, 'GUIDE_KIM', '김철수 팀장', '하나투어 푸꾸옥 전담', '010-3344-5566', 'guide_kim_pqc', 0.25),
    (2, 'GUIDE_LEE', '이영희 실장', '모두투어 VIP', '010-7788-9900', 'guide_lee_pqc', 0.25),
    (3, 'GUIDE_PARK', '박민수 가이드', '푸꾸옥 고스트 제휴', '010-1122-3344', 'guide_park_pqc', 0.25)
]
for g in clean_guides:
    c.execute("""
        UPDATE guides 
        SET name = ?, agency = ?, phone = ?, kakao_id = ?, commission_rate = ?
        WHERE id = ?
    """, (g[2], g[3], g[4], g[5], g[6], g[0]))

conn.commit()
conn.close()
print("Database successfully restored with clean Korean strings!")
