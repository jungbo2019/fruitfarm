# -*- coding: utf-8 -*-
with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')

# 1. FIX HERO QUICK VALUE CARD
old_quick_card = '''        <!-- Hero Quick Value Card -->
        <div class="w-full max-w-md luxury-card-gold p-6 sm:p-7 rounded-3xl border border-gold-500/40 relative shadow-2xl backdrop-blur-xl">
            <div class="flex items-center justify-between pb-4 border-b border-gold-500/20">
                <div class="flex items-center space-x-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span class="text-xs font-black text-white uppercase tracking-wider">안심 보증 & 특급 혜택</span>
                </div>
                <span class="text-[10px] text-gold-300 font-bold bg-gold-500/20 px-2 py-0.5 rounded">HACCP 100%</span>
            </div>

            <div class="space-y-4 py-4 text-xs">
                <div class="flex items-start space-x-3">
                    <div class="w-7 h-7 rounded-lg bg-gold-500/20 text-gold-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i class="fa-solid fa-plane-shield"></i>
                    </div>
                    <div>
                        <div class="font-bold text-white">{{ settings.get('text_benefit_1_title', '대한민국 100% 무사통관 보증제') }}</div>
                        <div class="text-[11px] text-slate-400">{{ settings.get('text_benefit_1_desc', '식물검역법 적합 밀봉 가공식품 · 1인당 $150 소액면세 엄격 준수') }}</div>
                    </div>
                </div>

                <div class="flex items-start space-x-3">
                    <div class="w-7 h-7 rounded-lg bg-gold-500/20 text-gold-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i class="fa-solid fa-suitcase-rolling"></i>
                    </div>
                    <div>
                        <div class="font-bold text-white">{{ settings.get('text_benefit_2_title', '수하물 초과운임 ZERO 무료 직배송') }}</div>
                        <div class="text-[11px] text-slate-400">{{ settings.get('text_benefit_2_desc', '$100 이상 구매 시 한국 자택 문 앞까지 3~5일 안전 배송') }}</div>
                    </div>
                </div>

                <div class="flex items-start space-x-3">
                    <div class="w-7 h-7 rounded-lg bg-gold-500/20 text-gold-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i class="fa-solid fa-motorcycle"></i>
                    </div>
                    <div>
                        <div class="font-bold text-white">{{ settings.get('text_benefit_3_title', '푸꾸옥 전지역 리조트 당일 2시간 배달') }}</div>
                        <div class="text-[11px] text-slate-400">{{ settings.get('text_benefit_3_desc', '빈펄, 풀만, 인터컨티넨탈, 노보텔 로비로 그랩 퀵 직배송') }}</div>
                    </div>
                </div>
            </div>'''

