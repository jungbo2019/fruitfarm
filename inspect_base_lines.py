with open('templates/base.html', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(555, min(580, len(lines))):
    print(f"L{i+1}: {lines[i].strip().encode('ascii', errors='replace').decode('ascii')}")
