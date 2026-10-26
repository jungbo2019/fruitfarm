# 1. Update templates/base.html
with open(r'E:\fruitfarm\templates\base.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

target_base = "<li>• 실시간 상담: 카카오톡 채널 @fruitfarm</li>"
replace_base = """<li>• 실시간 상담: 카카오톡 채널 @fruitfarm</li>
                    <li>• 공식 커뮤니티: <a href="{{ settings.get('discord_invite_url', 'https://discord.gg/Kym2WKGDX') }}" target="_blank" class="text-[#5865F2] hover:underline font-bold inline-flex items-center gap-1.5"><i class="fa-brands fa-discord text-sm"></i> 디스코드 커뮤니티</a></li>"""

if target_base in base_html and 'discord_invite_url' not in base_html:
    base_html = base_html.replace(target_base, replace_base)
    with open(r'E:\fruitfarm\templates\base.html', 'w', encoding='utf-8') as f:
        f.write(base_html)
    print("Updated templates/base.html with discord link")
else:
    print("base.html already updated or target not found")

# 2. Update templates/admin/base_admin.html
with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

target_admin = """            <a href="{{ url_for('index') }}" target="_blank" class="flex items-center space-x-2 text-stone-400 hover:text-amber-400 px-3 py-2 rounded-lg transition font-bold">
                <i class="fa-solid fa-arrow-up-right-from-square"></i>
                <span>고객 쇼핑몰 바로가기</span>
            </a>"""

replace_admin = """            <a href="{{ url_for('index') }}" target="_blank" class="flex items-center space-x-2 text-stone-400 hover:text-amber-400 px-3 py-2 rounded-lg transition font-bold">
                <i class="fa-solid fa-arrow-up-right-from-square"></i>
                <span>고객 쇼핑몰 바로가기</span>
            </a>
            <a href="{{ settings.get('discord_invite_url', 'https://discord.gg/Kym2WKGDX') }}" target="_blank" class="flex items-center space-x-2 text-[#5865F2] hover:text-[#7983f5] px-3 py-2 rounded-lg transition font-bold">
                <i class="fa-brands fa-discord text-sm"></i>
                <span>디스코드 관제 채널</span>
            </a>"""

if target_admin in admin_html and 'discord_invite_url' not in admin_html:
    admin_html = admin_html.replace(target_admin, replace_admin)
    with open(r'E:\fruitfarm\templates\admin\base_admin.html', 'w', encoding='utf-8') as f:
        f.write(admin_html)
    print("Updated templates/admin/base_admin.html with discord link")
else:
    print("admin_base.html already updated or target not found")
