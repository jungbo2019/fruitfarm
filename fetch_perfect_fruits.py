import urllib.request
import json
import re

def search_unsplash_photo(query):
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(query)}&per_page=5"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = data.get('results', [])
            if results:
                # get regular url
                raw_url = results[0]['urls']['regular']
                return raw_url
    except Exception as e:
        print(f"Error searching {query}: {e}")
    return None

items = {
    'passionfruit.jpg': 'sliced passion fruit fresh ripe',
    'cashew.jpg': 'roasted cashew nuts in bowl',
    'macadamia.jpg': 'macadamia nuts shelled',
    'longan.jpg': 'fresh longan fruit bunch'
}

for filename, query in items.items():
    print(f"Searching for {query}...")
    photo_url = search_unsplash_photo(query)
    if photo_url:
        dest = f"static/images/products/{filename}"
        print(f"Found! Downloading {dest} from {photo_url}...")
        req = urllib.request.Request(photo_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as r:
            content = r.read()
            with open(dest, 'wb') as f:
                f.write(content)
            print(f"Saved {dest}: {len(content)} bytes")
    else:
        print(f"Could not find photo for {query}")
