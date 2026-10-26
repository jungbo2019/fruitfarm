import re

# 1. Fix templates/index.html - replace broken fa-plane-shield with fa-shield-halved
with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Check for fa-plane-shield
if 'fa-plane-shield' in idx:
    idx = idx.replace('fa-plane-shield', 'fa-shield-halved')
    print("[PASS] Fixed fa-plane-shield in index.html to fa-shield-halved")

with open(r'E:\fruitfarm\templates\index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

# 2. Fix templates/admin/marketing.html
with open(r'E:\fruitfarm\templates\admin\marketing.html', 'r', encoding='utf-8') as f:
    mkt = f.read()

# Fix multi-line alert in marketing.html
mkt = re.sub(
    r"alert\('선택하신 SNS 최적화 마케팅 문구가 클립보드에 복사되었습니다![\s\r\n]+원하시는 채널에 바로 붙여넣기\(Ctrl\+V\) 하세요\.'\);",
    r"alert('선택하신 SNS 최적화 마케팅 문구가 클립보드에 복사되었습니다! 원하시는 채널에 바로 붙여넣기(Ctrl+V) 하세요.');",
    mkt
)

# Also put default pre-filled text inside textarea so it is NEVER blank even if JS is loading
default_marketing_text = """🥭 푸꾸옥 여행 선물 살 때 캐리어 15kg 수하물 무게 걱정 끝! ✈️

베트남 올 때 이미 꽉 찬 캐리어 때문에 건망고 살까 말까 고민하셨죠?
소나시 상가 메인에 있는 FRUIT FARM 직영 플래그십은 $100 이상 구매 시 10+2 증정에 한국 집 문 앞까지 무료 직배송해 줍니다! ✨

무거운 짐 손으로 들고 공항 갈 필요 없이, 몸만 가볍게 귀국하세요! 🌴

📍 위치: 푸꾸옥 소나시 상가 12가 (노보텔 바로 앞)
🔗 온라인 바로 주문: http://127.0.0.1:5000

#푸꾸옥여행 #푸꾸옥후르츠팜 #소나시야시장 #노보텔푸꾸옥 #푸꾸옥쇼핑 #무설탕건망고 #푸꾸옥기념품 #푸꾸옥맛집 #베트남여행선물"""

mkt = re.sub(
    r'<textarea id="viralOutput"[^>]*></textarea>',
    f'<textarea id="viralOutput" rows="11" readonly class="w-full p-4 rounded-2xl border border-stone-200 bg-stone-50 font-sans text-xs text-stone-800 leading-relaxed focus:outline-none focus:bg-white transition">{default_marketing_text}</textarea>',
    mkt
)

with open(r'E:\fruitfarm\templates\admin\marketing.html', 'w', encoding='utf-8') as f:
    f.write(mkt)
print("[PASS] Fixed marketing.html JS alerts and added default textarea content")

# 3. Fix templates/admin/crm.html
with open(r'E:\fruitfarm\templates\admin\crm.html', 'r', encoding='utf-8') as f:
    crm = f.read()

crm = re.sub(
    r"alert\('사후관리 타겟 메시지가 복사되었습니다![\s\r\n]+고객 카카오톡이나 SMS로 바로 전송하세요\.'\);",
    r"alert('사후관리 타겟 메시지가 복사되었습니다! 고객 카카오톡이나 SMS로 바로 전송하세요.');",
    crm
)

with open(r'E:\fruitfarm\templates\admin\crm.html', 'w', encoding='utf-8') as f:
    f.write(crm)
print("[PASS] Fixed crm.html JS alerts")

# 4. Fix templates/admin/guides.html
with open(r'E:\fruitfarm\templates\admin\guides.html', 'r', encoding='utf-8') as f:
    gds = f.read()

gds = re.sub(
    r"alert\('\[' \+ activeGuideCodeForQr \+ '\] 가이드 전용 주문 링크가 복사되었습니다:[\s\r\n]+\\n' \+ link\);",
    r"alert('[' + activeGuideCodeForQr + '] 가이드 전용 주문 링크가 복사되었습니다:\\n' + link);",
    gds
)

gds = re.sub(
    r"alert\('손님 카톡 전송용 추천 문구가 복사되었습니다![\s\r\n]+손님 단체방에 바로 붙여넣기\(Ctrl\+V\) 하세요\.'\);",
    r"alert('손님 카톡 전송용 추천 문구가 복사되었습니다! 손님 단체방에 바로 붙여넣기(Ctrl+V) 하세요.');",
    gds
)

with open(r'E:\fruitfarm\templates\admin\guides.html', 'w', encoding='utf-8') as f:
    f.write(gds)
print("[PASS] Fixed guides.html JS alerts")
