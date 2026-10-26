# -*- coding: utf-8 -*-
with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')

# 1. Polish FRUIT FARM column in competitor matrix for high contrast
text = text.replace(
    'class="py-4 px-4 bg-gold-500/20 text-gold-300 font-black border-l border-gold-500/40">FRUIT FARM 푸꾸옥 2호점',
    'class="py-4 px-4 bg-amber-500 text-stone-950 font-black border-l border-amber-600 text-sm">FRUIT FARM 푸꾸옥 2호점'
)

text = text.replace(
    'bg-gold-500/10 text-gold-200 font-bold border-l border-gold-500/40',
    'bg-amber-50 text-amber-950 font-bold border-l-2 border-amber-400'
)

# 2. Polish live ticker text in calculator
text = text.replace(
    'class="font-bold text-white mt-0.5" id="mainLiveTickerText">',
    'class="font-bold text-stone-100 mt-0.5 text-xs tracking-wide" id="mainLiveTickerText">'
)

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Polished competitor column and ticker contrast!")
