import os
import re

for root, dirs, files in os.walk(r'E:\fruitfarm\templates'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                c = fp.read()
                scripts = re.findall(r'<script>([\s\S]*?)</script>', c)
                for sc in scripts:
                    lines = sc.splitlines()
                    for idx, line in enumerate(lines):
                        if line.count("'") % 2 != 0 and '`' not in line:
                            print(f"{f}:{idx+1}: {line.strip()[:80]}")
