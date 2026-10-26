import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/cloud.png",
    "embeds": [
        {
            "title": "⚡ [서버 재가동 완료] PC 재부팅에 따른 서비스 자동 복구",
            "description": "사용자 PC 재부팅으로 중단되었던 Flask 웹서버 및 Cloudflare 터널을 정상 재가동하였습니다.",
            "color": 3066993,
            "fields": [
                {
                    "name": "🌐 신규 외부 공용 주소",
                    "value": "https://smith-citizen-hopkins-pic.trycloudflare.com",
                    "inline": False
                },
                {
                    "name": "⚙️ 현재 가동 상태",
                    "value": "Flask 포트 5000 (HTTP 200 OK) · Cloudflare 터널 정상 연동",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM System Recovery Bot"
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
