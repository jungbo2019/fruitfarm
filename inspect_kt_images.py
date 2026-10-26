import os
from PIL import Image

for i in range(14):
    suffix = f"_{i:02d}" if i > 0 else ""
    fname = f"static/images/KakaoTalk_20261011_114455074{suffix}.jpg"
    if os.path.exists(fname):
        im = Image.open(fname)
        print(f"{fname}: {im.size}, mode={im.mode}")
