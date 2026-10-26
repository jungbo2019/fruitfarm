with open(r'E:\fruitfarm\templates\base.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<li>• 공식 커뮤니티: <a href="{{ settings.get(\'discord_invite_url\', \'https://discord.gg/Kym2WKGDX\') }}" target="_blank" class="text-[#5865F2] hover:underline font-bold inline-flex items-center gap-1.5"><i class="fa-brands fa-discord text-sm"></i> 디스코드 커뮤니티</a></li>\n'

if target in content:
    content = content.replace(target, '')
    print("Removed target with newline.")
else:
    # Try line without trailing newline
    target_no_nl = '<li>• 공식 커뮤니티: <a href="{{ settings.get(\'discord_invite_url\', \'https://discord.gg/Kym2WKGDX\') }}" target="_blank" class="text-[#5865F2] hover:underline font-bold inline-flex items-center gap-1.5"><i class="fa-brands fa-discord text-sm"></i> 디스코드 커뮤니티</a></li>'
    if target_no_nl in content:
        content = content.replace(target_no_nl, '')
        print("Removed target without newline.")
    else:
        print("Target not found directly, performing regex check")
        import re
        content = re.sub(r'\s*<li>• 공식 커뮤니티:.*?</li>', '', content)

# Also clean duplicate "플래그십 플래그십"
content = content.replace('푸꾸옥 플래그십 플래그십 스토어', '푸꾸옥 직영 플래그십 스토어')

with open(r'E:\fruitfarm\templates\base.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved base.html")
