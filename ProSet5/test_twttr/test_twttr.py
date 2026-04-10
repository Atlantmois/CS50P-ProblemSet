from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"


def test_mixed():
    assert shorten("HEllo") == "Hll"
    assert shorten("twItTeR") == "twtTR"


def test_punc():
    assert shorten("Hello, 'sir'!") == "Hll, 'sr'!"


def test_number():
    assert shorten("12345") == "12345"
    assert shorten("aibcde123") == "bcd123"


def test_void():
    assert shorten("") == ""
    