with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect hero section
hero_start = text.find('<!-- 1. Hero Section')
if hero_start == -1:
    hero_start = text.find('<section class="relative min-h-[580px]')

hero_end = text.find('</section>', hero_start)
print("Hero section length:", hero_end - hero_start)
print(text[hero_start:hero_start+1000].encode('ascii', errors='replace').decode('ascii'))
