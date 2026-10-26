with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update cart button badge in templates/base.html
old_cart_btn = '''                <!-- Cart Button -->
                <button onclick="openCartModal()" class="flex items-center space-x-2.5 bg-amber-500 hover:bg-amber-600 text-stone-950 px-4 py-2.5 rounded-xl text-xs font-black transition shadow-md shadow-amber-500/20 transform hover:-translate-y-0.5 cursor-pointer">
                    <i class="fa-solid fa-bag-shopping text-sm"></i>
                    <span>장바구니</span>
                    <span id="nav-cart-badge" class="bg-stone-950 text-white rounded-full h-5 w-5 flex items-center justify-center text-[10px] font-black ml-0.5">0</span>
                </button>'''

new_cart_btn = '''                <!-- Cart Button -->
                <button onclick="openCartModal()" class="flex items-center space-x-2 bg-amber-500 hover:bg-amber-600 text-stone-950 px-4 py-2.5 rounded-xl text-xs font-black transition shadow-md shadow-amber-500/20 transform hover:-translate-y-0.5 cursor-pointer">
                    <i class="fa-solid fa-bag-shopping text-sm"></i>
                    <span>장바구니</span>
                    <span class="bg-stone-950/15 text-stone-950 px-2 py-0.5 rounded-full text-xs font-black ml-1 border border-stone-950/20">(<span id="nav-cart-badge">0</span>)</span>
                </button>'''

if old_cart_btn in text:
    text = text.replace(old_cart_btn, new_cart_btn)
    print('Updated cart button with clean badge!')
else:
    # slice replacement
    idx = text.find('nav-cart-badge')
    if idx != -1:
        btn_start = text.rfind('<button onclick="openCartModal()"', 0, idx)
        btn_end = text.find('</button>', idx)
        text = text[:btn_start] + new_cart_btn + text[btn_end+9:]
        print('Updated cart button by slice!')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(text)
