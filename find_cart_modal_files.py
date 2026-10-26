import os

for root, dirs, files in os.walk(r'E:\fruitfarm'):
    for f in files:
        if f.endswith(('.html', '.py', '.txt', '.bak')):
            fp = os.path.join(root, f)
            try:
                with open(fp, 'r', encoding='utf-8') as f_obj:
                    c = f_obj.read()
                    if 'id="cartModal"' in c or "id='cartModal'" in c or 'cartModal' in c:
                        print(f"File {fp}: length {len(c)}")
            except:
                pass
