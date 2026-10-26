with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_end = text.find('</section>')
print(text[hero_end:hero_end+1200].encode('ascii', errors='replace').decode('ascii'))
