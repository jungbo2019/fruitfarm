# -*- coding: utf-8 -*-

# 1. Update templates/index.html Hero Quick Card contact line
with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')

old_contact_block = '''            <div class="pt-3 border-t border-gold-500/20 flex justify-between items-center text-[11px]">
                <span class="text-slate-400">매장 고객센터:</span>
                <span class="font-mono font-black text-stone-900 bg-amber-200/80 px-2.5 py-1 rounded-md text-xs sm:text-sm border border-amber-300">{{ settings.get('store_phone', '+84 386 074 755') }}</span>
            </div>'''

new_contact_block = '''            <!-- AI 24h Concierge Replacement (Zero Customer Service Burden) -->
            <div class="pt-3.5 border-t border-stone-200 flex justify-between items-center text-xs">
                <span class="text-stone-500 font-bold flex items-center gap-1.5">
                    <i class="fa-solid fa-headset text-amber-600"></i>
                    <span>24시간 고객지원:</span>
                </span>
                <button onclick="openAIChatbot()" class="bg-stone-950 hover:bg-black text-white font-black px-3.5 py-1.5 rounded-xl transition shadow-md border border-amber-400 flex items-center gap-1.5 text-xs">
                    <i class="fa-solid fa-robot text-amber-400"></i>
                    <span>AI 24시 즉시상담 (통관·배송)</span>
                </button>
            </div>'''

if old_contact_block in text:
    text = text.replace(old_contact_block, new_contact_block)
    print("Updated Hero contact line to AI Concierge button!")
else:
    print("Warning: old_contact_block not found directly")

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Add AI Chatbot Modal & Floating Widget to templates/base.html
with open('E:/fruitfarm/templates/base.html', 'r', encoding='utf-8') as f:
    base_text = f.read()

base_text = base_text.replace('\r\n', '\n')

