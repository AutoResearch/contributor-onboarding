
from utils import sum


def test_sum():
    for a in range(10):
        for b in range(10):
            assert sum(a,b) == a+b


