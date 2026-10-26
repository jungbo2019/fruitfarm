import urllib.request
import json
import urllib.parse

def find_titles(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=opensearch&search=File:{urllib.parse.quote(query)}&limit=10&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'FruitFarmStoreBot/2.0 (contact@fruitfarm.example)'})
    with urllib.request.urlopen(req, timeout=10) as r:
        data = json.loads(r.read().decode('utf-8'))
        return data[1]

for q in ["Passion fruit", "Cashew nut", "Longan", "Coconut chips", "Hibiscus tea"]:
    res = find_titles(q)
    print(f"Query '{q}':")
    for item in res[:4]:
        print(f"  {item}")
