# 1. Update templates/base.html
with open('templates/base.html', 'r', encoding='utf-8') as f:
    btext = f.read()

# Replace guarantee block in footer
old_guarantee = '''                <ul class="space-y-2 text-[11px]">
                    <li class="flex items-center space-x-1.5"><i class="fa-solid fa-check text-gold-400"></i><span>1인당 $150 관세청 면세 한도 엄격 준수</span></li>
                    <li class="flex items-center space-x-1.5"><i class="fa-solid fa-check text-gold-400"></i><span>100$ 이상 주문 시 한국 집 앞 무료 직배송</span></li>
                    <li class="flex items-center space-x-1.5"><i class="fa-solid fa-check text-gold-400"></i><span>푸꾸옥 전지역 리조트 당일 2시간 퀵 배송</span></li>
                    <li class="flex items-center space-x-1.5"><i class="fa-solid fa-check text-gold-400"></i><span>FEFO 선입선출 바코드 유통기한 전수 검수</span></li>
                </ul>'''

new_guarantee = '''                <ul class="space-y-2.5 text-xs font-bold text-stone-700">
                    <li class="flex items-center space-x-2"><i class="fa-solid fa-check text-amber-500 font-black"></i><span>100% 무설탕 저온건조 프리미엄 특산품 보증</span></li>
                    <li class="flex items-center space-x-2"><i class="fa-solid fa-check text-amber-500 font-black"></i><span>$100 이상 주문 시 한국 자택 무료 직배송</span></li>
                    <li class="flex items-center space-x-2"><i class="fa-solid fa-check text-amber-500 font-black"></i><span>푸꾸옥 전지역 리조트 당일 2시간 퀵 배달</span></li>
                    <li class="flex items-center space-x-2"><i class="fa-solid fa-check text-amber-500 font-black"></i><span>배송 중 파손·변질 시 100% 즉시 무상 맞교환</span></li>
                </ul>'''

if old_guarantee in btext:
    btext = btext.replace(old_guarantee, new_guarantee)
    print('Updated guarantee block in base.html footer!')
else:
    # slice replacement
    g_start = btext.find('안심 쇼핑 보증')
    if g_start != -1:
        ul_start = btext.find('<ul', g_start)
        ul_end = btext.find('</ul>', ul_start)
        btext = btext[:ul_start] + new_guarantee + btext[ul_end+5:]
        print('Updated guarantee block by slice!')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(btext)

# 2. Update templates/index.html
with open('templates/index.html', 'r', encoding='utf-8') as f:
    itext = f.read()

# Remove .00 from prices
itext = itext.replace('$100.00', '$100')
itext = itext.replace('${{ "%.2f"|format(prod.price_usd) }}', '${{ prod.price_usd|int }}')
itext = itext.replace('${{ "%.2f"|format(p.price_usd) }}', '${{ p.price_usd|int }}')

# Fix Catalog Section Header
itext = itext.replace(
    '푸꾸옥 2호점 단품 상품 전수 검수관',
    'FRUIT FARM 푸꾸옥 직영 플래그십 전 상품'
)
itext = itext.replace(
    '푸꾸옥 플래그십 단품 상품 전수 검수관',
    'FRUIT FARM 푸꾸옥 직영 플래그십 전 상품'
)
itext = itext.replace(
    'PC 바코드 기반 FEFO(유통기한 선입선출) 시스템으로 가장 신선한 로트만을 선별하여 출고합니다.',
    '호치민 직영 HACCP 공장에서 무설탕 저온건조로 정직하게 가공한 프리미엄 특산품입니다.'
)

# Fix FLAGSHIP STORE section colors and phone exposure
loc_start = itext.find('id="store-location"')
if loc_start == -1:
    loc_start = itext.find('FLAGSHIP STORE')
    loc_start = itext.rfind('<section', 0, loc_start)

loc_end = itext.find('</section>', loc_start)
old_loc_block = itext[loc_start:loc_end+10]

