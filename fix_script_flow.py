with open('E:/fruitfarm/templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c_norm = c.replace('\r\n', '\n')

old_part = '''    // Curated Human-Eye Tab Navigation Logic'''
idx = c_norm.find(old_part)
if idx != -1:
    end_idx = c_norm.find('</script>', idx)
    if end_idx != -1:
        new_script = '''    // Natural Full Page Flow (All sections accessible by scrolling)
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('section[data-tab]').forEach(sec => {
            sec.style.display = 'block';
            sec.classList.remove('hidden');
        });
    });'''
        c_norm = c_norm[:idx] + new_script + c_norm[end_idx:]
        print("Replaced script successfully!")

with open('E:/fruitfarm/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)
