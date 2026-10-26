with open(r'E:\fruitfarm\templates\admin\marketing.html', 'r', encoding='utf-8') as f:
    content = f.read()

discord_card_html = '''
    <!-- DISCORD LIVE NOTIFICATION & COMMUNITY BOT ENGINE -->
    <div class="bg-gradient-to-br from-[#5865F2]/10 via-white to-amber-500/5 p-6 sm:p-7 rounded-3xl border border-[#5865F2]/30 shadow-sm space-y-5">
        <div class="flex flex-col sm:flex-row justify-between sm:items-center gap-4 pb-4 border-b border-stone-200">
            <div class="flex items-center space-x-3.5">
                <div class="w-12 h-12 rounded-2xl bg-[#5865F2] text-white flex items-center justify-center text-2xl shadow-md">
                    <i class="fa-brands fa-discord"></i>
                </div>
                <div>
                    <div class="inline-flex items-center space-x-1.5 px-2.5 py-0.5 rounded-full bg-[#5865F2]/15 text-[#5865F2] text-[10px] font-black uppercase tracking-wider mb-0.5">
                        <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                        <span>DISCORD BOT & WEBHOOK REAL-TIME LINK</span>
                    </div>
                    <h3 class="text-lg font-black text-stone-900">디스코드 주문 관제 & 공식 커뮤니티 연동</h3>
                </div>
            </div>
            <div class="flex items-center gap-2">
                <a href="{{ settings.get('discord_invite_url', 'https://discord.gg/Kym2WKGDX') }}" target="_blank"
                   class="px-4 py-2.5 bg-[#5865F2] hover:bg-[#4752c4] text-white text-xs font-black rounded-xl transition shadow flex items-center gap-2">
                    <i class="fa-brands fa-discord text-sm"></i>
                    <span>디스코드 서버 입장하기</span>
                    <i class="fa-solid fa-arrow-up-right-from-square text-[10px]"></i>
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
            <!-- Left: Community Invite Info -->
            <div class="p-4 rounded-2xl bg-white border border-stone-200 space-y-3">
                <div class="flex justify-between items-center">
                    <span class="text-xs font-black text-stone-900 flex items-center gap-1.5">
                        <i class="fa-solid fa-link text-[#5865F2]"></i> 공식 디스코드 초대 링크
                    </span>
                    <span class="text-[10px] px-2 py-0.5 bg-emerald-100 text-emerald-800 rounded-full font-bold">공식 채널 연결됨</span>
                </div>
                <div class="flex items-center gap-2">
                    <input type="text" readonly value="{{ settings.get('discord_invite_url', 'https://discord.gg/Kym2WKGDX') }}" id="discordInviteInput"
                           class="w-full px-3.5 py-2 text-xs font-mono bg-stone-50 border border-stone-200 rounded-xl text-stone-800 focus:outline-none select-all font-bold">
                    <button onclick="copyDiscordInvite()" class="px-3.5 py-2 bg-stone-900 hover:bg-black text-white text-xs font-bold rounded-xl whitespace-nowrap transition flex items-center gap-1">
                        <i class="fa-regular fa-copy text-amber-400"></i>
                        <span>복사</span>
                    </button>
                </div>
                <p class="text-[11px] text-stone-500 leading-relaxed">
                    FRUIT FARM 푸꾸옥 플래그십 공식 디스코드 서버 초대 링크입니다. 쇼핑몰 하단 푸터에도 방문자용 공식 링크로 자동 연동됩니다.
                </p>
            </div>

            <!-- Right: Webhook Trigger & Test -->
            <div class="p-4 rounded-2xl bg-white border border-stone-200 space-y-3">
                <div class="flex justify-between items-center">
                    <span class="text-xs font-black text-stone-900 flex items-center gap-1.5">
                        <i class="fa-solid fa-bolt text-amber-500"></i> 실시간 주문 알림 웹훅 (Webhook)
                    </span>
                    <span class="text-[10px] text-stone-500 font-mono">Real-time Push</span>
                </div>
                <div class="space-y-2">
                    <div class="flex items-center gap-2">
                        <input type="text" id="discordWebhookInput" placeholder="https://discord.com/api/webhooks/..."
                               value="{{ settings.get('discord_webhook_url', '') }}"
                               class="w-full px-3.5 py-2 text-xs font-mono bg-stone-50 border border-stone-200 rounded-xl text-stone-800 focus:ring-2 focus:ring-amber-500 focus:outline-none">
                        <button onclick="saveDiscordWebhook()" class="px-3.5 py-2 bg-amber-500 hover:bg-amber-600 text-stone-950 text-xs font-black rounded-xl whitespace-nowrap transition shadow-sm">
                            웹훅 저장
                        </button>
                    </div>
                    <div class="flex items-center justify-between pt-1">
                        <span class="text-[11px] text-stone-400">신규 주문 및 라이더 배차 시 디스코드 채널로 즉시 임베드 알림 전송</span>
                        <button onclick="testDiscordWebhook()" id="btnTestDiscord" class="px-3 py-1.5 bg-[#5865F2]/10 hover:bg-[#5865F2]/20 text-[#5865F2] text-xs font-black rounded-lg transition flex items-center gap-1 border border-[#5865F2]/30">
                            <i class="fa-solid fa-paper-plane text-xs"></i>
                            <span>테스트 전송</span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
'''

discord_js = '''
function copyDiscordInvite() {
    const inviteInput = document.getElementById('discordInviteInput');
    navigator.clipboard.writeText(inviteInput.value).then(() => {
        alert('디스코드 공식 초대 링크가 복사되었습니다:\n' + inviteInput.value);
    });
}

function saveDiscordWebhook() {
    const webhookUrl = document.getElementById('discordWebhookInput').value.trim();
    const formData = new FormData();
    formData.append('webhook_url', webhookUrl);
    
    fetch('/api/admin/discord/save-webhook', {
        method: 'POST',
        body: formData
    })
    .then(r => r.json())
    .then(data => {
        alert(data.message);
    })
    .catch(err => {
        alert('저장 중 오류가 발생했습니다: ' + err);
    });
}

function testDiscordWebhook() {
    const btn = document.getElementById('btnTestDiscord');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin text-xs"></i> <span>전송 중...</span>';

    fetch('/api/admin/discord/test', {
        method: 'POST'
    })
    .then(r => r.json())
    .then(data => {
        alert(data.message);
    })
    .catch(err => {
        alert('테스트 전송 통신 오류: ' + err);
    })
    .finally(() => {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa-solid fa-paper-plane text-xs"></i> <span>테스트 전송</span>';
    });
}
'''

if 'DISCORD LIVE NOTIFICATION' not in content:
    # Insert right after the header banner
    target = '<!-- 1. KAKAOTALK LIVE LOCATION LINK GENERATOR FOR RECENT ORDERS -->'
    if target in content:
        content = content.replace(target, discord_card_html + "\n\n    " + target)

    # Insert JS functions before </script>
    if '</script>' in content:
        content = content.replace('</script>', discord_js + "\n</script>")

    with open(r'E:\fruitfarm\templates\admin\marketing.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added Discord card and functions to marketing.html")
else:
    print("Discord card already in marketing.html")
