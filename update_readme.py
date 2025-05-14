import os

# Klasör ve dosya yolları
ICON_DIR = "iconset"
README_PATH = "README.md"

# Markdown tablosu için satırları hazırla
index_lines = [
    "## 🧾 Icon Index",
    "| Icon | Filename |",
    "|------|----------|"
]

for icon_file in sorted(os.listdir(ICON_DIR)):
    if icon_file.endswith(".png"):
        line = f"| ![icon]({ICON_DIR}/{icon_file}) | `{icon_file}` |"
        index_lines.append(line)

# README'yi oku
with open(README_PATH, "r") as f:
    lines = f.readlines()

# Marker'lar
start_marker = "<!-- ICON_INDEX_START -->"
end_marker = "<!-- ICON_INDEX_END -->"

try:
    start = lines.index(start_marker + "\n")
    end = lines.index(end_marker + "\n")
except ValueError:
    # Eğer markerlar yoksa ekle
    lines.append("\n" + start_marker + "\n")
    lines.append(end_marker + "\n")
    start = lines.index(start_marker + "\n")
    end = lines.index(end_marker + "\n")

# Yeni bloğu oluştur
new_block = [start_marker + "\n"] + [l + "\n" for l in index_lines] + [end_marker + "\n"]

# README'yi güncelle
updated_lines = lines[:start] + new_block + lines[end+1:]

with open(README_PATH, "w") as f:
    f.writelines(updated_lines)
