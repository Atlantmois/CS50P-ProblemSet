import pytest

from jar import Jar


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(4)
    assert jar2.capacity == 4


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
    jar.deposit(3)
    assert jar.size == 3

def test_withdraw():
    jar = Jar(6)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)