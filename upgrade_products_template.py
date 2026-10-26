with open(r'E:\fruitfarm\templates\admin\products.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the edit form inside the card
old_form = """            <!-- Edit Form in Card -->
            <form method="POST" action="{{ url_for('admin_products') }}" class="p-4 bg-stone-50 border-t border-stone-100 space-y-3 text-xs">
                <input type="hidden" name="action" value="edit">
                <input type="hidden" name="product_id" value="{{ p.id }}">

                <div class="grid grid-cols-2 gap-2">
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">가격 (USD $)</label>
                        <input type="number" step="0.5" name="price_usd" value="{{ p.price_usd }}" required class="w-full p-2 border rounded-xl bg-white font-black text-amber-700 text-sm">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">가격 (KRW ₩)</label>
                        <input type="number" name="price_krw" value="{{ p.price_krw }}" required class="w-full p-2 border rounded-xl bg-white font-bold text-stone-900 text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-2">
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">재고 수량</label>
                        <input type="number" name="stock" value="{{ p.stock }}" required class="w-full p-2 border rounded-xl bg-white font-black {% if p.stock < 25 %}border-red-400 bg-red-50 text-red-700{% else %}text-stone-900{% endif %}">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">뱃지 (예: BEST)</label>
                        <input type="text" name="badge" value="{{ p.badge or '' }}" class="w-full p-2 border rounded-xl bg-white text-stone-900">
                    </div>
                </div>

                <div class="flex items-center space-x-2 pt-1">
                    <button type="submit" class="flex-grow py-2.5 bg-stone-950 hover:bg-black text-white font-black rounded-xl transition text-xs shadow-sm">
                        수정 저장
                    </button>
                    <button type="submit" name="action" value="delete" onclick="return confirm('정말 이 상품을 삭제하시겠습니까?');" class="px-3.5 py-2.5 bg-red-50 hover:bg-red-600 hover:text-white text-red-600 border border-red-200 font-bold rounded-xl transition text-xs">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                </div>
            </form>"""

new_form = """            <!-- Edit Form in Card -->
            <form method="POST" action="{{ url_for('admin_products') }}" onsubmit="submitProductEdit(event, this)" class="p-4 bg-stone-50 border-t border-stone-100 space-y-2.5 text-xs">
                <input type="hidden" name="action" value="edit">
                <input type="hidden" name="product_id" value="{{ p.id }}">

                <div>
                    <label class="block text-[10px] font-bold text-stone-600 mb-0.5">상품명 수정</label>
                    <input type="text" name="name" value="{{ p.name }}" required class="w-full p-2 border rounded-xl bg-white font-bold text-stone-900 text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                </div>

                <div class="grid grid-cols-2 gap-2">
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">가격 (USD $)</label>
                        <input type="number" step="0.5" name="price_usd" value="{{ p.price_usd }}" required class="w-full p-2 border rounded-xl bg-white font-black text-amber-700 text-sm focus:ring-2 focus:ring-amber-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">가격 (KRW ₩)</label>
                        <input type="number" name="price_krw" value="{{ p.price_krw }}" required class="w-full p-2 border rounded-xl bg-white font-bold text-stone-900 text-sm focus:ring-2 focus:ring-amber-500 focus:outline-none">
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-2">
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">재고 수량</label>
                        <input type="number" name="stock" value="{{ p.stock }}" required class="w-full p-2 border rounded-xl bg-white font-black {% if p.stock < 25 %}border-red-400 bg-red-50 text-red-700{% else %}text-stone-900{% endif %} focus:ring-2 focus:ring-amber-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold text-stone-600 mb-0.5">뱃지 (예: BEST)</label>
                        <input type="text" name="badge" value="{{ p.badge or '' }}" placeholder="뱃지 없음" class="w-full p-2 border rounded-xl bg-white text-stone-900 font-bold focus:ring-2 focus:ring-amber-500 focus:outline-none">
                    </div>
                </div>

                <div class="flex items-center space-x-2 pt-1">
                    <button type="submit" class="submit-btn flex-grow py-2.5 bg-stone-950 hover:bg-black text-white font-black rounded-xl transition text-xs shadow-sm flex items-center justify-center gap-1.5">
                        <i class="fa-solid fa-floppy-disk text-amber-400"></i>
                        <span>수정 저장</span>
                    </button>
                    <button type="submit" name="action" value="delete" onclick="return confirm('정말 이 상품을 삭제하시겠습니까?');" class="px-3.5 py-2.5 bg-red-50 hover:bg-red-600 hover:text-white text-red-600 border border-red-200 font-bold rounded-xl transition text-xs" title="상품 삭제">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                </div>
            </form>"""

if old_form in html:
    html = html.replace(old_form, new_form)
    print("Replaced old_form in products.html")
else:
    print("old_form exact match not found, performing regex replacement")
    import re
    html = re.sub(r'<!-- Edit Form in Card -->[\s\S]*?</form>', new_form, html)

# Add JS handler for submitProductEdit at bottom of products.html
js_handler = """
<script>
function submitProductEdit(e, form) {
    e.preventDefault();
    const btn = form.querySelector('.submit-btn');
    const originalHtml = btn.innerHTML;
    
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> <span>저장 중...</span>';

    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: formData
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            btn.classList.remove('bg-stone-950', 'hover:bg-black');
            btn.classList.add('bg-emerald-600', 'text-white');
            btn.innerHTML = '<i class="fa-solid fa-check"></i> <span>수정 완료!</span>';
            
            // Show alert confirmation
            alert('상품 정보가 성공적으로 수정 저장되었습니다!');

            setTimeout(() => {
                btn.classList.remove('bg-emerald-600');
                btn.classList.add('bg-stone-950', 'hover:bg-black');
                btn.disabled = false;
                btn.innerHTML = originalHtml;
            }, 2000);
        } else {
            alert('수정 실패: ' + (data.message || '오류 발생'));
            btn.disabled = false;
            btn.innerHTML = originalHtml;
        }
    })
    .catch(err => {
        // Fallback to normal form submit if fetch fails
        form.submit();
    });
}
</script>
{% endblock %}
"""

if 'submitProductEdit' not in html:
    html = html.replace('{% endblock %}', js_handler)

with open(r'E:\fruitfarm\templates\admin\products.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated products.html with editable name and instant AJAX save handler.")
