with open(r'E:\fruitfarm\templates\admin\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

matrix_html = '''    <!-- 4-TIER MERCHANDISING PRIORITY MATRIX & FEFO RULES -->
    <div class="bg-stone-50 p-6 rounded-3xl border border-stone-200 space-y-4">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 pb-3 border-b border-stone-200">
            <div>
                <span class="text-[10px] font-black text-amber-600 uppercase tracking-widest">MERCHANDISING SOP & PRIORITIES</span>
                <h4 class="font-black text-base text-stone-900">FRUIT FARM 상품 관리 4대 우선순위 & FEFO 재고 원칙</h4>
                <p class="text-xs text-stone-500">어떤 상품을 먼저 전면에 내세우고 재고를 관리해야 하는지 명확한 운영 기준입니다.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-[11px] font-bold text-stone-600 bg-white px-3 py-1 rounded-full border border-stone-300">FEFO 180일 선입선출</span>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
            <!-- Priority 1 -->
            <div class="p-4 rounded-2xl bg-white border-2 border-amber-400 shadow-sm space-y-2">
                <div class="flex justify-between items-center">
                    <span class="px-2 py-0.5 rounded-full bg-amber-500 text-stone-950 font-black text-[10px]">최우선순위 1위</span>
                    <span class="text-[10px] font-bold text-amber-800">AOV $100+ 견인</span>
                </div>
                <h5 class="font-black text-stone-900 text-sm">10+2 기획선물세트</h5>
                <p class="text-[11px] text-stone-500 leading-relaxed">
                    한국 자택 무료 직배송($100 이상) 조건을 충족시키는 핵심 패키지. 전체 매출의 65% 이상을 차지하므로 최상단에 상시 고정 진열합니다.
                </p>
                <div class="pt-1 text-[10px] font-bold text-stone-700">권장 안전재고: 150세트 이상</div>
            </div>

            <!-- Priority 2 -->
            <div class="p-4 rounded-2xl bg-white border border-stone-200 shadow-sm space-y-2">
                <div class="flex justify-between items-center">
                    <span class="px-2 py-0.5 rounded-full bg-stone-900 text-white font-black text-[10px]">핵심 시그니처 2위</span>
                    <span class="text-[10px] font-bold text-stone-500">시식 전환율 88%</span>
                </div>
                <h5 class="font-black text-stone-900 text-sm">100% 무설탕 골드망고 3종</h5>
                <p class="text-[11px] text-stone-500 leading-relaxed">
                    푸꾸옥 매장 무료 시식 시 구매 전환율이 가장 높은 시그니처 아이템. 설탕 무첨가 저온건조 특허 기술로 차별화합니다.
                </p>
                <div class="pt-1 text-[10px] font-bold text-stone-700">권장 안전재고: 각 300봉 이상</div>
            </div>

            <!-- Priority 3 -->
            <div class="p-4 rounded-2xl bg-white border border-stone-200 shadow-sm space-y-2">
                <div class="flex justify-between items-center">
                    <span class="px-2 py-0.5 rounded-full bg-stone-100 text-stone-700 font-bold text-[10px]">단가/구색 3위</span>
                    <span class="text-[10px] font-bold text-stone-500">선물 완성도 제고</span>
                </div>
                <h5 class="font-black text-stone-900 text-sm">프리미엄 통 견과류 2종</h5>
                <p class="text-[11px] text-stone-500 leading-relaxed">
                    HACCP 통캐슈넛, 통마카다미아 등 건망고와 함께 선물용 바구니를 구성하는 필수 구색 상품으로 객단가를 보강합니다.
                </p>
                <div class="pt-1 text-[10px] font-bold text-stone-700">권장 안전재고: 각 100봉 이상</div>
            </div>

            <!-- Priority 4 -->
            <div class="p-4 rounded-2xl bg-white border border-stone-200 shadow-sm space-y-2">
                <div class="flex justify-between items-center">
                    <span class="px-2 py-0.5 rounded-full bg-stone-100 text-stone-700 font-bold text-[10px]">고객경험 4위</span>
                    <span class="text-[10px] font-bold text-stone-500">참여형 만족도</span>
                </div>
                <h5 class="font-black text-stone-900 text-sm">DIY 10+2 골라담기</h5>
                <p class="text-[11px] text-stone-500 leading-relaxed">
                    고객이 원하는 12봉을 마음대로 조합할 수 있는 인터랙티브 빌더. 개별 단품 대비 이탈률을 40% 이상 낮춰줍니다.
                </p>
                <div class="pt-1 text-[10px] font-bold text-stone-700">원클릭 프리셋 빌더 연동</div>
            </div>
        </div>
    </div>
'''

if '4-TIER MERCHANDISING PRIORITY MATRIX' not in content:
    target = '    <!-- Products Grid / Cards'
    if target in content:
        content = content.replace(target, matrix_html + "\n\n" + target)
        with open(r'E:\fruitfarm\templates\admin\products.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated products.html with 4-tier merchandising matrix.")
    else:
        print("Target not found in products.html")
else:
    print("Already updated products.html")
