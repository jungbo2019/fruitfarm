import os
import sys
import json
import urllib.request
from datetime import datetime

# Discord Webhook Storage Path
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'discord_agent_config.json')

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {
        'webhook_url': os.environ.get('DISCORD_AGENT_WEBHOOK_URL', ''),
        'invite_url': 'https://discord.gg/Kym2WKGDX'
    }

def save_config(webhook_url):
    cfg = load_config()
    cfg['webhook_url'] = webhook_url.strip()
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
    return cfg

def report_agent_task(task_title, details, status='IN_PROGRESS', fields=None):
    """
    Broadcasts AI Agent (Antigravity) real-time work progress to Discord channel.
    """
    cfg = load_config()
    webhook_url = cfg.get('webhook_url', '').strip()

    if not webhook_url:
        print("[DISCORD REPORTER] Webhook URL not set yet. Waiting for user's webhook URL.")
        return False, "Webhook URL 미설정"

    status_colors = {
        'IN_PROGRESS': 0x3B82F6, # Blue
        'SUCCESS': 0x10B981,     # Emerald Green
        'WARNING': 0xF59E0B,     # Amber
        'ERROR': 0xEF4444        # Red
    }

    status_emojis = {
        'IN_PROGRESS': '⚡ [진행중]',
        'SUCCESS': '✅ [완료됨]',
        'WARNING': '⚠️ [주의]',
        'ERROR': '🚨 [오류 발생]'
    }

    embed_fields = fields or []
    embed = {
        "title": f"{status_emojis.get(status, '🛠️')} {task_title}",
        "description": details,
        "color": status_colors.get(status, 0x10B981),
        "fields": embed_fields,
        "footer": {
            "text": "Antigravity AI Agent · Real-time Workspace Dispatcher",
            "icon_url": "https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    payload = {
        "username": "Antigravity AI Assistant",
        "avatar_url": "https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg",
        "embeds": [embed]
    }

    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode('utf-8'),
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Antigravity-Agent-Reporter/1.0'
            }
        )
        with urllib.request.urlopen(req, timeout=6) as resp:
            code = resp.getcode()
            print(f"[DISCORD REPORTER] Successfully reported to Discord (HTTP {code})")
            return True, f"HTTP {code}"
    except Exception as e:
        print(f"[DISCORD REPORTER] Failed to report to Discord: {e}")
        return False, str(e)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].startswith('http'):
        save_config(sys.argv[1])
        print("Webhook URL saved.")
        report_agent_task(
            "Antigravity AI 에이전트 실시간 디스코드 연동 완료",
            "지금부터 제가 수행하는 모든 코딩 작업, 파일 수정, 서버 구동, 버그 수정, QA 테스트 등의 실시간 업무 진행 상황이 이 디스코드 채널로 자동 보고됩니다.",
            status='SUCCESS',
            fields=[
                {"name": "연동 서버", "value": "일반 채널 (Kym2WKGDX)", "inline": True},
                {"name": "에이전트", "value": "Google DeepMind Antigravity", "inline": True},
                {"name": "대상 프로젝트", "value": "FRUIT FARM 푸꾸옥 직영 플래그십", "inline": False}
            ]
        )
    else:
        print("Usage: python discord_agent_reporter.py <DISCORD_WEBHOOK_URL>")
