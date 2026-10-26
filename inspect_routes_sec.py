import re

with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

routes = re.findall(r'@app\.route\([\'\"](.*?)[\'\"]', text)
print(f'Total routes: {len(routes)}')
for r in routes:
    if 'api' in r or 'admin' in r:
        print(f' - {r}')
