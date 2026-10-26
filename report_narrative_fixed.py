import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/storytelling.png",
    "embeds": [
        {
            "title": "✨ [스토리텔링 & 모바일 문맥 단절 전면 복구]",
            "description": "스마트폰에서 타사 단점만 짤려 나와 문맥이 끊기던 문제를 해결하고, [3대 비교 카드 ➔ 수하물 절약 ➔ $100 세트 구매]로 물 흐르듯 이어지는 완전한 구매 동선을 구축하였습니다.",
            "color": 15105570,
            "fields": [
                {
                    "name": "1. 📱 모바일 1:1 직관적 비교 카드 도입",
                    "value": "우측으로 짤리던 5열 엑셀 표를 [시판 마트 vs 후르츠팜] 1:1 대조 카드로 모바일 전용 개편",
                    "inline": False
                },
                {
                    "name": "2. 🌉 자연스러운 문맥 연결 다리 (CTA Bridge)",
                    "value": "수하물 계산기 하단에 `[인기 $100 기획 세트 둘러보기 ↓]` 연결 버튼을 배치하여 구매로 직결",
                    "inline": False
                },
                {
                    "name": "3. 📜 법률 고지문 재배치",
                    "value": "문맥을 끊던 공정거래법 박스를 섹션 최하단 안내 각주로 단정하게 정리",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM Narrative & Mobile UX QA Pass"
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
