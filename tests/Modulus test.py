import unittest




from src.utils import modulo


def test_modulo():
    a = 7
    b = 3

    assert modulo(a, b) == 1