import re
import sys
from pathlib import Path

HEADER_RE = re.compile(r"^(#{1,6})\s+")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?(\s*:?-+:?\s*\|)+\s*$")


def parse_headers(path):
    headers = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        m = HEADER_RE.match(line)
        if m:
            headers.append(len(m.group(1)))

    return headers, lines


def extract_tables(lines):
    tables = []
    i = 0
    n = len(lines)

    while i < n - 1:
        if "|" in lines[i] and TABLE_SEPARATOR_RE.match(lines[i + 1]):
            # Table seperator
            data_rows = 0
            j = i + 2
            while j < n and "|" in lines[j]:
                if lines[j].strip() != "":
                    data_rows += 1
                j += 1

            tables.append(data_rows)
            i = j
        else:
            i += 1

    return tables


readme_en = Path("README.md")
readme_zh = Path("README_zh.md")

if not readme_en.exists() or not readme_zh.exists():
    print("❌ README files missing")
    sys.exit(1)

# Check levels of title
h_en, lines_en = parse_headers(readme_en)
h_zh, lines_zh = parse_headers(readme_zh)

if h_en != h_zh:
    print("❌ Heading level structure mismatch")
    print("EN:", h_en)
    print("ZH:", h_zh)
    sys.exit(1)

# Check lines of table
tables_en = extract_tables(lines_en)
tables_zh = extract_tables(lines_zh)

if len(tables_en) != len(tables_zh):
    print("❌ Number of tables mismatch")
    print("EN tables:", len(tables_en))
    print("ZH tables:", len(tables_zh))
    sys.exit(1)

for i, (en_rows, zh_rows) in enumerate(zip(tables_en, tables_zh), 1):
    if en_rows != zh_rows:
        print(f"❌ Table {i} row count mismatch")
        print(f"   EN rows: {en_rows}")
        print(f"   ZH rows: {zh_rows}")
        sys.exit(1)

print("✅ README headings and table row counts are consistent")
