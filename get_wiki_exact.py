import urllib.request
import json

def get_wiki_file(filename):
    endpoint = "https://commons.wikimedia.org/w/api.php"
    params = f"?action=query&titles=File:{urllib.parse.quote(filename)}&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json"
    req = urllib.request.Request(endpoint + params, headers={'User-Agent': 'FruitFarmStoreBot/2.0 (contact@fruitfarm.example)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pinfo in pages.items():
                if 'imageinfo' in pinfo:
                    return pinfo['imageinfo'][0].get('thumburl') or pinfo['imageinfo'][0].get('url')
    except Exception as e:
        print(f"Error for {filename}: {e}")
    return None

test_files = [
    "Dried_Mango_Slices.JPG",
    "Passion_fruit_-_whole_and_halved.jpg",
    "Cashews_in_bowl.jpg",
    "Macadamia_nuts.jpg",
    "Longan_fruit.jpg",
    "A_half_cut_Pitaya_(Red_dragon_fruit)_in_West_Bengal,_India.jpg",
    "Papaya_cross_section_BNC.jpg"
]

for tf in test_files:
    u = get_wiki_file(tf)
    print(f"{tf} -> {u}")
