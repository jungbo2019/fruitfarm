import re

path = r"E:\fruitfarm\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Let's find competitor section
target_section_start = "{# ---------------- SECTION: COMPETITOR MATRIX ---------------- #}"
target_section_end = "{# ---------------- SECTION: PROMO SETS ---------------- #}"

idx1 = html.find(target_section_start)
idx2 = html.find(target_section_end)

if idx1 == -1 or idx2 == -1:
    print("Could not find section boundaries!")
    exit(1)

new_competitor_section = """{# ---------------- SECTION: COMPETITOR MATRIX ---------------- #}
    {% elif s == 'competitor' and settings.get('show_competitor_matrix', '1') == '1' %}
    <section id="competitor-matrix" data-tab="quality" class="py-12 sm:py-16 bg-dark-800 border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <!-- Section Header: Clear, Narrative Title -->
            <div class="text-center max-w-3xl mx-auto mb-8 sm:mb-12">
                <span class="text-xs font-black text-gold-400 tracking-widest uppercase">{{ settings.get('text_competitor_badge', 'WHY FRUIT FARM?') }}</span>
                <h2 class="text-2xl sm:text-4xl font-black text-stone-900 mt-1 [word-break:keep-all] break-keep leading-snug">
                    왜 야시장이나 킹콩마트가 아닌<br class="sm:hidden"> <span class="text-amber-600">FRUIT FARM(후르츠팜)</span>인가?
                </h2>
                <p class="text-xs sm:text-sm text-stone-600 mt-2 [word-break:keep-all] break-keep">
                    현지 재래시장, 마트 시판 건망고와 당사 FRUIT FARM 직영 플래그십의 <strong>3대 핵심 차이점</strong>을 투명하게 안내해드립니다.
                </p>
            </div>

            <!-- =========================================================================
                 1. MOBILE INTUITIVE 3-CARD COMPARISON (Shown on Mobile, hidden on md+)
                 ========================================================================= -->
            <div class="block md:hidden space-y-4 mb-8">
                <!-- Card 1: Sugar & Processing -->
                <div class="bg-white rounded-2xl border-2 border-stone-200 p-4 shadow-sm space-y-3">
                    <div class="flex items-center justify-between pb-2 border-b border-stone-100">
                        <span class="text-xs font-black text-stone-900 flex items-center gap-1.5">
                            <i class="fa-solid fa-lemon text-amber-500"></i>
                            <span>1. 가공 방식 & 설탕 첨가</span>
                        </span>
                        <span class="text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">맛과 품질 비교</span>
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div class="bg-stone-50 p-2.5 rounded-xl border border-stone-200">
                            <div class="text-[10px] font-bold text-red-600 mb-1 flex items-center gap-1">
                                <i class="fa-solid fa-xmark"></i> 시판 마트 / 야시장
                            </div>
                            <div class="text-[11px] text-stone-600 font-medium leading-relaxed">
                                정제 설탕 5~10% 절임으로 <strong>인공적인 단맛</strong>, 출처 불명 위생 우려
                            </div>
                        </div>
                        <div class="bg-amber-50 p-2.5 rounded-xl border-2 border-amber-400">
                            <div class="text-[10px] font-black text-amber-900 mb-1 flex items-center gap-1">
                                <i class="fa-solid fa-crown text-amber-500"></i> 후르츠팜 플래그십
                            </div>
                            <div class="text-[11px] text-stone-900 font-bold leading-relaxed">
                                <strong>100% 무설탕 저온건조!</strong> 순수 16.5 Brix 특등급 생망고 천연 단맛
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 2: Airport Baggage & Shipping -->
                <div class="bg-white rounded-2xl border-2 border-stone-200 p-4 shadow-sm space-y-3">
                    <div class="flex items-center justify-between pb-2 border-b border-stone-100">
                        <span class="text-xs font-black text-stone-900 flex items-center gap-1.5">
                            <i class="fa-solid fa-plane-departure text-amber-500"></i>
                            <span>2. 귀국 수하물 & 배송 방식</span>
                        </span>
                        <span class="text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">여행 편의 비교</span>
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div class="bg-stone-50 p-2.5 rounded-xl border border-stone-200">
                            <div class="text-[10px] font-bold text-red-600 mb-1 flex items-center gap-1">
                                <i class="fa-solid fa-xmark"></i> 시판 마트 / 야시장
                            </div>
                            <div class="text-[11px] text-stone-600 font-medium leading-relaxed">
                                무거운 짐 직접 운반, 15kg 초과 시 <strong>공항 벌금 kg당 1.5만원</strong>
                            </div>
                        </div>
                        <div class="bg-amber-50 p-2.5 rounded-xl border-2 border-amber-400">
                            <div class="text-[10px] font-black text-amber-900 mb-1 flex items-center gap-1">
                                <i class="fa-solid fa-crown text-amber-500"></i> 후르츠팜 플래그십
                            </div>
                            <div class="text-[11px] text-stone-900 font-bold leading-relaxed">
                                <strong>$100 이상 한국 무료 직배송!</strong> 공항 캐리어 무게 부담 0kg 완벽 실현
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 3: Customs & Exchange Guarantee -->
                <div class="bg-white rounded-2xl border-2 border-stone-200 p-4 shadow-sm space-y-3">
                    <div class="flex items-center justify-between pb-2 border-b border-stone-100">
                        <span class="text-xs font-black text-stone-900 flex items-center gap-1.5">
                            <i class="fa-solid fa-shield-halved text-amber-500"></i>
                            <span>3. 세관 통관 및 사후 교환 보증</span>
                        </span>
                        <span class="text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">안심 보증 비교</span>
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-xs">
                        <div class="bg-stone-50 p-2.5 rounded-xl border border-stone-200">
                            <div class="text-[10px] font-bold text-red-600 mb-1 flex items-center gap-1">
                                <i class="fa-solid fa-xmark"></i> 시판 마트 / 야시장
                            </div>
                            <div class="text-[11px] text-stone-600 font-medium leading-relaxed">
                                귀국 후 변질·파손 시 연락 두절, 비위생 포장 세관 적발 폐기 위험
                            </div>
                        </div>
                        <div class="bg-amber-50 p-2.5 rounded-xl border-2 border-amber-400">
                            <div class="text-[10px] font-black text-amber-900 mb-1 flex items-center gap-1">
                                <i class="fa-solid fa-crown text-amber-500"></i> 후르츠팜 플래그십
                            </div>
                            <div class="text-[11px] text-stone-900 font-bold leading-relaxed">
                                <strong>관세청 $150 면세 100% 무사통관</strong>, 배송 중 파손 시 1:1 즉시 맞교환
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Toggle Button to show full desktop matrix on mobile if desired -->
                <div class="text-center pt-1">
                    <button type="button" onclick="document.getElementById('mobileFullTableWrapper').classList.toggle('hidden')" class="inline-flex items-center gap-1.5 text-xs font-bold text-stone-600 bg-stone-100 hover:bg-stone-200 px-4 py-2 rounded-xl transition border border-stone-300">
                        <i class="fa-solid fa-table-list text-amber-600"></i>
                        <span>상세 비교표(5개 열 전체 매트릭스) 펼쳐보기</span>
                        <i class="fa-solid fa-chevron-down text-[10px]"></i>
                    </button>
                </div>
            </div>

            <!-- =========================================================================
                 2. FULL DESKTOP TABLE (Always shown on md+, expandable on mobile)
                 ========================================================================= -->
            <div id="mobileFullTableWrapper" class="hidden md:block overflow-x-auto -mx-4 px-4 sm:mx-0 sm:px-0 mb-8">
                <!-- Mobile Swipe Guide Badge -->
                <div class="block sm:hidden mb-3">
                    <div class="bg-amber-100 text-amber-950 border border-amber-300 rounded-xl px-3.5 py-2.5 text-xs font-black flex items-center justify-between shadow-xs">
                        <span>👉 표를 좌우로 넘겨 전체 비교표를 확인하세요</span>
                        <i class="fa-solid fa-arrows-left-right text-amber-600 animate-pulse text-sm"></i>
                    </div>
                </div>
                <table class="min-w-[760px] w-full text-left text-xs border border-stone-300 rounded-2xl overflow-hidden shadow-sm bg-white [word-break:keep-all]">
                    <thead class="bg-stone-900 text-stone-200 font-bold uppercase border-b border-stone-300">
                        <tr>
                            <th class="py-4 px-3 sm:px-4 min-w-[120px] text-stone-300 font-black">비교 핵심 기준</th>
                            <th class="py-4 px-3 sm:px-4 min-w-[150px] text-stone-400 font-bold">푸꾸옥 킹콩마트<br><span class="text-[10px] text-stone-500">(즈엉동/소나시)</span></th>
                            <th class="py-4 px-3 sm:px-4 min-w-[140px] text-stone-400 font-bold">즈엉동·소나시 야시장<br><span class="text-[10px] text-stone-500">(로컬 가판)</span></th>
                            <th class="py-4 px-3 sm:px-4 min-w-[140px] text-stone-400 font-bold">추후 진입 모방업체<br><span class="text-[10px] text-stone-500">(단순 소매상)</span></th>
                            <th class="py-4 px-3 sm:px-4 min-w-[210px] bg-amber-500 text-stone-950 font-black text-sm border-l-2 border-amber-600 shadow-md">
                                <div class="flex items-center space-x-1.5">
                                    <i class="fa-solid fa-crown text-stone-950"></i>
                                    <span>FRUIT FARM 푸꾸옥 플래그십</span>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-stone-200 font-medium">
                        <tr class="hover:bg-stone-50 transition">
                            <td class="py-4 px-4 font-black text-stone-900 bg-stone-100">가공 & 위생 인증</td>
                            <td class="py-4 px-4 text-red-600 font-medium">Vinahe 등 시판 건망고 대부분 <strong>정제 설탕 5~10% 절임</strong> (인공 단맛)</td>
                            <td class="py-4 px-4 text-stone-600">출처 불명 비닐 소분, 설탕 범벅, 당도 불균일</td>
                            <td class="py-4 px-4 text-stone-600">도매상 설탕 절임 제품 납품받아 라벨만 교체</td>
                            <td class="py-4 px-4 bg-amber-50/90 text-stone-900 border-l-2 border-amber-400">
                                <div class="text-amber-800 font-black text-[11px] mb-0.5">★ 호치민 직영 HACCP 자체공장 가공</div>
                                <div class="font-bold text-stone-900">100% 무설탕 저온건조 (순수 16.5 Brix 특등급 생망고만 사용)</div>
                            </td>
                        </tr>
                        <tr class="hover:bg-stone-50 transition">
                            <td class="py-4 px-4 font-black text-stone-900 bg-stone-100">한국 세관 통관 & 검역</td>
                            <td class="py-4 px-4 text-red-600 font-medium">무거운 박스를 직접 운반 (공항 15kg 초과 벌금 1kg당 1.5만원 고객 부담)</td>
                            <td class="py-4 px-4 text-stone-600">포장 부실로 캐리어 내 짓눌림 및 파손 위험</td>
                            <td class="py-4 px-4 text-stone-600">한국 직배송 물류망 전무 (현장 포장만 지원)</td>
                            <td class="py-4 px-4 bg-amber-50/90 text-stone-900 border-l-2 border-amber-400">
                                <div class="text-amber-800 font-black text-[11px] mb-0.5">★ $100 이상 한국 무료 직배송</div>
                                <div class="font-bold text-stone-900">자택 문앞 배송 · 공항 캐리어 무게 부담 0kg (수하물 초과벌금 ZERO)</div>
                            </td>
                        </tr>
                        <tr class="hover:bg-stone-50 transition">
                            <td class="py-4 px-4 font-black text-stone-900 bg-stone-100">배송 및 물류 편의</td>
                            <td class="py-4 px-4 text-red-600 font-medium">일반 휴대품 반입 (세관/검역 문제 발생 시 고객 본인 책임)</td>
                            <td class="py-4 px-4 text-stone-600">비위생 비닐 포장 검역 불합격 적발 시 몰수 폐기 위험</td>
                            <td class="py-4 px-4 text-stone-600">정식 통관 라이선스 부재로 항공 직배송 통관 불가</td>
                            <td class="py-4 px-4 bg-amber-50/90 text-stone-900 border-l-2 border-amber-400">
                                <div class="text-amber-800 font-black text-[11px] mb-0.5">★ 정식 수출입 통관 라이선스</div>
                                <div class="font-bold text-stone-900">식품검역법 정식 수출입 승인 + 관세청 $150 소액면세 100% 무사통관 보증</div>
                            </td>
                        </tr>
                        <tr class="hover:bg-stone-50 transition">
                            <td class="py-4 px-4 font-black text-stone-900 bg-stone-100">가격 체계 & 정찰제</td>
                            <td class="py-4 px-4 text-red-600 font-medium">외국인 바가지 흥정, 카드 불가 (현금 강요)</td>
                            <td class="py-4 px-4 text-stone-600">정찰제, 카드 결제 가능, 번들 할인 미미</td>
                            <td class="py-4 px-4 text-stone-600">정찰제, 여행카페 회원 3% 할인 바우처</td>
                            <td class="py-4 px-4 bg-amber-50/90 text-stone-900 border-l-2 border-amber-400">
                                <div class="text-amber-800 font-black text-[11px] mb-0.5">★ 투명한 정찰제 & 보너스 패키지</div>
                                <div class="font-bold text-stone-900">$100 기획세트 (10+2 / 5+1) + 카드/원화 이체 지원</div>
                            </td>
                        </tr>
                        <tr class="hover:bg-stone-50 transition">
                            <td class="py-4 px-4 font-black text-stone-900 bg-stone-100">고객 안심 & 사후 보장</td>
                            <td class="py-4 px-4 text-red-600 font-medium">귀국 후 파손/변질 발생 시 교환·환불 불가</td>
                            <td class="py-4 px-4 text-stone-600">로컬 가판 특성상 구매 즉시 연락 두절, 환불 불가</td>
                            <td class="py-4 px-4 text-stone-600">자체 CS 인력 부재로 교환 처리 지연</td>
                            <td class="py-4 px-4 bg-amber-50/90 text-stone-900 border-l-2 border-amber-400">
                                <div class="text-amber-800 font-black text-[11px] mb-0.5">★ 100% 고객 안심 무상 보장</div>
                                <div class="font-bold text-stone-900">100% 무상 재발송 보증 (배송 중 파손·변질 시 즉시 1:1 맞교환)</div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- =========================================================================
                 3. SMART BAGGAGE SAVINGS CALCULATOR (Narrative Bridge)
                 ========================================================================= -->
            <div class="p-6 sm:p-8 rounded-3xl bg-white border-2 border-amber-300 shadow-2xl space-y-6">
                <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 pb-6 border-b border-stone-200">
                    <div class="space-y-2">
                        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs font-black tracking-wider uppercase border border-red-200">
                            <i class="fa-solid fa-plane-circle-exclamation text-red-600"></i>
                            <span>한국인 여행객 공감 100% 귀국 수하물 팩트체크</span>
                        </div>
                        <h3 class="text-xl sm:text-2xl font-black text-stone-900 leading-snug [word-break:keep-all] break-keep">
                            🧳 LCC 공항 수하물 초과요금 폭탄 피하는 스마트 직배송 계산기
                        </h3>
                        <p class="text-xs sm:text-sm text-stone-600 max-w-2xl leading-relaxed [word-break:keep-all] break-keep">
                            제주항공·진에어·티웨이·비엣젯 15kg 기본 수하물 초과 시 <strong class="text-red-600 font-black bg-red-50 px-1 py-0.5 rounded border border-red-200">1kg당 15,000원 벌금</strong>이 부과됩니다. 무겁게 들고 가지 마시고 호텔에서 주문하면 한국 집 문 앞으로 무료 직배송됩니다.
                        </p>
                    </div>

                    <!-- Live Real-Time Ticker (High Contrast) -->
                    <div class="bg-stone-950 border-2 border-amber-400 rounded-2xl p-4 flex items-center space-x-3.5 flex-shrink-0 shadow-lg w-full lg:w-auto">
                        <span class="w-3 h-3 rounded-full bg-amber-400 animate-ping flex-shrink-0"></span>
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
                            <div class="text-[11px] text-stone-900 font-black" id="mainSavingsDisplay">$100 결제 시 ₩75,000원 즉시 절약!</div>
                        </div>
                    </div>
                </div>

                <!-- Narrative Call-To-Action Link to $100 Packages -->
                <div class="pt-4 border-t border-stone-100 flex flex-col sm:flex-row items-center justify-between gap-3 bg-amber-50/50 p-4 rounded-2xl">
                    <div class="text-xs font-bold text-stone-800 text-center sm:text-left">
                        <i class="fa-solid fa-circle-check text-emerald-600 mr-1.5"></i>
                        <span>단 1박스만 주문해도 <strong>한국 자택 100% 무료 직배송</strong> 혜택이 적용됩니다.</span>
                    </div>
                    <a href="#promo" class="w-full sm:w-auto inline-flex items-center justify-center space-x-2 bg-stone-950 hover:bg-black text-white font-black px-6 py-3 rounded-xl text-xs transition shadow-md border border-stone-800 cursor-pointer">
                        <span>인기 $100 기획 세트 둘러보기</span>
                        <i class="fa-solid fa-arrow-down text-amber-400"></i>
                    </a>
                </div>
            </div>

            <!-- Legal Compliance Note: Placed discreetly at bottom -->
            <div class="mt-6 text-center">
                <p class="text-[10px] text-stone-400 leading-relaxed max-w-2xl mx-auto">
                    ※ <strong>[공정거래 및 표시광고법 준수 고지]</strong> 상기 비교는 베트남 시중 유통 건망고의 원재료 표시사항(통상 정제설탕 5~10% 첨가) 및 푸꾸옥 현지 물류 특성을 사실에 근거하여 객관적으로 정리한 것이며, 당사 제품은 설탕 무첨가(No Added Sugar) 및 식물검역법·관세청 소액면세 규정을 엄격히 준수합니다.
                </p>
            </div>
        </div>
    </section>
    """

html = html[:idx1] + new_competitor_section + html[idx2:]

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully rebuilt competitor section with seamless narrative flow!")
