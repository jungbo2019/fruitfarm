with open('templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="competitor"')
if idx == -1:
    idx = text.find('COMPETITOR BENCHMARK')
end_idx = text.find('</table>', idx)

print(text[idx:end_idx+8].encode('ascii', errors='replace').decode('ascii'))
