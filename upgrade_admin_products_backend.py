with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = """        elif action == 'edit':
            prod_id = request.form.get('product_id')
            price_usd = float(request.form.get('price_usd', 0))
            price_krw = int(request.form.get('price_krw', 0))
            stock = int(request.form.get('stock', 0))
            badge = request.form.get('badge', '').strip()

            cursor.execute('''
                UPDATE products
                SET price_usd = ?, price_krw = ?, stock = ?, badge = ?
                WHERE id = ?
            ''', (price_usd, price_krw, stock, badge, prod_id))
            conn.commit()
            flash('상품 정보가 수정되었습니다.', 'success')"""

replacement = """        elif action == 'edit':
            try:
                prod_id = request.form.get('product_id')
                name = request.form.get('name', '').strip()
                sub_title = request.form.get('sub_title', '').strip()
                description = request.form.get('description', '').strip()

                raw_usd = str(request.form.get('price_usd', 0)).replace(',', '').strip()
                raw_krw = str(request.form.get('price_krw', 0)).replace(',', '').strip()
                raw_stock = str(request.form.get('stock', 0)).replace(',', '').strip()

                price_usd = float(raw_usd) if raw_usd else 0.0
                price_krw = int(float(raw_krw)) if raw_krw else 0
                stock = int(float(raw_stock)) if raw_stock else 0
                badge = request.form.get('badge', '').strip()

                if name:
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
                    ''', (price_usd, price_krw, stock, badge, prod_id))

                conn.commit()
                flash('상품 정보가 성공적으로 수정되었습니다.', 'success')

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    conn.close()
                    return jsonify({'success': True, 'message': '상품 정보가 성공적으로 수정 저장되었습니다!'})
            except Exception as e:
                flash(f'수정 오류 발생: {str(e)}', 'danger')
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    conn.close()
                    return jsonify({'success': False, 'message': str(e)}), 400"""

if target in code:
    code = code.replace(target, replacement)
    with open(r'E:\fruitfarm\app.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Upgraded product edit handler in app.py")
else:
    print("Target not found in app.py")
