import re

# 1. Update templates/base.html
base_path = r"E:\fruitfarm\templates\base.html"
with open(base_path, "r", encoding="utf-8") as f:
    base_html = f.read()

# Fix floating button in base.html
old_floating = """    <!-- Floating Customer Care Button (Single, Clean, High Contrast) -->
    <div class="fixed bottom-6 right-6 z-50">
        <a href="{{ settings.get('kakao_channel_url', 'https://pf.kakao.com') }}" target="_blank"
           class="flex items-center space-x-2.5 bg-[#FEE500] hover:bg-[#edd500] text-black px-5 py-3.5 rounded-full shadow-2xl font-black text-xs border border-yellow-300 transition transform hover:scale-105 cursor-pointer">
            <i class="fa-solid fa-comment text-lg"></i>
            <span>카톡 1:1 상담 / 리조트 배달</span>
        </a>
    </div>"""

new_floating = """    <!-- Floating Customer Care Button (Mobile Responsive High Contrast) -->
    <div class="fixed bottom-4 right-3 sm:bottom-6 sm:right-6 z-40">
        <a href="{{ settings.get('kakao_channel_url', 'https://pf.kakao.com') }}" target="_blank"
           class="flex items-center gap-1.5 bg-[#FEE500] hover:bg-[#edd500] text-black px-3.5 py-2.5 sm:px-5 sm:py-3.5 rounded-full shadow-2xl font-black text-xs border border-yellow-400 transition transform hover:scale-105 cursor-pointer">
            <i class="fa-solid fa-comment text-base sm:text-lg"></i>
            <span class="hidden sm:inline">카톡 1:1 상담 / 리조트 배달</span>
            <span class="inline sm:hidden font-black text-[11px]">카톡 1:1 상담</span>
        </a>
    </div>"""

if old_floating in base_html:
    base_html = base_html.replace(old_floating, new_floating)
    print("1. Updated floating kakao button in base.html!")
else:
    print("WARNING: old_floating not found verbatim in base.html!")

with open(base_path, "w", encoding="utf-8") as f:
    f.write(base_html)

# 2. Update templates/index.html
index_path = r"E:\fruitfarm\templates\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Fix Hero CTA buttons & Real store snippet
old_hero_cta = """            <!-- CTA Buttons -->
            <div class="flex flex-wrap items-center gap-3 pt-2">
                <a href="#promo" class="bg-gradient-to-r from-gold-500 to-amber-600 hover:from-gold-400 hover:to-amber-500 text-dark-900 font-black px-6 py-3.5 rounded-2xl text-xs sm:text-sm transition shadow-lg shadow-gold-500/25 flex items-center space-x-2">
                    <i class="fa-solid fa-gift text-base"></i>
                    <span>$100 면세 추천세트 보기</span>
                </a>
                <a href="#custom-builder" style="color: #FFFFFF !important;" class="btn-keep-white bg-stone-950 hover:bg-black text-white font-black px-6 py-3.5 rounded-2xl text-xs sm:text-sm border-2 border-amber-400 shadow-xl transition flex items-center space-x-2">
                    <i class="fa-solid fa-sliders text-amber-400 text-sm"></i>
                    <span style="color: #FFFFFF !important;" class="btn-keep-white font-extrabold tracking-wide">10+2 내맘대로 골라담기</span>
                </a>
            </div>

            <!-- Real Store Address snippet -->
            <div class="pt-2 text-[11px] text-slate-400 flex items-center space-x-2">
                <i class="fa-solid fa-store text-gold-400"></i>
                <span>실제 매장: 소나시 바이쯔엉 SV2A-V07 (소나시 12가) | 연중무휴 상시 무료시식</span>
            </div>"""

