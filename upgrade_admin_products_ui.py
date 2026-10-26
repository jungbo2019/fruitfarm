import re

path = r"E:\fruitfarm\templates\admin\products.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update image container in product card
old_img_container = """                <!-- Real Fruit Image Container -->
                <div class="relative h-48 bg-stone-100 overflow-hidden">
                    <img src="{{ p.image_url }}" alt="{{ p.name }}" class="w-full h-full object-cover">
                    <span class="absolute top-3 left-3 bg-stone-950/90 text-white text-[10px] font-black px-2 py-1 rounded-md border border-stone-700">
                        {{ p.category }}
                    </span>
                    {% if p.badge %}
                    <span class="absolute top-3 right-3 bg-amber-500 text-stone-950 text-[10px] font-black px-2.5 py-1 rounded-md shadow-sm border border-amber-600">
                        {{ p.badge }}
                    </span>
                    {% endif %}
                </div>"""

new_img_container = """                <!-- Real Fruit Image Container with Direct Photo Edit -->
                <div class="relative h-48 bg-stone-100 overflow-hidden group">
                    <img id="prodImg_{{ p.id }}" src="{{ p.image_url }}" alt="{{ p.name }}" class="w-full h-full object-cover transition duration-300 group-hover:scale-105">
                    <span class="absolute top-3 left-3 bg-stone-950/90 text-white text-[10px] font-black px-2 py-1 rounded-md border border-stone-700">
                        {{ p.category }}
                    </span>
                    {% if p.badge %}
                    <span class="absolute top-3 right-3 bg-amber-500 text-stone-950 text-[10px] font-black px-2.5 py-1 rounded-md shadow-sm border border-amber-600">
                        {{ p.badge }}
                    </span>
                    {% endif %}
                    
                    <!-- Direct Photo Change Overlay Button -->
                    <label for="imgUpload_{{ p.id }}" class="absolute bottom-2.5 right-2.5 bg-stone-950/90 hover:bg-black text-white text-[11px] font-black px-3 py-1.5 rounded-xl border border-stone-600 shadow-md cursor-pointer flex items-center space-x-1.5 transition transform hover:scale-105">
                        <i class="fa-solid fa-camera text-amber-400"></i>
                        <span>사진 교체</span>
                    </label>
                    <input type="file" id="imgUpload_{{ p.id }}" accept="image/*" class="hidden" onchange="uploadProductImageFile(this, {{ p.id }})">
                </div>"""

if old_img_container in html:
    html = html.replace(old_img_container, new_img_container)
    print("1. Replaced image container with direct camera overlay button!")
else:
    print("WARNING: old_img_container not found verbatim!")

# 2. Add image_url input field in the edit form
old_form_start = """            <!-- Edit Form in Card -->
            <form method="POST" action="{{ url_for('admin_products') }}" onsubmit="submitProductEdit(event, this)" class="p-4 bg-stone-50 border-t border-stone-100 space-y-2.5 text-xs">
                <input type="hidden" name="action" value="edit">
                <input type="hidden" name="product_id" value="{{ p.id }}">

                <div>
                    <label class="block text-[10px] font-bold text-stone-600 mb-0.5">상품명 수정</label>
                    <input type="text" name="name" value="{{ p.name }}" required class="w-full p-2 border rounded-xl bg-white font-bold text-stone-900 text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                </div>"""

new_form_start = """            <!-- Edit Form in Card -->
            <form method="POST" action="{{ url_for('admin_products') }}" onsubmit="submitProductEdit(event, this)" class="p-4 bg-stone-50 border-t border-stone-100 space-y-2.5 text-xs">
                <input type="hidden" name="action" value="edit">
                <input type="hidden" name="product_id" value="{{ p.id }}">

                <!-- Direct Image Edit Field -->
                <div>
                    <div class="flex items-center justify-between mb-0.5">
                        <label class="text-[10px] font-bold text-stone-600">사진 직접 수정 (파일 업로드 / 웹 URL)</label>
                        <label for="imgUpload_{{ p.id }}" class="text-[10px] font-black text-amber-600 hover:text-amber-700 cursor-pointer flex items-center gap-1">
                            <i class="fa-solid fa-cloud-arrow-up"></i>
                            <span>내 PC 사진 업로드</span>
                        </label>
                    </div>
                    <div class="flex items-center space-x-1.5">
                        <input type="text" name="image_url" id="imgUrlInput_{{ p.id }}" value="{{ p.image_url }}" oninput="updateImagePreview({{ p.id }}, this.value)" class="w-full p-2 border rounded-xl bg-white font-mono text-[11px] text-stone-700 focus:ring-2 focus:ring-amber-500 focus:outline-none" placeholder="/static/images/products/... 또는 https://...">
                    </div>
                </div>

                <div>
                    <label class="block text-[10px] font-bold text-stone-600 mb-0.5">상품명 수정</label>
                    <input type="text" name="name" value="{{ p.name }}" required class="w-full p-2 border rounded-xl bg-white font-bold text-stone-900 text-xs focus:ring-2 focus:ring-amber-500 focus:outline-none">
                </div>"""