new_quick_card = '''        <!-- Hero Quick Value Card -->
        <div class="w-full max-w-md bg-white p-6 sm:p-7 rounded-3xl border-2 border-amber-300 relative shadow-2xl">
            <div class="flex items-center justify-between pb-4 border-b border-stone-200">
                <div class="flex items-center space-x-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-pulse"></span>
                    <span class="text-xs font-black text-stone-900 uppercase tracking-wider">안심 보증 & 특급 혜택</span>
                </div>
                <span class="text-[11px] text-amber-900 font-black bg-amber-100 border border-amber-300 px-2.5 py-0.5 rounded-full">HACCP 100%</span>
            </div>

            <div class="space-y-4 py-4 text-xs">
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center flex-shrink-0 font-black text-sm shadow-xs">
                        <i class="fa-solid fa-plane-shield text-stone-950"></i>
                    </div>
                    <div>
                        <div class="font-black text-stone-900 text-sm leading-tight">{{ settings.get('text_benefit_1_title', '대한민국 100% 무사통관 보증제') }}</div>
                        <div class="text-[11px] text-stone-600 mt-0.5">{{ settings.get('text_benefit_1_desc', '식물검역법 적합 밀봉 가공식품 · 1인당 $150 소액면세 엄격 준수') }}</div>
                    </div>
                </div>

                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center flex-shrink-0 font-black text-sm shadow-xs">
                        <i class="fa-solid fa-suitcase-rolling text-stone-950"></i>
                    </div>
                    <div>
                        <div class="font-black text-stone-900 text-sm leading-tight">{{ settings.get('text_benefit_2_title', '수하물 초과운임 ZERO 무료 직배송') }}</div>
                        <div class="text-[11px] text-stone-600 mt-0.5">{{ settings.get('text_benefit_2_desc', '$100 이상 구매 시 한국 자택 문 앞까지 3~5일 안전 배송') }}</div>
                    </div>
                </div>

                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center flex-shrink-0 font-black text-sm shadow-xs">
                        <i class="fa-solid fa-motorcycle text-stone-950"></i>
                    </div>
                    <div>
                        <div class="font-black text-stone-900 text-sm leading-tight">{{ settings.get('text_benefit_3_title', '푸꾸옥 전지역 리조트 당일 2시간 배달') }}</div>
                        <div class="text-[11px] text-stone-600 mt-0.5">{{ settings.get('text_benefit_3_desc', '빈펄, 풀만, 인터컨티넨탈, 노보텔 로비로 그랩 퀵 직배송') }}</div>
                    </div>
                </div>
            </div>'''

if old_quick_card in text:
    text = text.replace(old_quick_card, new_quick_card)
    print("1. Hero Quick Value Card updated successfully!")
else:
    print("Warning: old_quick_card not found directly")

# 2. REMOVE REDUNDANT STICKY TAB BAR
old_sticky_bar = '''<!-- STICKY CURATED TAB BAR (Cognitive Load Reduction - Human-Eye Focus) -->
<div class="sticky top-0 z-30 bg-[#FAF7F2]/95 backdrop-blur-md border-b border-amber-200 py-3 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between gap-4">
        <div class="flex items-center space-x-1.5 sm:space-x-2 text-xs font-bold overflow-x-auto no-scrollbar py-0.5">
            <button onclick="switchMainTab('promo')" id="tab-btn-promo" class="main-tab-btn px-4 py-2 rounded-xl transition bg-amber-500 text-white font-extrabold shadow-sm flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-gift"></i>
                <span>★ $100 베스트 세트</span>
            </button>
            <button onclick="switchMainTab('builder')" id="tab-btn-builder" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-sliders"></i>
                <span>10+2 직접 담기</span>
            </button>
            <button onclick="switchMainTab('quality')" id="tab-btn-quality" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-shield-halved"></i>
                <span>품질 비교 & 수하물 계산</span>
            </button>
            <button onclick="switchMainTab('store')" id="tab-btn-store" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-store"></i>
                <span>소나시 매장 실사 & 배달</span>
            </button>
            <button onclick="switchMainTab('catalog')" id="tab-btn-catalog" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-boxes-stacked"></i>
                <span>전체 단품</span>
            </button>
            <button onclick="switchMainTab('all')" id="tab-btn-all" class="main-tab-btn px-3 py-2 rounded-xl transition bg-stone-100 text-stone-500 hover:text-stone-800 border border-stone-200 flex items-center gap-1 whitespace-nowrap">
                <i class="fa-solid fa-layer-group"></i>
                <span>전체 펼쳐보기</span>
            </button>
        </div>
        <div class="hidden lg:flex items-center text-xs text-amber-800 font-bold bg-amber-100/70 px-3 py-1.5 rounded-lg border border-amber-200">
            <i class="fa-solid fa-truck-fast text-amber-600 mr-1.5"></i>
            <span>$100 이상 결제 시 한국 자택 무료 직배송 (소액면세 보증)</span>
        </div>
    </div>
</div>'''

