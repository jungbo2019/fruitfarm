path = r"E:\fruitfarm\app.py"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# Let's inspect the broken region
target = """@app.route('/admin/products', methods=['GET', 'POST'])
@login_required

@app.route('/api/admin/product/upload-image', methods=['POST'])
@login_required
def admin_product_upload_image():"""

replacement = """@app.route('/api/admin/product/upload-image', methods=['POST'])
@login_required
def admin_product_upload_image():"""

if target in code:
    # First remove the misplaced decorators
    code = code.replace(target, replacement)
    # Then ensure @app.route('/admin/products') is right above def admin_products():
    code = code.replace("def admin_products():", "@app.route('/admin/products', methods=['GET', 'POST'])\n@login_required\ndef admin_products():")
    with open(path, "w", encoding="utf-8") as f:
        f.write(code)
    print("SUCCESS: Fixed decorators in app.py!")
else:
    print("Target not found, checking with regex")
    import re
    pattern = r"@app\.route\('/admin/products'[\s\S]*?def admin_product_upload_image\(\):"
    m = re.search(pattern, code)
    if m:
        print("Found matching regex pattern:", m.group(0))
