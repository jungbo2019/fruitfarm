with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """                    <a href="{{ url_for('admin_marketing') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/marketing' %}bg-amber-500 text-stone-950 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-bullhorn text-sm"></i>
                        <span>SNS 바이럴 & 카톡 전송</span>
                    </a>"""

replacement = """                    <a href="{{ url_for('admin_marketing') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/marketing' %}bg-amber-500 text-stone-950 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-bullhorn text-sm"></i>
                        <span>SNS 바이럴 & 카톡 전송</span>
                    </a>
                    <a href="{{ url_for('admin_crm') }}" class="flex items-center space-x-3 px-3.5 py-2.5 rounded-xl transition hover:bg-stone-800 hover:text-white {% if request.path == '/admin/crm' %}bg-amber-500 text-stone-950 font-black shadow-sm{% endif %}">
                        <i class="fa-solid fa-heart text-sm"></i>
                        <span>고객 사후관리 & 재구매 CRM</span>
                    </a>"""

if target in text and 'admin_crm' not in text:
    text = text.replace(target, replacement)
    with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added admin_crm to base_admin.html")
else:
    print("Already added or target not found")
