crm_template = '''{% extends "admin/base_admin.html" %}

{% block page_title %}고객 사후관리(CRM) & 재구매 LTV 센터{% endblock %}

{% block admin_content %}
<div class="space-y-6">

    <!-- Header Banner -->
    <div class="bg-gradient-to-r from-stone-950 via-stone-900 to-stone-950 text-white p-6 sm:p-8 rounded-3xl border border-stone-800 shadow-xl flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6">
        <div>
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-400 text-xs font-black uppercase tracking-wider mb-2 border border-amber-500/30">
                <i class="fa-solid fa-heart text-amber-400"></i>
                <span>CUSTOMER RETENTION & LTV MULTIPLIER</span>
            </div>
            <h1 class="text-2xl sm:text-3xl font-black text-white">
                기존 고객 사후관리 (CRM) & 한국 재구매 허브
            </h1>
            <p class="text-xs sm:text-sm text-stone-300 mt-1 max-w-2xl leading-relaxed">
                푸꾸옥 현지에서 구매한 여행객이 한국 귀국 후에도 정기적으로 재구매할 수 있도록 생애주기별 맞춤 사후관리와 재구매 쿠폰을 관리합니다.
            </p>
        </div>

        <div class="flex items-center gap-3">
            <button onclick="exportCrmCsv()" class="px-5 py-3 bg-amber-500 hover:bg-amber-400 text-stone-950 rounded-2xl text-xs font-black transition flex items-center gap-2 shadow-lg border border-amber-600">
                <i class="fa-solid fa-file-csv text-sm"></i>
                <span>고객 DB 엑셀(CSV) 추출</span>
            </button>
        </div>
    </div>

    <!-- 4 KPI Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- 1. Total Customers -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm">
            <div class="flex justify-between items-start">
                <span class="text-xs font-bold text-stone-500">누적 구매 고객 수</span>
                <span class="p-2 bg-stone-100 text-stone-900 rounded-xl text-xs"><i class="fa-solid fa-user-group"></i></span>
            </div>
            <div class="text-2xl font-black text-stone-900 mt-2">{{ stats.total_customers }}명</div>
            <div class="text-[11px] text-stone-500 mt-1">푸꾸옥 현지 및 한국 직배송 고객</div>
        </div>

        <!-- 2. Repeat Customers & Rate -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm">
            <div class="flex justify-between items-start">
                <span class="text-xs font-bold text-stone-500">2회 이상 재구매 고객</span>
                <span class="p-2 bg-amber-50 text-amber-700 rounded-xl text-xs"><i class="fa-solid fa-arrows-rotate"></i></span>
            </div>
            <div class="text-2xl font-black text-amber-700 mt-2">{{ stats.repeat_customers }}명 <span class="text-sm font-bold text-stone-500">({{ stats.repeat_rate }}%)</span></div>
            <div class="text-[11px] text-stone-500 mt-1">재구매율 목표: 35.0% 이상</div>
        </div>

        <!-- 3. VIP Customers -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm">
            <div class="flex justify-between items-start">
                <span class="text-xs font-bold text-stone-500">VIP 우수 고객 ($300+)</span>
                <span class="p-2 bg-stone-950 text-amber-400 rounded-xl text-xs"><i class="fa-solid fa-crown"></i></span>
            </div>
            <div class="text-2xl font-black text-stone-900 mt-2">{{ stats.vip_customers }}명</div>
            <div class="text-[11px] text-stone-500 mt-1">누적 $300 이상 대량 구매자</div>
        </div>

        <!-- 4. Average Order Value -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm">
            <div class="flex justify-between items-start">
                <span class="text-xs font-bold text-stone-500">고객당 평균 결제액 (AOV)</span>
                <span class="p-2 bg-emerald-50 text-emerald-700 rounded-xl text-xs"><i class="fa-solid fa-wallet"></i></span>
            </div>
            <div class="text-2xl font-black text-stone-900 mt-2">${{ "%.0f"|format(stats.avg_aov) }}</div>
            <div class="text-[11px] text-stone-500 mt-1">총 고객 생애가치: ${{ "%.0f"|format(stats.total_clv) }}</div>
        </div>
    </div>

    <!-- 4 Cohort Targeting Strategy Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <!-- Cohort 1 -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm space-y-3 flex flex-col justify-between">
            <div>
                <span class="text-[10px] font-black uppercase text-amber-600 tracking-wider">COHORT 1 · 귀국 30일차</span>
                <h4 class="font-black text-stone-900 text-sm mt-0.5">망고 재구매 골든타임 케어</h4>
                <p class="text-[11px] text-stone-500 mt-1">푸꾸옥 여행 후 건망고가 다 떨어질 시점! 한국 집 문 앞 무료 직배송 $15 시크릿 쿠폰 제안.</p>
            </div>
            <button onclick="copyCohortMessage('return_30')" class="w-full py-2 bg-stone-950 hover:bg-black text-white text-xs font-black rounded-xl transition flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-solid fa-paper-plane text-amber-400"></i>
                <span>30일 재구매 문구 복사</span>
            </button>
        </div>

        <!-- Cohort 2 -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm space-y-3 flex flex-col justify-between">
            <div>
                <span class="text-[10px] font-black uppercase text-amber-600 tracking-wider">COHORT 2 · VIP 우수 고객</span>
                <h4 class="font-black text-stone-900 text-sm mt-0.5">블랙 다이아몬드 전용 특전</h4>
                <p class="text-[11px] text-stone-500 mt-1">누적 $300 이상 VIP에게 10+3 기획팩 및 호치민 직영 공장 당일 포장 특송 혜택 제공.</p>
            </div>
            <button onclick="copyCohortMessage('vip')" class="w-full py-2 bg-stone-950 hover:bg-black text-white text-xs font-black rounded-xl transition flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-solid fa-crown text-amber-400"></i>
                <span>VIP 전용 혜택문 복사</span>
            </button>
        </div>

        <!-- Cohort 3 -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm space-y-3 flex flex-col justify-between">
            <div>
                <span class="text-[10px] font-black uppercase text-amber-600 tracking-wider">COHORT 3 · 첫 구매 고객</span>
                <h4 class="font-black text-stone-900 text-sm mt-0.5">100% 안심 보증 & 포토리뷰</h4>
                <p class="text-[11px] text-stone-500 mt-1">배송 중 파손 시 100% 즉시 무상 맞교환 약속 및 네이버/인스타 후기 작성 시 $5 적립금.</p>
            </div>
            <button onclick="copyCohortMessage('welcome')" class="w-full py-2 bg-stone-950 hover:bg-black text-white text-xs font-black rounded-xl transition flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-solid fa-shield-heart text-amber-400"></i>
                <span>안심보증 알림톡 복사</span>
            </button>
        </div>

        <!-- Cohort 4 -->
        <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm space-y-3 flex flex-col justify-between">
            <div>
                <span class="text-[10px] font-black uppercase text-red-600 tracking-wider">COHORT 4 · 이탈 방지</span>
                <h4 class="font-black text-stone-900 text-sm mt-0.5">컴백 20% 시크릿 바우처</h4>
                <p class="text-[11px] text-stone-500 mt-1">마지막 주문 후 45일 이상 경과된 고객 대상 한정 특별 할인 쿠폰을 발송하여 재활성화.</p>
            </div>
            <button onclick="copyCohortMessage('winback')" class="w-full py-2 bg-stone-950 hover:bg-black text-white text-xs font-black rounded-xl transition flex items-center justify-center gap-1.5 shadow-sm">
                <i class="fa-solid fa-ticket text-amber-400"></i>
                <span>컴백 20% 문구 복사</span>
            </button>
        </div>
    </div>

    <!-- Customer Roster Table -->
    <div class="bg-white rounded-3xl border border-stone-200 shadow-sm overflow-hidden">
        <div class="p-5 border-b border-stone-200 bg-stone-50 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
            <div>
                <h3 class="text-sm font-black text-stone-900 flex items-center space-x-2">
                    <i class="fa-solid fa-address-book text-amber-500"></i>
                    <span>고객 관리 원장 & 재구매 이력</span>
                </h3>
                <p class="text-[11px] text-stone-500 mt-0.5">주문자명, 연락처, 구매 횟수, 총 결제액 및 마지막 주문일자 기준 정렬</p>
            </div>
            <span class="text-xs font-bold text-stone-700 bg-amber-100 px-3 py-1 rounded-full border border-amber-300">총 {{ customers|length }}명 관리중</span>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
                <thead class="bg-stone-50 text-stone-600 font-bold uppercase border-b border-stone-200">
                    <tr>
                        <th class="py-3 px-4">고객명</th>
                        <th class="py-3 px-4">연락처 / 카카오톡</th>
                        <th class="py-3 px-4 text-center">구매 등급</th>
                        <th class="py-3 px-4 text-right">주문 횟수</th>
                        <th class="py-3 px-4 text-right">총 구매 누적액</th>
                        <th class="py-3 px-4">최근 주문일</th>
                        <th class="py-3 px-4">주요 배송지</th>
                        <th class="py-3 px-4 text-center">사후관리 액션</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-stone-100 font-medium">
                    {% for c in customers %}
                    <tr class="hover:bg-amber-50/30 transition">
                        <td class="py-3.5 px-4 font-bold text-stone-900">
                            {{ c.customer_name }}
                        </td>
                        <td class="py-3.5 px-4 text-stone-600 font-mono">
                            <div>{{ c.customer_phone }}</div>
                            <div class="text-[10px] text-amber-700 font-semibold"><i class="fa-solid fa-comment mr-1"></i>{{ c.customer_kakao or '-' }}</div>
                        </td>
                        <td class="py-3.5 px-4 text-center">
                            {% if c.total_spent_usd >= 300 %}
                            <span class="bg-stone-950 text-amber-400 font-black text-[10px] px-2.5 py-0.5 rounded-full border border-stone-800">
                                <i class="fa-solid fa-crown mr-0.5"></i>VIP
                            </span>
                            {% elif c.order_count >= 2 %}
                            <span class="bg-amber-100 text-amber-900 font-black text-[10px] px-2.5 py-0.5 rounded-full border border-amber-300">
                                단골
                            </span>
                            {% else %}
                            <span class="bg-stone-100 text-stone-600 font-bold text-[10px] px-2.5 py-0.5 rounded-full">
                                일반
                            </span>
                            {% endif %}
                        </td>
                        <td class="py-3.5 px-4 text-right font-black text-stone-900">
                            {{ c.order_count }}회
                        </td>
                        <td class="py-3.5 px-4 text-right font-black text-amber-700">
                            ${{ "%.0f"|format(c.total_spent_usd) }}
                            <div class="text-[10px] text-stone-400 font-normal">₩{{ "{:,}".format(c.total_spent_krw) }}</div>
                        </td>
                        <td class="py-3.5 px-4 text-[11px] text-stone-500 font-mono">
                            {{ c.last_order_date }}
                        </td>
                        <td class="py-3.5 px-4 text-stone-600 text-[11px] max-w-xs truncate">
                            {{ c.delivery_address }}
                        </td>
                        <td class="py-3.5 px-4 text-center">
                            <button onclick="sendPersonalReorderMessage('{{ c.customer_name }}', '{{ c.customer_phone }}', '{{ c.customer_kakao }}')" class="px-2.5 py-1.5 bg-stone-900 hover:bg-black text-white font-bold text-[10px] rounded-lg transition shadow-sm flex items-center gap-1 mx-auto">
                                <i class="fa-solid fa-paper-plane text-amber-400"></i>
                                <span>재구매 쿠폰</span>
                            </button>
                        </td>
                    </tr>
                    {% else %}
                    <tr>
                        <td colspan="8" class="py-8 text-center text-stone-400 text-xs">
                            현재 등록된 고객 데이터가 없습니다.
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

</div>

<script>
function copyCohortMessage(cohortType) {
    let msg = '';
    const origin = window.location.origin;

    if (cohortType === 'return_30') {
        msg = `[FRUIT FARM 푸꾸옥 플래그십 귀국 재구매 감사 $15 쿠폰 🥭]\n\n고객님, 푸꾸옥에서 맛보셨던 100% 무설탕 골드망고의 달콤한 추억이 생각나시지 않나요?\n귀국 후에도 한국 자택 문 앞까지 무료 직배송으로 안전하게 받아보실 수 있는 [전용 $15 할인 쿠폰]을 드립니다!\n\n쿠폰 코드: REORDER15\n주문 링크: ${origin}\n\n100% 무설탕 저온건조 프리미엄 건망고를 한국 식탁에서 다시 만나보세요. ✨`;
    } else if (cohortType === 'vip') {
        msg = `[FRUIT FARM VIP 블랙 다이아몬드 특별 10+3 기획팩 안내 👑]\n\nFRUIT FARM 푸꾸옥 플래그십을 아껴주신 소중한 VIP 고객님께 감사드립니다.\nVIP 전용 혜택으로 10팩 주문 시 시그니처 3팩을 추가 증정하는 [10+3 프리미엄 기획팩]이 열렸습니다.\n\nVIP 전용 링크: ${origin}\n베트남 호치민 직영 HACCP 공장에서 가장 신선한 로트만 선별하여 항공 직배송해 드립니다.`;
    } else if (cohortType === 'welcome') {
        msg = `[FRUIT FARM 푸꾸옥 플래그십 100% 고객 안심 보증 안내 🌴]\n\n고객님, 주문하신 상품은 안전하게 받아보셨나요?\nFRUIT FARM은 배송 중 혹시 모를 파손이나 품질 이상 발생 시 [100% 무상 즉시 맞교환]을 약속드립니다.\n\n네이버 카페(푸꿕고스트)나 인스타그램에 시식 포토리뷰를 남겨주시면 다음 주문 시 사용 가능한 $5 포인트를 적립해 드립니다!`;
    } else if (cohortType === 'winback') {
        msg = `[FRUIT FARM 컴백 20% 시크릿 바우처가 도착했습니다 🎁]\n\n오랫동안 뵙지 못한 고객님을 위해 특별히 준비한 컴백 20% 할인권입니다.\n새롭게 입고된 통마카다미아와 무설탕 건망고 신로트를 특가에 만나보세요!\n\n바우처 코드: COMEBACK20\n주문 바로가기: ${origin}`;
    }

    navigator.clipboard.writeText(msg).then(() => {
        alert('사후관리 타겟 메시지가 복사되었습니다!\n고객 카카오톡이나 SMS로 바로 전송하세요.');
    });
}

function sendPersonalReorderMessage(name, phone, kakao) {
    const origin = window.location.origin;
    const msg = `[FRUIT FARM 푸꾸옥 플래그십] 안녕하세요, ${name} 고객님!\n푸꾸옥에서 주문하셨던 프리미엄 무설탕 건망고 맛있게 드셨나요?\n\n${name} 고객님만을 위한 [한국 자택 무료배송 $15 재구매 쿠폰]이 발급되었습니다.\n\n🎁 쿠폰 번호: REORDER-${phone ? phone.slice(-4) : 'VIP'}\n👉 바로 주문하기: ${origin}\n\n항상 최고의 프리미엄 품질만 정직하게 보내드리겠습니다. 감사합니다! 🌴`;

    navigator.clipboard.writeText(msg).then(() => {
        alert(`[${name}] 고객님을 위한 1:1 개인화 재구매 쿠폰 메시지가 복사되었습니다!\n(수신처: ${phone || kakao})`);
    });
}

function exportCrmCsv() {
    window.location.href = '/admin/sales/export-csv';
}
</script>
{% endblock %}
'''

with open(r'E:\fruitfarm\templates\admin\crm.html', 'w', encoding='utf-8') as f:
    f.write(crm_template)

print("Created templates/admin/crm.html successfully.")
