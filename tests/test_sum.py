from utils import sum

def test_sum():
    a = 3
    b = 4
    c = -12
    d = 17.34

    assert sum(a, b) == 7
    assert sum(a, c) == -9
    assert sum(a, d) == 20.34