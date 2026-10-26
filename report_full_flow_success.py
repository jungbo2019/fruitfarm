import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/shop.png",
    "embeds": [
        {
            "title": "🛒 [쇼핑몰 전 기능 복구 및 팩트 점검 완료]",
            "description": "사이트 팩트 정밀 점검과 함께 중단되었던 장바구니·주문 결제 프로세스 전반을 완벽히 복구 및 엔드투엔드 검증하였습니다.",
            "color": 15105570,
            "fields": [
                {
                    "name": "1. 🗺️ 구글 지도 매장 버튼 정상화",
                    "value": "단순 빈 지도가 아닌 푸꾸옥 소나시 매장 실제 위치 검색(`Sonasea Shopping Center Phu Quoc`)으로 직결",
                    "inline": False
                },
                {
                    "name": "2. 🛍️ 장바구니 & 주문서 모달 누락 복구",
                    "value": "`base.html` 내 JS 문법 오류 수정 및 슬라이드 장바구니 서랍(`cartModal`)과 주문 결제 모달(`checkoutModal`) 완비",
                    "inline": False
                },
                {
                    "name": "3. 📦 주문 생성 및 실시간 관제 연동",
                    "value": "상품 담기 ➔ 주문서 작성 ➔ DB 실시간 기록(`orders`) ➔ 실시간 배송조회(`/order/track`) 100% 정상 작동 검증",
                    "inline": False
                },
                {
                    "name": "4. 🎁 10+2 맞춤 골라담기 패키지",
                    "value": "기본 10봉 + 보너스 2봉 선택 시 $100 장바구니 자동 적재 로직 정상 가동",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM 푸꾸옥 플래그십 관제 센터 • Full Flow QA Passed"
            }
        }
    ]
}

req = urllib.request.Request(
    DISCORD_WEBHOOK,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json", "User-Agent": "FruitFarmAgent/1.0"}
)

try:
    with urllib.request.urlopen(req) as resp:
        print(f"Discord report status: {resp.status}")
except Exception as e:
    print(f"Failed to report to discord: {e}")
