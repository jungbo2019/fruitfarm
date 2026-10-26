import os

path = r"E:\fruitfarm\templates\admin\login.html"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if "푸꾸옥 플래그십 보안 관제 시스템" in line:
        continue
    if "inline-block bg-amber-100" in line:
        continue
    if skip:
        skip = False
        continue
    new_lines.append(line)

# Let's be extra clean: inspect lines
clean_lines = []
for line in lines:
    if "푸꾸옥 플래그십 보안 관제 시스템" in line:
        # also remove the previous line if it was the opening div
        if clean_lines and "inline-block bg-amber-100" in clean_lines[-1]:
            clean_lines.pop()
        continue
    if clean_lines and "푸꾸옥" not in line and line.strip() == "</div>" and len(lines) > 0:
        # check if it closed that badge
        pass
    clean_lines.append(line)

# Let's do regex replacement on full text
full_text = "".join(lines)
import re
# remove the entire div
modified = re.sub(r'\s*<div class="inline-block bg-amber-100[\s\S]*?</div>', '', full_text)

with open(path, "w", encoding="utf-8") as f:
    f.write(modified)

print("Done! Length before:", len(full_text), "after:", len(modified))
