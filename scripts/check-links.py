from pathlib import Path
from urllib.parse import unquote
import re

root = Path(__file__).resolve().parents[1] / "dist"
html_files = list(root.rglob("*.html"))
internal_links = set()
broken = []

for html_file in html_files:
    text = html_file.read_text(encoding="utf-8", errors="ignore")
    for link in re.findall(r'href=["\'](/[^"\'#?]+)', text):
        internal_links.add(link)
        target = root / unquote(link.lstrip("/"))
        if not target.exists() and not (target / "index.html").exists():
            broken.append((str(html_file.relative_to(root)), link))

print(f"html_files={len(html_files)}")
print(f"internal_links={len(internal_links)}")
print(f"broken={len(broken)}")
for item in broken[:30]:
    print(f"{item[0]} -> {item[1]}")
raise SystemExit(1 if broken else 0)