new_hero_cta = """            <!-- CTA Buttons -->
            <div class="grid grid-cols-1 sm:flex items-center gap-2.5 pt-2 w-full sm:w-auto">
                <a href="#promo" class="w-full sm:w-auto bg-gradient-to-r from-gold-500 to-amber-600 hover:from-gold-400 hover:to-amber-500 text-dark-900 font-black px-6 py-3.5 rounded-2xl text-xs sm:text-sm transition shadow-lg shadow-gold-500/25 flex items-center justify-center space-x-2 cursor-pointer">
                    <i class="fa-solid fa-gift text-base"></i>
                    <span>$100 면세 추천세트 보기</span>
                </a>
                <a href="#custom-builder" style="color: #FFFFFF !important;" class="w-full sm:w-auto btn-keep-white bg-stone-950 hover:bg-black text-white font-black px-6 py-3.5 rounded-2xl text-xs sm:text-sm border-2 border-amber-400 shadow-xl transition flex items-center justify-center space-x-2 cursor-pointer">
                    <i class="fa-solid fa-sliders text-amber-400 text-sm"></i>
                    <span style="color: #FFFFFF !important;" class="btn-keep-white font-extrabold tracking-wide">10+2 내맘대로 골라담기</span>
                </a>
            </div>

            <!-- Real Store Address snippet with high contrast -->
            <div class="pt-2">
                <div class="inline-flex items-center space-x-2 bg-stone-950/85 backdrop-blur-md px-3.5 py-2 rounded-xl border border-stone-700 text-white text-[11px] font-bold shadow-md">
                    <i class="fa-solid fa-store text-amber-400"></i>
                    <span>실제 매장: 소나시 메인 스트리트 SV2A-V07 (노보텔·풀만 도보 5분) · 상시 무료 시식</span>
                </div>
            </div>"""

if old_hero_cta in index_html:
    index_html = index_html.replace(old_hero_cta, new_hero_cta)
    print("2. Updated hero buttons & address snippet in index.html!")
else:
    print("WARNING: old_hero_cta not found verbatim in index.html!")

# Fix Competitor Benchmark Table: add mobile swipe banner and min-width to table
old_competitor_table_start = """            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border border-stone-300 rounded-2xl overflow-hidden shadow-sm bg-white">
                    <thead class="bg-stone-900 text-stone-200 font-bold uppercase border-b border-stone-300">
                        <tr>
                            <th class="py-4 px-4 w-1/5 text-stone-300 font-black">비교 핵심 기준</th>
                            <th class="py-4 px-4 w-1/5 text-stone-400 font-bold">푸꾸옥 킹콩마트 (즈엉동/소나시)</th>
                            <th class="py-4 px-4 w-1/5 text-stone-400 font-bold">즈엉동·소나시 야시장 (로컬 가판)</th>
                            <th class="py-4 px-4 w-1/5 text-stone-400 font-bold">추후 진입 모방업체 (단순 소매상)</th>
                            <th class="py-4 px-4 w-1/5 bg-amber-500 text-stone-950 font-black text-sm border-l-2 border-amber-600 shadow-md">"""

new_competitor_table_start = """            <div class="overflow-x-auto -mx-4 px-4 sm:mx-0 sm:px-0">
                <!-- Mobile Swipe Guide Badge -->
                <div class="block sm:hidden mb-3">
                    <div class="bg-amber-100 text-amber-950 border border-amber-300 rounded-xl px-3.5 py-2.5 text-xs font-black flex items-center justify-between shadow-xs">
                        <span>👉 표를 좌우로 넘겨 전체 비교표를 확인하세요</span>
                        <i class="fa-solid fa-arrows-left-right text-amber-600 animate-pulse text-sm"></i>
                    </div>
                </div>
                <table class="min-w-[760px] w-full text-left text-xs border border-stone-300 rounded-2xl overflow-hidden shadow-sm bg-white [word-break:keep-all]">
                    <thead class="bg-stone-900 text-stone-200 font-bold uppercase border-b border-stone-300">
                        <tr>
                            <th class="py-4 px-3 sm:px-4 min-w-[120px] text-stone-300 font-black">비교 핵심 기준</th>
                            <th class="py-4 px-3 sm:px-4 min-w-[150px] text-stone-400 font-bold">푸꾸옥 킹콩마트<br><span class="text-[10px] text-stone-500">(즈엉동/소나시)</span></th>
                            <th class="py-4 px-3 sm:px-4 min-w-[140px] text-stone-400 font-bold">즈엉동·소나시 야시장<br><span class="text-[10px] text-stone-500">(로컬 가판)</span></th>
                            <th class="py-4 px-3 sm:px-4 min-w-[140px] text-stone-400 font-bold">추후 진입 모방업체<br><span class="text-[10px] text-stone-500">(단순 소매상)</span></th>
                            <th class="py-4 px-3 sm:px-4 min-w-[210px] bg-amber-500 text-stone-950 font-black text-sm border-l-2 border-amber-600 shadow-md">"""

