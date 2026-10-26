with open(r'E:\fruitfarm\templates\admin\login.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """            <div class="inline-block bg-amber-100 text-amber-900 text-xs font-black px-3.5 py-1 rounded-full border border-amber-300">
                푸꾸옥 플래그십 보안 관제 시스템
            </div>"""

if target in content:
    content = content.replace(target, '')
    print("Exact target match removed.")
else:
    import re
    content = re.sub(r'<div class="inline-block bg-amber-100[\s\S]*?</div>', '', content)
    print("Regex match removed.")

with open(r'E:\fruitfarm\templates\admin\login.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved login.html.")
