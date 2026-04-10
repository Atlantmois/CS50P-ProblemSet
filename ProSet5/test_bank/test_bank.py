from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello, world") == 0
    assert value("HELLO there") == 0


def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20


def test_other():
    assert value("what's up") == 100
    assert value("Good morning") == 100
    assert value("") == 100