if old_competitor_table_start in index_html:
    index_html = index_html.replace(old_competitor_table_start, new_competitor_table_start)
    print("3. Updated competitor table with horizontal scroll & min-width!")
else:
    print("WARNING: old_competitor_table_start not found verbatim in index.html!")

# Fix "직접 맛 선택" button contrast in promo set cards
old_taste_btn = """                        <div class="grid grid-cols-2 gap-2">
                            <button onclick="addToCart({{ p.id }}, '{{ p.name }}', {{ p.price_usd }}, {{ p.price_krw }}, '{{ p.image_url }}', 1)"
                                    class="bg-gradient-to-r from-gold-500 to-amber-600 hover:from-gold-400 hover:to-amber-500 text-dark-900 font-black py-3 rounded-xl text-xs transition shadow flex items-center justify-center space-x-1.5">
                                <i class="fa-solid fa-cart-plus"></i>
                                <span>바로 담기</span>
                            </button>
                            <a href="#custom-builder" class="bg-dark-800 hover:bg-dark-700 text-slate-200 border border-slate-700 font-bold py-3 rounded-xl text-xs transition flex items-center justify-center">
                                <span>직접 맛 선택</span>
                            </a>
                        </div>"""

new_taste_btn = """                        <div class="grid grid-cols-2 gap-2">
                            <button onclick="addToCart({{ p.id }}, '{{ p.name }}', {{ p.price_usd }}, {{ p.price_krw }}, '{{ p.image_url }}', 1)"
                                    class="bg-amber-500 hover:bg-amber-600 text-stone-950 font-black py-3 rounded-xl text-xs transition shadow flex items-center justify-center space-x-1.5 cursor-pointer">
                                <i class="fa-solid fa-cart-plus"></i>
                                <span>바로 담기</span>
                            </button>
                            <a href="#custom-builder" class="bg-stone-100 hover:bg-stone-200 text-stone-900 border border-stone-300 font-black py-3 rounded-xl text-xs transition flex items-center justify-center space-x-1 shadow-xs cursor-pointer">
                                <i class="fa-solid fa-sliders text-amber-600"></i>
                                <span>직접 맛 선택</span>
                            </a>
                        </div>"""

if old_taste_btn in index_html:
    index_html = index_html.replace(old_taste_btn, new_taste_btn)
    print("4. Fixed 직접 맛 선택 button contrast in index.html!")
else:
    print("WARNING: old_taste_btn not found verbatim in index.html!")

# Add [word-break:keep-all] break-keep to titles
index_html = index_html.replace(
    'class="text-2xl sm:text-4xl font-black text-stone-900 mt-1"',
    'class="text-xl sm:text-4xl font-black text-stone-900 mt-1 [word-break:keep-all] break-keep leading-snug"'
)

# Reduce excessive section paddings
index_html = index_html.replace('class="py-16 bg-dark-800 border-b border-slate-800"', 'class="py-10 sm:py-16 bg-dark-800 border-b border-slate-800"')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print("index.html mobile optimization complete!")
