with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix Hero padding
text = text.replace(
    'py-20 text-center sm:text-left flex flex-col lg:flex-row items-center justify-between gap-12',
    'pt-28 sm:pt-36 pb-20 text-center sm:text-left flex flex-col lg:flex-row items-center justify-between gap-12'
)

# 2. Fix Hero Card Concierge button -> Clean Customer Service text
old_hero_ai = '''            <!-- AI 24h Concierge Replacement (Zero Customer Service Burden) -->
            <div class="pt-3.5 border-t border-stone-200 flex justify-between items-center text-xs">
                <span class="text-stone-500 font-bold flex items-center gap-1.5">
                    <i class="fa-solid fa-headset text-amber-600"></i>
                    <span>24시간 고객지원:</span>
                </span>
                <button onclick="openAIChatbot()" style="color: #FFFFFF !important;" class="btn-keep-white bg-black hover:bg-stone-900 text-white font-black px-3.5 py-2 rounded-xl text-xs flex items-center space-x-1.5 transition shadow-md border border-amber-400/50">
                    <i class="fa-solid fa-robot text-amber-400"></i>
                    <span>AI 24시 즉시상담 (통관·배송)</span>
                </button>
            </div>'''

new_hero_ai = '''            <!-- 24h Customer Support Reassurance -->
            <div class="pt-3.5 border-t border-stone-200 flex justify-between items-center text-xs">
                <span class="text-stone-500 font-bold flex items-center gap-1.5">
                    <i class="fa-solid fa-headset text-amber-500"></i>
                    <span>고객지원:</span>
                </span>
                <span class="inline-flex items-center gap-1.5 text-stone-900 font-black">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span>카카오톡 24시간 실시간 상담 운영</span>
                </span>
            </div>'''

if old_hero_ai in text:
    text = text.replace(old_hero_ai, new_hero_ai)
    print('Hero card customer service simplified!')
else:
    print('old_hero_ai exact match not found, looking for openAIChatbot in hero...')
    start = text.find('<!-- AI 24h Concierge Replacement')
    if start != -1:
        end = text.find('</div>\n        </div>\n    </div>', start)
        text = text[:start] + new_hero_ai + '\n        </div>\n    </div>' + text[end+30:]
        print('Hero card replaced by slice!')

# 3. Remove duplicate announcement banner under hero
dup_banner = '''<!-- Top Brand Value Notification Strip (Clean & Non-Intrusive) -->
<div class="bg-amber-100/90 border-b border-amber-300/60 py-2.5 px-4 text-center text-xs font-black text-amber-900">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-2">
        <i class="fa-solid fa-plane-departure text-amber-600"></i>
        <span>$100 이상 주문 시 한국 자택 100% 무료 항공 직배송 (15kg 수하물 오버차지 ZERO 면세 보증)</span>
    </div>
</div>'''

if dup_banner in text:
    text = text.replace(dup_banner, '')
    print('Removed duplicate announcement banner under hero!')
else:
    print('dup_banner not found')

# 4. Update Showroom Gallery Cards
old_gallery_cards = '''            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="luxury-card rounded-2xl overflow-hidden group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_exterior.png" alt="소나시 12가 매장 외관" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span class="absolute bottom-2.5 left-2.5 bg-dark-900/80 backdrop-blur-md text-white text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">
                            소나시 12가 단독 매장
                        </span>
                    </div>
                    <div class="p-3.5">
                        <div class="font-bold text-xs text-white">푸꾸옥 2호점 단독 플래그십</div>
                        <div class="text-[11px] text-slate-400 mt-0.5">SV2A-V07 Sonasea Bãi Trường</div>
                    </div>
                </div>

                <div class="luxury-card rounded-2xl overflow-hidden group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_interior_tasting.jpg" alt="청결한 위생 시식대 & 진열대" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span class="absolute bottom-2.5 left-2.5 bg-dark-900/80 backdrop-blur-md text-gold-300 text-[10px] font-bold px-2 py-0.5 rounded border border-gold-500/40">
                            무료 시식 바 & 우드 진열장
                        </span>
                    </div>
                    <div class="p-3.5">
                        <div class="font-bold text-xs text-white">청결한 위생 시식 테이블</div>
                        <div class="text-[11px] text-slate-400 mt-0.5">망고, 용안, 용과 선물용 무제한 맛보기</div>
                    </div>
                </div>

                <div class="luxury-card rounded-2xl overflow-hidden group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_shelves_promo.jpg" alt="10+2 / 5+1 기획세트 진열대" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span class="absolute bottom-2.5 left-2.5 bg-dark-900/80 backdrop-blur-md text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-emerald-500/40">
                            10+2 / 5+1 기획 진열
                        </span>
                    </div>
                    <div class="p-3.5">
                        <div class="font-bold text-xs text-white">현장 정찰제 공식 프로모션</div>
                        <div class="text-[11px] text-slate-400 mt-0.5">매장과 온라인 완전 동일한 투명 가격</div>
                    </div>
                </div>

                <div class="luxury-card rounded-2xl overflow-hidden group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_window_display.jpg" alt="매장 전경 & 디스플레이" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span class="absolute bottom-2.5 left-2.5 bg-dark-900/80 backdrop-blur-md text-white text-[10px] font-bold px-2 py-0.5 rounded border border-slate-700">
                            쾌적한 원목 쇼핑
                        </span>
                    </div>
                    <div class="p-3.5">
                        <div class="font-bold text-xs text-white">쾌적한 원목 쇼핑 공간</div>
                        <div class="text-[11px] text-slate-400 mt-0.5">에어컨 완비, 캐리어 무료 보관 서비스</div>
                    </div>
                </div>
            </div>'''

