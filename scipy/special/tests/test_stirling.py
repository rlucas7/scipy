import pytest
from math import comb
from numpy import isnan, nan, inf
from scipy.special import stirling2

class TestStirling2:
     @pytest.mark.parametrize('n, k, expected', [
        (-1, 1, 0),
        (1, -1, 0),
        (0, 1, 0),
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
        (1, 2, 0),
        (2, 0, 0),
        (2, 1, 1),
        (2, 2, 1),
        (3, 0, 0),
        (3, 1, 1),
        (3, 2, 3),
        (3, 3, 1),
        (3, 4, 0),
        (4, 0, 0),
        (4, 1, 1),
        (4, 2, 7),
        (4, 3, 6),
        (4, 4, 1),
        (4, 5, 0),
        (5, 0, 0),
        (5, 1, 1),
        (5, 2, 15),
        (5, 3, 25),
        (5, 4, 10),
        (5, 5, 1),
        (5, 6, 0),
        (6, 0, 0),
        (6, 1, 1),
        (6, 2, 31),
        (6, 3, 90),
        (6, 4, 65),
        (6, 5, 15),
        (6, 6, 1),
        (6, 7, 0),
    ])
    def test_triangle(self):
        assert stirling2(n, k) == expected

    @pytest.mark.parametrize('n, k, expected', [
        (nan, 1, nan),
        (1, nan, nan),
        (nan, -1, nan),
        (-1, nan, nan),
    ])
    def test_nans(self):
        assert stirling2(n, k) == expected

    @pytest.mark.parametrize('n, k, expected', [
        (inf, inf, nan),
        (inf, 1, nan),
        (1, inf, 0),
        (inf, -1, nan),
        (-1, inf, 0),
    ])
    def test_infs(self):
        assert stirling2(n, k) == expected

    def test_modulus(self):
        # do not need to fix seed
        n = randrange(7, 12)
        k = randrange(n)
        # uses theorem 2.1 from: http://www.oyeat.com/papers/stirling_final.pdf
        assert stirling2(n, k) % 2 == comb(n - (k//2) - 1, n - k) % 2
