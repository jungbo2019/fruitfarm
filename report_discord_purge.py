from discord_agent_reporter import report_agent_task

report_agent_task(
    "쇼핑몰 및 관리자 시스템 UI 내 디스코드 완전 제거 완료",
    "사용자님의 지시에 따라 쇼핑몰 푸터, 관리자 마케팅 허브, 사이드바, 환경설정 등 모든 시스템 화면에서 디스코드 관련 카드, 링크, 버튼을 100% 영구 삭제하였습니다.\n\n디스코드는 이제 화면에 노출되지 않으며, 오직 관리자님을 위한 '외부 무인 관제 & AI 에이전트 개발 리포터'로만 뒷단에서 작동합니다.",
    status="SUCCESS",
    fields=[
        {"name": "쇼핑몰 푸터", "value": "디스코드 링크 완전 삭제 (카카오톡 채널 단독 유지)", "inline": True},
        {"name": "관리자 마케팅 허브", "value": "디스코드 관제 카드 제거 ➔ 카카오톡 단체 공지로 교체", "inline": True},
        {"name": "관리자 사이드바", "value": "디스코드 메뉴 삭제 완료", "inline": True}
    ]
)
print("Discord task reported.")
