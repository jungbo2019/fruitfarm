import re

with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert Tab Bar right before the CMS section loop
tab_bar_html = """
<!-- STICKY CURATED TAB BAR (Cognitive Load Reduction - Human-Eye Focus) -->
<div class="sticky top-0 z-30 bg-[#FAF7F2]/95 backdrop-blur-md border-b border-amber-200 py-3 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex items-center justify-between gap-4">
        <div class="flex items-center space-x-1.5 sm:space-x-2 text-xs font-bold overflow-x-auto no-scrollbar py-0.5">
            <button onclick="switchMainTab('promo')" id="tab-btn-promo" class="main-tab-btn px-4 py-2 rounded-xl transition bg-amber-500 text-white font-extrabold shadow-sm flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-gift"></i>
                <span>★ $100 베스트 세트</span>
            </button>
            <button onclick="switchMainTab('builder')" id="tab-btn-builder" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-sliders"></i>
                <span>10+2 직접 담기</span>
            </button>
            <button onclick="switchMainTab('quality')" id="tab-btn-quality" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-shield-halved"></i>
                <span>품질 비교 & 수하물 계산</span>
            </button>
            <button onclick="switchMainTab('store')" id="tab-btn-store" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-store"></i>
                <span>소나시 매장 실사 & 배달</span>
            </button>
            <button onclick="switchMainTab('catalog')" id="tab-btn-catalog" class="main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap">
                <i class="fa-solid fa-boxes-stacked"></i>
                <span>전체 단품</span>
            </button>
            <button onclick="switchMainTab('all')" id="tab-btn-all" class="main-tab-btn px-3 py-2 rounded-xl transition bg-stone-100 text-stone-500 hover:text-stone-800 border border-stone-200 flex items-center gap-1 whitespace-nowrap">
                <i class="fa-solid fa-layer-group"></i>
                <span>전체 펼쳐보기</span>
            </button>
        </div>
        <div class="hidden lg:flex items-center text-xs text-amber-800 font-bold bg-amber-100/70 px-3 py-1.5 rounded-lg border border-amber-200">
            <i class="fa-solid fa-truck-fast text-amber-600 mr-1.5"></i>
            <span>$100 이상 결제 시 한국 자택 무료 직배송 (소액면세 보증)</span>
        </div>
    </div>
</div>
"""

target_hero_end = '</section>\n\n<!-- DYNAMIC CMS SECTION ORDERING LOOP -->'
if target_hero_end in content:
    content = content.replace(target_hero_end, '</section>\n' + tab_bar_html + '\n<!-- DYNAMIC CMS SECTION ORDERING LOOP -->')
    print("Tab bar inserted successfully.")
else:
    print("Target hero end not found exactly, checking alternatives...")

# 2. Add data-tab to sections
content = content.replace('<section id="store-gallery"', '<section id="store-gallery" data-tab="store"')
content = content.replace('<section id="competitor-matrix"', '<section id="competitor-matrix" data-tab="quality"')
content = content.replace('<section id="promo"', '<section id="promo" data-tab="promo"')
content = content.replace('<section id="custom-builder"', '<section id="custom-builder" data-tab="builder"')
content = content.replace('<section id="products"', '<section id="products" data-tab="catalog"')
content = content.replace('<section id="sample"', '<section id="sample" data-tab="catalog"')
content = content.replace('<section id="store-location"', '<section id="store-location" data-tab="store"')

# 3. Add switchMainTab JS logic before </script>
switch_js = """
    // Curated Human-Eye Tab Navigation Logic
    function switchMainTab(tabKey) {
        document.querySelectorAll('.main-tab-btn').forEach(btn => {
            btn.className = 'main-tab-btn px-4 py-2 rounded-xl transition bg-white text-stone-600 hover:text-stone-900 border border-stone-200 hover:border-amber-300 flex items-center gap-1.5 whitespace-nowrap';
        });
        const activeBtn = document.getElementById('tab-btn-' + tabKey);
        if (activeBtn) {
            if (tabKey === 'all') {
                activeBtn.className = 'main-tab-btn px-3 py-2 rounded-xl transition bg-stone-800 text-white font-extrabold shadow-sm flex items-center gap-1 whitespace-nowrap';
            } else {
                activeBtn.className = 'main-tab-btn px-4 py-2 rounded-xl transition bg-amber-500 text-white font-extrabold shadow-sm flex items-center gap-1.5 whitespace-nowrap';
            }
        }

        const sections = document.querySelectorAll('section[data-tab]');
        sections.forEach(sec => {
            if (tabKey === 'all' || sec.getAttribute('data-tab') === tabKey) {
                sec.style.display = 'block';
                sec.classList.remove('hidden');
            } else {
                sec.style.display = 'none';
                sec.classList.add('hidden');
            }
        });

        sessionStorage.setItem('curated_main_tab', tabKey);
    }

    // Auto-detect hash or initialize curated tab on load
    document.addEventListener('DOMContentLoaded', () => {
        const hash = window.location.hash;
        if (hash.includes('promo')) switchMainTab('promo');
        else if (hash.includes('builder')) switchMainTab('builder');
        else if (hash.includes('competitor')) switchMainTab('quality');
        else if (hash.includes('store') || hash.includes('location')) switchMainTab('store');
        else if (hash.includes('product') || hash.includes('sample')) switchMainTab('catalog');
        else {
            switchMainTab(sessionStorage.getItem('curated_main_tab') || 'promo');
        }
    });
</script>
"""

content = content.replace('</script>\n{% endblock %}', switch_js + '\n{% endblock %}')

with open(r'E:\fruitfarm\templates\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")
