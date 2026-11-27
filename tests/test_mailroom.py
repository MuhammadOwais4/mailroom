from mailroom import count_total, count_by_group, first_monday_of_next_month

DATA = "data/subscribers.csv"


def test_total_is_24():
    assert count_total(DATA) == 24


def test_tea_curious_is_8():
    assert count_by_group(DATA)["tea-curious"] == 8


def test_daily_drinkers_is_8():
    assert count_by_group(DATA)["daily-drinkers"] == 8


def test_gift_buyers_is_8():
    assert count_by_group(DATA)["gift-buyers"] == 8


def test_first_monday_after_2026_11_20_is_2026_12_07():
    assert first_monday_of_next_month("2026-11-20") == "2026-12-07"


def test_first_monday_after_2026_12_31_is_2027_01_04():
    assert first_monday_of_next_month("2026-12-31") == "2027-01-04"
