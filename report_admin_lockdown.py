from discord_agent_reporter import report_agent_task

fields = [
    {
        "name": "🌐 외부 접속용 관리자 주소 (전세계 어디서나)",
        "value": "https://rotary-haven-oclc-trees.trycloudflare.com/admin/login",
        "inline": False
    },
    {
        "name": "🏠 동일 와이파이(LAN) 관리자 주소",
        "value": "http://192.168.1.174:5000/admin/login",
        "inline": False
    },
    {
        "name": "🛡️ 로그인 전면 차단 보안 정책 (100% 적용)",
        "value": "비로그인 상태에서는 /admin 하위 모든 페이지(대시보드, 주문, 상품, 가이드, CRM 등) 접속이 즉시 전면 차단되며 로그인 화면으로 강제 리다이렉트됩니다.",
        "inline": False
    }
]

report_agent_task(
    "관리자 외부 접속 주소 발급 및 비로그인 접근 전면 차단 완료",
    "다른 직원이나 관계자가 어디서나 관리자 화면에 접근할 수 있도록 안전한 보안 HTTPS 외부 접속 주소를 발급하고, 비로그인 상태에서의 관리자 페이지 진입을 100% 완전 차단했습니다.",
    status="SUCCESS",
    fields=fields
)
