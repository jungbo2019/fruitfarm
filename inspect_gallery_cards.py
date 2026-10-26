with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

gallery_start = text.find('id="store-gallery"')
gallery_end = text.find('</section>', gallery_start)
print(text[gallery_start:gallery_end].encode('ascii', errors='replace').decode('ascii'))
