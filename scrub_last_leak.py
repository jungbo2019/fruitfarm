with open('templates/base.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('alert(`[${d.guide.name}]')
if idx != -1:
    # find enclosing function or script block
    func_start = text.rfind('function', 0, idx)
    func_end = text.find('}', idx)
    text = text[:func_start] + '// guide partner scripts removed\n' + text[func_end+1:]
    print('Removed remaining guide alert script from base.html!')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(text)
