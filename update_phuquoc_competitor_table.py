import re

with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_thead = """<th class="py-4 px-4 w-1/5">비교 항목</th>
                            <th class="py-4 px-4 w-1/5 text-slate-400">재래시장 (즈엉동 야시장)</th>
                            <th class="py-4 px-4 w-1/5 text-slate-400">대형마트 (롯데마트/킹콩마트)</th>
                            <th class="py-4 px-4 w-1/5 text-slate-300">엘스토어 (L-Store 다낭)</th>
                            <th class="py-4 px-4 w-1/5 bg-gold-500/20 text-gold-300 font-black border-l border-gold-500/40">FRUIT FARM 푸꾸옥 2호점</th>"""

new_thead = """<th class="py-4 px-4 w-1/5">비교 핵심 기준</th>
                            <th class="py-4 px-4 w-1/5 text-stone-500">푸꾸옥 킹콩마트 (즈엉동/소나시)</th>
                            <th class="py-4 px-4 w-1/5 text-stone-500">즈엉동·소나시 야시장 (로컬 가판)</th>
                            <th class="py-4 px-4 w-1/5 text-stone-500">추후 진입 모방업체 (단순 소매상)</th>
                            <th class="py-4 px-4 w-1/5 bg-amber-500/10 text-amber-900 font-black border-l border-amber-400">★ FRUIT FARM 푸꾸옥 2호점</th>"""

text = text.replace("재래시장 (즈엉동 야시장)", "푸꾸옥 킹콩마트 (즈엉동/소나시)")
text = text.replace("대형마트 (롯데마트/킹콩마트)", "즈엉동·소나시 야시장 (로컬 가판)")
text = text.replace("엘스토어 (L-Store 다낭)", "추후 진입 모방업체 (단순 소매상)")
text = text.replace("비교 항목", "비교 핵심 기준")
text = text.replace("왜 야시장이나 대형마트가 아닌 푸룻팜인가?", "푸꾸옥 현지 업체 및 추후 진입업체 전수 비교")
text = text.replace("베트남 현지 재래시장, 롯데마트, 엘스토어(L-Store)와 당사 FRUIT FARM의 실제 비교 매트릭스입니다.", "푸꾸옥 킹콩마트, 즈엉동/소나시 야시장, 그리고 추후 생길 모방 소매점들과 당사 FRUIT FARM 푸꾸옥 2호점의 실질적 격차를 사실에 기반하여 투명하게 공개합니다.")

# Update row 1:
text = text.replace("HACCP 없음, 야외 상온 노출, 설탕 범벅 저질 원육", "Vinahe 등 시판 건망고 대부분 <strong>정제 설탕 5~10% 절임</strong> (인공 단맛)")
text = text.replace("시판 공장형 대량 유통, 방부제 첨가 제품 다수", "출처 불명 비닐 소분, 설탕 범벅, 당도 불균일")
text = text.replace("자체 위생 포장, 오가닉 컨셉 부티크", "도매상 설탕 절임 제품 납품받아 라벨만 교체")
text = text.replace("★ HACCP 호치민 직영공장 100% 무설탕 저온건조", "★ 호치민 직영 HACCP 공장 <strong>100% 무설탕 (NO SUGAR) 저온건조</strong> · 순수 16.5 Brix 특등급 생망고만 사용")

# Update row 2:
text = text.replace("식물검역 불합격 적발 시 몰수 폐기 및 과태료 위험", "무거운 박스를 직접 운반 (공항 15kg 초과 벌금 1kg당 1.5만원 고객 부담)")
text = text.replace("수하물 반입 가능하나 직접 운반 책임", "포장 부실로 캐리어 내 짓눌림 및 파손 위험")
text = text.replace("가공품 수하물 반입 허용 (항공 직배송 미지원)", "한국 직배송 물류망 전무 (현장 포장만 지원)")
text = text.replace("★ 관세청 $150 면세 + 검역 100% 무사통관 보증", "★ <strong>$100 이상 한국 자택 무료 직배송</strong> · 공항 캐리어 무게 부담 0kg (수하물 초과벌금 ZERO)")

# Update row 3:
text = text.replace("배송 불가, 직접 들고 이동 (수하물 15kg 초과운임 직격탄)", "일반 휴대품 반입 (세관/검역 문제 발생 시 고객 본인 책임)")
text = text.replace("현지 리조트 배달(Speed L), 한국 직배송 불가", "비위생 비닐 포장 검역 불합격 적발 시 몰수 폐기 위험")
text = text.replace("매장 직접 픽업 위주", "정식 통관 라이선스 부재로 항공 직배송 통관 불가")
text = text.replace("★ $100이상 한국 자택 무료 직배송 + 당일 2시간 룸배달", "★ <strong>식물검역법 정식 수출입 승인 + 대한민국 관세청 $150 소액면세 100% 무사통관 보증</strong>")

with open(r'E:\fruitfarm\templates\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Phu Quoc competitor matrix successfully!")
