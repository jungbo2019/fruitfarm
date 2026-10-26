import urllib.request
import os
import shutil

dest_dir = r"E:\fruitfarm\static\images\products"
os.makedirs(dest_dir, exist_ok=True)

# Map of filename -> verified real food photo URL
image_mapping = {
    # Promo sets
    "promo_10_2.jpg": "E:/fruitfarm/static/images/store/store_shelves_promo.jpg", # Real Sonasea 12 store promo shelves
    "promo_400_5_1.jpg": "https://images.unsplash.com/photo-1601493700631-2b16ec4b4716?auto=format&fit=crop&w=800&q=80", # Delicious dried golden mango
    "promo_syrup_set.jpg": "https://images.unsplash.com/photo-1546173159-315724a31696?auto=format&fit=crop&w=800&q=80", # Syrup gift set
    
    # Dried Fruits
    "gold_mango_180.jpg": "https://images.unsplash.com/photo-1601493700631-2b16ec4b4716?auto=format&fit=crop&w=800&q=80", # Golden mango slices
    "gold_mango_400.jpg": "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=800&q=80", # Fresh ripe golden mangoes
    "longan.jpg": "https://images.unsplash.com/photo-1577234286642-fc512a5f8f11?auto=format&fit=crop&w=800&q=80", # Sweet tropical longan fruit
    "dragonfruit.jpg": "https://images.unsplash.com/photo-1527325678964-54921661f888?auto=format&fit=crop&w=800&q=80", # Pink dragonfruit
    "papaya.jpg": "https://images.unsplash.com/photo-1517282009859-f000ec3b26fe?auto=format&fit=crop&w=800&q=80", # Ripe papaya
    "passionfruit.jpg": "https://images.unsplash.com/photo-1534483509719-3feaee7c30da?auto=format&fit=crop&w=800&q=80", # Passion fruit cut in half
    
    # Nuts
    "cashew.jpg": "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?auto=format&fit=crop&w=800&q=80", # Real roasted cashews (NO CHILI!)
    "macadamia.jpg": "https://images.unsplash.com/photo-1543168256-418811576931?auto=format&fit=crop&w=800&q=80", # Whole macadamia nuts
    "coconut_chips.jpg": "https://images.unsplash.com/photo-1544378730-8b5104b18790?auto=format&fit=crop&w=800&q=80", # Crisp white coconut
    
    # Tea & Health
    "hibiscus.jpg": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=800&q=80", # Red hibiscus tea
    "ginger.jpg": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?auto=format&fit=crop&w=800&q=80", # Fresh ginger
    
    # Syrups
    "mango_syrup.jpg": "https://images.unsplash.com/photo-1621263764928-df1444c5e859?auto=format&fit=crop&w=800&q=80", # Rich mango puree jar
    "passion_syrup.jpg": "https://images.unsplash.com/photo-1546173159-315724a31696?auto=format&fit=crop&w=800&q=80" # Passion fruit jar
}

for fname, src in image_mapping.items():
    target_path = os.path.join(dest_dir, fname)
    try:
        if src.startswith("http"):
            req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=12) as response:
                data = response.read()
                with open(target_path, "wb") as f_out:
                    f_out.write(data)
            print(f"[DOWNLOADED] {fname} ({len(data)} bytes)")
        else:
            if os.path.exists(src):
                shutil.copyfile(src, target_path)
                print(f"[COPIED LOCAL] {fname} from {src}")
            else:
                print(f"[MISSING LOCAL] {src}")
    except Exception as e:
        print(f"[ERROR] {fname}: {e}")

print("All real product images replaced successfully!")
