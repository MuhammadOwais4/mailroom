from pathlib import Path

from mailroom.subscribers import count_subscribers

DATA = Path(__file__).parent.parent / "data" / "subscribers.csv"


def test_total_is_24():
    assert count_subscribers(DATA)["total"] == 24


def test_tea_curious_is_8():
    assert count_subscribers(DATA)["groups"]["tea-curious"] == 8


def test_daily_drinkers_is_8():
    assert count_subscribers(DATA)["groups"]["daily-drinkers"] == 8


def test_gift_buyers_is_8():
    assert count_subscribers(DATA)["groups"]["gift-buyers"] == 8