new_gallery_cards = '''            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-white rounded-2xl overflow-hidden border border-stone-200 shadow-sm group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_exterior.png" alt="소나시 12가 매장 외관" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span style="color: #FFFFFF !important; background-color: rgba(17, 24, 39, 0.88) !important;" class="absolute bottom-2.5 left-2.5 text-xs font-bold px-2.5 py-1 rounded-lg border border-amber-400/50 shadow-md">
                            소나시 12가 단독 매장
                        </span>
                    </div>
                    <div class="p-4 bg-white">
                        <div class="font-black text-sm text-stone-900">푸꾸옥 2호점 단독 플래그십</div>
                        <div class="text-xs text-stone-500 mt-1">SV2A-V07 Sonasea Bãi Trường</div>
                    </div>
                </div>

                <div class="bg-white rounded-2xl overflow-hidden border border-stone-200 shadow-sm group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_interior_tasting.jpg" alt="청결한 위생 시식대 & 진열대" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span style="color: #FFFFFF !important; background-color: rgba(17, 24, 39, 0.88) !important;" class="absolute bottom-2.5 left-2.5 text-xs font-bold px-2.5 py-1 rounded-lg border border-amber-400/50 shadow-md">
                            무료 시식 바 & 우드 진열장
                        </span>
                    </div>
                    <div class="p-4 bg-white">
                        <div class="font-black text-sm text-stone-900">청결한 위생 시식 테이블</div>
                        <div class="text-xs text-stone-500 mt-1">망고, 용안, 용과 선물용 무제한 맛보기</div>
                    </div>
                </div>

                <div class="bg-white rounded-2xl overflow-hidden border border-stone-200 shadow-sm group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_shelves_promo.jpg" alt="10+2 / 5+1 기획세트 진열대" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span style="color: #FFFFFF !important; background-color: rgba(17, 24, 39, 0.88) !important;" class="absolute bottom-2.5 left-2.5 text-xs font-bold px-2.5 py-1 rounded-lg border border-amber-400/50 shadow-md">
                            10+2 / 5+1 기획 진열
                        </span>
                    </div>
                    <div class="p-4 bg-white">
                        <div class="font-black text-sm text-stone-900">현장 정찰제 공식 프로모션</div>
                        <div class="text-xs text-stone-500 mt-1">매장과 온라인 완전 동일한 투명 가격</div>
                    </div>
                </div>

                <div class="bg-white rounded-2xl overflow-hidden border border-stone-200 shadow-sm group">
                    <div class="h-56 overflow-hidden relative">
                        <img src="/static/images/store/store_window_display.jpg" alt="매장 전경 & 디스플레이" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <span style="color: #FFFFFF !important; background-color: rgba(17, 24, 39, 0.88) !important;" class="absolute bottom-2.5 left-2.5 text-xs font-bold px-2.5 py-1 rounded-lg border border-amber-400/50 shadow-md">
                            쾌적한 원목 쇼핑 공간
                        </span>
                    </div>
                    <div class="p-4 bg-white">
                        <div class="font-black text-sm text-stone-900">쾌적한 원목 쇼핑 공간</div>
                        <div class="text-xs text-stone-500 mt-1">에어컨 완비, 캐리어 무료 보관 서비스</div>
                    </div>
                </div>
            </div>'''

# Replace gallery cards using markers
g_start = text.find('<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">')
if g_start != -1:
    g_end = text.find('</div>\n        </div>\n    </section>', g_start)
    if g_end != -1:
        text = text[:g_start] + new_gallery_cards + text[g_end:]
        print('Showroom gallery cards updated with high contrast readable badges!')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
