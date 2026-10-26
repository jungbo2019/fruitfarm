with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Nav & Right Header
old_nav_block = '''            <!-- Clean Customer Navigation Links -->
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

new_nav_block = '''            <!-- Clean Customer Navigation Links -->
            <nav class="hidden lg:flex items-center space-x-8 text-xs font-bold text-slate-700">
                <a href="{{ url_for('index') }}#promo" class="hover:text-amber-500 transition py-1">추천 기획세트 ($100)</a>
                <a href="{{ url_for('index') }}#custom-builder" class="hover:text-amber-500 transition py-1 text-amber-500 font-extrabold">10+2 골라담기</a>
                <a href="{{ url_for('index') }}#products" class="hover:text-amber-500 transition py-1">전체 상품</a>
                <a href="{{ url_for('index') }}#delivery-info" class="hover:text-amber-500 transition py-1">무료 직배송 안내</a>
            </nav>

            <!-- Right Actions: Cart Only -->
            <div class="flex items-center space-x-3">
                <button onclick="openCartModal()" class="flex items-center space-x-2.5 bg-amber-500 hover:bg-amber-600 text-stone-950 px-4 py-2.5 rounded-xl text-xs font-black transition shadow-md shadow-amber-500/20 transform hover:-translate-y-0.5 cursor-pointer">
                    <i class="fa-solid fa-bag-shopping text-sm"></i>
                    <span>장바구니</span>
                    <span id="nav-cart-badge" class="bg-stone-950 text-white rounded-full h-5 w-5 flex items-center justify-center text-[10px] font-black ml-0.5">0</span>
                </button>
            </div>'''

if old_nav_block in text:
    text = text.replace(old_nav_block, new_nav_block)
    print('Header nav simplified successfully!')
else:
    # Try finding by key marker
    idx = text.find('<!-- Clean Customer Navigation Links -->')
    end_idx = text.find('</header>')
    if idx != -1 and end_idx != -1:
        text = text[:idx] + new_nav_block + '\n        </div>\n    ' + text[end_idx:]
        print('Header nav replaced by slice successfully!')

# Replace Floating Buttons with Single Clean Kakao/Care Button
fl_start = text.find('<!-- Floating Concierge Actions')
if fl_start != -1:
    fl_end = text.find('<!-- Guide Access Modal -->')
    if fl_end == -1:
        fl_end = text.find('<footer')
    clean_floating = '''<!-- Floating Customer Care Button (Single, Clean, High Contrast) -->
    <div class="fixed bottom-6 right-6 z-50">
        <a href="{{ settings.get('kakao_channel_url', 'https://pf.kakao.com') }}" target="_blank"
           class="flex items-center space-x-2.5 bg-[#FEE500] hover:bg-[#edd500] text-black px-5 py-3.5 rounded-full shadow-2xl font-black text-xs border border-yellow-300 transition transform hover:scale-105 cursor-pointer">
            <i class="fa-solid fa-comment text-lg"></i>
            <span>카톡 1:1 상담 / 리조트 배달</span>
        </a>
    </div>

    '''
    text = text[:fl_start] + clean_floating + text[fl_end:]
    print('Replaced floating buttons with single clean button!')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(text)
