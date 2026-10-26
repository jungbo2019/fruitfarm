with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix showroom title to dark text
text = text.replace(
    'text-2xl sm:text-4xl font-black text-white mt-1">{{ settings.get(\'text_gallery_title\'',
    'text-2xl sm:text-4xl font-black text-stone-900 mt-1">{{ settings.get(\'text_gallery_title\''
)
text = text.replace(
    'text-xs sm:text-sm text-slate-400 mt-2',
    'text-xs sm:text-sm text-stone-600 mt-2'
)

# 2. Fix Hero Card Concierge button
old_button_block = '''                <button onclick="openAIChatbot()" style="color: #FFFFFF !important;" class="btn-keep-white bg-black hover:bg-stone-900 text-white font-black px-3.5 py-1.5 rounded-xl transition shadow-md border-2 border-amber-400 flex items-center gap-1.5 text-xs">
                    <i class="fa-solid fa-robot text-amber-400"></i>
                    <span style="color: #FFFFFF !important;" class="btn-keep-white font-black">AI 24시 즉시상담 (통관·배송)</span>
                </button>'''

new_button_block = '''                <a href="{{ settings.get('kakao_channel_url', 'https://pf.kakao.com') }}" target="_blank"
                   class="bg-amber-500 hover:bg-amber-600 text-stone-950 font-black px-3.5 py-1.5 rounded-xl transition shadow-md flex items-center gap-1.5 text-xs">
                    <i class="fa-solid fa-comment"></i>
                    <span>카톡 24시간 실시간 상담</span>
                </a>'''

if old_button_block in text:
    text = text.replace(old_button_block, new_button_block)
    print('Replaced hero AI button with Kakao consultation link!')
else:
    # slice replacement
    idx = text.find('AI 24시 즉시상담')
    if idx != -1:
        b_start = text.rfind('<button', 0, idx)
        b_end = text.find('</button>', idx)
        text = text[:b_start] + new_button_block + text[b_end+9:]
        print('Replaced hero AI button by slice!')

# 3. Remove duplicate notification strip under hero
idx_strip = text.find('Top Brand Value Notification Strip')
if idx_strip != -1:
    s_start = text.rfind('<!--', 0, idx_strip)
    s_end = text.find('</div>\n</div>', idx_strip)
    text = text[:s_start] + text[s_end+14:]
    print('Removed duplicate notification strip!')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
