with open(r'E:\fruitfarm\templates\admin\guides.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        alert('[' + activeGuideCodeForQr + '] 가이드 전용 주문 링크가 복사되었습니다:
' + link);"""

replacement = """        alert('[' + activeGuideCodeForQr + '] 가이드 전용 주문 링크가 복사되었습니다: ' + link);"""

if target in text:
    text = text.replace(target, replacement)
    with open(r'E:\fruitfarm\templates\admin\guides.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed alert in guides.html")
else:
    import re
    text = re.sub(r"alert\('\[' \+ activeGuideCodeForQr \+ '\] 가이드 전용 주문 링크가 복사되었습니다:[\r\n]+' \+ link\);",
                  r"alert('[' + activeGuideCodeForQr + '] 가이드 전용 주문 링크가 복사되었습니다: ' + link);", text)
    with open(r'E:\fruitfarm\templates\admin\guides.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed alert via regex in guides.html")
