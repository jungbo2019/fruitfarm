with open(r'E:\fruitfarm\templates\base.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in base.html: {len(lines)}")

# Let's find script tags in base.html
in_script = False
script_lines = []
for i, line in enumerate(lines):
    if '<script' in line:
        in_script = True
    if in_script:
        script_lines.append((i + 1, line))
    if '</script>' in line:
        in_script = False

print(f"Total script lines: {len(script_lines)}")

# Let's write script lines to a file and check JS syntax with node or python
with open(r'E:\fruitfarm\check_script_syntax.js', 'w', encoding='utf-8') as f:
    for num, line in script_lines:
        if '<script' in line or '</script>' in line:
            f.write(f"// LINE {num}: {line}\n")
        else:
            f.write(line)

print("Saved script to check_script_syntax.js")
