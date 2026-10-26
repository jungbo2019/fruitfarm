import re

with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Competitor Headers for Strict Legal Compliance (Fair Trade & Advertising Laws)
text = text.replace(
    '<th class="py-4 px-4 w-1/5 text-stone-500">푸꾸옥 킹콩마트 (즈엉동/소나시)</th>',
    '<th class="py-4 px-4 w-1/5 text-stone-500">푸꾸옥 시내 대형마트 (시판 유통품)</th>'
)
text = text.replace(
    '<th class="py-4 px-4 w-1/5 text-stone-500">즈엉동·소나시 야시장 (로컬 가판)</th>',
    '<th class="py-4 px-4 w-1/5 text-stone-500">재래시장 로컬 야시장 (노점 가판)</th>'
)
text = text.replace(
    '<th class="py-4 px-4 w-1/5 text-stone-500">추후 진입 모방업체 (단순 소매상)</th>',
    '<th class="py-4 px-4 w-1/5 text-stone-500">일반 기념품점 (외주 위탁 소매점)</th>'
)

# 2. Add Legal Compliance Footnote to Comparison Section
legal_note = """
            <div class="mt-4 p-3 rounded-xl bg-stone-100/80 border border-stone-200 text-[11px] text-stone-500 flex items-start space-x-2">
                <i class="fa-solid fa-scale-balanced text-amber-600 mt-0.5 flex-shrink-0"></i>
                <div class="leading-relaxed">
                    <strong>[공정거래 및 표시광고법 준수 고지]</strong> 상기 비교는 베트남 시중 유통 건망고의 원재료 표시사항(통상 정제설탕 5~10% 첨가) 및 푸꾸옥 현지 물류 특성을 사실에 근거하여 객관적으로 정리한 것이며, 당사 제품은 설탕 무첨가(No Added Sugar) 및 식물검역법·관세청 소액면세 규정을 엄격히 준수합니다.
                </div>
            </div>
"""

# Insert legal note right after the competitor table closing tag
table_close = '</table>\n            </div>'
if table_close in text and legal_note.strip() not in text:
    text = text.replace(table_close, table_close + '\n' + legal_note)
    print("Legal compliance footnote added.")
else:
    print("Table close pattern check...")

with open(r'E:\fruitfarm\templates\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html with legal compliance!")
