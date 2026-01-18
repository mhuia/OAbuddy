import re
import sys
from pathlib import Path


def extract_headers(path):
    headers = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"(#{1,6})\s+", line)
            if m:
                headers.append(len(m.group(1)))
    return headers


readme_en = Path("README.md")
readme_zh = Path("README_zh.md")

if not readme_en.exists() or not readme_zh.exists():
    print("❌ README.md or README_zh.md not found")
    sys.exit(1)

h_en = extract_headers(readme_en)
h_zh = extract_headers(readme_zh)

if h_en != h_zh:
    print("❌ README structure mismatch!")
    print("EN:", h_en)
    print("ZH:", h_zh)
    sys.exit(1)

print("✅ README structure is consistent")
