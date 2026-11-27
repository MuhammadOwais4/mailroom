import csv
from collections import Counter


def count_subscribers(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    groups = Counter(row["group"] for row in rows)
    return {"total": len(rows), "groups": dict(groups)}
