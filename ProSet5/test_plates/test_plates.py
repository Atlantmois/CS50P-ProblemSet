from plates import is_valid


def test_start():
    assert is_valid("CS")
    assert not is_valid("11CS")
    assert not is_valid("123456")


def test_len():
    assert is_valid("CS5050")
    assert not is_valid("C")
    assert not is_valid("CS12345")


def test_location():
    assert not is_valid("AA222A")
    assert not is_valid("CS0111")


def test_punc():
    assert not is_valid("CS,.22")
    assert not is_valid("CS50!?")