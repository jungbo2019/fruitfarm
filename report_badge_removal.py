import json
import urllib.request
import os

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/bot.png",
    "embeds": [
        {
            "title": "⚡ [UI 수정 완료] 관리자 로그인 배지 제거 보고",
            "description": "사용자 요청에 따라 로그인 페이지 내 하단 배지 요소를 완벽히 제거하였습니다.",
            "color": 15105570,
            "fields": [
                {
                    "name": "🎯 제거 항목",
                    "value": "~~`푸꾸옥 플래그십 보안 관제 시스템`~~ (노란색 알약 배지 삭제)",
                    "inline": False
                },
                {
                    "name": "📁 수정 파일",
                    "value": "`E:\\fruitfarm\\templates\\admin\\login.html`",
                    "inline": True
                },
                {
                    "name": "🌐 실시간 접속 확인",
                    "value": "https://rotary-haven-oclc-trees.trycloudflare.com/admin/login",
                    "inline": True
                },
                {
                    "name": "🔍 시각적 QA",
                    "value": "헤더 타이틀(`FRUIT FARM ADMIN`) 바로 아래 입력폼 연결 확인 (불필요한 태그/뱃지 전면 제거 완료)",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM 푸꾸옥 플래그십 개발 에이전트 • Automated QA Pass"
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
