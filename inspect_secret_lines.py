with open('templates/index.html', encoding='utf-8') as f:
    lines = f.readlines()

print("Lines 395 to 415:")
for i in range(394, min(415, len(lines))):
    print(f"L{i+1}: {lines[i].strip().encode('ascii', errors='replace').decode('ascii')}")

print("\nLines 570 to 615:")
for i in range(569, min(615, len(lines))):
    print(f"L{i+1}: {lines[i].strip().encode('ascii', errors='replace').decode('ascii')}")
