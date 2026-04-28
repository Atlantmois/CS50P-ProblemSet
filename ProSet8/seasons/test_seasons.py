from datetime import date

from seasons import get_diff

# I'm tired, so I use AI(sorry)
def test_get_diff():
    # Edge case: same day
    assert get_diff(date(2000, 1, 1), date(2000, 1, 1)) == 0

    # Edge case: one day apart
    assert get_diff(date(2000, 1, 1), date(2000, 1, 2)) == 1440

    # Leap year: Feb 28 to Mar 1 has 2 days (leap day adds extra day)
    assert get_diff(date(2000, 2, 28), date(2000, 3, 1)) == 2880

    # Non-leap year: Feb 28 to Mar 1 has 1 day
    assert get_diff(date(1999, 2, 28), date(1999, 3, 1)) == 1440

    # One full year (non-leap, 365 days)
    assert get_diff(date(1999, 1, 1), date(2000, 1, 1)) == 525600

    # One full year (leap, 366 days)
    assert get_diff(date(2000, 1, 1), date(2001, 1, 1)) == 527040

    # Multiple years with leap years
    assert get_diff(date(1995, 1, 1), date(2000, 1, 1)) == 2629440

    # Non-Jan-1 to non-Jan-1 span
    assert get_diff(date(2020, 6, 1), date(2032, 1, 1)) == 6092640