if old_form_start in html:
    html = html.replace(old_form_start, new_form_start)
    print("2. Added image_url text input with PC file upload link to card form!")
else:
    print("WARNING: old_form_start not found verbatim!")

# 3. Add JS functions at the end of products.html
js_scripts = """
<script>
function updateImagePreview(prodId, url) {
    const img = document.getElementById(`prodImg_${prodId}`);
    if (img && url) {
        img.src = url;
    }
}

function uploadProductImageFile(fileInput, prodId) {
    const file = fileInput.files[0];
    if (!file) return;

    // 1. Instant local preview
    const reader = new FileReader();
    reader.onload = function(e) {
        const img = document.getElementById(`prodImg_${prodId}`);
        if (img) img.src = e.target.result;
    };
    reader.readAsDataURL(file);

    // 2. Upload via AJAX FormData
    const formData = new FormData();
    formData.append('product_id', prodId);
    formData.append('image_file', file);

    const toast = document.createElement('div');
    toast.className = 'fixed bottom-5 right-5 z-50 bg-stone-900 text-amber-400 px-4 py-2.5 rounded-xl text-xs font-bold shadow-2xl flex items-center gap-2 border border-stone-700';
    toast.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i><span>새 사진 서버 업로드 중...</span>';
    document.body.appendChild(toast);

    fetch('/api/admin/product/upload-image', {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        toast.remove();
        if (data.success) {
            const urlInput = document.getElementById(`imgUrlInput_${prodId}`);
            if (urlInput) urlInput.value = data.image_url;
            const img = document.getElementById(`prodImg_${prodId}`);
            if (img) img.src = data.image_url;

            const successToast = document.createElement('div');
            successToast.className = 'fixed bottom-5 right-5 z-50 bg-emerald-600 text-white px-4 py-2.5 rounded-xl text-xs font-black shadow-2xl flex items-center gap-2 border border-emerald-400';
            successToast.innerHTML = '<i class="fa-solid fa-circle-check"></i><span>사진이 성공적으로 변경되었습니다!</span>';
            document.body.appendChild(successToast);
            setTimeout(() => successToast.remove(), 2500);
        } else {
            alert('사진 업로드 실패: ' + data.message);
        }
    })
    .catch(err => {
        toast.remove();
        alert('업로드 오류: ' + err);
    });
}

function submitProductEdit(event, form) {
    event.preventDefault();
    const btn = form.querySelector('.submit-btn');
    const origHtml = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> <span>저장 중...</span>';

    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            btn.className = btn.className.replace('bg-stone-950', 'bg-emerald-600').replace('hover:bg-black', 'hover:bg-emerald-700');
            btn.innerHTML = '<i class="fa-solid fa-check"></i> <span>수정 완료!</span>';
            setTimeout(() => {
                btn.className = btn.className.replace('bg-emerald-600', 'bg-stone-950').replace('hover:bg-emerald-700', 'hover:bg-black');
                btn.innerHTML = origHtml;
                btn.disabled = false;
            }, 2000);
        } else {
            alert('저장 실패: ' + data.message);
            btn.innerHTML = origHtml;
            btn.disabled = false;
        }
    })
    .catch(err => {
        form.submit(); // fallback to normal form submit
    });
}
</script>
"""

if "<script>" not in html or "uploadProductImageFile" not in html:
    html = html.replace("{% endblock %}", js_scripts + "\n{% endblock %}")
    print("3. Injected JavaScript uploadProductImageFile and submitProductEdit!")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML upgrade completed successfully!")
