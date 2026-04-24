from um import count


def test_count_single():
    assert count("Hello, um world") == 1


def test_count_multiple():
    assert count("Um, um, um") == 3


def test_count_case_insensitive():
    assert count("UM um Um") == 3


def test_count_no_um():
    assert count("Hello, world") == 0


def test_count_um_in_larger_word():
    assert count("Yummy") == 0


def test_count_empty():
    assert count("") == 0