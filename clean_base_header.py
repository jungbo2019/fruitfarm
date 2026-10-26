# -*- coding: utf-8 -*-
with open('E:/fruitfarm/templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')

# 1. CLEAN TOP UTILITY BAR (Remove Admin login & Raw exchange rate, keep clean customer info)
old_top_bar = '''    <!-- Top Luxury Announcement & Dual Pricing Bar -->
    <div class="bg-gradient-to-r from-dark-900 via-dark-800 to-dark-900 border-b border-gold-400/20 text-xs py-2 px-4">
        <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
            <div class="flex items-center space-x-2.5">
                <span class="bg-gold-500/20 text-gold-300 border border-gold-500/40 text-[10px] font-black px-2 py-0.5 rounded tracking-wide">
                    푸꾸옥 2호점 직영
                </span>
                <span class="text-slate-300 text-[11px] sm:text-xs">
                    {{ settings.get('top_announcement_text', '$100 이상 결제 시 한국 자택 100% 무료 직배송 (Zero Baggage 캐리어 부담 제로)') }}
                </span>
            </div>
            
            <div class="flex items-center space-x-3 text-[11px]">
                <span class="hidden sm:inline text-slate-400">기준환율: 1 USD = <strong class="text-gold-300">{{ settings.get('usd_krw_rate', '1380') }}원</strong></span>
                <span class="text-slate-600">|</span>
                <a href="{{ url_for('order_track') }}" class="text-slate-300 hover:text-gold-300 transition font-semibold flex items-center space-x-1">
                    <i class="fa-solid fa-truck-fast text-gold-400"></i>
                    <span>배송조회</span>
                </a>
                <span class="text-slate-600">|</span>
                <a href="{{ url_for('admin_login') }}" class="text-slate-500 hover:text-slate-300">관리자</a>
            </div>
        </div>
    </div>'''

new_top_bar = '''    <!-- Top Customer Benefit Bar (Clean & Focused on Delivery Benefit) -->
    <div class="bg-gradient-to-r from-dark-900 via-dark-800 to-dark-900 border-b border-gold-400/20 text-xs py-2 px-4">
        <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
            <div class="flex items-center space-x-2.5">
                <span class="bg-amber-500 text-stone-950 font-black text-[10px] px-2 py-0.5 rounded">
                    푸꾸옥 직영
                </span>
                <span class="text-slate-200 text-[11px] sm:text-xs font-medium">
                    ✈️ $100 이상 주문 시 한국 자택 100% 무료 항공 직배송 (15kg 수하물 오버차지 ZERO)
                </span>
            </div>
            
            <div class="flex items-center space-x-3 text-[11px]">
                <a href="{{ url_for('order_track') }}" class="text-slate-200 hover:text-amber-300 transition font-bold flex items-center space-x-1">
                    <i class="fa-solid fa-truck-fast text-amber-400"></i>
                    <span>실시간 배송조회</span>
                </a>
            </div>
        </div>
    </div>'''

if old_top_bar in text:
    text = text.replace(old_top_bar, new_top_bar)
    print("1. Cleaned Top Utility Bar (Removed admin link & raw exchange rate)!")
else:
    print("Warning: old_top_bar not found directly")

# 2. STREAMLINE MAIN HEADER NAVIGATION (Focused on Customer Shopping & AI Concierge)
old_nav = '''            <!-- Navigation Links -->
            <nav class="hidden lg:flex items-center space-x-7 text-xs font-bold text-slate-300">
                <a href="{{ url_for('index') }}#promo" class="hover:text-gold-300 transition py-1">100$ 면세 추천세트</a>
                <a href="{{ url_for('index') }}#custom-builder" class="hover:text-gold-300 transition py-1 text-gold-400">10+2 DIY 패키지</a>
                <a href="{{ url_for('index') }}#competitor-matrix" class="hover:text-gold-300 transition py-1">타업체 비교검증</a>
                <a href="{{ url_for('index') }}#products" class="hover:text-gold-300 transition py-1">전체 상품</a>
                <a href="{{ url_for('index') }}#delivery-info" class="hover:text-gold-300 transition py-1">한국 직배송·호텔 배달</a>
                <a href="{{ url_for('index') }}#sample" class="hover:text-gold-300 transition py-1 text-amber-300">가이드 무료샘플</a>
            </nav>

            <!-- Right Actions: Dual Pricing Switcher & Cart -->
            <div class="flex items-center space-x-3">
                {% if settings.get('show_guide_b2b_button', '1') == '1' %}
                <!-- Mode Toggle Button -->
                <button id="guideModeToggleBtn" onclick="openGuideModal()" class="flex items-center space-x-1.5 px-3 py-2 rounded-xl text-xs font-bold transition border border-gold-500/30 bg-gold-500/10 hover:bg-gold-500/20 text-gold-300">
                    <i class="fa-solid fa-handshake"></i>
                    <span id="guideModeBtnText">가이드 파트너 B2B</span>
                </button>
                {% endif %}

                <!-- Cart Button -->
                <button onclick="openCartModal()" class="flex items-center space-x-2.5 bg-gradient-to-r from-gold-500 to-amber-600 hover:from-gold-400 hover:to-amber-500 text-dark-900 px-4 py-2.5 rounded-xl text-xs font-black transition shadow-lg shadow-gold-500/20 transform hover:-translate-y-0.5">
                    <i class="fa-solid fa-bag-shopping text-sm"></i>
                    <span>장바구니</span>
                    <span id="nav-cart-badge" class="bg-dark-900 text-gold-300 rounded-full h-5 w-5 flex items-center justify-center text-[10px] font-black ml-0.5">0</span>
                </button>
            </div>'''

