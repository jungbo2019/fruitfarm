import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/camera.png",
    "embeds": [
        {
            "title": "📸 [기능 개발 완료] 상품 사진 직접 교체/업로드 기능 추가",
            "description": "관리자 페이지에서 상품 대표 사진을 내 컴퓨터 파일 업로드 또는 이미지 URL로 즉시 변경할 수 있도록 개편하였습니다.",
            "color": 15105570,
            "fields": [
                {
                    "name": "1. 📷 사진 위 [사진 교체] 원클릭 카메라 버튼",
                    "value": "상품 이미지 우측 하단 버튼 클릭 시 PC 파일 탐색기 즉시 호출 및 실시간 교체",
                    "inline": False
                },
                {
                    "name": "2. ☁️ 파일 직접 업로드 API 신설",
                    "value": "`/api/admin/product/upload-image` 엔드포인트 연동 (JPG, PNG, WEBP 지원)",
                    "inline": False
                },
                {
                    "name": "3. 🔗 이미지 웹 URL 직접 입력 지원",
                    "value": "입력 폼 내 이미지 경로 직접 수정 및 즉시 미리보기(Live Preview) 지원",
                    "inline": False
                },
                {
                    "name": "🌐 관리자 상품 페이지 확인",
                    "value": "https://rotary-haven-oclc-trees.trycloudflare.com/admin/products",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM 푸꾸옥 플래그십 관제 센터 • Photo Management Live"
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
