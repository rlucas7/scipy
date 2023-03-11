import numpy as np
import pytest
from numpy.testing import assert_array_equal
from math import comb
from random import randrange
from scipy.special import stirling2


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
def test_triangle_exact(n, k, expected):
    assert stirling2(n, k, exact=True) == expected


@pytest.mark.parametrize('n,expected', [
    (0, [1]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (3, [0, 1, 3, 1]),
    (4, [0, 1, 7, 6, 1]),
    (5, [0, 1, 15, 25, 10, 1]),
    (6, [0, 1, 31, 90, 65, 15, 1]),
    (7, [0, 1, 63, 301, 350, 140, 21, 1]),
    (8, [0, 1, 127, 966, 1701, 1050, 266, 28, 1]),
    (9, [0, 1, 255, 3025, 7770, 6951, 2646, 462, 36, 1]),
    (10, [0, 1, 511, 9330, 34105, 42525, 22827, 5880, 750, 45, 1]),
])
def test_triangle_inexact(n, expected):
    """Test full triangle of values for 0 <= n <= 10

    Values taken from Wikipedia
    https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
    """
    assert_array_equal(stirling2(n, np.arange(0, n + 1), exact=False), expected)


@pytest.mark.parametrize('n', [101, 199, 401, 797, 1601, 3217])
@pytest.mark.parametrize('k', [19, 41, 59, 79, 101])
def test_modulus(n, k):
    # uses theorem 2.1 from: http://www.oyeat.com/papers/stirling_final.pdf
    assert stirling2(n, k) % 2 == comb(n - (k//2) - 1, n - k) % 2
