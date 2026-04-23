from numb3rs import validate


def test_num():
    assert validate("123.55.11.1")
    assert not validate("dad.mom.aha.bye")
    assert not validate("111.aha.11.11")


def test_digit():
    assert not validate("22222.33333.44444")
    assert not validate(".2.3.")
    assert not validate("2.2.2.2.2.2.2.2.2")


def test_range():
    assert validate("255.255.255.255")
    assert not validate("275.3.6.28")
    assert not validate("11.11.11.275")

def test_dot():
    assert not validate("255")
