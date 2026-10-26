import glob

for p in glob.glob('templates/**/*.html', recursive=True):
    with open(p, encoding='utf-8') as f:
        text = f.read()
    if '안심 쇼핑 보증' in text or '관세청 면세 한도' in text or 'FEFO 선입선출' in text:
        print(f"Found in {p}")
        idx = text.find('안심 쇼핑 보증')
        if idx == -1:
            idx = text.find('관세청 면세 한도')
        print(text[idx-50:idx+400].encode('ascii', errors='replace').decode('ascii'))
