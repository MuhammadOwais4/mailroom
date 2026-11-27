import csv
import sys
from collections import Counter
from datetime import date, timedelta


def read_subscribers(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_total(path):
    return len(read_subscribers(path))


def count_by_group(path):
    return dict(Counter(row["group"] for row in read_subscribers(path)))


def first_monday_of_next_month(run_date):
    day = date.fromisoformat(run_date)
    if day.month == 12:
        first = date(day.year + 1, 1, 1)
    else:
        first = date(day.year, day.month + 1, 1)
    while first.weekday() != 0:
        first = first + timedelta(days=1)
    return first.isoformat()


def main(args):
    if args == ["subscribers"]:
        path = "data/subscribers.csv"
        print(f"Total: {count_total(path)}")
        for group, count in sorted(count_by_group(path).items()):
            print(f"{group}: {count}")
    else:
        print("Usage: uv run mailroom.py subscribers")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
