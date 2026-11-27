from mailroom import count_total, count_by_group, first_monday_of_next_month

DATA = "data/subscribers.csv"

assert count_total(DATA) == 24

groups = count_by_group(DATA)
assert groups["tea-curious"] == 8
assert groups["daily-drinkers"] == 8
assert groups["gift-buyers"] == 8

assert first_monday_of_next_month("2026-11-20") == "2026-12-07"
assert first_monday_of_next_month("2026-12-31") == "2027-01-04"

print("All checks passed.")
