# -*- coding: utf-8 -*-
with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('\r\n', '\n')

# 1. REPLACE B2B RS ROW WITH CUSTOMER SATISFACTION / WARRANTY ROW
old_b2b_row = '''                        <tr class="hover:bg-slate-800/40 transition">
                            <td class="py-4 px-4 font-bold text-white bg-dark-900/60">가이드 B2B 수수료 (RS)</td>
                            <td class="py-4 px-4 text-rose-400">불투명한 비공식 뒷돈 흥정 (분쟁 잦음)</td>
                            <td class="py-4 px-4 text-slate-400">수수료 정책 전무 (가이드 메리트 0)</td>
                            <td class="py-4 px-4 text-slate-300">일부 협력사 바우처 제휴</td>
                            <td class="py-4 px-4 bg-gold-500/10 text-gold-200 font-bold border-l border-gold-500/40">
                                ★ 이중가격제 & 가이드 전용 25% RS 실시간 자동 정산
                            </td>
                        </tr>'''

new_customer_row = '''                        <tr class="hover:bg-slate-800/40 transition">
                            <td class="py-4 px-4 font-bold text-white bg-dark-900/60">고객 안심 & 사후 보장</td>
                            <td class="py-4 px-4 text-rose-400">귀국 후 파손/변질 발생 시 교환·환불 불가</td>
                            <td class="py-4 px-4 text-slate-400">로컬 가판 특성상 구매 즉시 연락 두절, 환불 불가</td>
                            <td class="py-4 px-4 text-slate-300">자체 CS 인력 부재로 교환 처리 지연</td>
                            <td class="py-4 px-4 bg-gold-500/10 text-gold-200 font-bold border-l border-gold-500/40">
                                ★ <strong>100% 무상 재발송 보증</strong> (배송 중 파손·변질 시 즉시 1:1 맞교환)
                            </td>
                        </tr>'''

if old_b2b_row in text:
    text = text.replace(old_b2b_row, new_customer_row)
    print("1. Replaced B2B RS row with Customer Satisfaction Guarantee row!")
else:
    print("Warning: old_b2b_row not found directly")

# 2. REDESIGN LCC BAGGAGE CALCULATOR (Clean White Card, High Contrast, Human-eye Friendly)
old_calculator_start = '''            <!-- Korean Sentiment Kinetic Calculator: LCC Baggage Penalty vs Free Korea Direct Delivery -->
            <div class="mt-8 p-6 sm:p-8 rounded-3xl bg-gradient-to-br from-amber-500/10 via-dark-800 to-red-500/10 border border-gold-500/40 shadow-2xl">'''

new_calculator_markup = '''            <!-- Korean Sentiment Kinetic Calculator: LCC Baggage Penalty vs Free Korea Direct Delivery -->
            <div class="mt-8 p-6 sm:p-8 rounded-3xl bg-white border-2 border-amber-300 shadow-2xl space-y-6">
                <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 pb-6 border-b border-stone-200">
                    <div class="space-y-2">
                        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs font-black tracking-wider uppercase border border-red-200">
                            <i class="fa-solid fa-plane-circle-exclamation text-red-600"></i>
                            <span>한국인 여행객 공감 100% 귀국 수하물 팩트체크</span>
                        </div>
                        <h3 class="text-xl sm:text-2xl font-black text-stone-900">
                            🧳 LCC 공항 수하물 초과요금 폭탄 피하는 스마트 직배송 계산기
                        </h3>
                        <p class="text-xs sm:text-sm text-stone-600 max-w-2xl leading-relaxed">
                            제주항공·진에어·티웨이·비엣젯 15kg 기본 수하물 초과 시 <strong class="text-red-600 font-black bg-red-50 px-1 py-0.5 rounded border border-red-200">1kg당 15,000원 벌금</strong>이 부과됩니다. 무겁게 들고 가지 마시고 호텔에서 주문하면 한국 집 문 앞으로 무료 직배송됩니다.
                        </p>
                    </div>

                    <!-- Live Real-Time Ticker (High Contrast) -->
                    <div class="bg-stone-950 border-2 border-amber-400 rounded-2xl p-4 flex items-center space-x-3.5 flex-shrink-0 shadow-lg">
                        <span class="w-3 h-3 rounded-full bg-amber-400 animate-ping"></span>
                        <div class="text-xs">
                            <div class="text-amber-400 font-black flex items-center gap-1">
                                <i class="fa-solid fa-bell"></i>
                                <span id="mainLiveTickerTime">방금 전</span>
                            </div>
                            <div class="font-bold text-white mt-0.5" id="mainLiveTickerText">
                                [소나시 노보텔 304호] 10+2 세트 로비 배달 접수
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Slider and Comparison -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 pt-2 items-center">
                    <div class="lg:col-span-6 space-y-3">
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-stone-700 font-bold">기념품 구매 예상 무게:</span>
                            <span class="text-xl font-black text-amber-600"><span id="mainWeightVal">5</span> kg</span>
                        </div>
                        <input type="range" min="2" max="15" value="5" step="1" id="mainWeightSlider"
                               class="w-full accent-amber-500 cursor-pointer h-3 bg-stone-200 rounded-lg"
                               oninput="updateMainBaggageCalc(this.value)">
                        <div class="flex justify-between text-[11px] text-stone-500 font-bold">
                            <span>가벼운 단품 (2kg)</span>
                            <span>10+2 1박스 (5kg)</span>
                            <span>2세트 (10kg)</span>
                            <span>초과 한도 (15kg)</span>
                        </div>
                    </div>

                    <div class="lg:col-span-6 grid grid-cols-1 sm:grid-cols-2 gap-3.5">
                        <!-- Penalty Box (Alert Red) -->
                        <div class="p-4 rounded-2xl bg-red-50 border-2 border-red-200 space-y-1">
                            <div class="text-[11px] font-bold text-red-700 flex items-center justify-between">
                                <span>LCC 공항 현장 초과 벌금</span>
                                <i class="fa-solid fa-triangle-exclamation"></i>
                            </div>
                            <div class="text-2xl font-black text-red-600" id="mainPenaltyDisplay">₩75,000원</div>
                            <div class="text-[10px] text-red-500 font-medium">공항 카운터에서 생돈 낭비</div>
                        </div>

                        <!-- Fruit Farm Free Shipping (Mango Highlight) -->
                        <div class="p-4 rounded-2xl bg-amber-500 text-stone-950 border border-amber-600 space-y-1 shadow-md shadow-amber-500/20">
                            <div class="text-[11px] font-bold text-stone-900 flex items-center justify-between">
                                <span>FRUIT FARM 항공 직배송</span>
                                <i class="fa-solid fa-circle-check"></i>
                            </div>
                            <div class="text-2xl font-black text-stone-950">₩0원 (완전 무료)</div>
                            <div class="text-[11px] text-stone-950 font-black" id="mainSavingsDisplay">$100 결제 시 ₩75,000원 즉시 절약!</div>
                        </div>
                    </div>
                </div>
            </div>'''

# Find entire calculator block
calc_start_idx = text.find('<!-- Korean Sentiment Kinetic Calculator:')
calc_end_idx = text.find('</section>', calc_start_idx)

if calc_start_idx != -1 and calc_end_idx != -1:
    # replace calculator
    text = text[:calc_start_idx] + new_calculator_markup + '\n        </div>\n    ' + text[calc_end_idx:]
    print("2. Redesigned LCC Baggage Calculator to clean high contrast card!")
else:
    print("Warning: could not locate calculator section bounds")

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Competitor and calculator updates completed!")