new_nav = '''            <!-- Clean Customer Navigation Links -->
            <nav class="hidden lg:flex items-center space-x-7 text-xs font-bold text-slate-300">
                <a href="{{ url_for('index') }}#promo" class="hover:text-amber-400 transition py-1">추천 기획세트 ($100)</a>
                <a href="{{ url_for('index') }}#custom-builder" class="hover:text-amber-400 transition py-1 text-amber-400">10+2 골라담기</a>
                <a href="{{ url_for('index') }}#products" class="hover:text-amber-400 transition py-1">전체 상품</a>
                <a href="{{ url_for('index') }}#delivery-info" class="hover:text-amber-400 transition py-1">무료 직배송 안내</a>
                <button onclick="openAIChatbot()" class="hover:text-amber-400 transition py-1 flex items-center gap-1.5 text-amber-300 font-extrabold">
                    <i class="fa-solid fa-robot text-amber-400"></i>
                    <span>AI 24시 상담원</span>
                </button>
            </nav>

            <!-- Right Actions: Cart & AI Assist -->
            <div class="flex items-center space-x-3">
                <!-- AI Quick Inquire Button -->
                <button onclick="openAIChatbot()" class="hidden sm:flex items-center space-x-1.5 px-3 py-2 rounded-xl text-xs font-bold transition border border-amber-400/40 bg-amber-500/10 hover:bg-amber-500/20 text-amber-400">
                    <i class="fa-solid fa-robot"></i>
                    <span>AI 즉시상담</span>
                </button>

                <!-- Cart Button -->
                <button onclick="openCartModal()" class="flex items-center space-x-2.5 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-stone-950 px-4 py-2.5 rounded-xl text-xs font-black transition shadow-lg shadow-amber-500/20 transform hover:-translate-y-0.5">
                    <i class="fa-solid fa-bag-shopping text-sm"></i>
                    <span>장바구니</span>
                    <span id="nav-cart-badge" class="bg-stone-950 text-white rounded-full h-5 w-5 flex items-center justify-center text-[10px] font-black ml-0.5">0</span>
                </button>
            </div>'''

if old_nav in text:
    text = text.replace(old_nav, new_nav)
    print("2. Streamlined Main Header Navigation for Ordinary Customers!")
else:
    print("Warning: old_nav not found directly")

# 3. ADD B2B & ADMIN LINKS TO FOOTER (Clean place where customers are not bothered)
footer_anchor = '''            <!-- Col 4: Store Info -->'''
b2b_footer_snippet = '''            <!-- Col 4: Partner & B2B Discreet Access -->
            <div class="space-y-3">
                <h4 class="text-xs font-black text-slate-300 uppercase tracking-wider">파트너 & 시스템</h4>
                <div class="text-xs text-slate-500 space-y-2">
                    <div>
                        <button onclick="openGuideModal()" class="text-stone-400 hover:text-amber-400 transition flex items-center gap-1.5">
                            <i class="fa-solid fa-handshake"></i>
                            <span>가이드/여행사 B2B 파트너 전용</span>
                        </button>
                    </div>
                    <div>
                        <a href="{{ url_for('admin_login') }}" class="text-stone-500 hover:text-stone-300 transition flex items-center gap-1.5 text-[11px]">
                            <i class="fa-solid fa-lock"></i>
                            <span>관리자 포털 로그인</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Col 5: Store Info -->'''

if footer_anchor in text:
    text = text.replace(footer_anchor, b2b_footer_snippet)
    print("3. Moved B2B Partner and Admin Login to Footer!")

with open('E:/fruitfarm/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Base.html updated successfully!")
