import re

def find_cart_markup():
    for fpath in [r'E:\fruitfarm\templates\base.html', r'E:\fruitfarm\templates\index.html']:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"=== {fpath} ===")
        # find any tag with id containing 'cart'
        matches = re.findall(r'<[a-zA-Z0-9]+\s+[^>]*?id=[\'"]([^\'"]*cart[^\'"]*)[\'"]', content, re.I)
        print("IDs with 'cart':", set(matches))
        # find modal IDs
        modals = re.findall(r'<[a-zA-Z0-9]+\s+[^>]*?id=[\'"]([^\'"]*modal[^\'"]*)[\'"]', content, re.I)
        print("IDs with 'modal':", set(modals))

if __name__ == '__main__':
    find_cart_markup()
