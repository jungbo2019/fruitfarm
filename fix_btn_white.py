with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '''<a href="#custom-builder" class="bg-stone-900 hover:bg-black text-white font-black px-6 py-3.5 rounded-2xl text-xs sm:text-sm border-2 border-amber-400 shadow-xl transition flex items-center space-x-2">
                    <i class="fa-solid fa-sliders text-amber-400 text-sm"></i>
                    <span class="text-white font-extrabold tracking-wide">10+2 내맘대로 골라담기</span>
                </a>'''

replacement = '''<a href="#custom-builder" style="color: #FFFFFF !important;" class="btn-keep-white bg-stone-950 hover:bg-black text-white font-black px-6 py-3.5 rounded-2xl text-xs sm:text-sm border-2 border-amber-400 shadow-xl transition flex items-center space-x-2">
                    <i class="fa-solid fa-sliders text-amber-400 text-sm"></i>
                    <span style="color: #FFFFFF !important;" class="btn-keep-white font-extrabold tracking-wide">10+2 내맘대로 골라담기</span>
                </a>'''

c_norm = c.replace('\r\n', '\n')
if target in c_norm:
    c_norm = c_norm.replace(target, replacement)
    print("Successfully injected inline color and btn-keep-white class!")
else:
    print("Could not find exact target string")

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)
