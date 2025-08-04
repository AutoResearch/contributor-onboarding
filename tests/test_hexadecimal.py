from src.utils import return_hexadecimal
def test_hexadecimal():
    a = 2
    b = 3

    assert return_hexadecimal(a) == hex(a)
