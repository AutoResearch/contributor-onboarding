from utils import return_hexadecimal
def test_hex():
    a = 14

    result = '0xe'

    assert return_hexadecimal(a) == result
