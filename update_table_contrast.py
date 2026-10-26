with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix competitor section title
text = text.replace(
    'text-2xl sm:text-4xl font-black text-white mt-1">{{ settings.get(\'text_competitor_title\'',
    'text-2xl sm:text-4xl font-black text-stone-900 mt-1">{{ settings.get(\'text_competitor_title\''
)

# Replace table HTML
table_start = text.find('<table class="w-full text-left text-xs')
table_end = text.find('</table>', table_start)

new_table = '''<table class="w-full text-left text-xs border border-stone-300 rounded-2xl overflow-hidden shadow-sm bg-white">
                    <thead class="bg-stone-900 text-stone-200 font-bold uppercase border-b border-stone-300">
                        <tr>
                            <th class="py-4 px-4 w-1/5 text-stone-300 font-black">비교 핵심 기준</th>
                            <th class="py-4 px-4 w-1/5 text-stone-400 font-bold">푸꾸옥 킹콩마트 (즈엉동/소나시)</th>
                            <th class="py-4 px-4 w-1/5 text-stone-400 font-bold">즈엉동·소나시 야시장 (로컬 가판)</th>
                            <th class="py-4 px-4 w-1/5 text-stone-400 font-bold">추후 진입 모방업체 (단순 소매상)</th>
                            <th class="py-4 px-4 w-1/5 bg-amber-500 text-stone-950 font-black text-sm border-l-2 border-amber-600 shadow-md">
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
                                <div class="text-amber-800 font-black text-[11px] mb-0.5">★ 호치민 직영 HACCP 공장 가공</div>
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
                                <div class="font-bold text-stone-900">식품검역법 정식 수출입 승인 + 대한민국 관세청 $150 소액면세 100% 무사통관 보증</div>
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
                </table>'''

if table_start != -1 and table_end != -1:
    text = text[:table_start] + new_table + text[table_end+8:]
    print('Competitor benchmark table updated with high contrast readable styling!')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
