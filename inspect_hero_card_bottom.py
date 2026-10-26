with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_card_idx = text.find('안심 보증 & 특급 혜택')
print(text[hero_card_idx+1200:hero_card_idx+2200].encode('ascii', errors='replace').decode('ascii'))
