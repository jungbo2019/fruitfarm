with open(r'E:\fruitfarm\templates\admin\dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

value_chain_html = '''
    <!-- 9-STAGE FULL E-COMMERCE VALUE CHAIN & MASTER OPERATION SOP -->
    <div class="bg-gradient-to-br from-stone-950 via-stone-900 to-stone-950 text-white p-6 sm:p-7 rounded-3xl border border-stone-800 shadow-xl space-y-5">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 pb-3 border-b border-stone-800">
            <div>
                <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-400 text-[10px] font-black uppercase tracking-wider mb-1 border border-amber-500/30">
                    <i class="fa-solid fa-arrows-split-up-and-left text-amber-400"></i>
                    <span>END-TO-END E-COMMERCE VALUE CHAIN ARCHITECTURE</span>
                </div>
                <h3 class="text-xl font-black text-white">
                    FRUIT FARM 9단계 이커머스 통합 밸류체인 관제 로드맵
                </h3>
                <p class="text-xs text-stone-300 mt-0.5">
                    SNS 광고 유입부터 현지 모객, FEFO 재고 출고, 리조트 2시간 퀵, 사후관리 및 귀국 재구매까지 한눈에 직관적으로 운영합니다.
                </p>
            </div>
            <div class="flex items-center gap-2">
                <a href="{{ url_for('admin_operations') }}" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-stone-950 rounded-xl text-xs font-black transition shadow flex items-center gap-1.5">
                    <i class="fa-solid fa-play text-xs"></i>
                    <span>인터랙티브 SOP 가이드</span>
                </a>
            </div>
        </div>

        <!-- 9 Pipeline Steps Horizontal Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-3 lg:grid-cols-9 gap-2.5 text-xs">
            <!-- Step 1: SNS Ads -->
            <a href="{{ url_for('admin_marketing') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">01. SNS 광고</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">인스타/네이버</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">릴스, 스토리, 카페 내돈내산 바이럴 소재 배포</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>소재 생성기 &rarr;</span>
                </div>
            </a>

            <!-- Step 2: Acquisition -->
            <a href="{{ url_for('admin_guides') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">02. 모객 유치</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">가이드 RS 25%</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">전담 가이드 제휴 링크 & 무료 시식 샘플 배포</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>파트너 관리 &rarr;</span>
                </div>
            </a>

            <!-- Step 3: Checkout -->
            <a href="{{ url_for('admin_orders') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">03. 주문 결제</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">$100+ 무료배송</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">10+2 세트 유도 및 원화/달러 자동 환산</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>결제 검증 &rarr;</span>
                </div>
            </a>

            <!-- Step 4: Inventory -->
            <a href="{{ url_for('admin_inventory_scan') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">04. 재고 FEFO</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">바코드 스캔 출고</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">180일 유통기한 선입선출 및 진공 포장 검수</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>FEFO 스캐너 &rarr;</span>
                </div>
            </a>

            <!-- Step 5: Logistics -->
            <a href="{{ url_for('admin_orders') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">05. 운송 분기</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">퀵 vs 항공 직배송</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">푸꾸옥 2시간 퀵 라이더 vs 한국 항공 직송</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>라이더 배차 &rarr;</span>
                </div>
            </a>

            <!-- Step 6: Situation -->
            <a href="{{ url_for('admin_control_center') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">06. 상황 관제</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">디스코드 & GPS</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">실시간 디스코드 푸시 및 라이더 이동 위치 관제</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>실시간 관제 &rarr;</span>
                </div>
            </a>

            <!-- Step 7: Progress -->
            <a href="{{ url_for('admin_orders') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">07. 진행여부</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">5단계 파이프라인</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">접수 ➔ 검수 ➔ 배차 ➔ 이동 ➔ 로비전달</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>단계 전진 &rarr;</span>
                </div>
            </a>

            <!-- Step 8: Post-purchase -->
            <a href="{{ url_for('admin_crm') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">08. 사후관리</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">100% 안심보증</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">파손 시 무상 맞교환 및 만족도 해피콜</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>고객 케어 &rarr;</span>
                </div>
            </a>

            <!-- Step 9: Reorder -->
            <a href="{{ url_for('admin_crm') }}" class="p-3 rounded-2xl bg-stone-900/90 border border-stone-800 hover:border-amber-400 transition flex flex-col justify-between group">
                <div>
                    <span class="text-[10px] font-mono text-amber-400 font-bold block">09. 추가매출</span>
                    <h5 class="font-black text-stone-100 group-hover:text-amber-400 text-xs mt-1">귀국 재구매 LTV</h5>
                    <p class="text-[10px] text-stone-400 mt-1 line-clamp-2">귀국 30일차 $15 쿠폰 & VIP 정기배송 특전</p>
                </div>
                <div class="mt-2 text-[10px] text-amber-400/80 font-bold flex items-center justify-between">
                    <span>LTV 센터 &rarr;</span>
                </div>
            </a>
        </div>
    </div>
'''

if '9-STAGE FULL E-COMMERCE VALUE CHAIN' not in content:
    target = '<!-- Charts Row -->'
    if target in content:
        content = content.replace(target, value_chain_html + "\n\n    " + target)
        with open(r'E:\fruitfarm\templates\admin\dashboard.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Injected 9-stage value chain into dashboard.html")
    else:
        print("Target 'Charts Row' not found")
else:
    print("Already injected into dashboard.html")
