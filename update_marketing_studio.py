with open(r'E:\fruitfarm\templates\admin\marketing.html', 'r', encoding='utf-8') as f:
    content = f.read()

generator_html = '''
    <!-- INTERACTIVE SNS VIRAL STUDIO PROGRAM (상황별 원클릭 SNS 홍보 자동 생성 프로그램) -->
    <div class="bg-white p-6 sm:p-7 rounded-3xl border border-stone-200 shadow-sm space-y-6">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 pb-4 border-b border-stone-100">
            <div>
                <div class="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-amber-100 text-amber-900 text-xs font-black uppercase tracking-wider mb-1">
                    <i class="fa-solid fa-wand-magic-sparkles text-amber-600"></i>
                    <span>INTERACTIVE VIRAL COPYWRITING STUDIO</span>
                </div>
                <h3 class="text-xl font-black text-stone-900">상황별 SNS 바이럴 마케팅 자동화 프로그램</h3>
                <p class="text-xs text-stone-500 mt-0.5">홍보 채널과 상황을 선택하면 즉시 최적화된 마케팅 문구와 해시태그가 자동 생성됩니다.</p>
            </div>
            <span class="text-xs font-bold text-stone-600 bg-stone-100 px-3 py-1.5 rounded-xl border border-stone-200">
                <i class="fa-solid fa-bolt text-amber-500 mr-1"></i>실시간 자동 생성기 가동
            </span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <!-- Left Controls: Channel & Scenario Selection -->
            <div class="lg:col-span-5 space-y-4 text-xs">
                <div>
                    <label class="block font-black text-stone-800 mb-1.5">1. 홍보 채널 선택</label>
                    <div class="grid grid-cols-2 gap-2">
                        <button type="button" onclick="selectChannel('instagram', this)" class="channel-btn p-3 rounded-2xl border-2 border-amber-500 bg-amber-50/50 font-black text-stone-900 text-left transition flex items-center gap-2">
                            <i class="fa-brands fa-instagram text-base text-pink-600"></i>
                            <span>인스타그램 피드/릴스</span>
                        </button>
                        <button type="button" onclick="selectChannel('naver', this)" class="channel-btn p-3 rounded-2xl border border-stone-200 bg-white font-bold text-stone-700 text-left hover:border-amber-400 transition flex items-center gap-2">
                            <span class="w-5 h-5 rounded-full bg-emerald-500 text-white flex items-center justify-center font-black text-[10px]">N</span>
                            <span>네이버 카페 (푸꿕고스트)</span>
                        </button>
                        <button type="button" onclick="selectChannel('dm', this)" class="channel-btn p-3 rounded-2xl border border-stone-200 bg-white font-bold text-stone-700 text-left hover:border-amber-400 transition flex items-center gap-2">
                            <i class="fa-solid fa-paper-plane text-amber-600"></i>
                            <span>인플루언서 협찬 제안 DM</span>
                        </button>
                        <button type="button" onclick="selectChannel('discord', this)" class="channel-btn p-3 rounded-2xl border border-stone-200 bg-white font-bold text-stone-700 text-left hover:border-amber-400 transition flex items-center gap-2">
                            <i class="fa-brands fa-discord text-base text-[#5865F2]"></i>
                            <span>디스코드/카톡 번개 공지</span>
                        </button>
                    </div>
                </div>

                <div>
                    <label class="block font-black text-stone-800 mb-1.5">2. 타겟 고객 및 프로모션 상황 선택</label>
                    <select id="scenarioSelect" onchange="generateViralCopy()" class="w-full p-3 border rounded-2xl font-bold text-stone-900 bg-stone-50 focus:outline-none focus:ring-2 focus:ring-amber-500 text-xs">
                        <option value="scenario_luggage" selected>[상황 A] 귀국 전 LCC 항공 15kg 수하물 무게 걱정 해소 ($100 한국 무료 직배송)</option>
                        <option value="scenario_sugarfree">[상황 B] 즈엉동 야시장 설탕 절임 망고 vs 소나시 100% 무설탕 골드망고 리얼 비교</option>
                        <option value="scenario_resort">[상황 C] 호텔에서 쉬면서 즐기는 푸꾸옥 전지역 2시간 당일 퀵 배달</option>
                        <option value="scenario_gift102">[상황 D] 여행 선물 종결! 10+2 골라담기 기획 선물 세트 한정 특가</option>
                    </select>
                </div>

                <div class="p-4 rounded-2xl bg-amber-50/70 border border-amber-200 space-y-1.5 text-[11px] text-amber-900">
                    <span class="font-black flex items-center gap-1.5"><i class="fa-solid fa-lightbulb text-amber-600"></i> 마케팅 꿀팁</span>
                    <p class="leading-relaxed">
                        여행 마지막 날 체크아웃 전 고객에게 "캐리어에 넣지 말고 한국 집으로 무료 직배송 받으세요" 메시지를 노출하면 전환율이 가장 높습니다.
                    </p>
                </div>
            </div>

            <!-- Right: Real-time Live Generated Content Preview -->
            <div class="lg:col-span-7 flex flex-col justify-between space-y-3">
                <div class="flex justify-between items-center">
                    <span class="text-xs font-black text-stone-800 flex items-center gap-1.5">
                        <i class="fa-solid fa-sparkles text-amber-500"></i> 생성된 바이럴 텍스트 프리뷰
                    </span>
                    <span id="previewTag" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-pink-100 text-pink-700">인스타그램 최적화</span>
                </div>

                <textarea id="viralOutput" rows="11" readonly class="w-full p-4 rounded-2xl border border-stone-200 bg-stone-50 font-sans text-xs text-stone-800 leading-relaxed focus:outline-none focus:bg-white transition"></textarea>

                <div class="flex items-center gap-2 pt-1">
                    <button onclick="copyGeneratedViralCopy()" class="flex-grow py-3 bg-stone-950 hover:bg-black text-white text-xs font-black rounded-xl transition shadow flex items-center justify-center gap-2">
                        <i class="fa-regular fa-copy text-amber-400"></i>
                        <span>홍보 문구 클립보드 원클릭 복사</span>
                    </button>
                    <button onclick="shareDirectlyToDiscord()" class="px-4 py-3 bg-[#5865F2] hover:bg-[#4752c4] text-white text-xs font-black rounded-xl transition flex items-center gap-1.5">
                        <i class="fa-brands fa-discord"></i>
                        <span>디스코드 공유</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
'''

