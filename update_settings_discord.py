with open(r'E:\fruitfarm\templates\admin\settings.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                <div>
                    <label class="block font-bold text-stone-700 mb-1">카카오톡 채널 상담 URL *</label>
                    <input type="text" name="kakao_channel_url" value="{{ settings_dict.get('kakao_channel_url', 'https://pf.kakao.com') }}" required class="w-full p-2.5 border rounded-xl font-mono">
                    <p class="text-[11px] text-stone-400 mt-1">고객이 카톡 상담 버튼 클릭 시 연결될 채널 주소</p>
                </div>"""

replacement = """                <div>
                    <label class="block font-bold text-stone-700 mb-1">카카오톡 채널 상담 URL *</label>
                    <input type="text" name="kakao_channel_url" value="{{ settings_dict.get('kakao_channel_url', 'https://pf.kakao.com') }}" required class="w-full p-2.5 border rounded-xl font-mono">
                    <p class="text-[11px] text-stone-400 mt-1">고객이 카톡 상담 버튼 클릭 시 연결될 채널 주소</p>
                </div>

                <div>
                    <label class="block font-bold text-stone-700 mb-1">디스코드 공식 커뮤니티 초대 URL *</label>
                    <input type="text" name="discord_invite_url" value="{{ settings_dict.get('discord_invite_url', 'https://discord.gg/Kym2WKGDX') }}" required class="w-full p-2.5 border rounded-xl font-mono">
                    <p class="text-[11px] text-stone-400 mt-1">쇼핑몰 및 관리자에서 연결되는 공식 디스코드 초대 링크</p>
                </div>

                <div>
                    <label class="block font-bold text-stone-700 mb-1">디스코드 실시간 주문 웹훅 (Webhook URL)</label>
                    <input type="text" name="discord_webhook_url" value="{{ settings_dict.get('discord_webhook_url', '') }}" placeholder="https://discord.com/api/webhooks/..." class="w-full p-2.5 border rounded-xl font-mono">
                    <p class="text-[11px] text-stone-400 mt-1">신규 주문 및 배송 상태 변경 시 실시간 임베드 알림을 수신할 웹훅 주소</p>
                </div>"""

if target in content and 'discord_invite_url' not in content:
    content = content.replace(target, replacement)
    with open(r'E:\fruitfarm\templates\admin\settings.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated settings.html with discord fields")
else:
    print("Already updated or target not found")
