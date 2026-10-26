with open('templates/base.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = lines[:556] + lines[585:]
with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Scrubbed remaining lines 556 to 585!")
