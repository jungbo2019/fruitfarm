path = r"E:\fruitfarm\templates\index.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

target = 'href="https://maps.google.com"'
replacement = 'href="https://www.google.com/maps/search/?api=1&query=Sonasea+Shopping+Center+Phu+Quoc" target="_blank" rel="noopener noreferrer"'

if target in text:
    text = text.replace(target, replacement)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("SUCCESS: Google Maps URL updated with exact Sonasea Phu Quoc location query!")
else:
    print("Target not found!")
