import urllib.request
import urllib.parse
import json
import os

def get_wikimedia_photo(search_term):
    query_str = search_term + " filetype:bitmap"
    encoded = urllib.parse.quote(query_str)
    url = "https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=" + encoded + "&srlimit=6&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'FruitFarmPhuQuoc/1.0 (contact@fruitfarm.vn)'})
    try:
        res = json.loads(urllib.request.urlopen(req, timeout=10).read().decode('utf-8'))
        results = res.get('query', {}).get('search', [])
        for r in results:
            title = r['title']
            if not title.startswith('File:'):
                continue
            lower_title = title.lower()
            if any(bad in lower_title for bad in ['stamp', 'book', 'drawing', 'map', 'specimen', 'herbarium', 'chart', 'pdf']):
                continue
            # get image url
            info_url = "https://commons.wikimedia.org/w/api.php?action=query&titles=" + urllib.parse.quote(title) + "&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json"
            req2 = urllib.request.Request(info_url, headers={'User-Agent': 'FruitFarmPhuQuoc/1.0'})
            res2 = json.loads(urllib.request.urlopen(req2, timeout=10).read().decode('utf-8'))
            pages = res2.get('query', {}).get('pages', {})
            for _, pv in pages.items():
                ii = pv.get('imageinfo', [])
                if ii:
                    return ii[0].get('thumburl') or ii[0].get('url')
    except Exception as e:
        print("Error for", search_term, ":", e)
    return None

terms = [
    ('cashew', 'roasted cashew nuts'),
    ('macadamia', 'Macadamia integrifolia nuts'),
    ('dried_mango', 'dried mango slices'),
    ('longan', 'Dimocarpus longan fruit'),
    ('hibiscus', 'Hibiscus sabdariffa dried calyces'),
    ('ginger', 'crystallized candied ginger'),
    ('mango_syrup', 'mango puree juice glass')
]

for name, term in terms:
    photo_url = get_wikimedia_photo(term)
    print(name, "->", photo_url)
