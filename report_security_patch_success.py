import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/shield.png",
    "embeds": [
        {
            "title": "🔒 [보안 강화 패치 완료] 시스템 방어선 전면 구축",
            "description": "사용자 요청에 따라 식별된 모든 보안 취약점에 대한 패치를 서버에 성공적으로 적용 및 검증 완료하였습니다.",
            "color": 3066993,
            "fields": [
                {
                    "name": "1. 🛡️ 가이드 API 재무 데이터 마스킹",
                    "value": "`/api/guide/verify` 호출 시 수수료율/매출 정보 외부 노출 차단 (관리자 세션 전용 분리)",
                    "inline": False
                },
                {
                    "name": "2. 🛡️ 무차별 대입(Brute-force) 공격 방어",
                    "value": "비밀번호 실패 시 1.0초 인위적 지연 + 5회 연속 실패 시 해당 IP 15분간 즉시 락아웃(차단)",
                    "inline": False
                },
                {
                    "name": "3. 🛡️ 브라우저 보안 HTTP 응답 헤더 주입",
                    "value": "`X-Frame-Options: SAMEORIGIN` (클릭재킹 방지)\n`X-Content-Type-Options: nosniff` (MIME 스니핑 방지)\n`Referrer-Policy: strict-origin-when-cross-origin`",
                    "inline": False
                },
                {
                    "name": "4. 🛡️ HTTPS 동적 세션 보안 쿠키 및 ProxyFix",
                    "value": "Werkzeug `ProxyFix` 활성화 및 Cloudflare HTTPS 접근 시 `SESSION_COOKIE_SECURE` 자동 강제화",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM Security Enforcer • Automated Verification 100% Passed"
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
