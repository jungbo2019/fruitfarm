import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/shield.png",
    "embeds": [
        {
            "title": "🛡️ [보안 감사 결과 보고] 사이트 전체 보안 점검 완료",
            "description": "시스템 전체에 대한 보안 취약점 점검을 완료하였습니다. 핵심 보안 방어선은 견고하며, 일부 추가 강화 권장 사항을 도출하였습니다.",
            "color": 3066993,
            "fields": [
                {
                    "name": "✅ 통과 항목 (Pass)",
                    "value": "• 관리자 접근 제어 (`before_request` 100% 잠금)\n• SQL 인젝션 방어 (파라미터 바인딩 100%)\n• 비밀번호 단방향 해싱 (`werkzeug` PBKDF2)\n• 세션 쿠키 보호 (`HttpOnly`, `SameSite=Lax`)",
                    "inline": False
                },
                {
                    "name": "⚠️ 개선 및 보완 권장 (Action Needed)",
                    "value": "1. `/api/guide/verify` 가이드 수수료/매출 데이터 노출 마스킹\n2. 관리자 로그인 연속 실패 시 Brute-force 딜레이 추가\n3. 보안 HTTP 헤더(`X-Frame-Options`, `nosniff`) 주입",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM Security Auditor • 종합 평가: 양호 (B+)"
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