# Replace with a clean subtle top announcement or clean divider
new_sticky_bar = '''<!-- Top Brand Value Notification Strip (Clean & Non-Intrusive) -->
<div class="bg-amber-100/90 border-b border-amber-300/60 py-2.5 px-4 text-center text-xs font-black text-amber-900">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-2">
        <i class="fa-solid fa-plane-departure text-amber-600"></i>
        <span>$100 이상 주문 시 한국 자택 100% 무료 항공 직배송 (15kg 수하물 오버차지 ZERO 면세 보증)</span>
    </div>
</div>'''

if old_sticky_bar in text:
    text = text.replace(old_sticky_bar, new_sticky_bar)
    print("2. Redundant sticky tab bar removed and replaced with clean notification strip!")
else:
    print("Warning: old_sticky_bar not found directly")

# 3. FIX PROMO SETS GIFT BAG PILL
old_promo_pill = '''                <div class="text-xs text-gold-300 bg-gold-500/10 border border-gold-500/30 px-3.5 py-2 rounded-xl flex items-center space-x-2">
                    <i class="fa-solid fa-gift text-gold-400"></i>
                    <span>선물용 쇼핑백 & 위생 박스 무료 동봉</span>
                </div>'''

new_promo_pill = '''                <div class="text-xs font-black text-amber-900 bg-amber-100 border border-amber-300 px-4 py-2 rounded-xl flex items-center space-x-2 shadow-xs">
                    <i class="fa-solid fa-gift text-amber-600"></i>
                    <span>선물용 쇼핑백 & 위생 박스 무료 동봉</span>
                </div>'''

if old_promo_pill in text:
    text = text.replace(old_promo_pill, new_promo_pill)
    print("3. Promo gift bag pill updated with high contrast!")
else:
    print("Warning: old_promo_pill not found directly")

# 4. REMOVE SECTION HIDING IN JS
old_js_tabs = '''    // Curated Main Tab Switcher
    function switchMainTab(tabKey) {
        document.querySelectorAll('.main-tab-btn').forEach(btn => {
            btn.className = 'main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap';
        });
        const activeBtn = document.getElementById('tab-btn-' + tabKey);
        if (activeBtn) {
            if (tabKey === 'all') {
                activeBtn.className = 'main-tab-btn px-3 py-2 rounded-xl transition bg-stone-800 text-white font-extrabold shadow-sm flex items-center gap-1 whitespace-nowrap';
            } else {
                activeBtn.className = 'main-tab-btn px-4 py-2 rounded-xl transition bg-amber-500 text-white font-extrabold shadow-sm flex items-center gap-1.5 whitespace-nowrap';
            }
        }

        const sections = document.querySelectorAll('section[data-tab]');
        sections.forEach(sec => {
            if (tabKey === 'all' || sec.getAttribute('data-tab') === tabKey) {
                sec.style.display = 'block';
                sec.classList.remove('hidden');
            } else {
                sec.style.display = 'none';
                sec.classList.add('hidden');
            }
        });

        sessionStorage.setItem('curated_main_tab', tabKey);
    }

    // Auto-detect hash or initialize curated tab on load
    document.addEventListener('DOMContentLoaded', () => {
        const hash = window.location.hash;
        if (hash.includes('promo')) switchMainTab('promo');
        else if (hash.includes('builder')) switchMainTab('builder');
        else if (hash.includes('competitor')) switchMainTab('quality');
        else if (hash.includes('store') || hash.includes('location')) switchMainTab('store');
        else if (hash.includes('product') || hash.includes('sample')) switchMainTab('catalog');
        else {
            switchMainTab(sessionStorage.getItem('curated_main_tab') || 'promo');
        }
    });'''

new_js_tabs = '''    // All sections naturally flow for smooth browsing
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('section[data-tab]').forEach(sec => {
            sec.style.display = 'block';
            sec.classList.remove('hidden');
        });
    });'''

if old_js_tabs in text:
    text = text.replace(old_js_tabs, new_js_tabs)
    print("4. JavaScript section hiding logic removed! Natural scrolling enabled!")
else:
    print("Warning: old_js_tabs not found directly")

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Finished applying UX flaw fixes!")
