with open(r'E:\fruitfarm\templates\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function updateBuilderRegular')
if idx != -1:
    print(text[idx:idx+1200])
