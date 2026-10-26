import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Color Palette: Deep Slate Obsidian & Champagne Gold
    BG_COLOR = RGBColor(11, 17, 32)        # #0B1120
    SURFACE_COLOR = RGBColor(22, 30, 49)   # #161E31
    SURFACE_BORDER = RGBColor(39, 51, 78)  # #27334E
    GOLD = RGBColor(230, 162, 60)          # #E6A23C
    GOLD_LIGHT = RGBColor(253, 226, 170)   # #FDE2AA
    WHITE = RGBColor(255, 255, 255)
    GRAY_LIGHT = RGBColor(203, 213, 225)   # #CBD5E1
    GRAY_MUTED = RGBColor(148, 163, 184)   # #94A3B8
    GREEN_ACCENT = RGBColor(16, 185, 129)  # #10B981
    BLUE_ACCENT = RGBColor(56, 189, 248)   # #38BDF8
    RED_ACCENT = RGBColor(248, 113, 113)   # #F87171

    store_img_dir = r"E:\fruitfarm\static\images\store"
    exterior_path = os.path.join(store_img_dir, "store_exterior.png")
    shelves_path = os.path.join(store_img_dir, "store_shelves_promo.jpg")
    tasting_path = os.path.join(store_img_dir, "store_interior_tasting.jpg")

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.color.rgb = BG_COLOR
        return bg

    def add_header(slide, title, category, page_num):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8), Inches(0.4))
        tf_c = cat_box.text_frame
        tf_c.word_wrap = True
        p_c = tf_c.paragraphs[0]
        p_c.text = f"FRUIT FARM 푸꾸옥 2호점 사업계획서  |  {category.upper()}"
        p_c.font.size = Pt(11)
        p_c.font.bold = True
        p_c.font.color.rgb = GOLD

        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(10), Inches(0.7))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = WHITE

        p_box = slide.shapes.add_textbox(Inches(11.8), Inches(0.4), Inches(1), Inches(0.4))
        tf_p = p_box.text_frame
        p_p = tf_p.paragraphs[0]
        p_p.alignment = PP_ALIGN.RIGHT
        p_p.text = f"{page_num} / 9"
        p_p.font.size = Pt(11)
        p_p.font.color.rgb = GRAY_MUTED

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide (표지)
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.8), Inches(0.12), Inches(3.8))
    bar.fill.solid()
    bar.fill.fore_color.rgb = GOLD
    bar.line.fill.background()

    tbox = s1.shapes.add_textbox(Inches(1.3), Inches(1.6), Inches(7.2), Inches(4.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "FRUIT FARM PHU QUOC 2호점 (VƯỜN HOA QUẢ)"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = GOLD

    p1 = tf1.add_paragraph()
    p1.text = "온·오프라인 옴니채널 사업계획서\n및 가이드 이중가격제 운영 전략"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p1.space_before = Pt(10)
    p1.space_after = Pt(16)

    p2 = tf1.add_paragraph()
    p2.text = "• 소나시 12가 실제 쇼룸 거점 기반 옴니채널\n• 타업체(엘스토어·롯데마트) 실증 비교 & 차별화\n• 가이드 B2B 수수료(RS 25%) 이중가격제 시스템\n• PC 바코드 선입선출(FEFO) 스마트 재고관리 & SNS 바이럴"
    p2.font.size = Pt(12)
    p2.font.color.rgb = GRAY_LIGHT

    # Real Store Photo on Cover
    if os.path.exists(exterior_path):
        s1.shapes.add_picture(exterior_path, Inches(8.8), Inches(1.8), width=Inches(3.8))

    meta_bg = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(6.0), Inches(11.3), Inches(0.8))
    meta_bg.fill.solid()
    meta_bg.fill.fore_color.rgb = SURFACE_COLOR
    meta_bg.line.color.rgb = SURFACE_BORDER
    
    mtbox = s1.shapes.add_textbox(Inches(1.2), Inches(6.05), Inches(11.0), Inches(0.6))
    mtf = mtbox.text_frame
    mp = mtf.paragraphs[0]
    mp.text = "사업장: SV2A - V07 Khu Sonasea Bãi Trường, Phú Quốc (소나시 12가)  |  전화: +84 386 074 755  |  2026 Q4 전략본"
    mp.font.size = Pt(11)
    mp.font.color.rgb = GRAY_MUTED

    # -------------------------------------------------------------
    # SLIDE 2: Real Store Infrastructure (실제 매장 인프라)
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "푸꾸옥 2호점 실제 쇼룸 인프라 및 입지 경쟁력", "Physical Showroom", 2)

    # Left: Store Photos
    if os.path.exists(shelves_path):
        s2.shapes.add_picture(shelves_path, Inches(0.8), Inches(1.8), width=Inches(3.6))
    if os.path.exists(tasting_path):
        s2.shapes.add_picture(tasting_path, Inches(0.8), Inches(4.3), width=Inches(3.6))

    # Right: Operational Highlights
    rc = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.7), Inches(1.8), Inches(7.8), Inches(5.0))
    rc.fill.solid()
    rc.fill.fore_color.rgb = SURFACE_COLOR
    rc.line.color.rgb = SURFACE_BORDER

    tbr = rc.text_frame
    tbr.word_wrap = True

    p = tbr.paragraphs[0]
    p.text = "소나시 바이쯔엉(Sonasea 12가) 직영 쇼룸의 4대 핵심 자산"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GOLD
    p.space_after = Pt(12)

    assets = [
        ("최고급 리조트 벨트 최적의 입지", "노보텔, 풀만, 인터컨티넨탈, 베스트웨스턴 등 한국인 여행객 밀집 특급 리조트 도보 5분 거리. 소나시 야시장 메인 스트리트 입지로 자연스러운 워킹 트래픽 유입."),
        ("상시 위생 무료 시식 라운지 운영", "원목 & 라탄 테이블에서 골드망고, 건용안, 과일청 전 품목을 구매 전 시식. 시식을 통한 압도적 품질 확인이 1인당 $100 세트 구매 전환율 70% 이상 견인."),
        ("현장 정찰제 프로모션 (180g 10+2 / 400g 5+1)", "재래시장의 불투명한 흥정과 달리, 진열대 전면 정찰제 태그 부착. 매장 구매와 온라인 주문의 가격 일원화로 신뢰도 100% 확보."),
        ("가이드 전용 웰컴 라운지 & 무료 샘플 수령처", "푸꾸옥 현지 가이드 및 인솔자가 편하게 방문하여 노쇼핑/쇼핑1회 팀 무료 샘플팩을 수령하고 25% RS 정산 내역을 현장에서 즉시 확인 가능.")
    ]

    for title, desc in assets:
        p = tbr.add_paragraph()
        p.text = f"✔ {title}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.space_before = Pt(6)

        p = tbr.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = GRAY_LIGHT
        p.space_before = Pt(2)

    # -------------------------------------------------------------
    # SLIDE 3: Market & Pain Points
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "시장 환경 분석 & 관광객 3대 핵심 페인포인트", "Market & Pain Points", 3)

    pain_points = [
        ("01", "항공사 위탁수하물 15kg 엄격 제한", "LCC 항공사(비엣젯, 진에어, 제주항공 등)의 무료 위탁수하물 15kg 규제로 인해, 현지에서 대량 선물 구매 시 1kg당 1.5만~2만원의 막대한 초과운임 발생.", "해결책: $100 이상 구매 시 한국 집 앞 100% 무료 직배송 (Zero Baggage 캐리어 부담 제거)"),
        ("02", "식물검역법 생망고 국내 반입 절대 금지", "대한민국 식물방역법상 생망고 등 생과일은 검역 금지 품목으로, 인천공항 적발 시 전량 폐기 몰수 및 최대 300만원 과태료 처분 대상.", "해결책: HACCP 인증 호치민 공장 정식 가공 밀봉 건과일 & 과일청 ($150 면세 합법 세관 통관)"),
        ("03", "재래시장(야시장/한시장)의 위생 불신 & 바가지", "설탕 범벅 저질 망고, 파리/먼지 노출, 포장 갈이, 저울 무게 속임수, 카드 결제 거부로 인한 한국인 관광객의 지속적인 피로감 및 불만 누적.", "해결책: 100% 무설탕 저온건조 골드망고 정찰제 + 상시 시식존 + 카드/계좌이체 영수증 발급")
    ]

    for i, (num, title, desc, sol) in enumerate(pain_points):
        x = Inches(0.8 + i * 3.9)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.7), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE_COLOR
        card.line.color.rgb = SURFACE_BORDER

        tb = s3.shapes.add_textbox(x + Inches(0.2), Inches(2.0), Inches(3.3), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = num
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = RED_ACCENT

        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.space_before = Pt(8)
        p.space_after = Pt(12)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(11)
        p.font.color.rgb = GRAY_LIGHT
        p.space_after = Pt(16)

        p = tf.add_paragraph()
        p.text = sol
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = GREEN_ACCENT

    # -------------------------------------------------------------
    # SLIDE 4: Competitor Matrix
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "타업체 심층 비교 분석 및 차별화 전략 매트릭스", "Competitor Matrix", 4)

    rows, cols = 6, 5
    table_shape = s4.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8))
    table = table_shape.table
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(2.3)
    table.columns[2].width = Inches(2.3)
    table.columns[3].width = Inches(2.3)
    table.columns[4].width = Inches(2.6)

    matrix_data = [
        ["구분 / 평가 항목", "재래시장 (즈엉동 야시장)", "대형마트 (롯데마트/킹콩)", "엘스토어 (L-Store 다낭)", "FRUIT FARM 푸꾸옥 2호점"],
        ["위생 & 가공 인증", "HACCP 부재, 야외 상온노출\n설탕 다량 첨가, 비위생", "시판 공장형 대량 유통\n방부제·설탕 첨가 다수", "자체 포장 프리미엄화\n오가닉 컨셉, 청결 매장", "★ HACCP 인증 호치민 공장\n100% 무설탕 저온건조 공법"],
        ["가격 및 정찰제", "흥정 필수, 바가지 성행\n카드 불가 (현금만 수취)", "정찰제, 영수증 발급\n선물용 번들 할인 미흡", "정찰제, 여행카페 3% 할인\n패키지 고급화로 객단가 ↑", "★ $100 프로모션 (10+2 / 5+1)\n단품 10$ 완전 정찰제 & 투명성"],
        ["물류 및 배송 편의", "배달 불가, 직접 휴대 운반\n수하물 무게 초과 직격탄", "Speed L 앱 배송 (숙소 로비)\n한국 직배송 불가 (수하물 限)", "시내 픽업 위주\n한국 항공 택배 서비스 제한적", "★ 한국 무료 직배송 (Zero-Baggage)\n+ 푸꾸옥 리조트 당일 2시간 배송"],
        ["가이드 제휴 (B2B RS)", "개별 흥정 리베이트 (불투명)\n정산 분쟁 다수 발생", "가이드 수수료 일절 없음\n(B2B 유인책 전무)", "여행사 제휴 바우처 모델\n(사전 협약 가이드 일부)", "★ 이중 가격제 & 25% 즉시 정산\n가이드 전용 링크/QR 시스템화"],
        ["체험 및 쇼핑 편의", "위생 문제로 시식 기피\n언어 소통 불편", "시식 제한적, 직원 응대 부족\n장바구니형 쇼핑", "무료 시음/시식 바 완비\n한국어 전담 직원 상주", "★ 전메뉴 무료 시식 + 맞춤 DIY\n가이드 사전 무료 샘플팩 공급"]
    ]

    for r_idx, row in enumerate(matrix_data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(10)
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = GOLD if c_idx == 4 else SURFACE_COLOR
                p.font.color.rgb = BG_COLOR if c_idx == 4 else WHITE
                p.font.bold = True
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(30, 42, 68) if c_idx == 4 else RGBColor(18, 24, 38)
                p.font.color.rgb = GOLD_LIGHT if c_idx == 4 else GRAY_LIGHT
                p.font.bold = (c_idx == 4)

    # -------------------------------------------------------------
    # SLIDE 5: Dual Pricing & B2B RS Model
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "이중 가격제(Dual Pricing) 및 가이드 B2B 수수료(RS) 구조", "Dual Pricing & B2B RS", 5)

    c_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    c_card.fill.solid()
    c_card.fill.fore_color.rgb = SURFACE_COLOR
    c_card.line.color.rgb = SURFACE_BORDER

    tfc = c_card.text_frame
    tfc.word_wrap = True

    p = tfc.paragraphs[0]
    p.text = "1. 일반 관광객 노출 화면 (B2C)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE_ACCENT

    points_c = [
        "소비자 정상 판매가 노출 및 가치 제안",
        "• 기획 세트 소비자 정가: $100.00 (₩138,000 / 10+2 세트)",
        "• $100 이상 결제 시: 한국 자택 무료 직배송 혜택 자동 적용",
        "• 푸꾸옥 리조트 배달: 그랩 퀵으로 2시간 내 로비 무료 배송",
        "• 면세 보증: 1인당 $150 관세청 소액면세 한도 내 안전 통관",
        "• 가이드 커미션 정보 완벽 차단: 손님 화면에는 순수 정가와 사은 혜택만 노출되어 브랜드 신뢰도 100% 확보"
    ]
    for i, pt in enumerate(points_c):
        p = tfc.add_paragraph()
        p.text = pt
        p.font.size = Pt(12 if i == 0 else 11)
        p.font.color.rgb = GRAY_MUTED if i == 0 else GRAY_LIGHT
        p.space_after = Pt(10 if i == 0 else 4)

    g_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    g_card.fill.solid()
    g_card.fill.fore_color.rgb = SURFACE_COLOR
    g_card.line.color.rgb = GOLD

    tfg = g_card.text_frame
    tfg.word_wrap = True

    p = tfg.paragraphs[0]
    p.text = "2. 가이드 파트너 전용 화면 (B2B RS)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GOLD

    points_g = [
        "공급 원가 + 실시간 25% 수수료 자동 누적",
        "• 가이드 B2B 공급가: $75.00 (₩103,500) | 마진 25% 보장",
        "• 실시간 RS 적립금: 세트당 $25.00 (₩34,500) 즉시 누적",
        "• 나만의 손님 전용 주문 링크 발급: (?ref=GUIDE_KIM)",
        "  - 손님이 링크로 주문 시, 손님은 $100 정가만 보고 가이드 장부로 자동 수수료 적립",
        "• 실시간 정산 원장: 관리자 페이지 연동으로 당일 동화(VND)/한화(KRW) 즉시 결산 지원",
        "• 노쇼핑/쇼핑1회 팀 지원: 10개들이 무료 맛보기 샘플팩 무제한 공급"
    ]
    for i, pt in enumerate(points_g):
        p = tfg.add_paragraph()
        p.text = pt
        p.font.size = Pt(12 if i == 0 else 11)
        p.font.color.rgb = GRAY_MUTED if i == 0 else (GOLD_LIGHT if "25%" in pt or "$75" in pt else GRAY_LIGHT)
        p.space_after = Pt(10 if i == 0 else 4)

    # -------------------------------------------------------------
    # SLIDE 6: Operations & Barcode FEFO WMS
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "스마트 물류 운영 체계 & PC 바코드 FEFO 선입선출", "Operations & FEFO WMS", 6)

    ops_steps = [
        ("STEP 01", "호치민 공장 입고 & 바코드 등록", "호치민 직영 HACCP 공장에서 생산 직후 푸꾸옥 2호점 입고. 입고일시 및 유통기한(EXP) 기반 로트 바코드 자동 매핑 (8936...)", "입고 LOT 등록"),
        ("STEP 02", "FEFO 기반 선입선출 자동 배정", "PC 바코드 스캐너를 찍는 순간, 유통기한이 가장 임박한 로트(선도 관리 최우선)부터 자동 감산. 재고 오출고 및 유통기한 경과 0% 달성.", "FEFO 자동 감산"),
        ("STEP 03", "푸꾸옥 리조트 당일 배송 (2시간)", "현지 여행객 리조트(빈펄, 프리미어빌리지, 인터컨티넨탈 등) 로비로 그랩 퀵 배송. 객실 냉장 보관 및 선물 포장 완료 전달.", "로컬 2시간 딜리버리"),
        ("STEP 04", "한국 직배송 & 무사통관 풀필먼트", "개인통관고유부호(P번호) 자동 검증 + 관세청 면세 150$ 미만 패키징. 항공 특송으로 귀국일정에 맞춰 고객 집 앞 문앞 배송.", "Zero-Baggage 3일 배송")
    ]

    for i, (step, title, desc, badge) in enumerate(ops_steps):
        x = Inches(0.8 + i * 2.95)
        box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
        box.fill.solid()
        box.fill.fore_color.rgb = SURFACE_COLOR
        box.line.color.rgb = SURFACE_BORDER

        tf = box.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = step
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = GOLD

        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.space_before = Pt(6)
        p.space_after = Pt(10)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(11)
        p.font.color.rgb = GRAY_LIGHT
        p.space_after = Pt(16)

        p = tf.add_paragraph()
        p.text = f"▶ {badge}"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = GREEN_ACCENT

    # -------------------------------------------------------------
    # SLIDE 7: SNS & Viral Marketing
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "SNS 바이럴 및 여행자 커뮤니티 전방위 마케팅 전략", "SNS & Viral Growth", 7)

    sns_strategies = [
        ("네이버 여행 카페 제휴", "푸꾸옥고스트 · 체크인푸꾸옥 · 다낭도깨비", "• 제휴 등급 혜택: 카페 회원 전용 5% 추가 할인 or 미니 과일청 1병 증정\n• 무료 시식 교환권 배포: 즈엉동 매장 방문 유도 (워킹 트래픽 폭증)\n• 실제 구매자 '내돈내산' 생생 후기 작성 시 카카오페이 5천원 페이백"),
        ("인스타그램 & 틱톡 숏폼", "2030 자유여행객 & 가족 단위 여행자", "• 릴스 챌린지: '풀빌라 수영장에서 즐기는 리얼 망고청 에이드 레시피'\n• '귀국할 때 캐리어 무게 0kg 비법: 푸룻팜 한국 무료 직배송 언박싱'\n• 매월 베스트 숏폼 리뷰어 선정: 푸꾸옥 특급 리조트 숙박권 증정"),
        ("현지 가이드 네트워크 (B2B)", "하나투어 · 모두투어 · 노랑풍선 인솔자", "• 버스 탑승객 전원 웰컴 시식팩 무료 협찬 (가이드 부담 제로)\n• 1인당 QR 리플렛 배부 -> 버스 안에서 모바일 즉시 주문 유도\n• 주문 발생 즉시 가이드 카카오톡으로 실시간 25% 수수료 적립 알림"),
        ("카카오톡 채널 & 재구매", "귀국 후 한국 거주 기구매 고객 (리텐션)", "• 통관 진행 상황 & 배송 조회 카카오 알림톡 실시간 전송 (신뢰도 극대화)\n• 귀국 30일 후 '베트남 여행의 감동 다시 느끼기' 재구매 10% 쿠폰 발송\n• 계절별 제철 열대과일(망고스틴, 두리안 건과) 사전 예약 판매")
    ]

    for i, (channel, target, action) in enumerate(sns_strategies):
        row, col = i // 2, i % 2
        x = Inches(0.8 + col * 5.9)
        y = Inches(1.8 + row * 2.5)

        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.7), Inches(2.3))
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE_COLOR
        card.line.color.rgb = SURFACE_BORDER

        tf = card.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = f"{i+1}. {channel}  |  {target}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = GOLD

        p = tf.add_paragraph()
        p.text = action
        p.font.size = Pt(10)
        p.font.color.rgb = GRAY_LIGHT
        p.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 8: Financials
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "일·월·년 재무 예측 및 월 매출 1.2억원 달성 로드맵", "Financial Plan", 8)

    fc = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9))
    fc.fill.solid()
    fc.fill.fore_color.rgb = SURFACE_COLOR
    fc.line.color.rgb = SURFACE_BORDER

    tbf = fc.text_frame
    tbf.word_wrap = True

    p = tbf.paragraphs[0]
    p.text = "월간 손익 구조 분석 (월 900세트 기준)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.space_after = Pt(10)

    pnl_items = [
        ("총 매출액 (Gross Revenue)", "124,200,000원 ($90,000)", "100.0%", GOLD),
        ("제조 원가 (COGS - 호치민 공장)", "43,470,000원 ($31,500)", "35.0%", GRAY_LIGHT),
        ("가이드 B2B 수수료 (RS 25%)", "31,050,000원 ($22,500)", "25.0%", BLUE_ACCENT),
        ("국제 항공특송 & 그랩 물류비", "7,452,000원 ($5,400)", "6.0%", GRAY_LIGHT),
        ("마케팅 & 카페 제휴 비용", "6,210,000원 ($4,500)", "5.0%", GRAY_LIGHT),
        ("매장 임대료 & 인건비(현지 2명)", "3,500,000원 ($2,536)", "2.8%", GRAY_LIGHT),
        ("최종 영업이익 (Operating Profit)", "32,518,000원 ($23,564)", "26.2%", GREEN_ACCENT)
    ]

    for item, amt, pct, color in pnl_items:
        p = tbf.add_paragraph()
        p.text = f"• {item}: {amt} [{pct}]"
        p.font.size = Pt(11)
        p.font.bold = (color in [GOLD, GREEN_ACCENT])
        p.font.color.rgb = color
        p.space_before = Pt(4)

    sc = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
    sc.fill.solid()
    sc.fill.fore_color.rgb = SURFACE_COLOR
    sc.line.color.rgb = SURFACE_BORDER

    tbs = sc.text_frame
    tbs.word_wrap = True

    p = tbs.paragraphs[0]
    p.text = "매출 스케일업 마일스톤 (일·월·년)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = GOLD
    p.space_after = Pt(10)

    milestones = [
        ("일일 운영 목표 (Daily)", "하루 30세트 판매 ($3,000 / ₩4,140,000)\n• 가이드 제휴팀(20세트) + 매장 워킹/온라인(10세트)\n• 일 영업이익: 약 1,080,000원"),
        ("월간 운영 목표 (Monthly)", "월 900세트 판매 ($90,000 / ₩124,200,000)\n• 전담 가이드 파트너 30명 가동 (인당 월 25세트 유치)\n• 월 순 영업이익: 약 3,250만원 (이익률 26.2%)"),
        ("연간 운영 목표 (Yearly)", "연 10,800세트 판매 ($1,080,000 / ₩14.9억원)\n• 성수기(11월~4월) 집중 프로모션 및 나트랑 3호점 확장\n• 연간 누적 영업이익: 약 3.9억원 창출 달성")
    ]

    for title, desc in milestones:
        p = tbs.add_paragraph()
        p.text = f"▶ {title}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.space_before = Pt(8)

        p = tbs.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = GRAY_LIGHT
        p.space_before = Pt(2)

    # -------------------------------------------------------------
    # SLIDE 9: Action Plan
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "즉각 실행 30일 액션 플랜 & 핵심 관리 지표(KPI)", "Action Plan & KPI", 9)

    weeks = [
        ("WEEK 1 (Day 1 ~ 7)", "시스템 안착 & 매장 셋업", [
            "PC 바코드 스캐너 연동 완료",
            "16개 품목 바코드 태그 부착",
            "FEFO 로트별 유통기한 등록",
            "매장 무료 시식 쇼룸 세팅"
        ]),
        ("WEEK 2 (Day 8 ~ 14)", "가이드 파트너십 1차 가동", [
            "푸꾸옥 가이드 30명 네트워킹",
            "무료 샘플 키트 100세트 배포",
            "개인별 주문 QR 코드 발급",
            "B2B RS 25% 정산 체계 교육"
        ]),
        ("WEEK 3 (Day 15 ~ 21)", "온라인 바이럴 캠페인", [
            "푸꾸옥고스트 제휴 배너 게재",
            "인스타그램 릴스 체험단 20명",
            "리조트 룸 배달 퀵망 확정",
            "한국 직배송 항공 스케줄 점검"
        ]),
        ("WEEK 4 (Day 22 ~ 30)", "월 매출 1억 궤도 진입", [
            "일 판매 30세트 돌파",
            "가이드 주간 정산 리포트 발행",
            "재구매 카카오 쿠폰 발송",
            "피드백 반영 2호점 안정화"
        ])
    ]

    for i, (week, title, items) in enumerate(weeks):
        x = Inches(0.8 + i * 2.95)
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.8), Inches(4.9))
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE_COLOR
        card.line.color.rgb = SURFACE_BORDER

        tf = card.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = week
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = GOLD

        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.space_before = Pt(4)
        p.space_after = Pt(12)

        for itm in items:
            p = tf.add_paragraph()
            p.text = f"✔ {itm}"
            p.font.size = Pt(10.5)
            p.font.color.rgb = GRAY_LIGHT
            p.space_before = Pt(6)

    output_path = r"E:\fruitfarm\FRUIT_FARM_푸꾸옥2호점_사업계획서_및_운영전략.pptx"
    prs.save(output_path)
    print(f"9-Slide Presentation saved successfully: {output_path}")

if __name__ == '__main__':
    create_deck()
