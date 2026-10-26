with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- Floating Concierge Actions -->'
end_marker = '<!-- Guide Access Modal -->'

s_idx = text.find(start_marker)
e_idx = text.find(end_marker)

if s_idx != -1 and e_idx != -1:
    new_block = '''<!-- Floating Concierge Actions (AI + Kakao) -->
    <div class="fixed bottom-6 right-6 z-50 flex flex-col space-y-2.5 items-end">
        <button onclick="openAIChatbot()" id="aiFloatingBtn"
                class="flex items-center space-x-2.5 bg-stone-950 hover:bg-black text-white px-4 py-3 rounded-2xl shadow-2xl border-2 border-amber-400 font-black text-xs transition transform hover:scale-105 cursor-pointer">
            <div class="relative flex items-center justify-center">
                <i class="fa-solid fa-robot text-amber-400 text-base"></i>
                <span class="absolute -top-1 -right-1 w-2 h-2 bg-amber-500 rounded-full animate-ping"></span>
            </div>
            <span>🤖 AI 24시 즉시상담 (통관·배송)</span>
        </button>
        <a href="{{ settings.get('kakao_channel_url', 'https://pf.kakao.com') }}" target="_blank"
           class="flex items-center space-x-2 bg-[#FEE500] hover:bg-[#edd500] text-black px-4 py-3 rounded-2xl border border-yellow-300 shadow-2xl font-black text-xs transition transform hover:scale-105">
            <i class="fa-solid fa-comment text-lg"></i>
            <span>💬 카톡 1:1 상담 / 리조트 배달</span>
        </a>
    </div>

    '''
    text = text[:s_idx] + new_block + text[e_idx:]
    with open('templates/base.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Floating block successfully replaced by marker!')
else:
    print('Markers not found')
