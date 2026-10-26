import re

# 1. Update templates/admin/marketing.html
with open(r'E:\fruitfarm\templates\admin\marketing.html', 'r', encoding='utf-8') as f:
    mkt = f.read()

# Remove the top Discord Card entirely
mkt = re.sub(r'<!-- DISCORD LIVE NOTIFICATION & COMMUNITY BOT ENGINE -->[\s\S]*?<!-- 1\. KAKAOTALK LIVE LOCATION', '<!-- 1. KAKAOTALK LIVE LOCATION', mkt)

# In the viral studio, replace Discord channel button with Kakao channel button
discord_btn_target = """                        <button type="button" onclick="selectChannel('discord', this)" class="channel-btn p-3 rounded-2xl border border-stone-200 bg-white font-bold text-stone-700 text-left hover:border-amber-400 transition flex items-center gap-2">
                            <i class="fa-brands fa-discord text-base text-[#5865F2]"></i>
                            <span>디스코드/카톡 번개 공지</span>
                        </button>"""

kakao_btn_replace = """                        <button type="button" onclick="selectChannel('kakao', this)" class="channel-btn p-3 rounded-2xl border border-stone-200 bg-white font-bold text-stone-700 text-left hover:border-amber-400 transition flex items-center gap-2">
                            <i class="fa-solid fa-comment text-base text-amber-500"></i>
                            <span>카카오톡 채널 단체 공지</span>
                        </button>"""

if discord_btn_target in mkt:
    mkt = mkt.replace(discord_btn_target, kakao_btn_replace)
else:
    mkt = re.sub(r'<button[^>]*selectChannel\(\'discord\'[\s\S]*?</button>', kakao_btn_replace, mkt)

# Remove the "디스코드 공유" button
mkt = re.sub(r'<button onclick="shareDirectlyToDiscord\(\)"[\s\S]*?</button>', '', mkt)

# Remove all discord JS functions
discord_funcs = [
    r'function copyDiscordInvite\(\)[\s\S]*?\}',
    r'function saveDiscordWebhook\(\)[\s\S]*?\}',
    r'function testDiscordWebhook\(\)[\s\S]*?\}',
    r'function shareDirectlyToDiscord\(\)[\s\S]*?\}',
]
for df in discord_funcs:
    mkt = re.sub(df, '', mkt)

# In selectChannel JS: replace discord logic with kakao logic
mkt = mkt.replace("} else if (channel === 'discord') {", "} else if (channel === 'kakao') {")
mkt = mkt.replace("previewTag.innerText = '디스코드/카톡 번개 공지';", "previewTag.innerText = '카카오톡 채널 단체 공지 최적화';")
mkt = mkt.replace("} else if (currentChannel === 'discord') {", "} else if (currentChannel === 'kakao') {")
mkt = mkt.replace("📢 [FRUIT FARM 푸꾸옥 플래그십] 오늘 하루 번개 특가 프로모션 공지! ⚡\\n\\n안녕하세요 푸꾸옥 여행자 여러분!\\n오늘 소나시 직영 매장 및 온라인 주문 고객님께 [10+2 골라담기 패키지] 구매 시 시그니처 패션후르츠 1봉을 추가 증정합니다!\\n\\n✔️ 100% 무설탕 저온건조 보증\\n✔️ 푸꾸옥 전지역 리조트 당일 2시간 퀵 배달\\n✔️ $100 이상 한국 자택 무료 직배송\\n\\n지금 바로 참여하세요:\\n👉 ${origin}\\n공식 디스코드 커뮤니티: https://discord.gg/Kym2WKGDX",
                  "📢 [FRUIT FARM 푸꾸옥 플래그십] 오늘 하루 번개 특가 프로모션 공지! ⚡\\n\\n안녕하세요 고객님!\\n오늘 소나시 직영 매장 및 온라인 주문 고객님께 [10+2 골라담기 패키지] 구매 시 시그니처 1봉을 추가 증정합니다!\\n\\n✔️ 100% 무설탕 저온건조 보증\\n✔️ 푸꾸옥 전지역 리조트 당일 2시간 퀵 배달\\n✔️ $100 이상 한국 자택 무료 직배송\\n\\n지금 바로 참여하세요:\\n👉 주문 바로가기: ${origin}")

with open(r'E:\fruitfarm\templates\admin\marketing.html', 'w', encoding='utf-8') as f:
    f.write(mkt)
print("[PASS] Cleaned marketing.html")

# 2. Update templates/admin/base_admin.html
with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'r', encoding='utf-8') as f:
    adm = f.read()

adm = re.sub(r'<a href="\{\{ settings\.get\(\'discord_invite_url\'[\s\S]*?</a>\s*', '', adm)
with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'w', encoding='utf-8') as f:
    f.write(adm)
print("[PASS] Cleaned base_admin.html")

# 3. Update templates/admin/settings.html
with open(r'E:\fruitfarm\templates\admin\settings.html', 'r', encoding='utf-8') as f:
    stg = f.read()

stg = re.sub(r'<div>\s*<label[^>]*>디스코드 공식 커뮤니티 초대 URL[\s\S]*?</div>\s*<div>\s*<label[^>]*>디스코드 실시간 주문 웹훅[\s\S]*?</div>', '', stg)
with open(r'E:\fruitfarm\templates\admin\settings.html', 'w', encoding='utf-8') as f:
    f.write(stg)
print("[PASS] Cleaned settings.html")

# 4. Update templates/admin/dashboard.html
with open(r'E:\fruitfarm\templates\admin\dashboard.html', 'r', encoding='utf-8') as f:
    dsh = f.read()

dsh = dsh.replace('디스코드 & GPS', 'WMS & 실시간 GPS')
dsh = dsh.replace('실시간 디스코드 푸시 및 라이더 이동 위치 관제', '실시간 WMS 관제 및 라이더 이동 위치 관제')
with open(r'E:\fruitfarm\templates\admin\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dsh)
print("[PASS] Cleaned dashboard.html")

print("All Discord UI elements successfully purged from the system.")