ai_chatbot_markup = '''
    <!-- ==================== 24/7 AI SMART CONCIERGE CHATBOT MODAL ==================== -->
    <div id="aiChatModal" class="fixed inset-0 z-50 hidden bg-black/60 backdrop-blur-xs flex items-end sm:items-center justify-end sm:justify-end sm:p-6 p-2">
        <div class="bg-white rounded-3xl w-full sm:max-w-md h-[550px] shadow-2xl border border-stone-200 flex flex-col overflow-hidden animate-in fade-in slide-in-from-bottom-6 duration-300">
            <!-- Chatbot Header -->
            <div class="bg-stone-950 text-white p-4 flex items-center justify-between border-b border-stone-800">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-2xl bg-amber-500 flex items-center justify-center text-stone-950 text-lg font-black shadow-md shadow-amber-500/20">
                        <i class="fa-solid fa-robot"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h3 class="font-black text-sm text-white">FRUIT FARM AI 컨시어지</h3>
                            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        </div>
                        <p class="text-[10px] text-stone-400">24시간 무인 자동상담 (업무부담 ZERO)</p>
                    </div>
                </div>
                <button onclick="closeAIChatbot()" class="text-stone-400 hover:text-white p-2">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>
            </div>

            <!-- Chat Messages Container -->
            <div id="aiChatBody" class="flex-grow p-4 overflow-y-auto space-y-3.5 text-xs bg-stone-50">
                <!-- Bot Welcome Message -->
                <div class="flex items-start space-x-2.5">
                    <div class="w-7 h-7 rounded-lg bg-amber-500 text-stone-950 flex items-center justify-center flex-shrink-0 text-xs font-black">
                        AI
                    </div>
                    <div class="bg-white p-3 rounded-2xl rounded-tl-none border border-stone-200 text-stone-800 shadow-xs max-w-[85%] space-y-2 leading-relaxed">
                        <p>안녕하세요! <strong>FRUIT FARM 푸꾸옥 2호점 24시 AI 상담원</strong>입니다. 🥭</p>
                        <p>배송, 통관, 리조트 퀵배달 등 궁금하신 점을 아래 버튼을 누르시거나 직접 물어보세요!</p>
                    </div>
                </div>

                <!-- Quick FAQ Chips -->
                <div class="pt-1 space-y-1.5">
                    <span class="text-[10px] font-black text-stone-400 uppercase tracking-wider block">자주 묻는 질문 원클릭 답변:</span>
                    <div class="flex flex-wrap gap-1.5">
                        <button onclick="askAIQuestion('한국 직배송 며칠 걸려요?')" class="px-2.5 py-1 bg-white hover:bg-amber-50 text-stone-700 hover:text-amber-900 border border-stone-200 rounded-lg text-[11px] font-bold transition shadow-xs">
                            ✈️ 한국 배송 소요기간
                        </button>
                        <button onclick="askAIQuestion('리조트 로비 배달은 언제 오나요?')" class="px-2.5 py-1 bg-white hover:bg-amber-50 text-stone-700 hover:text-amber-900 border border-stone-200 rounded-lg text-[11px] font-bold transition shadow-xs">
                            🛵 푸꾸옥 리조트 당일 배달
                        </button>
                        <button onclick="askAIQuestion('10+2 세트는 어떻게 골라담나요?')" class="px-2.5 py-1 bg-white hover:bg-amber-50 text-stone-700 hover:text-amber-900 border border-stone-200 rounded-lg text-[11px] font-bold transition shadow-xs">
                            🎁 10+2 골라담기 혜택
                        </button>
                        <button onclick="askAIQuestion('개인통관고유부호가 없어요')" class="px-2.5 py-1 bg-white hover:bg-amber-50 text-stone-700 hover:text-amber-900 border border-stone-200 rounded-lg text-[11px] font-bold transition shadow-xs">
                            🛂 통관부호 발급 방법
                        </button>
                        <button onclick="askAIQuestion('설탕이나 첨가물이 들어가나요?')" class="px-2.5 py-1 bg-white hover:bg-amber-50 text-stone-700 hover:text-amber-900 border border-stone-200 rounded-lg text-[11px] font-bold transition shadow-xs">
                            🥭 무설탕 저온건조 품질
                        </button>
                    </div>
                </div>
            </div>

            <!-- Chat Input Form -->
            <form id="aiChatForm" onsubmit="handleAIChatSubmit(event)" class="p-3 bg-white border-t border-stone-200 flex items-center gap-2">
                <input type="text" id="aiChatInput" placeholder="질문을 입력하세요 (예: 배송비, 리조트 배달...)" required
                       class="flex-grow p-2.5 bg-stone-100 border border-stone-300 rounded-xl text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                <button type="submit" class="px-4 py-2.5 bg-amber-500 hover:bg-amber-600 text-stone-950 font-black rounded-xl text-xs transition shadow-sm flex items-center gap-1">
                    <span>전송</span>
                    <i class="fa-solid fa-paper-plane text-xs"></i>
                </button>
            </form>
        </div>
    </div>

    <!-- Floating AI Concierge Button (Bottom Right) -->
    <button onclick="openAIChatbot()" id="aiFloatingBtn"
            class="fixed bottom-6 right-6 z-40 bg-stone-950 hover:bg-black text-white px-4 py-3 rounded-full shadow-2xl border-2 border-amber-400 flex items-center gap-2.5 font-black text-xs transition transform hover:scale-105">
        <div class="relative">
            <i class="fa-solid fa-robot text-amber-400 text-base"></i>
            <span class="absolute -top-1 -right-1 w-2.5 h-2.5 bg-amber-500 rounded-full animate-ping"></span>
        </div>
        <span>AI 24시 즉시상담</span>
    </button>

    <script>
    function openAIChatbot() {
        document.getElementById('aiChatModal').classList.remove('hidden');
        document.getElementById('aiFloatingBtn').classList.add('hidden');
        document.getElementById('aiChatInput').focus();
    }

    function closeAIChatbot() {
        document.getElementById('aiChatModal').classList.add('hidden');
        document.getElementById('aiFloatingBtn').classList.remove('hidden');
    }

    function askAIQuestion(q) {
        document.getElementById('aiChatInput').value = q;
        handleAIChatSubmit(new Event('submit'));
    }

    function handleAIChatSubmit(e) {
        e.preventDefault();
        const input = document.getElementById('aiChatInput');
        const q = input.value.trim();
        if (!q) return;

        const body = document.getElementById('aiChatBody');

        // Append user question
        const userDiv = document.createElement('div');
        userDiv.className = 'flex items-start justify-end space-x-2';
        userDiv.innerHTML = `
            <div class="bg-amber-500 text-stone-950 font-bold p-3 rounded-2xl rounded-tr-none text-xs max-w-[85%] shadow-xs leading-relaxed">
                ${q}
            </div>
        `;
        body.appendChild(userDiv);
        input.value = '';
        body.scrollTop = body.scrollHeight;

        // Simulate typing and AI response
        setTimeout(() => {
            const answer = generateAIAnswer(q);
            const botDiv = document.createElement('div');
            botDiv.className = 'flex items-start space-x-2.5';
            botDiv.innerHTML = `
                <div class="w-7 h-7 rounded-lg bg-amber-500 text-stone-950 flex items-center justify-center flex-shrink-0 text-xs font-black">
                    AI
                </div>
                <div class="bg-white p-3 rounded-2xl rounded-tl-none border border-stone-200 text-stone-800 shadow-xs max-w-[85%] space-y-2 leading-relaxed">
                    ${answer}
                </div>
            `;
            body.appendChild(botDiv);
            body.scrollTop = body.scrollHeight;
        }, 500);
    }

    function generateAIAnswer(q) {
        const query = q.toLowerCase();
        if (query.includes('한국') || query.includes('직배송') || query.includes('택배') || query.includes('소요') || query.includes('며칠')) {
            return `
                <p><strong>✈️ 한국 무료 항공 직배송 안내</strong></p>
                <p>• <strong>배송 기간</strong>: 결제 완료 후 <strong>3~5일 이내</strong> 한국 자택 문 앞까지 안전 배송됩니다.</p>
                <p>• <strong>무료배송 혜택</strong>: $100 이상 주문 시 배송비 전액 무료 (LCC 15kg 수하물 오버차지 6만원 절약!)</p>
                <p>• <strong>우체국 택배</strong>와 연동되어 국내 송장번호가 발급됩니다.</p>
            `;
        } else if (query.includes('리조트') || query.includes('호텔') || query.includes('로비') || query.includes('당일') || query.includes('시간')) {
            return `
                <p><strong>🛵 푸꾸옥 전지역 리조트 로비 2시간 당일 배달</strong></p>
                <p>• <strong>대상 리조트</strong>: 노보텔, 인터컨티넨탈, 풀만, 리젠트, 세일링클럽, 빈펄 등 푸꾸옥 전지역 리조트 로비 정문</p>
                <p>• <strong>배달 시간</strong>: 주문 후 <strong>당일 2시간 이내</strong> 그랩 퀵 라이더가 신속 전달합니다.</p>
                <p>• <strong>운영 시간</strong>: 매일 09:00 ~ 22:00 (연중무휴)</p>
            `;
        } else if (query.includes('10+2') || query.includes('골라담기') || query.includes('프로모션') || query.includes('세트')) {
            return `
                <p><strong>🎁 10+2 내맘대로 골라담기 패키지 안내</strong></p>
                <p>• 180g 말린과일 및 견과류 중 원하시는 품목 10봉을 자유롭게 선택하시면, 가장 인기 있는 <strong>골드망고 2봉을 무료로 증정</strong>하여 총 12봉을 안전 포장 박스에 담아 보내드립니다!</p>
                <p><a href="#custom-builder" onclick="closeAIChatbot()" class="inline-block mt-1 px-3 py-1 bg-amber-500 text-stone-950 font-black rounded-lg text-[11px]">👉 10+2 직접 담으러 가기</a></p>
            `;
        } else if (query.includes('통관') || query.includes('부호') || query.includes('유니패스') || query.includes('관세')) {
            return `
                <p><strong>🛂 개인통관고유부호(P부호) 안내</strong></p>
                <p>• 대한민국 관세청 <strong>1인당 $150 소액면세 규정</strong>을 엄격히 준수하여 관부가세 0원으로 무사통관됩니다.</p>
                <p>• 통관부호가 없으신 경우, 관세청 유니패스에서 휴대폰 인증으로 <strong>1분 만에 무료 발급</strong>받으실 수 있습니다.</p>
                <p><a href="https://unipass.customs.go.kr" target="_blank" class="inline-block mt-1 px-3 py-1 bg-stone-900 text-white font-bold rounded-lg text-[11px]">🔗 관세청 유니패스 바로가기</a></p>
            `;
        } else if (query.includes('설탕') || query.includes('품질') || query.includes('haccp') || query.includes('방부제') || query.includes('원산지')) {
            return `
                <p><strong>🥭 100% 무설탕 저온건조 & HACCP 직영공장 품질</strong></p>
                <p>• 설탕 시럽에 절인 저가 로컬 야시장 제품과 달리, <strong>설탕 0% · 방부제 0%</strong>로 과육 자체의 깊은 천연 단맛만을 담았습니다.</p>
                <p>• 호치민 직영 HACCP 인증 위생 공장에서 45℃ 저온 건조(Low-temperature Dehydration)하여 쫀득하고 신선합니다.</p>
            `;
        } else {
            return `
                <p>질문해 주신 내용에 대해 확인했습니다.</p>
                <p>• <strong>한국 무료 직배송</strong>: $100 이상 결제 시 3~5일 내 무료 직배송</p>
                <p>• <strong>푸꾸옥 리조트 배달</strong>: 당일 2시간 내 로비 그랩 퀵 배송</p>
                <p class="pt-1">혹시 개별 맞춤 상담이 필요하시면 아래 1:1 카카오톡 채널로 문의해 주시면 매장 직원이 즉시 안내해 드립니다.</p>
                <p><a href="https://pf.kakao.com" target="_blank" class="inline-block mt-1 px-3 py-1 bg-[#FEE500] text-black font-black rounded-lg text-[11px]"><i class="fa-solid fa-comment mr-1"></i>카카오톡 1:1 매장 상담</a></p>
            `;
        }
    }
    </script>
'''

if '<!-- ==================== 24/7 AI SMART CONCIERGE CHATBOT MODAL ==================== -->' not in base_text:
    base_text = base_text.replace('</body>', ai_chatbot_markup + '\n</body>')
    print("Injected AI Smart Concierge Chatbot & Floating Widget into base.html!")

with open('E:/fruitfarm/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_text)

print("All AI updates completed successfully!")