new_loc_block = '''<section id="store-location" data-tab="location" class="py-16 bg-stone-100 border-b border-stone-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <div class="bg-white rounded-3xl p-8 border border-stone-200 shadow-sm flex flex-col lg:flex-row items-center gap-10">
                <div class="lg:w-1/2 space-y-4">
                    <span class="text-xs font-black text-amber-600 tracking-widest uppercase">FLAGSHIP STORE</span>
                    <h2 class="text-2xl sm:text-3xl font-black text-stone-900 mt-1">FRUIT FARM 푸꾸옥 직영 플래그십</h2>
                    <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
                        푸꾸옥 최고의 리조트 밀집 지역인 소나시(Sonasea) 야시장 메인 스트리트에 위치하고 있습니다. 노보텔, 풀만, 인터컨티넨탈에서 도보 5분 거리에 위치하여 언제든 편하게 무료 시식하러 오실 수 있습니다.
                    </p>

                    <div class="space-y-3 pt-4 border-t border-stone-100 text-xs text-stone-800">
                        <div class="flex items-start space-x-3">
                            <div class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center flex-shrink-0 mt-0.5">
                                <i class="fa-solid fa-location-dot"></i>
                            </div>
                            <div>
                                <strong class="text-stone-900 font-black">공식 매장 주소:</strong>
                                <span class="text-stone-700 font-bold ml-1">SV2A - V07 Khu Sonasea Bãi Trường, Phú Quốc (소나시 12가 메인 스트리트)</span>
                            </div>
                        </div>

                        <div class="flex items-center space-x-3">
                            <div class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center flex-shrink-0">
                                <i class="fa-solid fa-clock"></i>
                            </div>
                            <div>
                                <strong class="text-stone-900 font-black">운영 시간:</strong>
                                <span class="text-stone-700 font-bold ml-1">매일 09:00 ~ 22:00 (연중무휴 · 전 품목 무료 시식 상시 운영)</span>
                            </div>
                        </div>

                        <div class="flex items-center space-x-3">
                            <div class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center flex-shrink-0">
                                <i class="fa-solid fa-comment"></i>
                            </div>
                            <div>
                                <strong class="text-stone-900 font-black">실시간 고객 상담:</strong>
                                <span class="text-stone-700 font-bold ml-1">카카오톡 채널 @fruitfarm (24시간 리조트 배달 및 주문 안내)</span>
                            </div>
                        </div>
                    </div>

                    <div class="pt-4 flex flex-wrap gap-3">
                        <a href="https://maps.google.com" target="_blank"
                           class="inline-flex items-center space-x-2 bg-stone-900 hover:bg-black text-white px-5 py-3 rounded-xl text-xs font-black transition shadow">
                            <i class="fa-solid fa-map-location-dot text-amber-400"></i>
                            <span>구글 지도에서 매장 찾기</span>
                        </a>
                        <a href="{{ settings.get('kakao_channel_url', 'https://pf.kakao.com') }}" target="_blank"
                           class="inline-flex items-center space-x-2 bg-[#FEE500] hover:bg-[#edd500] text-black px-5 py-3 rounded-xl text-xs font-black border border-yellow-300 transition shadow">
                            <i class="fa-solid fa-comment"></i>
                            <span>카톡으로 리조트 배달 요청</span>
                        </a>
                    </div>
                </div>

                <div class="lg:w-1/2 w-full h-80 rounded-2xl overflow-hidden shadow-md border border-stone-200">
                    <img src="/static/images/store/store_exterior.png" alt="FRUIT FARM 푸꾸옥 플래그십 매장 전경" class="w-full h-full object-cover">
                </div>
            </div>
        </div>
    </section>'''

itext = itext[:loc_start] + new_loc_block + itext[loc_end+10:]
print('Updated FLAGSHIP STORE section with bold readable dark text and no raw phone!')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(itext)

print('All 4 critical user requests applied!')
