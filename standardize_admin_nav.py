import re

# 1. Update base_admin.html navigation
with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

new_nav = """            <!-- Nav Links (Standardized 4 Categories & Consistent Design) -->
            <nav class="p-4 space-y-4 text-xs font-semibold overflow-y-auto max-h-[calc(100vh-180px)]">
                <!-- Group 1: Operations & Orders -->
                <div class="space-y-1">
                    <span class="px-3 text-[10px] uppercase tracking-wider font-bold text-stone-500 block">운영 총괄 & 파이프라인</span>
                    <a href="{{ url_for('admin_operations') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/operations' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-tower-broadcast text-sm"></i>
                        <span>1~10 마스터 관제 타워</span>
                    </a>
                    <a href="{{ url_for('admin_orders') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/orders' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-dolly text-sm"></i>
                        <span>주문 & 배송 파이프라인</span>
                    </a>
                    <a href="{{ url_for('admin_dashboard') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin' or request.path == '/admin/dashboard' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-chart-pie text-sm"></i>
                        <span>대시보드 종합 요약</span>
                    </a>
                </div>

                <!-- Group 2: Inventory & Barcode -->
                <div class="space-y-1">
                    <span class="px-3 text-[10px] uppercase tracking-wider font-bold text-stone-500 block">재고 & 물류 관리</span>
                    <a href="{{ url_for('admin_inventory_scan') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/inventory/scan' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-barcode text-sm"></i>
                        <span>PC 바코드 & FEFO 출고</span>
                    </a>
                    <a href="{{ url_for('admin_inventory_reports') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/inventory/reports' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-chart-line text-sm"></i>
                        <span>일·월·년 재고 수불부</span>
                    </a>
                    <a href="{{ url_for('admin_products') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/products' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-boxes-stacked text-sm"></i>
                        <span>상품 & 재고 관리</span>
                    </a>
                </div>

                <!-- Group 3: Financial & B2B Guides -->
                <div class="space-y-1">
                    <span class="px-3 text-[10px] uppercase tracking-wider font-bold text-stone-500 block">매출·지출 & 가이드 정산</span>
                    <a href="{{ url_for('admin_sales') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/sales' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-calculator text-sm"></i>
                        <span>월매출·지출 정산</span>
                    </a>
                    <a href="{{ url_for('admin_guides') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/guides' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-handshake-angle text-sm"></i>
                        <span>가이드 B2B 수수료 (RS)</span>
                    </a>
                    <a href="{{ url_for('admin_samples') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/samples' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-clipboard-list text-sm"></i>
                        <span>가이드 샘플 지원 접수</span>
                    </a>
                </div>

                <!-- Group 4: SNS Marketing & Customizer -->
                <div class="space-y-1">
                    <span class="px-3 text-[10px] uppercase tracking-wider font-bold text-stone-500 block">마케팅 & 시스템 설정</span>
                    <a href="{{ url_for('admin_marketing') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/marketing' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-bullhorn text-sm"></i>
                        <span>SNS 바이럴 마케팅</span>
                    </a>
                    <a href="{{ url_for('admin_design') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/design' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-palette text-sm"></i>
                        <span>디자인 & 레이아웃 CMS</span>
                    </a>
                    <a href="{{ url_for('admin_settings') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/settings' %}bg-amber-500 text-stone-900 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-gear text-sm"></i>
                        <span>매장 정보 & 환율 설정</span>
                    </a>
                </div>
            </nav>"""

nav_start = base_html.find('<nav class="p-4 space-y-1 text-xs font-semibold">')
nav_end = base_html.find('</nav>') + len('</nav>')
if nav_start != -1 and nav_end != -1:
    base_html = base_html[:nav_start] + new_nav + base_html[nav_end:]
    with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'w', encoding='utf-8') as f:
        f.write(base_html)
    print("base_admin.html navigation standardized successfully!")
else:
    print("nav markers not found in base_admin.html")
