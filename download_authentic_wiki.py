import urllib.request
import json
import urllib.parse

from get_wiki_exact import get_wiki_file

files = {
    'static/images/products/gold_mango_180.jpg': 'Dried_Mango_Slices.JPG',
    'static/images/products/gold_mango_400.jpg': 'Dried_Mango_Slices.JPG',
    'static/images/products/passionfruit.jpg': 'Passion_fruits_-_whole_and_halved.jpg',
    'static/images/products/cashew.jpg': 'Cashews.jpg',
    'static/images/products/longan.jpg': 'Longan_fruits.jpg',
    'static/images/products/dragonfruit.jpg': 'A_half_cut_Pitaya_(Red_dragon_fruit)_in_West_Bengal,_India.jpg',
    'static/images/products/papaya.jpg': 'Papaya_cross_section_BNC.jpg',
    'static/images/products/macadamia.jpg': 'Macadamia_nuts.jpg'
}

for dest, wiki_name in files.items():
    url = get_wiki_file(wiki_name)
    print(f"{dest} -> {url}")
    if url:
        req = urllib.request.Request(url, headers={'User-Agent': 'FruitFarmStoreBot/2.0 (contact@fruitfarm.example)'})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                with open(dest, 'wb') as f:
                    f.write(data)
                print(f"Successfully downloaded {dest}: {len(data)} bytes")
        except Exception as e:
            print(f"Error downloading {dest}: {e}")
