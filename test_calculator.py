
from calculator import add


def test_add_positive_numbers():
    assert add(5, 3) == 8


def test_add_negative_numbers():
    assert add(-2, -4) == -6


def test_add_zero():
    assert add(10, 0) == 10
