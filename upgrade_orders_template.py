orders_template = """{% extends "admin/base_admin.html" %}

{% block page_title %}순차 주문 & 배송 파이프라인 관리 (푸꾸옥 2호점){% endblock %}

{% block admin_content %}
<div class="space-y-6">

    <!-- 1. SEQUENTIAL 5-STAGE PIPELINE SUMMARY BAR -->
    <div class="bg-white p-6 rounded-3xl border border-stone-200 shadow-sm space-y-4">
        <div class="flex justify-between items-center pb-3 border-b border-stone-100">
            <div>
                <span class="text-xs font-black text-amber-600 uppercase tracking-widest">ORDER PIPELINE</span>
                <h3 class="text-lg font-black text-stone-900 mt-0.5">판매부터 배송완료까지 5단계 순차 파이프라인</h3>
            </div>
            <span class="text-xs text-stone-500">모든 단계는 버튼 하나로 실시간 자동 연동됩니다.</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 text-xs">
            <div class="p-3.5 rounded-2xl bg-stone-50 border border-stone-200 text-center">
                <span class="text-stone-500 font-bold block mb-1">1단계: 신규 접수</span>
                <span class="text-xl font-black text-stone-800">대기중</span>
            </div>
            <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 text-center">
                <span class="text-amber-700 font-bold block mb-1">2단계: FEFO 검수</span>
                <span class="text-xl font-black text-amber-700">바코드 매칭</span>
            </div>
            <div class="p-3.5 rounded-2xl bg-blue-50 border border-blue-200 text-center">
                <span class="text-blue-700 font-bold block mb-1">3단계: 배차 출발</span>
                <span class="text-xl font-black text-blue-700">라이더 인계</span>
            </div>
            <div class="p-3.5 rounded-2xl bg-purple-50 border border-purple-200 text-center">
                <span class="text-purple-700 font-bold block mb-1">4단계: 실시간 배송</span>
                <span class="text-xl font-black text-purple-700">GPS 관제</span>
            </div>
            <div class="p-3.5 rounded-2xl bg-emerald-50 border border-emerald-200 text-center">
                <span class="text-emerald-700 font-bold block mb-1">5단계: 배송 완료</span>
                <span class="text-xl font-black text-emerald-700">로비 전달</span>
            </div>
        </div>
    </div>

    <!-- 2. ORDERS LIST TABLE -->
    <div class="bg-white rounded-3xl border border-stone-200 shadow-sm overflow-hidden">
        <div class="p-5 border-b border-stone-100 flex flex-wrap justify-between items-center gap-4">
            <h3 class="font-black text-stone-900 text-base flex items-center gap-2">
                <i class="fa-solid fa-list-check text-amber-500"></i>
                <span>실시간 주문 목록 (총 {{ orders|length }}건)</span>
            </h3>

            <div class="text-xs text-stone-500">
                각 주문의 <strong>[다음 단계 전진]</strong> 버튼을 누르면 고객 화면에 즉시 실시간 반영됩니다.
            </div>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
                <thead class="bg-stone-50 text-stone-600 font-bold border-b border-stone-200">
                    <tr>
                        <th class="p-4">주문번호 / 일시</th>
                        <th class="p-4">고객정보 / 배송지</th>
                        <th class="p-4">주문 상품</th>
                        <th class="p-4">매출 & 지출 마진</th>
                        <th class="p-4">현재 단계</th>
                        <th class="p-4 text-center">원클릭 순차 전진 & 추적</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-stone-100">
                    {% for o in orders %}
                    <tr class="hover:bg-stone-50/80 transition">
                        <!-- Order Number -->
                        <td class="p-4 align-top whitespace-nowrap">
                            <span class="font-mono font-bold text-stone-900 text-sm block">{{ o.order_number }}</span>
                            <span class="text-[11px] text-stone-400">{{ o.created_at }}</span>
                            <div class="mt-2">
                                <a href="/order/track?query={{ o.order_number }}" target="_blank"
                                   class="text-[11px] text-amber-600 hover:text-amber-700 font-bold flex items-center gap-1">
                                    <i class="fa-solid fa-map-location-dot"></i>
                                    <span>고객 실시간 지도 보기</span>
                                </a>
                            </div>
                        </td>

                        <!-- Customer & Destination -->
                        <td class="p-4 align-top max-w-xs">
                            <div class="font-bold text-stone-900 text-sm">{{ o.customer_name }}</div>
                            <div class="text-stone-500 font-mono text-xs">{{ o.customer_phone }}</div>
                            <div class="mt-1.5 flex items-center gap-1.5">
                                {% if o.delivery_type == 'direct_korea' %}
                                <span class="bg-blue-600 text-white font-bold text-[10px] px-2 py-0.5 rounded">
                                    <i class="fa-solid fa-plane mr-1"></i>한국 직배송
                                </span>
                                {% else %}
                                <span class="bg-emerald-600 text-white font-bold text-[10px] px-2 py-0.5 rounded">
                                    <i class="fa-solid fa-motorcycle mr-1"></i>푸꾸옥 로비 배달
                                </span>
                                {% endif %}
                            </div>
                            <p class="text-stone-700 text-xs mt-1 leading-relaxed">{{ o.delivery_address }}</p>
                            {% if o.rider_name and o.delivery_type != 'direct_korea' %}
                            <div class="text-[11px] text-stone-500 mt-1 font-mono">
                                🛵 기사: {{ o.rider_name }} ({{ o.rider_plate }})
                            </div>
                            {% endif %}
                        </td>

                        <!-- Items -->
                        <td class="p-4 align-top max-w-xs space-y-1">
                            {% for item in o.order_items %}
                            <div class="flex justify-between text-stone-700 text-xs">
                                <span class="truncate font-medium">{{ item.name }}</span>
                                <span class="font-bold ml-2">x{{ item.qty }}</span>
                            </div>
                            {% endfor %}
                        </td>

                        <!-- Financial Ledger per order -->
                        <td class="p-4 align-top whitespace-nowrap">
                            <div class="font-black text-stone-900 text-base">${{ "%.2f"|format(o.total_amount_usd) }}</div>
                            <div class="text-[11px] text-stone-500 mt-0.5">
                                원가 COGS: -${{ "%.2f"|format(o.cogs_usd or 45.0) }}<br>
                                배송/포장비: -${{ "%.2f"|format((o.expense_delivery_usd or 3.0) + (o.expense_packaging_usd or 1.5)) }}<br>
                                {% if o.guide_commission_usd and o.guide_commission_usd > 0 %}
                                가이드 RS: -${{ "%.2f"|format(o.guide_commission_usd) }}<br>
                                {% endif %}
                            </div>
                            <div class="text-xs font-black text-emerald-600 mt-1 pt-1 border-t border-stone-200">
                                순이익: +${{ "%.2f"|format(o.total_amount_usd - (o.cogs_usd or 45.0) - (o.expense_delivery_usd or 3.0) - (o.expense_packaging_usd or 1.5) - (o.guide_commission_usd or 0)) }}
                            </div>
                        </td>

                        <!-- Current Stage Badge -->
                        <td class="p-4 align-top whitespace-nowrap">
                            <span class="px-3 py-1.5 rounded-xl text-xs font-bold inline-block
                                {% if o.order_status == 'delivered' %}bg-emerald-100 text-emerald-800 border border-emerald-300
                                {% elif o.order_status == 'shipping' %}bg-purple-100 text-purple-800 border border-purple-300
                                {% elif o.order_status == 'dispatched' %}bg-blue-100 text-blue-800 border border-blue-300
                                {% elif o.order_status in ['checked', 'preparing'] %}bg-amber-100 text-amber-800 border border-amber-300
                                {% else %}bg-stone-100 text-stone-700 border border-stone-300{% endif %}">
                                {% if o.order_status == 'received' %}1단계: 주문 접수
                                {% elif o.order_status in ['checked', 'preparing'] %}2단계: FEFO 검수완료
                                {% elif o.order_status == 'dispatched' %}3단계: 라이더 배차출발
                                {% elif o.order_status == 'shipping' %}4단계: 실시간 이동중
                                {% elif o.order_status == 'delivered' %}5단계: 배송완료
                                {% else %}{{ o.order_status }}{% endif %}
                            </span>
                        </td>

                        <!-- Sequential 1-Click Action Button -->
                        <td class="p-4 align-top whitespace-nowrap text-center">
                            {% if o.order_status == 'received' %}
                            <form action="{{ url_for('admin_advance_order_stage') }}" method="POST">
                                <input type="hidden" name="order_id" value="{{ o.id }}">
                                <input type="hidden" name="next_stage" value="checked">
                                <button type="submit" class="w-full px-3.5 py-2 bg-amber-500 hover:bg-amber-400 text-stone-900 font-bold rounded-xl text-xs transition shadow-sm">
                                    ▶ 2단계: FEFO 검수 완료
                                </button>
                            </form>
                            {% elif o.order_status in ['checked', 'preparing'] %}
                            <form action="{{ url_for('admin_advance_order_stage') }}" method="POST">
                                <input type="hidden" name="order_id" value="{{ o.id }}">
                                <input type="hidden" name="next_stage" value="dispatched">
                                <button type="submit" class="w-full px-3.5 py-2 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl text-xs transition shadow-sm">
                                    ▶ 3단계: 라이더 배차 출발
                                </button>
                            </form>
                            {% elif o.order_status == 'dispatched' %}
                            <form action="{{ url_for('admin_advance_order_stage') }}" method="POST">
                                <input type="hidden" name="order_id" value="{{ o.id }}">
                                <input type="hidden" name="next_stage" value="shipping">
                                <button type="submit" class="w-full px-3.5 py-2 bg-purple-600 hover:bg-purple-500 text-white font-bold rounded-xl text-xs transition shadow-sm animate-pulse">
                                    ▶ 4단계: 실시간 배송중 전환
                                </button>
                            </form>
                            {% elif o.order_status == 'shipping' %}
                            <form action="{{ url_for('admin_advance_order_stage') }}" method="POST">
                                <input type="hidden" name="order_id" value="{{ o.id }}">
                                <input type="hidden" name="next_stage" value="delivered">
                                <button type="submit" class="w-full px-3.5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl text-xs transition shadow-sm">
                                    ▶ 5단계: 로비 전달 완료
                                </button>
                            </form>
                            {% else %}
                            <div class="text-xs text-emerald-600 font-bold py-1">
                                <i class="fa-solid fa-circle-check text-sm mr-1"></i>최종 완료
                            </div>
                            {% endif %}
                        </td>
                    </tr>
                    {% else %}
                    <tr>
                        <td colspan="6" class="text-center py-12 text-stone-400 text-xs">등록된 주문 내역이 없습니다.</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

</div>
{% endblock %}
"""

with open(r'E:\fruitfarm\templates\admin\orders.html', 'w', encoding='utf-8') as f:
    f.write(orders_template)

print("orders.html upgraded with sequential pipeline and financial breakdown!")
