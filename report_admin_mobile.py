import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/admin-settings-male.png",
    "embeds": [
        {
            "title": "📱 [관리자 페이지 모바일 최적화 & 외부 링크 통합 완료]",
            "description": "스마트폰에서 접속할 수 있는 관리자 실시간 링크 제공 및 모바일 화면(햄버거 메뉴, 터치 친화적 카드, 간편 사진 촬영 교체) 전면 개편을 완료했습니다.",
            "color": 16750848,
            "fields": [
                {
                    "name": "1. 모바일/외부 접속용 관리자 링크",
                    "value": "https://smith-citizen-hopkins-pic.trycloudflare.com/admin/products\n(스마트폰 및 외부 PC에서 즉시 접속 가능)",
                    "inline": False
                },
                {
                    "name": "2. 모바일 반응형 전용 UI 구축",
                    "value": "• 모바일 슬라이드 햄버거 메뉴 드로어 신설\n• 상단 긴 가이드 아코디언 접기 처리\n• 폰 카메라/앨범 연동 즉시 사진 교체 버튼 최적화",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM 푸꾸옥 플래그십 관리 시스템"
            }
        }
    ]
}

req = urllib.request.Request(
    DISCORD_WEBHOOK,
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
)

try:
    with urllib.request.urlopen(req) as res:
        print(f"Discord report sent: {res.status}")
except Exception as e:
    print(f"Failed to report to discord: {e}")
