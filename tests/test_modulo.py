from src.utils import modulo

def test_modulo():
    a = 10
    b = 3

    assert modulo(a, b) == a % b

def test_modulo_by_hand():
    a = 30
    b = 7

    result = a - (int(a/b) * b)

    assert modulo(a, b) == result

if __name__ == "__name__":
    test_modulo()
    test_modulo_by_hand()