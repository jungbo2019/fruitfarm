import urllib.request
import json
import os

headers = {'User-Agent': 'FruitFarmBot/1.0 (fruitfarm@example.com)'}

targets = [
    {
        'file': 'static/images/products/passionfruit.jpg',
        'query': 'Passiflora edulis sliced ripe fruit',
        'fallback_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Passion_fruit_-_whole_and_halved.jpg/640px-Passion_fruit_-_whole_and_halved.jpg'
    },
    {
        'file': 'static/images/products/cashew.jpg',
        'query': 'Roasted cashew nuts in bowl',
        'fallback_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Cashews_in_bowl.jpg/640px-Cashews_in_bowl.jpg'
    },
    {
        'file': 'static/images/products/macadamia.jpg',
        'query': 'Macadamia nuts raw and shelled',
        'fallback_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Macadamia_nuts.jpg/640px-Macadamia_nuts.jpg'
    },
    {
        'file': 'static/images/products/longan.jpg',
        'query': 'Dimocarpus longan fruit peeled',
        'fallback_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Longan_fruit.jpg/640px-Longan_fruit.jpg'
    }
]

for t in targets:
    url = t['fallback_url']
    dest = t['file']
    print(f"Downloading authentic image for {dest} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(dest, 'wb') as f:
                f.write(data)
            print(f"Success: {dest} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {dest}: {e}")
