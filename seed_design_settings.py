import sqlite3
import os

DB_PATH = os.path.join(r"E:\fruitfarm", "fruitfarm.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

design_defaults = {
    'theme_preset': 'luxury_dark', # 'luxury_dark', 'modern_light', 'tropical_emerald', 'sunset_amber'
    'theme_primary_color': '#E6A23C',
    'hero_badge_text': 'Phu Quoc Sonasea 12 메인 스트리트 플래그십',
    'hero_title_line1': '베트남 최상위 1% 골드망고',
    'hero_title_line2': '무설탕 저온건조의 압도적 풍미',
    'hero_subtitle': '호치민 직영 HACCP 공장 가공 · 전 품목 100% 무설탕 저온건조 프리미엄 특산품. $100 이상 결제 시 한국 자택 무료 직배송으로 15kg 항공 수하물 초과운임 없이 가볍게 여행하세요.',
    'hero_bg_image': '/static/images/store/store_exterior.png',
    'top_announcement_text': '$100 이상 결제 시 한국 자택 100% 무료 직배송 (Zero Baggage 캐리어 부담 제로)',
    'show_store_gallery': '1',
    'show_competitor_matrix': '1',
    'show_diy_builder': '1',
    'show_guide_b2b_button': '1'
}

for k, v in design_defaults.items():
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (k, v))

conn.commit()
conn.close()
print("Design settings initialized successfully!")
