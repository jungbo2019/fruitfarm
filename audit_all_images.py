import os
from PIL import Image

files = [
    'gold_mango_180.jpg',
    'gold_mango_400.jpg',
    'passionfruit.jpg',
    'cashew.jpg',
    'longan.jpg',
    'dragonfruit.jpg',
    'papaya.jpg',
    'macadamia.jpg',
    'coconut_chips.jpg',
    'hibiscus.jpg',
    'ginger.jpg',
    'mango_syrup.jpg',
    'passion_syrup.jpg',
    'promo_10_2.jpg',
    'promo_400_5_1.jpg',
    'promo_syrup_set.jpg'
]

print("Verifying 16 product images:")
for f in files:
    path = os.path.join('static/images/products', f)
    if os.path.exists(path):
        im = Image.open(path)
        print(f"  {f}: size={im.size}, mode={im.mode}")
    else:
        print(f"  MISSING: {f}")
