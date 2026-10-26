with open(r'E:\fruitfarm\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "rate = float(get_settings().get('usd_krw_rate', 1380))"
replacement = """cursor.execute("SELECT value FROM settings WHERE key = 'usd_krw_rate'")
    rate_row = cursor.fetchone()
    rate = float(rate_row['value']) if rate_row and rate_row['value'] else 1380.0"""

text = text.replace(target, replacement)

with open(r'E:\fruitfarm\app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed line 1212 in app.py successfully!")
