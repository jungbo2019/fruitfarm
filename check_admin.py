import urllib.request, re

with urllib.request.urlopen('http://127.0.0.1:5000/admin/products') as resp:
    html = resp.read().decode('utf-8')

titles = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL)
print("=== TITLES ===")
for t in titles:
    clean = re.sub('<[^<]+?>', '', t).strip()
    print('TITLE:', repr(clean))

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print('\n=== IMAGES ===', len(imgs))
for img in imgs:
    print('IMG:', img)

# Also check for duplicate images
from collections import Counter
counts = Counter(imgs)
print('\n=== DUPLICATE IMAGES ===')
for img, count in counts.items():
    if count > 1:
        print(f"DUPLICATE ({count}x): {img}")
