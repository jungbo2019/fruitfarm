modals_markup = """
    <!-- ==================== SHOPPING CART DRAWER / MODAL ==================== -->
    <div id="cartModal" class="fixed inset-0 z-50 hidden bg-black/70 backdrop-blur-xs flex justify-end">
        <div class="bg-white w-full max-w-md h-full shadow-2xl flex flex-col justify-between overflow-hidden animate-in slide-in-from-right duration-300">
            <!-- Header -->
            <div class="p-5 border-b border-stone-200 flex items-center justify-between bg-stone-50">
                <div class="flex items-center space-x-2.5">
                    <div class="w-8 h-8 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center font-black">
                        <i class="fa-solid fa-basket-shopping"></i>
                    </div>
                    <div>
                        <h3 class="font-black text-stone-900 text-base">쇼핑백 장바구니</h3>
                        <p class="text-[11px] text-stone-500">선택하신 품목을 확인하세요 (<span id="cart-item-count-badge">0개</span>)</p>
                    </div>
                </div>
                <button onclick="closeCartModal()" class="w-8 h-8 rounded-full bg-stone-200 hover:bg-stone-300 text-stone-600 flex items-center justify-center transition cursor-pointer">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <!-- Free Shipping Progress -->
            <div class="bg-amber-50 p-3.5 border-b border-amber-200/60">
                <div class="flex justify-between items-center text-xs font-black text-stone-800 mb-1.5">
                    <span id="shippingProgressText">$100 이상 주문 시 한국 무료 직배송</span>
                    <span id="shippingProgressPercent" class="text-amber-600 font-bold">0%</span>
                </div>
                <div class="w-full bg-stone-200 rounded-full h-2 overflow-hidden">
                    <div id="shippingProgressBar" class="bg-gradient-to-r from-amber-500 to-amber-600 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
                </div>
            </div>

            <!-- Cart Items List -->
            <div id="cartItemsList" class="flex-grow p-4 overflow-y-auto space-y-3">
                <!-- Rendered by JS -->
            </div>

            <!-- Footer / Totals & Checkout Button -->
            <div class="p-5 border-t border-stone-200 bg-stone-50 space-y-3">
                <div class="space-y-1.5 text-xs text-stone-600">
                    <div class="flex justify-between">
                        <span>상품 합계</span>
                        <span id="cartSubtotalUsd" class="font-bold text-stone-900">$0.00</span>
                    </div>
                    <div class="flex justify-between">
                        <span>국제 항공 배송비</span>
                        <span id="cartShippingUsd" class="font-bold text-emerald-600">무료</span>
                    </div>
                    <div class="flex justify-between text-base font-black text-stone-950 pt-2 border-t border-stone-200">
                        <span>최종 결제 예상액</span>
                        <div class="text-right">
                            <div id="cartTotalUsd" class="text-amber-600 font-black">$0.00</div>
                            <div id="cartTotalKrw" class="text-xs text-stone-500 font-bold">₩0원</div>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-2">
                    <button onclick="closeCartModal()" class="w-full py-3 rounded-xl border border-stone-300 text-stone-700 font-black text-xs hover:bg-stone-100 transition cursor-pointer">
                        계속 쇼핑하기
                    </button>
                    <button onclick="openCheckoutModal()" class="w-full py-3 rounded-xl bg-amber-500 hover:bg-amber-600 text-stone-950 font-black text-xs shadow-md shadow-amber-500/20 transition flex items-center justify-center space-x-1.5 cursor-pointer">
                        <span>주문서 작성</span>
                        <i class="fa-solid fa-arrow-right text-xs"></i>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ==================== CHECKOUT & ORDER MODAL ==================== -->
    <div id="checkoutModal" class="fixed inset-0 z-50 hidden bg-black/75 backdrop-blur-xs flex items-center justify-center p-4 overflow-y-auto">
        <div class="bg-white w-full max-w-lg rounded-3xl shadow-2xl border border-stone-200 overflow-hidden my-8 animate-in fade-in zoom-in-95 duration-200">
            <!-- Modal Header -->
            <div class="p-5 bg-stone-950 text-white flex items-center justify-between">
                <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center font-black">
                        <i class="fa-solid fa-receipt"></i>
                    </div>
                    <div>
                        <h3 class="font-black text-white text-base">주문서 작성 및 배송 정보</h3>
                        <p class="text-[11px] text-stone-400">품목 수량: <span id="cartOrderCountText">0</span>개 · 무사통관 100% 보증</p>
                    </div>
                </div>
                <button onclick="closeCheckoutModal()" class="text-stone-400 hover:text-white p-2 cursor-pointer">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>
            </div>

            <!-- Form -->
            <form onsubmit="submitFinalOrder(event)" class="p-6 space-y-4 max-h-[75vh] overflow-y-auto text-xs">
                <!-- Delivery Type Radio Selection -->
                <div>
                    <label class="block font-black text-stone-900 mb-2">배송 방식 선택 *</label>
                    <div class="grid grid-cols-2 gap-3">
                        <label id="labelDirectKorea" class="cursor-pointer border-2 border-amber-500 bg-amber-50/50 p-3 rounded-2xl flex flex-col items-center text-center transition">
                            <input type="radio" name="delivery_type" value="direct_korea" checked onchange="toggleDeliveryType(this.value)" class="sr-only">
                            <i class="fa-solid fa-plane-departure text-amber-600 text-base mb-1"></i>
                            <span class="font-black text-stone-900 text-xs">대한민국 직배송</span>
                            <span class="text-[10px] text-stone-500 mt-0.5">$100 이상 무료 항공직송</span>
                        </label>
                        <label id="labelLocalPhuquoc" class="cursor-pointer border-2 border-stone-200 bg-stone-50 p-3 rounded-2xl flex flex-col items-center text-center transition">
                            <input type="radio" name="delivery_type" value="local_phuquoc" onchange="toggleDeliveryType(this.value)" class="sr-only">
                            <i class="fa-solid fa-hotel text-stone-600 text-base mb-1"></i>
                            <span class="font-black text-stone-900 text-xs">푸꾸옥 리조트 배달</span>
                            <span class="text-[10px] text-stone-500 mt-0.5">당일 2시간 그랩 퀵 직배송</span>
                        </label>
                    </div>
                </div>

                <!-- Guide Display -->
                <div class="bg-stone-100 p-2.5 rounded-xl flex items-center justify-between text-[11px]">
                    <span class="text-stone-600 font-bold">제휴 안내:</span>
                    <span id="displayGuideCodeInOrder" class="font-mono text-stone-500">일반 고객 주문 (가이드 없음)</span>
                </div>

                <!-- Customer Details -->
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block font-bold text-stone-700 mb-1">주문자 성함 *</label>
                        <input id="custName" type="text" required placeholder="홍길동"
                               class="w-full px-3 py-2.5 border border-stone-300 rounded-xl text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block font-bold text-stone-700 mb-1">연락처 *</label>
                        <input id="custPhone" type="tel" required placeholder="010-0000-0000"
                               class="w-full px-3 py-2.5 border border-stone-300 rounded-xl text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                    </div>
                </div>

                <div>
                    <label class="block font-bold text-stone-700 mb-1">카카오톡 ID (주문 확인 및 배송 알림용) *</label>
                    <input id="custKakao" type="text" required placeholder="카카오톡 아이디 또는 휴대폰 번호"
                           class="w-full px-3 py-2.5 border border-stone-300 rounded-xl text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                </div>

                <!-- Quick Resort Selector (Shown when local_phuquoc is active) -->
                <div id="quickResortSelector" class="hidden bg-amber-50/60 p-3 rounded-2xl border border-amber-200">
                    <label class="block font-black text-amber-900 text-[11px] mb-1.5">빠른 리조트 선택 (클릭 시 자동 입력)</label>
                    <div class="flex flex-wrap gap-1.5">
                        <button type="button" onclick="selectQuickResort('소나시 노보텔 리조트')" class="px-2 py-1 bg-white border border-amber-300 rounded-lg text-[10px] font-bold text-stone-800 hover:bg-amber-100">노보텔</button>
                        <button type="button" onclick="selectQuickResort('풀만 리조트 푸꾸옥')" class="px-2 py-1 bg-white border border-amber-300 rounded-lg text-[10px] font-bold text-stone-800 hover:bg-amber-100">풀만</button>
                        <button type="button" onclick="selectQuickResort('인터컨티넨탈 푸꾸옥')" class="px-2 py-1 bg-white border border-amber-300 rounded-lg text-[10px] font-bold text-stone-800 hover:bg-amber-100">인터컨티넨탈</button>
                        <button type="button" onclick="selectQuickResort('세일링 클럽 시그니처')" class="px-2 py-1 bg-white border border-amber-300 rounded-lg text-[10px] font-bold text-stone-800 hover:bg-amber-100">세일링클럽</button>
                        <button type="button" onclick="selectQuickResort('JW 메리어트 에메랄드 베이')" class="px-2 py-1 bg-white border border-amber-300 rounded-lg text-[10px] font-bold text-stone-800 hover:bg-amber-100">JW메리어트</button>
                        <button type="button" onclick="selectQuickResort('프리미어 빌리지 푸꾸옥')" class="px-2 py-1 bg-white border border-amber-300 rounded-lg text-[10px] font-bold text-stone-800 hover:bg-amber-100">프리미어빌리지</button>
                        <button type="button" onclick="selectQuickResort('빈펄 리조트 & 스파 푸꾸옥')" class="px-2 py-1 bg-white border border-amber-300 rounded-lg text-[10px] font-bold text-stone-800 hover:bg-amber-100">빈펄</button>
                    </div>
                </div>

                <div>
                    <label id="addressLabel" class="block font-bold text-stone-700 mb-1">배송 주소 (한국 자택 도로명 주소) *</label>
                    <input id="custAddress" type="text" required placeholder="도로명 주소 및 상세 동호수를 입력하세요"
                           class="w-full px-3 py-2.5 border border-stone-300 rounded-xl text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                </div>

                <!-- Customs ID Container -->
                <div id="customsIdContainer">
                    <label class="block font-bold text-stone-700 mb-1">개인통관고유부호 (한국 직배송 시 필수) *</label>
                    <input id="custCustomsId" type="text" placeholder="P로 시작하는 13자리 (예: P123456789012)"
                           class="w-full px-3 py-2.5 border border-stone-300 rounded-xl text-xs font-mono uppercase focus:ring-2 focus:ring-amber-500 focus:outline-none">
                    <p class="text-[10px] text-stone-500 mt-1">관세청 통관을 위한 필수 기재 항목이며, 1인당 $150 소액 면세 혜택이 적용됩니다.</p>
                </div>

                <div>
                    <label class="block font-bold text-stone-700 mb-1">배송 요청 사항 (선택)</label>
                    <textarea id="custNote" rows="2" placeholder="부재 시 문 앞 보관 또는 요청사항"
                              class="w-full px-3 py-2 border border-stone-300 rounded-xl text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none"></textarea>
                </div>

                <div class="pt-3">
                    <button id="btnFinalSubmit" type="submit"
                            class="w-full py-3.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-stone-950 font-black text-sm shadow-lg shadow-amber-500/25 transition flex items-center justify-center space-x-2 cursor-pointer">
                        <i class="fa-solid fa-lock text-xs"></i>
                        <span>안심 주문 접수하기</span>
                    </button>
                    <p class="text-[10px] text-center text-stone-400 mt-2">
                        주문 접수 즉시 담당자가 카카오톡/문자로 계좌 안내 및 출고 일정을 실시간 공유해드립니다.
                    </p>
                </div>
            </form>
        </div>
    </div>
"""

path = r"E:\fruitfarm\templates\base.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

target = "<!-- ==================== 24/7 AI SMART CONCIERGE CHATBOT MODAL ==================== -->"
if target in html:
    html = html.replace(target, modals_markup + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: Added cartModal and checkoutModal to base.html!")
else:
    print("Target not found in base.html!")
