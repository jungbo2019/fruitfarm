with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("SELECT id, name, category, stock_quantity, weight_g, barcode\n        FROM products\n        WHERE stock_quantity < 25\n        ORDER BY stock_quantity ASC",
                    "SELECT id, name, category, stock, weight_g, barcode\n        FROM products\n        WHERE stock < 25\n        ORDER BY stock ASC")

text = text.replace("stock_quantity < 25", "stock < 25")
text = text.replace("ORDER BY stock_quantity ASC", "ORDER BY stock ASC")
text = text.replace("category, stock_quantity", "category, stock")

with open(r'E:\fruitfarm\app.py', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'E:\fruitfarm\templates\admin\operations.html', 'r', encoding='utf-8') as f:
    op_text = f.read()

op_text = op_text.replace("item.stock_quantity", "item.stock")

with open(r'E:\fruitfarm\templates\admin\operations.html', 'w', encoding='utf-8') as f:
    f.write(op_text)

print("Fixed stock column name in app.py and operations.html!")
