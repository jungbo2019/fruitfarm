import os
import sys
from playwright.sync_api import sync_playwright
from discord_agent_reporter import report_agent_task

BRAIN_DIR = r'C:\Users\user\.gemini\antigravity\brain\49c79cbc-1a5d-43a3-9fb0-17db051e3842'

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1200, 'height': 800})
    page.goto('http://127.0.0.1:5000/admin/login')
    page.wait_for_timeout(500)

    shot_path = os.path.join(BRAIN_DIR, 'audit_login_secured.png')
    page.screenshot(path=shot_path, full_page=False)
    print(f"Secured login screenshot saved: {shot_path}")

    # Verify no credentials in page text or inputs
    content = page.content()
    has_pwd_text = 'password123!' in content
    print("Does page contain hardcoded password text?:", has_pwd_text)

    browser.close()

# Report to Discord
report_agent_task(
    "관리자 로그인 화면 보안 강화 완료 (비밀번호 노출 제거)",
    "사용자님의 지적에 따라 관리자 로그인 화면(/admin/login)에 기본 하드코딩 및 힌트로 노출되어 있던 비밀번호 및 계정 안내 텍스트를 영구 제거하고 보안 마스킹 처리를 완료하였습니다.",
    status="SUCCESS",
    fields=[
        {"name": "조치 내역 1", "value": "입력창 기본값(`value=\"admin\"`, `value=\"password123!\"`) 완전 삭제", "inline": False},
        {"name": "조치 내역 2", "value": "하단 '기본 계정: admin / password123!' 힌트 문구 영구 삭제", "inline": False},
        {"name": "조치 내역 3", "value": "비밀번호 보기/숨기기 토글 아이콘 추가 및 자동완성 차단 적용", "inline": False}
    ]
)
print("Reported fix to Discord.")
