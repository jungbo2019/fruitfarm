with open(r'E:\fruitfarm\templates\admin\marketing.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('viralOutput')
print("Position:", idx)
# print line number
lines = text[:idx].splitlines()
print("Line number:", len(lines))
