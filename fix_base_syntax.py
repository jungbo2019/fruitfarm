import os

path = r"E:\fruitfarm\templates\base.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the dangling closing bracket with proper DOMContentLoaded
old_block = """            updateCartUI();
            applyGuideModeUI();
        });"""

new_block = """        document.addEventListener('DOMContentLoaded', function() {
            updateCartUI();
            if (typeof applyGuideModeUI === 'function') {
                applyGuideModeUI();
            }
        });"""

content_norm = content.replace("\r\n", "\n")
old_block_norm = old_block.replace("\r\n", "\n")
new_block_norm = new_block.replace("\r\n", "\n")

if old_block_norm in content_norm:
    content_norm = content_norm.replace(old_block_norm, new_block_norm)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content_norm)
    print("SUCCESSFULLY FIXED base.html JS SYNTAX ERROR!")
else:
    print("Target block not found, printing lines 550-565:")
    lines = content_norm.split("\n")
    for i, l in enumerate(lines[548:565], 549):
        print(f"{i}: {repr(l)}")
