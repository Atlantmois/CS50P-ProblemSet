import pytest
from working import convert


def test_convert_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:30 PM to 12:30 AM") == "12:30 to 00:30"
    assert convert("4:30 PM to 11:45 AM") == "16:30 to 11:45"


def test_convert_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")