from discord_agent_reporter import report_agent_task

fields = [
    {
        "name": "1. 가이드 B2B 수수료 관제 (/admin/guides)",
        "value": "• [+ 신규 가이드 등록] 모달 & API 연동\n• 가이드 전용 QR 디지털 명함 실시간 생성기\n• 10팩 무료 시식 샘플 키트 지급 상태 원클릭 토글\n• 25% RS 실시간 수불 대장 및 정산 전표 기능",
        "inline": False
    },
    {
        "name": "2. 9단계 이커머스 밸류체인 (/admin/dashboard)",
        "value": "SNS광고 ➔ 모객 ➔ 결제 ➔ 재고(FEFO) ➔ 운송 ➔ 상황(WMS) ➔ 진행여부 ➔ 이후관리 ➔ 추가매출 9단계 직관적 마스터 관제 맵 탑재",
        "inline": False
    },
    {
        "name": "3. 상품 관리 4대 우선순위 매트릭스 (/admin/products)",
        "value": "• 최우선 1위: 10+2 기획선물세트 (AOV $100+ 무료배송 견인)\n• 핵심 2위: 100% 무설탕 소프트 골드망고 3종 (시식 전환율 88%)\n• 구색 3위: 통캐슈넛 / 통마카다미아 견과류 2종\n• 경험 4위: DIY 10+2 커스텀 골라담기 빌더",
        "inline": False
    },
    {
        "name": "4. 상황별 SNS 바이럴 자동화 스튜디오 (/admin/marketing)",
        "value": "인스타그램 피드/릴스, 네이버 카페 내돈내산 후기, 인플루언서 제안 DM, 디스코드 번개 공지 원클릭 생성 및 복사",
        "inline": False
    },
    {
        "name": "5. 고객 사후관리 (CRM) & 재구매 허브 (/admin/crm)",
        "value": "귀국 30일차 고객 $15 재구매 쿠폰(REORDER15), VIP 특전, 이탈 방지 20% 바우처 및 고객 DB CSV 추출",
        "inline": False
    }
]

report_agent_task(
    "FRUIT FARM 푸꾸옥 직영 플래그십 시스템 구축 종합 보고",
    "정보맨님의 디스코드 서버와 실시간 에이전트 연동이 완료되었습니다.\n지금까지 구축 및 정비된 핵심 시스템 현황을 보고드립니다.",
    status="SUCCESS",
    fields=fields
)
