import re

app_path = r"E:\fruitfarm\app.py"
with open(app_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update admin_products UPDATE query to include image_url
old_query = """                if name:
                    cursor.execute('''
                        UPDATE products
                        SET name = ?, sub_title = ?, description = ?, price_usd = ?, price_krw = ?, stock = ?, badge = ?
                        WHERE id = ?
                    ''', (name, sub_title, description, price_usd, price_krw, stock, badge, prod_id))
                else:
                    cursor.execute('''
                        UPDATE products
                        SET price_usd = ?, price_krw = ?, stock = ?, badge = ?
                        WHERE id = ?
                    ''', (price_usd, price_krw, stock, badge, prod_id))"""

new_query = """                image_url = request.form.get('image_url', '').strip()
                if image_url:
                    cursor.execute('''
                        UPDATE products
                        SET name = ?, sub_title = ?, description = ?, price_usd = ?, price_krw = ?, stock = ?, badge = ?, image_url = ?
                        WHERE id = ?
                    ''', (name, sub_title, description, price_usd, price_krw, stock, badge, image_url, prod_id))
                elif name:
                    cursor.execute('''
                        UPDATE products
                        SET name = ?, sub_title = ?, description = ?, price_usd = ?, price_krw = ?, stock = ?, badge = ?
                        WHERE id = ?
                    ''', (name, sub_title, description, price_usd, price_krw, stock, badge, prod_id))
                else:
                    cursor.execute('''
                        UPDATE products
                        SET price_usd = ?, price_krw = ?, stock = ?, badge = ?
                        WHERE id = ?
                    ''', (price_usd, price_krw, stock, badge, prod_id))"""

if old_query in code:
    code = code.replace(old_query, new_query)
    print("1. Updated admin_products SQL query with image_url!")
else:
    print("WARNING: old_query not found verbatim in app.py!")

# 2. Add /api/admin/product/upload-image route
upload_route = """
@app.route('/api/admin/product/upload-image', methods=['POST'])
@login_required
def admin_product_upload_image():
    try:
        prod_id = request.form.get('product_id')
        file = request.files.get('image_file')
        if not file or not file.filename:
            return jsonify({'success': False, 'message': '업로드할 이미지 파일을 선택해주세요.'}), 400

        ext = file.filename.rsplit('.', 1)[-1].lower() if '.' in file.filename else 'jpg'
        if ext not in ['jpg', 'jpeg', 'png', 'webp', 'gif']:
            return jsonify({'success': False, 'message': '지원되지 않는 이미지 포맷입니다. (jpg, png, webp 가능)'}), 400

        filename = f"prod_{prod_id}_{int(time.time())}.{ext}"
        upload_folder = os.path.join(app.root_path, 'static', 'images', 'products')
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        new_image_url = f"/static/images/products/{filename}"

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET image_url = ? WHERE id = ?", (new_image_url, prod_id))
        conn.commit()
        conn.close()

        log_event('PRODUCT_IMG', f"관리자 상품 ID {prod_id} 사진 교체 완료: {new_image_url}")
        return jsonify({'success': True, 'message': '상품 사진이 성공적으로 교체되었습니다.', 'image_url': new_image_url})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
"""

if "/api/admin/product/upload-image" not in code:
    code = code.replace("def admin_products():", upload_route + "\ndef admin_products():")
    print("2. Added /api/admin/product/upload-image endpoint!")

with open(app_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Backend update complete!")
