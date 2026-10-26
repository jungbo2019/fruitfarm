import sqlite3
import os

DB_PATH = os.path.join(r"E:\fruitfarm", "fruitfarm.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cms_defaults = {
    # Section Order (Comma separated section IDs)
    'section_order': 'gallery,competitor,promo,builder,catalog,sample,location',

    # Section 1: Gallery
    'text_gallery_badge': 'REAL STORE GALLERY',
    'text_gallery_title': '푸꾸옥 2호점 실제 쇼룸 & 무료 시식 현장',
    'text_gallery_subtitle': '컴퓨터 속 가상 상점이 아닙니다. 소나시 12가 메인 스트리트에 위치한 직영 플래그십 매장에서 눈으로 확인하고 시식하세요.',

    # Section 2: Competitor Matrix
    'text_competitor_badge': 'COMPETITOR BENCHMARK',
    'text_competitor_title': '왜 야시장이나 대형마트가 아닌 푸룻팜인가?',
    'text_competitor_subtitle': '베트남 현지 재래시장, 롯데마트, 엘스토어(L-Store)와 당사 FRUIT FARM의 실제 비교 매트릭스입니다.',

    # Section 3: Promo Set
    'text_promo_badge': 'BEST $100 PACKAGES',
    'text_promo_title': '한국 무료 직배송 $100 기획 세트',
    'text_promo_subtitle': '단 하나의 세트만 주문해도 한국 자택 무료 직배송 혜택이 적용되는 베스트 선물 패키지입니다.',

    # Section 4: 10+2 Builder
    'text_builder_badge': 'CUSTOM DIY PACK',
    'text_builder_title': '10+2 내 맘대로 골라담기 패키지 ($100)',
    'text_builder_subtitle': '180g 말린과일과 견과류 중 원하는 10봉을 고르면, 2봉을 무료로 추가 증정하여 총 12봉을 한국 자택으로 무료 직배송해드립니다.',

    # Section 5: Catalog
    'text_catalog_badge': 'CATALOG & FEFO',
    'text_catalog_title': '푸꾸옥 2호점 단품 상품 전수 검수관',
    'text_catalog_subtitle': 'PC 바코드 기반 FEFO(유통기한 선입선출) 시스템으로 가장 신선한 로트만을 선별하여 출고합니다.',

    # Section 6: Sample Request
    'text_sample_badge': 'FOR GUIDES & TOUR LEADERS',
    'text_sample_title': '가이드 무료 맛보기 샘플팩 지원 신청',
    'text_sample_subtitle': '노쇼핑 / 쇼핑 1회 팀 전담 가이드님을 위해 10개들이 프리미엄 시식 키트를 푸꾸옥 호텔 로비로 그랩 배달해드립니다.',

    # Section 7: Store Location
    'text_location_badge': 'FLAGSHIP STORE',
    'text_location_title': 'FRUIT FARM 푸꾸옥 2호점',
    'text_location_subtitle': '푸꾸옥 최고의 리조트 밀집 지역인 소나시(Sonasea) 야시장 메인 스트리트에 위치하고 있습니다. 노보텔, 풀만, 인터컨티넨탈에서 도보 5분 거리에 위치하여 언제든 편하게 시식하러 오실 수 있습니다.',

    # 3 Value Benefit Cards in Hero
    'text_benefit_1_title': '대한민국 100% 무사통관 보증제',
    'text_benefit_1_desc': '식물검역법 적합 밀봉 가공식품 · 1인당 $150 소액면세 엄격 준수',
    'text_benefit_2_title': '수하물 초과운임 ZERO 무료 직배송',
    'text_benefit_2_desc': '$100 이상 구매 시 한국 자택 문 앞까지 3~5일 안전 배송',
    'text_benefit_3_title': '푸꾸옥 전지역 리조트 당일 2시간 배달',
    'text_benefit_3_desc': '빈펄, 풀만, 인터컨티넨탈, 노보텔 로비로 그랩 퀵 직배송'
}

for k, v in cms_defaults.items():
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (k, v))

conn.commit()
conn.close()
print("CMS text and layout settings initialized successfully!")
