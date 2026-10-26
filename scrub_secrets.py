import re

# 1. Clean templates/index.html
with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove guide-dual-pricing-card elements
text = re.sub(r'<div class="guide-dual-pricing-card.*?</div>\s*</div>', '', text, flags=re.DOTALL)
text = re.sub(r'<div class="guide-dual-pricing-card.*?</div>', '', text, flags=re.DOTALL)

# Remove the sample section entirely
sample_sec_pattern = r'\{#\s*-+\s*SECTION:\s*SAMPLE\s*-+\s*#\}.*?\{#\s*-+\s*SECTION:'
m = re.search(sample_sec_pattern, text, flags=re.DOTALL)
if m:
    text = text[:m.start()] + '{# -------- SECTION:' + text[m.end():]
    print('Scrubbed sample section from index.html!')
else:
    # Try alternative
    s_idx = text.find("{% elif s == 'sample' %}")
    if s_idx != -1:
        e_idx = text.find("{% elif s ==", s_idx + 10)
        if e_idx == -1:
            e_idx = text.find("{% endif %}", s_idx + 10)
        text = text[:s_idx] + text[e_idx:]
        print('Scrubbed sample section by elif index!')

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Clean templates/base.html
with open('templates/base.html', 'r', encoding='utf-8') as f:
    btext = f.read()

# Remove guide modal
gm_start = btext.find('<!-- Guide Access Modal -->')
if gm_start != -1:
    gm_end = btext.find('<!-- Cart Drawer Modal -->')
    if gm_end == -1:
        gm_end = btext.find('<footer')
    btext = btext[:gm_start] + btext[gm_end:]
    print('Scrubbed guide modal from base.html!')

# Remove guide JS alerts and functions from customer view
btext = re.sub(r'function activateGuideCode\(.*?\n        \}', '// guide mode removed from retail', btext, flags=re.DOTALL)
btext = re.sub(r'function applyGuideModeUI\(.*?\n        \}', '// guide mode removed from retail', btext, flags=re.DOTALL)
btext = re.sub(r'function copyCustomerLink\(.*?\n        \}', '// guide mode removed from retail', btext, flags=re.DOTALL)

# In Footer, replace "가이드 B2B 파트너십" column with "고객 안심 품질 보증"
old_footer_guide = '''                <div>
                    <h4 class="text-white font-black text-xs uppercase tracking-wider mb-3">가이드 B2B 파트너십</h4>
                    <p class="text-[11px] text-slate-400 leading-relaxed mb-3">
                        푸꾸옥 현지 여행사 및 프리랜서 가이드님을 위한 공급가 전용 발주 시스템과 결제 건당 25% 실시간 정산 파트너십을 상시 운영합니다.
                    </p>
                    <button onclick="openGuideModal()" class="text-xs text-gold-400 hover:text-gold-300 font-bold flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-handshake"></i>
                        <span>파트너 전용 모드 전환</span>
                    </button>
                </div>'''

new_footer_guide = '''                <div>
                    <h4 class="text-stone-900 font-black text-xs uppercase tracking-wider mb-3">품질 보증 & 고객 지원</h4>
                    <p class="text-[11px] text-stone-500 leading-relaxed mb-3">
                        호치민 직영 HACCP 가공 시설에서 생산된 100% 무설탕 저온건조 특산품만을 정직하게 엄선하여 배송 중 파손이나 통관 문제 시 100% 무상 재발송을 보증합니다.
                    </p>
                    <div class="text-xs text-stone-700 font-bold flex items-center space-x-2">
                        <i class="fa-solid fa-shield-check text-amber-500"></i>
                        <span>100% 고객 안심 보증제 운영</span>
                    </div>
                </div>'''

if old_footer_guide in btext:
    btext = btext.replace(old_footer_guide, new_footer_guide)
    print('Scrubbed guide column from footer!')
else:
    # search by header
    f_idx = btext.find('가이드 B2B 파트너십')
    if f_idx != -1:
        f_start = btext.rfind('<div>', 0, f_idx)
        f_end = btext.find('</div>', f_idx)
        f_end = btext.find('</div>', f_end + 1)
        btext = btext[:f_start] + new_footer_guide + btext[f_end+6:]
        print('Scrubbed guide column by slice!')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(btext)

print('ALL B2B SECRETS SCRUBBED CLEAN!')
