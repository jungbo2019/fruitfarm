import sqlite3

conn = sqlite3.connect(r'E:\fruitfarm\fruitfarm.db')
c = conn.cursor()

updates = {
    'text_competitor_title': '왜 야시장이나 킹콩마트가 아닌 FRUIT FARM(후르츠팜)인가?',
    'text_competitor_subtitle': '베트남 현지 재래시장, 킹콩마트, 모방업체와 당사 FRUIT FARM 직영 플래그십의 실제 품질·위생·통관 비교입니다.',
    'store_address': 'SV2A - V07 Khu Sonasea Bãi Trường, Phú Quốc (소나시 12가 메인 스트리트)',
    'hero_subtitle': '호치민 직영 HACCP 공장 가공 · 100% 무설탕 저온건조 프리미엄 특산품. $100 이상 결제 시 한국 자택 100% 무료 항공 직배송 (수하물 초과운임 ZERO).'
}

for k, v in updates.items():
    c.execute("UPDATE settings SET value = ? WHERE key = ?", (v, k))

conn.commit()
conn.close()
print("Updated database settings successfully!")
