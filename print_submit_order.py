import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'E:\fruitfarm\broken_script_2.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function submitFinalOrder')
print(text[idx:idx+1500])
