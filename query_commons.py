import urllib.request
import json
import urllib.parse

def search_wikimedia(query):
    endpoint = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": "6", # File:
        "gsrlimit": "3",
        "prop": "imageinfo",
        "iiprop": "url|mime",
        "iiurlwidth": "640",
        "format": "json"
    }
    url = f"{endpoint}?{urllib.parse.urlencode(params)}"
    headers = {'User-Agent': 'FruitFarmStoreBot/2.0 (contact@fruitfarm.example)'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for page_id, info in pages.items():
                imageinfo = info.get('imageinfo', [])
                if imageinfo:
                    thumburl = imageinfo[0].get('thumburl') or imageinfo[0].get('url')
                    if thumburl:
                        return thumburl
    except Exception as e:
        print(f"Error for {query}: {e}")
    return None

queries = {
    'gold_mango_180.jpg': 'File:Dried mango slices food.jpg OR Dried mango',
    'gold_mango_400.jpg': 'File:Dried mango strips.jpg OR Dehydrated mango',
    'passionfruit.jpg': 'Passiflora edulis fruit cut halved',
    'cashew.jpg': 'Anacardium occidentale roasted cashew nuts in bowl',
    'longan.jpg': 'Dimocarpus longan fruit bunch',
    'dragonfruit.jpg': 'Pitaya red dragon fruit sliced',
    'papaya.jpg': 'Dried papaya slices food',
    'macadamia.jpg': 'Macadamia integrifolia nuts raw shelled'
}

for dest, q in queries.items():
    print(f"Querying {dest}: {q}...")
    img_url = search_wikimedia(q)
    print(f"  -> Result: {img_url}")
