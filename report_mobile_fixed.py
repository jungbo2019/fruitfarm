import json
import urllib.request

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1563830486864887829/myafrjEZomCXKIIkLVtguSbWD6cDEnMINDM--IviAn_tcPO18Ku0sQMxOc56WDLz4V-K"

payload = {
    "username": "Fruit Farm AI Agent",
    "avatar_url": "https://img.icons8.com/color/96/iphone.png",
    "embeds": [
        {
            "title": "📱 [모바일 UI 최적화 & 상시 가동 2단계 적용 완료]",
            "description": "스마트폰 화면 기준 글자 깨짐/맞춤법 오류/버튼 시인성을 전면 개편하고, 윈도우 부팅 시 자동 시작 및 클라우드 배포 패키지 구성을 완료하였습니다.",
            "color": 15105570,
            "fields": [
                {
                    "name": "1. 📊 비교 매트릭스 표 모바일 스와이프화",
                    "value": "글자가 세로 1글자씩 깨지던 현상 해결 (최소 폭 760px + 좌우 스와이프 안내 배지)",
                    "inline": False
                },
                {
                    "name": "2. 🔤 브랜드 명칭 및 맞춤법 정돈",
                    "value": "비표준 표기('푸룻팜') ➔ 정식 국영문 표준 **'FRUIT FARM (후르츠팜)'** 전수 통일, 어색한 단어 끊김(`break-keep`) 수정",
                    "inline": False
                },
                {
                    "name": "3. 🔘 버튼 시인성 및 플로팅 버튼 최적화",
                    "value": "`[직접 맛 선택]` 흐릿한 회색 폰트 ➔ 고대비 볼드 버튼 교체, 화면 가리던 카톡 버튼 컴팩트화",
                    "inline": False
                },
                {
                    "name": "4. 🚀 2번 진행 (윈도우 자동실행 등록 & 클라우드 패키지 완비)",
                    "value": "PC 부팅 시 서버/터널 자동 실행(`shell:startup`) 등록 완료 및 24시간 클라우드 배포 파일(Dockerfile, Procfile) 생성 완료",
                    "inline": False
                }
            ],
            "footer": {
                "text": "FRUIT FARM Mobile QA & 24/7 Architecture"
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
