with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c_norm = c.replace('\r\n', '\n')

old_btn = '''<a href="#custom-builder" class="bg-dark-800/90 hover:bg-dark-700 text-white font-bold px-6 py-3.5 rounded-2xl text-xs sm:text-sm border border-slate-700 hover:border-gold-500/40 transition flex items-center space-x-2">
                    <i class="fa-solid fa-sliders text-gold-400"></i>
                    <span>10+2 내맘대로 골라담기</span>
                </a>'''

new_btn = '''<a href="#custom-builder" class="bg-stone-900 hover:bg-black text-white font-black px-6 py-3.5 rounded-2xl text-xs sm:text-sm border-2 border-amber-400 shadow-xl transition flex items-center space-x-2">
                    <i class="fa-solid fa-sliders text-amber-400 text-sm"></i>
                    <span class="text-white font-extrabold tracking-wide">10+2 내맘대로 골라담기</span>
                </a>'''

old_phone = '''<span class="font-mono font-bold text-gold-300">{{ settings.get('store_phone', '+84 386 074 755') }}</span>'''
new_phone = '''<span class="font-mono font-black text-stone-900 bg-amber-200/80 px-2.5 py-1 rounded-md text-xs sm:text-sm border border-amber-300">{{ settings.get('store_phone', '+84 386 074 755') }}</span>'''

if old_btn in c_norm:
    c_norm = c_norm.replace(old_btn, new_btn)
    print("Hero button updated successfully!")
else:
    print("Warning: old_btn not found directly")

if old_phone in c_norm:
    c_norm = c_norm.replace(old_phone, new_phone)
    print("Phone number updated successfully!")
else:
    print("Warning: old_phone not found directly")

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)
