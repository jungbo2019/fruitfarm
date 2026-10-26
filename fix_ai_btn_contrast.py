# -*- coding: utf-8 -*-
with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')

old_btn = '''                <button onclick="openAIChatbot()" class="bg-stone-950 hover:bg-black text-white font-black px-3.5 py-1.5 rounded-xl transition shadow-md border border-amber-400 flex items-center gap-1.5 text-xs">
                    <i class="fa-solid fa-robot text-amber-400"></i>
                    <span>AI 24시 즉시상담 (통관·배송)</span>
                </button>'''

new_btn = '''                <button onclick="openAIChatbot()" style="color: #FFFFFF !important;" class="btn-keep-white bg-stone-950 hover:bg-black font-black px-3.5 py-1.5 rounded-xl transition shadow-md border-2 border-amber-400 flex items-center gap-1.5 text-xs">
                    <i class="fa-solid fa-robot text-amber-400"></i>
                    <span style="color: #FFFFFF !important;" class="btn-keep-white font-black">AI 24시 즉시상담 (통관·배송)</span>
                </button>'''

if old_btn in text:
    text = text.replace(old_btn, new_btn)
    print("Fixed AI button text contrast!")
else:
    print("Warning: old_btn not found directly")

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