studio_js = '''
let currentChannel = 'instagram';

function selectChannel(channel, btn) {
    currentChannel = channel;
    document.querySelectorAll('.channel-btn').forEach(b => {
        b.classList.remove('border-amber-500', 'bg-amber-50/50', 'font-black');
        b.classList.add('border-stone-200', 'bg-white', 'font-bold');
    });
    btn.classList.remove('border-stone-200', 'bg-white', 'font-bold');
    btn.classList.add('border-amber-500', 'bg-amber-50/50', 'font-black');

    const previewTag = document.getElementById('previewTag');
    if (channel === 'instagram') {
        previewTag.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-pink-100 text-pink-700';
        previewTag.innerText = '인스타그램 최적화';
    } else if (channel === 'naver') {
        previewTag.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800';
        previewTag.innerText = '네이버 카페 후기 최적화';
    } else if (channel === 'dm') {
        previewTag.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800';
        previewTag.innerText = '인플루언서 제안 DM 포맷';
    } else if (channel === 'discord') {
        previewTag.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-[#5865F2]/20 text-[#5865F2]';
        previewTag.innerText = '디스코드/카톡 번개 공지';
    }

    generateViralCopy();
}

function generateViralCopy() {
    const scenario = document.getElementById('scenarioSelect').value;
    const origin = window.location.origin;
    let text = '';

    if (currentChannel === 'instagram') {
        if (scenario === 'scenario_luggage') {
            text = `🥭 푸꾸옥 여행 선물 살 때 캐리어 15kg 수하물 무게 걱정 끝! ✈️\\n\\n베트남 올 때 이미 꽉 찬 캐리어 때문에 건망고 살까 말까 고민하셨죠?\\n소나시 상가 메인에 있는 FRUIT FARM 직영 플래그십은 $100 이상 구매 시 10+2 증정에 한국 집 문 앞까지 무료 직배송해 줍니다! ✨\\n\\n무거운 짐 손으로 들고 공항 갈 필요 없이, 몸만 가볍게 귀국하세요! 🌴\\n\\n📍 위치: 푸꾸옥 소나시 상가 12가 (노보텔 바로 앞)\\n🔗 온라인 바로 주문: ${origin}\\n\\n#푸꾸옥여행 #푸꾸옥후르츠팜 #소나시야시장 #노보텔푸꾸옥 #푸꾸옥쇼핑 #무설탕건망고 #푸꾸옥기념품 #푸꾸옥맛집 #베트남여행선물`;
        } else if (scenario === 'scenario_sugarfree') {
            text = `⚠️ 즈엉동 야시장 설탕 범벅 망고 말고 진짜 100% 무설탕 찾았습니다! 🥭\\n\\n야시장에서 샀던 건망고, 설탕 덩어리에 끈적거려서 실망한 적 있으시죠?\\nFRUIT FARM은 설탕 0% 무첨가 저온건조 특허 기술로 생망고 본연의 쫀득함과 새콤달콤함이 살아있어요! 💛\\n\\n무료 시식 상시 운영 중이니 직접 먹어보고 결정하세요!\\n\\n📍 푸꾸옥 소나시 보행자 거리 FRUIT FARM 직영 플래그십\\n📦 한국 집 무료 직배송: ${origin}\\n\\n#푸꾸옥건망고 #무설탕골드망고 #푸꾸옥선물추천 #소나시맛집 #베트남건망고 #푸꾸옥자유여행`;
        } else if (scenario === 'scenario_resort') {
            text = `🌴 푸꾸옥 리조트 수영장에서 시원하게 건망고 땡길 때? 당일 2시간 퀵 배달! 🛵\\n\\n인터컨, 노보텔, JW메리어트, 풀만 등 푸꾸옥 전지역 리조트 로비로 2시간 안에 신선하게 달려갑니다!\\n밤에 맥주 한잔할 때 안주로 최고인 프리미엄 통캐슈넛 & 소프트 건망고 세트 ✨\\n\\n지금 바로 모바일로 간편 주문하세요!\\n🔗 배달 주문: ${origin}\\n\\n#푸꾸옥리조트 #푸꾸옥호캉스 #푸꾸옥배달 #푸꾸옥야식 #푸꾸옥노보텔 #푸꾸옥인터컨`;
        } else {
            text = `🎁 푸꾸옥 선물 종결! 10+2 골라담기 선물세트 한정 런칭! ✨\\n\\n내가 원하는 과일(무설탕 골드망고, 패션후르츠, 무화과, 통캐슈넛, 통마카다미아) 마음대로 12봉 골라담고 $100에 겟!\\n+ 대한민국 전지역 무료 항공 직배송까지 포함 ✈️\\n\\n직장 동료, 가족, 친구 선물 고민 1분 만에 끝내세요!\\n👉 나만의 세트 만들기: ${origin}\\n\\n#푸꾸옥선물 #푸꾸옥쇼핑리스트 #건망고선물세트 #푸꾸옥플래그십 #FRUITFARM`;
        }
    } else if (currentChannel === 'naver') {
        text = `[푸꾸옥 4박5일] 즈엉동 야시장 말고 소나시 FRUIT FARM 직영점에서 쇼핑 끝낸 내돈내산 후기! 🥭\\n\\n안녕하세요 푸꿕고스트 회원님들!\\n이번에 가족여행 다녀오면서 지인들 귀국 선물 고민이 제일 컸는데, 소나시 상가 12가에 있는 FRUIT FARM 들렀다가 완전 반했습니다.\\n\\n1. 진짜 100% 무설탕이라 설탕 알갱이 씹히는 야시장 망고랑 차원이 다름 (애기들 간식으로 딱)\\n2. $100 사면 10+2로 2봉 더 주고 한국 집으로 무료 직배송해줘서 LCC 15kg 수하물 오버차지 세이브!\\n3. 호텔 로비로 2시간 만에 퀵 배달도 와서 짐 챙길 시간 벌었습니다.\\n\\n푸꾸옥 가시는 분들 꼭 매장 가서 무료 시식 먼저 해보세요 강추합니다!\\n(온라인으로도 주문 가능하더라구요: ${origin})`;
    } else if (currentChannel === 'dm') {
        text = `안녕하세요 작가님! 푸꾸옥의 아름다운 여행 피드 너무 잘 보고 있습니다 🌴\\n\\n저희는 푸꾸옥 소나시 메인 스트리트에 위치한 100% 무설탕 프리미엄 건망고 브랜드 [FRUIT FARM 푸꾸옥 직영 플래그십]입니다.\\n작가님의 감성적인 여행 콘텐츠에 반해, 푸꾸옥 체류 기간 동안 즐기실 수 있는 [FRUIT FARM 시그니처 웰컴 기프트 박스]를 숙소 로비로 선물해 드리고 싶어 연락드렸습니다.\\n\\n한국 귀국 시 무거운 짐 없이 편안하게 받아보실 수 있는 자택 무료 직배송권도 함께 포함되어 있습니다.\\n선물 수령을 희망하시는 호텔명과 체크인 일정을 편하게 답장 주시면 정성껏 준비하겠습니다. 즐거운 푸꾸옥 여행 되세요! ✨\\n\\nFRUIT FARM 드림\\n브랜드 안내: ${origin}`;
    } else if (currentChannel === 'discord') {
        text = `📢 [FRUIT FARM 푸꾸옥 플래그십] 오늘 하루 번개 특가 프로모션 공지! ⚡\\n\\n안녕하세요 푸꾸옥 여행자 여러분!\\n오늘 소나시 직영 매장 및 온라인 주문 고객님께 [10+2 골라담기 패키지] 구매 시 시그니처 패션후르츠 1봉을 추가 증정합니다!\\n\\n✔️ 100% 무설탕 저온건조 보증\\n✔️ 푸꾸옥 전지역 리조트 당일 2시간 퀵 배달\\n✔️ $100 이상 한국 자택 무료 직배송\\n\\n지금 바로 참여하세요:\\n👉 ${origin}\\n공식 디스코드 커뮤니티: https://discord.gg/Kym2WKGDX`;
    }

    document.getElementById('viralOutput').value = text;
}

function copyGeneratedViralCopy() {
    const copyText = document.getElementById('viralOutput');
    navigator.clipboard.writeText(copyText.value).then(() => {
        alert('선택하신 SNS 최적화 마케팅 문구가 클립보드에 복사되었습니다!\n원하시는 채널에 바로 붙여넣기(Ctrl+V) 하세요.');
    });
}

function shareDirectlyToDiscord() {
    alert('디스코드 공식 커뮤니티 채널로 이동합니다.\n붙여넣기(Ctrl+V)하여 바로 공지하세요!');
    window.open('https://discord.gg/Kym2WKGDX', '_blank');
}

// Auto-run on load
window.addEventListener('DOMContentLoaded', () => {
    generateViralCopy();
});
'''

if 'INTERACTIVE SNS VIRAL STUDIO PROGRAM' not in content:
    target = '    <!-- 1. KAKAOTALK LIVE LOCATION LINK GENERATOR FOR RECENT ORDERS -->'
    if target in content:
        content = content.replace(target, generator_html + "\n\n    " + target)
        if '</script>' in content:
            content = content.replace('</script>', studio_js + "\n</script>")
        with open(r'E:\fruitfarm\templates\admin\marketing.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Injected interactive Viral Studio into marketing.html")
    else:
        print("Target not found in marketing.html")
else:
    print("Already injected into marketing.html")
